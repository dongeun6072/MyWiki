---
title: >-
    신 NaviSDK 스프린트 상세: 내부 API 설계 - 통합검색, 길찾기, DP 경로선 세팅 (2024-12)
category: references
project: orbis-sdk
tags: [navisdk, sprint, kmp, core-layer, visibility/internal]
aliases: [내부 API 설계 - 통합검색 길찾기 DP 경로선 세팅 - 스크럼, 내부 API 설계 - 리뷰, "[12/04] 내부 API 설계", "[12/16] 내부 API 설계"]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/645267633
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/656048130
summary: >-
    2024-12-04 스크럼(표 4개 시점)과 12-16 리뷰. NaviMainThread 필요 여부, 프로젝트 구조(Presentation/Core Layer), INaviController 역할, suspend 미사용 결정.
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

# 신 NaviSDK 스프린트 상세: 내부 API 설계 - 통합검색, 길찾기, DP 경로선 세팅 (2024-12)

목표는 지도에 경로선이 표출되는 상황까지의 내부 API 설계로, Core(메인)-엔진 데이터 연동 구조 설계와 Auth/권한을 포함한다. 12/04 스크럼 페이지에는 한 페이지에 4개 시점의 표가 쌓여 있다(날짜 없음, 시점 1~4로 표기) ^[ambiguous]. 앞 구간 [[sdk-sprint-initial-map-display-2024-q4]], 다음 구간 [[sdk-sprint-kmp-base-logic-2025-01]], 허브 [[sdk-sprints-2024-2025-hub]].

## [12/04] 내부 API 설계 - 스크럼

- 목표: 내부 API 설계(통합검색, 길찾기, DP 경로선 세팅). Core(메인)-엔진 데이터 연동 구조 설계, Auth/권한.

### 시점 1

| 담당 | 완료 | 진행중/할것 |
|---|---|---|
| 앱 개발자 1 | - | NSDK-275, NSDK-286, NSDK-279 |
| 앱 개발자 2 | NSDK-280, NSDK-285, NSDK-293 | NSDK-291 |
| 앱 개발자 3 | - | NSDK-276, NSDK-277, NSDK-278, NSDK-284 |
| [[이동은]] | NSDK-272 | NSDK-283, NSDK-259 |

소절:
- 앱 개발자 1: static Lib 통합 완료. iOS에서 Core 데이터 Flow 수신 확인(앱 개발자 2와 함께).
- 앱 개발자 2: 공통 모듈 중 네트워크 모듈 완료. Core 데이터 Flow 구조 설계(앱 개발자 1과 함께).
- 앱 개발자 3: static Lib 통합은 DP부터 시작하고 이후 MMC 모듈 통합(DP 완료 시 지도 표출 확인). iOS 권한 로직.
- [[이동은]]: 인증 로직 완료. 공통, AOS 권한 로직.

### 시점 2

| 담당 | 완료 | 진행중/할것 | 문제 | 후속논의 |
|---|---|---|---|---|
| 앱 개발자 1 | NSDK-275 | NSDK-286 | - | - |
| 앱 개발자 2 | NSDK-280, NSDK-285, NSDK-293 | NSDK-291 | NaviMainThread 필요 여부: 앱 개발자 1은 필요, 앱 개발자 2는 "최선인가?" | 역할 세분화 필요: 상태 관리(주행, UI, 모의주행, 지도이동) |
| 앱 개발자 3 | NSDK-279, NSDK-276 | NSDK-277, NSDK-278, NSDK-284 | - | - |
| [[이동은]] | NSDK-272, NSDK-283, NSDK-259 | - | - | - |

소절:
- 앱 개발자 1: iOS에서 데이터 Flow를 받아 수신부 처리.
- 앱 개발자 2: (공통) 데이터 구조 완성, (공통) GPS 데이터 구조 설계, 검색 API 작업 예정.
- 앱 개발자 3: (내용 없음)
- [[이동은]]: iOS Moko-Permission 검토(미정).

후속논의(공통): NaviMainThread가 필요한지 확인. 역할을 세분화해야 하며 문제/장점을 정리한다. 예: 상태 관리(주행, UI, 모의주행, 지도이동), 엔진(MMC/안내) 호출 주기 등.

### 시점 3

