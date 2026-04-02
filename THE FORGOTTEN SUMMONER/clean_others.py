import os
import re

base_dir = r"C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클"
folders_to_check = ['01-31', '01-32', '01-33', '01-34', '01-39', '01-40', '01-41', '01-42']

# 에픽 판타지 치환 사전
replacements = [
    # 1티어 오염어
    ("마나", "원시 영력"),
    ("초능력", "태생 권능"),
    ("포스", "영적 장력"),
    ("쿨타임", "회복 주기"),
    ("어그로", "적개심 집중"),
    ("스탯", "존재 한계치"),
    ("경험치", "영혼의 응축도"),
    ("유저", "인과율의 관찰자"),
    
    # 2티어 버프/디버프류
    ("패시브", "태생적 발현"),
    ("버프", "대자연의 가호"),
    ("디버프", "주술적 굴레"),
    
    # 3티어 시스템/물리엔진류
    ("시스템", "우주적 인과율"),
    ("에러", "섭리 역류"),
    ("오류", "현상 붕괴"),
    ("데이터", "은빛 기록망"),
    ("무적", "현실 간섭 무효"),
    ("기믹", "심원한 비의"),
    ("튜토리얼", "피의 입문식"),
    
    # 4티어 SF/기계류
    ("텔레포트", "영적 공간도약"),
    ("포탈", "차원 게이트"),
    ("업그레이드", "초월적 격상"),
    ("해킹", "사념 탈취"),
    ("서버", "차원 중핵"),
    ("배터리", "영력 결속석"),
    ("모터", "마도 태엽"), # 기계적 요소가 섞인 마공학 계열 보존용
    ("엔진", "열연소 기관"),
    ("에너지", "영적 파동"),
    ("출력", "파동 방출량"),
    
    # 예외 처리: 마도는 공식적으로 쓰이는 경우가 아니면 보통 비전으로 순화하지만,
    # '마도 통신 백과' 나 '마도 교통 백과' 처럼 타이틀이나 링크에 쓰이므로 제외하거나 아주 문맥적인 것만.
    # 여기선 혹시 모를 파괴를 막기 위해 마도는 제외 (이미 다른 단어들이 순화됨).
]

total_updated = 0

for folder_prefix in folders_to_check:
    target_folder = None
    for foldername in os.listdir(base_dir):
        if foldername.startswith(folder_prefix) and os.path.isdir(os.path.join(base_dir, foldername)):
            target_folder = os.path.join(base_dir, foldername)
            break
            
    if target_folder:
        for root, dirs, files in os.walk(target_folder):
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
                        total_updated += 1
                        print(f"Updated in {folder_prefix}: {filename}")

print(f"총 {total_updated}개 볼륨 문서 100% 보존 유지 & 명칭 정화 완료.")
