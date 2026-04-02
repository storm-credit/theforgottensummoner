import os
import glob

folder = r"C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 백과 (Hero Archive)\01-14-2. 현존 영웅\7. 무소속 영웅"
files = glob.glob(os.path.join(folder, "*.md"))

for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "범대륙 마도 방랑자 도감" in content:
        content = content.replace("범대륙 마도 방랑자 도감", "범대륙 방랑자 도감")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

print("Title fixed.")
