---
description: Integrated Faction & Lore Creation Workflow (All-in-One)
---

# 🌏 세력 및 세계관 통합 생성 워크플로우 (Unified Workflow)

이 워크플로우는 **거점(Location) - 인물(Character) - 아이템(Item)** 3대 요소를 유기적으로 연결하여 한 번에 생성하는 **통합 공정**입니다.
세력 리뉴얼이나 신규 세력 창설 시 이 순서를 따르십시오.

> [!important] 📂 기본 경로 (Base Paths)
> - **거점 (Location):** `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)`
> - **인물 (Character):** `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)`
> - **아이템 (Item):** `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-19. 아이템 도감 (Item Encyclopedia)`

> [!CAUTION] 🚫 파일명 생성 규칙 (Filename Policy)
> **모든 파일 생성 시 URL 인코딩 문자(`%20`, `%28`, `%29` 등) 사용 금지.**
> - **잘못된 예:** `황제의_지팡이_%28Staff%20of%20Emperor%29.md`
> - **올바른 예:** `황제의 지팡이 (Staff of Emperor).md` 또는 `황제의_지팡이_Staff_of_Emperor.md`
> - AI가 도구를 호출할 때 `TargetFile` 경로에 **절대 인코딩된 문자열을 넣지 말 것.** 사람이 읽을 수 있는 그대로의 경로를 사용하십시오.

---

## 🔍 Phase 0. 현황 파악 (Inventory Check) - CRITICAL
> *"지도를 믿지 말고 눈으로 확인하라."*

1.  **물리적 전수 조사 (Physical Directory Scan):**
    - **절대 메인 인덱스(`세력.md`)만 보고 판단하지 마십시오.** 인덱스는 누락되거나 최신화되지 않았을 수 있습니다.
    - 반드시 `list_dir` 도구를 사용하여 **해당 세력 폴더 및 하위 폴더(`도시`, `요새` 등)의 실제 파일 목록**을 직접 눈으로 확인하십시오.
    - **체크리스트:**
        - [ ] 누락된 파일이 있는가?
        - [ ] 중복 파일(구버전)이 있는가?
        - [ ] 넘버링이 안 된 파일이 있는가?

---

## 🏗️ Phase 1. 무대 설정: 거점 (Location)
> *"배우가 서기 전에 무대부터 완성한다."*

1.  **참조 워크플로우:** `Location_Creation_Standard.md`
2.  **실행 절차:**
    - ① 세력 내 **중요 거점**을 `도시`, `요새`, `성지` 등 **하위 폴더(Subfolder)** 단위로 분류.
    - ② **하위 폴더별 개별 넘버링(Per-Subfolder Numbering):** 각 폴더 안에서 1번부터 다시 시작.
        - 예: `도시/1. 수도`, `도시/2. 항구`, `요새/1. 전초기지`, `요새/2. 본성`
    - ③ **프리미엄 템플릿** 적용하여 거점 파일 생성.
    - ④ `핵심 인물 슬롯`을 비워두거나 예정된 인물명(`[[ ]]`) 기입.
    - ⑤ **메인 인덱스 연결:** 거점(Root) 파일에서 `[[하위폴더/파일명]]` 형태로 정확히 링크.

---

## 🦸‍♂️ Phase 2. 주연 등장: 인물 (Character)
> *"무대 위에 배우를 세우고 역할을 부여한다."*

1.  **참조 워크플로우:** `Character_Creation_Standard.md`
2.  **실행 절차:**
    - ① Phase 1의 `핵심 인물 슬롯`에 기재된 **모든 주요 인물**을 리스트업.
    - ② **[Loop: 점검 및 갱신 (Check & Update)]** 각 인물에 대해:
        - **(파일 있음):** 기존 내용을 **Strict Grade System** 및 **프리미엄 템플릿**에 맞춰 **리뉴얼(Update)**.
        - **(파일 없음):** 신규 생성(Create).
        - **공통:** 취향/서사/장비 정보 보강 및 **[맵핑]** 연결 상태 확인.

