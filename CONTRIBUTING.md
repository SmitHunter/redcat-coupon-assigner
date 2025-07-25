# Contributing to RedCat Coupon Assigner

Thank you for your interest in contributing to the RedCat Coupon Assigner! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Types of Contributions

We welcome several types of contributions:

- 🐛 **Bug Reports**: Report issues or unexpected behavior
- 💡 **Feature Requests**: Suggest new features or improvements
- 📝 **Documentation**: Improve or add documentation
- 🔧 **Code Contributions**: Fix bugs or implement new features
- 🧪 **Testing**: Help test the application on different platforms
- 🎨 **UI/UX Improvements**: Enhance the user interface

## 🚀 Getting Started

### Prerequisites

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/redcat-coupon-assigner.git
   cd redcat-coupon-assigner
   ```
3. **Set up the development environment**:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # If available
   ```

### Development Setup

1. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

3. **Make your changes** following the guidelines below

4. **Test your changes** thoroughly

5. **Commit and push** your changes:
   ```bash
   git add .
   git commit -m "Add: your descriptive commit message"
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request** on GitHub

## 📋 Contribution Guidelines

### Code Style

- **Python Style**: Follow PEP 8 guidelines
- **Line Length**: Maximum 100 characters per line
- **Imports**: Group imports according to PEP 8 (standard library, third-party, local)
- **Function Names**: Use snake_case for functions and variables
- **Class Names**: Use PascalCase for class names
- **Constants**: Use UPPER_CASE for constants

### Code Quality

- **Documentation**: Add docstrings to all functions and classes
- **Comments**: Use inline comments for complex logic
- **Error Handling**: Implement proper exception handling
- **Type Hints**: Use type hints where appropriate (Python 3.8+)

Example:
```python
def assign_coupon(token: str, coupon_id: int, member_ids: List[int]) -> Dict[str, Any]:
    """
    Assign a coupon to multiple members.
    
    Args:
        token: Authentication token
        coupon_id: ID of the coupon to assign
        member_ids: List of member IDs to assign coupons to
        
    Returns:
        Dictionary containing the API response
        
    Raises:
        ValueError: If coupon_id is invalid
        requests.RequestException: If API request fails
    """
    # Implementation here
```

### Commit Messages

Use clear, descriptive commit messages:

- **Format**: `Type: Brief description`
- **Types**: 
  - `Add:` for new features
  - `Fix:` for bug fixes
  - `Update:` for updates to existing features
  - `Remove:` for removing features
  - `Docs:` for documentation changes
  - `Test:` for testing changes
  - `Refactor:` for code refactoring

Examples:
- `Add: bulk coupon assignment with progress tracking`
- `Fix: error handling for invalid member IDs`
- `Update: improve UI responsiveness on small screens`
- `Docs: add installation guide for Linux users`

### Testing

- **Manual Testing**: Test your changes with the actual application
- **Edge Cases**: Test with invalid inputs, network errors, etc.
- **Platform Testing**: Test on different operating systems if possible
- **Documentation**: Update documentation if your changes affect usage

### Pull Request Process

1. **Title**: Use a clear, descriptive title
2. **Description**: Provide a detailed description of changes
3. **Testing**: Describe how you tested your changes
4. **Screenshots**: Include screenshots for UI changes
5. **Breaking Changes**: Clearly mark any breaking changes

Pull Request Template:
```markdown
## Description
Brief description of changes made.

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
- [ ] Tested on Windows
- [ ] Tested on macOS
- [ ] Tested on Linux
- [ ] Manual testing completed
- [ ] Edge cases tested

## Screenshots (if applicable)
Add screenshots of UI changes.

## Additional Notes
Any additional information or context.
```

## 🐛 Reporting Bugs

### Before Submitting a Bug Report

1. **Check existing issues** to avoid duplicates
2. **Test with the latest version** of the application
3. **Gather system information**:
   - Operating system and version
   - Python version
   - Application version
   - Error messages (full stack trace)

### Bug Report Template

```markdown
**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**System Information:**
- OS: [e.g. Windows 10, macOS 11.0, Ubuntu 20.04]
- Python version: [e.g. 3.9.7]
- Application version: [e.g. 1.0.0]

**Additional context**
Add any other context about the problem here.
```

## 💡 Suggesting Features

### Feature Request Template

```markdown
**Is your feature request related to a problem?**
A clear and concise description of what the problem is.

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions or features you've considered.

**Additional context**
Add any other context or screenshots about the feature request here.
```

## 📝 Documentation Contributions

- **README.md**: Main documentation and usage guide
- **INSTALL.md**: Installation instructions
- **API.md**: API documentation (if created)
- **Code Comments**: Inline documentation
- **Docstrings**: Function and class documentation

## 🏗️ Development Workflow

### Setting Up Development Environment

1. **Install development dependencies**:
   ```bash
   pip install black flake8 mypy  # Code formatting and linting
   ```

2. **Configure your editor** for Python development:
   - Enable PEP 8 checking
   - Set up automatic formatting (Black)
   - Enable type checking (MyPy)

### Code Review Process

1. **Self-review** your code before submitting
2. **Address feedback** from reviewers promptly
3. **Update documentation** if needed
4. **Rebase** your branch if requested
5. **Squash commits** if requested

### Release Process

1. **Version numbering**: Follow Semantic Versioning (SemVer)
2. **Changelog**: Update CHANGELOG.md
3. **Testing**: Comprehensive testing before release
4. **Documentation**: Update version-specific documentation

## 🎯 Areas Where We Need Help

Current areas where contributions are especially welcome:

- **Cross-platform testing** (Windows, macOS, Linux)
- **Error handling improvements**
- **Performance optimizations**
- **UI/UX enhancements**
- **Documentation improvements**
- **Automated testing framework**
- **Configuration validation**
- **Accessibility improvements**

## 📞 Getting Help

If you need help while contributing:

1. **Check existing documentation** first
2. **Search closed issues** for similar questions
3. **Create a discussion** on GitHub Discussions
4. **Join our community** (if applicable)

## 🏆 Recognition

Contributors will be recognized in:

- **README.md** contributors section
- **CHANGELOG.md** for significant contributions
- **GitHub** contributors page
- **Release notes** for major contributions

## 📋 Code of Conduct

### Our Pledge

We are committed to making participation in this project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment include:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team. All complaints will be reviewed and investigated promptly and fairly.

## 📜 License

By contributing to this project, you agree that your contributions will be licensed under the same MIT License that covers the project.

---

**Thank you for contributing to RedCat Coupon Assigner!** 🎉

Your contributions help make this tool better for everyone in the community.