import os
import re

d = r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-15. 인물 백과 (Character Archive)\0. 주인공 일행 (Main Characters)\04. 팻 (Pets & Companions)"

pets_info = {
    "01": {"name": "루미에스", "eng": "Lumies", "title": "거룩한 재의 파랑새", "faction": "[[1. 성국 (Saint Haven)]]"},
    "02": {"name": "이그니스", "eng": "Ignis", "title": "부화하지 않은 폭염룡의 알", "faction": "[[1. 솔라리안 제국 (Solarian Empire)]]"},
    "03": {"name": "윈터팡", "eng": "Winterfang", "title": "서리늑대 새끼 '펜리르'의 파편", "faction": "[[01-8-12. 프로스트본 연합 (Frostborn Tribes)]]"},
    "04": {"name": "아라크네", "eng": "Arachne", "title": "심연을 엮는 거미 군락", "faction": "[[01-8-27. 그림자 연맹 (Shadow Syndicate)]]"},
    "05": {"name": "비오타", "eng": "Biota", "title": "피눈물 흘리는 천사상", "faction": "[[1. 솔라리안 제국 (Solarian Empire)]]"},
    "06": {"name": "아이언웜", "eng": "Ironwyrm", "title": "강철-공생체 슬라임", "faction": "[[01-8-25. 검은 파도 용병단 (Black Tide Mercenaries)]]"},
    "07": {"name": "포켓", "eng": "Pocket", "title": "아공간 배불뚝이 모그와이", "faction": "[[01-8-33. 차원 탐사단 (Dimensional Explorers)]]"},
    "08": {"name": "크리서스", "eng": "Croesus", "title": "재복의 황금 두꺼비상", "faction": "[[01-8-30. 황금 손아귀 (Golden Claw)]]"},
    "09": {"name": "오메가", "eng": "Omega", "title": "버려진 호문쿨루스 코어", "faction": "[[2. 아르카나 잔재 (Arkana Remnants)]]"}
}

for filename in os.listdir(d):
    if not filename.endswith(".md"): continue
    
    prefix = filename[:2]
    if prefix not in pets_info: continue
    
    info = pets_info[prefix]
    new_filename = f"{prefix}. {info['name']} ({info['eng']}).md"
    
    filepath = os.path.join(d, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Refactor Heading
    # From: # 01. 거룩한 재의 파랑새 '루미에스' (Lumies)
    # To: # 01. 루미에스 (Lumies)
    content = re.sub(r'# \d\d\. .*?\n', f"# {prefix}. {info['name']} ({info['eng']})\n", content)
    
    # Check if Faction is explicitly listed in section 1 or 2
    # I will add a bullet point for Faction right after Core Origin to ensure compliance
    # We look for "## 🧬 [A. 결속수 기본 생태 및 기원 (Core Origin)]"
    faction_addition = f"- **0. 세력 (Faction)**: `{info['faction']}` - 이 결속수가 소속되거나 기원한 세력적 기반."
    if "**0. 세력 (Faction)**" not in content:
        content = content.replace(
            "## 🧬 [A. 결속수 기본 생태 및 기원 (Core Origin)]\n",
            f"## 🧬 [A. 결속수 기본 생태 및 기원 (Core Origin)]\n\n{faction_addition}"
        )

    # Change aliases to ensure name and title are clean
    # Remove existing aliases line and add new one
    content = re.sub(r'aliases: \[.*?\]\n', f'aliases: ["{info["title"]} \'{info["name"]}\'", "{info["name"]}", "{info["title"]}"]\n', content)

    # Write temporarily, then rename
    new_filepath = os.path.join(d, new_filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    if filename != new_filename:
        os.rename(filepath, new_filepath)
        print(f"Renamed: {filename} -> {new_filename}")
        
