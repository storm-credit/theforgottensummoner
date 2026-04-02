import os
import re

base_dir = r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 백과 (Hero Archive)\01-14-3. 소환 영웅"

replacements = {
    # A-Rank
    "19. 다리우스 아이언팽 (Darius Ironfang).md": "**[대지의 굴레 (Burden of the Earth)]** - 다리우스를 소환하여 적의 초강력 데미지를 막아낼 때마다, 대지의 무게를 대신 짊어져 에반의 뼈마디가 비명을 지르는 듯한 서사적 중압감과 깊은 체력 고갈을 감내해야 함.",
    "20. 엘리자 블랙스틸 (Eliza Blacksteel).md": "**[어둠의 맹약 (Vow of Shadows)]** - 초고속 암살 동선을 에반 본체가 지각하려 들면, 그림자를 넘나드는 기적의 대가로 한동안 빛을 잃은 듯 시야가 타들어가는 일시적 맹목(Tunnel Vision) 상태에 빠진 채 전투를 견뎌야 함.",
    # Legion 06 was made in turn 2
    "06. 심연의 철갑 마병단 (Ironclad Cavalry of the Abyss).md": "**[망령의 지휘봉 (Weight of the Doomed)]** - 300개의 유령 심장에 에반의 심장이 동기화되어, 영혼을 이끄는 전술 지휘관으로서 가슴이 조여드는 극심한 마력 스태미나 고갈과 숨 막히는 압박감을 치름.",
    "21. 고든 베오울프 (Gordon Beowulf).md": "**[광전사의 굴레 (Burden of the Berserker)]** - 야수의 끝없는 분노를 대신 짊어져, 에반의 근육이 찢어질 듯한 극심한 경련(마력 과열)을 겪으며 칼조차 정상적으로 쥐지 못하게 되는 전사로서의 극심한 탈진.",
    "22. 실비아 윈드워크 (Sylvia Windwalk).md": "**[바람의 눈속임 (Tears of the Wind)]** - 5km 바깥의 저격 시야를 동기화하기 위해 시력을 잠시 한계 이상으로 확장. 이후 에반의 시야엔 눈물이 고이고 반나절 동안은 사물이 흐려 보이는 치명적인 '마력 빛 번짐' 페널티에 시달림.",
    "07. 황동 나팔의 팔랑크스 (Phalanx of the Brazen Clarion).md": "**[수호자의 방패벽 (Shieldwall's Rebound)]** - 400명의 병사가 치르는 막대한 적의 충돌 압력을 전술 지휘관인 에반이 고스란히 영혼으로 수신. 적 돌진을 한 번 막을 때마다 에반의 갈비뼈에 엄청난 둔기가 부딪히는 듯한 숨 막히는 압박과 호흡 곤란을 겪음.",
    "08. 비탄의 포병대 (Artillery of Lamentation).md": "**[대지의 포효 진동 (Tremor of the Siege)]** - 150문의 대포가 동시에 뿜는 거대한 반동파를 부대장의 영혼으로 버텨냄. 엄청난 지축의 진동 때문에 고막이 터질 듯한 이명과 일시적 평형 감각 상실을 딛고 서 있어야 함.",
    "23. 아자젤 블러드본 (Azazel Bloodborn).md": "**[진혈의 서약 (Pact of True Blood)]** - 귀족 뱀파이어의 마력을 강제로 빌어 쓰는 대가로, 본체 생명력의 절반을 일시적으로 심연에 저당 잡힌 채 극도의 현기증과 스태미나 쇼크를 겪어야만 유지되는 오만한 금기.",
    "24. 발탄 스컬브레이커 (Valtan Skullbreaker).md": "**[심해의 억압 (Pressure of the Abyss)]** - 1만 미터의 수압 마법을 동기화하기에, 마력을 끊는 순간 온몸을 옥죄던 깊은 바다의 신성한 무게가 훅 풀려나가며 관절이 덜덜 떨리는 지독한 탈력감에 시달림.",
    "25. 셀레나 실버문 (Selena Silvermoon).md": "**[월광의 마리오네트 (Marionette of Moonlight)]** - 다수의 적 뇌를 조종하는 환상을 강제하기 위해 에반의 두뇌 연산력이 수십 배로 폭발. 해제 직후 에반은 거짓과 진실의 경계에서 시달리며 무거운 환각과 자아 분열적 혼란을 하루 종일 버텨야 함.",
    "09. 녹슨 사슬의 검투사들 (Gladiators of the Rusted Chain).md": "**[속박의 아드레날린 (Chains of Vigor)]** - 투기장의 거친 무규칙 생존열이 주인의 심장과 직결. 소환 즉시 몸에 불이 날 듯 맥박이 치솟지만 철수 후에는 전신의 힘이 풀려 그 자리에서 무릎을 꿇게 되는 극한의 흥분-소진 사이클.",
    "10. 역병 까마귀 비행단 (Plague Raven Squadron).md": "**[까마귀의 장막 (Veil of the Raven)]** - 수천 마리의 타락한 깃털 시야를 공유하느라 에반의 영혼이 독안개 속에 갇혀 극도의 현기증과 방향 상실을 겪으며, 잿빛 재(Ash)를 콜록거리며 뱉어내는 처절한 희생.",
    "05. 차원 유랑자 제로 (Zero the Dimensional Drifter).md": "**[시스템 오버로드 (System Overload)]** - 아스트라리스의 이치를 거스르는 무기를 쓰는 대가로, 에반의 대뇌를 연산 서버로 사용하게 되어 심각한 마력 편두통과 시야의 깨짐(노이즈) 같은 서사적 페널티 묘사를 가짐.",
    "06. 강철군주 메카트로닉스 (Mechatronics the Iron Lord).md": "**[플라즈마-싱크로 (Plasma Synchro)]** - 마나가 없는 군주의 코어를 에반의 영혼(배터리)으로 점화하므로, 메카가 방전될 때마다 에반의 몸속에 벼락이 치는 듯한 날카로운 뇌전 쇼크와 마비가 스쳐 지나감.",
    "06. 잊혀진 마왕의 그림자 (Shadow of the Forgotten Demon King).md": "**[절대 악의 심판 (Judgement of the Void)]** - 인과율을 거스르고 마왕의 잔재를 꺼내 부린 죗값으로, 마왕이 현현하는 매 1초마다 에반의 남은 수명과 영혼이 조금씩 갉아먹히는 최악의 생명 담보 룰렛.",
    "07. 심연의 리바이어던 (Leviathan of the Abyss).md": "**[가라앉은 호흡 (Drowned Breath)]** - 거대한 대양을 사막 위에 억지로 쏟아부은 거대한 기적의 대가. 에반 본인이 물 한 모금 마시지 않고도 폐 속에 무거운 바닷물을 머금은 듯 숨이 턱턱 막히고 가라앉는 호흡 곤란을 견뎌야 함.",
    "07. 시조의 나무 위그드라실의 잔재 (Remnant of Yggdrasil).md": "**[기원의 거름 (Tribute of Origins)]** - 세계수의 기적(부활)을 끌어올리기 위해 오직 소환사 자신의 생명력을 제물(거름)로 바쳐야 하기에, 스킬 시전 시 피부가 창백한 나무껍질처럼 변하며 체력이 바닥까지 소진되는 희생의 절정.",
    "01. 황금의 나비 (The Golden Butterfly).md": "**[인과율의 제물 (Sacrifice of Causality)]** - 세계의 시간을 강제로 되감은 대가. 타인의 목숨을 기워내는 대신 에반 본인의 가장 아름답고 소중했던 과거의 기억 한 조각이 나비의 인분처럼 부서져 영구히 망각되는 비참한 헌신.",
    "02. 운명의 방적기 (Loom of Destiny).md": "**[운명 반발의 저주 (Karma Rebound)]** - 패배했어야 할 파티의 인과율을 강제로 조작(Miss)하여 기적을 도둑질한 대가. 곧이어 필연적으로 우주의 분노가 에반 하나에게 쏠려 한동안 극도의 불행과 위협(우연한 사고)을 운명적으로 짊어져야 함."
}

def clean_file(path_str):
    with open(path_str, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(path_str)
    if filename not in replacements: return
    
    new_cost = replacements[filename]
    # 찾기 정규식 패턴: 10번 항목의 전체 줄
    pattern = r"(\-\ \*\*10\.\ 치명적 대가 \(Grim Plausibility & Overload Cost\)\*\*\:\s).*"
    
    match = re.search(pattern, content)
    if match:
        replaced_line = match.group(1) + new_cost
        new_content = re.sub(pattern, replaced_line, content)
        with open(path_str, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed tone in: {filename}")

for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith(".md"):
            clean_file(os.path.join(root, f))
