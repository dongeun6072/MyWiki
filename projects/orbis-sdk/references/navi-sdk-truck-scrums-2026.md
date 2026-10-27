---
title: >-
    Navi SDK Truck향 스크럼 (2026-03)
category: references
project: orbis-sdk
tags: [sdk, scrum, truck, visibility/internal]
aliases: [Navi SDK Truck향 스크럼]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1771405315
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1796407298
summary: >-
    2026-03 Navi SDK Truck향 #1~#2. 탐색 Lib 1.0.1.4 연동, MMC 엔진 교체, 지도 버전 분기, 에어 3월 패치 항목.
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

# Navi SDK Truck향 스크럼 #1~#2 (2026-03)

2026년 3월 11일과 18일의 "Navi SDK Truck향" 스크럼이다. 트럭용 경로 사양(차량 제한 탐색)을 담은 Navi SDK를 만드는 짧은 스프린트로, 이전은 [[map-sdk-commercialization-scrums-2026]], 다음은 [[navi-sdk-improvement-scrums-2026]]이다. 트럭 경로 개념은 [[vehicle-restriction-routing]]을 참고한다. 목차는 [[sdk-sprints-2025-2026-hub]].

목표: AOS/iOS Navi SDK Truck 서비스, NaviSDK 유지보수.

## [3/11] #1 (pageId 1771405315)
- 앱 개발자 1/4
  - (완료) 가이드 문서 작성, (완료) 샘플 소스/데모앱(샘플앱) (Map SDK 스프린트에서 이월)
  - 트럭향: 지도 버전 분기 / 탐색 Lib(1.0.1.4) 연동 / MMC 엔진 교체 / API 추가
- 공통
  - **호주향** - Style.json 1벌로 통일(언어, 테마) (이 페이지부터 "호주향"이 앞에 붙음)
  - 통계: SDK 사용자 수 - Appkey당 사용자 수, Appkey/UniqueKey(UUID) 전달
- 언젠가: 인증 실패 시 API 차단 예외 처리, 로그 on/off API(MMC 전달 예정, 탐색은 디버그 출력 생기면)
- [TSD-A01]: Map 카드 메뉴 장소가 언어 변경에 따라 바뀌지 않는 이슈, step1 로그 확인, step2 MW 수정 또는 펌웨어 요청
- **[AIR] 3월 패치 (처음 등장)**
  - 핀크럭스: 신규 광고 유형 송출 - Agent
  - PlanetAD: SDK 버전 업데이트
  - Agent: 에어 캐시룰렛 적립금액 비율 조절 / 에어 미(未)캐시 적립 유효시간 축소 ^[ambiguous]
  - w3w 호출 수 감소
- 접두어: navisdk `inv`, mapsdk `igm`
- 로드맵: 26년 1분기 Map SDK 서비스(~3월 중), Map SDK 가이드 작업, web Map SDK 연동 / 상시 대응(변동 없음)

## [3/18] #2 (pageId 1796407298)
- 앱 개발자 1/4: (완료) 트럭향 - 지도 버전 분기, 탐색 Lib(1.0.1.4) 연동, MMC 엔진 교체, API 추가 / **준상용서버에서 확인** (처음 등장)
- 공통: 호주향 Style.json 1벌, 통계(동일)
- 언젠가: 동일, TSD-A01 항목은 이 페이지에서 사라짐
- [AIR] 3월 패치: 핀크럭스 신규 광고 유형 송출, PlanetAD SDK 업데이트, 에어 캐시룰렛 적립 비율 조절, 에어 미 캐시 적립 유효시간 축소 (w3w 호출 수 감소 항목은 빠짐)
- 앱 개발자 2와의 점심 면담이 24일로 잡힘 (일정 메모)
- 접두어, 로드맵 동일

## 항목 상태
| 항목 | 처음 | 상태 |
|---|---|---|
| 트럭향 4개 작업(지도 버전 분기, 탐색 Lib 1.0.1.4, MMC 엔진 교체, API 추가) | 3/11 | 3/18 완료, 준상용서버 확인 단계 |
| 가이드/샘플/데모앱 | 2/25 | 3/11 완료 |
| 에어 3월 패치 | 3/11 | 3/18까지 유지 (이후 [[sdk-scrum-common-items-2026]]) |

## Related
- [[sdk-sprints-2025-2026-hub]] — 목차
- [[vehicle-restriction-routing]] — 트럭 차량 제한 경로
- [[map-sdk-commercialization-scrums-2026]] — 이전
- [[navi-sdk-improvement-scrums-2026]] — 다음
- [[orbis-sdk]]

## Sources
- Confluence "[3/11] Navi SDK Truck향 #1 - 스크럼" (pageId 1771405315) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[3/18] Navi SDK Truck향 #2 - 스크럼" (pageId 1796407298) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
