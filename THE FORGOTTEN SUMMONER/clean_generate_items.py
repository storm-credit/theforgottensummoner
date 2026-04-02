import os
import glob
import shutil

base_dir = r"c:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-19. 아이템 도감 (Item Encyclopedia)\01-19-1. 무기 (Weapons)"

# 1. Cleanup all existing mis-named files (anything containing W-SH or hero names)
bad_patterns = [
    "W-SH-*.md",
    "*솔라리스 블레이드*.md",
    "*심판봉*.md",
    "*테르시오*.md",
    "*성장*.md",
    "*홍염 대검*.md",
    "*대방패*.md",
    "*폭풍창*.md",
    "*여명 지팡이*.md",
    "*아카식*.md",
    "*은빛 부채*.md"
]

for folder in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder)
    if os.path.isdir(folder_path):
        for pat in bad_patterns:
            for f in glob.glob(os.path.join(folder_path, pat)):
                try:
                    os.remove(f)
                    print(f"Removed: {f}")
                except:
                    pass

# 2. Re-create the 13 completely pure items
items = [
    {
        "folder": "01. 한손검 (One-handed Swords)",
        "filename": "솔라리스 블레이드 (Solaris Blade).md",
        "title": "솔라리스 블레이드 (Solaris Blade)",
        "tag_type": "one_handed_sword",
        "rank": "mythic",
        "kor_rank": "신화급 🔴",
        "owner": "leonis_valerius",
        "owner_kor": "레오니스 발레리우스 (Leonis Valerius)",
        "type_str": "한손검",
        "desc": "아득한 여명 속에서 타오르는 단 하나의 진리. 이 검이 향하는 곳에 이단의 그림자는 없다.",
        "desc_src": "『루멘 성전록』 파편 1장",
        "maker": "초대 태양의 대장장이 일루미나",
        "mat": "융합된 태양석 덩어리, 천사의 깃털 화석",
        "appearance": "눈을 뜰 수 없을 만큼 강렬한 백금색 빛을 영구적으로 방출하는 한손검입니다. 칼날 자체의 재질이 금속이 아닌 압축된 태양의 플라즈마처럼 넘실거리며, 검자루는 성스러운 고대 루멘 문자가 황금 가루로 깊게 수놓아져 있습니다.",
        "atk": "대륙 단층 붕괴급",
        "dur": "영구적 보존",
        "attr": "극(極) 신성",
        "attr_note": "어둠 저항 100% 무시",
        "skill_name": "여명의 심판",
        "skill_cond": "소유자의 성력을 코어 끝까지 완전히 개방.",
        "skill_eff": "칼날에서 태양의 광이가 연장되어 수백 미터에 달하는 거대한 빛의 참격을 일으켜, 대지와 적진을 통째로 증발시킵니다.",
        "skill_note": "참격이 지나간 자리에는 며칠 동안 심연의 기운이 깃들지 못하는 성역이 임시 전개됩니다.",
        "sub_skill": "**광염의 거절:** 무기에서 뻗어나오는 광휘 자체가 주변의 환술과 저주를 지속적으로 태워 없애는 정화 오라를 발산합니다.",
        "origin": "성국의 개국 시절, 대륙 절반을 덮은 심연을 거둬내기 위해 태양의 신 솔라리스가 직접 하늘에서 떨어뜨린 첫 번째 유성우의 파편을 제련해 만든 기적의 검입니다.",
        "lore": "수백 년 전 일어났던 '성국 건국사 내전'의 마지막을 장식했던 무효화 검병기이기도 합니다. 심연의 군주를 참살하고 오염된 북방의 숲 전체를 재기능하도록 정화했던 기적이 아직도 신도들에게 교리로 전해져 내려옵니다."
    },
    {
        "folder": "09. 둔기 (Blunt Weapons)",
        "filename": "율법의 심판봉 (Gavel of Judgment).md",
        "title": "율법의 심판봉 (Gavel of Judgment)",
        "tag_type": "blunt_weapon",
        "rank": "legendary",
        "kor_rank": "전설급 🟠",
        "owner": "cassiel_arcturus",
        "owner_kor": "카시엘 아크투루스 (Cassiel Arcturus)",
        "type_str": "둔기",
        "desc": "탕, 탕, 탕. 율법의 선언이 곧 파멸이 될지어다.",
        "desc_src": "아크투루스 가문 이단 심문 기록실",
        "maker": "초대 대법관 율리우스",
        "mat": "빛을 흡수한 고밀도 신성나무, 천공 합금",
        "appearance": "일반적인 법원의 의사봉과 다르게, 성스러운 성인이 휘두를 수 있을 만큼 거대하고 묵직한 황금빛 타격 무기입니다. 손잡이에서 망치 머리까지 율법의 문구가 빼곡히 새겨져 있으며, 심판자의 기력이 주입될 때마다 글귀들이 찬연하게 빛을 냅니다.",
        "atk": "차원 균열 분쇄급",
        "dur": "영구적",
        "attr": "물리 관통",
        "attr_note": "결계 및 마법 실드 파괴 100%",
        "skill_name": "이단의 철퇴",
        "skill_cond": "이단자에 대한 최종 유죄 판결 선언.",
        "skill_eff": "공중에 십수 미터에 달하는 거대한 황금빛 심판봉의 형상을 강림시켜, 저항이 불가능한 압도적인 물리 질량으로 단일 대상을 짓뭉개버립니다.",
        "skill_note": "율법을 등지고 완전히 타락한 이단일수록 타격 질량이 기하급수적으로 무한 증폭됩니다.",
        "sub_skill": "**거짓의 튕겨냄:** 심판봉의 타격면에 닿는 모든 구조 변경 마법 혹은 환술 방어막은 유리 파편처럼 깨져나갑니다.",
        "origin": "루멘 법정을 처음 설립했던 성국 초창기, 말로 타협이 불가능한 최상위 악마들과의 이단 심문을 물리적으로 집행하기 위해 제작되었습니다.",
        "lore": "아크투루스 가문에 세습되면서, 이 봉 앞에서는 그 어떤 성역이나 귀족의 권위도 통하지 않았습니다. 법정의 가장 무겁고 공포스러운 결정을 대변하며, 부패한 고위 사제들의 결계를 단숨에 박살냈던 '정당한 숙청'의 기록이 빼곡합니다."
    },
    {
        "folder": "16. 스태프 (Staves)",
        "filename": "권천의 성장 (Holy Staff of Heaven).md",
        "title": "권천의 성장 (Holy Staff of Heaven)",
        "tag_type": "staff",
        "rank": "epic",
        "kor_rank": "영웅급 🟣",
        "owner": "benedictus_tercio",
        "owner_kor": "베네딕투스 테르시오 (Benedictus Tercio)",
        "type_str": "스태프",
        "desc": "자비로운 빛은 파괴가 아닌, 다시 일어설 용기를 스며들게 한다.",
        "desc_src": "베네딕투스의 기도문",
        "maker": "자애의 장인단",
        "mat": "루멘 성지의 유백색 대리석 코어, 대천사의 성배 조각",
        "appearance": "자극적이거나 뾰족한 위협 요소가 1밀리미터도 섞이지 않은 매우 부드럽고 매끄러운 유백색 지팡이입니다. 지팡이 머리에는 은은하게 떠다니는 빛무리가 구처럼 맴돌고 있으며 영롱한 생명력을 방출합니다.",
        "atk": "극히 낮음",
        "dur": "강건함",
        "attr": "생명 회복력 +400%",
        "attr_note": "즉사기 1회 보호",
        "skill_name": "대지에 깃든 축복",
        "skill_cond": "시전자의 생명 마나를 깊게 동조시켜 지면에 성장 타격.",
        "skill_eff": "파괴되고 오염된 전장의 지맥을 순간 반전시켜 은은한 파동을 퍼트립니다. 이 파동 안에 들어온 대규모 아군 진영은 사기와 마력이 쉼 없이 차오릅니다.",
        "skill_note": "성결의 대지를 부패로부터 원천적으로 보호하는 안식처 전개기로 평가받습니다.",
        "sub_skill": "**영적 위로:** 반경 50미터 내 심연의 광기에 노출되었거나 트라우마를 입은 동맹군들의 뇌리를 차분하게 진정시키는 패시브 위로 마법.",
        "origin": "수백 년 전, 테르시오 가문의 평온주의자들이 성력의 무기화를 강하게 반대하며 오직 '구원과 생명 유지'만을 위한 대사제 전용 성구를 기획하여 만들어 냈습니다.",
        "lore": "가장 무력한 자들의 기도가 스며들어 있어, 권력보다는 신앙적 조화를 추구하는 베네딕투스에게 가장 어울리는 장비가 되었습니다."
    },
    {
        "folder": "02. 양손검 (Two-handed Swords)",
        "filename": "홍염 대검 (Solar Flare Greatsword).md",
        "title": "홍염 대검 (Solar Flare Greatsword)",
        "tag_type": "two_handed_sword",
        "rank": "legendary",
        "kor_rank": "전설급 🟠",
        "owner": "gabriel_solgrid",
        "owner_kor": "가브리엘 솔그리드 (Gabriel Solgrid)",
        "type_str": "양손검",
        "desc": "물러서지 마라! 이 불타오르는 투지야말로 이단에게 내리는 솔라리스의 심판일지니!",
        "desc_src": "선봉장 가브리엘 솔그리드의 포효",
        "maker": "태양화로의 강철 대장장이",
        "mat": "폭발하는 태양의 광력석, 극강도의 철제 코어",
        "appearance": "어마어마한 질량과 크기를 자랑하는 초거대 대검으로, 거인조차 들기 버거울 정도입니다. 칼날 전체에 꺼지지 않는 태양의 홍염이 이글거리고 있으며, 휘두를 때마다 칼날에서 뜨거운 폭풍의 잔영이 무겁게 뒤따릅니다.",
        "atk": "적 방어선 소멸급",
        "dur": "초고도 열 내성 보장",
        "attr": "광휘 타격",
        "attr_note": "화염 피해 완전 흡수",
        "skill_name": "광휘의 맹진",
        "skill_cond": "모든 공포와 망설임을 버리고 적진 한복판으로 돌진.",
        "skill_eff": "대검에 태양의 화염을 점화시켜 공기를 찢고 폭발적인 압축 참격을 날려 적진 전열 수 킬로미터를 증발시킵니다.",
        "skill_note": "참격이 날아가는 궤적 자체가 거대한 빛의 단층선으로 찢어져 적의 거대 마수조차 정면으로 갈라냅니다.",
        "sub_skill": "**홍염의 장벽 해방:** 공격 방향 전면부에서 날아오는 마법 화살 세례를 대검의 홍염으로 태워버리는 공세 특화 방어기.",
        "origin": "성국의 수세적이고 답답한 보수 방어전에 종지부를 찍기 위해, 공격만이 살길을 외치는 무골의 전사 솔그리드를 위해 제작된 결전 병기.",
        "lore": "수백 번이 넘는 전장의 한복판에서 대갈통을 박살내던 타협 없는 무력을 상징합니다. 성국 내부의 수비 지향파들이 두려워하는 무기이기도 합니다."
    },
    {
        "folder": "30. 기타 (Others)",
        "filename": "무명 대방패 (Nameless Greatshield).md",
        "title": "무명 대방패 (Nameless Greatshield)",
        "tag_type": "others",
        "rank": "legendary",
        "kor_rank": "전설급 🟠",
        "owner": "michael_durandal",
        "owner_kor": "미카엘 듀란달 (Michael Durandal)",
        "type_str": "기타 (특수 방어구 겸용)",
        "desc": "이름조차 부여되지 않은 쇳덩어리. 그러나 이 성벽을 넘어선 이단은 단 하나도 없었다.",
        "desc_src": "제3차 심연 공성전, 철혈 기사단의 기록",
        "maker": "철벽의 수호자 건국 영웅",
        "mat": "고밀도 성광 철광석, 침묵의 산맥 암반",
        "appearance": "장식이나 보석 따위의 사치스러운 공예가 전혀 들어가지 않은 압도적으로 두껍고 광활한 무광 합금 대방패입니다. 성문 두 짝을 합쳐 거푸집에 부어넣은 듯 투박하며 패인 전투 흔적이 가득합니다.",
        "atk": "측정 불가",
        "dur": "무한 복구 임계점 보장",
        "attr": "철혈 방어",
        "attr_note": "충격파 100% 흡수",
        "skill_name": "절대 방위진",
        "skill_cond": "퇴로가 없는 절체절명의 방어선에서 방패를 대지에 박아 넣음.",
        "skill_eff": "방패를 매개로 거대한 순백의 홀로그램 장성을 수 킬로미터 폭으로 뻗어나가게 구축합니다. 하늘을 덮는 폭격조차 막아냅니다.",
        "skill_note": "방어선이 지속되는 동안 소유자는 발을 뗄 수 없으나 방벽 내구도가 소유자의 정신력과 동기화됩니다.",
        "sub_skill": "**광휘 흡수 임계:** 적의 마법 공격을 방패면으로 흡수할 때마다 잠시 질량과 면적이 팽창하여 수백 명을 커버합니다.",
        "origin": "부서진 13개의 공성 전차 장갑판을 성력으로 이어붙이며 들고 싸웠던 파편에서 유래.",
        "lore": "건국 이래 단 한 번도 뒤로 물러선 적 없는 수호자의 정체성이 깃든 역사의 증거. '뒤에는 성국과 구원받지 못한 백성이 있다'는 이념의 결정체입니다."
    },
    {
        "folder": "07. 창 (Spears)",
        "filename": "폭풍창 (Storm Lance).md",
        "title": "폭풍창 (Storm Lance)",
        "tag_type": "spear",
        "rank": "epic",
        "kor_rank": "영웅급 🟣",
        "owner": "lucian_zephyros",
        "owner_kor": "루시안 제피로스 (Lucian Zephyros)",
        "type_str": "창 (기창)",
        "desc": "구름을 찢어라. 우리의 길이 곧 창공의 율법이다.",
        "desc_src": "은빛 그리폰 출격 구호",
        "maker": "바람의 대마법사들과 제피로스",
        "mat": "폭풍의 정령석, 비룡 석영 뼈대",
        "appearance": "어마어마한 회전력을 견디기 위해 스크류 형태로 꼬인 은백색 기창입니다. 내부가 텅 빈 공기 역학적 튜브 구조이며 주변 기류를 빨아들입니다.",
        "atk": "초음속 관통급",
        "dur": "유연하고 질김",
        "attr": "폭풍 및 뇌전",
        "attr_note": "강하 타격 위력 300% 증가",
        "skill_name": "천궁의 내리꽂기",
        "skill_cond": "일정 고도 이상의 하늘에서 지면을 향해 급강하 타격.",
        "skill_eff": "강하 시 압축된 기류 폭풍이 창살 끝에 밀집하여 타격 순간 거대한 마나의 소닉붐을 일으켜 적 방어막을 완전히 철거해 버립니다.",
        "skill_note": "찌르기의 궤적을 중심으로 거대한 소용돌이가 남습니다.",
        "sub_skill": "**기류 왜곡 실드:** 비행 전방에 부딪히는 대공 요격을 흘려보내는 환영 보호막을 자동 전개합니다.",
        "origin": "정령 연합의 기술을 빌려 비정규적으로 제작된 맞춤형 공중전 전용 결전기.",
        "lore": "교단의 축사 없이 제작되어 이단의 무기라 폄하받았으나 비행 마수들의 날개를 수없이 꺾어버린 무패의 전적을 자랑합니다."
    },
    {
        "folder": "16. 스태프 (Staves)",
        "filename": "여명 지팡이 (Staff of Dawn).md",
        "title": "여명 지팡이 (Staff of Dawn)",
        "tag_type": "staff",
        "rank": "legendary",
        "kor_rank": "전설급 🟠",
        "owner": "elias_aurelius",
        "owner_kor": "엘리아스 아우렐리우스 (Elias Aurelius)",
        "type_str": "스태프",
        "desc": "무지의 심연을 들춰내는 단 하나의 진리는 가장 차갑고도 찬란한 빛뿐이다.",
        "desc_src": "지식의 서고 포고문",
        "maker": "미상 (고대 유적 출토품)",
        "mat": "성은(聖銀) 알루미늄, 별빛 크리스탈",
        "appearance": "눈부시게 투명하고 매끄러운 은색 알루미늄 광물로 길게 뻗은 우아한 마법 지팡이입니다. 꼭대기에는 마력 코어가 떠 있으며 정밀한 마법 진형이 톱니바퀴처럼 공전합니다.",
        "atk": "전방위 섬멸급",
        "dur": "반영구 복구",
        "attr": "빛 진동 코어",
        "attr_note": "캐스팅 시간 단축 99%",
        "skill_name": "천상의 포화",
        "skill_cond": "타겟팅 궤도 싱크 완료.",
        "skill_eff": "하늘을 마나의 거울로 덮은 뒤 수천 개의 능축된 빛의 구체를 응집시켜 적 전체를 대공 포화처럼 타격하여 분해합니다.",
        "skill_note": "타격 지표면의 오염을 잃고 가장 비옥한 흙으로 재조립하는 부가 효과가 있습니다.",
        "sub_skill": "**상념 부스팅:** 대륙 스케일로 압축 전송 마법을 던지는 릴레이 안테나 역할을 수행합니다.",
        "origin": "현 대륙에 존재하지 않는 잊혀진 가공 기술로 빚어진 유물. 고대 격납고에서 발굴되었습니다.",
        "lore": "이단의 기술이라 의심받았지만 성도의 심연 구름을 물리친 뒤 그 권위를 확립했습니다. 신비학보다는 정밀한 마도 공학의 산물에 가깝습니다."
    },
    {
        "folder": "18. 마법서 (Grimoires)",
        "filename": "아카식 마도서의 찢어진 장 (Torn Page of Akashic Tome).md",
        "title": "아카식 마도서의 찢어진 장 (Torn Page of Akashic Tome)",
        "tag_type": "grimoires",
        "rank": "mythic",
        "kor_rank": "신화급 🔴",
        "owner": "elias_aurelius",
        "owner_kor": "엘리아스 아우렐리우스 (Elias Aurelius)",
        "type_str": "마법서",
        "desc": "기록되지 않은 지식이 이단의 세계를 연다. 나는 그 문을 들여다본 자일뿐.",
        "desc_src": "엘리아스 진술 기록록",
        "maker": "태초의 창조 신성",
        "mat": "시공간 법칙이 고정된 영원의 양피지",
        "appearance": "두껍고 무거운 책이 아닌, 빛의 문자가 홀로그램처럼 허공에 떠오르는 단 한 장의 찢어진 마도 양피지입니다. 종이 자체는 만지면 공기처럼 잡히지 않습니다.",
        "atk": "개념 붕괴 수준",
        "dur": "파괴 불가능",
        "attr": "아카식 레코드",
        "attr_note": "소모 마력 0%",
        "skill_name": "태초의 정화구역",
        "skill_cond": "찢어진 장의 마지막 활자 낭독.",
        "skill_eff": "우주와 완전히 격리된 마력의 성역을 깔아 오염된 육체와 흑마법 인가율조차 분자 단위로 순수한 에테르로 해체시킵니다.",
        "skill_note": "연구적 통달 능력이 임계점을 넘은 자만 발동 통제가 가능합니다.",
        "sub_skill": "**진리의 해석:** 세상의 모든 암호화된 환각이나 마도 통신을 즉시 번역합니다.",
        "origin": "절대자들의 설계도 중 한 장이 차원의 틈새로 찢어져 나갔다는 신화적 기원을 가집니다.",
        "lore": "이 유물의 해석본을 통해 성국의 편협한 교리가 뒤집히기도 했으며, 학회에선 경외와 공포의 대상으로 다루어집니다."
    },
    {
        "folder": "19. 부채 (Fans)",
        "filename": "은빛 부채 (Silver Fan).md",
        "title": "은빛 부채 (Silver Fan)",
        "tag_type": "fans",
        "rank": "epic",
        "kor_rank": "영웅급 🟣",
        "owner": "seryl_sylphia",
        "owner_kor": "세릴 실피아 (Seryl Sylphia)",
        "type_str": "부채",
        "desc": "가장 맹렬한 폭풍도 부채 끝에서 부드러운 순풍이 되리니.",
        "desc_src": "아군 부상병 호송 기록록",
        "maker": "정령 연합의 은둔 세공사",
        "mat": "비룡의 석영 뼈거울, 정령 비단 날개",
        "appearance": "빛 굴절에 따라 반짝이는 은빛 깃털로 엮인 대형 부채. 무희의 소품처럼 화려하나 끝단이 매우 얇은 진공 칼날의 구조를 가집니다.",
        "atk": "중상급 절단력",
        "dur": "자체 복원",
        "attr": "빛과 바람 공명",
        "attr_note": "물리 반사와 힐링 동시 수행",
        "skill_name": "성결한 칼바람",
        "skill_cond": "부채를 전개하여 마나를 싣고 강하게 스윙.",
        "skill_eff": "수만 개의 빛의 칼날 폭풍을 흩뿌려 적에게는 마법 참각을 입히고, 아군에게 닿으면 상처를 지혈하고 피로를 씻어냅니다.",
        "skill_note": "초거대 광역 힐링과 도륙을 섞은 유틸리티 결전기입니다.",
        "sub_skill": "**순풍의 인도:** 펄럭이는 부가 효과로 아군의 기동력과 체공 시간을 폭발적으로 올립니다.",
        "origin": "빈민 구호소의 헤진 부채 원형을 정령 유니온의 은둔자가 복각해준 장비.",
        "lore": "귀족들에겐 무희의 도구라 욕먹었으나 징집병 평민들에겐 유일하게 믿음직한 구원의 방어구로 통용됩니다."
    },
    {
        "folder": "16. 스태프 (Staves)",
        "filename": "태양 지팡이 (Solar Staff).md",
        "title": "태양 지팡이 (Solar Staff)",
        "tag_type": "staff",
        "rank": "epic",
        "kor_rank": "영웅급 🟣",
        "owner": "marian_ceres",
        "owner_kor": "마리안 세레스 (Marian Ceres)",
        "type_str": "스태프",
        "desc": "가장 작은 온기조차 수만 명을 깨우는 아침 햇살이 될 수 있기를.",
        "desc_src": "어린 사제들의 찬양시집",
        "maker": "신전 부속 공방",
        "mat": "황금빛 해바라기 원목, 태양의 파편",
        "appearance": "섬세하게 깎인 황금빛 원목 지팡이로, 지팡이 머리가 포용하듯 피어나는 태양꽃의 형상을 띄고 있습니다.",
        "atk": "거의 없음",
        "dur": "가볍고 단단함",
        "attr": "자애로운 타겟 치유",
        "attr_note": "디버프 면역 지원",
        "skill_name": "햇살의 포옹",
        "skill_cond": "진심 어린 회복의 기도를 읊으며 지팡이 거상.",
        "skill_eff": "따뜻하고 눈부신 황금빛 치유력이 반경 내 모든 동맹의 저주나 독성 물질을 완벽히 분해하고 타버린 신경 조직조차 다시 이어줍니다.",
        "skill_note": "신체적 부상뿐만 아니라 병적인 공포(Fear) 상태도 즉시 해제합니다.",
        "sub_skill": "**희망의 싹:** 주변 토지에 씨앗을 빠르게 발아시켜 전장의 황폐화를 늦춥니다.",
        "origin": "전장의 후방에서 묵묵히 기도하는 치유 사제단들의 정성이 모여 발현된 기적.",
        "lore": "세레스의 인자함과 결합되어 한낱 원목 스태프가 전설적인 성구와 맞먹는 신성 마나 효율을 끌어냅니다."
    },
    {
        "folder": "29. 마도구 (Magitek)",
        "filename": "은광 램프 (Silver Lamp).md",
        "title": "은광 램프 (Silver Lamp)",
        "tag_type": "magitek",
        "rank": "legendary",
        "kor_rank": "전설급 🟠",
        "owner": "seraphina_noctis",
        "owner_kor": "세라피나 녹티스 (Seraphina Noctis)",
        "type_str": "마도구",
        "desc": "별이 뜨지 않는 암야(暗夜)라 할지라도, 내가 든 이 등불 하나면 족하다.",
        "desc_src": "이단 심문소 은밀 강하 전의 맹세록",
        "maker": "암흑 장인들의 지하 길드",
        "mat": "그림자 진주석, 백금",
        "appearance": "작고 고풍스러운 수수께끼의 은빛 램프 장신구 형태. 램프 유리 너머로는 불꽃 대신 차가운 푸른빛의 그림자 에테르가 너울거리고 있습니다.",
        "atk": "침묵의 절단",
        "dur": "극고내성 구조체",
        "attr": "물리/마법 혼성 은신",
        "attr_note": "광학 미채 전력 100%",
        "skill_name": "야상곡의 장막",
        "skill_cond": "램프의 뚜껑을 반쯤 열어 마력을 방출.",
        "skill_eff": "소유자와 소속 소대의 존재감은 물론 냄새, 체온, 마력장까지 주변 파장과 완전 동기화시켜 지워버립니다.",
        "skill_note": "심연의 맹수조차 냄새를 맡지 못하는 궁극의 인지 강탈 마도구입니다.",
        "sub_skill": "**그림자 칼날 생성:** 램프에서 뻗어나오는 그림자들을 예리한 쌍검 형태로 형상화해 암살 무기로 전환 가능.",
        "origin": "초기 이단 소탕 작전에서 지하 범죄 조직 우두머리에게서 압수한 물건을 녹티스가 개조함.",
        "lore": "성국의 순백 기사들이 혐오하는 '암습'의 상징이지만 그림자 부대의 성공률을 90% 이상으로 끌어올린 전공의 일등 공신."
    },
    {
        "folder": "11. 활 (Bows)",
        "filename": "항성궁 (Stellar Bow).md",
        "title": "항성궁 (Stellar Bow)",
        "tag_type": "bow",
        "rank": "epic",
        "kor_rank": "영웅급 🟣",
        "owner": "evangeline_astel",
        "owner_kor": "에반젤린 아스텔 (Evangeline Astel)",
        "type_str": "활",
        "desc": "그녀의 시위가 당겨지면 우주의 차가운 별무리가 지상으로 비처럼 떨어졌다.",
        "desc_src": "천궁 초계 부대의 시말서",
        "maker": "별빛 마도공학 결사제",
        "mat": "추락한 혜성 암석, 탄소 초합금",
        "appearance": "본체인 활대의 형상이 물리적인 선이 아니라 뚜렷하게 빛나는 세 개의 별점(은하 궤도)을 허공에서 연결해 놓은 기하학적인 마력궁입니다. 화살을 잴 필요 없이 당기기만 하면 성단 마나가 화살로 맺힙니다.",
        "atk": "원거리 장갑 격파",
        "dur": "파손 불가 (형상 없음)",
        "attr": "항성 포화 (관통)",
        "attr_note": "물리적 중력 영향 0%",
        "skill_name": "유성우의 사출",
        "skill_cond": "정조준 상태로 5초 이상의 시위 인장.",
        "skill_eff": "하나의 성간 화살을 상공으로 발사하면, 하늘에서 화살이 수백 갈래 유성우로 분할되어 적 방어선의 정수리에 융단 포격을 가합니다.",
        "skill_note": "사거리가 시야 확보 반경과 완전히 동일하여 저격의 한계가 없습니다.",
        "sub_skill": "**항성 추적:** 타깃 지정 시 우주적 인장 마크가 박혀 장애물 뒤로 도망쳐도 화살이 꺾어 들어가 유도 타격합니다.",
        "origin": "별빛 투시력에 각성한 에반젤린을 위해 특수 조직된 마도공학 마스터들이 심혈을 기울여 완성시킨 병기.",
        "lore": "별의 궤도를 읽는 아스텔 가문 특유의 예측 회로와 완벽하게 맞물려 활 쏘는 매 순간이 정밀한 궤도 폭격 포병과 흡사한 파괴력을 냅니다."
    },
    {
        "folder": "30. 기타 (Others)",
        "filename": "은빛 지휘봉 (Silver Baton).md",
        "title": "은빛 지휘봉 (Silver Baton)",
        "tag_type": "others",
        "rank": "legendary",
        "kor_rank": "전설급 🟠",
        "owner": "theodor_vanguard",
        "owner_kor": "테오도르 뱅가드 (Theodor Vanguard)",
        "type_str": "기타 (지휘관용 마도구)",
        "desc": "이 작은 막대기가 10만의 군단을 유기수처럼 춤추게 하리라.",
        "desc_src": "뱅가드 참모 총회 일지",
        "maker": "성도 루멘 최고의 귀금속 세공사",
        "mat": "축복받은 백금, 고출력 정보 통신 크리스탈",
        "appearance": "마도 오케스트라의 지휘봉과 같은 아주 얇고 우아한 백금 막대입니다. 끝부분에 박힌 정보 크리스탈판이 초단위로 깜빡거리며 전장의 흐름을 연산하고 있습니다.",
        "atk": "무기력함 (개인)",
        "dur": "쉽게 부러짐",
        "attr": "전장 정보 통일 지휘",
        "attr_note": "전술 공유 마력장 생성",
        "skill_name": "그랜드 마에스트로",
        "skill_cond": "지휘봉으로 전장의 청사진 도면을 허공에 연주하듯 허가 코드를 발송.",
        "skill_eff": "반경 5km 내의 모든 동맹 부대의 통신 방해를 무시하고, 지휘관 테오도르의 눈에 맺힌 미니맵과 적군 약점 스캐닝을 실시간으로 장교들의 뇌리에 동기화시킵니다.",
        "skill_note": "개인의 무력은 최하위지만 군단 차원에서는 파멸적인 전술 우위를 선점하게 만듭니다.",
        "sub_skill": "**집단 사기 고양:** 지휘봉이 그려내는 궤적에 따라 부대원들의 심장 박동과 마나 순환이 최적화됩니다.",
        "origin": "참모 총장 승진 시 가문에서 헌납한 최고급 전장 지휘 마도기.",
        "lore": "기사들의 돌진만을 중시하던 낡은 교리를 타파하고 현대적인 군단 단위 컨트롤 마도 공학을 성국 내에 가장 처음 도입시킨 상징물."
    }
]

template = """---
tags:
  - item/weapon
  - rank/{rank}
  - owner/{owner}
  - faction/saint_haven
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
| **가치** | 산출 불가 (국보급) |
| **현재 소유자** | [[{owner_kor}]] |
| **세력 귀속** | [[성국 (Saint Haven)]] |
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

- **획득처:** 특별 세습 또는 퀘스트 연성
- **관련 퀘스트:** -

---

## 🔗 관련 문서
- [[{owner_kor}]]
- [[성국 (Saint Haven)]]
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
    print(f"Created: {out_path}")

print("Successfully wiped old prefixed files and deployed 13 perfectly named items!")
