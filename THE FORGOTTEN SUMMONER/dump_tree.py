import os

dirs = [
    r"C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\00. 세계의 틀",
    r"C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클"
]

out_file = r"C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\tree_dump.txt"

with open(out_file, "w", encoding="utf-8") as f:
    for base_dir in dirs:
        for root, d_names, f_names in os.walk(base_dir):
            rel_path = os.path.relpath(root, r"C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER")
            f.write(f"{rel_path}\n")

print("Done")
