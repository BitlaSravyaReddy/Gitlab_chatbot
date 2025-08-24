# utils/extract_gitlab_direction_single.py

import requests
from bs4 import BeautifulSoup
import os

url = "https://about.gitlab.com/direction/"
output_file = "Final_partitions_of_Gitlab_chatbot/Part1/data/Direction/direction_cleaned.txt"

os.makedirs("Final_partitions_of_Gitlab_chatbot/Part1/data/Direction", exist_ok=True)

def clean_html(html):
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "footer", "header", "nav"]):
        tag.decompose()
    return soup.get_text(separator="\n", strip=True)

response = requests.get(url)
response.raise_for_status()

cleaned_text = clean_html(response.text)

with open(output_file, "w", encoding="utf-8") as f:
    f.write("## SECTION: GitLab Direction Main Page\n\n")
    f.write(cleaned_text)

print(f"✅ Saved cleaned Direction content to: {output_file}")
