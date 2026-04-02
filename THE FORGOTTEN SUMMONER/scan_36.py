import os
import re

base_dir = r"c:\Users\Storm 시크릿\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-36. 주술 백과"
# Fix the user path
base_dir = r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-36. 주술 백과"

pattern = re.compile(r'(패시브|액티브|스킬|버프|디버프|쿨타임|어그로|경험치|업그레이드|시스템|스탯|유저|에러|오류|에너지|출력|튜토리얼|해킹|서버|무적|기믹|데이터|모터|엔진|배터리|텔레포트|포탈|마나|초능력|포스|마도|주화입마|레벨)')

found_words = set()
for root, dirs, files in os.walk(base_dir):
    for filename in files:
        if filename.endswith(".md"):
            filepath = os.path.join(root, filename)
            try:
                content = None
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                matches = pattern.findall(content)
                found_words.update(matches)
            except Exception as e:
                pass

with open("scan_results_36.txt", "w", encoding="utf-8") as f:
    f.write("Found words: " + ", ".join(found_words))
