from prompt_toolkit.output import DummyOutput

# from tests.questionary.utils import KeyInputs
from tests.questionary.utils import execute_with_input_pipe


def ask_with_patched_input(q, text):
    def run(inp):
        inp.send_text(text)
        return q(input=inp, output=DummyOutput())

    return execute_with_input_pipe(run)