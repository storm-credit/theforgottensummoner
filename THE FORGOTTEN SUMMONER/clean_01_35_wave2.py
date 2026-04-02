import os

base_dir = r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-35. 마법 공학 백과"

replacements = [
    # Wave 2 terms
    ("무적", "물리 간섭 무효"),
    ("싱크로율", "영혼 감응 결속률"),
    ("싱크로", "영적 동기화"),
    ("기믹", "비밀스러운 섭리"),
    ("출력", "에테르 방출량"),
    ("에러", "동력 역류"),
    ("해킹", "결계 침식"),
    ("서버", "거대 마나 중핵"),
    ("사이버", "비전 연성"),
    ("에너지", "에테르 진액"),
    ("업그레이드", "형상 진화"),
    ("유저", "인과율의 자식"),
    ("스킬", "고유 권능"),
    ("버프", "성스러운 축복"),
    ("다운로드", "영지 흡수"),
    ("네트워크", "사념의 그물망"),
    ("튜토리얼", "입문 의식")
]

for root, dirs, files in os.walk(base_dir):
    for filename in files:
        if filename.endswith(".md"):
            filepath = os.path.join(root, filename)
            
            # Trying different encodings
            content = None
            encodings_to_try = ['utf-8', 'utf-8-sig', 'cp949', 'euc-kr']
            used_encoding = 'utf-8'
            for enc in encodings_to_try:
                try:
                    with open(filepath, 'r', encoding=enc) as f:
                        content = f.read()
                    used_encoding = enc
                    break
                except UnicodeDecodeError:
                    continue
            
            if content is None:
                # specifically for corrupt files
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
                        content = f.read()
                except Exception as e:
                    print(f"Skipping completely {filename}: {e}")
                    continue

            original_content = content
            for old_text, new_text in replacements:
                content = content.replace(old_text, new_text)
                
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated (Wave 2): {filename}")

print("01-35. 마법 공학 백과 2차(Wave 2) 정화 루틴 완료.")
