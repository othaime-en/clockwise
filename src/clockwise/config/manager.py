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

    def save_config(self):
        """Save current configuration to file."""
        if tomli_w is None:
            # Fallback: write TOML manually
            self._write_toml_manually()
        else:
            with open(self.config_file, "wb") as f:
                tomli_w.dump(self.config, f)

    def _write_toml_manually(self):
        """Write TOML config manually without tomli_w."""
        lines = ["[settings]"]
        for key, value in self.config.get("settings", {}).items():
            if isinstance(value, str):
                lines.append(f'{key} = "{value}"')
            elif isinstance(value, bool):
                lines.append(f"{key} = {str(value).lower()}")
            else:
                lines.append(f"{key} = {value}")

        lines.append("\n[presets]")
        for preset_id, preset_data in self.config.get("presets", {}).items():
            lines.append(f"\n[presets.{preset_id}]")
            for key, value in preset_data.items():
                if isinstance(value, str):
                    lines.append(f'{key} = "{value}"')
                else:
                    lines.append(f"{key} = {value}")

        with open(self.config_file, "w") as f:
            f.write("\n".join(lines))

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

    def get_setting(self, key: str, default: Any = None) -> Any:
        """Get a setting value."""
        return self.config.get("settings", {}).get(key, default)

    def set_setting(self, key: str, value: Any):
        """Set a setting value."""
        if "settings" not in self.config:
            self.config["settings"] = {}
        self.config["settings"][key] = value
        self.save_config()