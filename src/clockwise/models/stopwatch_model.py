"""Stopwatch model for elapsed time tracking."""

from typing import List


class Stopwatch:
    """Stopwatch model with lap tracking."""

    def __init__(self):
        """Initialize stopwatch."""
        self.elapsed = 0
        self.running = False
        self.laps: List[int] = []

    def start(self):
        """Start the stopwatch."""
        self.running = True

    def pause(self):
        """Pause the stopwatch."""
        self.running = False

    def toggle(self):
        """Toggle between running and paused."""
        if self.running:
            self.pause()
        else:
            self.start()

    def reset(self):
        """Reset stopwatch to zero and clear laps."""
        self.elapsed = 0
        self.running = False
        self.laps = []

    def tick(self):
        """Increase elapsed time by 1 second."""
        if self.running:
            self.elapsed += 1

    def add_lap(self):
        """Record current elapsed time as a lap."""
        if self.elapsed > 0:
            self.laps.append(self.elapsed)

    def get_last_lap_time(self) -> int:
        """Get the time of the last lap (difference from previous)."""
        if not self.laps:
            return 0
        if len(self.laps) == 1:
            return self.laps[0]
        return self.laps[-1] - self.laps[-2]

    def get_current_lap_time(self) -> int:
        """Get time since last lap."""
        if not self.laps:
            return self.elapsed
        return self.elapsed - self.laps[-1]