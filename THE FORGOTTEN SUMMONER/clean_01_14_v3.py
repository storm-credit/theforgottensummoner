import os
import re

directory = r"C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 백과 (Hero Archive)"

replacements = [
    (re.compile(r'삭제\s*\(Delete\)'), r'소거(Obliterate)'),
    (re.compile(r'영적 정보 서버로'), r'영적 교차점(Nexus)으로'),
    (re.compile(r'물리 서버를'), r'물리적 중추를'),
    (re.compile(r'서버 권한 남용'), r'세계의 섭리 권한 남용'),
    (re.compile(r'서버 관리자\s*\(Admin\)'), r'섭리 통제자(Dominator)'),
    (re.compile(r'서버 관리자'), r'사념망 관리자'),
    (re.compile(r'단일 서버 포트로'), r'단일 영적 연결망으로'),
    (re.compile(r'메인 서버 배터리 팩'), r'마력 공급 중추 팩'),
    (re.compile(r'서버망으로'), r'마도망으로'),
    (re.compile(r'서버실'), r'비밀 중추소'),
    (re.compile(r'서버장'), r'공명자'),
    (re.compile(r'서버 랙 같은'), r'마도력 증폭기 같은'),
    (re.compile(r'과거 서버에'), r'과거의 시간축에'),
    (re.compile(r'서버 1위를'), r'제국 1위를'),
    (re.compile(r'그의 서버를 강제 재부팅'), r'그의 사념을 강제 각성'),
    (re.compile(r'핵심 서버\s*\(Server\)'), r'핵심 공명점(Nexus)'),
    (re.compile(r'시야 정보를 해킹해'), r'시야 정보를 사념 탈취해'),
    (re.compile(r'시야 정보만을 해킹해'), r'시야 정보만을 사념 탈취해'),
    (re.compile(r'정보베이스를 실시간 마력 스트리밍\s*\(Streaming\)으로 보고하는'), r'영적 정보를 실시간 마력 공명(Resonance)으로 보고하는 진보된 인간형 허브'),
    (re.compile(r'클론 첩보'), r'분신 첩보'),
    (re.compile(r'코더'), r'주술사'),
    (re.compile(r'물리 엔진상'), r'물리 법칙상'),
]

count = 0
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            original_content = content
            for pattern, repl in replacements:
                content = pattern.sub(repl, content)
                
            if content != original_content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                count += 1
                print(f"Updated: {file}")

print(f"Total files updated: {count}")
