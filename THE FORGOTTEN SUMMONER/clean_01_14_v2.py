import os
import re

directory = r"C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 백과 (Hero Archive)"

# Regex replacement mapping
# Use tuple (pattern, replacement)
replacements = [
    (re.compile(r'패시브 및 전투 특성\s*\(Passive Traits & Gimmicks\)'), r'태생적 권능 및 우주적 섭리 (Innate Traits & Providence)'),
    (re.compile(r'스턴\s*\([Ff]ear\)'), r'마비(Paralysis)'),
    (re.compile(r'스턴\s*\(Stun\)|스턴기|스턴'), r'절대 마비(Paralysis)'),
    (re.compile(r'디버프\s*\(?Debuff\)?|디버프'), r'재앙적 저주(Curse)'),
    (re.compile(r'버프\s*\(?Buff\)?|버프'), r'신성한 가호(Blessing)'),
    (re.compile(r'텔레포트\s*\(?Teleport\)?|텔레포트'), r'공간 도약(Dimensional Leap)'),
    (re.compile(r'패시브\s*\(?Passive\)?|패시브'), r'태생적 권능(Innate Grace)'),
    (re.compile(r'시스템\s*\(?System\)?|시스템'), r'세계의 섭리'),
    (re.compile(r'스탯\s*\(?Stat\)?|스탯'), r'경박한 수치화 기운'),
    (re.compile(r'기믹\s*\(?Gimmick\)?|기믹'), r'우주적 변수(Providence)'),
    (re.compile(r'버그\s*\(?Bug\)?|버그'), r'인과율의 균열(Anomaly)'),
    (re.compile(r'데이터\s*\(?Data\)?|데이터상|데이터'), r'영적 기록(Record)'),
    (re.compile(r'서버 삭제\s*\(?Delete\)?'), r'영구 소각(Delete)'),
    (re.compile(r'롤백\s*\(Rollback\)'), r'인과율 회귀(Rollback)'),
    (re.compile(r'치트의 대가'), r'금기의 대가'),
    (re.compile(r'힐링\s*\(?Healing\)?|힐링'), r'치유의 기적'),
    (re.compile(r'힐을 받을수록'), r'치유 권능을 받을수록'),
    (re.compile(r'해킹'), r'사념 공명 탈취'),
    (re.compile(r'너프해버리는'), r'열화(Degradation)시켜버리는'),
]

count = 0
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            original_content = content
            # Apply regex replacements
            for pattern, repl in replacements:
                content = pattern.sub(repl, content)
                
            if content != original_content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                count += 1
                print(f"Updated: {file}")

print(f"Total files updated: {count}")
