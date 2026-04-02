import os

base_path = r"C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)"

valid_heroes = [
    "카이엔 루미나 (Cayenne Lumina).md",
    "드라켄 발타르 (Draken Baltar).md",
    "레오나르드 솔라리안 (Leonard Solarian).md",
    "벨라시아 문 (Velasia Moon).md",
    "칼리안 드라코 (Kalian Drako).md",
    "사하르 바르칸 (Sahar Barkan).md",
    "에드윈 발몽 (Edwin Valmont).md"
]

# Wipe invalid heroes
for root, _, files in os.walk(base_path):
    for f in files:
        if f.endswith('.md'):
            if f not in valid_heroes:
                try:
                    os.remove(os.path.join(root, f))
                    print(f"Purged invalid hero: {f}")
                except Exception as e:
                    print(f"Failed to remove {f}: {e}")

# Create strict folder structures mapped from the prompt
dirs_to_create = [
    r"6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\1. 저주받은 용병단 (Cursed Mercenaries)",
    r"6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\2. 그리핀 기사단 (Order of the Gryphon)",
    r"6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\3. 붉은 칼날 용병단 (Red Blades Mercenaries)",
    r"6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\4. 검은 파도 용병단 (Black Tide Mercenaries)",
    r"6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\5. 어둠의 손 (Shadow Hand)",
    r"6. 중립세력 (Neutral)\2. 마법연구조직 (Magic Research)\1. 마법협회 (Arcane Society)",
    r"6. 중립세력 (Neutral)\2. 마법연구조직 (Magic Research)\5. 심연의 별무리 (Stellar Abyss Collective)",
    r"7. 암흑조직 (Underworld Factions)\1. 그림자 연맹 (Shadow Syndicate)",
    r"7. 암흑조직 (Underworld Factions)\2. 검은 여우단 (Black Fox Syndicate)",
    r"7. 단체 및 결사 (Societies)\3. 황야의 추적자들 (Hunters of the Wild)", # Placed in 7 but will put under Underworld
    r"7. 암흑조직 (Underworld Factions)\3. 황야의 추적자들 (Hunters of the Wild)",
    r"7. 암흑조직 (Underworld Factions)\4. 황금 손아귀 (Golden Claw)",
    r"8. 특수세력 및 교단 (Oceanic, Tech, Religion)\1. 해양 세력 (Oceanic Forces)\1. 심연의 별무리 (Stellar Abyss Collective)", 
    r"8. 특수세력 및 교단 (Oceanic, Tech, Religion)\1. 해양 세력 (Oceanic Forces)\2. 붉은 파도 해적단 (Crimson Tide Raiders)",
    r"8. 특수세력 및 교단 (Oceanic, Tech, Religion)\1. 해양 세력 (Oceanic Forces)\3. 바다의 교단 (Church of the Sea)",
    r"8. 특수세력 및 교단 (Oceanic, Tech, Religion)\2. 기술 세력 (Technological Forces)\1. 강철의 형제단 (Brotherhood of Steel)",
    r"8. 특수세력 및 교단 (Oceanic, Tech, Religion)\2. 기술 세력 (Technological Forces)\2. 황금 기계단 (Golden Mechanists)",
    r"8. 특수세력 및 교단 (Oceanic, Tech, Religion)\3. 종교 세력 (Religious Forces)\1. 신성 계약단 (Divine Covenant)",
    r"8. 특수세력 및 교단 (Oceanic, Tech, Religion)\3. 종교 세력 (Religious Forces)\2. 신들의 후계자 (Heirs of the Gods)",
    r"8. 특수세력 및 교단 (Oceanic, Tech, Religion)\3. 종교 세력 (Religious Forces)\3. 자연의 방랑자 (Wanderers of Nature)"
]

for d in dirs_to_create:
    dp = os.path.join(base_path, d)
    os.makedirs(dp, exist_ok=True)
    print(f"Created/Verified Directory: {d}")
