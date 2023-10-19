# Selection token used to indicate the selection cursor in a list
DEFAULT_SELECTED_POINTER = "☞"

# Item prefix to identify selected items in a checkbox list
INDICATOR_SELECTED = "●"

# Item prefix to identify unselected items in a checkbox list
INDICATOR_UNSELECTED = "○"

# Prefix displayed in front of questions
DEFAULT_QUESTION_PREFIX = "✍️"

# Default message style
DEFAULT_STYLE = [
    ("qmark", "fg:#E91E63 bold"),  # token in front of the question
    ("question", "fg:#FF9D00 bold"),  # question text
    ("answer", "fg:#5F819D"),  # submitted answer text behind the question
    ("pointer", "fg:#2196f3 bold"),  # pointer used in select and checkbox prompts
    ("selected", "fg:#FFFFFF bg:#CC5454 bold italic"),  # style for a selected item of a checkbox
    ("separator", "fg:#6C6C6C"),  # separator in lists
    ("instruction", "fg:#F44336"),  # user instructions for select, rawselect, checkbox
    ("text", "fg:#FBE9E7"),  # any other text
    ("highlighted", "fg:#673AB7 bold italic"),
    ("disabled", "fg:#858585 italic"),
]
