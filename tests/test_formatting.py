"""Tests for formatting utilities."""

import pytest
from clockwise.utils.formatting import format_time

class TestFormatTime:
    """Tests for format_time function."""

    def test_format_seconds(self):
        """Test formatting seconds only."""
        assert format_time(45, show_hours=False) == "00:45"
        assert format_time(5, show_hours=False) == "00:05"

    def test_format_minutes(self):
        """Test formatting minutes and seconds."""
        assert format_time(125, show_hours=False) == "02:05"
        assert format_time(600, show_hours=False) == "10:00"

    def test_format_hours(self):
        """Test formatting with hours."""
        assert format_time(3661, show_hours=True) == "01:01:01"
        assert format_time(7200, show_hours=True) == "02:00:00"

    def test_format_with_show_hours_false(self):
        """Test that hours are hidden when show_hours=False and hours=0."""
        assert format_time(59, show_hours=False) == "00:59"
        assert format_time(3600, show_hours=False) == "60:00"  # Shows as minutes

    def test_zero_time(self):
        """Test formatting zero."""
        assert format_time(0, show_hours=False) == "00:00"
        assert format_time(0, show_hours=True) == "00:00:00"