---

## ⚔️ Phase 3. 소품 배치: 아이템 (Item)
> *"배우에게 걸맞은 명품 소품을 쥐여준다."*

1.  **참조 워크플로우:** `Item_Creation_Standard.md`
2.  **실행 절차:**
    - ① 인물의 `Equipment` 섹션에 기입된 **전용 장비(무기/아티팩트)** 확인.
    - ② **영웅급(Heroic)** 이상 아이템은 별도 파일로 생성 (아이템 도감 폴더).
    - ③ **[맵핑]:** 아이템 파일 `소유자`에 `[[인물명]]` 링크, 인물 파일에 `[[아이템명]]` 링크 연결.

---

## 🔗 Phase 4. 하네시스 구조 최종 통합 (Hanesis Integration & Check)
> *"세계관의 피와 뼈가 완벽하게 맞물려 돌아가는지 확인한다."*

1.  **가혹한 섭리 검증 (Grim Plausibility Check)**
    - "단순한 기계적 개연성이 아니라, 이 **거점**에 사는 **등장인물**이 이 **아이템**을 획득하고 유지하기 위해 어떤 **가혹한 대가**를 치르고 있는가?"
    - 영웅 간의 파워 밸런스가 단순한 전투력 나열이 아닌, 서사적 상성(정치적 알력, 마법적 상극 등)으로 구현되었는가?
    - 13대 백과(마법, 교통, 통신, 종교 등)와의 N:N `[[Wikilink]]` 통합이 완료되었는가?

2.  **인덱싱 (Indexing)**
    - `01-8. 세력 아카이브` (거점 추가)
    - `01-14. 영웅 백과` (인물 추가)
    - `01-19. 아이템 도감` (아이템 추가)

3.  **알림 (Notify)**
    - 사용자에게 "거점-인물-아이템 세트" 완성 보고.

---

## 📚 Appendix: 대륙 및 세력별 검수 경로 사전 (Directory Dictionary)

AI 챗봇에게 특정 세력의 로어 업데이트 및 설정 검수를 지시할 때, 이 부록을 활용하여 다음과 같이 명령하십시오:
> **프롬프트 예시:** `"Lore_Update_Standard.md에 정리된 [크림슨 대륙 - 솔라리안 제국]의 경로를 전부 확인해서 개연성을 점검해 줘."`

### 1. 에테르 대륙 (Ether Continent)
- **[공통 배경]**: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-3. 생명의 숲 – 에테르 대륙 (Eter Continent)`

**1. 성국 (Saint Haven)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\1. 에테르 대륙 (Ether Continent)\1. 성국 (Saint Haven)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\1. 에테르 대륙\1. 성국 (Saint Haven)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\1. 에테르 대륙 (Ether Continent)\1. 성국 (Saint Haven)`

**2. 왕국연합 (Allied Kingdoms)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\1. 에테르 대륙 (Ether Continent)\2. 왕국연합 (Allied Kingdoms)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\1. 에테르 대륙\2. 왕국연합 (Allied Kingdoms)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\1. 에테르 대륙 (Ether Continent)\2. 왕국연합 (Allied Kingdoms)`

**3. 자유도시연합 (Crossroad Cities)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\1. 에테르 대륙 (Ether Continent)\3. 자유도시연합 (Crossroad Cities)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\1. 에테르 대륙\3. 자유도시연합 (Crossroad Cities)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\1. 에테르 대륙 (Ether Continent)\3. 자유도시연합 (Crossroad Cities)`

**4. 마법협회 (Arcane Society)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\1. 에테르 대륙 (Ether Continent)\4. 마법협회 (Arcane Society)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\1. 에테르 대륙\4. 마법협회 (Arcane Society)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\1. 에테르 대륙 (Ether Continent)\4. 마법협회 (Arcane Society)`

**5. 정령연합 (Spirit Union)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\1. 에테르 대륙 (Ether Continent)\5. 정령연합 (Spirit Union)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\1. 에테르 대륙\5. 정령 연합 (Spirit Union)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\1. 에테르 대륙 (Ether Continent)\5. 정령연합 (Spirit Union)`

