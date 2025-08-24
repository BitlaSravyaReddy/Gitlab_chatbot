# utils/compare_handbook_versions.py

from pathlib import Path
from difflib import SequenceMatcher

file1 = Path("Final_partitions_of_Gitlab_chatbot/Part1/Data_Acquisition/raw_data/Handbook/handbook_cleaned.txt")
file2 = Path("Final_partitions_of_Gitlab_chatbot/Part1/data/handbook_cleaned_FULL.txt")

def load_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

text1 = load_text(file1)
text2 = load_text(file2)

lines1 = text1.splitlines()
lines2 = text2.splitlines()

words1 = text1.split()
words2 = text2.split()

print("🔍 Basic Stats:")
print(f"{file1.name}: {len(lines1)} lines | {len(words1)} words")
print(f"{file2.name}: {len(lines2)} lines | {len(words2)} words")

# Unique section headers
headers1 = set(line for line in lines1 if line.startswith("## SECTION:"))
headers2 = set(line for line in lines2 if line.startswith("## SECTION:"))

print("\n📁 Section Header Comparison:")
print(f"{file1.name}: {len(headers1)} sections")
print(f"{file2.name}: {len(headers2)} sections")
print(f"New sections added in FULL: {len(headers2 - headers1)}")

# Paragraph-level uniqueness (basic)
paras1 = set(text1.split("\n\n"))
paras2 = set(text2.split("\n\n"))

common = paras1 & paras2
only_in_file1 = paras1 - paras2
only_in_file2 = paras2 - paras1

print("\n📄 Paragraph-Level Comparison:")
print(f"Common Paragraphs: {len(common)}")
print(f"Unique in {file1.name}: {len(only_in_file1)}")
print(f"Unique in {file2.name}: {len(only_in_file2)}")

# Overall similarity (optional)
similarity = SequenceMatcher(None, text1, text2).ratio()
print(f"\n📊 Overall Text Similarity Score: {similarity:.4f}")
