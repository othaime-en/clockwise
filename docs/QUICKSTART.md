# Clockwise Quick Start Guide

Get up and running with Clockwise in 5 minutes!

## Installation

```bash
pip install clockwise-tui
```

## First Run

```bash
clockwise
```

You'll see a split-screen interface with Timer on the left and Stopwatch on the right.

## 5-Minute Tutorial

### 1. Start a Pomodoro Timer (1 minute)

```
1. Press 'p' - Opens preset menu
2. Press Enter on "Pomodoro" (25 minutes)
3. Press Space - Timer starts counting down
4. Watch the progress bar fill up!
```

### 2. Use the Stopwatch (1 minute)

```
1. Press Tab - Switch to stopwatch
2. Press Space - Stopwatch starts
3. Press 'l' - Record a lap
4. Press 'l' again - Record another lap
5. Press Space - Pause
```

### 3. Create a Custom Timer (1 minute)

```
1. Press Tab - Switch back to timer
2. Press 'n' - New timer dialog opens
3. Enter name: "My Timer"
4. Enter duration: "5m" (or "10m", "1h", etc.)
5. Press Enter - Timer is set!
6. Press Space - Timer starts
```

### 4. Reset and Try Again (30 seconds)

```
Timer:
  Press 'r' - Resets to original duration

Stopwatch:
  Press Tab to switch
  Press 'r' - Resets to 00:00:00
```

### 5. Exit (30 seconds)

```
Press 'q' - Quit Clockwise
```

When you restart, your timers will resume where they left off (if you had them running)!

## Essential Keyboard Shortcuts

### Must-Know Shortcuts

```
q          - Quit
Tab        - Switch between Timer/Stopwatch
Space      - Start/Pause (works on focused widget)
r          - Reset (works on focused widget)
p          - Presets menu (timer only)
n          - New timer
l          - Lap (stopwatch only)
?          - Help
```

### Focus Indicator

- **Colored border** = Currently focused
- **Grayed border** = Not focused
- Shortcuts affect the focused widget

## Common Use Cases

### Use Case 1: Pomodoro Work Session

```bash
# Start Clockwise
clockwise

# Quick workflow:
p           # Open presets
[Select Pomodoro]
Space       # Start 25-min timer
[Work until timer completes]
d           # Dismiss alert
p           # Open presets
[Select Short Break]
Space       # Start 5-min break
```

### Use Case 2: Track Exercise

```bash
# Start stopwatch
Tab         # Switch to stopwatch
Space       # Start

# During exercise:
l           # Lap after each set
l           # Another lap
l           # Another lap

# When done:
Space       # Pause
# Review lap times
r           # Reset when ready
```

### Use Case 3: Cooking Multiple Items

```bash
# Timer 1: Pasta
n           # New timer
"Pasta"     # Name
"8m"        # Duration
Space       # Start

# Note: Currently, you can only run one timer at a time
# But you can use stopwatch simultaneously!
Tab         # Switch to stopwatch
Space       # Start stopwatch to track total cooking time
```

## Time Input Formats

When creating a new timer, you can use any of these formats:

| Input     | Meaning             |
| --------- | ------------------- |
| `30`      | 30 seconds          |
| `5m`      | 5 minutes           |
| `25m`     | 25 minutes          |
| `1h`      | 1 hour              |
| `1h30m`   | 1 hour 30 minutes   |
| `90s`     | 90 seconds          |
| `1:30`    | 1 minute 30 seconds |
| `1:30:00` | 1 hour 30 minutes   |

**Tip**: Minutes are usually easiest! Just use `25m`, `5m`, etc.

## Built-in Presets

Press `p` to access these presets:

- **Pomodoro** - 25 minutes (focus work)
- **Short Break** - 5 minutes (quick rest)
- **Long Break** - 15 minutes (extended rest)
- **Quick Timer** - 1 minute (rapid countdown)

## Configuration

### Where is my config file?

- **Linux**: `~/.config/clockwise/config.toml`
- **macOS**: `~/Library/Application Support/clockwise/config.toml`
- **Windows**: `%APPDATA%\clockwise\config.toml`

### How do I add a custom preset?

Edit your config file and add:

```toml
[presets.my_timer]
name = "My Custom Timer"
duration = 600  # 10 minutes in seconds
```

Save, restart Clockwise, and press `p` to see your new preset!

## Tips for Beginners

1. **Start Simple**: Just use the built-in Pomodoro preset first
2. **One Thing at a Time**: Focus timer OR stopwatch, master one before using both
3. **Tab is Your Friend**: Use Tab to switch focus between widgets
4. **Space to Start/Pause**: This works for both timer and stopwatch
5. **Press '?' for Help**: Forgot a shortcut? Press '?' anytime

## Common Questions

### Q: Can I run multiple timers at once?

A: Not yet! But you can run a timer AND stopwatch simultaneously.

### Q: Do my timers save when I close Clockwise?

A: Yes! By default, state persistence is enabled. Your timers will resume.

### Q: How do I disable state persistence?

A: Edit your config file:

```toml
[settings]
state_persistence = false
```

### Q: Can I change the colors?

A: Not yet, but themes are planned for a future release!

### Q: What if I want sound alerts?

A: Sound alerts are planned but not yet implemented.

## Next Steps

1. **Read the full [User Guide](USER_GUIDE.md)** - Detailed documentation
2. **Customize your presets** - Add timers for your specific needs
3. **Try different workflows** - Pomodoro, exercise tracking, cooking
4. **Give feedback** - Open issues or contribute on GitHub!

## Troubleshooting

### Nothing happens when I press keys

- Make sure terminal is focused
- Try clicking inside the Clockwise window
- Check if another app is intercepting keys

### Unicode characters look broken

- Use a modern terminal (Windows Terminal, iTerm2, etc.)
- Install a font with emoji support

### Timer/Stopwatch not updating

- Press any key to refresh
- Try resizing terminal
- Restart Clockwise

## Getting Help

- Press `?` inside Clockwise for keyboard shortcuts
- Read the [User Guide](USER_GUIDE.md)
- Check [GitHub Issues](https://github.com/othaime-en/clockwise/issues)
- Open a new issue if you found a bug

---

**You're ready to go!**

Launch Clockwise and start being productive:

```bash
clockwise
```
