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

    DEFAULT_CSS = """
    NewTimerScreen {
        align: center middle;
    }

    NewTimerScreen > Container {
        width: 60;
        height: auto;
        background: $surface;
        border: thick $primary;
        padding: 2;
    }

    NewTimerScreen #new-timer-title {
        text-align: center;
        text-style: bold;
        color: $accent;
        margin-bottom: 1;
    }

    NewTimerScreen Label {
        margin: 1 0 0 0;
    }

    NewTimerScreen Input {
        margin: 0 0 1 0;
    }

    NewTimerScreen #button-container {
        layout: horizontal;
        height: auto;
        margin-top: 1;
    }

    NewTimerScreen Button {
        width: 1fr;
        margin: 0 1;
    }

    NewTimerScreen #help-text {
        color: $text-muted;
        text-align: center;
        margin: 1 0;
    }
    """

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

    def on_mount(self) -> None:
        """Focus the name input on mount."""
        self.query_one("#name-input", Input).focus()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press."""
        if event.button.id == "cancel-button":
            self.dismiss(None)
        elif event.button.id == "create-button":
            name_input = self.query_one("#name-input", Input)
            duration_input = self.query_one("#duration-input", Input)

            name = name_input.value.strip()
            duration_str = duration_input.value.strip()

            if not name:
                self.notify("Please enter a timer name", severity="error")
                return

            if not duration_str:
                self.notify("Please enter a duration", severity="error")
                return

            try:
                from ..utils.formatting import parse_time_input
                duration = parse_time_input(duration_str)

                if duration <= 0:
                    self.notify("Duration must be greater than 0", severity="error")
                    return

                self.dismiss({"name": name, "duration": duration})
            except ValueError:
                self.notify("Invalid duration format", severity="error")

