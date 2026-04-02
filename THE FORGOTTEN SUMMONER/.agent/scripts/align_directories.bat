@echo off
set "BASE=C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)"

:: Clean up previously hallucinated custom roots
rmdir /S /Q "%BASE%\7. 암흑조직 (Underworld Factions)" 2>nul
rmdir /S /Q "%BASE%\7. 단체 및 결사 (Societies)" 2>nul
rmdir /S /Q "%BASE%\8. 특수세력 및 교단 (Oceanic, Tech, Religion)" 2>nul

:: Create exactly mapped folders based on Faction Archive mapping
mkdir "%BASE%\1. 에테르 대륙 (Ether Continent)\4. 마법협회 (Arcane Society)" 2>nul
mkdir "%BASE%\3. 프로스트 대륙 (Frost Continent)\4. 그림자 항구 (Shadowwake Cove)" 2>nul
mkdir "%BASE%\4. 오벨리스크 대륙 (Obelisk Continent)\1. 심연 군단 (Abyssal Legion)" 2>nul
mkdir "%BASE%\4. 오벨리스크 대륙 (Obelisk Continent)\2. 망자의 왕국 (Kingdom of the Dead)" 2>nul
mkdir "%BASE%\4. 오벨리스크 대륙 (Obelisk Continent)\3. 잊힌 자들의 연합 (Forgotten Alliance)" 2>nul
mkdir "%BASE%\4. 오벨리스크 대륙 (Obelisk Continent)\4. 봉인 수호단 (Seal Wardens)" 2>nul
mkdir "%BASE%\5. 해양 대륙 (Oceanic Continent)\1. 해적 연합 (Pirate Confederacy)" 2>nul
mkdir "%BASE%\5. 해양 대륙 (Oceanic Continent)\2. 황금 함대 (Golden Armada)" 2>nul
mkdir "%BASE%\5. 해양 대륙 (Oceanic Continent)\3. 바다의 교단 (Church of the Sea)" 2>nul

:: Neutral hierarchy
mkdir "%BASE%\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\1. 저주받은 용병단 (Cursed Mercenaries)" 2>nul
mkdir "%BASE%\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\2. 그리핀 기사단 (Order of the Gryphon)" 2>nul
mkdir "%BASE%\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\3. 붉은 칼날 용병단 (Red Blades Mercenaries)" 2>nul
mkdir "%BASE%\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\4. 검은 파도 용병단 (Black Tide Mercenaries)" 2>nul
mkdir "%BASE%\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\5. 유랑 기사단 (Wandering Knights)" 2>nul
mkdir "%BASE%\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\6. 철혈 부대 (Iron Blood Corps)" 2>nul
mkdir "%BASE%\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\7. 바람의 칼날 (Wind Blades)" 2>nul
mkdir "%BASE%\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\8. 바이퍼 해적단 (Viper Raiders)" 2>nul
mkdir "%BASE%\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\9. 황금 기계단 (Golden Mechanists)" 2>nul
mkdir "%BASE%\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\10. 강철의 형제단 (Brotherhood of Steel)" 2>nul
mkdir "%BASE%\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\11. 신성 계약단 (Divine Covenant)" 2>nul
mkdir "%BASE%\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\12. 자연의 방랑자 (Wanderers of Nature)" 2>nul

mkdir "%BASE%\6. 중립세력 (Neutral)\2. 마법연구조직 (Magic Research)\1. 천상의 서고 (Celestial Archive)" 2>nul
mkdir "%BASE%\6. 중립세력 (Neutral)\2. 마법연구조직 (Magic Research)\2. 연금술사의 길드 (Guild of Alchemists)" 2>nul
mkdir "%BASE%\6. 중립세력 (Neutral)\2. 마법연구조직 (Magic Research)\3. 차원 탐사단 (Dimensional Explorers)" 2>nul
mkdir "%BASE%\6. 중립세력 (Neutral)\2. 마법연구조직 (Magic Research)\4. 진실의 눈 (Eye of Truth)" 2>nul
mkdir "%BASE%\6. 중립세력 (Neutral)\2. 마법연구조직 (Magic Research)\5. 심연의 별무리 (Stellar Abyss Collective)" 2>nul
mkdir "%BASE%\6. 중립세력 (Neutral)\2. 마법연구조직 (Magic Research)\6. 밤의 계약단 (Coven of the Night)" 2>nul

mkdir "%BASE%\6. 중립세력 (Neutral)\3. 첩보 (Intelligence)\1. 어둠의 손 (Shadow Hand)" 2>nul
mkdir "%BASE%\6. 중립세력 (Neutral)\3. 첩보 (Intelligence)\2. 그림자 연맹 (Shadow Syndicate)" 2>nul
mkdir "%BASE%\6. 중립세력 (Neutral)\3. 첩보 (Intelligence)\3. 검은 여우단 (Black Fox Syndicate)" 2>nul
mkdir "%BASE%\6. 중립세력 (Neutral)\3. 첩보 (Intelligence)\4. 황야의 추적자들 (Hunters of the Wild)" 2>nul
mkdir "%BASE%\6. 중립세력 (Neutral)\3. 첩보 (Intelligence)\5. 황금 손아귀 (Golden Claw)" 2>nul

:: Move Serian Weaver to correct location
move /Y "%BASE%\6. 중립세력 (Neutral)\2. 마법연구조직 (Magic Research)\1. 마법협회 (Arcane Society)\세리안 웨버 (Serian Weaver).md" "%BASE%\1. 에테르 대륙 (Ether Continent)\4. 마법협회 (Arcane Society)\"
rmdir /S /Q "%BASE%\6. 중립세력 (Neutral)\2. 마법연구조직 (Magic Research)\1. 마법협회 (Arcane Society)" 2>nul
