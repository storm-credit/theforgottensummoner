import re
import json

file_path = r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-35. 마법 공학 백과\마법 공학 도감\6-4. 강철 의체 (Steel Prosthetics).md"
out_path = r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-35. 마법 공학 백과\마법 공학 도감\broken_lines.txt"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    broken_lines = []
    
    for i, line in enumerate(lines):
        if "|" in line:
            # Check for multiple isolated Korean characters (5 or more space-separated characters)
            if re.search(r'([가-힣]\s){5,}', line) or "콕핏" in line or "5기어" in line:
                broken_lines.append(f"L{i+1}: {line.strip()}")
                
    with open(out_path, "w", encoding="utf-8") as out:
        out.write("\n".join(broken_lines))
        
except Exception as e:
    with open(out_path, "w", encoding="utf-8") as out:
        out.write(f"Error: {e}")
