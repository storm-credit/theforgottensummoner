import re

file_path = r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-35. 마법 공학 백과\마법 공학 도감\6-4. 강철 의체 (Steel Prosthetics).md"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines):
        # Find lines that look like table rows with lots of broken single words
        if "|" in line and sum(1 for c in line if "\uac00" <= c <= "\ud7a3") > 10:
            # Let's just find lines with 5 consecutive spaces between Korean characters
            if re.search(r'([가-힣]\s){5,}', line) or "콕핏" in line or "Madman" in line or "5기어" in line:
                print(f"L{i+1}: {line.strip()}")

except Exception as e:
    print(f"Error: {e}")
