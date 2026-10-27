---
title: >-
    에어 HUD 정식서비스 및 안정화 스크럼 #1~#5 (2023-12~2024-01)
category: references
project: inavi-air
tags: [air, scrum, hud, voice, 2024, visibility/internal]
aliases: [스크럼 #1 - HUD 정식서비스 및 안정화, 스크럼 #2 - HUD 정식서비스 및 안정화, 스크럼 #3 - HUD 정식서비스 및 안정화, 스크럼 #4 - HUD 정식서비스 및 안정화, 스크럼 #5 - HUD 정식서비스 및 안정화]
relationships:
  - target: "[[inavi-air]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/305397821
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/310804721
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/317947905
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/324861953
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/330170369
summary: >-
    HUD 정식 서비스와 에어 안정화를 안건으로 한 스크럼 5회. 신규 음성(발랄한/차분한/클래식) 검토, 상품구매 Admin, 할인 정책, 스텝형 주소검색 지하 추가, 스마트 재탐색 로직 검토 포함.
provenance:
  extracted: 0.90
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T13:00:00+09:00
updated: 2026-10-26T13:00:00+09:00
---

# 에어 HUD 정식서비스 및 안정화 스크럼 #1~#5 (2023-12~2024-01)

HUD(로드피아) 정식 서비스 준비와 에어 안정화를 다룬 스크럼 5회분이다. 날짜가 적힌 회차는 #3(2024-01-16), #4(2024-01-23), #5(2024-01-30)이고 #1·#2는 비어 있어 2023-12월~2024-01월 초로 추정된다. ^[inferred] 같은 시기의 광고 스크럼은 [[air-skp-ad-scrums-2024]], HUD 연동 배경은 [[air-hud-integration-2023]], 전체 목차는 [[air-scrum-records-hub]]다.

## 공통 사항

- 회의 10:30~12:00. 참석: #1·#2는 멘션 10명, #3~#5는 멘션 없음.
- ToDo(전 회차 동일, 한 번도 완료 표시 안 됨): 기획 공지 팝업 문구 작성·스토어 문구 작성 / 디자인 공지 팝업 이미지 제작·스토어 이미지 현행화 / PM TC 작성. (템플릿 잔존 항목으로 보임) ^[inferred]
- Issues: #1~#3은 영역별 빈 항목(기획/디자인/Agent/App/PM/사업).
- 신규 음성 3종(Test Apk 배포): 발랄한 / 차분한 / 아이나비 클래식. 각각 서로 다른 성우가 맡았다(성우 이름은 미수록).
- ALL: 신규 음성 의견 검토(발랄한, 차분한) — 음성 퀄리티 검토 (#1 최초, #5까지 진행)

## #1 (날짜 미기재)

- **Agenda**: HUD 정식 서비스 / 에어 안정화
- **Agent**: 상품구매 Admin 구성
- **App**: 음성 Test Apk Test 버전 배포 (진행)
- **ALL**: 신규 음성 의견 검토(발랄한, 차분한) - 음성 퀄리티 검토
- 기획/디자인/PM/엔진: 비어 있음
- **Request**: 체크리스트 "…"(빈 항목)

## #2 (날짜 미기재)

- Agenda 동일.
- Agent: 상품구매 Admin 구성(계속)
- App: 음성 Test Apk Test 버전 배포 **(완료)**
- **엔진(신규)**: 스마트 재탐색 시 기존 경로에 교통정보 갱신 없이 신규 경로와 비교하는 로직 검토 — 금주 중으로 개발서버 적용 후 테스트
- ALL: 신규 음성 의견 검토(계속)
- Request: "…"

## #3 (2024-01-16)

- Agenda 동일.
- **기획(신규)**: 할인 가격 정책 정의 / 스텝형 주소검색 "지하" 추가
- Agent: 상품구매 Admin 구성(계속)
- **App(신규)**: 스텝형 주소검색 "지하" 추가 / 음성 Test Apk 배포(완료 유지)
- 엔진: 스마트 재탐색 로직 검토 — 금주 중 개발서버 적용 후 테스트(계속)
- ALL: 신규 음성 의견 검토(계속)
- **Request**: [ ] 할인정책(할인율, 할인금액) / [ ] 스탬프 2배 적립 이벤트

## #4 (2024-01-23)

- **Agenda 추가**: 사용자 분석 및 앱테크 기능 추가(에어 퀴즈)
- 기획: 할인 가격 정책 정의 (완료) / 스텝형 주소검색 "지하" 추가 (완료)
- **디자인(신규)**: 설 이벤트 디자인 가이드 / 상품 할인 디자인 가이드 (완료) / 스텝형 주소검색 "지하" 디자인 가이드 (완료)
- Agent: 상품구매 Admin 구성 (완료) / **상품구매 상용 적용**(신규)
- App: 스텝형 주소검색 "지하" 추가(진행) / 음성 Test Apk 배포(완료 유지)
- 엔진: 스마트 재탐색 개발서버 적용 후 테스트 (완료) / **신규 경로가 3분 이상 오래 걸리는 경로가 나오면 탐색 성공 (1/26)** (신규, 1월 26일 기준)
- ALL: 신규 음성 의견 검토(계속)
- **Issues (PM)**: 독일 출장 2월 12일~3월 3일
- **Request**: [x] 할인정책(할인율, 할인금액) 완료 / [x] 스탬프 2배 적립 이벤트 완료

## #5 (2024-01-30)

- **Agenda**: HUD 정식 서비스(**3월 서비스**) / 에어 안정화 / 사용자 분석 및 앱테크 기능 추가(에어 퀴즈)
- **기획(신규)**: 에어 퀴즈 분석 결과 정리 / SKP 광고 검토
- 디자인: 설 이벤트 디자인 가이드 (완료) / **차량 사이즈 축소 검토**(신규)
- Agent: 상품구매 상용 서버 적용(진행)
- App: 스텝형 주소검색 "지하" 추가 (완료) / 음성 Test Apk 배포(완료 유지)
- 엔진: 스마트 재탐색 로직 검토 두 항목 모두 (완료)
- ALL: 신규 음성 의견 검토 — **설 연휴 테스트 후 논의**
- Issues (PM): 독일 출장 2월 12일~3월 3일
- Request: "…"
- 이후 안건은 [[air-skp-ad-scrums-2024]]로 이어짐.

## 항목별 상태 변화 요약

| 항목 | 최초 | 완료 / 최종 |
|---|---|---|
| 상품구매 Admin 구성 | #1 | #4 완료 → 상용 적용 #4 → 상용 서버 적용 #5 진행 |
| 신규 음성 Test Apk 배포 | #1 | #2 완료 |
| 신규 음성 품질 검토 | #1 | #5까지 진행, 설 연휴 테스트 후 논의로 이월 |
| 스마트 재탐색 신규 경로 비교 | #2 | #4 개발서버 테스트 완료, 3분 이상 조건 #5 완료 |
| 할인 가격 정책 | #3 | #4 완료 |
| 스텝형 주소검색 "지하" | #3 | 기획·디자인 #4 완료, App #5 완료 |
| 설 이벤트 디자인 가이드 | #4 | #5 완료 |
| 스탬프 2배 적립 이벤트 | #3 Request | #4 완료 |
| 에어 퀴즈 분석 / SKP 광고 검토 | #5 | [[air-skp-ad-scrums-2024]]에서 계속 |

## Related
- [[air-scrum-records-hub]] — 목차
- [[air-hud-integration-2023]] — HUD 연동 배경
- [[air-skp-ad-scrums-2024]] — 같은 시기 후속 스크럼
- [[air-confluence-scrum-and-voice-2023-2024]] — 요약본(음성 포함)
- [[inavi-air]] — 프로젝트 허브

## Sources
- Confluence "스크럼 #1 - HUD 정식서비스 및 안정화" (pageId 305397821) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "스크럼 #2 - HUD 정식서비스 및 안정화" (pageId 310804721) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "스크럼 #3 - HUD 정식서비스 및 안정화" (pageId 317947905) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "스크럼 #4 - HUD 정식서비스 및 안정화" (pageId 324861953) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "스크럼 #5 - HUD 정식서비스 및 안정화" (pageId 330170369) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
