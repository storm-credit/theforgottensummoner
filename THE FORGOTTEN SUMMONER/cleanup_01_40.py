import os
import shutil

folder = r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-40. 마도 통신 백과"

keep_files = [
    "1. 대륙 간 통신 시스템의 기원과 마나 교감망 (Evolution & Origins).md",
    "2. 주요 통신 방식과 대륙별 인프라 (Core Methods & Regional Differences).md",
    "3. 영적 혼선과 통신의 한계 (Resonance Interference & Limitations).md",
    "4. 마법적 방첩망과 은닉 첩보 체계 (Magical Espionage & Veil Networks).md",
    "5. 금지된 흑마법 통신과 지하 범죄망 (Forbidden Telepathy & Syndicates).md"
]

for item in os.listdir(folder):
    item_path = os.path.join(folder, item)
    if os.path.isfile(item_path):
        if item not in keep_files:
            os.remove(item_path)
            print(f"Deleted file: {item}")
    elif os.path.isdir(item_path):
        shutil.rmtree(item_path)
        print(f"Deleted folder: {item}")
