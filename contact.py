import json
from datetime import datetime
 
REQUIRED_FIELDS = ["name", "email", "message"]
MAX_MESSAGE_LENGTH = 500
 
def validate_form(data):
    for field in REQUIRED_FIELDS:
        if not data.get(field):
            return False, f"{field} is required"
    if len(data["message"]) > MAX_MESSAGE_LENGTH:
        return False, "Message is too long"
    return True, "OK"
 
def process_contact_form(form_data):
    is_valid, error = validate_form(form_data)
    if not is_valid:
        return {"success": False, "error": error}
 
    name      = form_data["name"]
    email     = form_data["email"]
    message   = form_data["message"]
    timestamp = datetime.now().isoformat()
 
    return {"success": True, "name": name, "email": email, "timestamp": timestamp}
 
if __name__ == "__main__":
    test = {"name": "Bilal", "email": "bilal@example.com", "message": "Hello team!"}
    print(json.dumps(process_contact_form(test), indent=2))
