"""krupy CLI entrypoint."""
from .cli import krupyApp

krupy_app_run = krupyApp.run
if __name__ == "__main__":
    krupy_app_run()
