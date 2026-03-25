import os
import re

# --- CONFIGURATION ---
# Define the directory to scrub
DOCS_DIR = 'docs'

# Define the replacement pairs (Forbidden Word: Replacement)
INCLUSIVE_MAP = {
    r'\bmaster\b': 'primary',
    r'\bslave\b': 'secondary',
    r'\bwhitelist\b': 'allowlist',
    r'\bblacklist\b': 'blocklist'
}

# Regex Patterns for PII
EMAIL_PATTERN = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
UUID_PATTERN = r'[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'

def scrub_content(text):
    # 1. Replace Non-Inclusive Language (Case-Insensitive)
    for pattern, replacement in INCLUSIVE_MAP.items():
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    
    # 2. Redact Emails
    text = re.sub(EMAIL_PATTERN, '[name@example.com]', text)
    
    # 3. Redact UUIDs/System IDs
    text = re.sub(UUID_PATTERN, '[00000000-0000-0000-0000-000000000000]', text)
    
    return text

def walk_and_scrub():
    print("🚀 Starting Documentation Scrubbing...")
    count = 0
    
    # Walk through the docs directory recursively
    for root, dirs, files in os.walk(DOCS_DIR):
        for file in files:
            # Only process Markdown files
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Perform the cleaning
                clean_content = scrub_content(content)
                
                # Only write back if changes were actually made
                if content != clean_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(clean_content)
                    print(f"✅ Scrubbed: {file_path}")
                    count += 1
    
    print(f"✨ Finished! {count} files were sanitized.")

if __name__ == "__main__":
    walk_and_scrub()