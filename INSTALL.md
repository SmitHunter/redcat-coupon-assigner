# Installation Guide

This guide provides detailed instructions for installing and setting up the RedCat Coupon Assigner on different platforms.

## System Requirements

### Minimum Requirements
- **Operating System**: Windows 10, macOS 10.14, or Linux Ubuntu 18.04+ (or equivalent)
- **Python**: Version 3.8 or higher
- **RAM**: 512 MB available memory
- **Storage**: 50 MB free disk space
- **Network**: Internet connection for API access

### Recommended Requirements
- **Python**: Version 3.10 or higher
- **RAM**: 1 GB available memory
- **Display**: 1024x768 resolution or higher

## Installation Methods

### Method 1: Git Clone (Recommended)

1. **Install Git** (if not already installed):
   - Windows: Download from [git-scm.com](https://git-scm.com/download/win)
   - macOS: Install via Xcode Command Line Tools or Homebrew
   - Linux: `sudo apt install git` (Ubuntu/Debian) or equivalent

2. **Clone the repository**:
   ```bash
   git clone https://github.com/SmitHunter/redcat-coupon-assigner.git
   cd redcat-coupon-assigner
   ```

### Method 2: Download ZIP

1. Go to [https://github.com/SmitHunter/redcat-coupon-assigner](https://github.com/SmitHunter/redcat-coupon-assigner)
2. Click the "Code" button and select "Download ZIP"
3. Extract the ZIP file to your desired location
4. Open a terminal/command prompt in the extracted folder

## Python Installation

### Windows

1. **Download Python**:
   - Visit [python.org](https://www.python.org/downloads/)
   - Download Python 3.10+ for Windows
   - **Important**: Check "Add Python to PATH" during installation

2. **Verify installation**:
   ```cmd
   python --version
   pip --version
   ```

### macOS

1. **Using Homebrew (Recommended)**:
   ```bash
   brew install python
   ```

2. **Using official installer**:
   - Download from [python.org](https://www.python.org/downloads/macos/)
   - Run the installer

3. **Verify installation**:
   ```bash
   python3 --version
   pip3 --version
   ```

### Linux

1. **Ubuntu/Debian**:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-tk
   ```

2. **CentOS/RHEL/Fedora**:
   ```bash
   sudo yum install python3 python3-pip tkinter
   # or for newer versions:
   sudo dnf install python3 python3-pip python3-tkinter
   ```

3. **Verify installation**:
   ```bash
   python3 --version
   pip3 --version
   ```

## Dependency Installation

1. **Navigate to the project directory**:
   ```bash
   cd redcat-coupon-assigner
   ```

2. **Install required packages**:
   
   **Windows**:
   ```cmd
   pip install -r requirements.txt
   ```
   
   **macOS/Linux**:
   ```bash
   pip3 install -r requirements.txt
   ```

## Configuration Setup

1. **Copy the configuration template**:
   ```bash
   cp config.json config.json.backup
   ```

2. **Edit the configuration**:
   Open `config.json` in your preferred text editor and update:
   ```json
   {
       "api": {
           "base_url": "https://your-redcat-api-endpoint.com/api/v1",
           "auth_type": "U"
       }
   }
   ```

3. **Save the configuration** and close the editor.

## Testing the Installation

1. **Run the application**:
   
   **Windows**:
   ```cmd
   python main.py
   ```
   
   **macOS/Linux**:
   ```bash
   python3 main.py
   ```

2. **Verify the interface**:
   - The application window should appear
   - You should see the dark-themed interface
   - All sections should be visible and properly formatted

3. **Test basic functionality**:
   - Try entering credentials (don't need to be real for UI testing)
   - Enter a sample coupon ID and member ID
   - The interface should respond to input

## Troubleshooting Installation Issues

### Python Not Found

**Issue**: `python: command not found` or `python3: command not found`

**Solutions**:
- **Windows**: Reinstall Python with "Add to PATH" checked
- **macOS**: Use `python3` instead of `python`
- **Linux**: Install Python3 using your package manager

### Permission Errors

**Issue**: Permission denied when installing packages

**Solutions**:
- **All platforms**: Use `--user` flag: `pip install --user -r requirements.txt`
- **Linux/macOS**: Use virtual environment (see below)
- **Windows**: Run Command Prompt as Administrator

### GUI Not Displaying

**Issue**: Application starts but no window appears

**Solutions**:
- **Linux**: Install tkinter: `sudo apt install python3-tk`
- **All platforms**: Ensure you have a display environment
- **Remote servers**: Use X11 forwarding or VNC

### Module Import Errors

**Issue**: `ModuleNotFoundError` when running the application

**Solutions**:
1. Verify all dependencies installed: `pip list`
2. Reinstall requirements: `pip install --force-reinstall -r requirements.txt`
3. Check Python version: `python --version`

## Virtual Environment Setup (Optional but Recommended)

Using a virtual environment isolates the project dependencies:

1. **Create virtual environment**:
   ```bash
   python -m venv redcat-env
   ```

2. **Activate the environment**:
   
   **Windows**:
   ```cmd
   redcat-env\Scripts\activate
   ```
   
   **macOS/Linux**:
   ```bash
   source redcat-env/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python main.py
   ```

5. **Deactivate when done**:
   ```bash
   deactivate
   ```

## Creating Desktop Shortcuts

### Windows

1. Right-click on desktop → New → Shortcut
2. Browse to your Python executable and add: `"C:\Python310\python.exe" "C:\path\to\redcat-coupon-assigner\main.py"`
3. Name it "RedCat Coupon Assigner"
4. Optionally, change the icon

### macOS

1. Open Automator
2. Create new Application
3. Add "Run Shell Script" action
4. Enter: `cd /path/to/redcat-coupon-assigner && python3 main.py`
5. Save as "RedCat Coupon Assigner.app"

### Linux

Create a `.desktop` file:
```ini
[Desktop Entry]
Name=RedCat Coupon Assigner
Comment=Assign coupons to RedCat members
Exec=python3 /path/to/redcat-coupon-assigner/main.py
Icon=/path/to/redcat-coupon-assigner/icon.png
Terminal=false
Type=Application
Categories=Office;
```

## Updating the Application

1. **Using Git**:
   ```bash
   git pull origin main
   pip install -r requirements.txt
   ```

2. **Manual update**:
   - Download the latest version
   - Replace old files (keep your `config.json`)
   - Reinstall dependencies if needed

## Uninstallation

1. **Remove the application folder**:
   ```bash
   rm -rf redcat-coupon-assigner
   ```

2. **Remove Python packages** (if using virtual environment):
   ```bash
   rm -rf redcat-env
   ```

3. **System-wide cleanup** (optional):
   ```bash
   pip uninstall customtkinter requests
   ```

## Getting Help

If you encounter issues during installation:

1. Check the [Troubleshooting section](README.md#troubleshooting) in the main README
2. Search for similar issues in the [GitHub Issues](https://github.com/SmitHunter/redcat-coupon-assigner/issues)
3. Create a new issue with:
   - Your operating system and version
   - Python version (`python --version`)
   - Complete error messages
   - Steps you've already tried

---

**Need additional help?** Open an issue on GitHub with detailed information about your setup and the problem you're experiencing.