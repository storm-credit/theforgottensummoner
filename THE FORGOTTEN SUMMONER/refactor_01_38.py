import os
import re

base_dir = r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클"
old_dir_name = "01-38. 팻 백과"
new_dir_name = "01-38. 동반수 백과"

old_dir_path = os.path.join(base_dir, old_dir_name)
new_dir_path = os.path.join(base_dir, new_dir_name)

# 1. Rename root directory
if os.path.exists(old_dir_path):
    os.rename(old_dir_path, new_dir_path)
    print(f"Renamed root directory: '{old_dir_name}' -> '{new_dir_name}'")
    target_dir = new_dir_path
else:
    print(f"Directory '{old_dir_name}' not found. Perhaps it was already renamed to '{new_dir_name}'?")
    if os.path.exists(new_dir_path):
        target_dir = new_dir_path
    else:
        print("Target directory does not exist! Aborting.")
        exit(1)

# Text replacement rules
replacements = [
    # Metadata aliases and exact matches prioritizing spaces
    ("aliases: [\"팻 백과", "aliases: [\"동반수 백과"),
    ("팻 백과", "동반수 백과"),
    ("펫 백과", "동반수 백과"),
    ("펫 도감", "동반수 도감"),
    ("팻 도감", "동반수 도감"),
    ("팻", "동반수"),
    ("펫", "동반수"),
    
    # Systems / Game Meta
    ("패시브", "태생적 권능"),
    ("스탯", "고유 역량"),
    ("어그로", "증오의 시선"),
    ("경험치", "치열한 교감의 증거"),
    ("경험", "경험"), # '경험치' will be caught first, '경험' alone is safe
    ("시스템", "대자연의 섭리"),
    ("레벨", "생태적 계위")
]

# 2. Walk bottom-up to rename directories and files
for root, dirs, files in os.walk(target_dir, topdown=False):
    # Rename files
    for filename in files:
        if filename.endswith(".md"):
            filepath = os.path.join(root, filename)
            
            # Read and replace content
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            for old_word, new_word in replacements:
                content = content.replace(old_word, new_word)
                
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Rename file if filename contains '팻' or '펫'
            new_filename = filename.replace("팻", "동반수").replace("펫", "동반수")
            # If there's an issue with double spaces (e.g. "5. 동반수  도감")
            new_filename = new_filename.replace("  ", " ")
            if new_filename != filename:
                new_filepath = os.path.join(root, new_filename)
                os.rename(filepath, new_filepath)
                print(f"Renamed file: '{filename}' -> '{new_filename}'")
                
    # Rename directories
    for dirname in dirs:
        new_dirname = dirname.replace("팻", "동반수").replace("펫", "동반수")
        new_dirname = new_dirname.replace("  ", " ")
        if new_dirname != dirname:
            old_dir_full = os.path.join(root, dirname)
            new_dir_full = os.path.join(root, new_dirname)
            os.rename(old_dir_full, new_dir_full)
            print(f"Renamed dir: '{dirname}' -> '{new_dirname}'")

print("Refactoring complete.")
