---
description: Item Encyclopedia Creation Standard (Premium Quality)
---

# 💎 아이템 도감 생성 표준 워크플로우

이 워크플로우는 **프리미엄 퀄리티**의 아이템(무기, 방어구, 장신구, 도구 등) 파일을 생성하기 위한 표준 절차입니다. `01-19. 아이템 도감`의 체계를 따릅니다.

---

## 🚀 1. 준비 단계 (Preparation)

1.  **분류 확인 (Category)**
    - **무기 (Weapons):** 검, 창, 활, 지팡이 등.
    - **방어구 (Armor):** 갑옷, 투구, 방패 등.
    - **악세서리 (Accessories):** 반지, 목걸이, 귀걸이 등.
    - **유물 (Relics):** 고대 유물, 신물 등.

3.  **무기 세부 종류 태그 (Weapon Subtype)** — 무기인 경우 반드시 지정
    - `weapon-type/longsword` — 한손검 (Longsword)
    - `weapon-type/greatsword` — 양손검 (Greatsword)
    - `weapon-type/dagger` — 단검 (Dagger)
    - `weapon-type/spear` — 창 (Spear)
    - `weapon-type/lance` — 랜스 (Lance)
    - `weapon-type/bow` — 활 (Bow)
    - `weapon-type/crossbow` — 석궁 (Crossbow)
    - `weapon-type/staff` — 지팡이 (Staff)
    - `weapon-type/wand` — 완드 (Wand)
    - `weapon-type/axe` — 도끼 (Axe)
    - `weapon-type/mace` — 철퇴/메이스 (Mace)
    - `weapon-type/whip` — 채찍 (Whip)
    - `weapon-type/fist` — 권갑/너클 (Fist)
    - `weapon-type/special` — 특수 (부채, 펜, 묵주 등)

4.  **폴더 구조 규칙 (Folder Organization)**
    - 모든 아이템은 **세력별 폴더** 안에 정리 (현재 무기 구조와 동일)
    - 방어구, 악세서리, 유물도 세력별 하위 폴더 생성
    - 무기 종류는 폴더가 아닌 **YAML 태그**로 분류
    - 파일명 규칙: `[코드]-[번호]. [한글명] ([영어명]).md`
      - 예: `W-SH-001. 태양의 셉터 (Scepter of the Sun).md`
      - 코드: W(무기), A(방어구), AC(악세서리), R(유물) + 세력약자
    
2.  **등급 설정 (Rank System)**
    - **신화 (Mythic)**: 🔴 **Red** - 신의 힘, 세계관 유일템.
    - **전설 (Legendary)**: 🟠 **Orange** - 역사적 영웅의 유물.
    - **영웅 (Heroic)**: 🟣 **Purple** - 특수 능력이 있는 명품.
    - **희귀 (Rare)**: 🔵 **Blue** - 마법이 깃든 장비.
    - **일반 (Common)**: ⚪ **White** - 표준 장비.

---

## 📝 2. 파일 생성 (Creation) - 프리미엄 템플릿

아래 양식을 복사하여 새 파일을 생성합니다.

```markdown
---
tags:
  - item/[category:weapon/armor/accessory/relic]
  - rank/[rank:mythic/legendary/heroic/rare/common]
  - weapon-type/[subtype] # 무기인 경우만 (longsword/greatsword/dagger/spear 등)
  - owner/[소유자명_혹은_none]
  - faction/[소속_세력명]
aliases:
  - [영어 이름]
  - [한글 이름]
  - [별명]
type: item
---

# [한글 아이템명] ([영어 아이템명])

> *"[아이템에 얽힌 전설이나 묘사 한 줄]"*

---

## 1. 기본 정보

| 항목 | 내용 |
|------|------|
| **분류** | [무기/방어구/악세서리] - [세부 유형: 롱소드, 판갑 등] |
| **등급** | **[등급 (예: 전설급)]** [이모지: 🔴/🟠/🟣/🔵/⚪] |
| **가치** | [금화 가격 혹은 '산출 불가'] |
| **현재 소유자** | **[[소유자 이름]]** |

### 외형 묘사
- [아이템의 시각적 특징, 재질, 빛깔 등]
- [착용 시 특이사항]

---

## 2. 성능 및 효과 (Stats & Effects)

| 유형 | 효과 | 비고 |
|------|------|------|
| **기본 성능** | [공격력/방어력 수치 또는 묘사] | [내구도 등] |
| **마법 효과** | [인챈트 효과] | [속성 등] |

### **고유 능력: 《[능력명]》**
- **설명:** [구체적인 발동 조건 및 효과]
- **패널티:** [사용 시 부작용이나 제약 사항 (없으면 생략)]

---

## 3. 배경 스토리 & 전승 (Lore)

### **[제작 기원]**
[누가, 언제, 어떻게 만들었는가? 재료는 무엇인가?]

### **[역대 주인]**
[이 아이템을 거쳐 간 인물들이나 얽힌 사건]

---

## 4. 입수 경로 & 퀘스트 (Acquisition)

- **[획득처]:** [던전 드롭, 제작, 혹은 특정 NPC 소지]
- **[관련 퀘스트]:** [퀘스트명 혹은 획득 조건]

---

## 🔗 관련 문서
- [[현재 소유자 (Current Owner)]]
- [[관련 지역 (Related Location)]]
```

---

## ✅ 3. 하네시스 검증 및 생태계 맵핑 (Hanesis Verification & Ecosystem Mapping)

1.  **가혹한 섭리 등급화 (Grim Balancing)**
    - "이 압도적인 성능에 걸맞은 치명적인 페널티(수명 단축, 마나 중독, 이성 상실 등)가 존재하는가?"
    - "고유 능력이 세계관의 핵심 마법 체계(01-31~01-42)에 위배되지 않는가?"
    
2.  **N:N 맵핑 (N:N Cross-Mapping)**
    - **아이템 ↔ 인물:** `현재 소유자` 링크(`[[ ]]`)가 올바르게 연결되었는가? (소유자의 무기고에도 이 아이템 링크가 양방향으로 연결되어야 함)
    - **13대 백과 연동:** 아이템의 기원과 특수 기능이 **마도공학 백과(01-35)**, **연금 백과(01-34)** 등 아스트라리스 크로니클의 적절한 마스터 백과와 명확한 `[[Wikilink]]`를 맺고 있는가?