---

### 2. 크림슨 대륙 (Crimson Continent)
- **[공통 배경]**: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-4. 붉은 황무지 – 크림슨 대륙 (Crimson Continent)`

**1. 솔라리안 제국 (Solarian Empire)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\2. 크림슨 대륙 (Crimson Continent)\1. 솔라리안 제국 (Solarian Empire)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\2. 크림슨 대륙 (Crimson Continent)\1. 솔라리안 제국 (Solarian Empire)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\2. 크림슨 대륙 (Crimson Continent)\1. 솔라리안 제국 (Solarian Empire)`

**2. 아르카나 잔재 (Arkana Remnants)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\2. 크림슨 대륙 (Crimson Continent)\2. 아르카나 잔재 (Arkana Remnants)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\2. 크림슨 대륙 (Crimson Continent)\2. 아르카나 잔재 (Arkana Remnants)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\2. 크림슨 대륙 (Crimson Continent)\2. 아르카나 잔재 (Arkana Remnants)`

**3. 용의 후예 (Dragon Descendants)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\2. 크림슨 대륙 (Crimson Continent)\3. 용의 후예 (Dragon Descendants)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\2. 크림슨 대륙 (Crimson Continent)\3. 용의 후예 (Dragon Descendants)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\2. 크림슨 대륙 (Crimson Continent)\3. 용의 후예 (Dragon Descendants)`

**4. 붉은 사막 부족 (Red Desert Tribes)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\2. 크림슨 대륙 (Crimson Continent)\4. 붉은 사막 부족 (Red Desert Tribes)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\2. 크림슨 대륙 (Crimson Continent)\4. 붉은 사막 부족 (Red Desert Tribes)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\2. 크림슨 대륙 (Crimson Continent)\4. 붉은 사막 부족 (Red Desert Tribes)`

**5. 잊혀진 서고단 (Forgotten Library Order)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\2. 크림슨 대륙 (Crimson Continent)\5. 잊혀진 서고단 (Forgotten Library Order)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\2. 크림슨 대륙 (Crimson Continent)\5. 잊혀진 서고단 (Forgotten Library Order)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\2. 크림슨 대륙 (Crimson Continent)\5. 잊혀진 서고단 (Forgotten Library Order)`

---

### 3. 프로스트 대륙 (Frost Continent)
- **[공통 배경]**: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-5. 얼음의 땅 – 프로스트 대륙 (Frost Continent)`

**1. 딥 포지 왕국 (Deep Forge Kingdom)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\3. 프로스트 대륙 (Frost Continent)\1. 딥 포지 왕국 (Deep Forge Kingdom)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\3. 프로스트 대륙 (Frost Continent)\1. 딥 포지 왕국 (Deep Forge Kingdom)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\3. 프로스트 대륙 (Frost Continent)\1. 딥 포지 왕국 (Deep Forge Kingdom)`

**2. 프로스트본 연합 (Frostborn Tribes)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\3. 프로스트 대륙 (Frost Continent)\2. 프로스트본 연합 (Frostborn Tribes)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\3. 프로스트 대륙 (Frost Continent)\2. 프로스트본 연합 (Frostborn Tribes)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\3. 프로스트 대륙 (Frost Continent)\2. 프로스트본 연합 (Frostborn Tribes)`

**3. 빙하의 신전 (Frozen Sanctum)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\3. 프로스트 대륙 (Frost Continent)\3. 빙하의 신전 (Frozen Sanctum)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\3. 프로스트 대륙 (Frost Continent)\3. 빙하의 신전 (Frozen Sanctum)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\3. 프로스트 대륙 (Frost Continent)\3. 빙하의 신전 (Frozen Sanctum)`

