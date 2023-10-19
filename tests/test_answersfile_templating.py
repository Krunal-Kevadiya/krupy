from pathlib import Path
from typing import Optional

import pytest

import krupy
from krupy.user_data import load_answersfile_data

from .helpers import build_file_tree


@pytest.fixture(scope="module")
def template_path(tmp_path_factory: pytest.TempPathFactory) -> str:
    root = tmp_path_factory.mktemp("template")
    build_file_tree(
        {
            root
            / "{{ _krupy_conf.answers_file }}.jinja": """\
                # Changes here will be overwritten by Krupy
                {{ _krupy_answers|to_nice_yaml }}
                """,
            root
            / "krupy.yml": """\
                _answers_file: ".krupy-answers-{{ module_name }}.yml"

                module_name:
                    type: str
                """,
        }
    )
    return str(root)


@pytest.mark.parametrize("answers_file", [None, ".changed-by-user.yml"])
def test_answersfile_templating(
    template_path: str, tmp_path: Path, answers_file: Optional[str]
) -> None:
    """
    Test krupy behaves properly when _answers_file contains a template

    Checks that template is resolved successfully and that a subsequent
    copy that resolves to a different answers file doesn't clobber the
    old answers file.
    """
    krupy.run_copy(
        template_path,
        tmp_path,
        {"module_name": "mymodule"},
        answers_file=answers_file,
        defaults=True,
        overwrite=True,
        unsafe=True,
    )
    first_answers_file = (
        ".krupy-answers-mymodule.yml"
        if answers_file is None
        else ".changed-by-user.yml"
    )
    assert (tmp_path / first_answers_file).exists()
    answers = load_answersfile_data(tmp_path, first_answers_file)
    assert answers["module_name"] == "mymodule"

    krupy.run_copy(
        template_path,
        tmp_path,
        {"module_name": "anothermodule"},
        defaults=True,
        overwrite=True,
        unsafe=True,
    )

    # Assert second one created
    second_answers_file = ".krupy-answers-anothermodule.yml"
    assert (tmp_path / second_answers_file).exists()
    answers = load_answersfile_data(tmp_path, second_answers_file)
    assert answers["module_name"] == "anothermodule"

    # Assert first one still exists
    assert (tmp_path / first_answers_file).exists()
    answers = load_answersfile_data(tmp_path, first_answers_file)
    assert answers["module_name"] == "mymodule"
