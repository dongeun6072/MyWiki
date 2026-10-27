---
title: >-
    서울동행맵 테스트 케이스 전체 (TC 512건)
category: references
tags: [seoul-donghaengmap, testing, qa, accessibility, visibility/internal]
aliases: [TC 전체, 테스트 케이스, RTM]
relationships:
  - target: "[[seoul-donghaengmap-screen-design]]"
    type: derived_from
sources: [~/Develop/Wiki/_raw/articles/project-seoul/TestCase_아이나비시스템즈/TC-전체_260914.xlsx]
summary: >-
    2026-09-14 기준 테스트 케이스 512건의 구성: 41개 화면, 135개 요건 커버, 성격별(기능 269, 접근성 167, 비기능 47), 상태(미실행 427, 보류 85), TC 항목 형식과 예시.
provenance:
  extracted: 0.90
  inferred: 0.10
  ambiguous: 0.00
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: peripheral
created: 2026-10-26T09:31:30+09:00
updated: 2026-10-26T09:31:30+09:00
snapshots:
  - "[[_raw/_archived/TC-전체_260914.xlsx|TC-전체_260914.xlsx]]"
---

# 서울동행맵 테스트 케이스 전체 (TC 512건)

아이나비시스템즈가 만든 테스트 케이스 워크북(2026-09-14)이다. 시트 5개(요약, TC 전체, 매핑, 화면별, 요건별 RTM)로 이루어지고, **정본은 저장소의 `QA/tc/*.toml`(16개 파일)이며 이 엑셀은 그 정본에서 생성한 산출물**이다. 여기서 수정한 값은 정본에 반영되지 않는다. 프로젝트는 [[seoul-donghaengmap]]이다.

## 규모

| 항목 | 값 |
|---|---|
| TC 총 건수 | **512** |
| 대상 화면 | 41(ID 부여 28 + 미부여 13) |
| 커버한 요건 | 135개(TC가 1건 이상 걸린 PRD 요건 ID) |

| 성격 | 건수 | | 상태 | 건수 |
|---|---|---|---|---|
| 기능 | 269 | | 미실행 | 427 (실행 전 초안) |
| 접근성 | 167 | | 보류 | 85 (UX·PRD 사양이 갈려 합불 판정 불가) |
| 비기능 | 47 | | | |
| 시나리오 | 18 | | | |
| 사용자평가 | 1 | | | |
| 대상외 | 10 | | | |

접근성 TC가 전체의 약 **1/3**(167건)이다. 접근성이 사업의 핵심 품질 기준이라는 점이 TC 구성에 그대로 나타난다. ^[inferred] ([[korean-public-mobile-app-compliance]])

## TC 항목 구조

`No`, `TC ID`(예: `TC-AUTH-01-01`), 파일(예: 01-온보딩), 화면(AUTH-01), 요건(V-1, NFR-04, SG-3 등), 성격, 상태, 전제, 절차, 기대결과, KS(한국 표준 연계 열), 근거(UX 문서 절 번호), 비고, 대상외 사유. 요건 ID 접두는 V(시각), NFR(비기능), AC(접근성 수용), SG 등이다.

### 예시 (로그인 화면 AUTH-01)

- 소셜 로그인 버튼이 세로 4개이고 순서가 카카오 → 네이버 → 구글 → 애플인가(iOS)
- Android는 TalkBack을 켠 상태에서 **애플 자리에 빈 항목이나 비활성 버튼이 없고 포커스가 지나가지 않는가**(애플은 iOS 전용)
- 각 버튼에 로고와 텍스트가 함께 있고 **브랜드 색만으로 공급자를 구분하지 않는가**
- 스크린리더 낭독 순서: 서비스명 → 이용 방식 안내 1문장 → 로그인 수단 → 비회원으로 시작하기
- 버튼 낭독 문자열이 "카카오로 로그인, 버튼"처럼 목적지를 담는가
- 인증 실패 시 색·텍스트·아이콘 3채널로 표시하고 포커스가 소셜 버튼 묶음으로 돌아오며 재시도 수단이 남는가

화면기획서([[seoul-donghaengmap-screen-design]])의 낭독 순서와 3채널 표기 원칙, 디자인 가이드([[seoul-donghaengmap-design-system]])의 색 단독 금지가 **TC의 기대결과로 번역**된 모습이다. 접근권한 고지는 U-25가 미확정이라 해당 TC의 판정 대상이 아니라는 비고가 붙어 있다.

## 보류 85건의 의미

화면기획 문서와 PRD의 사양이 서로 달라 합불 기준을 못 정한 항목이다. 두 문서를 맞추는 작업이 끝나기 전에는 실행할 수 없다. ^[inferred]

## Open Questions

- 실행 결과가 없고 전부 초안(미실행)이라 통과율은 알 수 없다.
- TC 정본(`QA/tc/*.toml`)과 `scripts/check_tc.py`는 저장소 안에 있으며 이 vault에는 없다.

## Sources

- [[_raw/_archived/TC-전체_260914.xlsx]] — 테스트 케이스 워크북
