import os
import shutil

base_dir = r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-41. 마도 교통 백과"

dirs = [
    "1. 대륙 간 육상 교통망 (Overland)",
    "2. 해상 교역로와 항구 (Maritime)",
    "3. 공중 항로와 부유 성채 (Aerial)",
    "4. 차원의 문과 공간 도약 (Dimensional)",
    "5. 교통 패권 전쟁 (Politics)",
    r"1. 대륙 간 육상 교통망 (Overland)\1-1. 육상 교역망과 루트 (Networks)",
    r"1. 대륙 간 육상 교통망 (Overland)\1-2. 육상 이동 수단 (Vehicles)",
    r"2. 해상 교역로와 항구 (Maritime)\2-1. 주요 해상 항로 및 항구 (Routes & Hubs)",
    r"2. 해상 교역로와 항구 (Maritime)\2-2. 해상 이동 수단 (Vessels)",
    r"3. 공중 항로와 부유 성채 (Aerial)\3-1. 공중 비행 궤도와 성역 (Skyways)",
    r"3. 공중 항로와 부유 성채 (Aerial)\3-2. 공중 이동 수단 (Aircrafts)",
    r"4. 차원의 문과 공간 도약 (Dimensional)\4-1. 워프 게이트 네트워크 (Warp Gates)"
]

for d in dirs:
    os.makedirs(os.path.join(base_dir, d), exist_ok=True)

moves = {
    "1. 대륙 간 육상 교통망과 이동 수단 (Overland Networks & Vehicles).md": 
        r"1. 대륙 간 육상 교통망 (Overland)\01. 육상 교통 개요.md",
    "2. 해상 교역로와 잊혀진 항구의 지배자 (Maritime Routes & Naval Hubs).md": 
        r"2. 해상 교역로와 항구 (Maritime)\02. 해상 교통 개요.md",
    "3. 공중 항로와 부유하는 하늘의 성채 (Aerial Routes & Sky Cities).md": 
        r"3. 공중 항로와 부유 성채 (Aerial)\03. 공중 교통 개요.md",
    "4. 차원의 문과 마법 교통 (Dimensional & Magical Transit).md": 
        r"4. 차원의 문과 공간 도약 (Dimensional)\04. 차원 교통 개요.md",
    "5. 교통 패권과 대륙 간 전쟁의 역사 (Transportation Politics & Warfare).md": 
        r"5. 교통 패권 전쟁 (Politics)\05. 교통 물류 패권 전쟁의 역사.md"
}

for src, dst in moves.items():
    src_path = os.path.join(base_dir, src)
    dst_path = os.path.join(base_dir, dst)
    if os.path.exists(src_path):
        shutil.move(src_path, dst_path)

main_overview = os.path.join(base_dir, "0. 마도 교통 백과 개요.md")
if not os.path.exists(main_overview):
    with open(main_overview, "w", encoding="utf-8") as f:
        f.write("# 0. 마도 교통 백과 개요\n\n> *\"아스트라리스 세계관의 문명과 전장, 그리고 무역로를 관통하는 육/해/공/차원 마도 인프라의 마스터 분류 지침서.\"*\n\n이 백과는 아스트라리스 크로니클 내 에테리움 동력과 정령, 그리고 마수들을 활용한 육해공 마도 교통망과 이동 수단 체계를 세부적으로 다룹니다.\n\n각 항목은 '경로망(Networks)'과 '이동 수단(Vehicles)'으로 나뉘어 방대한 세계관의 디테일을 구축합니다.")

print("Restructuring Complete.")
