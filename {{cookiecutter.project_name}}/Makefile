init:
	poetry config virtualenvs.in-project true
	poetry install
	poetry run pre-commit install --hook-type pre-commit --install-hooks
	poetry run pre-commit autoupdate

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
	poetry run pytest tests -v

lint:
	poetry run flake8 src tests
	poetry run mypy src tests
	poetry run pydocstyle src tests

format:
	poetry run isort src tests
	poetry run black src tests

check: test lint format

publish:
	poetry publish --build --repository repo
