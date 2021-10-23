import typer

app = typer.Typer()


@app.command()
def main() -> None:
    """{{cookiecutter.friendly_name}}."""


if __name__ == "__main__":
    app(prog_name="{{cookiecutter.project_name}}")  # pragma: no cover
