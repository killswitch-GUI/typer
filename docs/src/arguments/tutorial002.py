import typer


def main(name: str = typer.Argument(None)):
    if name is None:
        typer.echo("Hello World!")
    else:
        typer.echo(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
