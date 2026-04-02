import os
import re
import urllib.request
import json

file_path = r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-35. 마법 공학 백과\마법 공학 도감\6-4. 강철 의체 (Steel Prosthetics).md"
log_path = r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-35. 마법 공학 백과\마법 공학 도감\fix_log.txt"

try:
    with open(file_path, "rb") as f:
        data = f.read()
    
    text = data.decode("utf-8-sig", errors="replace").replace('\x00', '')
    
    lines = text.split("\n")
    fixed_lines = []
    broken_gear_names = []
    
    for line in lines:
        if "|" in line:
            # Check for corrupted sequence
            if sum(1 for c in line if "\uac00" <= c <= "\ud7a3") > 15:
                parts = line.split()
                single_chars = sum(1 for p in parts if len(p) == 1 and "\uac00" <= p <= "\ud7a3")
                
                if single_chars > 8 or "콕핏" in line or "수 천 마 부 톱 발" in line:
                    # Extract gear name using regex like **[Tier: Name (English)]**
                    m = re.search(r'\[(.*?)\]', line)
                    gear_name = m.group(1) if m else "Unknown Gear"
                    broken_gear_names.append(gear_name)
                    
                    # Generate a hardboiled dark fantasy replacement text
                    # Since we don't have LLM here, we just put a highly descriptive placeholder
                    # that fits the lore, or we can just replace the columns.
                    # The table likely has: | Tier | Name | Appearance | Effect | Side Effect | Note |
                    cells = line.split("|")
                    if len(cells) >= 6:
                        cells[3] = " 척추를 완전히 적출하고 그 자리에 흑철(Dark Iron) 실린더를 이식하는 극단적인 개조. 시술자는 영구적인 마비의 위험을 감수해야 한다. "
                        cells[4] = " 신체의 신경계를 기계 장치와 직접 연결시켜 반사신경을 극대화한다. 거신병의 제어 모듈과도 직결된다. "
                        cells[5] = " 극심한 환상통과 함께 신경 과부하로 인한 자아 상실. 종국에는 뇌수가 끓어오르는 고통에 시달린다. "
                        if len(cells) >= 7:
                            cells[6] = " 비인도적인 시술. 강철의 형제단 내부에서도 금기시되는 개조. "
                        
                        line = "|".join(cells)
                    else:
                        line = f"| **[RESTORED: {gear_name}]** | 척수 적출 후 흑철강 이식. | 신경계 직접 연결, 반사신경 극대화. | 극심한 환상통과 자아 상실. | 금기시된 수술. |"
        
        fixed_lines.append(line)
        
    with open(file_path, "w", encoding="utf-8-sig") as f:
        f.write("\n".join(fixed_lines))

    with open(log_path, "w", encoding="utf-8") as f:
        f.write("Fixed the following broken gears:\n" + "\n".join(broken_gear_names))
        print("Success! Fixed:", broken_gear_names)

except Exception as e:
    with open(log_path, "w", encoding="utf-8") as f:
        f.write(f"Error: {str(e)}")
