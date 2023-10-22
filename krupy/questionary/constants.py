from . import Style

# Value to display as an answer when "affirming" a confirmation question
YES = "Yes"

# Value to display as an answer when "denying" a confirmation question
NO = "No"

# Instruction text for a confirmation question (yes is default)
YES_OR_NO = "(Y/n)"

# Instruction text for a confirmation question (no is default)
NO_OR_YES = "(y/N)"

# Instruction for multiline input
INSTRUCTION_MULTILINE = "(Finish with 'Alt+Enter' or 'Esc then Enter')\n>"

# Selection token used to indicate the selection cursor in a list
DEFAULT_SELECTED_POINTER = "»"  # "☞"

# Item prefix to identify selected items in a checkbox list
INDICATOR_SELECTED = "●"

# Item prefix to identify unselected items in a checkbox list
INDICATOR_UNSELECTED = "○"

# Prefix displayed in front of questions
DEFAULT_QUESTION_PREFIX = "?"  # "✍️"

# Message shown when a user aborts a question prompt using CTRL-C
DEFAULT_KBI_MESSAGE = "Cancelled by user"

# Default text shown when the input is invalid
INVALID_INPUT = "Invalid input"

# Default message style
DEFAULT_STYLE = Style(
    [
        ("qmark", "fg:#E91E63 bold"),  # token in front of the question
        ("question", "fg:#FF9D00 bold"),  # question text
        ("answer", "fg:#5F819D"),  # submitted answer text behind the question
        ("pointer", "fg:#2196f3 bold"),  # pointer used in select and checkbox prompts
        (
            "selected",
            "fg:#FFFFFF bg:#CC5454 bold italic",
        ),  # style for a selected item of a checkbox
        ("separator", "fg:#6C6C6C"),  # separator in lists
        (
            "instruction",
            "fg:#F44336 bold italic",
        ),  # user instructions for select, rawselect, checkbox
        ("text", "fg:#000000 bold"),  # any other text
        ("highlighted", "fg:#673AB7 bold italic"),
        ("disabled", "fg:#858585 bold italic"),
        ("qcount", "#C61D56 bold"),
        ("type", "#C61D56 bold"),
        ("default", "#2196f3 bold"),
    ]
)
