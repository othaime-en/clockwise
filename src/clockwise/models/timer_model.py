"""Timer model for countdown functionality."""

from typing import Optional


class Timer:
    """Countdown timer model."""

    def __init__(self, duration: int = 0, name: str = "Timer"):
        """
        Initialize timer.

        Args:
            duration: Timer duration in seconds
            name: Name/label for the timer
        """
        self.duration = duration
        self.name = name
        self.remaining = duration
        self.running = False
        self.completed = False

    def start(self):
        """Start the timer."""
        if self.remaining > 0:
            self.running = True
            self.completed = False

    def pause(self):
        """Pause the timer."""
        self.running = False

    def toggle(self):
        """Toggle between running and paused."""
        if self.running:
            self.pause()
        else:
            self.start()

    def reset(self):
        """Reset timer to initial duration."""
        self.remaining = self.duration
        self.running = False
        self.completed = False

    def tick(self):
        """Decrease remaining time by 1 second."""
        if self.running and self.remaining > 0:
            self.remaining -= 1
            if self.remaining == 0:
                self.running = False
                self.completed = True

    def set_duration(self, duration: int, name: str = "Timer"):
        """
        Set new duration and reset timer.

        Args:
            duration: New duration in seconds
            name: New timer name
        """
        self.duration = duration
        self.name = name
        self.reset()