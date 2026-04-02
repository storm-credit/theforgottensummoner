import os
import glob
import re

hero_dir = r"C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)"
class_dir = r"C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-20. 직업 & 클래스 (Classes & Jobs)\직업 도감"

# Get all class files
class_files = {}
for root, _, files in os.walk(class_dir):
    for f in files:
        if f.endswith(".md"):
            class_files[f] = os.path.join(root, f)

# Parse heroes
hero_data = []
for root, _, files in os.walk(hero_dir):
    for f in files:
        if f.endswith(".md"):
            hero_name = f.replace(".md", "")
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Extract summary
            summary = ""
            sum_match = re.search(r'\* \s*\*\*한 줄 요약\*\*:\s*(.*)', content)
            if sum_match:
                summary = sum_match.group(1).strip()
            else:
                lore_match = re.search(r'## 📖 인물 서사.*?\n+(.*?)\n', content, re.DOTALL)
                if lore_match and len(lore_match.group(1)) > 10:
                    summary = lore_match.group(1)[:100].replace("[[", "").replace("]]", "") + "..."
                else:
                    summary = "아스트라리스 세계의 굳건한 영웅."
                    
            text = content.lower()
            jobs = set()
            
            # Heuristics
            if any(k in text for k in ["기사", "검술", "기사단"]): jobs.add("06. 기사 (Knight).md")
            if any(k in text for k in ["성기사", "팔라딘", "신성"]): jobs.add("07. 성기사 (Paladin).md")
            if any(k in text for k in ["수도승", "무투"]): jobs.add("09. 수도승 (Monk).md")
            if any(k in text for k in ["이단 심문관", "처형인"]): jobs.add("17. 이단 심문관 (Inquisitor).md")
            
            if any(k in text for k in ["사제", "교단", "성녀"]): jobs.add("08. 사제 (Cleric).md")
            if any(k in text for k in ["마법사", "마탑", "원소"]): jobs.add("10. 마법사 (Mage).md")
            if any(k in text for k in ["흑마법사", "저주"]): jobs.add("22. 흑마법사 (Warlock).md")
            if any(k in text for k in ["연금술", "포션"]): jobs.add("11. 연금술사 (Alchemist).md")
            if any(k in text for k in ["강령술", "언데드"]): jobs.add("15. 강령술사 (Necromancer).md")
            
            if any(k in text for k in ["암살", "단검", "그림자"]): jobs.add("12. 암살자 (Assassin).md")
            if any(k in text for k in ["용병", "유격대장"]): jobs.add("19. 용병 (Mercenary).md")
            if any(k in text for k in ["항해사", "해적", "함대"]): jobs.add("04. 항해사 (Navigator).md")
            if any(k in text for k in ["정찰병", "추적자"]): jobs.add("20. 정찰병 및 추적자 (Scout & Tracker).md")
            if any(k in text for k in ["사냥", "헌터"]): jobs.add("몬스터 헌터 (Monster Hunter).md")
            if any(k in text for k in ["현상금 사냥꾼"]): jobs.add("21. 현상금 사냥꾼 (Bounty Hunter).md")
            
            if any(k in text for k in ["주술사", "샤먼", "부족"]): jobs.add("23. 주술사 및 샤먼 (Shaman).md")
            if any(k in text for k in ["정령사", "정령"]): jobs.add("27. 정령사 (Spirit Summoner).md")
            if any(k in text for k in ["드루이드", "자연 수호자"]): jobs.add("28. 드루이드 및 자연 수호자 (Druid).md")
            
            if any(k in text for k in ["무희", "첩자"]): jobs.add("24. 무희 및 첩자 (Dancer).md")
            if any(k in text for k in ["밀수꾼"]): jobs.add("25. 밀수꾼 (Smuggler).md")
            if any(k in text for k in ["도적", "무법자", "산적"]): jobs.add("26. 도적 및 무법자 (Rogue & Outlaw).md")
            
            if any(k in text for k in ["검투사", "투기장"]): jobs.add("29. 검투사 (Gladiator).md")
            if any(k in text for k in ["전투 마법사"]): jobs.add("30. 전투 마법사 (Battlemage).md")
            if any(k in text for k in ["마검사"]): jobs.add("31. [히든] 마검사 (Magic Swordsman).md")
            if any(k in text for k in ["핏빛 군주", "혈귀"]): jobs.add("32. [히든] 핏빛 군주 (Blood Lord).md")
            
            if any(k in text for k in ["심마니", "채집"]): jobs.add("02. 심마니 (Herb Gatherer).md")
            if any(k in text for k in ["음유시인", "바드"]): jobs.add("05. 음유시인 (Bard).md")
            if any(k in text for k in ["기록관", "역사학자"]): jobs.add("33. 기록관 및 역사학자 (Archivist - Historian).md")
            if any(k in text for k in ["이계 소환사", "소환술"]): jobs.add("34. 이계 소환사 (Otherworldly Summoner).md")
            
            if len(jobs) == 0:
                jobs.add("19. 용병 (Mercenary).md")
                
            hero_data.append({"name": hero_name, "summary": summary, "jobs": list(jobs)})

inject_count = 0
for hero in hero_data:
    for job_filename in hero['jobs']:
        target_path = class_files.get(job_filename)
        if not target_path:
            # Fallback search
            for c_f, path in class_files.items():
                if job_filename in c_f or c_f in job_filename:
                    target_path = path
                    break
                    
        if target_path:
            try:
                with open(target_path, 'r', encoding='utf-8') as file:
                    class_content = file.read()
                    
                if hero['name'] not in class_content:
                    inject_string = f"*   **[[{hero['name']}]]**: {hero['summary']}"
                    
                    # Look for ## 🔗
                    if "\n---\n\n## 🔗" in class_content:
                        class_content = class_content.replace("\n---\n\n## 🔗", f"\n{inject_string}\n\n---\n\n## 🔗")
                    elif "\n---\n\n## 5." in class_content:
                        class_content = class_content.replace("\n---\n\n## 5.", f"\n{inject_string}\n\n---\n\n## 5.")
                    elif "<!-- HERO_INJECT_ANCHOR -->" in class_content:
                        class_content = class_content.replace("<!-- HERO_INJECT_ANCHOR -->", f"<!-- HERO_INJECT_ANCHOR -->\n{inject_string}")
                    else:
                        class_content += f"\n{inject_string}\n"
                        
                with open(target_path, 'w', encoding='utf-8') as file:
                    file.write(class_content)
                inject_count += 1
            except Exception as e:
                pass

print(f"Injection Complete: {inject_count} mappings inserted!")
