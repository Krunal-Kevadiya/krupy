# Krupy

![Python](https://img.shields.io/pypi/pyversions/krupy?logo=python&logoColor=%23959DA5)
[![PyPI](https://img.shields.io/pypi/v/krupy?logo=pypi&logoColor=%23959DA5)](https://pypi.org/project/krupy/)

A library and CLI app for rendering project templates.

-   Works with **local** paths and **Git URLs**.
-   Your project can include any file and Krupy can dynamically replace values in any kind of text file.
-   It generates a beautiful output and takes care of not overwriting existing files unless instructed to do so.

## Installation

1. Install Python 3.8 or newer.
1. Install Git 2.27 or newer.
1. To use as a CLI app: 
    ``

## Quick start

To create a template:

```shell
📁 my_krupy_template                        # your template project
├── 📄 krupy.yml                            # your template configuration
├── 📁 .git/                                 # your template is a Git repository
├── 📁 {{project_name}}                      # a folder with a templated name
│   └── 📄 {{module_name}}.py.jinja          # a file with a templated name
└── 📄 {{_krupy_conf.answers_file}}.jinja   # answers are recorded here
```

```yaml title="krupy.yml"
# questions
project_name:
    type: str
    help: What is your project name?

module_name:
    type: str
    help: What is your Python module name?
```

```python+jinja title="{{project_name}}/{{module_name}}.py.jinja"
print("Hello from {{module_name}}!")
```

```yaml+jinja title="{{_krupy_conf.answers_file}}.jinja"
# Changes here will be overwritten by Krupy
{{ _krupy_answers|to_nice_yaml -}}
```

To generate a project from the template:

-   On the command-line:

    ```shell
    krupy copy path/to/project/template path/to/destination
    ```

-   Or in Python code, programmatically:

    ```python
    from krupy import run_copy

    # Create a project from a local path
    run_copy("path/to/project/template", "path/to/destination")

    # Or from a Git URL.
    run_copy("https://github.com/Krunal-Kevadiya/krupy.git", "path/to/destination")

    # You can also use "gh:" as a shortcut of "https://github.com/"
    run_copy("gh:Krunal-Kevadiya/krupy.git", "path/to/destination")

    # Or "gl:" as a shortcut of "https://gitlab.com/"
    run_copy("gl:Krunal-Kevadiya/krupy.git", "path/to/destination")
    ```

## Basic concepts

Krupy is composed of these main concepts:

1. **Templates**. They lay out how to generate the subproject.
1. **Questionaries**. They are configured in the template. Answers are used to generate projects.
1. **Projects**. This is where your real program lives. But it is usually generated and/or updated from a template.

Krupy targets these main human audiences:

1.  **Template creators**. Programmers that repeat code too much and prefer a tool to do it for them.

    !!! tip

         Krupy doesn't replace the DRY principle... but sometimes you simply can't be
         DRY and you need a DRYing machine...

1.  **Template consumers**. Programmers that want to start a new project quickly, or that want to evolve it comfortably.

Non-humans should be happy also by using Krupy's CLI or API, as long as their expectations are the same as for those humans... and as long as they have feelings.

Templates have these goals:

1. **[Code scaffolding](<https://en.wikipedia.org/wiki/Scaffold_(programming)>)**. Help
   consumers have a working source code tree as quickly as possible. All templates allow scaffolding.
1. **Code lifecycle management**. When the template evolves, let consumers update their projects. Not all templates allow updating.

Krupy tries to have a smooth learning curve that lets you create simple templates that can evolve into complex ones as needed.

## Browse or tag public templates

You can browse public Krupy templates on GitHub using
[the `krupy-template` topic](https://github.com/topics/krupy-template). Use them as inspiration!

If you want your template to appear in that list, just add the topic to it! 🏷
