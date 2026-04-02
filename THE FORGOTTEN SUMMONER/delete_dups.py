import os
import shutil

base_path = r"C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 백과 (Hero Archive)\01-14-1. 성장 영웅"

dirs = os.listdir(base_path)
for d in dirs:
    if d.startswith("7. "):
        full_path = os.path.join(base_path, d)
        print("Found duplicate folder:", full_path)
        shutil.rmtree(full_path, ignore_errors=True)
        print("Deleted!")
