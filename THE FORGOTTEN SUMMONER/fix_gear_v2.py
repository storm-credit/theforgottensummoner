import os

folder = r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-40. 마도 통신 백과\05. 영적 공명 체계"
files = os.listdir(folder)
print("Files in dir:", files)

for f in files:
    if "기어" in f:
        new_f = f.replace("기어", "공명")
        os.rename(os.path.join(folder, f), os.path.join(folder, new_f))
        print(f"Renamed {f} to {new_f}")

print("Done renaming files. Now replacing contents...")

target_dirs = [
    folder,
    r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-40. 마도 통신 백과\마도 통신 도감",
    r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-40. 마도 통신 백과"
]

def replace_in_file(fp):
    with open(fp, "r", encoding="utf-8") as file:
        content = file.read()
    
    orig = content
    content = content.replace("1기어", "1공명").replace("2기어", "2공명").replace("3기어", "3공명")
    content = content.replace("4기어", "4공명").replace("5기어", "5공명").replace("6기어", "6공명").replace("7기어", "7공명")
    content = content.replace("별빛 기어", "공명 단계").replace("기어의 대가", "공명의 대가")
    content = content.replace("통신 1기어", "통신 1공명")
    content = content.replace("| 기어 |", "| 공명 |")
    
    if orig != content:
        with open(fp, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Replaced text in {fp}")

for d in target_dirs:
    for root, dirs, filenames in os.walk(d):
        for fname in filenames:
            if fname.endswith(".md"):
                replace_in_file(os.path.join(root, fname))

