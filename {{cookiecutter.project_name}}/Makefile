.PHONY: init
init:
	poetry config virtualenvs.in-project true
	poetry install
	poetry run pre-commit install --hook-type pre-commit

.PHONY: clean-pyc
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

.PHONY: clean-test
clean-test:
	rm -f .coverage
	rm -f coverage.*

.PHONY: clean
clean: clean-pyc clean-test

.PHONY: test
test: clean
	poetry run pytest tests -v --cov

.PHONY: flake8
flake8:
	poetry run flake8 src tests

.PHONY: mypy
mypy:
	poetry run mypy src tests

.PHONY: pydocstyle
pydocstyle:
	poetry run pydocstyle src tests

.PHONY: lint
lint: flake8 mypy pydocstyle

.PHONY: isort
isort:
	poetry run isort src tests

.PHONY: black
black:
	poetry run black src tests

.PHONY: format
format: isort black

.PHONY: check
check: test lint format

.PHONY: publish
publish:
	poetry publish --build --repository repo
