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

    def get_progress(self) -> float:
        """
        Get timer progress as percentage.

        Returns:
            Progress from 0.0 to 1.0
        """
        if self.duration == 0:
            return 0.0
        return (self.duration - self.remaining) / self.duration

    def get_state(self) -> dict:
        """Get current timer state for persistence."""
        return {
            "duration": self.duration,
            "name": self.name,
            "remaining": self.remaining,
            "running": self.running,
            "completed": self.completed,
        }

    def set_state(self, state: dict):
        """Restore timer state from persistence."""
        self.duration = state.get("duration", 0)
        self.name = state.get("name", "Timer")
        self.remaining = state.get("remaining", self.duration)
        self.running = state.get("running", False)
        self.completed = state.get("completed", False)
