# Contributing to Clockwise

Thank you for your interest in contributing to Clockwise! This document provides guidelines and instructions for contributing.

## Code of Conduct

Be respectful and constructive in all interactions. We're all here to make Clockwise better.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/othaime-en/clockwise.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate it and install dependencies: `pip install -e ".[dev]"`
5. Create a new branch: `git checkout -b feature/your-feature-name`

## Development Setup

### Prerequisites

- Python 3.8+
- Git
- A modern terminal that supports Unicode and colors

### Install Development Dependencies

```bash
pip install -e ".[dev]"
```

This installs:

- pytest (testing)
- pytest-cov (coverage)
- black (formatting)
- ruff (linting)

## Making Changes

### Code Style

We use:

- **Black** for code formatting (line length: 100)
- **Ruff** for linting
- Type hints where appropriate

Before committing, run:

```bash
# Format code
black src/ tests/

# Check linting
ruff check src/ tests/
```

### Writing Tests

- Add tests for all new features
- Maintain or improve test coverage
- Tests go in the `tests/` directory
- Use descriptive test names
- Follow the existing test patterns

Run tests:

```bash
pytest
```

Check coverage:

```bash
pytest --cov=clockwise --cov-report=html
```

### Commit Messages

Use clear, descriptive commit messages:

```
Add lap time export feature

- Implement CSV export for lap times
- Add export button to stopwatch widget
- Update documentation
```

Format:

- First line: Short summary (50 chars or less)
- Blank line
- Detailed description if needed

## Types of Contributions

### Bug Fixes

1. Check if the bug is already reported in Issues
2. If not, create a new issue describing the bug
3. Fork and create a branch: `fix/issue-number-description`
4. Fix the bug and add a test
5. Submit a pull request

### New Features

1. Create an issue to discuss the feature first
2. Get feedback from maintainers
3. Fork and create a branch: `feature/feature-name`
4. Implement the feature with tests
5. Update documentation
6. Submit a pull request

### Documentation

Documentation improvements are always welcome:

- Fix typos
- Clarify confusing sections
- Add examples
- Improve setup instructions

### Testing

Help improve test coverage:

- Add missing tests
- Improve existing tests
- Add integration tests

## Pull Request Process

1. **Update Documentation**: Ensure README.md and other docs are updated
2. **Add Tests**: All new code should have tests
3. **Pass CI**: Ensure all tests pass and code is formatted
4. **Update CHANGELOG**: Add your changes to CHANGELOG.md
5. **Write Clear Description**: Explain what changes you made and why

### PR Template

```markdown
## Description

Brief description of changes

## Type of Change

- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing

- [ ] Added tests
- [ ] All tests pass
- [ ] Manual testing completed

## Checklist

- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] Commits are clear and descriptive
```

## Project Structure

```
clockwise/
├── src/clockwise/       # Main application code
│   ├── models/          # Business logic (Timer, Stopwatch)
│   ├── widgets/         # UI components
│   ├── config/          # Configuration management
│   ├── state/           # State persistence
│   └── utils/           # Utility functions
├── tests/               # Test files
└── docs/                # Documentation
```

## Areas for Contribution

### High Priority

- [ ] Mouse support for widgets
- [ ] Themes/color schemes
- [ ] Sound alerts
- [ ] Timer history tracking
- [ ] Export lap times to CSV
- [ ] Custom keyboard shortcuts

### Nice to Have

- [ ] Multiple timers running simultaneously
- [ ] Timer templates/categories
- [ ] Statistics and analytics
- [ ] Integration with calendar apps
- [ ] Desktop notifications
- [ ] Pomodoro session tracking

### Documentation

- [ ] Video tutorials
- [ ] More screenshots
- [ ] Usage examples
- [ ] FAQ section
- [ ] Troubleshooting guide

## Testing Guidelines

### What to Test

- Core functionality (timer countdown, stopwatch counting)
- Edge cases (zero values, very large values)
- State persistence
- Configuration loading/saving
- Time parsing and formatting

### Test Structure

```python
def test_descriptive_name():
    """Test description."""
    # Arrange
    timer = Timer(duration=60)

    # Act
    timer.start()
    timer.tick()

    # Assert
    assert timer.remaining == 59
```

## Release Process

(For maintainers)

1. Update version in `pyproject.toml`
2. Update CHANGELOG.md
3. Create git tag: `git tag v0.2.0`
4. Push tag: `git push origin v0.2.0`
5. Build: `python -m build`
6. Upload: `twine upload dist/*`

## Questions?

- Open an issue for questions
- Check existing issues and PRs
- Read the documentation

## Recognition

Contributors will be added to the README.md contributors section.

Thank you for contributing to Clockwise!
