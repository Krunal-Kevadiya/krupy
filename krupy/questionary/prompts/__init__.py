from ..prompts import autocomplete
from ..prompts import checkbox
from ..prompts import confirm
from ..prompts import password
from ..prompts import path
from ..prompts import press_any_key_to_continue
from ..prompts import rawselect
from ..prompts import select
from ..prompts import text

AVAILABLE_PROMPTS = {
    "autocomplete": autocomplete.autocomplete,
    "confirm": confirm.confirm,
    "text": text.text,
    "select": select.select,
    "rawselect": rawselect.rawselect,
    "password": password.password,
    "checkbox": checkbox.checkbox,
    "path": path.path,
    "press_any_key_to_continue": press_any_key_to_continue.press_any_key_to_continue,
    # backwards compatible names
    "list": select.select,
    "rawlist": rawselect.rawselect,
    "input": text.text,
}


def prompt_by_name(name):
    return AVAILABLE_PROMPTS.get(name)
