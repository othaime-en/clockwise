"""Preset manager widget for selecting and managing timer presets."""

from textual.screen import ModalScreen
from textual.binding import Binding

from ..utils.formatting import format_time_natural


class PresetListScreen(ModalScreen):
    """Modal screen for selecting a timer preset."""

    BINDINGS = [
        Binding("escape", "dismiss", "Close"),
    ]

    def __init__(self, presets: dict, **kwargs):
        super().__init__(**kwargs)
        self.presets = presets