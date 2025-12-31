"""Preset manager widget for selecting and managing timer presets."""

from textual.app import ComposeResult
from textual.containers import Container, VerticalScroll
from textual.widgets import Button, Static
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