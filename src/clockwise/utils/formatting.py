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

    if show_hours:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    else:
        # Convert all time to minutes:seconds format
        total_minutes = seconds // 60
        secs = seconds % 60
        return f"{total_minutes:02d}:{secs:02d}"


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

def parse_time_input(time_str: str) -> int:
    """
    Parse time input string into seconds.
    Supports formats: "25m", "1h30m", "90", "1:30:00"

    Args:
        time_str: Time string to parse

    Returns:
        Total seconds

    Raises:
        ValueError: If format is invalid
    """
    time_str = time_str.strip().lower()

    # Check for natural format (25m, 1h30m, etc.)
    if any(unit in time_str for unit in ["h", "m", "s"]):
        total_seconds = 0
        current_num = ""

        for char in time_str:
            if char.isdigit():
                current_num += char
            elif char in "hms":
                if current_num:
                    num = int(current_num)
                    if char == "h":
                        total_seconds += num * 3600
                    elif char == "m":
                        total_seconds += num * 60
                    elif char == "s":
                        total_seconds += num
                    current_num = ""

        return total_seconds

    # Check for colon format (HH:MM:SS or MM:SS)
    if ":" in time_str:
        parts = time_str.split(":")
        if len(parts) == 2:
            minutes, seconds = map(int, parts)
            return minutes * 60 + seconds
        elif len(parts) == 3:
            hours, minutes, seconds = map(int, parts)
            return hours * 3600 + minutes * 60 + seconds
        else:
            raise ValueError("Invalid time format")

    # Just a number, assume seconds
    return int(time_str)