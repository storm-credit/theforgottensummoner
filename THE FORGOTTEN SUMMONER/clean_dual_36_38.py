import os

base_dirs = [
    r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-36. 주술 백과",
    r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-38. 동반수 백과"
]

replacements = [
    ("마나", "영적 생명력"), # Also "원시 에테르" could work, but let's go with "영적 생명력" or we can do context-dependent, but "영적 생명력" fits Shamanism and Beasts. Wait, let's use "생명력" mostly. I'll use "영적 생명력". Or "마나 감응수" -> "생명 감응수". Ah wait, the filenames like 5-9. 마나 감응수! Replacing 마나 might break the filename if I rename files, but I'm only modifying content. But the title inside will change to 생명 감응수. That's fine.
    ("패시브", "태생적 발현"),
    ("버프", "원시 정령의 가호"),
    ("디버프", "주술적 저주"),
    ("시스템", "우주의 규율"),
    ("데이터", "대자연의 궤적"),
    ("에너지", "원시 영력"),
    ("출력", "야성 방출량"),
    ("기믹", "자연의 변수"),
    ("무적", "육체 간섭 무효"),
    ("오류", "섭리 역류"),
    ("에러", "영혼망 충돌"),
    ("배터리", "영혼석"),
    ("엔진", "생명 연소로"),
    ("사이버", "주술 연성"),
    ("마도", "비전"),
    ("스킬", "고유 권능"),
    ("어그로", "살육 충동 대상"),
    ("경험치", "영적 결정체"),
    ("업그레이드", "형상 진화"),
    ("스탯", "생물학적 한계치"),
    ("유저", "인과율의 존재"),
    ("튜토리얼", "피의 입문식"),
    ("해킹", "사념 탈취"),
    ("서버", "거대 영혼 중핵"),
    ("텔레포트", "영적 공간도약"),
    ("포탈", "차원 균열")
]

for base_dir in base_dirs:
    for root, dirs, files in os.walk(base_dir):
        for filename in files:
            if filename.endswith(".md"):
                filepath = os.path.join(root, filename)
                
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
                    try:
                        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
                            content = f.read()
                    except Exception as e:
                        continue

                original_content = content
                for old_text, new_text in replacements:
                    content = content.replace(old_text, new_text)
                    
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated: {filename}")

print("01-36 & 01-38 정화 루틴 완료.")
