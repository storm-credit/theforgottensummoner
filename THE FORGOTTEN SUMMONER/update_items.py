import os, glob

base_dir = r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 백과 (Hero Archive)\01-14-2. 현존 영웅\1. 에테르 대륙 (Ether Continent)\1. 성국 (Saint Haven)"

mappings = {
    '01. 레오니스 발레리우스': [('고유 무기', '[[한손검 (One-handed Swords)]]'), ('고유 방어구', '[[판금 (Plate Armor)]]'), ('고대 유물', '[[성광 파편 (Shard of Holy Radiance)]]')],
    '02. 카시엘 아크투루스': [('고유 무기', '[[둔기 (Blunt Weapons)]]'), ('고유 악세서리', '[[안경 (Eyewear)]]'), ('고대 유물', '[[마법서 (Grimoires)]]')],
    '03. 베네딕투스 테르시오': [('고유 무기', '[[지팡이 (Staves)]]'), ('고유 방어구', '[[로브 (Robes)]]'), ('고대 유물', '[[도구 (Tools)]]')],
    '04. 가브리엘 솔그리드': [('고유 무기', '[[대검 (Greatswords)]]'), ('고유 방어구', '[[견갑 (Pauldrons)]]'), ('명마/성수', '[[탈것 (Mounts)]]')],
    '05. 미카엘 듀란달': [('고유 방패', '[[방패 (Shields)]]'), ('고유 방어구', '[[중갑 (Heavy Armor)]]'), ('고대 유물', '[[반지 (Rings)]]')],
    '06. 루시안 제피로스': [('고유 무기', '[[창 (Spears)]]'), ('고유 방어구', '[[경갑 (Light Armor)]]'), ('명마/성수', '[[탈것 (Mounts)]]')],
    '07. 엘리아스 아우렐리우스': [('고유 무기', '[[지팡이 (Staves)]]'), ('고유 방어구', '[[로브 (Robes)]]'), ('고대 유물', '[[마법서 (Grimoires)]]')],
    '08. 세릴 실피아': [('고유 무기', '[[마도구 (Magic Tools)]]'), ('고유 방어구', '[[신발 (Boots)]]'), ('고대 유물', '[[성광 파편 (Shard of Holy Radiance)]]')],
    '09. 마리안 세레스': [('고유 무기', '[[지팡이 (Staves)]]'), ('고유 방어구', '[[가운 (Gown)]]'), ('고대 유물', '[[기억의 구슬 (Memory Orb)]]')],
    '10. 세라피나 녹티스': [('고유 무기', '[[마도구 (Magic Tools)]]'), ('고유 방어구', '[[망토 (Cloaks)]]'), ('고대 유물', '[[반지 (Rings)]]')],
    '11. 에반젤린 아스텔': [('고유 무기', '[[활 (Bows)]]'), ('고유 방어구', '[[망토 (Cloaks)]]'), ('고대 유물', '[[특수 무기 (Special Weapons)]]')],
    '12. 테오도르 뱅가드': [('고유 무기', '[[지휘봉 (Batons)]]'), ('고유 악세서리', '[[안경 (Eyewear)]]'), ('고대 유물', '[[기억의 구슬 (Memory Orb)]]')]
}

for filename in os.listdir(base_dir):
    if not filename.endswith(".md"): continue
    
    hero_key = None
    for key in mappings.keys():
        if key in filename:
            hero_key = key
            break
            
    if not hero_key: continue
    
    file_path = os.path.join(base_dir, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    new_lines = []
    for line in lines:
        if line.strip().startswith("- **[") and "**:" in line:
            for keyword, category in mappings[hero_key]:
                # Check if the line has the relevant equipment slot like '고유 무기'
                if keyword in line and "(도감 연계" not in line:
                    line = line.rstrip() + f" (도감 연계: {category})\n"
                    break
        new_lines.append(line)
        
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

print("Patch complete!")
