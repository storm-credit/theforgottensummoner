import os
import re

base_dir = r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-35. 마법 공학 백과"
pattern = re.compile(r'(업그레이드|유저|스킬|버프|기믹|무적|출력|에러|에너지|패치|서버|네트워크|해킹|튜토리얼|사이버|리부트|싱크로)')

found_words = set()
for root, dirs, files in os.walk(base_dir):
    for filename in files:
        if filename.endswith(".md"):
            filepath = os.path.join(root, filename)
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    matches = pattern.findall(content)
                    found_words.update(matches)
            except Exception as e:
                pass

with open("scan_results.txt", "w", encoding="utf-8") as f:
    f.write("Found B-tier words remaining: " + str(found_words))
