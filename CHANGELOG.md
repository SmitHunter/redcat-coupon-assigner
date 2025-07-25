# Changelog

All notable changes to the RedCat Coupon Assigner will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial release preparation
- GitHub repository setup
- Documentation improvements

## [1.0.0] - 2024-07-25

### Added
- **Core Functionality**
  - Bulk coupon assignment to multiple members
  - Support for duplicate coupon assignments
  - Configurable quantity per member
  - Real-time progress tracking during assignments
  - Comprehensive error handling and validation

- **User Interface**
  - Modern dark-themed interface using CustomTkinter
  - Responsive design with resizable windows
  - Scrollable content for better usability
  - Real-time activity logging with timestamps
  - Progress bar for batch operations

- **API Integration**
  - Support for RedCat API authentication
  - Multiple assignment endpoints (create/schedule)
  - Token-based authentication
  - Automatic retry logic for failed requests
  - Comprehensive error handling for API responses

- **Configuration System**
  - JSON-based configuration file
  - Customizable API endpoints
  - UI customization options
  - Feature toggles for advanced functionality

- **Advanced Features**
  - Batch processing with progress callbacks
  - Multi-line member ID input support
  - Input validation and sanitization
  - Threading for non-blocking UI operations
  - Detailed logging and error reporting

- **Documentation**
  - Comprehensive README with usage examples
  - Detailed installation guide (INSTALL.md)
  - Contributing guidelines (CONTRIBUTING.md)
  - API integration documentation
  - Troubleshooting guides

- **Development Infrastructure**
  - Git repository initialization
  - Requirements specification
  - MIT License
  - Code organization and structure
  - Documentation templates

### Technical Details
- **Python Version**: 3.8+ support
- **UI Framework**: CustomTkinter 5.2.0+
- **HTTP Client**: Requests 2.31.0+
- **Architecture**: Single-file application with modular functions
- **Threading**: Background processing for API calls
- **Error Handling**: Comprehensive exception handling and user feedback

### Security
- Secure credential handling (password masking)
- Token-based API authentication
- Input validation to prevent injection attacks
- No credentials stored in configuration files

### Performance
- Efficient batch processing algorithms
- Non-blocking UI operations
- Progress tracking for long-running operations
- Memory-efficient handling of large member lists

### Compatibility
- **Windows**: Windows 10+ support
- **macOS**: macOS 10.14+ support
- **Linux**: Ubuntu 18.04+ and equivalent distributions

---

## Version History Summary

- **v1.0.0**: Initial release with full coupon assignment functionality
- **Future releases**: See [Unreleased] section above

## Migration Notes

### From Original VANTA Tools
If migrating from the original VANTA Tools coupon assigner:

1. **Configuration**: Update your `config.json` with the new format
2. **Dependencies**: Install the standalone requirements
3. **API Endpoints**: Verify your API endpoint configuration
4. **Features**: New features like duplicate handling and batch processing are now available

## Breaking Changes

None in initial release.

## Deprecation Notices

None in initial release.

## Known Issues

### Current Limitations
- Maximum batch size limited by API rate limiting
- No offline mode support
- Limited to RedCat API integration

### Planned Improvements
- Automated testing framework
- Export/import functionality for member lists
- Enhanced error recovery mechanisms
- Performance optimizations for very large batches

## Support and Compatibility

### Supported Python Versions
- Python 3.8+
- Python 3.9 (recommended)
- Python 3.10 (recommended)
- Python 3.11 (tested)

### Supported Platforms
- Windows 10/11
- macOS 10.14+ (Mojave and later)
- Linux (Ubuntu 18.04+, CentOS 7+, Fedora 32+)

### API Compatibility
- RedCat API v1
- Authentication: Token-based (auth_type: "U")
- Endpoints: `/login`, `/coupons/{id}/create`, `/coupons/{id}/schedule`

---

**For detailed information about any release, please refer to the corresponding GitHub release notes and documentation.**