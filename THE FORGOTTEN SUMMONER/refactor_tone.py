import os
import re

base_dir = r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-15. 인물 백과 (Character Archive)\0. 주인공 일행 (Main Characters)"
old_dir_name = r"04. 결속수 (Bound Companions)"
new_dir_name = r"04. 펫 및 환상종 (Pets & Mythic Beasts)"

old_dir_path = os.path.join(base_dir, old_dir_name)
new_dir_path = os.path.join(base_dir, new_dir_name)

# 1. Rename Directory
if os.path.exists(old_dir_path):
    os.rename(old_dir_path, new_dir_path)
    print(f"Renamed directory to: {new_dir_name}")
else:
    print("Old directory not found. Assuming already renamed or missing.")

# 2. Update the 9 Pet Files
if os.path.exists(new_dir_path):
    for filename in os.listdir(new_dir_path):
        if not filename.endswith(".md"): continue
        
        filepath = os.path.join(new_dir_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Tone adjustments
        content = content.replace("결속수 기본 생태", "환상종/패밀리어 기본 생태")
        content = content.replace("결속수가", "환상종이")
        content = content.replace("결속수는", "환상종은")
        content = content.replace("결속수", "환상종")
        content = content.replace("다크 판타지", "에픽 판타지")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated tone in {filename}")

# 3. Update the Template
template_path = r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\.agent\workflows\Pet_Creation_Standard.md"
if os.path.exists(template_path):
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    content = content.replace("성장형 결속수(Pet/Homunculus)", "성장형 펫 및 환상종(Pets & Mythic Beasts)")
    content = content.replace("결속수(Pet & Companion)", "펫 및 환상종(Pets & Mythic Beasts)")
    content = content.replace("다크 판타지", "에픽 판타지")
    content = content.replace("결속수 기본 생태", "환상종 기본 생태")
    content = content.replace("결속수", "펫/사역마")
    
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated Pet_Creation_Standard.md template.")
