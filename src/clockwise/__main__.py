"""Main entry point for Clockwise."""

import click
from .app import run


@click.command()
@click.version_option(version="0.1.0")
def main():
    """
    Clockwise - A minimalist TUI timer and stopwatch.

    Launch the application with beautiful terminal interface
    for managing timers and tracking time.
    """
    run()


if __name__ == "__main__":
    main()