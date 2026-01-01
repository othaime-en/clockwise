"""Configuration management for Clockwise."""

import tomllib
from pathlib import Path
from typing import Any, Dict

try:
    import tomli_w
except ImportError:
    tomli_w = None

from platformdirs import user_config_dir, user_data_dir

from .defaults import get_default_config


class ConfigManager:
    """Manages application configuration."""

    def __init__(self):
        self.app_name = "clockwise"
        self.config_dir = Path(user_config_dir(self.app_name))
        self.data_dir = Path(user_data_dir(self.app_name))
        self.config_file = self.config_dir / "config.toml"
        self.state_file = self.data_dir / "state.json"

        self.config: Dict[str, Any] = {}
        self._ensure_directories()

    def _ensure_directories(self):
        """Ensure config and data directories exist."""
        self.config_dir.mkdir(parents=True, exist_ok=True)
        self.data_dir.mkdir(parents=True, exist_ok=True)