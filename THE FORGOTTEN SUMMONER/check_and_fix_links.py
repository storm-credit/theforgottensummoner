import os
import re

directories = [
    r"C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-40. 마도 통신 백과",
    r"C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-41. 마도 교통 백과",
    r"C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-42. 차원 및 공간 마법 백과",
]

mappings = {
    r"\[\[(?:[^|\]]*?(?:자유도시연합|자유 도시 연합)[^|\]]*?)(?:\|([^\]]+))?\]\]": r"[[01-8. 세력 아카이브 (국가·조직 정리)\1. 에테르 대륙 (Ether Continent)\3. 자유도시연합 (Crossroad Cities)|\g<1>자유도시연합]]",
    r"\[\[(?:[^|\]]*?(?:솔라리안 제국|제국)[^|\]]*?)(?:\|([^\]]+))?\]\]": r"[[01-8. 세력 아카이브 (국가·조직 정리)\2. 크림슨 대륙 (Crimson Continent)\1. 솔라리안 제국 (Solarian Empire)|\g<1>솔라리안 제국]]",
    r"\[\[(?:[^|\]]*?(?:왕국연합|왕국 연합)[^|\]]*?)(?:\|([^\]]+))?\]\]": r"[[01-8. 세력 아카이브 (국가·조직 정리)\1. 에테르 대륙 (Ether Continent)\2. 왕국연합 (Allied Kingdoms)|\g<1>왕국연합]]",
    r"\[\[(?:[^|\]]*?(?:성국|빛과 재의 성국)[^|\]]*?)(?:\|([^\]]+))?\]\]": r"[[01-8. 세력 아카이브 (국가·조직 정리)\1. 에테르 대륙 (Ether Continent)\1. 성국 (Saint Haven)|\g<1>성국]]",
    r"\[\[(?:[^|\]]*?(?:정령연합|정령 연합)[^|\]]*?)(?:\|([^\]]+))?\]\]": r"[[01-8. 세력 아카이브 (국가·조직 정리)\1. 에테르 대륙 (Ether Continent)\5. 정령연합 (Spirit Union)|\g<1>정령연합]]",
    r"\[\[(?:[^|\]]*?(?:마법협회|마법 협회)[^|\]]*?)(?:\|([^\]]+))?\]\]": r"[[01-8. 세력 아카이브 (국가·조직 정리)\1. 에테르 대륙 (Ether Continent)\4. 마법협회 (Arcane Society)|\g<1>마법협회]]",
    r"\[\[(?:[^|\]]*?(?:심연의 군단|오벨리스크 카르텔)[^|\]]*?)(?:\|([^\]]+))?\]\]": r"[[01-8. 세력 아카이브 (국가·조직 정리)\4. 오벨리스크 대륙 (Obelisk Continent)\1. 심연 군단 (Abyssal Legion)|\g<1>심연 군단]]",
    r"\[\[(?:[^|\]]*?(?:해적 연합|해양 동맹)[^|\]]*?)(?:\|([^\]]+))?\]\]": r"[[01-8. 세력 아카이브 (국가·조직 정리)\5. 해양 대륙 (Oceanic Continent)\1. 해적 연합 (Pirate Confederacy)|\g<1>해적 연합]]",
    r"\[\[(?:[^|\]]*?(?:드워프 왕국|딥 포지 왕국)[^|\]]*?)(?:\|([^\]]+))?\]\]": r"[[01-8. 세력 아카이브 (국가·조직 정리)\3. 프로스트 대륙 (Frost Continent)\1. 딥 포지 왕국 (Deep Forge Kingdom)|\g<1>드워프 왕국]]",
}

def clean_label(match_str):
    # This prevents duplication like "자유도시연합자유도시연합"
    # Actually just simplifying standard names
    pass

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    changes_made = False
    
    for pattern, replacement in mappings.items():
        if re.search(pattern, new_content):
            # Simplistic but effective targeted replacement.
            # We don't want to replace with "\g<1>성국" if \g<1> is None.
            # To be safer let's use a function
            def repl(m):
                label = m.group(1) if m.group(1) else m.group(0).strip("[]").split("|")[-1]
                # the hardcoded parts in replacement. we need to map based on the specific term.
                # Let's just use the target label.
                # E.g. replace '성국' with absolute path + label.
                target_path = replacement.split("|")[0].replace("[[", "")
                
                # To prevent double replacing "성국" in a path we already fixed:
                if "01-8. 세력 아카이브" in m.group(0):
                    # Already partly or fully fixed, let's still ensure it's exactly correct
                    return f"[[{target_path}|{label}]]"
                return f"[[{target_path}|{label}]]"
            
            new_content = re.sub(pattern, repl, new_content)
            changes_made = True
            
    if changes_made:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated links in: {os.path.basename(filepath)}")

for d in directories:
    for root, dirs, files in os.walk(d):
        for f in files:
            if f.endswith('.md'):
                process_file(os.path.join(root, f))
print("Link update complete.")
