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

    def load_config(self) -> Dict[str, Any]:
        """Load configuration from file or create default."""
        if self.config_file.exists():
            try:
                with open(self.config_file, "rb") as f:
                    self.config = tomllib.load(f)
                # Merge with defaults to ensure all keys exist
                self.config = self._merge_with_defaults(self.config)
            except Exception as e:
                print(f"Error loading config: {e}")
                self.config = get_default_config()
        else:
            self.config = get_default_config()
            self.save_config()

        return self.config

    def _merge_with_defaults(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Merge loaded config with defaults to ensure all keys exist."""
        default = get_default_config()

        # Merge settings
        if "settings" not in config:
            config["settings"] = {}
        for key, value in default["settings"].items():
            if key not in config["settings"]:
                config["settings"][key] = value

        # Ensure presets exist
        if "presets" not in config:
            config["presets"] = default["presets"]

        return config