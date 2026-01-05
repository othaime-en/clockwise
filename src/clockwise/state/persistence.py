"""State persistence for Clockwise."""

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional


class StatePersistence:
    """Manages application state persistence."""

    def __init__(self, state_file: Path):
        self.state_file = state_file

    def save_state(self, timer_state: Dict[str, Any], stopwatch_state: Dict[str, Any]):
        """Save current application state."""
        state = {
            "timer": timer_state,
            "stopwatch": stopwatch_state,
            "timestamp": datetime.now().isoformat(),
        }

        try:
            with open(self.state_file, "w") as f:
                json.dump(state, f, indent=2)
        except Exception as e:
            # Silently fail - state persistence is not critical
            pass

    def load_state(self) -> Optional[Dict[str, Any]]:
        """Load saved application state."""
        if not self.state_file.exists():
            return None

        try:
            with open(self.state_file, "r") as f:
                state = json.load(f)
            return state
        except Exception as e:
            # If state is corrupted, return None
            return None

    def clear_state(self):
        """Clear saved state."""
        if self.state_file.exists():
            try:
                self.state_file.unlink()
            except Exception:
                pass

    def get_timer_state(self) -> Optional[Dict[str, Any]]:
        """Get saved timer state."""
        state = self.load_state()
        return state.get("timer") if state else None

    def get_stopwatch_state(self) -> Optional[Dict[str, Any]]:
        """Get saved stopwatch state."""
        state = self.load_state()
        return state.get("stopwatch") if state else None