import os, re
target_dir = r'C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-37. 소환 백과'
pattern = re.compile(r'(패시브|버프|디버프|쿨타임|어그로|경험치|업그레이드|시스템|스탯|유저|에러|오류|에너지|출력|튜토리얼|해킹|서버|무적|기믹|데이터|모터|엔진|배터리|텔레포트|포탈|마나|초능력|포스|마도)')
with open('debug_37.txt', 'w', encoding='utf-8') as out:
    for root, dirs, files in os.walk(target_dir):
        for filename in files:
            if filename.endswith('.md'):
                filepath = os.path.join(root, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    matches = list(set(pattern.findall(content)))
                    if matches:
                        out.write(f'{filename} -> {matches}\n')
                except: pass
