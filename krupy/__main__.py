"""Krupy CLI entrypoint."""
from .cli import KrupyApp

# HACK https://github.com/nix-community/poetry2nix/issues/504
krupy_app_run = KrupyApp.run
if __name__ == "__main__":
    krupy_app_run()
