"""Tests for formatting utilities."""

import pytest
from clockwise.utils.formatting import format_time, format_time_natural, parse_time_input


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


class TestFormatTimeNatural:
    """Tests for format_time_natural function."""

    def test_seconds_only(self):
        """Test formatting seconds only."""
        assert format_time_natural(45) == "45s"
        assert format_time_natural(5) == "5s"

    def test_minutes_only(self):
        """Test formatting minutes only."""
        assert format_time_natural(120) == "2m"
        assert format_time_natural(300) == "5m"

    def test_minutes_and_seconds(self):
        """Test formatting minutes and seconds."""
        assert format_time_natural(125) == "2m 5s"
        assert format_time_natural(90) == "1m 30s"

    def test_hours_only(self):
        """Test formatting hours only."""
        assert format_time_natural(3600) == "1h"
        assert format_time_natural(7200) == "2h"

    def test_hours_and_minutes(self):
        """Test formatting hours and minutes."""
        assert format_time_natural(3660) == "1h 1m"
        assert format_time_natural(5400) == "1h 30m"

    def test_hours_minutes_seconds(self):
        """Test formatting hours, minutes, and seconds."""
        assert format_time_natural(3661) == "1h 1m 1s"
        assert format_time_natural(3725) == "1h 2m 5s"

    def test_zero_time(self):
        """Test formatting zero."""
        assert format_time_natural(0) == "0s"


class TestParseTimeInput:
    """Tests for parse_time_input function."""

    def test_parse_seconds_only(self):
        """Test parsing plain numbers as seconds."""
        assert parse_time_input("60") == 60
        assert parse_time_input("90") == 90
        assert parse_time_input("5") == 5

    def test_parse_minutes(self):
        """Test parsing minutes format."""
        assert parse_time_input("5m") == 300
        assert parse_time_input("25m") == 1500
        assert parse_time_input("1m") == 60

    def test_parse_hours(self):
        """Test parsing hours format."""
        assert parse_time_input("1h") == 3600
        assert parse_time_input("2h") == 7200

    def test_parse_hours_and_minutes(self):
        """Test parsing combined hours and minutes."""
        assert parse_time_input("1h30m") == 5400
        assert parse_time_input("2h15m") == 8100

    def test_parse_hours_minutes_seconds(self):
        """Test parsing hours, minutes, and seconds."""
        assert parse_time_input("1h30m45s") == 5445
        assert parse_time_input("2h5m10s") == 7510

    def test_parse_colon_format_mm_ss(self):
        """Test parsing MM:SS format."""
        assert parse_time_input("05:30") == 330
        assert parse_time_input("1:30") == 90
        assert parse_time_input("25:00") == 1500

    def test_parse_colon_format_hh_mm_ss(self):
        """Test parsing HH:MM:SS format."""
        assert parse_time_input("01:30:00") == 5400
        assert parse_time_input("2:15:30") == 8130

    def test_parse_with_spaces(self):
        """Test parsing with spaces."""
        assert parse_time_input(" 5m ") == 300
        assert parse_time_input(" 1h 30m ") == 5400

    def test_parse_case_insensitive(self):
        """Test parsing is case insensitive."""
        assert parse_time_input("5M") == 300
        assert parse_time_input("1H") == 3600
        assert parse_time_input("30S") == 30

    def test_parse_invalid_format(self):
        """Test parsing invalid formats raises ValueError."""
        with pytest.raises(ValueError):
            parse_time_input("invalid")

        with pytest.raises(ValueError):
            parse_time_input("1:2:3:4")  # Too many colons

    def test_parse_empty_string(self):
        """Test parsing empty string raises ValueError."""
        with pytest.raises(ValueError):
            parse_time_input("")
