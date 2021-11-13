init:
	poetry config virtualenvs.in-project true
	poetry install
	poetry run pre-commit install --hook-type pre-commit

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f .coverage
	rm -f coverage.*

clean: clean-pyc clean-test

test: clean
	poetry run pytest tests -v --cov

flake8:
	poetry run flake8 src tests

mypy:
	poetry run mypy src tests

pydocstyle:
	poetry run pydocstyle src tests

isort:
	poetry run isort src tests

black:
	poetry run black src tests

pre-commit:
	poetry run pre-commit run --all-files --show-diff-on-failure --color=always

publish:
	poetry publish --build --repository repo
