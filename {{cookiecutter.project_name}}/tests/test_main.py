"""Test cases for the __main__ module."""
import pytest
from typer.testing import CliRunner

from {{cookiecutter.package_name}} import __main__


def test_main_runs(runner: CliRunner) -> None:
    """Exits with a status code of zero."""
    result = runner.invoke(__main__.app)
    assert result.exit_code == 0
