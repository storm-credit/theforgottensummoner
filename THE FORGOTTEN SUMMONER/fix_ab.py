import os
import glob
import re

directory = r"C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 백과 (Hero Archive)\01-14-2. 현존 영웅\6. 중립세력 (Neutral)"

count = 0
for filepath in glob.glob(directory + "/**/*.md", recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove any occurrence of: (`A-x` 연계) or (`A-x` 연계). etc
    new_content = re.sub(r'\s*\(`[A-Za-z]-[A-Za-z]` 연계\)\.*', '', content)
    
    if content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Fixed: {os.path.basename(filepath)}")

print(f"Total files fixed: {count}")
