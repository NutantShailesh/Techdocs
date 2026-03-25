import os
import re
import ipaddress

# --- CONFIGURATION ---
DOCS_DIR = 'docs'

# Regex Patterns
EMAIL_PATTERN = r'\b([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)\b'
IP_PATTERN = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
UUID_PATTERN = r'\b([0-9a-fA-F]{4})[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{8}([0-9a-fA-F]{4})\b'

def handle_email(match):
    full_email = match.group(0)
    user_part = match.group(1)
    domain_part = match.group(2)
    
    # 1. Skip Nutanix emails
    if domain_part.lower() == 'nutanix.com':
        return full_email
    
    # 2. Mask other emails (e.g., s***a@gmail.com)
    # We use '*' so it no longer matches the EMAIL_PATTERN (no infinite loop!)
    masked_user = f"{user_part[0]}***{user_part[-1]}" if len(user_part) > 2 else "***"
    return f"{masked_user}@{domain_part}"

def handle_ip(match):
    ip_str = match.group(0)
    try:
        ip_obj = ipaddress.ip_address(ip_str)
        # 3. Private IPs -> Full Redaction
        if ip_obj.is_private:
            return "[PRIVATE_IP_HIDDEN]"
        
        # 4. Public IPs -> Partial Masking (e.g., 8.x.x.8)
        parts = ip_str.split('.')
        return f"{parts[0]}.x.x.{parts[3]}"
    except ValueError:
        return ip_str

def handle_uuid(match):
    # 5. Mask UUIDs (e.g., 550e...0000)
    # This structure breaks the 8-4-4-4-12 pattern, so it won't be re-scrubbed.
    start = match.group(1)
    end = match.group(2)
    return f"{start}****-****-****-{end}"

def scrub_content(text):
    # Apply the handlers
    text = re.sub(EMAIL_PATTERN, handle_email, text)
    text = re.sub(IP_PATTERN, handle_ip, text)
    text = re.sub(UUID_PATTERN, handle_uuid, text)
    return text

def walk_and_scrub():
    print("🛡️ Starting Smart PII Scrubber...")
    count = 0
    if not os.path.exists(DOCS_DIR):
        print(f"❌ Error: Folder '{DOCS_DIR}' not found!")
        return

    for root, dirs, files in os.walk(DOCS_DIR):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                clean_content = scrub_content(content)
                
                if content != clean_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(clean_content)
                    print(f"✅ Sanitized: {file_path}")
                    count += 1
    print(f"✨ Finished! {count} files were processed.")

if __name__ == "__main__":
    walk_and_scrub()