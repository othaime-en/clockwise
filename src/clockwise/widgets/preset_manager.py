"""Preset manager widget for selecting and managing timer presets."""

from textual.app import ComposeResult
from textual.containers import Container, Vertical, VerticalScroll
from textual.widgets import Button, Static, Label, Input
from textual.screen import ModalScreen
from textual.binding import Binding

from ..utils.formatting import format_time_natural


class PresetListScreen(ModalScreen):
    """Modal screen for selecting a timer preset."""

    BINDINGS = [
        Binding("escape", "dismiss", "Close"),
    ]

    DEFAULT_CSS = """
    PresetListScreen {
        align: center middle;
    }

    PresetListScreen > Container {
        width: 60;
        height: auto;
        max-height: 80%;
        background: $surface;
        border: thick $primary;
        padding: 1 2;
    }

    PresetListScreen #preset-title {
        text-align: center;
        text-style: bold;
        color: $accent;
        margin-bottom: 1;
    }

    PresetListScreen Button {
        width: 100%;
        margin: 0 0 1 0;
    }

    PresetListScreen .preset-button {
        height: auto;
        min-height: 3;
    }

    PresetListScreen #close-button {
        margin-top: 1;
    }
    """

    def __init__(self, presets: dict, **kwargs):
        super().__init__(**kwargs)
        self.presets = presets

    def compose(self) -> ComposeResult:
        """Compose the preset selection screen."""
        with Container():
            yield Static("⏲️  Select Timer Preset", id="preset-title")
            with VerticalScroll():
                for preset_id, preset_data in self.presets.items():
                    name = preset_data["name"]
                    duration = preset_data["duration"]
                    duration_str = format_time_natural(duration)
                    button = Button(
                        f"{name}\n[dim]{duration_str}[/]",
                        id=f"preset-{preset_id}",
                        classes="preset-button"
                    )
                    button.preset_id = preset_id
                    button.preset_data = preset_data
                    yield button
            yield Button("Close", id="close-button", variant="primary")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press."""
        if event.button.id == "close-button":
            self.dismiss(None)
        elif event.button.id and event.button.id.startswith("preset-"):
            preset_data = event.button.preset_data
            self.dismiss(preset_data)


class NewTimerScreen(ModalScreen):
    """Modal screen for creating a new custom timer."""

    BINDINGS = [
        Binding("escape", "dismiss", "Cancel"),
    ]

    def compose(self) -> ComposeResult:
        """Compose the new timer screen."""
        with Container():
            yield Static("⏲️  Create New Timer", id="new-timer-title")
            yield Label("Timer Name:")
            yield Input(placeholder="e.g., Tea Timer", id="name-input")
            yield Label("Duration:")
            yield Input(placeholder="e.g., 5m, 1h30m, 90", id="duration-input")
            yield Static(
                "Formats: 5m, 1h30m, 90 (seconds), 1:30 (MM:SS)",
                id="help-text"
            )
            with Container(id="button-container"):
                yield Button("Create", variant="success", id="create-button")
                yield Button("Cancel", variant="default", id="cancel-button")