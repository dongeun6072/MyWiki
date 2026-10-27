---
title: >-
    신 NaviSDK 스프린트 상세: KMP Base 로직 강화 #1~#4 (2025-01~02)
category: references
project: orbis-sdk
tags: [navisdk, sprint, kmp, navimainthread, visibility/internal]
aliases: [KMP Base 로직 강화 - 리뷰, KMP Base 로직 강화 #2 - 리뷰, KMP Base 로직 강화 #3 - 리뷰, KMP Base 로직 강화 #4 - 리뷰, "[1/6] KMP Base 로직 강화", "[1/13] KMP Base 로직 강화 #2", "[1/20] KMP Base 로직 강화 #3", "[2/3] KMP Base 로직 강화 #4"]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/667190320
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/674725889
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/683049171
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/688947201
summary: >-
    KMP Base 로직 강화 스프린트 4회(1/6, 1/13, 1/20, 2/3) 리뷰 상세. NaviMainThread 역할 세분화, SMR/MMC 연동, INaviController 대표 API 구현 목표와 완료/이관 티켓.
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

# 신 NaviSDK 스프린트 상세: KMP Base 로직 강화 #1~#4 (2025-01~02)

기존 NaviMainThread의 역할을 세분화하고 프로젝트 구조를 정리하는 4개 스프린트의 리뷰 페이지다. 이 구간에는 스크럼 페이지가 없고 리뷰 4개만 있다. 앞 구간 [[sdk-sprint-internal-api-design-2024-12]], 다음 구간 [[sdk-sprint-driving-feature-api-2025-02]], 허브 [[sdk-sprints-2024-2025-hub]]. 모든 리뷰의 참석자는 앱 개발자 1~3과 [[이동은]]이다.

## [1/6] KMP Base 로직 강화 - 리뷰

- 스프린트 목표: 내부 KMP Base 로직 강화
  - 기존 NaviMainThread 역할을 세분화하여 구조화
  - 구조도와 소스(프로젝트) 구조 정리
- 완료: NSDK-300, NSDK-308, NSDK-305, NSDK-309
- 이관: NSDK-311(Orbis 표기), NSDK-306, NSDK-310(Orbis 표기)
- 차기 플래닝 목표
  - 내부 Base 로직 강화
    - NaviMainThread 역할 세분화: UseCase 개발 검토 후 결과 확인(동시성 문제 확인), MMC/안내 Data Flow 정리
    - 구조도와 소스 구조 정리: INaviController 역할 정리
  - 내부 Base 로직 세분화
    - MMC 엔진 초기화 및 연동
    - SMR 엔진 초기화 및 연동
    - INaviController 대표 API 구현: runRoute
- 이슈, 기타 의견: 없음

## [1/13] KMP Base 로직 강화 #2 - 리뷰

- 스프린트 목표: 위 목표에 세부 항목 추가
  - SMR 컨트롤러 구현
  - NaviMainThread의 데이터 수집/가공 구조 설계 및 구현
  - 탐색 길찾기 연동
  - MMC 데이터 연동
  - 구조도와 소스 구조 정리
- 완료: NSDK-318, NSDK-313, NSDK-321
- 이관: NSDK-320, NSDK-315, NSDK-324, NSDK-323, NSDK-314
- 차기 플래닝 목표
  - NaviMainThread 세분화: UseCase 개발 검토(동시성 확인), 데이터 관리 → 엔진(MMC, 안내) 데이터 수집/가공
  - INaviController 역할 정리 - **완료**
  - 내부 Base 로직 세분화: MMC/GPS 비즈니스 로직 통합(논의 후 티켓 정리 필요), SMR 엔진 연동 및 컨트롤러 구현, 길찾기 API(runRoute) 구현

## [1/20] KMP Base 로직 강화 #3 - 리뷰

- 스프린트 목표: #2와 동일
- 완료: NSDK-320, NSDK-326, NSDK-328, NSDK-324, NSDK-323, NSDK-314
- 이관: NSDK-332, NSDK-334, NSDK-333, NSDK-327, NSDK-329, NSDK-330, 그리고 번호 없이 링크만 있는 항목 1개(링크 항목, 내용 없음)
- 차기 플래닝 목표(내부 Base 로직 세분화)
  - iOS 포인터 배열 로직 개선
  - 현위치 및 LastGPS 관리 로직: NaviLocation 구조 통합 및 정리
  - MMC/GPS 비즈니스 로직 통합 및 정리
  - INaviController 대표 API 구현: rData, gData, tData 다운로드 및 Parsing

## [2/3] KMP Base 로직 강화 #4 - 리뷰

- 스프린트 목표: #2와 동일
- 완료: NSDK-332, NSDK-327, NSDK-335, NSDK-330, NSDK-329, NSDK-336, NSDK-337, NSDK-338
- 이관: NSDK-334, NSDK-333, NSDK-342, NSDK-340, NSDK-341, NSDK-331, NSDK-339
- 차기 플래닝 목표: 주행 Feature 및 API 개발 - 주행 컴포넌트 추가(TBT 필수), 검색/길찾기 등 API 개발 ([[sdk-sprint-driving-feature-api-2025-02]]로 이어짐)

## 목표 항목의 진행 변화

| 항목 | 처음 등장 | 상태 |
|---|---|---|
| NaviMainThread 역할 세분화(UseCase 검토, 동시성 확인) | 12/16 | 1/6, 1/13 차기 목표로 반복. 2/3 리뷰의 스프린트 목표에도 남아 있음 |
| INaviController 역할 정리 | 12/16 | 1/13 리뷰에서 "완료" |
| MMC 엔진 초기화/연동, SMR 엔진 초기화/연동 | 1/6 | 1/13에 SMR 컨트롤러 구현·MMC 데이터 연동으로 세분화 |
| 길찾기 API runRoute | 1/6 | 1/13에도 구현 목표 |
| MMC/GPS 비즈니스 로직 통합 | 1/13 | 1/20 "통합 및 정리" |
| rData/gData/tData 다운로드 및 Parsing | 1/20 | 2/3 이후 계획에 별도 언급 없음 |
| iOS 포인터 배열 로직 개선, NaviLocation 통합 | 1/20 | 완료 여부 원문에 없음 |

## 티켓 흐름(번호만)

| 티켓 | 이관 이력 | 완료 |
|---|---|---|
| NSDK-320, NSDK-324, NSDK-323, NSDK-314 | 1/13 이관 | 1/20 |
| NSDK-332, NSDK-327, NSDK-330, NSDK-329 | 1/20 이관 | 2/3 |
| NSDK-334, NSDK-333 | 1/20, 2/3 이관 | 이후 [[sdk-sprint-driving-feature-api-2025-02]]에 계속(NSDK-334는 2/24 리뷰에도 이관) |
| NSDK-331, NSDK-339, NSDK-340, NSDK-341, NSDK-342 | 2/3 이관 | 2/10 리뷰에서 NSDK-339, 340, 341, 342 완료 |
| NSDK-315 | 1/13 이관 | 이후 기록 없음 |
| NSDK-306, NSDK-311, NSDK-310 | 1/6 이관 | 이후 기록 없음 |

## Related
- [[navisdk-confluence-sprint-timeline-2024-2026]] — 기존 요약 타임라인
- [[orbis-navisdk-architecture-and-flutter-plan]] — 아키텍처 설계
- [[kmp-cmp-adoption]] — KMP 도입
- [[orbis-sdk]]

## Sources
- Confluence "[1/6] KMP Base 로직 강화 - 리뷰" (pageId 667190320) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[1/13] KMP Base 로직 강화 #2 - 리뷰" (pageId 674725889) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[1/20] KMP Base 로직 강화 #3 - 리뷰" (pageId 683049171) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[2/3] KMP Base 로직 강화 #4 - 리뷰" (pageId 688947201) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
