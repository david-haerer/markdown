import typer
from rich.console import Console
from rich.markdown import Markdown
from pathlib import Path

app = typer.Typer()

@app.command()
def main(path: Path):
    console = Console()
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    markdown = Markdown(content)
    console.print(markdown)


if __name__ == "__main__":
    app.run()
