import os
import re
import shutil

base_path = r"C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-19. 아이템 도감 (Item Encyclopedia)"
hero_dir = r"C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)"

# 1. Clean old '및' folders if possible
dirs_to_scan = ["01-19-2. 방어구 (Armor)", "01-19-3. 악세서리 (Accessories)", "01-19-4. 유물 (Relics)"]
for d in dirs_to_scan:
    p = os.path.join(base_path, d)
    if os.path.exists(p):
        for sub in os.listdir(p):
            if "및" in sub or "공간 및" in sub:
                tgt = os.path.join(p, sub)
                try:
                    shutil.rmtree(tgt)
                except:
                    try:
                        os.rename(tgt, tgt + "_DELETED")
                    except:
                        pass

# 2. Categories
categories = {
    "01-19-2. 방어구 (Armor)": [
        "01. 중갑 (Heavy Armor)", "02. 판금 갑옷 (Plate Armor)", "03. 경갑 (Light Armor)", "04. 가죽 갑옷 (Leather Armor)",
        "05. 로브 (Robes)", "06. 마법복 (Mystic Garb)", "07. 망토 (Cloaks)", "08. 외투 (Surcoats)",
        "09. 방패 (Shields)", "10. 투구 (Helms)", "11. 얼굴 가리개 (Visors)", "12. 장갑 (Gauntlets)",
        "13. 손목 보호대 (Bracers)", "14. 장화 (Boots)", "15. 각반 (Greaves)", "16. 견갑 (Pauldrons)"
    ],
    "01-19-3. 악세서리 (Accessories)": [
        "01. 반지 (Rings)", "02. 목걸이 (Necklaces)", "03. 팬던트 (Pendants)", "04. 귀걸이 (Earrings)",
        "05. 머리장식 (Tiaras)", "06. 브로치 (Brooches)", "07. 훈장 (Badges)", "08. 부적 (Amulets)",
        "09. 성물 (Holy Relics)", "10. 보석 (Gems)", "11. 마력핵 (Core Stones)", "12. 특수 마도구 (Magical Tools)"
    ],
    "01-19-4. 유물 (Relics)": [
        "01. 고대 제국의 유산 (Legacy of the Ancient Empire)", "02. 심연 토벌 전리품 (Spoils of the Abyssal Subjugation)",
        "03. 태고의 정령 유물 (Primordial Spirit Relics)", "04. 소환 매개체 (Summoning Catalysts)",
        "05. 차원 왜곡기 (Dimensional Distorters)", "06. 이계의 아티팩트 (Otherworldly Artifacts)"
    ]
}

def write_template(filepath, title, parent_folder):
    prefix = "Armor"
    if "Accessories" in parent_folder: prefix = "Accessory"
    elif "Relics" in parent_folder: prefix = "Relic"
    content = f"""---
aliases: [{title}]
tags: [Item_Encyclopedia, {prefix}, Hanesis_Protocol]
---

# {title}

> *"장비의 무게는 곧 생명의 무게이며, 그 안에 담긴 마력은 착용자의 영혼을 투영한다."*

이 문서는 아스트라리스 대륙 내에서 유통되거나 전설로 전해지는 **[{title}]**을 집대성한 공식 분류 백과입니다.

## 📖 분류 개요 (Overview)
각 장비는 단순한 스탯 상승이 아닌, '가혹한 세계'에 맞서기 위한 특수한 전술적 기믹과 대자연의 제약(리스크)을 동반합니다.

---

## ⚔️ 일반 및 희귀 등급 목록 (Standard & Rare Pool)

| 고유 번호 | 아이템명 | 형태 및 재질 | 전술적 기믹 및 부작용 |
| --- | --- | --- | --- |
| 001 | 낡은 철제 기본 장비 예시 | 내구도가 떨어지는 강철 | 튼튼하나 마법 저항력 0% |

---

## 👑 전설적 영웅의 전용 무구 (Relics of the Heroes)
이 섹션은 정규 영웅록에 등재된 **S급 주역 및 수장**들이 소유한 전용 장비 정보입니다.

| 소유 영웅 | 장비명 | 외형 및 설명 | 초월적 특능 및 기믹 효과 |
| --- | --- | --- | --- |
<!-- HERO_INJECT_ANCHOR -->
"""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    except:
        pass

for parent, subs in categories.items():
    p_path = os.path.join(base_path, parent)
    os.makedirs(p_path, exist_ok=True)
    for sub in subs:
        sub_dir = os.path.join(p_path, sub)
        os.makedirs(sub_dir, exist_ok=True)
        fpath = os.path.join(sub_dir, f"{sub}.md")
        title = sub[sub.find(" ")+1:]
        write_template(fpath, title, parent)

print("Created 34 precise categories securely.")

# Extract & Inject
cache = {}
for root, dirs, files in os.walk(base_path):
    if "01-19-1" in root or "DELETED" in root: continue
    for f in files:
        if f.endswith(".md") and "01-19-" not in f:
            cache[os.path.join(root, f)] = []

