"""Utility functions for time formatting."""


def format_time(seconds: int, show_hours: bool = True) -> str:
    """
    Format seconds into HH:MM:SS or MM:SS format.

    Args:
        seconds: Total seconds to format
        show_hours: Whether to show hours even if 0

    Returns:
        Formatted time string
    """
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    if hours > 0 or show_hours:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes:02d}:{secs:02d}"


def format_time_natural(seconds: int) -> str:
    """
    Format seconds into natural language (e.g., "5m 30s").

    Args:
        seconds: Total seconds to format

    Returns:
        Natural language time string
    """
    if seconds == 0:
        return "0s"

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    parts = []
    if hours > 0:
        parts.append(f"{hours}h")
    if minutes > 0:
        parts.append(f"{minutes}m")
    if secs > 0 or not parts:
        parts.append(f"{secs}s")

    return " ".join(parts)