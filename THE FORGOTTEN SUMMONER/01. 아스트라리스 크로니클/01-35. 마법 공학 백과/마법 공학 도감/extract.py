import re

file_path = "6-4. 강철 의체 (Steel Prosthetics).md"
out_path = "broken.txt"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    broken_pattern = re.compile(r"([가-힣] ){5,}[가-힣]|5기어: 광인 콕핏")
    
    with open(out_path, "w", encoding="utf-8") as out:
        out.write("Found broken lines:\n")
        for i, line in enumerate(lines):
            if broken_pattern.search(line):
                out.write(f"Line {i+1}: {line.strip()}\n")

except Exception as e:
    with open(out_path, "w", encoding="utf-8") as out:
        out.write(f"Error: {e}\n")
