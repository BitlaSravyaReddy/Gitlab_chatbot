# utils/extract_gitlab_handbook_safe_full.py

import os
import re
from pathlib import Path

HANDBOOK_DIR = "Final_partitions_of_Gitlab_chatbot/Part1/Data_Acquisition/raw_data/Handbook/content"
OUTPUT_FILE = "Final_partitions_of_Gitlab_chatbot/Part1/Data_Acquisition/data/Handbook/handbook_cleaned.txt"

def clean_markdown(text):
    # Remove YAML frontmatter
    text = re.sub(r"^---\s*\n.*?\n---\s*", "", text, flags=re.DOTALL | re.MULTILINE)
    # Remove image links
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)
    # Convert links to just text
    text = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", text)
    # Inline code and bold/italic
    text = re.sub(r"`{1,3}(.*?)`{1,3}", r"\1", text)
    text = re.sub(r"[*_]{1,3}", "", text)
    text = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)
    return text.strip()

def get_logical_path(root, file):
    relative_path = os.path.relpath(os.path.join(root, file), HANDBOOK_DIR)
    return relative_path.replace("\\", "/")

def extract_all_handbook():
    collected = []
    count = 0
    for root, _, files in os.walk(HANDBOOK_DIR):
        files = sorted(f for f in files if f.endswith(".md"))  # ✅ include everything
        for file in files:
            full_path = os.path.join(root, file)
            try:
                with open(full_path, "r", encoding="utf-8") as f:
                    raw = f.read()
                cleaned = clean_markdown(raw)
                section = get_logical_path(root, file)
                block = f"\n\n---\n## SECTION: {section}\n\n{cleaned}"
                collected.append(block)
                count += 1
            except Exception as e:
                print(f"❌ Failed to read {full_path}: {e}")

    print(f"✅ Processed {count} Markdown files.")
    return "\n".join(collected)

# Write to file
Path(os.path.dirname(OUTPUT_FILE)).mkdir(exist_ok=True)
output_text = extract_all_handbook()
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(output_text)

print(f"✅ Saved complete structured content to {OUTPUT_FILE}")