| 담당 | 완료 | 진행중/할것 |
|---|---|---|
| 앱 개발자 1 | - | NSDK-286, NSDK-302, NSDK-303 |
| 앱 개발자 2 | - | NSDK-296 |
| 앱 개발자 3 | - | NSDK-300, NSDK-301, NSDK-299 |
| [[이동은]] | NSDK-297 | NSDK-298 |

### 시점 3 이슈 소절

- 구조도의 명칭에 맞게 소스(프로젝트) 명칭 정리.
- Thread 필요 여부: ViewModel 설계 후 개발 검토. 동시성 문제가 있는지 확인 필요. ViewModel을 생성해 전달하는 방향으로 검토. SMR, MMC, 안내 로직 연동과 Data Routine 테스트 방향으로 진행(앱 개발자 2, [[이동은]] 담당).
- Core 모듈 Base 로직 중 미진한 부분 진행. INaviController 역할 정리는 협의 완료.
- 파편화된 테스트용 Usecase를 공통 로직으로 생성 필요: NaviController 초기 인증/검색/길찾기 등. NaviController 테스트 IF 구현(2차 목표 수준).

## [12/16] 내부 API 설계 - 리뷰

- 참석: 앱 개발자 1~3, [[이동은]]
- 스프린트 목표: 위와 동일(내부 API 설계, Core 엔진 데이터 연동 구조, Auth/권한)
- 완료 항목: NSDK-275, NSDK-284, NSDK-280, NSDK-285, NSDK-293, NSDK-291, NSDK-279, NSDK-276, NSDK-277, NSDK-278, NSDK-272, NSDK-283, NSDK-259
- 다음 스프린트 이관: NSDK-286, NSDK-292, NSDK-296
- 차기 스프린트 플래닝: 기존 목표 이어서 진행

### 리뷰 이슈 상세

**Core-NaviMainThread**
- 공통: 역할을 세분화해야 한다. 문제와 장점을 정리한다.
- 앱 개발자 1: "MMC → 안내"는 타이밍 이슈가 있을 수 있다. 상태 체크는 어떤 상황에서 필요한가.
- 앱 개발자 2: 기존 Thread 역할(상태 체크, 상태 데이터 관리)을 확인한 뒤 필요 여부를 결정해야 한다. 실제 개발 검토 후 동시성 문제가 있는지 확인.
- 공통: 구조도와 소스(프로젝트) 구조 정리.

프로젝트 구조 변경:

| 구분 | 현재 | 신규 |
|---|---|---|
| Project Level | Android App, iOS App | (Project Level) |
| Platform Level | androidMain, iOSMain | Presentation Layer: Android App, iOS App - NaviSDK |
| Kotlin Level | commonMain | Core Layer: androidMain + commonMain, iOSMain + commonMain |

- 구조도에 맞게 프로젝트 이름을 변경한다.

**Core-INaviController 역할 정의**
- Core Data Flow 전송을 위한 iOS 환경 구성(SKIE 사용).
- iOS에서 Core의 INaviController에 있는 Suspend 함수를 가져다 쓰기 어렵다. **Suspend는 사용하지 않는 것으로 정리**했다.

**UI는 Presentation Layer와 Core Layer로 역할 정리**
- Presentation: 이미지 관리, 플랫폼 종속적인 데이터
- Core: 공통 로직

## 항목별 상태 변화

| 항목 | 첫 등장 | 변화 |
|---|---|---|
| NaviMainThread 필요 여부 | 12/04 시점 2 | 12/16에도 미결, 역할 세분화로 [[sdk-sprint-kmp-base-logic-2025-01]]에서 이어짐 |
| NSDK-286 | 12/04 시점 1(앱 개발자 1) | 12/16 이관 |
| NSDK-296 | 12/04 시점 3 | 12/16 이관 |
| NSDK-292 | 12/16 이관 | 완료 여부 원문에 없음 |
| 인증 로직 | 12/04 시점 1 완료 | - |

## Related
- [[orbis-navisdk-architecture-and-flutter-plan]] — Presentation/Core Layer 구조의 배경
- [[kmp-cmp-adoption]] — KMP 도입
- [[navisdk-confluence-sprint-timeline-2024-2026]] — 기존 요약 타임라인
- [[orbis-sdk]]

## Sources
- Confluence "[12/04] 내부 API 설계 - 통합검색, 길찾기, DP 경로선 세팅 - 스크럼" (pageId 645267633) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[12/16] 내부 API 설계 - 통합검색, 길찾기, DP 경로선 세팅 - 리뷰" (pageId 656048130) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
