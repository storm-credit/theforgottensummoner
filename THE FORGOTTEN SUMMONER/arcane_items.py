import os

base_dir = r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-19. 아이템 도감 (Item Encyclopedia)\01-19-1. 무기 (Weapons)"

items = [
    {
        "folder": "12. 스태프 (Staves)",
        "filename": "통제와 심연의 지배 홀 (Scepter of Control and Abyssal Dominion).md",
        "title": "통제와 심연의 지배 홀 (Scepter of Control and Abyssal Dominion)",
        "tag_type": "staff",
        "rank": "mythic",
        "kor_rank": "신화급 🔴",
        "owner": "jeresys_arcadia",
        "owner_kor": "제레시스 아르카디아 (Jeresys Arcadia)",
        "type_str": "지팡이 (황실 권홀)",
        "desc": "권좌에 앉은 자는 일어서지 않는다. 발밑의 지맥이 몸소 그의 신경을 대변할 테니까.",
        "desc_src": "황제 즉위식 선서",
        "maker": "제1대 아르카디아 황제 및 신성 공방",
        "mat": "심연석 왕관 코어, 에테리움 압축금",
        "appearance": "한 손에 들어오는 짧고 육중한 황금빛 권홀. 끝부분에 매달린 투명한 마나 구슬 안에서 끊임없이 은하수의 축소판 같은 에테리움 파장이 소용돌이치고 있습니다.",
        "atk": "광역 마나 제압력 절대치",
        "dur": "파괴 면역 (마스터 종속)",
        "attr": "대지 마나 지맥 완전 통제",
        "attr_note": "마법 캐스팅 없이 광역기 자유자재 투사",
        "skill_name": "황제의 명 (Edict of the Emperor)",
        "skill_cond": "권홀을 지면에 내리찍으며 지맥과 공명함.",
        "skill_eff": "반경 1km 내에 분포된 적 군단의 영창 마법식 자체를 원천 무효화시키며, 대공간의 중력을 역전시켜 군대 전체를 공기 압박으로 압사시킵니다.",
        "skill_note": "마법에 대한 저항치가 높을수록 더욱 강력한 즉사 판정이 들어갑니다.",
        "sub_skill": "**침묵의 옥좌:** 제레시스를 제외한 모든 마법사의 마나 회로가 범위 내에서 50% 둔화됩니다.",
        "origin": "황제가 처음 심연과 계약했을 때, 통제를 상징하기 위해 자신과 심연의 경계를 깎아 만든 абсолют(절대) 매개체.",
        "lore": "협회 마도사들 사이에서는 이 홀 앞에서는 숨소리조차 권력의 지배를 받는다는 전설이 있습니다."
    },
    {
        "folder": "29. 마도구 (Magitek)",
        "filename": "영원 회귀의 시간 모래시계 (Hourglass of Eternal Recurrence).md",
        "title": "영원 회귀의 시간 모래시계 (Hourglass of Eternal Recurrence)",
        "tag_type": "magitek",
        "rank": "legendary",
        "kor_rank": "전설급 🟠",
        "owner": "xenos_arcadia",
        "owner_kor": "크세노스 아르카디아 (Xenos Arcadia)",
        "type_str": "마도구",
        "desc": "모래는 아래로만 떨어진다 착각하지 마라. 인과율은 내 손끝에서 역류할 수 있다.",
        "desc_src": "크세노스의 시간축 수정 전투 후",
        "maker": "고대 시간의 탑 초대 현자",
        "mat": "무한의 모래, 차원 결합 유리",
        "appearance": "손바닥보다 약간 큰 크기의 떠다니는 모래시계. 중력을 무시하고 위쪽으로 모래가 쏟아져 올라가거나 정지해 있는 등 기이한 시공간 왜곡을 물리적으로 보여줍니다.",
        "atk": "직접 타격력 0 (인과율 수정)",
        "dur": "외부 타격 무시 (투명화 상태 지속)",
        "attr": "타깃 시간축 강제 편집",
        "attr_note": "아성체급 심연 마수에게까지 통용",
        "skill_name": "크로노스 단층 (Chronos Fault)",
        "skill_cond": "시계의 상하를 뒤집고 마나 코어를 희생함.",
        "skill_eff": "적의 치명적인 참격이나 마법이 닿기 직전 1초 전으로 전체 필드의 시간을 정지 및 둔화시켜버려 아군이 무적의 템포에서 공격을 퍼붓게 만듭니다.",
        "skill_note": "공간을 정지시키는 것이 아닌 시간 프레임을 쪼개는 초고차원 권능.",
        "sub_skill": "**운명의 차감:** 적이 보유한 수명(남은 시간)을 빼앗아 모래시계의 동력으로 연료화합니다.",
        "origin": "시간 마법의 패널티로 소멸해간 아르카디아 선조들의 남은 수명과 마나를 모조리 압축시켜 응고시킨 유산.",
        "lore": "소유자는 전투에서 절대 패배하지 않으나, 대신 본인의 운명이 파괴된다는 가장 명예로운 저주를 담고 있습니다."
    },
    {
        "folder": "12. 스태프 (Staves)",
        "filename": "심연을 삼키는 어둠의 지팡이 (Staff of Darkness Swallowing the Abyss).md",
        "title": "심연을 삼키는 어둠의 지팡이 (Staff of Darkness Swallowing the Abyss)",
        "tag_type": "staff",
        "rank": "legendary",
        "kor_rank": "전설급 🟠",
        "owner": "marcus_corvus",
        "owner_kor": "마르쿠스 코르부스 (Marcus Corvus)",
        "type_str": "지팡이 (어둠 속성)",
        "desc": "네가 믿는 신은 너를 구원하지 못한다. 내 어둠만이 이 지옥을 끝낼 유일한 자비다.",
        "desc_src": "이단 심문관 학살 직전",
        "maker": "코르부스 가문 1대 흑마도사",
        "mat": "네메시스의 뼛조각, 응축된 그림자",
        "appearance": "주변의 광원을 모조리 블랙홀처럼 빨아들여 늘 칠흑 속에 덮여 있는 기형적인 곡선의 스태프. 끝부분에는 붉은 안구가 번쩍입니다.",
        "atk": "초광역 붕괴 타격급",
        "dur": "그림자로 수시 변환되어 파괴 불가",
        "attr": "빛 입자 절대 소멸 및 적성 마나 흡수",
        "attr_note": "광역 실명 및 적 무장 해제 효과",
        "skill_name": "칠흑의 아가리 (Maw of the Eclipse)",
        "skill_cond": "전장에 드리운 모든 그림자를 지팡이로 묶어 정렬함.",
        "skill_eff": "공간 상의 어둠을 초압축해 수십 대의 전함도 단숨에 씹어삼킬 거대한 흑염의 구를 투척, 심연 마수들의 사기(邪氣) 자체를 정화 소멸시킵니다.",
        "skill_note": "방어나 방패의 개념이 통하지 않는 존재론적 지우개 격발술.",
        "sub_skill": "**심연의 식욕:** 적병의 살점과 피를 흡수할 때마다 지팡이가 기분 나쁜 식살음을 냅니다.",
        "origin": "금단 서고의 최하층에 봉인되어 있던 재앙의 마도구를 마르쿠스 본인의 시야를 잃는 댓가로 제어해 낸 산물.",
        "lore": "흑마법사들은 이 무기가 자신들을 참수하는 단두대의 칼날이라 칭하며 공포에 떱니다."
    },
    {
        "folder": "29. 마도구 (Magitek)",
        "filename": "부정을 씻는 신성의 성광 (Holy Light Cleansing Impurity).md",
        "title": "부정을 씻는 신성의 성광 (Holy Light Cleansing Impurity)",
        "tag_type": "magitek",
        "rank": "legendary",
        "kor_rank": "전설급 🟠",
        "owner": "isadore_solea",
        "owner_kor": "이사도르 솔레아 (Isadore Solea)",
        "type_str": "마도구 (성십자 펜던트)",
        "desc": "우리의 기도는 단순히 눈물겨운 애원이 아닙니다. 대지를 침식하는 병균을 도려내는 매스입니다.",
        "desc_src": "이사도르의 최후의 기도",
        "maker": "최초의 빛의 교단 사제장",
        "mat": "응결된 여신의 눈물, 백금석",
        "appearance": "따스한 온기를 끊임없이 내뿜는 손바닥만 한 다이아몬드 형태의 백금 펜던트. 쥐는 순간 육신의 모든 탁한 기운이 정화되는 감정을 선사합니다.",
        "atk": "살상력 0 (언데드 및 심연 한정 극대치)",
        "dur": "주인의 신앙심과 마력이 계속되는 한 불멸",
        "attr": "초광역 자연 치유 및 악의 차단결계",
        "attr_note": "독, 저주, 역병계 100% 면역화",
        "skill_name": "새벽의 성좌 (Constellation of the Dawn)",
        "skill_cond": "피 흘리는 아군을 굽어보며 자신의 잔여 수명을 담보로 쥠.",
        "skill_eff": "하늘을 찢고 무수한 십자 형태의 빛의 기둥 폭격을 쏟아내, 심연 마수들을 순식간에 재사슬로 융해시키면서 아군의 절단된 사지마저 강제 봉합하는 기적을 일으킵니다.",
        "skill_note": "단 한 명의 아군도 포기하지 않는 철벽의 수호 결계.",
        "sub_skill": "**천사의 맥박:** 이사도르가 죽음에 가까워질수록 성광은 눈이 멀 정도로 찬란하게 증폭됩니다.",
        "origin": "성국의 탐욕스러운 주교들이 봉인해두려 했던 진정한 구원의 유물을, 마법협회가 목숨 걸고 빼돌려 이사도르에게 인도했습니다.",
        "lore": "빛은 오직 성국만의 전유물이 아님을 증명하는 마법협회 도덕성의 최종 병기입니다."
    },
    {
        "folder": "30. 기타 (Others)",
        "filename": "피의 매혹이 깃든 핏빛 제단 (Crimson Altar Imbued with Blood Charm).md",
        "title": "피의 매혹이 깃든 핏빛 제단 (Crimson Altar Imbued with Blood Charm)",
        "tag_type": "others",
        "rank": "epic",
        "kor_rank": "영웅급 🟣",
        "owner": "nerissa_sangard",
        "owner_kor": "네리사 샨가르드 (Nerissa Sangard)",
        "type_str": "기타 (이동식 의식 제단)",
        "desc": "한 방울의 피는 수만 명의 부대를 죽이는 전염병의 시작이 될 수 있지요.",
        "desc_src": "국경 요새 초토화 이후",
        "maker": "샨가르드 가문 흡혈 시조",
        "mat": "굳은 피의 결석, 백골(白骨) 지지대",
        "appearance": "허공에 반쯤 둥둥 떠서 네리사를 호위하듯 따라다니는 피 웅덩이 형태의 입방체 제단. 내부에서 혈관 같은 촉수들이 기형적으로 꿈틀거립니다.",
        "atk": "광역 신경망 붕괴",
        "dur": "피 흡수 시 내구도 무한 대형성",
        "attr": "대규모 혈류 적출 및 무기화",
        "attr_note": "적진 100% 흡혈 치사율",
        "skill_name": "진홍의 왈츠 (Waltz of the Crimson)",
        "skill_cond": "전장에 뿌려진 피 냄새 수치 임계점 도달.",
        "skill_eff": "적들이 흘린 피를 허공으로 끌어올려 단분자 수준의 날카로운 핏빛 바늘 수만 개로 경화시킨 뒤, 전 방위로 쏘아보내 적군을 말 그대로 고기 다지기처럼 짓이겨 버립니다.",
        "skill_note": "피부가 조금이라도 긁힌 자라면 그 상처에서 피가 역류해 목을 조르게 됩니다.",
        "sub_skill": "**선혈의 최면:** 제단이 뿜는 혈향을 맡은 병사들은 뇌신경이 타들어가 네리사의 명령에 따르는 꼭두각시 시체가 됩니다.",
        "origin": "뱀파이어 군주들을 학살하고 그들의 심장을 갈아붙여 완성한 광기의 예술품.",
        "lore": "아군조차 이 제단 앞에서는 자신의 맥박 소리를 억누르려 애쓴다고 합니다."
    },
    {
        "folder": "12. 스태프 (Staves)",
        "filename": "자유로운 나비의 환영 지팡이 (Illusionary Staff of the Free Butterfly).md",
        "title": "자유로운 나비의 환영 지팡이 (Illusionary Staff of the Free Butterfly)",
        "tag_type": "staff",
        "rank": "epic",
        "kor_rank": "영웅급 🟣",
        "owner": "lianna_somnua",
        "owner_kor": "리안나 솜누아 (Lianna Somnua)",
        "type_str": "지팡이 (환술 특화)",
        "desc": "저들에게 진짜 칼이 꽂혔는지는 중요치 않아요. 칼이 꽂혔다고 믿게 만든다면, 심장은 멈추게 되어 있으니까.",
        "desc_src": "적 지휘관 집단 심장마비 사건 후",
        "maker": "환영의 전당 은둔 마도사",
        "mat": "투명한 마녀의 눈물, 꿈을 가둔 자수정",
        "appearance": "손가락 하나로도 들어올릴 만큼 비정상적으로 가벼운 유리세공 지팡이. 끝에 달려 있는 수정에서 푸른 나비 형태의 마나 입자들이 나불나불 흩날립니다.",
        "atk": "물리 데미지 0 (정신 파괴 극상)",
        "dur": "물리 방어 전무, 그러나 실체를 찾을 수 없음",
        "attr": "광역 인식 조작 및 자아 분열",
        "attr_note": "환성/후각/촉각 동시 구현",
        "skill_name": "몽환의 늪 (Morass of Illusions)",
        "skill_cond": "지팡이를 허공에 부유시키고 자장가를 영창.",
        "skill_eff": "전장 한복판에 적 병사들이 가장 두려워하는 악몽(또는 가장 사랑하는 가족)을 시각적으로 실체화시켜 투영합니다. 피비린내 나는 군단이 무기를 버리고 허공을 껴안다 광기로 집단 붕괴하게 만듭니다.",
        "skill_note": "아무리 강력한 방패를 가졌더라도 눈꺼풀을 꿰뚫는 마법은 막지 못합니다.",
        "sub_skill": "**무의식 해킹:** 지팡이에 닿은 적은 혼절상태의 아군이 되어 적장의 목을 치러 달려갑니다.",
        "origin": "평민이었던 리안나가 귀족들의 압제에서 벗어나기 위해 현실 자체를 부정하는 과정에서 깨달은 상상의 궁극적 실체.",
        "lore": "그녀의 나비를 추적한 자들은 모두 미궁 벼랑에서 미소 지은 채 시체로 발견되었다고 합니다."
    },
    {
        "folder": "30. 기타 (Others)",
        "filename": "공간을 베어내는 차원의 문 열쇠 (Dimensional Gate Key Slashing Space).md",
        "title": "공간을 베어내는 차원의 문 열쇠 (Dimensional Gate Key Slashing Space)",
        "tag_type": "others",
        "rank": "legendary",
        "kor_rank": "전설급 🟠",
        "owner": "serios_ventaris",
        "owner_kor": "세리오스 벤타리스 (Serios Ventaris)",
        "type_str": "기타 (특수 차원 장비)",
        "desc": "닫을 수 없는 문은 없다. 베어낼 수 없는 허공 역시 단 하나도 없다.",
        "desc_src": "초거대 차원 게이트 붕괴 직전",
        "maker": "벤타리스 가문 차원 융합체",
        "mat": "이차원 운석 금속, 공간 고정 핀",
        "appearance": "열쇠라기 보다는 날카로운 검은색 메스의 형상. 손잡이 버튼을 누르면 칼날 대신 이공간을 찢는 비가시적 미세 진동 파장이 뻗어나갑니다.",
        "atk": "무한대 (공간 절단 시 방어구 무시)",
        "dur": "반영구. 차원 좌표 귀속",
        "attr": "절대 물리 절단 & 전송",
        "attr_note": "마나 실드 및 물리 장갑 100% 투과 베기",
        "skill_name": "단절의 지평선 (Horizon of Severance)",
        "skill_cond": "열쇠를 허공에 꽂아 넣고 공간 좌표를 이탈시킴.",
        "skill_eff": "적 군단의 돌격 루트 중간에 보이지 않는 차원의 균열을 유리창 깨듯 만들어냅니다. 그 선을 넘어오는 병사나 마수들은 질량을 상실하고 원자 단위로 깔끔하게 절개되어 소멸합니다.",
        "skill_note": "막거나 피할 수 없는, 세계의 설정 자체를 지워버리는 흉기.",
        "sub_skill": "**즉각 전송:** 공간의 일부를 잘라내 적장의 심장만 내손 안으로 바로 우편 전송시킵니다.",
        "origin": "차원의 뒤틀림을 연산하기 위해 세리오스 본인의 우측 눈 시력을 제물로 바쳐 벼려낸 궁극의 메스.",
        "lore": "세리오스가 검지를 들어올릴 때마다 대륙의 지도가 매번 다시 그려진다는 숭배의 상징입니다."
    },
    {
        "folder": "12. 스태프 (Staves)",
        "filename": "해방을 부르는 불사조의 겁화 (Hellfire of the Phoenix Calling for Liberation).md",
        "title": "해방을 부르는 불사조의 겁화 (Hellfire of the Phoenix Calling for Liberation)",
        "tag_type": "staff",
        "rank": "epic",
        "kor_rank": "영웅급 🟣",
        "owner": "valias_ignarion",
        "owner_kor": "발리아스 이그나리온 (Valias Ignarion)",
        "type_str": "지팡이 (둔기 혼용 스태프)",
        "desc": "이론과 주문 따위는 귀족 나리들이나 읊으라지. 내 마법은 타격 한 번이면 충분해!",
        "desc_src": "고대 화룡의 두개골을 박살 내며",
        "maker": "빈민가 대장장이와 용암 화구",
        "mat": "지옥불 마석, 화염룡의 허벅지뼈",
        "appearance": "마법 지팡이라 부르기 민망할 정도로 거칠고 무모하게 융접된 거대한 붉은 쇳덩이. 상단부에 고정된 지옥불 마석은 주변 산소를 상시 연소시킵니다.",
        "atk": "지진 타격 및 초폭염 혼합살상",
        "dur": "절대 영도 상태 외력에 방어",
        "attr": "물리 마찰 계수 연소 증폭",
        "attr_note": "타격 부위에서 2차 열압력탄 폭발",
        "skill_name": "라그나로크의 숨결 (Breath of Ragnarok)",
        "skill_cond": "발리아스의 아드레날린과 분노치가 맹목적 상한선 돌파.",
        "skill_eff": "지팡이를 몽둥이처럼 쥐고 지면이나 적 흉갑에 풀돌격으로 내려찍으면, 응축된 불꽃 코어가 터지며 화산 폭발급 지진 해일이 일어나 심연 마수 정예대를 통째로 가루로 만듭니다.",
        "skill_note": "마법과 무투파의 특성을 동시에 발휘하므로 사거포착이 불가능한 파괴 전차.",
        "sub_skill": "**잿더미 복원:** 발리아스의 상처를 불길로 지져 임시로 지혈 수복시키는 야만적 치유 기능을 지녔습니다.",
        "origin": "협회의 무긴 억압된 분노들을 모두 모아 화염룡 뼈다귀에 깡그리 녹여 부었더니 탄생한 혁명의 괴기물.",
        "lore": "귀족 마법사들의 유리 벽을 깨부수고 자유를 선포하는 가장 무식하고 아름다운 불기둥이라 불립니다."
    },
    {
        "folder": "26. 마도서 (Grimoires)",
        "filename": "비밀을 속삭이는 심연의 금서 (Forbidden Book of the Abyss Whispering Secrets).md",
        "title": "비밀을 속삭이는 심연의 금서 (Forbidden Book of the Abyss Whispering Secrets)",
        "tag_type": "grimoire",
        "rank": "epic",
        "kor_rank": "영웅급 🟣",
        "owner": "elias_nocturne",
        "owner_kor": "엘리아스 녹턴 (Elias Nocturne)",
        "type_str": "마도서",
        "desc": "책장을 열어라. 네놈들이 영원히 감추고 싶어 했던 종말의 진실을 내가 한 자 한 자 낭독해 주지.",
        "desc_src": "엘리아스의 진혼곡 도입부",
        "maker": "금단 서고의 첫 번째 배신자",
        "mat": "저주받은 양피지 꾸러미, 살아 움직이는 잉크",
        "appearance": "사람의 가죽으로 제본되었다는 소문이 짙은 기분 나쁜 자줏빛 대형 고서. 책이 스스로 맥박 뛰듯 숨을 쉬며 주변의 소리를 잉크로 자동 필사합니다.",
        "atk": "무형성 광역 디버프 (저주력 극상)",
        "dur": "파쇄 불가능 (찢어도 영혼으로 재봉합)",
        "attr": "타깃 마나 코어 신경독 잠식",
        "attr_note": "적의 방어 진형 지속적인 자멸 유도",
        "skill_name": "야상곡의 사문난적 (Heresy of the Nocturne)",
        "skill_cond": "책 위로 적장 핏방울 스캔 및 깃펜 영창 착수.",
        "skill_eff": "적들의 신체 정보 및 약점이 잉크 문자로 추출당하며, 그 문자를 엘리아스가 지워버리거나 붉은색으로 그어버림과 동시에 현장의 적병들이 피를 쏟고 급사하는 부두 저주 살상기.",
        "skill_note": "주무기 없이 책 하나로 수천 명의 심근경색을 조작하는 미친 암살 도구.",
        "sub_skill": "**활자 분열:** 마도서가 거미떼 같은 흑백 활자로 분열해 기사들의 갑옷 틈새를 기어 다니며 눈과 귀를 멀게 합니다.",
        "origin": "협회가 은폐하려던 뒷골목의 더러운 역사들을 모아 엘리아스가 본인의 영혼 자락을 접착제로 발라 만든 사적 심판물.",
        "lore": "지식을 통제하려 드는 오만한 자들의 혈통을 말려버리는 흑막의 바이블입니다."
    },
    {
        "folder": "30. 기타 (Others)",
        "filename": "진실을 기록하는 지혜의 깃펜 (Quill of Wisdom Recording Truth).md",
        "title": "진실을 기록하는 지혜의 깃펜 (Quill of Wisdom Recording Truth)",
        "tag_type": "others",
        "rank": "epic",
        "kor_rank": "영웅급 🟣",
        "owner": "cassian_veritas",
        "owner_kor": "카시안 베리타스 (Cassian Veritas)",
        "type_str": "기타 (오퍼레이팅 촉매제)",
        "desc": "한 번 엇나간 펜촉은 다시 주워담을 수 없듯, 전쟁의 톱니바퀴 역시 단 한 번의 오차도 용납하지 않는다.",
        "desc_src": "카시안의 후방 지휘 막사에서",
        "maker": "베리타스 가문 대제사장",
        "mat": "정령 부엉이 화석 깃털, 아카식 광석",
        "appearance": "순백의 섬세한 기운이 감도는 부드러운 깃펜. 종이가 없어도 허공에 아름다운 금빛 마나 수식을 실시간으로 필기해 냅니다.",
        "atk": "지원 및 전술 버프력 절대치",
        "dur": "반영구 (마나로 수복)",
        "attr": "아크(차원) 데이터 해독 및 연산 증폭",
        "attr_note": "동맹군 사망률 0% 극한 조율",
        "skill_name": "아카식의 궤적 (Trajectory of the Akashic)",
        "skill_cond": "허공에 광활한 전장 지도를 마나 입자로 드로잉함.",
        "skill_eff": "깃펜이 그려낸 궤적을 따라 아군 수백 명의 망막에 적의 공격 사거리와 이동루트가 1.5초 선행 예지되어 투여됩니다. 적이 손을 들 때 아군은 이미 회피 후 카운터 공격을 끝마치는 기적적 효율을 연출합니다.",
        "skill_note": "무력형이 아닌 연산 증강형의 지존급 지휘 지팡이.",
        "sub_skill": "**진리의 첨삭:** 치명상 통각을 순간 지워버려 아군이 고통 없이 후방으로 자력 탈출하게 돕습니다.",
        "origin": "역사를 조작하려는 황제들에 맞서 피눈물을 흘리며 밤을 새워 진실을 적어 내렸던 지식 수호자들의 정수.",
        "lore": "카시안의 펜 놀림 한 번이 소드마스터 천 명의 칼부림보다 대륙 지도를 빠르게 넓힌다고 평가받습니다."
    },
    {
        "folder": "29. 마도구 (Magitek)",
        "filename": "과거의 영광을 비추는 고대 석판 (Ancient Slate Illuminating the Glory of the Past).md",
        "title": "과거의 영광을 비추는 고대 석판 (Ancient Slate Illuminating the Glory of the Past)",
        "tag_type": "magitek",
        "rank": "legendary",
        "kor_rank": "전설급 🟠",
        "owner": "theresa_antiqua",
        "owner_kor": "테레사 안티콰 (Theresa Antiqua)",
        "type_str": "마도구 (공중 부양 석판 포대)",
        "desc": "이 가련한 현대의 공식을 보라. 신들이 별을 빚던 시절의 언어 단 한 글자에 쓸려 나가는 것을.",
        "desc_src": "테레사의 적군 마나 실드 강제 해체 시점",
        "maker": "태초의 아르카디아 문명 공학자",
        "mat": "창성석(Genesis Stone), 잊혀진 언어 금형",
        "appearance": "사람 몸집만 한 묵직하고 각진 바빌론 양식의 거대 석판. 지팡이 따위 쓰지 않고 공중에 3개를 띄워, 표면에 인각된 황금빛 고대 문자들을 빔 포대처럼 발사합니다.",
        "atk": "원초적 질량 함포 투사급",
        "dur": "세계 멸망 전까지 파괴 보류",
        "attr": "구시대 방어 수식 100% 분쇄 딜링",
        "attr_note": "마나 쉴드 및 이공간 방어 절대 파열",
        "skill_name": "아틀란티스의 개안 (Eclipse of the Ancestors)",
        "skill_cond": "석판 3개가 정삼각형의 포격 진형을 하늘에 전개함.",
        "skill_eff": "석판 중앙에서 모여든 태초의 빛의 기둥이 위성 레이저처럼 대지를 향해 수직 낙하합니다. 복잡한 마나 공식 찌꺼기 없이 순수 소스 코드로 찍어부르는 파괴의 폭력에 일대 지형이 가루로 갈려 나갑니다.",
        "skill_note": "소형 전함급의 이동 화력을 한 개인이 쏟아붓는 말도 안 되는 아티팩트.",
        "sub_skill": "**조상들의 탄식:** 석판에서 울려 퍼지는 초음파가 적군의 고막과 평형 감각을 철저히 유린합니다.",
        "origin": "테레사가 육신의 절반이 부서지는 저주를 감내하며 사막 깊은 곳 묻힌 수도원 최하층을 삽으로 직접 파내어 등짐 지고 온 국보급 광기.",
        "lore": "역사를 조작하려는 오만이 이 석판의 첫 번째 포격 버튼 리셋으로 지워졌다는 기록을 갖습니다."
    },
    {
        "folder": "30. 기타 (Others)",
        "filename": "잊혀진 시간의 유적 탐사등 (Ruins Exploration Lantern of Forgotten Time).md",
        "title": "잊혀진 시간의 유적 탐사등 (Ruins Exploration Lantern of Forgotten Time)",
        "tag_type": "others",
        "rank": "epic",
        "kor_rank": "영웅급 🟣",
        "owner": "lucien_artifex",
        "owner_kor": "루시엔 아르티팩스 (Lucien Artifex)",
        "type_str": "기타 (전술 탐사 및 분쇄 복합 장비)",
        "desc": "함정이 작동하기 전에 기어박스를 곡괭이 돌려 까기로 부수면 그만이야. 그게 내가 사는 방식이라고.",
        "desc_src": "초급수 살인 트랩 속 결사 해체작업",
        "maker": "루시엔 본인의 불법 뒷골목 개조",
        "mat": "강화 철제 램프, 고대 폭약 코어",
        "appearance": "수만 번 찍히고 긁힌 투박한 황동색 탐사용 램프. 하지만 내부 동력원에서는 적의 장갑 결합부와 마법 구동 조인트를 X-ray처럼 스캔해 내는 푸른 섬광이 예리하게 빛납니다.",
        "atk": "국소 급소 타격의 물리적 데미지 극대화",
        "dur": "폭탄 터져도 멀쩡한 티타늄 합금",
        "attr": "물리/마비 트랩 자동 투시 및 결계 무력화",
        "attr_note": "대형급 공성 병기 1초 분해능력",
        "skill_name": "파스투아의 해체 기하학 (Deconstruction Geometry of Fastua)",
        "skill_cond": "루시엔이 램프 고출력 스캔 후 곡괭이를 치켜듦.",
        "skill_eff": "램프의 빛이 적 거대 괴수나 공성 골렘의 가장 취약한 마디 부위를 마름모꼴로 강제 록온합니다. 이후 곡괭이 형태의 둔기로 그 1점만 타격하면, 건물이 도미노처럼 무너지듯 적들이 연쇄 붕괴를 일으킵니다.",
        "skill_note": "가장 비마법사다운 무식함으로 가장 완벽한 해체 마공을 선보이는 무구.",
        "sub_skill": "**도굴꾼의 직감:** 등불의 붉은 불빛 점멸 속도로 주변의 매복병과 은신 마수를 초단위로 탐지해 냅니다.",
        "origin": "유적 매몰 사고로 팔이 잘려 나간 동료들을 구하기 위해 지하 폭약을 뜯어다 자신의 눈과 등불을 하나로 개조해버린 미친 생존본능의 결정구.",
        "lore": "서고에서 커피나 마시는 귀족 놈들에겐 평생 쥐어지지 않을 가장 더럽고 숭고한 흙투성이 랜턴입니다."
    }
]

