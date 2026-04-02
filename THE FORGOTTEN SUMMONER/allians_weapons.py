import os
import glob

base_dir = r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-19. 아이템 도감 (Item Encyclopedia)\01-19-1. 무기 (Weapons)"

items = [
    {
        "folder": "02. 양손검 (Two-handed Swords)",
        "filename": "강철왕의 패검 (Blade of Dominion).md",
        "title": "강철왕의 패검 (Blade of Dominion)",
        "tag_type": "two_handed_sword",
        "rank": "mythic",
        "kor_rank": "신화급 🔴",
        "owner": "leonhart_cameloth",
        "owner_kor": "레온하르트 카멜로스 (Leonhart Cameloth)",
        "type_str": "양손검",
        "desc": "이 검이 무겁게 느껴진다면, 아직 왕관을 쓸 자격이 없는 것이다.",
        "desc_src": "카멜로스 왕가의 기록",
        "maker": "초대 전시 대장장이",
        "mat": "선대 왕들의 마나 골수, 대산맥의 심장 쇳덩이",
        "appearance": "성인 남성의 키를 훌쩍 뛰어넘는 거대한 칠흑빛 대검. 장식이 거의 없고 투박하지만, 검운상에 선혈을 흡수할 때마다 붉게 달아오르는 금이 가 있습니다.",
        "atk": "요새 단층 파괴급",
        "dur": "반영구적. 금이 갈지언정 절대 부러지지 않음",
        "attr": "압도적 질량 밀도",
        "attr_note": "물리적 중력 300% 왜곡 타격",
        "skill_name": "강철왕의 칙령",
        "skill_cond": "검자루에 피를 흘려 완전한 마나 동기화.",
        "skill_eff": "공간을 찢는 대신 공간 자체의 중력을 무겁게 뭉개버려 반경 수백 미터 적들의 무기를 강제로 땅에 떨어뜨리게 압각합니다.",
        "skill_note": "거대한 둔기처럼 적 방어벽을 통째로 함몰시킵니다.",
        "sub_skill": "**피의 구속:** 칼날과 스친 적의 상처는 재생력을 상실하고 지속적인 압박 대미지를 받습니다.",
        "origin": "왕국을 통일하는 과정에서 베어낸 7명의 반역 영주들의 무기를 녹여 단 하나의 검으로 주조했습니다.",
        "lore": "소유자가 치른 피의 양만큼 무거워진다는 전승이 있어, 평범한 전사는 이 검의 칼자루조차 땅에서 들어 올릴 수 없습니다."
    },
    {
        "folder": "29. 마도구 (Magitek)",
        "filename": "기하학 컴퍼스 (Geometric Compass).md",
        "title": "파브리스의 기하학 컴퍼스 (Geometric Compass of Fabrice)",
        "tag_type": "magitek",
        "rank": "legendary",
        "kor_rank": "전설급 🟠",
        "owner": "gerard_fabrice",
        "owner_kor": "제라르드 파브리스 (Gerard Fabrice)",
        "type_str": "마도구 (전술/방어용)",
        "desc": "이 세상에서 계산되지 못할 죽음은 없다.",
        "desc_src": "요새 건축 설계도 머리말",
        "maker": "파브리스 백작 본인",
        "mat": "성운 은합금, 공존의 마수 수정",
        "appearance": "단검 겸용으로 접힐 수 있는 차가운 은색 컴퍼스. 끝부분에 미세한 마력의 빛무리가 감돌며, 펴는 각도에 따라 대륙 지도가 렌더링됩니다.",
        "atk": "극히 낮음",
        "dur": "단단하나 마력 충격에 취약함",
        "attr": "공간 렌더링 좌표화",
        "attr_note": "환술 및 시야 방해 100% 면역",
        "skill_name": "요새화 프로토콜",
        "skill_cond": "미리 지정해둔 마력 함정 좌표 3개소와 공명.",
        "skill_eff": "적들이 밟고 있는 맨땅에서 즉석으로 30피트 두께의 마나 콘크리트 장벽을 실체화시켜 적군을 완전히 가두어버립니다.",
        "skill_note": "개인의 무력보다 지형 자체를 아군 무기로 변환시킵니다.",
        "sub_skill": "**공간 왜곡 일지:** 침투하는 적 암살자의 이동 경로를 수학적으로 일그러뜨려 환영 속에 가둬버립니다.",
        "origin": "강력한 마수들을 지능적으로 방어하기 위해 수백 번 고쳐 쓴 파브리스 지식의 결정체.",
        "lore": "칼이 아니라 펜과 작도구로도 수만 명을 도륙할 수 있다는 지적 학살의 상징적인 도구입니다."
    },
    {
        "folder": "01. 한손검 (One-handed Swords)",
        "filename": "단죄검 (Blade of Condemnation).md",
        "title": "레가스의 단죄검 (Blade of Condemnation)",
        "tag_type": "one_handed_sword",
        "rank": "epic",
        "kor_rank": "영웅급 🟣",
        "owner": "dominic_regas",
        "owner_kor": "도미닉 레가스 (Dominic Regas)",
        "type_str": "한손검 (대검 보조용)",
        "desc": "네놈의 변명은 사후세계에서 들어주지. 하지만 지금은 부서져라.",
        "desc_src": "도미닉의 돌격 명령",
        "maker": "레가스 가문의 전속 제련장 마티아스",
        "mat": "검은 번개석 광석, 투사의 징표 조각",
        "appearance": "전방의 체중을 싣기 위해 칼날 후반부가 극단적으로 넓고 묵직한 흑색 철검입니다. 장식조차 없어 커다란 쇳덩어리를 다듬어 낸 듯한 흉악한 외형입니다.",
        "atk": "단일 대상 장갑 절단급",
        "dur": "절대 영구 마모 회피",
        "attr": "저항 분쇄",
        "attr_note": "물리 관통 300% 추가 적용",
        "skill_name": "선고의 참격",
        "skill_cond": "적을 정면으로 노려보며 퇴로를 포기한 상태.",
        "skill_eff": "공기마저 베어내는 극단적인 밀도의 참격을 날려 성기사의 결계조차 단숨에 동강 내버립니다.",
        "skill_note": "막아내는 행위 자체가 적의 무기를 박살내버리기 때문에 회피 외에는 답이 없습니다.",
        "sub_skill": "**피의 맹약:** 참격 시전자의 고통에 비례해 칼날 끝에 검기가 사선 모양으로 더욱 폭넓게 폭발합니다.",
        "origin": "도미닉이 첫 전장에서 부러진 창날과 패잔병들의 철조각을 결합해 살아남았던 상징을 정식으로 복각한 무기.",
        "lore": "우직하고 더러운 전선 백병전에서 레가스 가문을 이끌어온 단순무식한 충직함 그 자체로 여겨집니다."
    },
    {
        "folder": "07. 창 (Spears)",
        "filename": "은빛 폭풍의 랜스 (Lance of Silver Tempest).md",
        "title": "은빛 폭풍의 랜스 (Lance of Silver Tempest)",
        "tag_type": "spear",
        "rank": "epic",
        "kor_rank": "영웅급 🟣",
        "owner": "bernard_silverlance",
        "owner_kor": "베르나르드 실버랜스 (Bernard Silverlance)",
        "type_str": "창 (기창)",
        "desc": "은빛 궤적이 지나간 자리에 적군은 남지 않을 것이다.",
        "desc_src": "실버랜스 기병대의 출정가",
        "maker": "폭풍 기병단 마도 공병대",
        "mat": "비룡의 날개뼈 합금, 백금",
        "appearance": "3미터에 달하는 길고 뾰족하며 날렵한 은색 기창. 바람 저항을 최소화하도록 나선형 홈이 파여져 있습니다.",
        "atk": "거대 질량 관통급",
        "dur": "탄력이 뛰어나 쉽게 구부러지지 않음",
        "attr": "초고속 기동 공명",
        "attr_note": "기승체 스피드 200% 증가",
        "skill_name": "폭풍 관통",
        "skill_cond": "기동 가속도 100km 임계점 도달.",
        "skill_eff": "적진의 방망을 순식간에 관통해버리며 기창 끝단에 소닉붐 폭발을 일으켜 주변 보병진을 튕겨냅니다.",
        "skill_note": "일격 필살의 파괴력만을 보장하고 돌격 외의 방어엔 취약합니다.",
        "sub_skill": "**가속 배리어:** 속도가 빠를수록 기창 끝에서부터 원추형 마나 배리어가 일시적으로 전개됩니다.",
        "origin": "기수와 안장, 기창이 한 몸이 되도록 특수 고안된 백작가의 결전 병기.",
        "lore": "귀족 특유의 고고함과 돌격의 무자비함이 결합된, 대평원을 장악하는 연합군의 상징입니다."
    },
    {
        "folder": "07. 창 (Spears)",
        "filename": "청뢰의 기창 (Lightning Lance).md",
        "title": "청뢰의 기창 (Lightning Lance)",
        "tag_type": "spear",
        "rank": "epic",
        "kor_rank": "영웅급 🟣",
        "owner": "calric_bluestrike",
        "owner_kor": "칼릭 블루스트라이크 (Calric Bluestrike)",
        "type_str": "창 (기창)",
        "desc": "번개는 핏줄과 가문을 가리지 않고 공평하게 대가리를 깬다.",
        "desc_src": "칼릭의 제1 초소 명언록",
        "maker": "벨가르드 야전 대장장이",
        "mat": "야생 청색 마력석, 투박한 강철봉",
        "appearance": "화려한 정련 과정 없이 실용성만을 극대화한 푸른빛의 거칠고 투박한 강철 기창. 손잡이에 마찰 전기가 끊임없이 튑니다.",
        "atk": "순간 전격 마비 타격급",
        "dur": "전투 중 날이 부러지면 벼락결정으로 자동 연장됨",
        "attr": "뇌전 돌파",
        "attr_note": "금속 갑주 타격 시 100% 감전",
        "skill_name": "청뢰 방전",
        "skill_cond": "적 대열 한가운데 궤도를 포착하고 마나 개방.",
        "skill_eff": "지면을 찍고 솟구쳐오르며 푸른 번개를 폭발시켜 반경 수십 미터 적군의 중추신경을 모조리 마비시킵니다.",
        "skill_note": "단기 돌파력이 최고점에 달하는 순간 유격전으로 적진을 농락합니다.",
        "sub_skill": "**실용주의 투지:** 1대 다수로 병력 차이가 클 때 번개의 사거리 출력이 한 단계 높아집니다.",
        "origin": "야전에서 망가진 무기들을 긁어모아 평민 마법사들이 번개 코어를 심어준 반항아의 창.",
        "lore": "장식 하나 없는 투박함 속에서 벼락 같은 실력으로 기병대장의 자리를 쟁취한 칼릭의 증명물입니다."
    },
    {
        "folder": "02. 양손검 (Two-handed Swords)",
        "filename": "불굴의 철권검 (Ironfist Sword of Resolve).md",
        "title": "불굴의 철권검 (Ironfist Sword of Resolve)",
        "tag_type": "two_handed_sword",
        "rank": "legendary",
        "kor_rank": "전설급 🟠",
        "owner": "edward_steelhart",
        "owner_kor": "에드워드 스틸하트 (Edward Steelhart)",
        "type_str": "양손검",
        "desc": "이 손에서 검이 떨어질 때는 오직 내 목이 떨어지는 순간뿐이다.",
        "desc_src": "에드워드, 40시간 결사 항전을 끝마치며",
        "maker": "의지의 전당 결사대",
        "mat": "절대 파손 불가 요새 축성 합금",
        "appearance": "건틀릿(철권) 자체가 검자루 부분과 일체형으로 용접되어, 팔을 검 자체에 밀어넣어 고정하는 특이한 백병전 대검. 핏자국이 겹겹이 굳어 있습니다.",
        "atk": "극강 방어 역반격",
        "dur": "무한내성 초합금",
        "attr": "진형 사수",
        "attr_note": "넉백(밀려남) 100% 면역",
        "skill_name": "진지 참호 전개",
        "skill_cond": "검의 끝을 진흙투성이 대지에 박음.",
        "skill_eff": "지층 자체를 밀어올려 전방에 임시 석조 참호를 끌어올려, 동료들이 숨어들 공간과 화살 방패를 мгновенно 제공합니다.",
        "skill_note": "개인의 데미지 출력보다는 소속 병사들의 진지 확보를 최우선으로 합니다.",
        "sub_skill": "**고통 치환:** 철권 방패면이 타격받을수록 스틸하트 부대원들의 체력이 틱 단위로 회복됩니다.",
        "origin": "한계를 넘어 팔 근육이 파열되어 검을 떨어뜨리는 병사들을 보고 스틸하트 본인이 직접 고안한 '무기 귀속' 병기.",
        "lore": "화려함은 배제하고 가장 처절하고 진흙투성이인 서민 병사들과 운명을 같이 하는 왕국연합의 척추와 같습니다."
    },
    {
        "folder": "09. 둔기 (Blunt Weapons)",
        "filename": "대지의 분쇄망치 (Warhammer of Earthshattering).md",
        "title": "대지의 분쇄망치 (Warhammer of Earthshattering)",
        "tag_type": "blunt_weapon",
        "rank": "epic",
        "kor_rank": "영웅급 🟣",
        "owner": "alexander_ironstone",
        "owner_kor": "알렉산더 아이언스톤 (Alexander Ironstone)",
        "type_str": "둔기 (워해머)",
        "desc": "문이 단단하게 닫혀있다면, 벽째로 부숴버리면 그만이지.",
        "desc_src": "적 요새 진입 전 포효",
        "maker": "아이언스톤 가문 최고위 파괴술사",
        "mat": "응축된 단층 지진석 코어, 운석 강철",
        "appearance": "어깨에 메기도 버거운 초거대형 쇠망치. 헤드 양옆에 가스 배출구 같은 구멍이 있어 타격 시 압축된 충격파를 배출합니다.",
        "atk": "건축물 즉각 붕괴급",
        "dur": "마모 없음, 강도 극한",
        "attr": "공성 파괴 타격",
        "attr_note": "방패 방어 시도 시 피해 200% 증가",
        "skill_name": "철거의 굉음",
        "skill_cond": "공중에 도약하여 적군의 가장 단단한 방진 타격.",
        "skill_eff": "메테오가 떨어지는 듯한 파멸적인 중력 붕괴를 일으켜 적들의 포메이션 전체를 지반째 꺼트려 으깨버립니다.",
        "skill_note": "마법적 실드조차 물리적 으깨짐으로 산산결절시킵니다.",
        "sub_skill": "**잔혹한 관성:** 무기를 허공에 휘두르는 궤적 자체에 회오리가 발생해 잡병들은 바람만으로 육신이 찢깁니다.",
        "origin": "전선의 단병접전이 아닌 요새 포격전 자체를 근거리에서 치르기 위해 제작된 인간용 공성 병기.",
        "lore": "알렉산더의 통제 불능한 파괴욕을 고스란히 담아, 아군 병사들마저 이 망치의 범위 내에 들어가지 않으려 도망칩니다."
    },
    {
        "folder": "30. 기타 (Others)",
        "filename": "대지수호의 방패검 (Shield-sword of Earth Guard).md",
        "title": "대지수호의 방패검 (Shield-sword of Earth Guard)",
        "tag_type": "others",
        "rank": "epic",
        "kor_rank": "영웅급 🟣",
        "owner": "gareth_stoneblade",
        "owner_kor": "가레스 스톤블레이드 (Gareth Stoneblade)",
        "type_str": "기타 (방패 결합 대검)",
        "desc": "이 어둠과 절망의 비가 멈출 때까지, 내가 너희의 우산이 되리라.",
        "desc_src": "폭우 속 굶주린 병사들에게 건네는 위로",
        "maker": "성도 수호 장인 조합",
        "mat": "초고밀도 고대 성곽 잔해",
        "appearance": "칼날이라고 부르기 민망할 정도로 넓은 정사각형 철제 비석 형태입니다. 날 부분은 이가 빠져있어도 방어 면적이 성문 짝만 합니다.",
        "atk": "매우 무딘 둔격 타격",
        "dur": "자가 재생",
        "attr": "지형 동기화 절대 방어",
        "attr_note": "마법 폭격 90% 흡수",
        "skill_name": "거산의 장벽",
        "skill_cond": "방패검을 등 뒤의 아군을 향한 방향으로 수직 전개.",
        "skill_eff": "바위 절벽처럼 치솟는 물리적인 토템 장벽으로 자신과 아군 소대 전체를 차폐하여 적의 무수한 포격을 모두 흡수합니다.",
        "skill_note": "가레스의 체력이 남는 한 방어막이 절대 뚫리지 않는 처절한 희생기.",
        "sub_skill": "**아픔의 공유:** 반경 100미터 치명상을 입기 직전의 아군 군사들의 상처를 가레스의 갑주로 전이시켜 대신 버팁니다.",
        "origin": "공격에만 미쳐있는 연합군 전략 속에서 자신의 부대원만은 버리지 않겠다던 그의 고집에서 유래했습니다.",
        "lore": "화려한 명예는 없으나 가장 처절하고 눈물겨운 전선에서 아군 병사들의 신처럼 떠오른 무기입니다."
    },
    {
        "folder": "11. 활 (Bows)",
        "filename": "은빛 달의 투사궁 (Projection Bow of the Silver Moon).md",
        "title": "은빛 달의 투사궁 (Projection Bow of the Silver Moon)",
        "tag_type": "bow",
        "rank": "epic",
        "kor_rank": "영웅급 🟣",
        "owner": "selena_arsienne",
        "owner_kor": "셀레나 아르시엔 (Selena Arsienne)",
        "type_str": "활",
        "desc": "밤하늘의 달빛이 아름답다고? 그것이 네 심장을 꿰뚫는 내 화살촉일지도 모르는데.",
        "desc_src": "수면 중인 적장 참살 직전",
        "maker": "왕립 직속 지하 마도암살 공작소",
        "mat": "달의 기운이 밴 그림자 석영, 야광 거미줄 시위",
        "appearance": "빛을 받으면 투명하게 사라지는 은백색의 활 본체. 활시위에는 화살 없이 달가루가 부서지듯 푸른 에너지 화살이 맺혀 있습니다.",
        "atk": "극소 응축 점사 파괴력",
        "dur": "유연하고 형상 유지율 높음",
        "attr": "은밀 저격술",
        "attr_note": "풍향/중력 패널티 100% 무시",
        "skill_name": "달무리 요격",
        "skill_cond": "목표 대상의 맥박과 조준경 중앙을 싱크.",
        "skill_eff": "소리 잃은 무음의 섬광이 포물선 없이 직선으로 날아가 무려 반경 수 km 밖에 은신한 요인의 미간을 깔끔하게 관통합니다.",
        "skill_note": "마법 방어막의 결함(1mm) 틈새를 찾아 파고드는 극한의 정밀성을 자랑합니다.",
        "sub_skill": "**기척 절단:** 활사위를 당기는 순간 사수의 생명 파장과 냄새마저 대자연 속으로 지위집니다.",
        "origin": "고아 출신인 셀레나를 살인 귀신으로 키우기 위해 왕국 심문소가 억지로 부여한 저주의 장비.",
        "lore": "병사들의 고기방패 전략을 경멸하는 셀레나에게 단 한 발로 전장을 리셋시키는 마스터키로 여겨집니다."
    },
    {
        "folder": "04. 도 (Sabers)",
        "filename": "바람의 칼날 (Blade of Gale).md",
        "title": "바람의 칼날 (Blade of Gale)",
        "tag_type": "saber",
        "rank": "epic",
        "kor_rank": "영웅급 🟣",
        "owner": "brian_windslasher",
        "owner_kor": "브라이언 윈드슬래셔 (Brian Windslasher)",
        "type_str": "도 (한쪽 날만 있는 예기)",
        "desc": "눈에 보이는 철구슬은 피할 수 있지만, 살갗을 스치는 바람마저 피할 순 없지 않나.",
        "desc_src": "보수 기사들의 튜토리얼에서 박장대소하며",
        "maker": "유랑하는 엘프 무구 공방",
        "mat": "하늘 제비의 뼛가루, 창공 합금",
        "appearance": "칼날 표면에 투명한 기류가 소용돌이치며 끊임없이 잔상을 만들어 내는 극도 경량형의 비대칭형 검입니다.",
        "atk": "진공 절단력",
        "dur": "얇지만 마나 코팅으로 쉽게 꺾이지 않음",
        "attr": "기류 타격",
        "attr_note": "타격 시 소닉붐 발생, 상대 반사신경 파괴",
        "skill_name": "태풍참",
        "skill_cond": "자신의 스태미나와 공기 저항을 동기화하여 고도 비상.",
        "skill_eff": "허공에서 수백 개의 초승달 모양 압축 공기 칼날을 난사하여, 물리적 상처 없이 적들의 갑옷 틈새의 혈관만 끊어버립니다.",
        "skill_note": "회피력과 일격 이탈 전술에 특화된 극단적 공격 효율을 보유하고 있습니다.",
        "sub_skill": "**순풍 걷기:** 무기를 쥔 상태에선 병사들이 진흙을 수면처럼 밟고 지나가는 부유 패시브 부여.",
        "origin": "기사도의 고정 관념을 파괴하기 위해 이단적으로 받아들인 바람 정령술의 산물.",
        "lore": "연합 회의에서는 기사도의 수치라 비난받지만 전장에서는 가장 병력 소모가 적은 유격 기사의 애장품입니다."
    },
    {
        "folder": "29. 마도구 (Magitek)",
        "filename": "설계자의 차원 나침반 (Dimensional Compass of the Architect).md",
        "title": "설계자의 차원 나침반 (Dimensional Compass of the Architect)",
        "tag_type": "magitek",
        "rank": "legendary",
        "kor_rank": "전설급 🟠",
        "owner": "theoric_ironcaster",
        "owner_kor": "테오릭 아이언캐스터 (Theoric Ironcaster)",
        "type_str": "마도구 (전술 타격용)",
        "desc": "이 판 위에 찍힌 점들은 이미 시체들의 무덤일 뿐이다.",
        "desc_src": "테오릭, 지도 위에 핀을 꽂아 넣으며",
        "maker": "테오릭 가문 비밀 병기소",
        "mat": "봉인된 이그니션 스피어, 정밀 태엽 나사",
        "appearance": "회중시계 크기의 정교한 황동 나침반으로 열면 미니맵 홀로그램 위로 폭격의 예상 범위와 화력 파괴도가 수치화되어 떠오릅니다.",
        "atk": "군단급 초광역 붕괴",
        "dur": "정밀기기, 타격엔 취약",
        "attr": "원격 좌표 포격 동조",
        "attr_note": "지형 및 건축물 일격 분해",
        "skill_name": "차원 폭격 제어",
        "skill_cond": "나침반으로 조준된 적진 좌표에 마법 포병 부대 권한 오버라이드.",
        "skill_eff": "왕국 본진에 있는 거대 공성 마포나 광역 화염 마법의 타격 좌표를 오차 0mm로 순간 전송 유도하여 적 지대 자체를 지워버립니다.",
        "skill_note": "자비 없는 광역 희생을 동반하므로 민간 지대까지 휘말리는 악랄함이 있습니다.",
        "sub_skill": "**아군 생략 연산:** 폭격 지점 인근에 갇힌 미끼 아군 병력의 생명값을 0으로 연산해 지체 없이 포격 스크롤을 승인하는 광기.",
        "origin": "가문의 자서전을 불태우고 그 자리에 '승리'만을 위해 조립한 악마적인 참모 기어.",
        "lore": "성도와 인권을 논하는 외교관들이 가장 파괴하고 싶어 하는 테오릭의 통제권 상징물입니다."
    },
    {
        "folder": "16. 스태프 (Staves)",
        "filename": "업화의 소각 지팡이 (Incineration Staff of Hellfire).md",
        "title": "업화의 소각 지팡이 (Incineration Staff of Hellfire)",
        "tag_type": "staff",
        "rank": "legendary",
        "kor_rank": "전설급 🟠",
        "owner": "magnus_flamesorcerer",
        "owner_kor": "마그누스 플레임소서 (Magnus Flamesorcerer)",
        "type_str": "스태프",
        "desc": "나를 묶었던 이 쇠사슬이 녹아내릴 고열이라면, 감히 왕의 왕좌쯤은 잿더미로 만들 수 있겠지.",
        "desc_src": "마그누스의 은밀한 맹세",
        "maker": "마그누스 본인",
        "mat": "압수된 노예 쇠사슬 구속구, 지옥 화산석 무구",
        "appearance": "화려한 정석 지팡이가 아니라, 시꺼멓게 탄 나무 지지대에 붉게 달궈진 굵은 쇠사슬이 뱀처럼 감겨 있는 야만적인 무기.",
        "atk": "초장각 광역 용암화",
        "dur": "용융 불가의 용암 내구도",
        "attr": "압도적 초고열 타격",
        "attr_note": "불꽃 시전자 본인 타격 반사 0%",
        "skill_name": "해방의 불기둥",
        "skill_cond": "과거 노예 족쇄의 억압 구조를 마나 폭발로 해제.",
        "skill_eff": "지면이 갈라지며 일대의 흙바닥이 즉각 마그마로 끓어올라, 적 방벽이고 신성 기사단의 장갑차고 분자 단위로 녹여버립니다.",
        "skill_note": "적진의 후방까지 통과하는 불의 파도로 휩쓸며, 시야 확보와 초토화를 동시 수행합니다.",
        "sub_skill": "**사슬 채찍 타격:** 근거리에 접근하는 적들을 지팡이에 감긴 초고열 쇠사슬을 채찍처럼 휘둘러 토막 냅니다.",
        "origin": "가장 밑바닥 신분이었던 광산 노예 시절, 자신을 결박하던 영주의 사슬을 스스로 마나로 달구어 뽑아낸 분노의 결과물.",
        "lore": "귀족 기사들은 야만인의 쓰레기라 욕하지만, 이 지팡이 끝에서 떨어지는 불똥 하나만으로도 군단 하나가 지워집니다."
    }
]

template = """---
tags:
  - item/weapon
  - rank/{rank}
  - owner/{owner}
  - faction/allied_kingdoms
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
| **가치** | 산출 불가 (국보급 희귀) |
| **현재 소유자** | [[{owner_kor}]] |
| **세력 귀속** | [[왕국연합 (Allied Kingdoms)]] |
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

- **획득처:** 특별 세습, 전장 획득 혹은 유적 연성
- **관련 퀘스트:** -

---

## 🔗 관련 문서
- [[{owner_kor}]]
- [[왕국연합 (Allied Kingdoms)]]
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

print("Allied Kingdoms: 12 pure item enclycopedia pages successfully deployed.")
