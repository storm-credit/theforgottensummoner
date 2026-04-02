import os
import re

base_dirs = [
    r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-36. 주술 백과",
    r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-38. 동반수 백과"
]

pattern = re.compile(r'(패시브|버프|디버프|쿨타임|어그로|경험치|업그레이드|시스템|스탯|유저|에러|오류|에너지|출력|튜토리얼|해킹|서버|무적|기믹|데이터|모터|엔진|배터리|텔레포트|포탈|마나|초능력|포스|마도)')

found_words = set()

for base_dir in base_dirs:
    for root, dirs, files in os.walk(base_dir):
        for filename in files:
            if filename.endswith(".md"):
                filepath = os.path.join(root, filename)
                try:
                    content = None
                    encodings_to_try = ['utf-8', 'utf-8-sig', 'cp949', 'euc-kr']
                    for enc in encodings_to_try:
                        try:
                            with open(filepath, 'r', encoding=enc) as f:
                                content = f.read()
                            break
                        except UnicodeDecodeError:
                            continue
                            
                    if content is None:
                        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()

                    matches = pattern.findall(content)
                    found_words.update(matches)
                except Exception as e:
                    continue

# Write to file instead of printing due to enc conflicts
with open("scan_results_dual.txt", "w", encoding="utf-8") as f:
    f.write("Remaining Words Check: " + ", ".join(found_words))
