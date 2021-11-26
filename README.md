![Luke Miloszewski](./assets/README.png)

# Python Template

A package template to automate python development 🐍

## Overview

* 🤖 Build automation with Makefile
* 📦 Dependency and package management with Poetry
* 🎣 Git hooks with Pre-Commit
* 🎃 Linting with Flake8, MyPy and Pydocstyle
* 👔 Formatting with Black and Isort
* 💻 Command-Line Interface with Typer
* 🎯 Testing and coverage checks with Pytest, Pytest-Cov and Tox
* ✅ Continuous integration with GitHub Actions
* ➕ Automated dependency updates with Dependabot
* 🚀 Release changelog with Release Drafter

This template supports Python 3.7.x, 3.8.x and 3.9.x.

## Requirements

* install python 3.7.x, 3.8.x, 3.9.x
* install [poetry](https://python-poetry.org)
* install [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.3/)
* install [tox](https://tox.wiki/en/latest/index.html)

## Installation

```shell
# install project
cookiecutter gh:lukemiloszewski/python-template

# initialise project
make init

# run linting and formatting
make pre-commit

# run tests
tox
```
