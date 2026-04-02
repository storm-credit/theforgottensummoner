import os
import glob

folder = r"C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 백과 (Hero Archive)\01-14-2. 현존 영웅\7. 무소속 영웅"
files = glob.glob(os.path.join(folder, "*.md"))

restorations = {
    "범대륙 방랑자 도감": "범대륙 마도 방랑자 도감",
    "비전 통신 백과": "마도 통신 백과",
    "비전 기동 백과": "마도 교통 백과",
    "비전 왕국": "마도 왕국",
    "비전 학파": "마도 학회",
    "대마법사": "대마도제",
    "전술 마법사": "전술 마도사",
    "흑마법사": "흑마도사",
    "비전 폭탄": "마도폭탄",
    "비전 투사포": "마도포",
    "에테르 병기": "마도 병기",
    "에테르 공학": "마도공학",
    "마법 우산": "마도 우산",
    "비전 체스": "마도 체스",
    "비전 감시망": "마도 감시망",
    "마법 연합": "마도 연합",
    "마법 연합체": "마도 연합체",
    "마법 대군": "마도 대군",
    "비전 체계": "마도 시스템",
    "비전력": "마도력",
    "에테르 연성진": "마도진",
    "비전학": "마도학",
    "비전서": "마도서",
    "비전": "마도" # Last one
}

for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old_val, new_val in restorations.items():
        content = content.replace(old_val, new_val)
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Restored Mado terminology successfully.")
