import os

base_dir = r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-19. 아이템 도감 (Item Encyclopedia)\01-19-1. 무기 (Weapons)"

items = [
    {
        "folder": "03. 단검 (Daggers)",
        "filename": "그림자절단의 단검 (Dagger of Shadowsevering).md",
        "title": "그림자절단의 단검 (Dagger of Shadowsevering)",
        "tag_type": "dagger",
        "rank": "legendary",
        "kor_rank": "전설급 🟠",
        "owner": "jayder_blackwind",
        "owner_kor": "제이더 블랙윈드 (Jayder Blackwind)",
        "type_str": "단검",
        "desc": "그림자는 결코 빛을 반사하지 않으며, 죽음은 소리내어 찾아오지 않는다.",
        "desc_src": "블랙윈드 가문 암살 교본",
        "maker": "그림자의 전당 고대 장인",
        "mat": "빛을 삼키는 심연석, 절망의 합금",
        "appearance": "칼날 자체가 빛을 반사하지 않는 침묵의 검은색이며, 허공을 그을 때마다 공간의 마나 파장마저 진공 상태로 빨아들이는 듯한 일그러짐이 발생합니다.",
        "atk": "극점 방어구 관통 타격급",
        "dur": "반영구적. 물리적 파손 내성 극대화",
        "attr": "마나 링크 침묵 결착",
        "attr_note": "물리 및 마법 결속 100% 절단",
        "skill_name": "심연의 맹점",
        "skill_cond": "타깃의 시야 사각지대에서 살기 0% 유지.",
        "skill_eff": "공격 경로 상의 모든 방어구 재질을 액체처럼 투과하여 대상의 심장과 마나 코어만을 물리적으로 적출해 내는 절대 암살 궤적을 긋습니다.",
        "skill_note": "상대가 방어막을 전개하는 행위 자체가 무의미해집니다.",
        "sub_skill": "**파장 삭제:** 타격하는 순간 발생하는 뼈 절단음과 충격파가 세계의 인식 시스템에서 강제 삭제됩니다.",
        "origin": "심연 군단의 지도자를 암살하기 위해 고독한 어둠 속에서 수십 년간 벼려낸 칠흑의 결정체.",
        "lore": "사용자의 투지가 불타오를수록 오히려 무기가 차갑게 얼어붙어 적을 기만하는 기괴한 물성을 지니고 있습니다."
    },
    {
        "folder": "02. 양손검 (Two-handed Swords)",
        "filename": "심연포효의 대검 (Greatsword of Abyssal Roar).md",
        "title": "심연포효의 대검 (Greatsword of Abyssal Roar)",
        "tag_type": "two_handed_sword",
        "rank": "legendary",
        "kor_rank": "전설급 🟠",
        "owner": "drake_roarson",
        "owner_kor": "드레이크 로어슨 (Drake Roarson)",
        "type_str": "양손검",
        "desc": "이 검이 뿜어내는 수왕의 포효 앞에서는, 오직 전진만이 허락된다.",
        "desc_src": "용병 연합 출정식",
        "maker": "골드마켓 대장간 길드 협동 제작",
        "mat": "심연 마수의 골격 코어, 피를 머금은 강철",
        "appearance": "일반적인 체구로는 들 수 없는 육중하고 거친 톱날형의 대검. 검신 곳곳에 짐승의 뼈 가시가 불규칙하게 돋아나 있습니다.",
        "atk": "전열 붕괴 초중량 타격급",
        "dur": "전장 피 흡수 시 자가 수리 버프",
        "attr": "야수적 질량 파동",
        "attr_note": "타격 시 30m 반경 적 사기 50% 하락",
        "skill_name": "괴수의 광란",
        "skill_cond": "전장의 피 냄새와 소유자의 아드레날린 최고치 도달.",
        "skill_eff": "검을 가로로 휘두르면 칼날에서 압축된 투기의 충격파가 거대한 사자의 턱처럼 사방으로 터져 나가, 중갑 기사단 한 중대를 통째로 날려 버립니다.",
        "skill_note": "섬세함과는 거리가 먼 극단적인 힘의 분출입니다.",
        "sub_skill": "**불굴의 폭주:** 데미지를 받을수록 대검에 서린 투기가 더욱 붉고 포악하게 일그러집니다.",
        "origin": "드레이크가 맨손으로 잡아찢은 심연 거북의 투박한 등갑을 그대로 녹여 칼잡이에 우겨넣은 파괴 무기.",
        "lore": "용병들에게는 승리를 부르는 토템이자, 적들에게는 지옥 문이 열리는 재앙의 신호탄으로 불립니다."
    },
    {
        "folder": "29. 마도구 (Magitek)",
        "filename": "절대 이행의 황금 계약서 (Golden Pact of Absolute Enforcement).md",
        "title": "절대 이행의 황금 계약서 (Golden Pact of Absolute Enforcement)",
        "tag_type": "magitek",
        "rank": "legendary",
        "kor_rank": "전설급 🟠",
        "owner": "marian_cardo",
        "owner_kor": "마리안 카르도 (Marian Cardo)",
        "type_str": "마도구",
        "desc": "가장 완벽한 감옥은 쇠창살이 아니라 서로의 합의로 만들어진 금화의 덫이다.",
        "desc_src": "마리안의 협상 테이블 종료 후",
        "maker": "고대 무역 도시의 대사제",
        "mat": "불멸의 황금 양피지, 지맥의 혈액 잉크",
        "appearance": "수백 년의 세월에도 닳지 않는 찬란한 황금빛 두루마리. 펼치면 서명자의 영혼과 공명하는 암흑 수식이 일렁입니다.",
        "atk": "무형의 제재 (논리적 파멸)",
        "dur": "절대 훼손 불가 (파훼 불능)",
        "attr": "절대 종속 제약",
        "attr_note": "계약 위반 시 영구적 마나 회로 붕괴",
        "skill_name": "자본주의적 파문",
        "skill_cond": "계약자의 묵시적 또는 명시적 계약 1조 위반 확정시.",
        "skill_eff": "계약을 어긴 대상의 체내 수분을 모두 황금빛 쇳물로 순간 치환시켜 버리며, 물리적 방어나 치유 마법이 일체 통용되지 않는 경제적 독살을 집행합니다.",
        "skill_note": "총도 칼도 없는 밀실에서 국가의 수장을 시체로 만들 수 있습니다.",
        "sub_skill": "**이익의 최면:** 문서를 읽고 있는 타깃은 자신의 손해를 가장 합리적인 성과라 착각하게 되는 환술에 걸립니다.",
        "origin": "황금의 전당 지하 가장 깊은 곳에 봉인되어 있던 고대 경제 제국의 패권 아이템.",
        "lore": "상대국의 군단 전체를 무덤으로 보내는 데 단 한 방울의 피도 요구하지 않는 가장 더러운 파멸의 유물입니다."
    },
    {
        "folder": "29. 마도구 (Magitek)",
        "filename": "탐욕의 차원 금고 (Dimensional Vault of Greed).md",
        "title": "탐욕의 차원 금고 (Dimensional Vault of Greed)",
        "tag_type": "magitek",
        "rank": "legendary",
        "kor_rank": "전설급 🟠",
        "owner": "edwin_cardas",
        "owner_kor": "에드윈 카르다스 (Edwin Cardas)",
        "type_str": "마도구",
        "desc": "네가 휘두르는 분노의 마나까지도, 결국 내게 진 빚의 원금에 불과하다.",
        "desc_src": "에드윈의 자산 동결 경고문",
        "maker": "초대 금고기사단 은행장",
        "mat": "공간 붕괴 축퇴성 마석, 미스릴 합금",
        "appearance": "한 손바닥 위에 올라가는 소형의 육면체 금고. 문이 열리는 순간 금고 내부가 이공간의 끝없는 심연과 연결된 블랙홀처럼 보입니다.",
        "atk": "마나 강제 징수 (비례 데미지)",
        "dur": "외력에 의한 파괴 및 해킹 불가",
        "attr": "마력 및 자산 흡착",
        "attr_note": "적의 공격 파장 100% 자산 흡수 변환",
        "skill_name": "강제 채권 징수",
        "skill_cond": "상대방이 에드윈을 적대하여 마나를 방출할 때.",
        "skill_eff": "적이 뿜어내는 마법이나 검기를 이공간 금고가 물리적으로 집어삼킨 뒤, 그 에너지를 곧바로 에드윈의 체력이나 금전적 가치로 암흑 변환해 버립니다.",
        "skill_note": "자신을 강하게 공격할수록 적 스스로가 파산(마나 고갈)하게 되는 질식 메커니즘.",
        "sub_skill": "**담보 화석화:** 흡수 상한치를 넘길 시 적의 갑옷과 육신 일부가 금화로 변이하여 부서집니다.",
        "origin": "빚을 갚지 못한 고위 마법사들과 왕족들의 영혼을 갈아 넣어 주조된 금융 패권의 절대 반지적 존재.",
        "lore": "자유도시의 모든 이권 싸움에서 은행이 언제나 최종 승리자가 되도록 보장하는 치트키 유물로 취급받습니다."
    },
    {
        "folder": "03. 단검 (Daggers)",
        "filename": "속삭임의 흑요석 단검 (Obsidian Dagger of Whispers).md",
        "title": "속삭임의 흑요석 단검 (Obsidian Dagger of Whispers)",
        "tag_type": "dagger",
        "rank": "epic",
        "kor_rank": "영웅급 🟣",
        "owner": "kalis_noir",
        "owner_kor": "칼리스 노이르 (Kalis Noir)",
        "type_str": "단검",
        "desc": "벽 없는 방에서도 벽이 듣고 있다는 공포, 그것이 내 통제력의 근원이지.",
        "desc_src": "정보상 칼리스 노이르의 신조",
        "maker": "그림자 일루셔니스트 집단",
        "mat": "지하수의 흑요석, 소리 잃은 인어의 비늘",
        "appearance": "날이 뭉툭하여 무기로서의 살상력은 바닥이지만, 칼자루 끝에 기괴한 귀 모양의 룬 투각이 붉게 빛나는 흑경 단검.",
        "atk": "치명성 제로 (물리 공격력 극하)",
        "dur": "유리처럼 얇으나 파괴 시 백업본 재생",
        "attr": "초장거리 도청 및 마나 공명",
        "attr_note": "반경 1km 무조건적 정보 수집",
        "skill_name": "바람의 밀고",
        "skill_cond": "특정 키워드를 사전 각인 후 벽이나 바닥에 단검을 꽂음.",
        "skill_eff": "키워드가 발상되는 순간, 1km 밖 적진의 모든 군사 작전회의 음성과 입모양 파장들이 단검을 통해 칼리스의 뇌리망으로 시각적 텍스트처럼 흘러들어갑니다.",
        "skill_note": "적의 전술 기만과 은폐 마법을 알고리즘 연산 수준으로 뚫어버립니다.",
        "sub_skill": "**진실의 환각:** 단검 근처의 적군들은 묘한 환청을 듣게 되어 스스로 의심과 분열에 빠집니다.",
        "origin": "칼리스가 암시장 바닥에서 거대 길드장들을 몰락시키기 위해 훔쳐냈던 전설적인 도청 아티팩트.",
        "lore": "자유도시의 어떤 귀족도 이 단검이 자신의 침상 밑에 꽂혀 있을까 두려워해 이불을 두 개 덮고 잔다고 합니다."
    },
    {
        "folder": "29. 마도구 (Magitek)",
        "filename": "심연 봉쇄의 인장 반지 (Signet Ring of Abyssal Seal).md",
        "title": "심연 봉쇄의 인장 반지 (Signet Ring of Abyssal Seal)",
        "tag_type": "magitek",
        "rank": "epic",
        "kor_rank": "영웅급 🟣",
        "owner": "cecilia_fairdealer",
        "owner_kor": "세실리아 페어딜러 (Cecilia Fairdealer)",
        "type_str": "마도구 (반지)",
        "desc": "이 차가운 금속 링 한 구멍 사이로, 너희의 수십만 병력이 퇴각할 것이다.",
        "desc_src": "세실리아의 외교 휴전식에서",
        "maker": "외교 전당의 대마법사 연맹",
        "mat": "심연의 억제석, 100년 묵은 정령은",
        "appearance": "세련되고 우아한 푸른 보석 알이 박힌 여성용 은반지. 하지만 보석 내부에 핏빛의 기하학적 족쇄 모양이 숨 쉬듯 명멸합니다.",
        "atk": "정치적 구속 (살상력 0)",
        "dur": "반영구 변형 불가",
        "attr": "적의 살의 원천 차단",
        "attr_note": "결속 시 상대 국가수장의 무장 해제 효과",
        "skill_name": "평화의 족쇄",
        "skill_cond": "상대 대표자와의 물리적 스킨십(악수) 또는 외교문서 도장 접촉.",
        "skill_eff": "타깃의 심부 마나 코어에 강제 휴전 코드를 이식하여, 적장이 배신을 도모하고 검을 뽑으려는 순간 근신경계 자체를 전기 쇼크로 마비시킵니다.",
        "skill_note": "상대의 자유의지를 논리적인 정치 계약으로 굴복시키는 무혈의 병기입니다.",
        "sub_skill": "**우아한 공황:** 반지가 뿜어내는 페로몬 파장이 상대 수행원들을 공황 상태에 빠뜨려 세실리아를 두려워하게 만듭니다.",
        "origin": "끝없는 암살과 전쟁을 문서로 묶기 위해 역대 수석 외교관들이 목숨을 걸고 개량해 온 정신 지배의 절정.",
        "lore": "아름다운 외모 뒤에 숨겨진 그 어떤 마검보다 잔혹한 독니라 불리며 경원의 표적이 됩니다."
    },
    {
        "folder": "30. 기타 (Others)",
        "filename": "운명 조작의 도박 주사위 (Dice of Fate Manipulation).md",
        "title": "운명 조작의 도박 주사위 (Dice of Fate Manipulation)",
        "tag_type": "others",
        "rank": "epic",
        "kor_rank": "영웅급 🟣",
        "owner": "lucas_goldchaser",
        "owner_kor": "루카스 골드체이서 (Lucas Goldchaser)",
        "type_str": "기타 (이능계 아티팩트)",
        "desc": "전장의 확률이 1%라면? 그 1%에 내 모가지와 이 주사위를 던질 뿐이지.",
        "desc_src": "카지노 습격 1분 전 뒷골목에서",
        "maker": "루카스 본인의 피 속 마나 공명체",
        "mat": "고대 상아, 잭팟의 혈흔석",
        "appearance": "루카스의 두 손가락 사이를 빙글빙글 도는 붉은색과 검은색의 앙증맞은 주사위 한 쌍. 각 면마다 악마와 천사, 해골 등이 조각되어 있습니다.",
        "atk": "확률에 따른 0 ~ 초차원 멸망급",
        "dur": "파손 불가이나 주사위 눈이 마모될 수 있음",
        "attr": "변수 창출 및 인과율 조작",
        "attr_note": "스킬 실패 시 본인 자멸 가능성 10%",
        "skill_name": "올인 (All-In)",
        "skill_cond": "적 대병력 한가운데서 주사위를 굴림.",
        "skill_eff": "특정 눈금 쌍이 터지면 하늘에서 초거대 메테오 골드바가 쏟아지거나 마수들이 개구리로 변하는 둥, 물리 법칙을 개무시하는 기적의 카지노 로또가 터집니다.",
        "skill_note": "적진 붕괴율은 최우수하나 1/1이 뜨면 자신의 무기가 소멸하는 극악의 밸런스 붕괴를 가집니다.",
        "sub_skill": "**행운 흡수:** 주사위가 공기 중의 적 마나(행운)를 빼앗아 상대방이 걸어가다 돌부리에 걸려 넘어지게 만듭니다.",
        "origin": "로토스 교단의 이단 사제가 만든 저주의 유물을, 루카스가 도박 한판으로 따내어 개량한 미친 무기.",
        "lore": "합리와 통계를 중시하는 군사학자들의 뇌에 마비와 분노를 일으키는 가장 불합리한 승리의 구심점."
    },
    {
        "folder": "30. 기타 (Others)",
        "filename": "철벽의 수문장 대방패 (Greatshield of the Bastion Gatekeeper).md",
        "title": "철벽의 수문장 대방패 (Greatshield of the Bastion Gatekeeper)",
        "tag_type": "others",
        "rank": "legendary",
        "kor_rank": "전설급 🟠",
        "owner": "balthazar_ravenheart",
        "owner_kor": "발타자르 라벤하트 (Balthazar Ravenheart)",
        "type_str": "기타 (초대형 방패)",
        "desc": "이 성벽이 밀려나면 그 뒤엔 벼랑뿐이다. 그러니 내 등 뒤를 피로 적시지 마라.",
        "desc_src": "실버포트 제3 성문 수성전 당시",
        "maker": "자유도시 건국 공병대",
        "mat": "초압축 흑장미 금속판, 지맥석기둥",
        "appearance": "방패라기보다는 대형 마차 문짝을 통째로 뜯어둔 듯한 위용. 흑색의 거대한 사각형 쇳덩어리에 수만 개의 화살촉 자국이 장식처럼 박혀 있습니다.",
        "atk": "무지막지한 강제 넉백 둔상",
        "dur": "무한내성",
        "attr": "지형 요새화 동기화",
        "attr_note": "폭격/공성 병기 데미지 100% 흡수반사",
        "skill_name": "결사항전의 토템",
        "skill_cond": "대방패를 지면에 박아 지력(地力)과 마나 링크 결속.",
        "skill_eff": "반경 200미터의 허공에 흑장미색 오라 장벽이 성곽 모양으로 솟구쳐, 심연 마수들의 초광역 브레스조차 흠집 하나 내지 못하게 차단합니다.",
        "skill_note": "방패 전개 중 발타자르의 두 다리는 돌덩이로 변해 기동력이 0이 되는 극한의 방위술입니다.",
        "sub_skill": "**사기 공명:** 등 뒤에서 떨고 있는 서민 출신 보병들에게 공포 면역과 체력 자연 회복 버프를 뿌려줍니다.",
        "origin": "도망치는 귀족 참모들을 욕하며, 무너지는 성문을 자신의 육신과 결합시켜버린 발타자르의 처절한 산물.",
        "lore": "기회주의의 도시 자유연합에서 유일하게 닻처럼 박혀있는 충직한 짐승의 무기로 칭송받습니다."
    },
    {
        "folder": "30. 기타 (Others)",
        "filename": "절망이 깃든 어둠의 망토 (Cloak of Despair-Infused Darkness).md",
        "title": "절망이 깃든 어둠의 망토 (Cloak of Despair-Infused Darkness)",
        "tag_type": "others",
        "rank": "epic",
        "kor_rank": "영웅급 🟣",
        "owner": "kyren_shadestrike",
        "owner_kor": "카이렌 쉐이드스트라이크 (Kyren Shadestrike)",
        "type_str": "기타 (방어구/무기 하이브리드 가죽)",
        "desc": "도망쳐봐야 소용없어. 어차피 이 망토의 그늘 밖으로 벗어날 순 없으니까.",
        "desc_src": "암흑가 골목, 배신자 청부 달성 순간",
        "maker": "정체불명의 심연 직물사",
        "mat": "절망을 먹고 자란 고대 거미줄, 나이트메어 직물",
        "appearance": "낡고 해진 듯한 칙칙한 검정 외투이나 가장자리 깃이 면도날처럼 날카롭고 유연한 마나로 코팅되어 있어 펄럭일 때마다 바람이 베여 나갑니다.",
        "atk": "연속 참절 타격급",
        "dur": "물리적 절단 불가. 찢어져도 그림자로 융합",
        "attr": "자유자재의 범위 참격",
        "attr_note": "소리 0% 발생, 회피와 공격을 동시 수행",
        "skill_name": "칠흑의 춤사위 (Dance of Pitch Black)",
        "skill_cond": "허공에 도약하여 전신을 망토로 휘감음.",
        "skill_eff": "카이렌의 본체가 허공에서 사라지고 수십 장의 검은 가죽 칼날이 회오리처럼 몰아치며 중갑 기사들을 단숨에 채썰어 육편으로 만듭니다.",
        "skill_note": "무기가 파괴되지 않으며, 암살자의 동선을 완벽히 무정형으로 흩뜨려 놓습니다.",
        "sub_skill": "**시야 차단:** 망토가 스치는 적들의 각막에 검은 잉크 무늬의 환영을 새겨 넣어 일시적으로 맹인으로 만듭니다.",
        "origin": "어린 시절 골드마켓 쓰레기장에 버려졌을 때 추위를 막아주던 넝마가 점차 살기와 마나를 흡수하며 요기로 진화한 결과물.",
        "lore": "어떤 파벌에도 속하지 않은 서늘한 독립 암살자의 가장 악랄하고 변칙적인 흉기로 암흑가에 악명이 높습니다."
    },
    {
        "folder": "09. 둔기 (Blunt Weapons)",
        "filename": "자유를 향한 해방의 망치 (Hammer of Liberation Formed for Freedom).md",
        "title": "자유를 향한 해방의 망치 (Hammer of Liberation Formed for Freedom)",
        "tag_type": "blunt_weapon",
        "rank": "legendary",
        "kor_rank": "전설급 🟠",
        "owner": "tyrus_stonebreaker",
        "owner_kor": "타이러스 스톤브레이커 (Tyrus Stonebreaker)",
        "type_str": "둔기 (해머)",
        "desc": "광산의 족쇄는 이 망치로 깼다. 다음은 네놈들의 부패한 성문을 부술 차례다.",
        "desc_src": "해방 전선 선포 첫 번째 포효",
        "maker": "노예 해방군 연합 주조장",
        "mat": "노예 족쇄 수만 개의 응축 철, 억압의 사슬",
        "appearance": "디자인이라곤 전혀 없는, 용접 자국이 처절하게 남은 기형적인 초거대 사각 쇠망치. 표면에 수많은 노예 출신 병사들의 이름이 피와 함께 새겨져 있습니다.",
        "atk": "일격 성벽 박살 파괴력",
        "dur": "사용자의 울분 지속시 절대 파괴 불가",
        "attr": "구속 전면 해제 타격",
        "attr_note": "상대방의 방패 파괴율 300% 이상 증대",
        "skill_name": "혁명의 진동",
        "skill_cond": "타이러스의 분노 수치 임계점 도달.",
        "skill_eff": "망치 머리로 땅과 적을 내리칠 때마다 억압받던 자들의 함성 소리가 물리적 충격파로 역류하여, 주변 병사들의 마비 디버프를 깨부수고 적군을 압사시킵니다.",
        "skill_note": "단일 공격력을 넘어 병단 전체의 억눌린 패널티들을 강제로 쳐부수는 정화 파동을 일으킵니다.",
        "sub_skill": "**부서진 사슬의 채찍:** 손잡이에 묶인 사슬을 늘어뜨려 원거리에 있는 적 장수의 목을 휘감아 처박습니다.",
        "origin": "채석장에서 죽어간 동료들의 피 묻은 곡괭이와 자신을 수십 년간 묶었던 쇠사슬을 홧김에 함께 녹여 만든 무기.",
        "lore": "자유도시 상인들이 뱉어내는 어떤 자본주의적 가치보다, 이 망치 한 번의 내리침이 병사들의 신장(腎臟)을 미친 듯이 뛰게 만듭니다."
    },
    {
        "folder": "03. 단검 (Daggers)",
        "filename": "은빛 비수에 새겨진 은닉 계약서 (Hidden Pact Carved on a Silver Dagger).md",
        "title": "은빛 비수에 새겨진 은닉 계약서 (Hidden Pact Carved on a Silver Dagger)",
        "tag_type": "dagger",
        "rank": "epic",
        "kor_rank": "영웅급 🟣",
        "owner": "oscar_silverfang",
        "owner_kor": "오스카 실버팽 (Oscar Silverfang)",
        "type_str": "단검",
        "desc": "협상의 가장 완벽한 끝맺음은, 내 사인 란에 묻은 네 피가 마르기 전에 도장을 찍는 것이다.",
        "desc_src": "경쟁 길드 마스터를 '양도 계약'으로 말살하며",
        "maker": "실버팽 가문의 지하 파문 세공사",
        "mat": "액체 은(銀), 배신자의 유골가루",
        "appearance": "화려한 백금색 손잡이를 가진 장식용 비수처럼 보이지만, 투명한 칼날 면 위에 독사처럼 꾸불꾸불한 계약 수식들이 초소형으로 각인되어 맥박처럼 꿈틀거립니다.",
        "atk": "낮음 (단일 부상 목적)",
        "dur": "일회성 징수 후 마나 재충전 3시간",
        "attr": "강제 채권 성립",
        "attr_note": "상처 생성 시 대상 영혼에 디버프 무한 종속",
        "skill_name": "혈서의 낙인",
        "skill_cond": "적의 피부 생살에 단 1mm라도 단검 날을 스치게 함.",
        "skill_eff": "비수에 새겨진 '노예 양도 및 절대 복종'의 인장식이 피폭자의 마나 코어에 바이러스처럼 침투하여 1분 안에 상대의 무력 체계를 영구히 붕괴시키거나 조종합니다.",
        "skill_note": "직접 찔러 죽일 필요가 없이 스치기만 해도 상대를 노예로 전락시킵니다.",
        "sub_skill": "**시장의 독소:** 비수를 뽑아낼 때 피 대신 대상의 뼛속 마나(통화량)가 흡수되어 실버팽 가문 금고로 직행합니다.",
        "origin": "정당한 로비로 마리안을 꺾을 수 없음을 깨닫고 암살과 상업을 결합시킨 사이코패스적 집념.",
        "lore": "적진 한복판에 들어가 웃으며 악수하는 오스카의 손짓 하나에 거대 용병단이 즉시 파산하고 항복한다는 전설이 깃든 공포의 도구입니다."
    },
    {
        "folder": "29. 마도구 (Magitek)",
        "filename": "심연 경제 조작의 설계 두루마리 (Scroll of Abyssal Economic Manipulation).md",
        "title": "심연 경제 조작의 설계 두루마리 (Scroll of Abyssal Economic Manipulation)",
        "tag_type": "magitek",
        "rank": "legendary",
        "kor_rank": "전설급 🟠",
        "owner": "leona_darkblade",
        "owner_kor": "레오나 다크블레이드 (Leona Darkblade)",
        "type_str": "마도구 (전술 컨트롤 패널)",
        "desc": "72번 포인트에 보병 중대 희생 처리. 그들의 피로 번 5분의 시간이 왕국군 좌익 붕괴 마진율 40%를 넘지.",
        "desc_src": "레오나의 전황 분석 브리핑",
        "maker": "다크블레이드 가문 고대 기계공학 파벌",
        "mat": "지맥 정보 홀로그램 수정, 양자 코딩 피륙",
        "appearance": "보통의 마법서나 지팡이가 전혀 아닌, 공중에 띄워두고 10개의 홀로그램 패널을 동시에 전개할 수 있는 반투명한 미래지향적 군수 설계 족자.",
        "atk": "연산 파탄 (마법 파동 붕괴)",
        "dur": "외부 타격엔 취약하나 차원 은폐 기술 적용",
        "attr": "광역 진형 강제 전송 제어",
        "attr_note": "적의 텔레포트 및 보급선 좌표 100% 해킹 무력화",
        "skill_name": "전장의 회계 감사",
        "skill_cond": "전장 전체를 바라볼 수 있는 고지대 혹은 통제실 착석.",
        "skill_eff": "적 군단의 진군 동선과 마법 공세 벡터를 역연산하여 스크롤에 입력, 허공에서 무수한 광선 레이저가 발사되어 적들의 방어진을 회계 장부 취소선 긋듯 깔끔하게 도륙냅니다.",
        "skill_note": "소규모 병력 타격용이 아닌, 군단급 이동을 차단하는 통제 광역기.",
        "sub_skill": "**강제 청산:** 연산 가치가 다 떨어진 아군 미끼 부대 근처로 적을 유인한 뒤, 아군과 적군을 통째로 차원 폭파시켜 버립니다.",
        "origin": "레오나가 감정이라는 불필요한 오류를 100% 삭제하고 오직 통계적 승리만을 위해 직접 코딩한 마도 아티팩트.",
        "lore": "병사들 사이에서 '저 여자의 두루마리에 당신 부대명이 적히면 영광스런 제물이 된 것이다'라는 섬뜩한 속담이 돕니다."
    }
]

template = """---
tags:
  - item/weapon
  - rank/{rank}
  - owner/{owner}
  - faction/crossroad_cities
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
| **세력 귀속** | [[자유도시연합 (Crossroad Cities)]] |
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
- [[자유도시연합 (Crossroad Cities)]]
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

print("Crossroad Cities: 12 pure item enclycopedia pages successfully deployed.")
