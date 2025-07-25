import customtkinter as ctk
import requests
import json
import os
from datetime import datetime
import threading

# --- Theme Setup ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

# --- Configuration Loading ---
def load_config():
    """Load configuration from config.json"""
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # Default configuration if file doesn't exist
        return {
            "api": {
                "base_url": "https://your-api-url.com/api/v1",
                "auth_type": "U"
            },
            "ui": {
                "window_title": "RedCat Coupon Assigner",
                "default_width": 700,
                "default_height": 800
            },
            "features": {
                "allow_duplicate_coupons": True,
                "enable_batch_processing": True,
                "max_batch_size": 1000
            }
        }

# Load configuration
CONFIG = load_config()
BASE_URL = CONFIG["api"]["base_url"]

# --- API Helpers ---
def login(username, password):
    """Authenticate with the API and return token"""
    url = f"{BASE_URL}/login"
    payload = {"username": username, "psw": password, "auth_type": CONFIG["api"]["auth_type"]}
    try:
        r = requests.post(url, json=payload)
        r.raise_for_status()
        response_data = r.json()
        if "token" not in response_data:
            raise ValueError(f"Login response missing token. Response: {response_data}")
        return response_data["token"]
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Login request failed: {e}")
    except KeyError as e:
        raise ValueError(f"Login response missing expected field: {e}. Response: {response_data}")