def assign_cat(name, desc, tclass):
    nd = name + desc
    target = ""
    if tclass == "armor":
        if any(w in nd for w in ["판금", "흉갑"]): target = "02. 판금 갑옷 (Plate Armor).md"
        elif any(w in nd for w in ["중갑", "철갑"]): target = "01. 중갑 (Heavy Armor).md"
        elif any(w in nd for w in ["가죽"]): target = "04. 가죽 갑옷 (Leather Armor).md"
        elif any(w in nd for w in ["경갑", "재킷"]): target = "03. 경갑 (Light Armor).md"
        elif any(w in nd for w in ["마법복", "의복", "드레스"]): target = "06. 마법복 (Mystic Garb).md"
        elif any(w in nd for w in ["로브", "사제복"]): target = "05. 로브 (Robes).md"
        elif any(w in nd for w in ["외투", "코트"]): target = "08. 외투 (Surcoats).md"
        elif any(w in nd for w in ["망토", "클로크"]): target = "07. 망토 (Cloaks).md"
        elif any(w in nd for w in ["견갑", "어깨", "숄더", "어깨띠"]): target = "16. 견갑 (Pauldrons).md"
        elif any(w in nd for w in ["방패", "방벽"]): target = "09. 방패 (Shields).md"
        elif any(w in nd for w in ["안경", "마스크", "얼굴", "가리개"]): target = "11. 얼굴 가리개 (Visors).md"
        elif any(w in nd for w in ["투구", "헬름"]): target = "10. 투구 (Helms).md"
        elif any(w in nd for w in ["손목", "토시", "보호대"]): target = "13. 손목 보호대 (Bracers).md"
        elif any(w in nd for w in ["장갑", "건틀릿", "글러브"]): target = "12. 장갑 (Gauntlets).md"
        elif any(w in nd for w in ["각반", "그리브"]): target = "15. 각반 (Greaves).md"
        elif any(w in nd for w in ["장화", "부츠", "신발"]): target = "14. 장화 (Boots).md"
        else: target = "03. 경갑 (Light Armor).md"
    else:
        if any(w in nd for w in ["반지", "가락지", "링"]): target = "01. 반지 (Rings).md"
        elif any(w in nd for w in ["팬던트"]): target = "03. 팬던트 (Pendants).md"
        elif any(w in nd for w in ["목걸이"]): target = "02. 목걸이 (Necklaces).md"
        elif any(w in nd for w in ["귀걸이", "이어링"]): target = "04. 귀걸이 (Earrings).md"
        elif any(w in nd for w in ["머리장식", "티아라", "왕관", "서클릿"]): target = "05. 머리장식 (Tiaras).md"
        elif any(w in nd for w in ["브로치"]): target = "06. 브로치 (Brooches).md"
        elif any(w in nd for w in ["훈장", "배지", "징표"]): target = "07. 훈장 (Badges).md"
        elif any(w in nd for w in ["성물", "십자가", "성서"]): target = "09. 성물 (Holy Relics).md"
        elif any(w in nd for w in ["부적", "애뮬릿", "수호부", "호부"]): target = "08. 부적 (Amulets).md"
        elif any(w in nd for w in ["마력핵", "마석", "정수"]): target = "11. 마력핵 (Core Stones).md"
        elif any(w in nd for w in ["보석", "수정", "원석"]): target = "10. 보석 (Gems).md"
        elif any(w in nd for w in ["나침반", "모래시계", "피리", "수정구", "마도구"]): target = "12. 특수 마도구 (Magical Tools).md"
        else: target = "12. 특수 마도구 (Magical Tools).md"
        
    for k in cache.keys():
        if target in k: return k
    return None

c = 0
for root, dirs, files in os.walk(hero_dir):
    for f in files:
        if f.endswith(".md"):
            hname = f.replace(".md", "")
            with open(os.path.join(root, f), 'r', encoding='utf-8') as file:
                content = file.read()
                
            amatch = re.search(r'### 🧥.*?(?=### 💍|---|\Z)', content, re.DOTALL)
            if amatch:
                items = re.findall(r'\* \*\*\[(.*?)\] (.*?)\*\*.*?\* \*\*설명\*\*: (.*?)\n.*?\* \*\*전술적 효과\*\*: (.*?)(?=\n\* |\Z)', amatch.group(0), re.DOTALL)
                for item in items:
                    slot, name, desc, effect = item
                    bp = assign_cat(name, desc, "armor")
                    if bp:
                        cache[bp].append(f"| [[{hname}]] | **{name.strip()}** | {desc.strip()} | {effect.strip()} |")
                        c += 1

            accmatch = re.search(r'### 💍.*?(?=---|\Z)', content, re.DOTALL)
            if accmatch:
                il = re.findall(r'\* \*\*\[(.*?)\] (.*?)\*\*: (.*?)\n', accmatch.group(0))
                for item in il:
                    slot, name, desc = item
                    bp = assign_cat(name, desc, "accessory")
                    if bp:
                        cache[bp].append(f"| [[{hname}]] | **{name.strip()}** | {desc.strip()} | - |")
                        c += 1
                ml = re.findall(r'\* \*\*\[(.*?)\] (.*?)\*\*.*?\* \*\*설명\*\*: (.*?)\n.*?\* \*\*전술적 효과\*\*: (.*?)(?=\n\* |\Z)', accmatch.group(0), re.DOTALL)
                for item in ml:
                    slot, name, desc, effect = item
                    bp = assign_cat(name, desc, "accessory")
                    if bp:
                        cache[bp].append(f"| [[{hname}]] | **{name.strip()}** | {desc.strip()} | {effect.strip()} |")
                        c += 1

for filepath, lines in cache.items():
    if not lines: continue
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            orig = f.read()
            
        inj = "\n".join(lines) + "\n"
        if "<!-- HERO_INJECT_ANCHOR -->" in orig:
            nc = orig.replace("<!-- HERO_INJECT_ANCHOR -->", "<!-- HERO_INJECT_ANCHOR -->\n" + inj)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(nc)
    except:
        pass

print(f">>> SYNCHRONIZATION COMPLETE. Extracted {c} items into purely split categories!")
