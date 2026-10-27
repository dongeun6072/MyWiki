---
title: >-
    에어 SKP 광고 스크럼 #1~#5 (2024-02~03)
category: references
project: inavi-air
tags: [air, scrum, skp, advertising, 2024, visibility/internal]
aliases: [스크럼 #1 - SKP 광고, 스크럼 #2 - SKP 광고, 스크럼 #3 - SKP 광고, 스크럼 #4 - SKP 광고, 스크럼 #5 - SKP 광고]
relationships:
  - target: "[[inavi-air]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/335577089
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/340361217
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/345210930
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/352124929
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/357629954
summary: >-
    2024년 2~3월 SKP 광고 적용, HUD 3월 서비스, 에어 퀴즈 사용자 분석을 안건으로 한 스크럼 5회. 차량/경로선 사이즈 검토(90%), 경로선 화살표 개선, SKP 포인트 서버 연동, ADAS 검토 포함.
provenance:
  extracted: 0.90
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T13:00:00+09:00
updated: 2026-10-26T15:30:00+09:00
snapshots:
  - "[[_raw/_archived/아이나비에어 제안.pdf|아이나비에어 제안.pdf]]"
---

# 에어 SKP 광고 스크럼 #1~#5 (2024-02~03)

[[air-hud-launch-stabilization-scrums-2024]] 이후 이어진 스크럼 5회분이다. 날짜는 #3(2024-02-20), #4(2024-02-27), #5(2024-03-05)가 적혀 있고 #1·#2는 비어 있어 2024-02월 초·중순으로 추정된다. ^[inferred] 목차는 [[air-scrum-records-hub]], 광고/제휴 맥락은 [[air-partner-integrations-2023]]을 본다.

## 공통 사항

- 회의 10:30~12:00. 참석: #1·#2 멘션 10명.
- Agenda(전 회차): HUD 정식 서비스(3월 서비스) / SKP 광고 적용 / 사용자 분석 및 앱테크 기능 추가(에어 퀴즈)
- ToDo(전 회차 동일, 완료 표시 없음): 기획 공지 팝업 문구 작성·스토어 문구 작성 / 디자인 공지 팝업 이미지 제작·스토어 이미지 현행화 / PM TC 작성
- ALL(전 회차): 신규 음성 의견 검토(발랄한, 차분한) — 설 연휴 테스트 후 논의
- Request: 전 회차 "…"(빈 체크박스)
- PM Issues — 독일 출장 일정이 회차별로 늘어남: #1 2월 12일~3월 3일, #2·#3 2월 12일~3월 8일, #4 2월 12일~3월 15일, #5 2월 12일~3월 8일(원문 표기, #4와 불일치). ^[ambiguous]

## #1 (날짜 미기재)

- 기획: 에어 퀴즈 분석 결과 정리 / SKP 광고 검토 / 발랄한 음성 타당성 검토(담당자와 함께)
- 디자인: 차량 사이즈 축소 검토
- Agent: 상품구매 상용 서버 적용 / Admin 페이지 기능 추가
- App: SKP 광고 적용

## #2 (날짜 미기재)

- 기획: #1과 동일
- 디자인: 차량 사이즈 축소 검토 / **[AA/CP] 차량/경로선 사이즈 검토(신규)** — 경로선은 현 상태 유지로 의견, 기본 차량 사이즈 90%로 변경 검토
- Agent: 상품구매 상용 서버 적용 / Admin 페이지 기능 추가(확인 필요) / **통계 API 기능 검토(신규, 일정 확인 필요)**
- App: SKP 광고 적용

## #3 (2024-02-20)

- 기획·디자인: #2와 동일
- Agent: 위 항목 + **SKP 포인트 서버 연동(신규)**
- App: SKP 광고 적용

## #4 (2024-02-27)

- 기획: 에어 퀴즈 분석 결과 정리 (완료) / SKP 광고 검토 (완료) / 발랄한 음성 타당성 검토 (완료) / **ADAS 검토 (완료, 신규 등장 시점부터 완료)**
- 디자인: 차량 사이즈 축소 검토 (완료) / [AA/CP] 차량/경로선 사이즈 검토 (완료, 결론 동일) / **경로선 화살표 개선 (진행중)** — 입체감 개선, 컬러 개선 / **상품 구매하기 번호입력 관련 공지사항 가이드 (진행중)**
- Agent: 상품구매 상용 서버 적용 (완료) / Admin 페이지 기능 추가 (완료) / 통계 API 기능 검토(일정 확인 필요, 미완) / SKP 포인트 서버 연동 (완료)
- App: SKP 광고 적용 (완료)

## #5 (2024-03-05)

- 기획: 에어 퀴즈 분석 결과 정리, SKP 광고 검토, 발랄한 음성 타당성 검토 (완료 유지) / **ADAS 검토 (진행중으로 되돌아감)** ^[ambiguous]
- 디자인: 차량 사이즈 축소 검토, [AA/CP] 차량/경로선 사이즈 검토 (완료 유지) / 경로선 화살표 개선 (진행중 유지: 입체감·컬러) / 상품 구매하기 번호입력 공지사항 가이드는 목록에서 빠짐
- Agent: 상품구매 상용 서버 적용·Admin 페이지 기능 추가·SKP 포인트 서버 연동 (완료 유지) / 통계 API 기능 검토(일정 확인 필요 유지)
- App: SKP 광고 적용 (완료)

## 항목별 상태 변화 요약

| 항목 | 최초 | 최종 상태 |
|---|---|---|
| 에어 퀴즈 분석 결과 정리 | [[air-hud-launch-stabilization-scrums-2024]] #5 | #4 완료 |
| SKP 광고 검토(기획) / 적용(App) | #1 | 기획 #4 완료, App #4 완료 |
| 발랄한 음성 타당성 검토 | #1 | #4 완료 |
| 차량 사이즈 축소 검토 / 차량·경로선 사이즈(AA/CP) | #1 / #2 | #4 완료. 경로선 유지, 기본 차량 90% 변경 검토 |
| 경로선 화살표 개선 | #4 | #5 진행중 |
| ADAS 검토 | #4 | #5 진행중 |
| 상품구매 상용 서버 적용 | #1 | #4 완료 |
| Admin 페이지 기능 추가 | #1 | #4 완료 |
| 통계 API 기능 검토 | #2 | #5까지 일정 확인 필요 |
| SKP 포인트 서버 연동 | #3 | #4 완료 |
| 상품 구매하기 번호입력 공지사항 가이드 | #4 | #5에서 소멸 |

## Related
- [[air-scrum-records-hub]] — 목차
- [[air-hud-launch-stabilization-scrums-2024]] — 직전 스크럼
- [[air-partner-integrations-2023]] — 외부 제휴 맥락
- [[air-usability-stats-and-release-notes-2024]] — 이후 사용성/통계/릴리즈 노트
- [[inavi-air]] — 프로젝트 허브

## 광고 인벤토리 개선 제안 (보강)

날짜가 없는 제안서(PDF)로, SKP 광고 운영 현황과 개선안을 담았다. 수치는 문서의 "최근 30일/7일" 기준이다.

- **현황**: 월 PV 약 164만(AOS 90% 이상), 월 매출 약 212만 원(AOS 95% 이상), DAU 약 2.9만(AOS 85%), 인당 일 광고 PV 2.2(iOS 0.8), CPM 약 1,289원(AOS가 iOS보다 높음), CTR 약 5%(Planet AD 적용 후 4배). 홈 인벤토리가 49%로 가장 크다.
- **제안 1, PV 확대**: 지금은 앱 최초 실행에서만 광고가 호출되므로, 페이지 이동 후 Back과 백그라운드에서 포그라운드 복귀 때마다 **Ad Refresh**를 적용(약 2배 PV 기대). iOS는 앱 종료 없이 BG→FG로 쓰는 비중이 높다. 배너는 각 페이지 첫 화면에 두고, 내비 핵심 동선인 **검색**에 신규 인벤토리를 추가.
- **제안 2, SDK 활용 강화**: 멀티 SDK **Waterfall 미디에이션**(고단가 SDK 우선, No Ad면 다음 SDK 호출)과 서버에서 SDK 호출 순서를 바꾸는 기능(앱 배포 없이), 네이티브 광고 지원 SDK(Google, Adfit)로 일관된 크리에이티브 구성.
- 앞선 스크럼의 항목별 상태는 위 표를 본다. ^[inferred]

## Sources
- Confluence "스크럼 #1 - SKP 광고" (pageId 335577089) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "스크럼 #2 - SKP 광고" (pageId 340361217) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "스크럼 #3 - SKP 광고" (pageId 345210930) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "스크럼 #4 - SKP 광고" (pageId 352124929) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "스크럼 #5 - SKP 광고" (pageId 357629954) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- [[_raw/_archived/아이나비에어 제안.pdf]] — 광고 개선 제안서
