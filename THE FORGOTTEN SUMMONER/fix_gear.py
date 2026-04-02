import os
import glob

folder = r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-40. 마도 통신 백과"

replacements = {
    "1기어": "1공명",
    "2기어": "2공명",
    "3기어": "3공명",
    "4기어": "4공명",
    "5기어": "5공명",
    "6기어": "6공명",
    "7기어": "7공명",
    "통신 1기어": "통신 1공명",
    "기어의 대가": "공명의 대가",
    "기어 기반": "공명 기반",
    "별빛 기어": "별빛 공명",
    "기어별": "공명별",
    "어떤 대계 차단이나": "어떤 대계 차단이나", # just dummy
    "기어": "공명 단계" # Need to be careful. I won't do a generic "기어" -> "공명" 
}

# First replace specific cases
generic_replacements = {
    "1기어": "1공명",
    "2기어": "2공명",
    "3기어": "3공명",
    "4기어": "4공명",
    "5기어": "5공명",
    "6기어": "6공명",
    "7기어": "7공명",
    "기어의 대가": "공명의 대가",
    "별빛 기어": "별빛 공명",
    "기어 기반": "공명 기반",
    "기어별": "공명 단계별"
}

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    for k, v in generic_replacements.items():
        content = content.replace(k, v)
    
    # Check if a standalone '기어 |' column header exists to replace it with '공명 |'
    content = content.replace("| 기어 |", "| 공명 |")
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

for root, dirs, files in os.walk(folder):
    for filename in files:
        if filename.endswith(".md"):
            filepath = os.path.join(root, filename)
            process_file(filepath)

# Rename the files in the "05. 영적 공명 체계" folder
res_dir = os.path.join(folder, "05. 영적 공명 체계")
if os.path.exists(res_dir):
    for i in range(1, 8):
        old_name = f"{i}기어.md"
        new_name = f"{i}공명.md"
        old_path = os.path.join(res_dir, old_name)
        new_path = os.path.join(res_dir, new_name)
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            print(f"Renamed {old_name} to {new_name}")
