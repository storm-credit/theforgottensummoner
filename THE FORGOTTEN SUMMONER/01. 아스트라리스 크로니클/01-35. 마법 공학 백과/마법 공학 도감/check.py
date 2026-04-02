import os

filename = "6-1. 마나 캐노니어 (Mana Cannoneer).md"
with open(filename, "rb") as f:
    content = f.read()

encoding = "utf-8"
try:
    text = content.decode("utf-8")
except:
    try:
        text = content.decode("utf-16")
        encoding = "utf-16"
    except:
        text = content.decode("cp949")
        encoding = "cp949"

with open("out.txt", "w", encoding="utf-8") as out:
    out.write(f"Size: {len(content)}\n")
    out.write(f"Encoding: {encoding}\n")
    out.write(f"Causality count: {text.count('인과율')}\n")
    out.write(f"Fate count: {text.count('운명')}\n")
    out.write(f"Providence count: {text.count('섭리')}\n")
    out.write(f"Gibberish count: {text.count('뼛가루 질산 융합')}\n")
    out.write(f"Lines count: {len(text.splitlines())}\n")
