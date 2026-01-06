"""Tests for Timer model."""

from clockwise.models.timer_model import Timer


def test_timer_initialization():
    """Test timer initializes correctly."""
    timer = Timer(duration=60, name="Test Timer")
    assert timer.duration == 60
    assert timer.name == "Test Timer"
    assert timer.remaining == 60
    assert timer.running is False
    assert timer.completed is False


def test_timer_start():
    """Test timer starts correctly."""
    timer = Timer(duration=60)
    timer.start()
    assert timer.running is True
    assert timer.completed is False


def test_timer_pause():
    """Test timer pauses correctly."""
    timer = Timer(duration=60)
    timer.start()
    timer.pause()
    assert timer.running is False


def test_timer_toggle():
    """Test timer toggle functionality."""
    timer = Timer(duration=60)

    timer.toggle()
    assert timer.running is True

    timer.toggle()
    assert timer.running is False


def test_timer_reset():
    """Test timer resets correctly."""
    timer = Timer(duration=60)
    timer.start()
    timer.tick()
    timer.tick()
    assert timer.remaining == 58

    timer.reset()
    assert timer.remaining == 60
    assert timer.running is False
    assert timer.completed is False


def test_timer_tick():
    """Test timer countdown."""
    timer = Timer(duration=5)
    timer.start()

    timer.tick()
    assert timer.remaining == 4
    assert timer.running is True

    # Tick until complete
    for _ in range(4):
        timer.tick()

    assert timer.remaining == 0
    assert timer.running is False
    assert timer.completed is True


def test_timer_tick_when_paused():
    """Test timer doesn't tick when paused."""
    timer = Timer(duration=60)
    initial_remaining = timer.remaining

    timer.tick()
    assert timer.remaining == initial_remaining


def test_timer_get_progress():
    """Test progress calculation."""
    timer = Timer(duration=100)
    assert timer.get_progress() == 0.0

    timer.start()
    for _ in range(50):
        timer.tick()

    assert timer.get_progress() == 0.5


def test_timer_set_duration():
    """Test setting new duration."""
    timer = Timer(duration=60, name="Old Timer")
    timer.start()
    timer.tick()

    timer.set_duration(120, "New Timer")
    assert timer.duration == 120
    assert timer.name == "New Timer"
    assert timer.remaining == 120
    assert timer.running is False


def test_timer_state_persistence():
    """Test state save and restore."""
    timer = Timer(duration=60, name="Test")
    timer.start()
    timer.tick()
    timer.tick()

    state = timer.get_state()
    assert state["duration"] == 60
    assert state["name"] == "Test"
    assert state["remaining"] == 58
    assert state["running"] is True

    # Create new timer and restore state
    new_timer = Timer()
    new_timer.set_state(state)
    assert new_timer.duration == 60
    assert new_timer.name == "Test"
    assert new_timer.remaining == 58
    assert new_timer.running is True
