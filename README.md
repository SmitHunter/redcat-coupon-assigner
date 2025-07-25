# RedCat Coupon Assigner

A standalone desktop application for efficiently assigning coupons to members through the RedCat API. This tool provides a user-friendly interface for bulk coupon assignments with advanced features like duplicate handling and batch processing.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

## ✨ Features

- 🎫 **Bulk Coupon Assignment**: Assign coupons to multiple members simultaneously
- 🔄 **Duplicate Handling**: Choose whether to allow multiple coupons per member
- 📊 **Quantity Control**: Specify how many coupons to assign to each member
- 📋 **Batch Processing**: Efficient processing of large member lists
- 🌙 **Dark Theme**: Modern, eye-friendly dark interface
- 📱 **Responsive Design**: Resizable window with scrollable content
- ⏱️ **Real-time Progress**: Live progress tracking during assignments
- 📝 **Activity Logging**: Detailed logs with timestamps for all operations
- ⚙️ **Configurable**: Easy configuration through JSON file

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- RedCat API access credentials

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SmitHunter/redcat-coupon-assigner.git
   cd redcat-coupon-assigner
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the application:**
   Edit `config.json` with your API settings:
   ```json
   {
       "api": {
           "base_url": "https://your-redcat-api.com/api/v1",
           "auth_type": "U"
       }
   }
   ```

4. **Run the application:**
   ```bash
   python main.py
   ```

## 📖 Usage Guide

### Basic Coupon Assignment

1. **Launch the application** by running `python main.py`
2. **Enter your credentials** in the Authentication section
3. **Fill in the coupon details:**
   - **Coupon ID**: The ID of the coupon to assign
   - **Member IDs**: Comma-separated list of member IDs
   - **Quantity**: Number of coupons per member (default: 1)
4. **Configure options:**
   - Check "Allow duplicate coupons" if members can receive the same coupon multiple times
5. **Click "Assign Coupons"** to start the process

### Bulk Assignment Example

```
Member IDs: 1001, 1002, 1003, 1004, 1005
Coupon ID: 230
Quantity: 2
Allow duplicates: ✓
```

This will assign 2 coupons (ID: 230) to each of the 5 members, totaling 10 coupon assignments.

### Advanced Features

#### Multi-line Member Input
You can enter member IDs in various formats:
```
1001, 1002, 1003
1004
1005, 1006
```

#### Progress Tracking
The application provides real-time progress updates:
- Authentication status
- Batch processing progress
- Completion percentage
- Detailed results for each batch

#### Error Handling
Comprehensive error handling for:
- Invalid credentials
- Network connectivity issues
- Invalid member IDs
- API rate limiting
- Malformed requests

## ⚙️ Configuration

The `config.json` file allows you to customize the application:

```json
{
    "api": {
        "base_url": "https://your-redcat-api.com/api/v1",
        "auth_type": "U"
    },
    "ui": {
        "window_title": "RedCat Coupon Assigner",
        "default_width": 700,
        "default_height": 800
    },
    "features": {
        "allow_duplicate_coupons": true,
        "enable_batch_processing": true,
        "max_batch_size": 1000
    }
}
```

### Configuration Options

| Option | Description | Default |
|--------|-------------|---------|
| `api.base_url` | Your RedCat API endpoint | Required |
| `api.auth_type` | Authentication type | "U" |
| `ui.window_title` | Application window title | "RedCat Coupon Assigner" |
| `ui.default_width` | Default window width | 700 |
| `ui.default_height` | Default window height | 800 |
| `features.allow_duplicate_coupons` | Default duplicate setting | true |
| `features.enable_batch_processing` | Enable batch processing | true |
| `features.max_batch_size` | Maximum batch size | 1000 |

## 🔌 API Integration

### Authentication
The application uses token-based authentication:
```python
POST /api/v1/login
{
    "username": "your_username",
    "psw": "your_password", 
    "auth_type": "U"
}
```

### Coupon Assignment Endpoints

#### Single Assignment (No Duplicates)
```python
POST /api/v1/coupons/{coupon_id}/create
Headers: {"X-Redcat-Authtoken": "your_token"}
{
    "Members": [1001, 1002, 1003],
    "HandleErrors": true,
    "ReturnAlias": true
}
```

#### Multiple Assignments (With Duplicates)
```python
POST /api/v1/coupons/{coupon_id}/schedule
Headers: {"X-Redcat-Authtoken": "your_token"}
{
    "Members": [1001, 1002, 1003],
    "Multiple": true
}
```

## 🧪 Testing

### Manual Testing
1. Test with a small group of members first
2. Verify coupon assignments in your RedCat dashboard
3. Test both duplicate and non-duplicate scenarios
4. Test error handling with invalid data

### Input Validation
The application validates:
- Required fields (username, password, coupon ID, member IDs)
- Numeric values (coupon ID, member IDs, quantity)
- Positive integers for quantities
- Network connectivity

## 🔧 Troubleshooting

### Common Issues

**"Login failed" Error**
- Verify your username and password
- Check that the API URL in config.json is correct
- Ensure your account has proper permissions

**"No valid member IDs found" Error**
- Ensure member IDs are numeric
- Check for proper comma separation
- Remove any extra spaces or special characters

**"Network request failed" Error**
- Check your internet connection
- Verify the API endpoint is accessible
- Check for firewall or proxy restrictions

**Application won't start**
- Ensure Python 3.8+ is installed
- Install required dependencies: `pip install -r requirements.txt`
- Check that all files are present

### Debug Mode
For additional debugging information, you can modify the logging level in the code or check the activity log for detailed error messages.

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [troubleshooting section](#troubleshooting)
2. Search existing [issues](https://github.com/SmitHunter/redcat-coupon-assigner/issues)
3. Create a new issue with detailed information

## 🔄 Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed history of changes.

## 📸 Screenshots

### Main Interface
The application features a clean, dark-themed interface with clearly organized sections:
- Authentication credentials
- Coupon assignment parameters
- Options and settings
- Real-time activity log

### Features in Action
- Real-time progress tracking during bulk assignments
- Detailed logging with timestamps
- Error handling and validation feedback
- Responsive design that works on different screen sizes

---

**Made with ❤️ for efficient coupon management**