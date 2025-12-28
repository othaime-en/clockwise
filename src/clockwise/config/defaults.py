"""Default configuration values for Clockwise."""

DEFAULT_CONFIG = {
    "settings": {
        "state_persistence": True,
        "alert_style": "flash",  # flash, border, color
        "time_format": "digital",  # digital, natural
    },
    "presets": {
        "pomodoro": {
            "name": "Pomodoro",
            "duration": 1500,  # 25 minutes
        },
        "short_break": {
            "name": "Short Break",
            "duration": 300,  # 5 minutes
        },
        "long_break": {
            "name": "Long Break",
            "duration": 900,  # 15 minutes
        },
        "quick_timer": {
            "name": "Quick Timer",
            "duration": 60,  # 1 minute
        },
    },
}


def get_default_config():
    """Return a copy of the default configuration."""
    import copy
    return copy.deepcopy(DEFAULT_CONFIG)