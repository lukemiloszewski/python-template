init:
	poetry config virtualenvs.in-project true
	poetry install
	poetry run pre-commit install --hook-type pre-commit

requirements:
	poetry export -f requirements.txt --output requirements.txt

test:
	poetry run pytest tests -v --cov

publish:
	poetry publish --build

flake8:
	poetry run flake8 src tests

mypy:
	poetry run mypy src tests

pydocstyle:
	poetry run pydocstyle src tests

black:
	poetry run black src tests

isort:
	poetry run isort src tests

lint: flake8 mypy pydocstyle

format: black isort

pre-commit:
	poetry run pre-commit run --all-files --show-diff-on-failure --color=always
