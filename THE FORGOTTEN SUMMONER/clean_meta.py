import os
import re
import glob

folder = r"C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 백과 (Hero Archive)\01-14-2. 현존 영웅\7. 무소속 영웅"
files = glob.glob(os.path.join(folder, "*.md"))

meta_keywords = ['고어', '삼류', '폐기', '삭제', '잔혹극', '역겨운', 'B급', '다크 설정', '설정은 지워버립니다', '배격하고', '단일명에서 벗어나']

for path in files:
    if "_Index.md" in path or "15-2" in path: continue
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Remove [초기화 및 검증] section
    # Matches "## 🛑 [초기화 및 검증]" up to "---" right before "## 👤 [A. 캐릭터 기본 파라미터 (Core Identity)]"
    pattern = r'## 🛑 \[초기화 및 검증\].*?---\s*(?=## 👤 \[A\.)'
    content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    # 2. Remove meta lines in the text (like "안구가 터진다는 삼류 묘사를 폐기...")
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        has_meta = any(kw in line for kw in meta_keywords)
        # If the line is purely a meta comment bullet or text in the penalty section, skip it
        if has_meta and ("**'성흔의 거룩한" not in line and "**'별빛의 공명통" not in line and "**'성좌의 맹목" not in line and "**'무중력의" not in line and "**'빛의 포식" not in line and "**'눈보라의" not in line and "**'영원의 극치" not in line): 
            continue
        
        # If the line contains lore PLUS meta like "- **'영원의 극치 현상'**: ~ 삭제합니다."
        if has_meta and "**: " in line:
            # We keep the bold title but remove the meta sentence if it's there
            parts = line.split("**: ")
            if any(kw in parts[1] for kw in meta_keywords):
                # Just change the line to the title only, or skip if it was just meta
                if "현상" in parts[0] or "로어" in parts[0] or "페널티" in parts[0] or "대가" in parts[0]:
                    new_lines.append(parts[0] + "**: 우주적 등가교환의 가혹한 섭리가 발현됩니다.")
                    continue
        new_lines.append(line)
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))
        
print("Meta commentary removed from all generated files.")
