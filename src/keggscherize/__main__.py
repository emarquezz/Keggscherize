"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Keggscherize."""


if __name__ == "__main__":
    main(prog_name="Keggscherize")  # pragma: no cover
