"""Main Clockwise application."""

from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.binding import Binding
from textual.widgets import Header, Footer

from .models.timer_model import Timer
from .models.stopwatch_model import Stopwatch
from .widgets.timer import TimerWidget
from .widgets.stopwatch import StopwatchWidget
from .widgets.preset_manager import PresetListScreen, NewTimerScreen
from .config.manager import ConfigManager

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

    def __init__(self):
        super().__init__()
        self.config_manager = ConfigManager()
        self.config = self.config_manager.load_config()

        # Initialize models
        self.timer = Timer()
        self.stopwatch = Stopwatch()

        self.timer_widget = None
        self.stopwatch_widget = None
        self.focused_widget = "timer"  # "timer" or "stopwatch"

    def compose(self) -> ComposeResult:
        """Compose the application layout."""
        yield Header(show_clock=True)
        with Horizontal():
            self.timer_widget = TimerWidget(self.timer, id="timer-widget")
            self.stopwatch_widget = StopwatchWidget(self.stopwatch, id="stopwatch-widget")
            yield self.timer_widget
            yield self.stopwatch_widget
        yield Footer()

    def on_mount(self) -> None:
        """Set up the application when mounted."""
        # Set initial focus
        self.timer_widget.add_class("focused")
        self.timer_widget.focus()

        # Set up tick timer (1 second interval)
        self.set_interval(1, self.tick_update)

    def tick_update(self):
        """Update timer and stopwatch every second."""
        self.timer_widget.handle_tick()
        self.stopwatch_widget.handle_tick()

    def action_switch_focus(self):
        """Switch focus between timer and stopwatch."""
        if self.focused_widget == "timer":
            self.focused_widget = "stopwatch"
            self.timer_widget.remove_class("focused")
            self.stopwatch_widget.add_class("focused")
            self.stopwatch_widget.focus()
        else:
            self.focused_widget = "timer"
            self.stopwatch_widget.remove_class("focused")
            self.timer_widget.add_class("focused")
            self.timer_widget.focus()

    def action_toggle_active(self):
        """Toggle start/pause for the focused widget."""
        if self.focused_widget == "timer":
            self.timer.toggle()
            self.timer_widget.update_display()
        else:
            self.stopwatch.toggle()
            self.stopwatch_widget.update_display()

    def action_reset_active(self):
        """Reset the focused widget."""
        if self.focused_widget == "timer":
            self.timer.reset()
            self.timer_widget.update_display()
        else:
            self.stopwatch.reset()
            self.stopwatch_widget.update_display()

    def action_show_presets(self):
        """Show preset selection screen (timer only)."""
        if self.focused_widget == "timer":
            presets = self.config_manager.get_presets()
            self.push_screen(PresetListScreen(presets), self._handle_preset_selection)

    def _handle_preset_selection(self, preset_data):
        """Handle preset selection."""
        if preset_data:
            self.timer.set_duration(preset_data["duration"], preset_data["name"])
            self.timer_widget.update_display()
            self.notify(f"Timer set: {preset_data['name']}")

    def action_new_timer(self):
        """Show new timer creation screen."""
        self.push_screen(NewTimerScreen(), self._handle_new_timer)

    def _handle_new_timer(self, timer_data):
        """Handle new timer creation."""
        if timer_data:
            self.timer.set_duration(timer_data["duration"], timer_data["name"])
            self.timer_widget.update_display()
            self.notify(f"Timer set: {timer_data['name']}")

    def action_add_lap(self):
        """Add lap time (stopwatch only)."""
        if self.focused_widget == "stopwatch":
            self.stopwatch.add_lap()
            self.stopwatch_widget.update_display()
            self.notify("Lap recorded")

    def action_dismiss_alert(self):
        """Dismiss timer completion alert."""
        if self.timer.completed:
            self.timer.reset()
            self.timer_widget.update_display()

    def action_help(self):
        """Show help message."""
        help_text = """
        Clockwise - Keyboard Shortcuts

        Global:
          q - Quit application
          Tab - Switch focus (Timer/Stopwatch)
          ? - Show this help

        Timer:
          Space - Start/Pause
          r - Reset
          p - Show presets
          n - Create new timer
          d - Dismiss completion alert

        Stopwatch:
          Space - Start/Pause
          r - Reset
          l - Record lap time
        """
        self.notify(help_text, timeout=10)

def run():
    """Run the Clockwise application."""
    app = ClockwiseApp()
    app.run()