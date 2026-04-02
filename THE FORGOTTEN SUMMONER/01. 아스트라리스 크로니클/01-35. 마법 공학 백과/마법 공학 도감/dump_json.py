import json

source = r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-35. 마법 공학 백과\마법 공학 도감\6-4. 강철 의체 (Steel Prosthetics).md"
dest = r"c:\Users\Storm Credit\output.json"

try:
    with open(source, "rb") as f:
        text = f.read().decode('utf-8-sig', errors='replace')
        
    broken_lines = []
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if "|" in line and sum(1 for c in line if "\uac00" <= c <= "\ud7a3") > 15:
            # Simple heuristic: find rows with many isolated space-separated characters
            parts = line.split()
            single_chars = sum(1 for p in parts if len(p) == 1 and "\uac00" <= p <= "\ud7a3")
            if single_chars > 8 or "콕핏" in line or "5기어" in line:
                broken_lines.append(f"L{i+1}: {line}")

    with open(dest, "w", encoding="utf-8") as f:
        json.dump({"broken": broken_lines}, f, ensure_ascii=False, indent=2)
except Exception as e:
    with open(dest, "w", encoding="utf-8") as f:
        json.dump({"error": str(e)}, f)
