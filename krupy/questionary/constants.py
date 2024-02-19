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
        ("qcount", "fg:#801336 bold italic"),  # question count down
        ("qmark", "fg:#C81912 bold italic"),  # question mark
        ("question", "fg:#CC561E bold"),  # question text
        ("type", "fg:#3E7063 bold italic"),  # question type
        ("default", "fg:#0F4C75 bold italic blink"),  # question default value
        ("answer", "fg:#004E32"),  # submitted answer text behind the question
        ("pointer", "fg:#05478A bold"),  # pointer used in select and checkbox prompts
        ("instruction", "fg:#673AB7 bold"),  # user instructions for select, rawselect, checkbox
        ("text", "fg:default bold"),  # any other text
        ("selected", "fg:#87a330 bg:default noreverse bold italic"),  # style for a selected item of a checkbox
        ("highlighted", "fg:#cc3399 bold"),  # any other hight light text
        ("separator", "fg:#6C6C6C"),  # separator in lists
        ("disabled", "fg:#858585"),  # any other disable text
    ]
)
