import warnings
from pathlib import Path

import pytest
from packaging.version import Version
from plumbum import local
from plumbum.cmd import git

import krupy
from krupy.errors import (
    OldTemplateWarning,
    UnknownKrupyVersionWarning,
    UnsupportedVersionError,
)

from .helpers import build_file_tree


@pytest.fixture(scope="module")
def template_path(tmp_path_factory: pytest.TempPathFactory) -> str:
    root = tmp_path_factory.mktemp("template")
    build_file_tree(
        {
            (root / "krupy.yaml"): (
                """\
                _min_krupy_version: "10.5.1"
                """
            ),
            (root / "README.md"): "",
        }
    )
    return str(root)


def test_version_less_than_required(
    template_path: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("krupy.__version__", "0.0.0a0")
    with pytest.raises(UnsupportedVersionError):
        krupy.run_copy(template_path, tmp_path)


def test_version_equal_required(
    template_path: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("krupy.__version__", "10.5.1")
    # assert no error
    krupy.run_copy(template_path, tmp_path)


def test_version_greater_than_required(
    template_path: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("krupy.__version__", "99.99.99")
    # assert no error
    krupy.run_copy(template_path, tmp_path)


def test_minimum_version_update(
    template_path: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("krupy.__version__", "11.0.0")
    krupy.run_copy(template_path, tmp_path)

    with local.cwd(tmp_path):
        git("init")
        git("config", "user.name", "Krupy Test")
        git("config", "user.email", "test@krupy")
        git("add", ".")
        git("commit", "-m", "hello world")

    monkeypatch.setattr("krupy.__version__", "0.0.0.post0")
    with pytest.raises(UnsupportedVersionError):
        krupy.run_copy(template_path, tmp_path)

    monkeypatch.setattr("krupy.__version__", "10.5.1")
    # assert no error
    krupy.run_copy(template_path, tmp_path)

    monkeypatch.setattr("krupy.__version__", "99.99.99")
    # assert no error
    krupy.run_copy(template_path, tmp_path)


def test_version_0_0_0_ignored(
    template_path: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("krupy.template.krupy_version", lambda: Version("0.0.0"))
    # assert no error
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        with pytest.raises(UnknownKrupyVersionWarning):
            krupy.run_copy(template_path, tmp_path)


def test_version_bigger_major_warning(
    template_path: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("krupy.__version__", "11.0.0a0")
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        with pytest.raises(OldTemplateWarning):
            krupy.run_copy(template_path, tmp_path)
