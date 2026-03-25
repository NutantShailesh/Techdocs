import os
import re

# --- CONFIGURATION ---
DOCS_DIR = 'docs'

# Regex Patterns for PII
# This catches standard email formats
EMAIL_PATTERN = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
# This catches 36-character UUIDs (8-4-4-4-12 format)
UUID_PATTERN = r'[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'

def scrub_content(text):
    # 1. Redact Emails
    # Replaces actual emails with a placeholder
    text = re.sub(EMAIL_PATTERN, '[name@example.com]', text)
    
    # 2. Redact UUIDs/System IDs
    # Replaces unique IDs with a zeroed-out version
    text = re.sub(UUID_PATTERN, '[00000000-0000-0000-0000-000000000000]', text)
    
    return text

def walk_and_scrub():
    print("🛡️ Starting PII Redaction (Emails & UUIDs)...")
    count = 0
    
    # Walk through the docs directory
    if not os.path.exists(DOCS_DIR):
        print(f"❌ Error: Folder '{DOCS_DIR}' not found!")
        return

    for root, dirs, files in os.walk(DOCS_DIR):
        for file in files:
            # IMPORTANT: The file MUST end in .md to be processed
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                clean_content = scrub_content(content)
                
                # Only save if something actually changed
                if content != clean_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(clean_content)
                    print(f"✅ Redacted PII in: {file_path}")
                    count += 1
    
    print(f"✨ Finished! {count} files were sanitized.")

if __name__ == "__main__":
    walk_and_scrub()