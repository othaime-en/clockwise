"""Stopwatch widget for Textual UI."""

from textual.app import ComposeResult
from textual.containers import Container, Vertical, VerticalScroll
from textual.widgets import Static
from textual.reactive import reactive

from ..models.stopwatch_model import Stopwatch
from ..utils.formatting import format_time


class StopwatchWidget(Container):
    """Widget displaying stopwatch."""

    DEFAULT_CSS = """
    StopwatchWidget {
        width: 1fr;
        height: 100%;
        border: solid $primary;
        padding: 1 2;
    }

    StopwatchWidget.focused {
        border: solid $accent;
    }

    StopwatchWidget #stopwatch-title {
        text-align: center;
        text-style: bold;
        color: $text;
        margin-bottom: 1;
    }

    StopwatchWidget #stopwatch-display {
        text-align: center;
        text-style: bold;
        height: 5;
        content-align: center middle;
    }

    StopwatchWidget #stopwatch-current-lap {
        text-align: center;
        color: $text-muted;
        margin-top: 1;
    }

    StopwatchWidget #stopwatch-status {
        text-align: center;
        color: $text-muted;
        height: 1;
        margin-top: 1;
    }

    StopwatchWidget #laps-container {
        height: auto;
        max-height: 10;
        margin-top: 1;
        border: solid $primary-darken-2;
        padding: 1;
    }

    StopwatchWidget #laps-title {
        text-style: bold;
        color: $accent;
    }

    StopwatchWidget .lap-entry {
        color: $text;
    }
    """

    elapsed_time = reactive(0)
    is_running = reactive(False)
    lap_count = reactive(0)

    def __init__(self, stopwatch: Stopwatch, **kwargs):
        super().__init__(**kwargs)
        self.stopwatch = stopwatch
        self.can_focus = True

    def compose(self) -> ComposeResult:
        """Compose the stopwatch widget."""
        yield Static("⏱️  STOPWATCH", id="stopwatch-title")
        with Vertical():
            yield Static(id="stopwatch-display")
            yield Static(id="stopwatch-current-lap")
            yield Static(id="stopwatch-status")
            with VerticalScroll(id="laps-container"):
                yield Static("📊 Laps", id="laps-title")
                yield Static(id="laps-list")
