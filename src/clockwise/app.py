"""Main Clockwise application."""

from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.binding import Binding
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

    BINDINGS = [
        Binding("q", "quit", "Quit", priority=True),
        Binding("question_mark", "help", "Help"),
        Binding("tab", "switch_focus", "Switch Focus"),
        Binding("space", "toggle_active", "Start/Pause"),
        Binding("r", "reset_active", "Reset"),
        Binding("p", "show_presets", "Presets (Timer)"),
        Binding("n", "new_timer", "New Timer"),
        Binding("l", "add_lap", "Lap (Stopwatch)"),
        Binding("d", "dismiss_alert", "Dismiss Alert"),
    ]

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