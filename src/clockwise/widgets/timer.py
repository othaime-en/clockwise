"""Timer widget for Textual UI."""

from textual.app import ComposeResult
from textual.containers import Container, Vertical
from textual.widgets import Static, ProgressBar, Button
from textual.reactive import reactive

from ..models.timer_model import Timer
from ..utils.formatting import format_time


class TimerWidget(Container):
    """Widget displaying countdown timer."""

    DEFAULT_CSS = """
    TimerWidget {
        width: 1fr;
        height: 100%;
        border: solid $primary;
        padding: 1 2;
    }

    TimerWidget.focused {
        border: solid $accent;
    }

    TimerWidget.completed {
        border: solid $success;
        background: $success 20%;
    }

    TimerWidget #timer-title {
        text-align: center;
        text-style: bold;
        color: $text;
        margin-bottom: 1;
    }

    TimerWidget #timer-display {
        text-align: center;
        text-style: bold;
        height: 5;
        content-align: center middle;
    }

    TimerWidget #timer-display-large {
        text-style: bold;
        color: $accent;
    }

    TimerWidget #timer-name {
        text-align: center;
        color: $text-muted;
        margin-top: 1;
    }

    TimerWidget ProgressBar {
        margin: 1 0;
    }

    TimerWidget #timer-status {
        text-align: center;
        color: $text-muted;
        height: 1;
        margin-top: 1;
    }
    """

    time_remaining = reactive(0)
    is_running = reactive(False)
    is_completed = reactive(False)
    timer_name = reactive("Timer")
    progress = reactive(0.0)

    def __init__(self, timer: Timer, **kwargs):
        super().__init__(**kwargs)
        self.timer = timer
        self.can_focus = True

    def compose(self) -> ComposeResult:
        """Compose the timer widget."""
        yield Static("⏲️  TIMER", id="timer-title")
        with Vertical():
            yield Static(id="timer-display")
            yield ProgressBar(total=100, show_eta=False, id="timer-progress")
            yield Static(id="timer-name")
            yield Static(id="timer-status")