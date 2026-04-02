import os
import re

target_dir = r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-35. 마법 공학 백과\마법 공학 도감"

# Tuple format: (old_file, new_file, old_title_keyword, new_epic_title)
merge_pairs = [
    ("6-1. 마나 캐노니어 (Mana Cannoneer).md", "6-1. 은빛 광자 캐노니어 (Astral Cannoneer).md", "마나 캐노니어", "은빛 광자 캐노니어 (Astral Cannoneer)"),
    ("6-2. 거대 공성포 (Giant Siege Cannon).md", "6-2. 대성궤 공성 병기 (Zenith Siege Artillery).md", "거대 공성포", "대성궤 공성 병기 (Zenith Siege Artillery)"),
    ("6-3. 파워 아머 (Power Armor).md", "6-3. 백은의 성기사 외골격 (Silver Paladin Exoskeleton).md", "파워 아머", "백은의 성기사 외골격 (Silver Paladin Exoskeleton)"),
    ("6-4. 강철 의체 (Steel Prosthetics).md", "6-4. 영적 동기화 의체 (Astral Prosthetics & Sync).md", "강철 의체", "영적 동기화 의체 (Astral Prosthetics & Sync)"),
    ("6-5. 트랩 메이커 (Trap Maker).md", "6-5. 역장 결계 메이커 (Force-Field Architect).md", "트랩 메이커", "역장 결계 메이커 (Force-Field Architect)"),
    ("6-6. 기계 암살 (Mechanical Assassination).md", "6-6. 침묵의 칼날 오토마타 강습 (Silent Blade Automata Strike).md", "기계 암살", "침묵의 칼날 오토마타 강습 (Silent Blade Automata Strike)"),
    ("6-7. 오토마톤 (Automaton).md", "6-7. 자아 각성형 성물 골렘 (Ego-Awakened Sentinel).md", "오토마톤", "자아 각성형 성물 골렘 (Ego-Awakened Sentinel)"),
    ("6-8. 컴뱃 드론 (Combat Drone).md", "6-8. 별빛 호위 칼날 편대 (Astral Blade Escort Swarm).md", "컴뱃 드론", "별빛 호위 칼날 편대 (Astral Blade Escort Swarm)"),
    ("6-10. 장갑 기동 부대 (Armored Mobile Unit).md", "6-10. 기간트 모빌 장갑 부대 (Gigant Armored Mobile Fortress).md", "장갑 기동 부대", "기간트 모빌 장갑 부대 (Gigant Armored Mobile Fortress)")
]

for old_filename, new_filename, old_kw, new_title in merge_pairs:
    old_filepath = os.path.join(target_dir, old_filename)
    new_filepath = os.path.join(target_dir, new_filename)
    
    if not os.path.exists(old_filepath):
        print(f"Skipping {old_filename} - Not found. Perhaps already merged?")
        continue
        
    try:
        # Read the rich old file
        with open(old_filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Replace the header title
        # It's usually like '# 6-3. 파워 아머 (Power Armor)'
        pattern = re.compile(r"# 6-\d+\.\s+.*")
        content = re.sub(pattern, f"# {new_filename.replace('.md', '')}", content, count=1)
        
        # We also might need to replace internal mentions of the old name, but they might be okay or already processed.
        # Let's replace the raw keyword in text just in case (e.g. 파워 아머 -> 백은의 성기사 외골격).
        clean_new_title = new_title.split("(")[0].strip()
        content = content.replace(old_kw, clean_new_title)
        
        # Write to the epic filename (overwriting the skinny 7KB file with the massive content)
        with open(new_filepath, "w", encoding="utf-8") as f:
            f.write(content)
            
        # Delete the old file
        os.remove(old_filepath)
        print(f"SUCCESS: {old_filename} merged into {new_filename}")
        
    except Exception as e:
        print(f"Error processing {old_filename}: {e}")

print("Merge completion!")