**4. 그림자 항구 (Shadowwake Cove)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\3. 프로스트 대륙 (Frost Continent)\4. 그림자 항구 (Shadowwake Cove)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\3. 프로스트 대륙 (Frost Continent)\4. 그림자 항구 (Shadowwake Cove)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\3. 프로스트 대륙 (Frost Continent)\4. 그림자 항구 (Shadowwake Cove)`

---

### 4. 오벨리스크 대륙 (Obelisk Continent)
- **[공통 배경]**: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-6. 그림자의 대지 – 오벨리스크 대륙 (Obelisk Continent)`

**1. 심연 군단 (Abyssal Legion)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\4. 오벨리스크 대륙 (Obelisk Continent)\1. 심연 군단 (Abyssal Legion)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\4. 오벨리스크 대륙 (Obelisk Continent)\1. 심연 군단 (Abyssal Legion)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\4. 오벨리스크 대륙 (Obelisk Continent)\1. 심연 군단 (Abyssal Legion)`

**2. 망자의 왕국 (Kingdom of the Dead)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\4. 오벨리스크 대륙 (Obelisk Continent)\2. 망자의 왕국 (Kingdom of the Dead)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\4. 오벨리스크 대륙 (Obelisk Continent)\2. 망자의 왕국 (Kingdom of the Dead)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\4. 오벨리스크 대륙 (Obelisk Continent)\2. 망자의 왕국 (Kingdom of the Dead)`

**3. 잊힌 자들의 연합 (Forgotten Alliance)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\4. 오벨리스크 대륙 (Obelisk Continent)\3. 잊힌 자들의 연합 (Forgotten Alliance)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\4. 오벨리스크 대륙 (Obelisk Continent)\3. 잊힌 자들의 연합 (Forgotten Alliance)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\4. 오벨리스크 대륙 (Obelisk Continent)\3. 잊힌 자들의 연합 (Forgotten Alliance)`

**4. 봉인 수호단 (Seal Wardens)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\4. 오벨리스크 대륙 (Obelisk Continent)\4. 봉인 수호단 (Seal Wardens)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\4. 오벨리스크 대륙 (Obelisk Continent)\4. 봉인 수호단 (Seal Wardens)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\4. 오벨리스크 대륙 (Obelisk Continent)\4. 봉인 수호단 (Seal Wardens)`

---

### 5. 해양 대륙 (Oceanic Continent)
- **[공통 배경]**: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-7. 끝없는 바다 – 해양 대륙 (Oceanic Continent)`

**1. 해적 연합 (Pirate Confederacy)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\5. 해양 대륙 (Oceanic Continent)\1. 해적 연합 (Pirate Confederacy)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\5. 해양 대륙 (Oceanic Continent)\1. 해적 연합 (Pirate Confederacy)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN 양식 보존`

**2. 황금 함대 (Golden Armada)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\5. 해양 대륙 (Oceanic Continent)\2. 황금 함대 (Golden Armada)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\5. 해양 대륙 (Oceanic Continent)\2. 황금 함대 (Golden Armada)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\5. 해양 대륙 (Oceanic Continent)\2. 황금 함대 (Golden Armada)`

**3. 바다의 교단 (Church of the Sea)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\5. 해양 대륙 (Oceanic Continent)\3. 바다의 교단 (Church of the Sea)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\5. 해양 대륙 (Oceanic Continent)\3. 바다의 교단 (Church of the Sea)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\5. 해양 대륙 (Oceanic Continent)\3. 바다의 교단 (Church of the Sea)`

---

### 6. 중립 세력 (Neutral)

#### [1] 용병단 (Mercenaries)

**1. 저주받은 용병단 (Cursed Mercenaries)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\1. 저주받은 용병단 (Cursed Mercenaries)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\1. 저주받은 용병단 (Cursed Mercenaries)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\1. 저주받은 용병단 (Cursed Mercenaries)`

**2. 그리핀 기사단 (Order of the Gryphon)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\2. 그리핀 기사단 (Order of the Gryphon)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\2. 그리핀 기사단 (Order of the Gryphon)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\2. 그리핀 기사단 (Order of the Gryphon)`

