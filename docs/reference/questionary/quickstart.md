# Quick Start

Questionary supports two different concepts:

- creating a **single question** for the user

```python3
  questionary.password("What's your secret?").ask()
```

- creating a **form with multiple questions** asked one after another

```python3
  answers = questionary.form(
    first = questionary.confirm("Would you like the next question?", default=True),
    second = questionary.select("Select item", choices=["item1", "item2", "item3"])
  ).ask()
```

# Asking a Single Question

Questionary ships with a lot of different [Question Types](../question_types) to provide
the right prompt for the right question. All of them work in the same way though.
Firstly, you create a question:

```python3
  import questionary

  question = questionary.text("What's your first name")
```

and secondly, you need to prompt the user to answer it:

```python3
  answer = question.ask()
```

Since our question is a `text` prompt, `answer` will
contain the text the user typed after they submitted it.

You can concatenate creating and asking the question in a single
line if you like, e.g.

```python3
  import questionary

  answer = questionary.text("What's your first name").ask()
```

!!! note

    There are a lot more question types apart from `text`.
    For a description of the different question types, head
    over to the [Question Types](../question_types).

# Asking Multiple Questions

You can use the [form()](../form) function to ask a collection
of [Questions <questionary.Question>](). The questions will be asked in
the order they are passed to [form()]().

```python3

  import questionary

  answers = questionary.form(
    first = questionary.confirm("Would you like the next question?", default=True),
    second = questionary.select("Select item", choices=["item1", "item2", "item3"])
  ).ask()

  print(answers)
```

The printed output will have the following format:

```python3

{'first': True, 'second': 'item2'}
```

The [prompt()]() function also allows you to ask a
collection of questions, however instead of taking [Question]()
instances, it takes a dictionary:

```python3

  import questionary

  questions = [
    {
      "type": "confirm",
      "name": "first",
      "message": "Would you like the next question?",
      "default": True,
    },
    {
      "type": "select",
      "name": "second",
      "message": "Select item",
      "choices": ["item1", "item2", "item3"],
    },
  ]

  questionary.prompt(questions)
```

The format of the returned answers is the same as the one for
[form()](). You can find more details on the configuration
dictionaries in [Create Questions from Dictionaries](../advanced).
