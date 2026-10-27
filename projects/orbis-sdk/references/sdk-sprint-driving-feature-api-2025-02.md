---
title: >-
    신 NaviSDK 스프린트 상세: 주행 Feature 및 API 개발 #1~#3 (2025-02)
category: references
project: orbis-sdk
tags: [navisdk, sprint, tbt, resource-management, visibility/internal]
aliases: [주행 Feature 및 API 개발 - 스크럼, 주행 Feature 및 API 개발 #1 - 리뷰, 주행 Feature 및 API 개발 #2 - 리뷰, 주행 Feature 및 API 개발 #3 - 리뷰, "[2/5] 주행 Feature 및 API 개발", "[2/10] 주행 Feature 및 API 개발 #1", "[2/17] 주행 Feature 및 API 개발 #2", "[2/24] 주행 Feature 및 API 개발 #3"]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/694681601
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/700383234
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/707166221
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/715423746
summary: >-
    주행 컴포넌트(TBT 필수)와 검색/길찾기 API 개발 스프린트(2025-02-05~02-24). iOS 모의주행 정지 원인(NSTimer), 이미지/문자열 공통 리소스 관리 검토 포함.
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

# 신 NaviSDK 스프린트 상세: 주행 Feature 및 API 개발 #1~#3 (2025-02)

주행 컴포넌트(TBT 필수 제공)와 검색/길찾기 API를 만드는 스프린트다. 2/5 스크럼 페이지에는 한 페이지에 4개 시점의 표가 쌓여 있고(날짜 없음) 이후 리뷰 3개(2/10, 2/17, 2/24)가 이어진다. 앞 구간 [[sdk-sprint-kmp-base-logic-2025-01]], 다음 구간은 [[sdk-sprint-taiwan-plan-and-structure-2025-03]], 허브 [[sdk-sprints-2024-2025-hub]].

## [2/5] 주행 Feature 및 API 개발 - 스크럼

- 목표: 주행 컴포넌트 추가(TBT 필수), 검색/길찾기 등 API 개발

### 시점 1

| 담당 | 완료 | 진행중/할것 | 문제 |
|---|---|---|---|
| 앱 개발자 1 | - | NSDK-334, NSDK-342 | iOS 모의주행 비정상 동작(멈춰 있는 상태에서 주행 안 함). MR 문제로 예상, 추가 검토 필요 |
| 앱 개발자 2 | NSDK-340 | NSDK-341, NSDK-347 | - |
| 앱 개발자 3 | - | NSDK-331 | - |
| [[이동은]] | NSDK-339 | NSDK-346 | - |

차기 진행 항목:
- 데이터 연동(공통) → 1명: runguidance 구동 로직, 안내(TBT) getter 로직(동시성 데이터 이슈 확인)
- View(OS별), ViewModel(공통) → 나머지: 아이콘 + 텍스트 표출, 이미지 관리(ViewModel 공통)

### 시점 2

| 담당 | 진행중/할것 |
|---|---|
| 앱 개발자 1 | NSDK-334, NSDK-351 |
| 앱 개발자 2 | NSDK-353 |
| [[이동은]] | NSDK-346 |

- 앱 개발자 2: 이미지 공통 리소스(이미지, strings 등) 관리 Lib 검토. 공통 관리 vs OS별 관리의 장단점 검토. 외부 변경 가능성(3rd Party, AIR 앱, NSDK)을 고려.
- 공통: OS View 작업 진행 방법 논의 필요.

### 시점 3

| 담당 | 진행중/할것 | 문제 |
|---|---|---|
| 앱 개발자 1 | NSDK-334, NSDK-351 | iOS 모의주행 비정상 동작(멈춰서 주행하지 않는 이슈). 기존 "MR 문제로 예상" 문구에 취소선 처리(원인 정정) |
| 앱 개발자 2 | NSDK-356 | - |
| 앱 개발자 3 | NSDK-354 | - |
| [[이동은]] | NSDK-357 | - |

- 앱 개발자 1: iOS 모의주행 정지 이슈. 원인은 iOS에서 사용하는 NSTimer가 비동기 컨텍스트에서 실행되면 동작하지 않는 것. 해결은 타이머 생성(초기화) 부분이 Main Thread에서 생성되도록 변경.
- 앱 개발자 2: 리소스(이미지, 문자열) 통합 관리.
- 앱 개발자 3, [[이동은]]: (내용 없음)

### 시점 4

| 담당 | 진행중/할것 |
|---|---|
| 앱 개발자 1 | NSDK-359 |
| 앱 개발자 2 | NSDK-360 |
| 앱 개발자 3 | NSDK-354 |
| [[이동은]] | NSDK-358, NSDK-357 |

## [2/10] 주행 Feature 및 API 개발 #1 - 리뷰

- 스프린트 목표: 주행 컴포넌트 추가(TBT 필수), 검색/길찾기 등 API 개발
- 상세: 데이터 연동(공통, 1명): runguidance 구동 로직, 안내(TBT) getter 로직(동시성 이슈 확인). View(OS별)/ViewModel(공통, 나머지 인원): 아이콘 + 텍스트 표출, 이미지 관리(ViewModel 공통).
- 완료: NSDK-340, NSDK-341, NSDK-347, NSDK-339, NSDK-342
- 이관: NSDK-334, NSDK-331, NSDK-346, NSDK-351
- 차기 플래닝 목표: 동일
- 이슈(기타 업무 대응): 앱 개발자 1은 orda 대응, 앱 개발자 2는 tomtom MW 대응

## [2/17] 주행 Feature 및 API 개발 #2 - 리뷰

- 스프린트 목표: 동일. 상세에서 "이미지 관리(ViewModel 공통)" 항목에 "이미지 공통 리소스 관리 장/단점 확인 검토"가 추가됨.
- 완료: NSDK-353, NSDK-346, NSDK-355
- 이관: NSDK-334, NSDK-351, NSDK-356, NSDK-354, NSDK-357
- 차기 플래닝 목표: 동일 + 이미지 공통 리소스(이미지, strings 등) 관리 Lib 검토 (공통 vs OS별, 장단점, 외부 변경 가능성: 3rd Party, AIR 앱, NSDK)
- 이슈: 기타 업무 대응(앱 개발자 1: orda, 앱 개발자 2: tomtom MW)

## [2/24] 주행 Feature 및 API 개발 #3 - 리뷰

- 스프린트 목표: #2와 동일
- 완료: NSDK-351, NSDK-356
- 이관: NSDK-334, NSDK-359, NSDK-360, NSDK-354, NSDK-358, NSDK-357
- 차기 플래닝 목표: 동일 + 공통 리소스 Lib 검토를 "이미지(xx, xxxhdpi), String(다국어), 컬러 공통 관리 가능 확인"으로 구체화
- 이슈: RoadColor 데이터 확인. 기타 업무 대응(앱 개발자 1: orda, 앱 개발자 2: tomtom MW)

## 항목별 상태 변화

| 항목 | 처음 등장 | 변화 |
|---|---|---|
| iOS 모의주행 정지 | 2/5 시점 1 | 시점 3에서 원인(NSTimer 비동기 컨텍스트) 확인 및 해결 방안(Main Thread 생성) 기록 |
| 공통 리소스 관리 Lib 검토 | 2/5 시점 2 | 2/17 목표로 명시, 2/24 "xx~xxxhdpi 이미지, 다국어 String, 컬러" 가능 확인으로 구체화 |
| NSDK-334 | 2/3 이관 | 2/10, 2/17, 2/24 연속 이관 |
| NSDK-351 | 2/5 시점 2 | 2/10 이관, 2/17 이관, 2/24 완료 |
| NSDK-346 | 2/5 시점 1 | 2/10 이관, 2/17 완료 |
| NSDK-354, NSDK-357 | 2/5 시점 3 | 2/17, 2/24 이관 |
| NSDK-356 | 2/5 시점 3 | 2/17 이관, 2/24 완료 |
| NSDK-359, NSDK-360, NSDK-358 | 2/5 시점 4 | 2/24 이관 |
| NSDK-331 | 2/5 시점 1 | 2/10 이관 이후 기록 없음 |
| 다른 업무 대응(orda, tomtom MW) | 2/10 | 2/24까지 이슈로 유지 |

## Related
- [[navisdk-confluence-sprint-timeline-2024-2026]] — 기존 요약 타임라인
- [[orbis-navisdk-architecture-and-flutter-plan]] — 구조 설계와 Flutter 계획
- [[orbismap-route-and-tomtom-sdk-review-2025]] — TomTom SDK 검토
- [[orbis-sdk]]

## Sources
- Confluence "[2/5] 주행 Feature 및 API 개발 - 스크럼" (pageId 694681601) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[2/10] 주행 Feature 및 API 개발 #1 - 리뷰" (pageId 700383234) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[2/17] 주행 Feature 및 API 개발 #2 - 리뷰" (pageId 707166221) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[2/24] 주행 Feature 및 API 개발 #3 - 리뷰" (pageId 715423746) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
