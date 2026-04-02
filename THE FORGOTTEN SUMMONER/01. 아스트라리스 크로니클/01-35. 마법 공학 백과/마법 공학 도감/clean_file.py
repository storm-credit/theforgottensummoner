import os

path = r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-35. 마법 공학 백과\마법 공학 도감\6-1. 마나 캐노니어 (Mana Cannoneer).md"

with open(path, "rb") as f:
    data = f.read()

text = data.decode("utf-8", errors="replace").replace('\x00', '')

with open(path, "w", encoding="utf-8-sig") as f:
    f.write(text)

with open(r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-35. 마법 공학 백과\마법 공학 도감\fix_result.txt", "w", encoding="utf-8") as f:
    f.write("File cleaned up successfully.\n")
