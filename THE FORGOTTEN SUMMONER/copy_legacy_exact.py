import os
import shutil

backup_base = r"C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\_Legacy_중립세력 (Backup)\3. 첩보 (Intelligence)"
live_base = r"C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\6. 범대륙 초국가 및 중립 세력 (Supranational & Neutral)\6-7. 그림자 첩보 조직 (Shadow Intelligence)"

mapping = {
    "1. 어둠의 손 (Shadow Hand)": "1. 어둠의 손 (Shadow Hand)",
    "2. 그림자 연맹 (Shadow Syndicate)": "2. 창백한 거미줄 첩보망 (Pale Web Syndicate)",
    "3. 검은 여우단 (Black Fox Syndicate)": "3. 검은 여우단 (Black Fox Syndicate)",
    "4. 황야의 추적자들 (Hunters of the Wild)": "4. 황야의 추적자들 (Hunters of the Wild)",
    "5. 황금 손아귀 (Golden Claw)": "5. 황금 손아귀 (Golden Claw)"
}

for b_folder, l_folder in mapping.items():
    src_dir = os.path.join(backup_base, b_folder, "9. 예하 부대 및 기사단 (Military Units)")
    dst_dir = os.path.join(live_base, l_folder, "9. 예하 부대 및 기사단 (Military Units)")
    
    # 1. Nuke the messed up live directory if it exists to clear my mistakes
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
        
    # 2. Copy exactly what is in the legacy folder to the live folder
    if os.path.exists(src_dir):
        shutil.copytree(src_dir, dst_dir)
        print(f"Copied {b_folder} -> {l_folder}")
    else:
        print(f"Source not found: {src_dir}")

print("Done copying legacy backup to live.")
