import os
import shutil

dirs_to_copy = [
    # 첩보 5개
    (r"3. 첩보 (Intelligence)\5. 황금 손아귀 (Golden Claw)", r"6-7. 그림자 첩보 조직 (Shadow Intelligence)\5. 황금 손아귀 (Golden Claw)"),
    (r"3. 첩보 (Intelligence)\4. 황야의 추적자들 (Hunters of the Wild)", r"6-7. 그림자 첩보 조직 (Shadow Intelligence)\4. 황야의 추적자들 (Hunters of the Wild)"),
    (r"3. 첩보 (Intelligence)\3. 검은 여우단 (Black Fox Syndicate)", r"6-7. 그림자 첩보 조직 (Shadow Intelligence)\3. 검은 여우단 (Black Fox Syndicate)"),
    (r"3. 첩보 (Intelligence)\2. 그림자 연맹 (Shadow Syndicate)", r"6-7. 그림자 첩보 조직 (Shadow Intelligence)\2. 창백한 거미줄 첩보망 (Pale Web Syndicate)"),
    (r"3. 첩보 (Intelligence)\1. 어둠의 손 (Shadow Hand)", r"6-7. 그림자 첩보 조직 (Shadow Intelligence)\1. 어둠의 손 (Shadow Hand)"),
    
    # 마법 5개
    (r"2. 마법연구조직 (Magic Research)\5. 심연의 별무리 (Stellar Abyss Collective)", r"6-6. 초국가 진리 연합 및 마탑 (Academia)\5. 심연의 별무리 (Stellar Abyss Collective)"),
    (r"2. 마법연구조직 (Magic Research)\4. 진실의 눈 (Eye of Truth)", r"6-6. 초국가 진리 연합 및 마탑 (Academia)\4. 진실의 눈 (Eye of Truth)"),
    (r"2. 마법연구조직 (Magic Research)\3. 차원 탐사단 (Dimensional Explorers)", r"6-6. 초국가 진리 연합 및 마탑 (Academia)\3. 차원 탐사단 (Dimensional Explorers)"),
    (r"2. 마법연구조직 (Magic Research)\2. 연금술사의 길드 (Guild of Alchemists)", r"6-6. 초국가 진리 연합 및 마탑 (Academia)\2. 연금술사의 길드 (Guild of Alchemists)"),
    (r"2. 마법연구조직 (Magic Research)\1. 천상의 서고 (Celestial Archive)", r"6-6. 초국가 진리 연합 및 마탑 (Academia)\1. 천상의 서고 (Celestial Archive)"),
    
    # 용병단 12개
    (r"1. 용병단(Mercenaries)\12. 자연의 방랑자 (Wanderers of Nature)", r"6-3. 대륙 용병단 (Mercenaries)\12. 자연의 방랑자 (Wanderers of Nature)"),
    (r"1. 용병단(Mercenaries)\11. 신성 계약단 (Divine Covenant)", r"6-3. 대륙 용병단 (Mercenaries)\11. 신성 계약단 (Divine Covenant)"),
    (r"1. 용병단(Mercenaries)\10. 강철의 형제단 (Brotherhood of Steel)", r"6-3. 대륙 용병단 (Mercenaries)\10. 강철의 형제단 (Brotherhood of Steel)"),
    (r"1. 용병단(Mercenaries)\9. 황금 기계단 (Golden Mechanists)", r"6-3. 대륙 용병단 (Mercenaries)\9. 황금 기계단 (Golden Mechanists)"),
    (r"1. 용병단(Mercenaries)\8. 바이퍼 해적단 (Viper Raiders)", r"6-3. 대륙 용병단 (Mercenaries)\8. 바이퍼 해적단 (Viper Raiders)"),
    (r"1. 용병단(Mercenaries)\7. 바람의 칼날 (Wind Blades)", r"6-3. 대륙 용병단 (Mercenaries)\7. 바람의 칼날 (Wind Blades)"),
    (r"1. 용병단(Mercenaries)\6. 철혈 부대 (Iron Blood Corps)", r"6-3. 대륙 용병단 (Mercenaries)\6. 철혈 부대 (Iron Blood Corps)"),
    (r"1. 용병단(Mercenaries)\5. 유랑 기사단 (Wandering Knights)", r"6-3. 대륙 용병단 (Mercenaries)\5. 유랑 기사단 (Wandering Knights)"),
    (r"1. 용병단(Mercenaries)\4. 검은 파도 용병단 (Black Tide Mercenaries)", r"6-3. 대륙 용병단 (Mercenaries)\4. 검은 파도 용병단 (Black Tide Mercenaries)"),
    (r"1. 용병단(Mercenaries)\3. 붉은 칼날 용병단 (Red Blades Mercenaries)", r"6-3. 대륙 용병단 (Mercenaries)\3. 붉은 칼날 용병단 (Red Blades Mercenaries)"),
    (r"1. 용병단(Mercenaries)\2. 그리핀 기사단 (Order of the Gryphon)", r"6-3. 대륙 용병단 (Mercenaries)\2. 그리핀 기사단 (Order of the Gryphon)"),
    (r"1. 용병단(Mercenaries)\1. 저주받은 용병단 (Cursed Mercenaries)", r"6-3. 대륙 용병단 (Mercenaries)\1. 저주받은 용병단 (Cursed Mercenaries)")
]

backup_base = r"C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\_Legacy_중립세력 (Backup)"
live_base = r"C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\6. 범대륙 초국가 및 중립 세력 (Supranational & Neutral)"

log_file = os.path.join(r"C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER", "copy_log.txt")

if os.path.exists(log_file):
    os.remove(log_file)

success_count = 0
for b_sub, l_sub in dirs_to_copy:
    src_dir = os.path.join(backup_base, b_sub, "9. 예하 부대 및 기사단 (Military Units)")
    dst_dir = os.path.join(live_base, l_sub, "9. 예하 부대 및 기사단 (Military Units)")
    
    if os.path.exists(src_dir):
        try:
            if os.path.exists(dst_dir):
                shutil.rmtree(dst_dir)
            os.makedirs(os.path.dirname(dst_dir), exist_ok=True)
            shutil.copytree(src_dir, dst_dir)
            success_count += 1
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(f"Copied: {src_dir} to {dst_dir}\n")
        except Exception as e:
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(f"ERROR COPYING {src_dir}: {str(e)}\n")
    else:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"MISSING SRC: {src_dir}\n")

with open(log_file, "a", encoding="utf-8") as f:
    f.write(f"DONE. {success_count} folders copied.\n")