def assign_coupon_single(token, coupon_id, member_ids, allow_duplicates=None):
    """Assign a coupon to members using the create endpoint (single assignment)"""
    url = f"{BASE_URL}/coupons/{coupon_id}/create"
    headers = {
        "X-Redcat-Authtoken": token,
        "Content-Type": "application/json"
    }
    payload = {
        "Members": member_ids,
        "HandleErrors": True,
        "ReturnAlias": True
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

def assign_coupon_multiple(token, coupon_id, member_ids, allow_duplicates=None):
    """Assign a coupon to members using the schedule endpoint (supports duplicates)"""
    url = f"{BASE_URL}/coupons/{coupon_id}/schedule"
    headers = {
        "X-Redcat-Authtoken": token,
        "Content-Type": "application/json"
    }
    payload = {
        "Members": member_ids
    }
    
    # Add Multiple parameter if specified (for async endpoint)
    if allow_duplicates is not None:
        payload["Multiple"] = allow_duplicates
    
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

def assign_coupon_batch(token, coupon_id, member_ids, quantity=1, allow_duplicates=False, progress_callback=None):
    """Assign coupons in batches with progress tracking"""
    # Choose the appropriate endpoint based on requirements
    assign_function = assign_coupon_multiple if allow_duplicates else assign_coupon_single
    
    try:
        if progress_callback:
            progress_callback("Processing coupon assignments...")
        
        result = assign_function(token, coupon_id, member_ids, allow_duplicates)
        
        if progress_callback:
            progress_callback(f"Progress: {len(member_ids)}/{len(member_ids)} (100.0%)")
    
    except Exception as e:
        raise ValueError(f"Batch assignment failed: {e}")
    
    return [result]

# --- GUI App ---
class CouponAssignerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(CONFIG["ui"]["window_title"])
        self.geometry(f"{CONFIG['ui']['default_width']}x{CONFIG['ui']['default_height']}")
        self.configure(fg_color="#1E1E1E")
        self.resizable(True, True)
        self.minsize(500, 600)

        self.token = None
        self.is_processing = False

        # Create main scrollable container
        main_container = ctk.CTkScrollableFrame(self, fg_color="#1E1E1E")
        main_container.pack(expand=True, padx=10, pady=10, fill="both")
        
        # Main content frame inside scrollable container
        frame = ctk.CTkFrame(main_container, fg_color="#1E1E1E")
        frame.pack(expand=True, padx=10, pady=10, fill="both")

        # -- Configuration Info --
        config_frame = ctk.CTkFrame(frame, fg_color="#404040", corner_radius=10)
        config_frame.pack(pady=(10, 15), padx=20, fill="x")
        
        config_title = ctk.CTkLabel(config_frame, text="⚙️ Configuration", font=("Arial", 12, "bold"))
        config_title.pack(pady=(8, 5))
        
        config_info = ctk.CTkLabel(config_frame, 
            text=f"API: {BASE_URL}\nBatch Processing: {'Enabled' if CONFIG['features']['enable_batch_processing'] else 'Disabled'}", 
            font=("Arial", 10), justify="left", text_color="#CCCCCC")
        config_info.pack(pady=(0, 8))

        # -- Credentials Section --
        creds_frame = ctk.CTkFrame(frame, fg_color="#2B2B2B", corner_radius=10)
        creds_frame.pack(pady=10, padx=20, fill="x")
        
        creds_title = ctk.CTkLabel(creds_frame, text="🔐 Authentication", font=("Arial", 14, "bold"))
        creds_title.pack(pady=(10, 5))
        
        self.username_entry = ctk.CTkEntry(creds_frame, placeholder_text="API Username", width=300, height=35)
        self.username_entry.pack(pady=5)
        
        self.password_entry = ctk.CTkEntry(creds_frame, placeholder_text="Password", show="*", width=300, height=35)
        self.password_entry.pack(pady=(5, 15))

        # -- Coupon Assignment Section --
        assignment_frame = ctk.CTkFrame(frame, fg_color="#2B2B2B", corner_radius=10)
        assignment_frame.pack(pady=10, padx=20, fill="x")
        
        assignment_title = ctk.CTkLabel(assignment_frame, text="🎫 Coupon Assignment", font=("Arial", 14, "bold"))
        assignment_title.pack(pady=(10, 5))

        # Coupon ID input
        coupon_label = ctk.CTkLabel(assignment_frame, text="Coupon ID:", font=("Arial", 12))
        coupon_label.pack(pady=(5, 2))
        self.coupon_id_entry = ctk.CTkEntry(assignment_frame, placeholder_text="Enter coupon ID", width=300, height=35)
        self.coupon_id_entry.pack(pady=(0, 10))

        # Member IDs input
        members_label = ctk.CTkLabel(assignment_frame, text="Member IDs (comma-separated):", font=("Arial", 12))
        members_label.pack(pady=(5, 2))
        self.member_ids_entry = ctk.CTkTextbox(assignment_frame, height=100, width=500)
        self.member_ids_entry.pack(pady=(0, 10))

        # Options
        options_frame = ctk.CTkFrame(assignment_frame, fg_color="transparent")
        options_frame.pack(pady=10, fill="x")

        self.allow_duplicates_var = ctk.BooleanVar(value=CONFIG["features"]["allow_duplicate_coupons"])
        self.allow_duplicates_checkbox = ctk.CTkCheckBox(
            options_frame, 
            text="Allow duplicate coupons for same member",
            variable=self.allow_duplicates_var,
            font=("Arial", 11)
        )
        self.allow_duplicates_checkbox.pack(pady=5)

        # Add info text for the checkbox
        duplicate_info = ctk.CTkLabel(
            options_frame, 
            text="ℹ️ When checked, members can receive the same coupon multiple times",
            font=("Arial", 9), 
            text_color="#888888"
        )
        duplicate_info.pack(pady=(0, 10))

        # Action buttons
        button_frame = ctk.CTkFrame(assignment_frame, fg_color="transparent")
        button_frame.pack(pady=10, fill="x")

        self.assign_button = ctk.CTkButton(
            button_frame, 
            text="🚀 Assign Coupons", 
            command=self.handle_assign_threaded, 
            width=200, 
            height=40,
            font=("Arial", 12, "bold")
        )
        self.assign_button.pack(side="left", padx=(0, 5))

        self.clear_button = ctk.CTkButton(
            button_frame, 
            text="🗑️ Clear", 
            command=self.clear_fields, 
            width=100, 
            height=40,
            fg_color="#666666",
            hover_color="#555555"
        )
        self.clear_button.pack(side="left", padx=(5, 0))
        
        # Center the button frame
        button_frame.pack_configure(anchor="center")

        # Progress bar
        self.progress_bar = ctk.CTkProgressBar(assignment_frame, width=500)
        self.progress_bar.pack(pady=(10, 15))
        self.progress_bar.set(0)

        # -- Activity Log --
        log_frame = ctk.CTkFrame(frame, fg_color="#2B2B2B", corner_radius=10)
        log_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        log_title = ctk.CTkLabel(log_frame, text="📋 Activity Log", font=("Arial", 14, "bold"))
        log_title.pack(pady=(10, 5))
        
        self.output_box = ctk.CTkTextbox(log_frame, height=250, width=640, wrap="word", state="disabled")
        self.output_box.pack(pady=(0, 15), fill="both", expand=True)
        self.output_box.configure(fg_color="#0D1117", text_color="#E6EDF3", font=("Consolas", 11))

    def log(self, message):
        """Add message to the activity log with timestamp"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted_message = f"[{timestamp}] {message}"
        
        self.output_box.configure(state="normal")
        self.output_box.insert("end", formatted_message + "\n")
        self.output_box.see("end")
        self.output_box.configure(state="disabled")

    def clear_fields(self):
        """Clear all input fields"""
        self.member_ids_entry.delete("1.0", "end")
        self.coupon_id_entry.delete(0, "end")
        self.progress_bar.set(0)
        self.log("🗑️ Fields cleared")

    def update_progress(self, message):
        """Update progress bar and log message"""
        self.log(message)
        # Extract percentage if present in message
        import re
        match = re.search(r'(\d+\.\d+)%', message)
        if match:
            percentage = float(match.group(1)) / 100
            self.progress_bar.set(percentage)

    def validate_inputs(self):
        """Validate all input fields"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        coupon_id = self.coupon_id_entry.get().strip()
        member_ids_text = self.member_ids_entry.get("1.0", "end").strip()
        quantity = "1"  # Fixed quantity of 1

        if not username or not password:
            raise ValueError("Username and password are required")
        
        if not coupon_id or not coupon_id.isdigit():
            raise ValueError("Valid coupon ID is required")
        
        if not member_ids_text:
            raise ValueError("At least one member ID is required")

        # Parse member IDs
        member_ids = []
        for mid in member_ids_text.replace('\n', ',').split(','):
            mid = mid.strip()
            if mid and mid.isdigit():
                member_ids.append(int(mid))
        
        if not member_ids:
            raise ValueError("No valid member IDs found")

        return {
            'username': username,
            'password': password,
            'coupon_id': int(coupon_id),
            'member_ids': member_ids,
            'quantity': int(quantity),
            'allow_duplicates': self.allow_duplicates_var.get()
        }

    def handle_assign_threaded(self):
        """Handle coupon assignment in a separate thread"""
        if self.is_processing:
            return
        
        # Run assignment in thread to prevent UI freezing
        thread = threading.Thread(target=self.handle_assign)
        thread.daemon = True
        thread.start()

    def handle_assign(self):
        """Handle the coupon assignment process"""
        self.is_processing = True
        original_text = self.assign_button.cget("text")
        
        try:
            # Update UI to show processing state
            self.assign_button.configure(text="⏳ Processing...", state="disabled")
            self.progress_bar.set(0)
            
            # Clear previous log
            self.output_box.configure(state="normal")
            self.output_box.delete("1.0", "end")
            self.output_box.configure(state="disabled")
            
            # Validate inputs
            self.log("🔍 Validating inputs...")
            inputs = self.validate_inputs()
            
            # Login
            self.log("🔐 Authenticating...")
            token = login(inputs['username'], inputs['password'])
            self.log("✅ Authentication successful")
            
            # Assign coupons
            self.log(f"🎫 Assigning coupon {inputs['coupon_id']} to {len(inputs['member_ids'])} members...")
            self.log(f"🔄 Allow duplicates: {'Yes' if inputs['allow_duplicates'] else 'No'}")
            
            results = assign_coupon_batch(
                token, 
                inputs['coupon_id'], 
                inputs['member_ids'],
                inputs['quantity'],
                inputs['allow_duplicates'],
                self.update_progress
            )
            
            # Success
            self.progress_bar.set(1.0)
            self.log("🎉 Coupon assignment completed successfully!")
            self.log(f"📈 Total assignments processed: {len(inputs['member_ids'])}")
            
            # Log detailed results
            for i, result in enumerate(results):
                if result.get("data") == "Coupons have been scheduled for creation":
                    self.log(f"✅ Batch {i+1}: Coupons scheduled for creation")
                else:
                    self.log(f"✅ Batch {i+1}: {result}")
                    
        except Exception as e:
            self.progress_bar.set(0)
            self.log(f"❌ Error: {str(e)}")
        finally:
            # Restore button state
            self.assign_button.configure(text=original_text, state="normal")
            self.is_processing = False

# --- Main ---
if __name__ == "__main__":
    app = CouponAssignerApp()
    app.mainloop()