**3. 붉은 칼날 용병단 (Red Blades Mercenaries)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\3. 붉은 칼날 용병단 (Red Blades Mercenaries)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\3. 붉은 칼날 용병단 (Red Blades Mercenaries)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\3. 붉은 칼날 용병단 (Red Blades Mercenaries)`

**4. 검은 파도 용병단 (Black Tide Mercenaries)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\4. 검은 파도 용병단 (Black Tide Mercenaries)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\4. 검은 파도 용병단 (Black Tide Mercenaries)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\4. 검은 파도 용병단 (Black Tide Mercenaries)`

**5. 유랑 기사단 (Wandering Knights)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\5. 유랑 기사단 (Wandering Knights)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\5. 유랑 기사단 (Wandering Knights)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\5. 유랑 기사단 (Wandering Knights)`

**6. 철혈 부대 (Iron Blood Corps)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\6. 철혈 부대 (Iron Blood Corps)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\6. 철혈 부대 (Iron Blood Corps)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\6. 철혈 부대 (Iron Blood Corps)`

**7. 바람의 칼날 (Wind Blades)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\7. 바람의 칼날 (Wind Blades)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\7. 바람의 칼날 (Wind Blades)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\7. 바람의 칼날 (Wind Blades)`

**8. 바이퍼 해적단 (Viper Raiders)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\8. 바이퍼 해적단 (Viper Raiders)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\8. 바이퍼 해적단 (Viper Raiders)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\8. 바이퍼 해적단 (Viper Raiders)`

**9. 황금 기계단 (Golden Mechanists)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\9. 황금 기계단 (Golden Mechanists)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\9. 황금 기계단 (Golden Mechanists)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\9. 황금 기계단 (Golden Mechanists)`

**10. 강철의 형제단 (Brotherhood of Steel)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\10. 강철의 형제단 (Brotherhood of Steel)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\10. 강철의 형제단 (Brotherhood of Steel)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\10. 강철의 형제단 (Brotherhood of Steel)`

**11. 신성 계약단 (Divine Covenant)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\11. 신성 계약단 (Divine Covenant)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\11. 신성 계약단 (Divine Covenant)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\11. 신성 계약단 (Divine Covenant)`

**12. 자연의 방랑자 (Wanderers of Nature)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\12. 자연의 방랑자 (Wanderers of Nature)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\12. 자연의 방랑자 (Wanderers of Nature)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\6. 중립세력 (Neutral)\1. 용병단(Mercenaries)\12. 자연의 방랑자 (Wanderers of Nature)`

#### [2] 마법연구조직 (Magic Research)

**1. 천상의 서고 (Celestial Archive)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\6. 중립세력 (Neutral)\2. 마법연구조직 (Magic Research)\1. 천상의 서고 (Celestial Archive)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\6. 중립세력 (Neutral)\2. 마법연구조직 (Magic Research)\1. 천상의 서고 (Celestial Archive)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\6. 중립세력 (Neutral)\2. 마법연구조직 (Magic Research)\1. 천상의 서고 (Celestial Archive)`

**2. 연금술사의 길드 (Guild of Alchemists)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\6. 중립세력 (Neutral)\2. 마법연구조직 (Magic Research)\2. 연금술사의 길드 (Guild of Alchemists)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\6. 중립세력 (Neutral)\2. 마법연구조직 (Magic Research)\2. 연금술사의 길드 (Guild of Alchemists)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\6. 중립세력 (Neutral)\2. 마법연구조직 (Magic Research)\2. 연금술사의 길드 (Guild of Alchemists)`

**3. 차원 탐사단 (Dimensional Explorers)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\6. 중립세력 (Neutral)\2. 마법연구조직 (Magic Research)\3. 차원 탐사단 (Dimensional Explorers)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\6. 중립세력 (Neutral)\2. 마법연구조직 (Magic Research)\3. 차원 탐사단 (Dimensional Explorers)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\6. 중립세력 (Neutral)\2. 마법연구조직 (Magic Research)\3. 차원 탐사단 (Dimensional Explorers)`

**4. 진실의 눈 (Eye of Truth)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\6. 중립세력 (Neutral)\2. 마법연구조직 (Magic Research)\4. 진실의 눈 (Eye of Truth)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\6. 중립세력 (Neutral)\2. 마법연구조직 (Magic Research)\4. 진실의 눈 (Eye of Truth)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\6. 중립세력 (Neutral)\2. 마법연구조직 (Magic Research)\4. 진실의 눈 (Eye of Truth)`

