import os
import re

target_dir = r"C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-37. 소환 백과"

replacements = [
    ("마나", "영적 생명력"),
    ("패시브", "태생적 발현"),
    ("버프", "차원 영령의 가호"),
    ("디버프", "차원 굴레"),
    ("시스템", "우주적 인과율"),
    ("데이터", "영혼의 궤적"),
    ("에너지", "영적 파동"),
    ("출력", "소환 방출량"),
    ("기믹", "차원적 비의"),
    ("무적", "현실 간섭 무효"),
    ("오류", "차원 붕괴 현상"),
    ("에러", "섭리 역류"),
    ("배터리", "영혼 결속석"),
    ("엔진", "심장 연소로"),
    ("사이버", "비전(Arcane)"),
    ("마도", "비전"),
    ("스킬", "태생 권능"),
    ("어그로", "영적 증오 집중"),
    ("경험치", "영혼의 응축"),
    ("업그레이드", "격상"),
    ("스탯", "존재 한계치"),
    ("유저", "인과율의 존재"),
    ("튜토리얼", "피의 입문식"),
    ("해킹", "사념 강탈"),
    ("서버", "차원 중핵"),
    ("텔레포트", "영적 공간도약"),
    ("포탈", "차원 균열"),
    ("포스", "차원 장력"),
    ("모터", "마력 태엽")
]

for root, dirs, files in os.walk(target_dir):
    for filename in files:
        if filename.endswith(".md"):
            filepath = os.path.join(root, filename)
            
            content = None
            for enc in ['utf-8', 'utf-8-sig', 'cp949', 'euc-kr']:
                try:
                    with open(filepath, 'r', encoding=enc) as f:
                        content = f.read()
                    break
                except UnicodeDecodeError:
                    continue
            if content is None:
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                except:
                    continue

            original_content = content
            for old_text, new_text in replacements:
                content = content.replace(old_text, new_text)
                
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated: {filename}")

print("01-37 소환 백과 정화 완료.")
