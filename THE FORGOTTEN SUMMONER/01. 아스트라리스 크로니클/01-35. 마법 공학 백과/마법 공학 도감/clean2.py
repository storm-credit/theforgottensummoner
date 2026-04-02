import os

filename = "6-1. 마나 캐노니어 (Mana Cannoneer).md"

with open(filename, "rb") as f:
    data = f.read()

# Decode and clean null bytes
text = data.decode("utf-8", errors="replace").replace('\x00', '')

# Ensure no duplicate gibberish or Causality terms are there.
text = text.replace("인과율", "섭리")

# Overwrite it safely
with open(filename, "w", encoding="utf-8") as f:
    f.write(text)

with open("done.txt", "w", encoding="utf-8") as f:
    f.write("Success! File rewrote properly.\n")
