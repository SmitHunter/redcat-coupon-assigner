# RedCat Coupon Assigner

**A desktop GUI application for bulk coupon assignment through the RedCat API.**

Efficiently assign coupons to multiple members at once with progress tracking and duplicate support.

## Quick Start

1. **Install Python 3.8+** and dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure your API endpoint** in `config.json`:
   ```json
   {
       "api": {
           "base_url": "https://your-redcat-api.com/api/v1"
       }
   }
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

## Usage

1. Enter your API username and password
2. Enter the coupon ID to assign
3. Enter member IDs (comma-separated)
4. Optionally set quantity per member and duplicate settings
5. Click "Assign Coupons"

## Features

- Bulk coupon assignment to multiple members
- Support for multiple coupons per member
- Real-time progress tracking
- Input validation and error handling
- Dark-themed, resizable interface

## Configuration

Edit `config.json` to customize:
- API endpoint URL
- UI settings (window size, title)
- Feature toggles (duplicates, batch processing)

## Files

- `main.py` - Main application
- `config.json` - Configuration settings
- `requirements.txt` - Python dependencies