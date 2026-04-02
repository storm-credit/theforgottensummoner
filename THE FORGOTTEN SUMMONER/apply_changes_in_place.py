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

if not os.path.exists(d):
    print("Directory does not exist!")
    exit(1)

for filename in os.listdir(d):
    if not filename.endswith(".md"): continue
    
    prefix = filename[:2]
    if prefix not in pets_info: continue
    
    info = pets_info[prefix]
    new_filename = f"{prefix}. {info['name']} ({info['eng']}).md"
    
    filepath = os.path.join(d, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Refactor Heading
    # Match any `# 01. ... (Eng)`
    content = re.sub(r'(?m)^# \d\d\. .*$', f"# {prefix}. {info['name']} ({info['eng']})", content)
    
    # 2. Add Faction if missing
    faction_addition = f"- **0. 세력 (Faction)**: `{info['faction']}` - 이 환상종이 소속되거나 기원한 세력적 기반."
    if "**0. 세력 (Faction)**" not in content and "결속수 기본" in content:
        content = content.replace(
            "## 🧬 [A. 결속수 기본 생태 및 기원 (Core Origin)]",
            f"## 🧬 [A. 결속수 기본 생태 및 기원 (Core Origin)]\n\n{faction_addition}"
        )
    elif "**0. 세력 (Faction)**" not in content and "환상종/패밀리어 기본" in content:
        content = content.replace(
            "## 🧬 [A. 환상종/패밀리어 기본 생태 및 기원 (Core Origin)]",
            f"## 🧬 [A. 환상종/패밀리어 기본 생태 및 기원 (Core Origin)]\n\n{faction_addition}"
        )

    # 3. Change aliases
    content = re.sub(r'(?m)^aliases: \[.*\]\n', f'aliases: ["{info["title"]} \'{info["name"]}\'", "{info["name"]}", "{info["title"]}"]\n', content)

    # 4. Epic Fantasy Tone Shift (Mixing 1 and 2: Pets/Familiars & Mythic Beasts, no "Dark Fantasy")
    content = content.replace("결속수 기본 생태", "환상종/사역마 기본 생태")
    content = content.replace("결속수가", "환상종이")
    content = content.replace("결속수는", "환상종은")
    content = content.replace("결속수", "환상종")
    content = content.replace("다크 판타지", "에픽 판타지")
    
    # Only write back
    new_filepath = os.path.join(d, new_filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    if filename != new_filename:
        os.rename(filepath, new_filepath)
        print(f"Renamed and updated: {filename} -> {new_filename}")
    else:
        print(f"Updated: {filename}")
