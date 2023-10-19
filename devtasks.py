"""Development helper tasks."""
import logging
import shutil
from pathlib import Path

from plumbum import local

_logger = logging.getLogger(__name__)
HERE = Path(__file__).parent


def clean():
    """Clean build, test or other process artifacts from the project workspace."""
    build_artefacts = (
        "build/",
        "dist/",
        "*.egg-info",
        "pip-wheel-metadata",
    )
    python_artefacts = (
        ".pytest_cache",
        "htmlcov",
        ".coverage",
        "**/__pycache__",
        "**/*.pyc",
        "**/*.pyo",
    )
    project_dir = Path(".").resolve()
    for pattern in build_artefacts + python_artefacts:
        for matching_path in project_dir.glob(pattern):
            print(f"Deleting {matching_path}")
            if matching_path.is_dir():
                shutil.rmtree(matching_path)
            else:
                matching_path.unlink()


def dev_setup():
    """Set up a development environment."""
    with local.cwd(HERE):
        local["direnv"]("allow")
        local["poetry"]("install")
