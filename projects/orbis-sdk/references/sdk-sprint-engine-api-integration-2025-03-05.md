---
title: >-
    신 NaviSDK 스프린트 상세: 엔진(지도/검색/탐색) API 연동 #1~#3 (2025-03-31~05-07)
category: references
project: orbis-sdk
tags: [navisdk, sprint, tomtom, engine-integration, visibility/internal]
aliases: [엔진(지도/검색/탐색) API 연동 #1, 엔진(지도/검색/탐색) API 연동 #2, 엔진(지도/검색/탐색) API 연동 #3, "[3/31] 엔진 API 연동", "[4/2] 엔진 API 연동", "[4/7] 엔진 API 연동", "[4/9] 엔진 API 연동", "[4/16] 엔진 API 연동", "[4/21] 엔진 API 연동", "[4/23] 엔진 API 연동", "[4/30] 엔진 API 연동", "[5/7] 엔진 API 연동"]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/752549912
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/756449281
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/760938536
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/762904605
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/769556481
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/772767745
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/776241153
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/783843329
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/788529153
summary: >-
    TomTom Maps SDK 컨트롤과 엔진(DP/검색/탐색) API 연동 스프린트 3회(2025-03-31~05-12)의 플래닝/스크럼 9개 페이지. 영역/역할별 진행, 요청 사항, 디자인/번역 진행 포함.
provenance:
  extracted: 0.88
  inferred: 0.08
  ambiguous: 0.04
base_confidence: 0.6
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T13:00:00+09:00
updated: 2026-10-26T13:00:00+09:00
---

# 신 NaviSDK 스프린트 상세: 엔진(지도/검색/탐색) API 연동 #1~#3 (2025-03-31~05-07)

TomTom Maps SDK를 컨트롤하고 지도(DP)/검색/탐색 엔진 API를 연동하는 구간이다. 이 시기부터 스크럼이 담당 영역(탐색=앱 개발자 1, 검색=앱 개발자 2, 지도=[[이동은]])으로 나뉘고 디자이너와 번역 담당의 진행도 함께 기록된다. 스크럼 표의 Jira/문서 링크는 번호 없이 링크로만 있어 "링크 N개"로만 표시한다. 앞 구간 [[sdk-sprint-taiwan-plan-and-structure-2025-03]], 다음 구간 [[sdk-sprint-main-state-and-screens-2025-05-06]], 허브 [[sdk-sprints-2024-2025-hub]].

## [3/31] 엔진 API 연동 #1 - 플래닝/리뷰 (3/31/2025)

- 스프린트 목표: TomTom Maps SDK 컨트롤
- 기간: 2025-03-31 ~ 2025-04-07 (완료/이관 비어 있음)
- 차기 스프린트 기간: 2025-04-07 ~ 2025-04-14
- 요청 사항
  - 지도: 자차 마커 Asset 정리, custom locationprovider와 camerapostion 차이 확인
  - 탐색: 메인에 필요한 데이터 확인
  - 검색: 데이터 확인, Feature 가능/불가능 부분 확인

## [4/2] 엔진 API 연동 #1 - 스크럼

- 목표: 엔진(DP/검색/탐색) API 연동
- 앱 개발자 1, 탐색: 메인에 사용할 필요 데이터 확인
- 앱 개발자 2, 검색: 데이터 확인 후 Feature별 가능/불가능 확인. **Search API 사용(MapsSDK-Search 모듈은 사용하지 않음).**
- [[이동은]], 지도
  - 자차 마커 Asset 정리: *.glb 사용
  - custom locationprovider와 camerapostion 차이 확인: MapsSDK의 MapDisplay/Location은 기본적으로 사용됨
- 디자이너: 주행 화면 디자인
- 번역 담당: 번역 스크립트

## [4/7] 엔진 API 연동 #2 - 플래닝/리뷰 (4/7/2025)

- 스프린트 목표: 엔진(DP/검색/탐색) API 연동
- 기간: 2025-04-07 ~ 2025-04-21 (완료/이관 비어 있음)
- 차기 스프린트: 목표 동일, 기간 2025-04-21 ~ 2025-05-12
- 요청 사항
  - 지도: (항목만 있음)
  - 탐색: 메인에 필요한 데이터 확인. Content-Type을 json으로 변경 요청. TBT 입력 방식.
  - 검색: 데이터 확인, Feature 가능/불가능 확인. **MVP 수준 가능.**

## [4/9] 엔진 API 연동 #2 - 스크럼

- 앱 개발자 1, 탐색: Content-Type 변경 요청. TBT 입력 방식은 메인에서 처리. 회전 타입은 MVP에서는 현 상태 유지.
- 앱 개발자 2, 검색: (항목만 있음)
- [[이동은]], 지도: (항목만 있음)
- 디자이너(표 1번 행에 별도 기재, 진행 링크 2개): 검색 화면 디자인
- 번역 담당: 번역 스크립트

## [4/16] 엔진 API 연동 #2 - 스크럼

- 표: 앱 개발자 1, 앱 개발자 2, [[이동은]] 각각 완료 링크 2, 진행 링크 1. 디자이너 완료 링크 2, 진행 링크 2.
- 앱 개발자 1: 탐색은 Map Reader so 적용 테스트 필요. 안내.
- 앱 개발자 2, 검색: 집/자주 가는 곳/즐겨찾기 Specout(검색 화면, 메인 화면 구성)
- [[이동은]]: 지도, 경로선택 UI 구성
- 이슈: 번역 리스트 확인 필요
- 디자이너
  - 앱 아이콘/주행/검색 화면 디자인
  - 집/자주 가는 곳/즐겨찾기/최근 목적지 specout. 최근 검색어 유지는 샘플앱에서 개발.
  - 메인 화면 하단바 specout. 개발 진행 후 Hidden 처리.
- 번역 담당: 번역 스크립트(한국어, 영문 같이 진행), 개발자 검토 진행

## [4/21] 엔진 API 연동 #3 - 플래닝/리뷰 (4/21/2025)

- 스프린트 목표: 엔진(DP/검색/탐색) API 연동, 화면별 GUI 구성
- 기간: 2025-04-21 ~ 2025-05-12 (완료/이관 비어 있음)
- 차기 플래닝: 목표 "엔진(DP/검색/탐색) API 연동", 기간 2025-04-21 ~ 2025-05-12
- 요청 사항: 지도, 탐색, 검색 (항목만 있음)

## [4/23] 엔진 API 연동 #3 - 스크럼

- 목표: 엔진(DP/검색/탐색) API 연동, 화면별 GUI 구성
- 내용은 4/16 스크럼과 동일(앱 개발자 1: Map Reader so 테스트, 안내 / 앱 개발자 2: Specout / [[이동은]]: 경로선택 UI / 디자이너 / 번역 담당). 표에서 번역 담당 행은 진행 링크 2개.

## [4/30] 엔진 API 연동 #3 - 스크럼

- 목표: 엔진(DP/검색/탐색) API 연동, 안내엔진(TBT) 개발, 화면별 GUI 구성
- 내용은 4/23과 동일. 차이점은 번역 담당의 **앱 이름 명명** 항목이 추가된 것.
- 표: 앱 개발자 1 완료 링크 3/진행 링크 1, 앱 개발자 2와 [[이동은]] 완료 링크 2/진행 링크 1, 번역 담당 완료 링크 1/진행 링크 2.

## [5/7] 엔진 API 연동 #3 - 스크럼

- 목표: 엔진 API 연동, 안내엔진(TBT) 개발, 화면별 GUI 구성
- 앱 개발자 1: 안내, 메인 상태 관리 정리
- 앱 개발자 2: 카테고리 검색
- [[이동은]]: 주행 컴포넌트(TBT View). 가로모드, 도로명 표출 영역 정리 필요.
- 디자이너: 4/30과 동일
- 번역 담당: 번역 스크립트(한국어, 영문 같이, 개발자 검토), 앱 이름 명명

## 항목별 상태 변화

| 항목 | 처음 등장 | 변화 |
|---|---|---|
| 탐색 메인 필요 데이터 확인 | 3/31 | 4/2 확인, 4/7 Content-Type json 변경 요청, TBT 입력 방식 논의 |
| TBT 입력 방식 | 4/7 | 4/9 메인에서 처리, 회전 타입은 MVP에서 현 상태 유지 |
| Map Reader so 적용 테스트 | 4/16 | 4/23, 4/30까지 "필요" 유지 |
| 검색 Feature 가능/불가능 | 3/31 | 4/7 MVP 수준 가능, 4/16 집/자주 가는 곳/즐겨찾기 Specout, 5/7 카테고리 검색 |
| 자차 마커 Asset | 3/31 | 4/2 *.glb 사용 |
| Search API | 4/2 | MapsSDK-Search 모듈은 사용 안 함 |
| 지도 구성 | 4/16 | 경로선택 UI 구성이 4/30까지 유지, 5/7에 주행 컴포넌트(TBT View)로 이동 |
| 번역 스크립트 | 4/2 | 4/16 한국어/영문 병행 + 개발자 검토, 4/30 앱 이름 명명 추가 |
| 안내엔진(TBT) 개발 | 4/30(목표 추가) | 5/7 안내, 메인 상태 관리 정리 |

## 후속 논의 / 이슈 모음
- 번역 리스트 확인 필요(4/16)
- 가로모드, 도로명 표출 영역 정리 필요(5/7)

## Related
- [[navisdk-confluence-sprint-timeline-2024-2026]] — 기존 요약 타임라인
- [[orbismap-route-and-tomtom-sdk-review-2025]] — TomTom SDK와 경로 검토
- [[taiwan-routeserver-api]] — 대만 RouteServer API
- [[orbis-navisdk-poc-prep-2025]] — PoC 준비
- [[orbis-sdk]]

## Sources
- Confluence "[3/31] 엔진(지도/검색/탐색) API 연동 #1 - 플래닝/리뷰" (pageId 752549912) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[4/2] 엔진(지도/검색/탐색) API 연동 #1 - 스크럼" (pageId 756449281) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[4/7] 엔진(지도/검색/탐색) API 연동 #2 - 플래닝/리뷰" (pageId 760938536) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[4/9] 엔진(지도/검색/탐색) API 연동 #2 - 스크럼" (pageId 762904605) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[4/16] 엔진(지도/검색/탐색) API 연동 #2 - 스크럼" (pageId 769556481) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[4/21] 엔진(지도/검색/탐색) API 연동 #3 - 플래닝/리뷰" (pageId 772767745) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[4/23] 엔진(지도/검색/탐색) API 연동 #3 - 스크럼" (pageId 776241153) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[4/30] 엔진(지도/검색/탐색) API 연동 #3 - 스크럼" (pageId 783843329) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[5/7] 엔진(지도/검색/탐색) API 연동 #3 - 스크럼" (pageId 788529153) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