**5. 심연의 별무리 (Stellar Abyss Collective)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\6. 중립세력 (Neutral)\2. 마법연구조직 (Magic Research)\5. 심연의 별무리 (Stellar Abyss Collective)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\6. 중립세력 (Neutral)\2. 마법연구조직 (Magic Research)\5. 심연의 별무리 (Stellar Abyss Collective)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\6. 중립세력 (Neutral)\2. 마법연구조직 (Magic Research)\5. 심연의 별무리 (Stellar Abyss Collective)`

**6. 밤의 계약단 (Coven of the Night)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\6. 중립세력 (Neutral)\2. 마법연구조직 (Magic Research)\6. 밤의 계약단 (Coven of the Night)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\6. 중립세력 (Neutral)\2. 마법연구조직 (Magic Research)\6. 밤의 계약단 (Coven of the Night)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\6. 중립세력 (Neutral)\2. 마법연구조직 (Magic Research)\6. 밤의 계약단 (Coven of the Night)`

#### [3] 첩보 (Intelligence)

**1. 어둠의 손 (Shadow Hand)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\6. 중립세력 (Neutral)\3. 첩보 (Intelligence)\1. 어둠의 손 (Shadow Hand)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\6. 중립세력 (Neutral)\3. 첩보 (Intelligence)\1. 어둠의 손 (Shadow Hand)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\6. 중립세력 (Neutral)\3. 첩보 (Intelligence)\1. 어둠의 손 (Shadow Hand)`

**2. 그림자 연맹 (Shadow Syndicate)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\6. 중립세력 (Neutral)\3. 첩보 (Intelligence)\2. 그림자 연맹 (Shadow Syndicate)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\6. 중립세력 (Neutral)\3. 첩보 (Intelligence)\2. 그림자 연맹 (Shadow Syndicate)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\6. 중립세력 (Neutral)\3. 첩보 (Intelligence)\2. 그림자 연맹 (Shadow Syndicate)`

**3. 검은 여우단 (Black Fox Syndicate)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\6. 중립세력 (Neutral)\3. 첩보 (Intelligence)\3. 검은 여우단 (Black Fox Syndicate)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\6. 중립세력 (Neutral)\3. 첩보 (Intelligence)\3. 검은 여우단 (Black Fox Syndicate)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\6. 중립세력 (Neutral)\3. 첩보 (Intelligence)\3. 검은 여우단 (Black Fox Syndicate)`

**4. 황야의 추적자들 (Hunters of the Wild)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\6. 중립세력 (Neutral)\3. 첩보 (Intelligence)\4. 황야의 추적자들 (Hunters of the Wild)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\6. 중립세력 (Neutral)\3. 첩보 (Intelligence)\4. 황야의 추적자들 (Hunters of 소실 복구)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\6. 중립세력 (Neutral)\3. 첩보 (Intelligence)\4. 황야의 추적자들 (Hunters of the Wild)`

**5. 황금 손아귀 (Golden Claw)**
- 세력 본문: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)\6. 중립세력 (Neutral)\3. 첩보 (Intelligence)\5. 황금 손아귀 (Golden Claw)`
- 주요 인물: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-1. 세력 주요 인물 (Faction Leaders)\6. 중립세력 (Neutral)\3. 첩보 (Intelligence)\5. 황금 손아귀 (Golden Claw)`
- 성장 영웅: `C:\Users\Storm Credit\Documents\Obsidian Vault\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 & 인물 백과 (Hero Archive)\01-14-2. 성장 영웅 (Growth Heroes)\6. 중립세력 (Neutral)\3. 첩보 (Intelligence)\5. 황금 손아귀 (Golden Claw)`