template = """---
tags:
  - item/weapon
  - rank/{rank}
  - owner/{owner}
  - faction/arcane_society
  - type/{tag_type}
aliases:
  - {eng_name}
  - {kor_name}
type: item
---

# {title}

> *"{desc}"*
> — {desc_src}

---

## 1. 기본 정보

| 항목 | 내용 |
|------|------|
| **분류** | 무기 — {type_str} |
| **등급** | **{kor_rank}** |
| **가치** | 산출 불가 (마법협회 특급 비품/국보급) |
| **현재 소유자** | [[{owner_kor}]] |
| **세력 귀속** | [[마법협회 (Arcane Society)]] |
| **제작자/장인** | {maker} |
| **재료** | {mat} |
| **거래 가능 여부** | 거래 불가 (귀속) |
| **강화 가능 여부** | 특수 조건부 강화 / 불가 |

### 외형 묘사
{appearance}

---

## 2. 성능 및 효과 (Stats & Effects)

| 유형 | 효과 | 비고 |
|------|------|------|
| **기본 성능** | 공격/방어력: {atk} | 내구도: {dur} |
| **속성** | {attr} | {attr_note} |

### **고유 능력: 《{skill_name}》**
- **발동 조건:** {skill_cond}
- **효과:** {skill_eff}
- **특이 사항:** {skill_note}

### 보조 능력
- {sub_skill}

---

## 3. 배경 스토리 & 전승 (Lore)

### 제작 기원
{origin}

### 전승
{lore}

### 관련 캐릭터
- [[{owner_kor}]]

---

## 4. 등장 장면 (Appearances)

| 챕터/화 | 장면 요약 |
|--------|----------|
| 미정 | 향후 서사에서 갱신 예정 |

---

## 5. 입수 경로 & 퀘스트 (Acquisition)

- **획득처:** 마법협회 특수 하사, 전장 획득 혹은 유적 발굴
- **관련 퀘스트:** -

---

## 🔗 관련 문서
- [[{owner_kor}]]
- [[마법협회 (Arcane Society)]]
"""

