import os
import glob
import re

d = r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-15. 인물 백과 (Character Archive)\0. 주인공 일행 (Main Characters)\03. 히로인"

# Replace pairs (Old -> New)
replacements = [
    ('릴리스', '엘라리스'),
    ('Lilith', 'Elaris'),
    ('실비아', '세이렌'),
    ('Sylvia', 'Seiren'),
    ('아리아', '오로라'),
    ('Aria', 'Aurora'),
    ('루시엔', '루미에르'),
    ('Lucien', 'Lumiere')
]

factions = {
    '01. ': '[[1. 성국 (Saint Haven)]]',
    '02. ': '[[1. 솔라리안 제국 (Solarian Empire)]]',
    '03. ': '[[01-8-36. 유랑 기사단 (Wandering Knights)]]',
    '04. ': '[[01-8-12. 프로스트본 연합 (Frostborn Tribes)]]',
    '05. ': '[[01-8-16. 망자의 왕국 (Kingdom of the Dead)]]', # 엘라리스
    '06. ': '[[01-8-26. 어둠의 손 (Shadow Hand)]]',
    '07. ': '[[01-8-19. 해적 연합 (Pirate Confederacy)]]',
    '08. ': '[[01-8-21. 바다의 교단 (Church of the Sea)]]', # 세이렌
    '09. ': '[[01-8-34. 진실의 눈 (Eye of Truth)]]', # 오로라
    '10. ': '[[3. 자유도시연합 (Crossroad Cities)]]' # 루미에르
}

for filename in os.listdir(d):
    path = os.path.join(d, filename)
    if not filename.endswith('.md'):
        continue
    
    # Check if file needs renaming (05, 08, 09, 10)
    new_filename = filename
    if any(prefix in filename for prefix in ['05.', '08.', '09.', '10.']):
        for old, new in replacements:
            new_filename = new_filename.replace(old, new)
        
        if new_filename != filename:
            new_path = os.path.join(d, new_filename)
            os.rename(path, new_path)
            path = new_path
            print(f"Renamed {filename} -> {new_filename}")

    # Read content
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
            
    # Content replacements (apply to all files in case other heroines reference them)
    for old, new in replacements:
        content = content.replace(old, new)
        
    # Faction link replacement
    for prefix, faction_link in factions.items():
        if new_filename.startswith(prefix):
            # Regex to replace faction link taking care of existing formatting
            content = re.sub(
                r'1\.\s*세력\s*\(Faction\)\*\*(?:\s*:\s*).*(\n|$)',
                f'1. 세력 (Faction)**: `{faction_link}` - \\1',
                content
            )
            # Alternatively just replace the tag directly
            content = re.sub(
                r'1\.\s*세력\s*\(Faction\)\*\*:\s*`\[\[.*?\]\]`',
                f'1. 세력 (Faction)**: `{faction_link}`',
                content
            )
            break
            
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated content in {new_filename}")
