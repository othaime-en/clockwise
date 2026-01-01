"""Main Clockwise application."""

from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Header, Footer

class ClockwiseApp(App):
    """A minimalist TUI timer and stopwatch application."""

    CSS = """
    Screen {
        background: $surface;
    }

    Header {
        background: $primary;
    }

    Footer {
        background: $primary;
    }

    Horizontal {
        height: 100%;
    }
    """

    def compose(self) -> ComposeResult:
        """Compose the application layout."""
        yield Header(show_clock=True)
        with Horizontal():
            pass
        yield Footer()

def run():
    """Run the Clockwise application."""
    app = ClockwiseApp()
    app.run()