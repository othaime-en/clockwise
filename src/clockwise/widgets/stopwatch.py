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

    def on_mount(self) -> None:
        """Set up the widget when mounted."""
        self.update_display()

    def update_display(self):
        """Update the display with current stopwatch state."""
        self.elapsed_time = self.stopwatch.elapsed
        self.is_running = self.stopwatch.running
        self.lap_count = len(self.stopwatch.laps)

        # Update main display
        display = self.query_one("#stopwatch-display", Static)
        time_str = format_time(self.stopwatch.elapsed, show_hours=True)
        color = "#00ff00" if self.stopwatch.running else "#888888"
        display.update(f"[bold {color}]{time_str}[/]")

        # Update current lap time
        current_lap_display = self.query_one("#stopwatch-current-lap", Static)
        current_lap_time = self.stopwatch.get_current_lap_time()
        current_lap_display.update(
            f"Current Lap: {format_time(current_lap_time, show_hours=False)}"
        )

        # Update status
        status = self.query_one("#stopwatch-status", Static)
        if self.stopwatch.running:
            status.update("▶️  Running - Press SPACE to pause, 'l' for lap")
        elif self.stopwatch.elapsed > 0:
            status.update("⏸️  Paused - Press SPACE to resume")
        else:
            status.update("Press SPACE to start")

        # Update laps list
        self.update_laps_list()

    def update_laps_list(self):
        """Update the laps list display."""
        laps_list = self.query_one("#laps-list", Static)

        if not self.stopwatch.laps:
            laps_list.update("[dim]No laps recorded[/]")
            return

        lines = []
        for i, lap_time in enumerate(self.stopwatch.laps, 1):
            if i == 1:
                lap_duration = lap_time
            else:
                lap_duration = lap_time - self.stopwatch.laps[i - 2]

            time_str = format_time(lap_time, show_hours=False)
            duration_str = format_time(lap_duration, show_hours=False)
            lines.append(f"Lap {i}: {time_str} (+{duration_str})")

        laps_list.update("\n".join(lines))

    def handle_tick(self):
        """Handle stopwatch tick."""
        self.stopwatch.tick()
        self.update_display()
