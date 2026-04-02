import os

base_dir = r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-35. 마법 공학 백과"

replacements = [
    # System / Sci-fi meta
    ("패시브 부활", "태생적 영혼 복귀"),
    ("패시브", "태생적 발현"),
    ("스텔스 크롤링", "영적 은신 기동"),
    ("스텔스 모드", "인과율 차단 형태"),
    ("스텔스", "영적 은신"),
    ("오버클럭", "마나 혈관 폭주"),
    ("오버드라이브 워커", "초출력 영魂 연소 기동"),
    ("오버드라이브", "강제 한계 돌파"),
    ("부스터", "에테르 추진"),
    ("캔슬 코팅", "영적 상쇄 도포"),
    ("캔슬", "영적 상쇄"),
    ("엔진 과부하", "동력로 과부하"),
    ("엔진", "동력로"),
    ("모터", "마나 펌프"),
    ("배터리", "동력 코어"),
    ("플라즈마", "초고열 에테르 진액"),
    ("홀로그램", "마력 투영"),
    ("블랙홀", "의 차원 붕괴 구렁"),
    
    # Weapons / Units
    ("레이저 강선", "광자 궤적"),
    ("레이저", "섬광 궤적"),
    ("빔 안구", "광자 안구"),
    ("빔", "에테르 섬광"),
    ("로봇", "강철 오토마타"),
    ("안드로이드", "기동 성물"),
    ("메카니카", "기계 거신"),
    ("메카니스트", "마동 기공사"),
    ("메카", "거대 병기"),

    # Generic B-tier RPG terms not fully purged
    ("텔레포트", "공간 도약"),
    ("포탈", "차원 회랑"),
    ("데이터", "별의 궤적"),
    ("시스템", "우주적 섭리"),
    ("스탯창", "영적 섭리창"),
    ("스탯", "고유 역량"),
    ("경험치", "치열한 궤적"),
    ("어그로", "증오의 시선")
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
                print(f"Skipping {filename}: Could not decode.")
                continue

            original_content = content
            for old_text, new_text in replacements:
                content = content.replace(old_text, new_text)
                
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f: # Save back as pure utf-8
                    f.write(content)
                print(f"Updated: {filename} (from {used_encoding})")

print("01-35. 마법 공학 백과 정화 루틴 완료.")
