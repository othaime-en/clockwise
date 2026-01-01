"""Main Clockwise application."""

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

class ClockwiseApp(App):
    """A minimalist TUI timer and stopwatch application."""

    def compose(self) -> ComposeResult:
        """Compose the application layout."""
        yield Header(show_clock=True)
        yield Footer()

def run():
    """Run the Clockwise application."""
    app = ClockwiseApp()
    app.run()