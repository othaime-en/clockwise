"""Stopwatch model for elapsed time tracking."""

class Stopwatch:
    """Stopwatch model with lap tracking."""

    def __init__(self):
        """Initialize stopwatch."""
        self.elapsed = 0
        self.running = False

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
        """Reset stopwatch to zero."""
        self.elapsed = 0
        self.running = False

    def tick(self):
        """Increase elapsed time by 1 second."""
        if self.running:
            self.elapsed += 1