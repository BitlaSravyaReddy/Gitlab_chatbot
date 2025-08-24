# utils/merge_clean_direction_files.py

from pathlib import Path
import re

# Input files
file1 = Path("Final_partitions_of_Gitlab_chatbot/Part1/Data_Acquisition/raw_data/Direction/direction_cleaned.txt")  # Clean but might miss extras
file2 = Path("Final_partitions_of_Gitlab_chatbot/Part1/Data_Acquisition/raw_data/Direction/raw_direction.txt")                # Raw dump with possibly missed parts

# Output file
output = Path("Final_partitions_of_Gitlab_chatbot/Part1/data/Direction/direction_final.txt")
output.parent.mkdir(exist_ok=True)

def clean_paragraph(para: str) -> str:
    para = para.strip()
    para = re.sub(r"\s+", " ", para)  # Normalize whitespace
    para = re.sub(r"©.*GitLab.*|Edit this page|Contact us|Get free trial", "", para, flags=re.IGNORECASE)
    para = para.strip("•")  # Clean bullets
    return para.strip()

def get_cleaned_paragraphs(text: str) -> set:
    paras = text.split("\n\n")
    return set(clean_paragraph(p) for p in paras if len(clean_paragraph(p)) > 50)

# Load and process both files
text1 = file1.read_text(encoding="utf-8")
text2 = file2.read_text(encoding="utf-8")

paras1 = get_cleaned_paragraphs(text1)
paras2 = get_cleaned_paragraphs(text2)

# Merge and deduplicate
merged_paras = sorted(paras1.union(paras2))

# Write final output
with open(output, "w", encoding="utf-8") as f:
    f.write("## SECTION: GitLab Direction (Enhanced)\n\n")
    f.write("\n\n".join(merged_paras))

print(f"✅ Final merged Direction file saved to: {output}")
print(f"📄 Total unique, cleaned paragraphs: {len(merged_paras)}")