for item in items:
    # Build content
    kor_name = item["title"].split(" (")[0]
    eng_name = item["title"].split("(")[1].replace(")", "")
    
    content = template.format(
        rank=item["rank"],
        owner=item["owner"],
        tag_type=item["tag_type"],
        eng_name=eng_name,
        kor_name=kor_name,
        title=item["title"],
        desc=item["desc"],
        desc_src=item["desc_src"],
        type_str=item["type_str"],
        kor_rank=item["kor_rank"],
        owner_kor=item["owner_kor"],
        maker=item["maker"],
        mat=item["mat"],
        appearance=item["appearance"],
        atk=item["atk"],
        dur=item["dur"],
        attr=item["attr"],
        attr_note=item["attr_note"],
        skill_name=item["skill_name"],
        skill_cond=item["skill_cond"],
        skill_eff=item["skill_eff"],
        skill_note=item["skill_note"],
        sub_skill=item["sub_skill"],
        origin=item["origin"],
        lore=item["lore"]
    )
    
    # Save file
    target_dir = os.path.join(base_dir, item["folder"])
    if not os.path.exists(target_dir):
        os.makedirs(target_dir, exist_ok=True)
        
    out_path = os.path.join(target_dir, item["filename"])
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created/Updated: {out_path}")

print("Arcane Society: 12 pure item enclycopedia pages successfully deployed.")
