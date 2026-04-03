import os
import shutil

backup_base = r"C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\_Legacy_중립세력 (Backup)"
live_base = r"C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\6. 범대륙 초국가 및 중립 세력 (Supranational & Neutral)"

mappings = [
    # (Backup Parent, Live Parent)
    ("2. 마법연구조직 (Magic Research)", "6-6. 초국가 진리 연합 및 마탑 (Academia)"),
    ("1. 용병단(Mercenaries)", "6-3. 대륙 용병단 (Mercenaries)")
]

def find_matching_live_folder(live_parent_path, legacy_folder_name):
    """Finds a folder in the live directory that starts with the same number as the legacy folder."""
    if not os.path.exists(live_parent_path):
        return None
    try:
        legacy_num = legacy_folder_name.split(".")[0].strip()
    except:
        return legacy_folder_name
        
    for live_folder in os.listdir(live_parent_path):
        if os.path.isdir(os.path.join(live_parent_path, live_folder)):
            if live_folder.startswith(f"{legacy_num}."):
                return live_folder
    return legacy_folder_name # Fallback to exact match if no number match found

for b_parent, l_parent in mappings:
    b_parent_path = os.path.join(backup_base, b_parent)
    l_parent_path = os.path.join(live_base, l_parent)
    
    if not os.path.exists(b_parent_path):
        print(f"Backup parent not found: {b_parent_path}")
        continue
        
    # Iterate through all faction folders in the backup parent (1., 2., 3., etc.)
    for legacy_folder in os.listdir(b_parent_path):
        b_faction_path = os.path.join(b_parent_path, legacy_folder)
        if not os.path.isdir(b_faction_path): continue
        
        legacy_units_path = os.path.join(b_faction_path, "9. 예하 부대 및 기사단 (Military Units)")
        if not os.path.exists(legacy_units_path):
            legacy_units_path = os.path.join(b_faction_path, "9. 예하 부대 (Military Units)") # Try without 기사단 just in case
            if not os.path.exists(legacy_units_path):
                continue # No units folder to copy
                
        # Find matching live folder
        live_folder = find_matching_live_folder(l_parent_path, legacy_folder)
        if not live_folder:
            print(f"Could not find matching live folder for {legacy_folder}")
            continue
            
        l_faction_path = os.path.join(l_parent_path, live_folder)
        
        # We must copy EXACTLY `9. 예하 부대 및 기사단 (Military Units)`
        live_units_path = os.path.join(l_faction_path, "9. 예하 부대 및 기사단 (Military Units)")
        
        print(f"Mapping: {legacy_folder} -> {live_folder}")
        
        # Delete existing live units folder to ensure a 1:1 clean copy
        if os.path.exists(live_units_path):
            shutil.rmtree(live_units_path)
            
        # Create parent live faction folder if it doesn't exist
        os.makedirs(l_faction_path, exist_ok=True)
            
        # Copy the folder
        shutil.copytree(legacy_units_path, live_units_path)
        print(f"Successfully copied units for {live_folder}")

print("All requested copy-pasting completed safely.")
