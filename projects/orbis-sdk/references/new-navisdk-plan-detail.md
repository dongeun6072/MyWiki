---
title: >-
    New NaviSDK Plan 상세 (신규 SDK 구조·UI 확장성·개발 순서)
category: references
project: orbis-sdk
tags: [navisdk, kmp, architecture, ui-extensibility, visibility/internal]
aliases: [New NaviSDK Plan, 신규 NaviSDK 계획]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/511311892
summary: >-
    제로베이스 신규 NaviSDK의 필요성, KMP 구조, 모듈 관계, UI 확장성 요구사항, 개발 순서, 다국어·사용량 체크·CI/CD 방안과 수정 이력 전체
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

# New NaviSDK Plan 상세

기존 NaviSDK의 한계를 해결하기 위해 제로베이스로 신규 SDK를 개발하는 계획 문서(마지막 수정 2025-03-26)를 압축 없이 옮긴 페이지다. 요약은 [[orbis-navisdk-architecture-and-flutter-plan]], 상태 관리 상세는 [[navisdk-ui-state-flow-detail]], Flutter 플러그인은 [[navisdk-flutter-plugin-plan-detail]]를 본다. 전체 목차는 [[orbis-design-and-review-hub]].

## 수정 내역

| 날짜 | 변경 |
|---|---|
| 2025-03-26 | SDK 세부구조도 변경(Default UI 관련 내용 추가), 모듈관계도 추가 |
| 2024-12-17 | SDK 구조도·세부구조도 변경, 공용 로직에서 각 플랫폼별 파일 저장 방안 추가 |
| 2024-11-25 | SDK 구조도·세부구조도 변경 |
| 2024-11-07 | SDK 구조도·세부구조도 변경, UI 확장성 검토 내용 추가, 불필요 내용 제거 |

## 개요
1. 기존 NaviSDK의 개선 및 문제점 해결을 위해 제로베이스에서 신규 SDK를 개발한다.
2. 신규 SDK를 사용하여 아이나비 에어(AIR)도 리뉴얼한다.

## 필요성
1. 3rd Party(고객사)가 원하는 시나리오대로 적용하기 어렵다.
   - 특정 UI를 숨기거나 표출하는 기능이 제한되어 있고, 위치 변경이나 동작 사양 개입이 불가능하다.
   - 예: 주행 화면에서 휴게소가 있는 경우에만 TBT를 표출, 사용자 UI가 좌측에 있어 TBT 등의 UI를 우측으로 옮기고 싶은 경우.
2. 기존 SDK 자체가 AIR에서 파생된 프로젝트라 레거시 코드가 많고 확장성을 고려하지 않아, 기존 구조를 바꿔서 확장성을 제공할 수 없다.
3. 최근 고객사에서 멀티플랫폼 SDK(Flutter) 문의가 들어와 Flutter Plugin 제공 필요성이 커졌다.

그러므로 UI를 확장할 수 있는 구조의 SDK를 개발하고, 필요 시 특정 UI는 해당 플랫폼에서 직접 구현하는 방식도 가능하게 한다.

## SDK 기능 범위
- UI는 최소화하되 확장 가능한 UI Component 형태로 제공한다.
  - 사용자 입장에서 다양한 시나리오를 적용하되 Navigation SDK 특성은 잃지 않는 선에서 UI를 제공한다.
  - 주행/모의주행 UI는 기존과 동일하게 제공한다(예: TBT, LaneView, SafetyView 등).
- 검색, 길찾기, 길안내, 모의주행, 특화 기능(자전거/도보 탐색, 트럭향 등)을 제공한다.

## 개발 방향성
1. New SDK 개발의 1차 목표는 UI와 시나리오(비즈니스 로직)를 분리한 구조로 확장성·유지보수를 개선하는 것이다.
2. UI Components는 사용자가 수정할 수 있어야 한다. 사용자가 표출 여부를 결정하고 위치를 변경할 수 있게 한다.
3. 멀티 모듈로 구성해 기능 간 결합도를 낮추고 재사용성을 높인다.
   - 공통 모듈, 기능별 모듈 등으로 구성해 기능 간섭을 낮춘다.
   - 예: 3rd party용 트럭 특화 기능을 모듈로 작성하면 Common SDK의 기존 기능과 간섭 없이 제작할 수 있고, 나중에 해당 모듈이 Common SDK에 포함될 때 쉽게 재사용할 수 있다.
4. 기본 기능(경로 안내 및 모의주행 가능한 수준까지) 구현 완료 후 Flutter Plugin 개발을 진행한다.

## 마일스톤
1. New Navi SDK [AOS, iOS Native] 개발 — 검색 → 길찾기 → 경로안내 → 모의주행/안내시작 기능이 한 사이클 도는 수준의 1차 버전.
2. 1차 버전 개선 및 보완.
3. SDK 정식 발행 — 기존 SDK가 제공하던 기타 기능(트럭 특화 등)을 포함해 고객사에 전달 가능한 수준.
4. Flutter Plugin 발행.

## 기대효과
- UI 확장성이 늘어 고객별 특화 기능을 API 수준에서 제공하고 UI는 사용자가 확장해 쓰게 하므로 UI 개발 인력 투입 필요성이 낮아진다.
- 이후 AIR의 핵심 기능이 New NaviSDK를 활용하게 해 AIR와 SDK 간 정합성을 보장하고 유지보수 비용을 줄인다.
- Flutter Plugin으로 멀티플랫폼 SDK를 제공한다.

## SDK 구성

제공되는 SDK 목록: Android SDK(.aar), iOS SDK(.xcframework), Flutter Plugin.

### SDK 구조도
(구조도는 이미지 항목, 내용 없음. 아래는 구조도 옆 설명)
- 공용 로직은 Kotlin 단일 모듈로 구성한다(추후 필요 시 모듈 분리).
- Domain Layer에는 ViewModel까지 포함하므로, 추후 Common SDK에서 제공하기 힘든 Custom UI가 필요하면 Presentation Layer만 추가 개발하고 Domain Layer는 재사용할 수 있다. Core SDK는 순수 Kotlin 모듈이라 AOS와 iOS가 재사용할 수 있다.

### 세부구조도 / MapView 다형성 / 모듈 관계도
(모두 이미지 항목. 아래는 구성 요소 정의)

| 구성 요소 | 역할 |
|---|---|
| Usecase | 비즈니스 로직 구현. 필요한 Repository를 생성자로 주입받으며 모든 로직은 usecase로 작성한다. NaviController, ViewModel 등에서 Repository를 직접 참조하지 않도록 규칙을 둔다. |
| Repository | Data 접근 로직(Local, Remote) 구현 |
| NaviMapView | 공용 모듈에서 사용하기 위한 MapView Expect Class. 기존 MapAdapter 기능을 담당하며 실제 MapView는 각 Platform Level에서 Flavor(INavi, Orbis)에 따라 구현한다. |
| NaviViewParent(가칭) | 각 View Components(MapView, TBTView, SafetyView 등)의 Super Class를 Expect~Actual 패턴으로 작성해, 이후 각 플랫폼(AOS, iOS)의 ViewGroup을 상속받아 구현한다. |
| MapViewViewModel | MapController I/F 로직, 지도 UI 컴포넌트(현위치, 줌 인/아웃, 앵글, bottomView) 담당 |
| NaviViewViewModel | NaviView I/F 로직, 내비게이션 컴포넌트(TBT, LaneView, Traffic 등) 담당 |
| NaviView I/F(가칭) | NSDK의 View 확장성 제공 기능(위치 변경, 배경색 변경 등) 담당 |
| Default UI | UI 컴포넌트의 페이지 단위 구현체(검색 화면, 경로 선택 화면 등). 프로젝트에 따라 UI 컴포넌트로 직접 구현하거나 제공되는 샘플 페이지를 사용한다. |

### 각 플랫폼별 실제 파일 저장 방안
- 각 플랫폼으로부터 내부 저장소 경로를 주입받아, Common 레벨에서 해당 경로를 사용해 각 단말에 파일을 저장한다(okio 라이브러리 사용).
- SDK 구조도 draw.io 파일이 첨부되어 있다(링크 항목, 내용 없음).

### Flutter Plugin 구조
- Native SDK는 Flutter 전용 SDK가 아니라 이미 개발된 Native SDK를 재사용한다.
- 기존 SDK 구조에서는 Flutter Plugin 포팅이 어렵다(높은 UI 결합도와 비즈니스 로직 난립 때문).
- 고객사(3rd party 앱)는 Flutter Plugin만 사용하면 되므로 Native 개발 지식이 필요 없다.

## UI 확장성 제공

### 요구사항
1. 사용자가 UI 컴포넌트(예: 차로안내, TBT)를 표출하지 않도록 수정할 수 있다.
2. 모든 컴포넌트(또는 컴포넌트 그룹)는 Show/Hide, 배경색 변경, 위치 지정이 가능하다.
   - 컴포넌트 그룹: Turnview와 SubTurnView는 같은 그룹이며 별개로 위치 지정은 불가능하다.
3. 다국어 지원이 적용된다.

### 확장성 제공 전략 검토
- 각 View의 속성을 정의해 스크립트화하고 JSON 파일로 관리하여 의존성을 주입한다. 예: bgColor, isVisible 등을 결정할 때 VM의 비즈니스 로직보다 해당 구조체의 정의값을 우선한다.
- 스크립트 데이터 서버 연동 검토
  - 현재의 MapData처럼 초기 Download Data에 포함시키는 방식.
  - 적용 전 Feature별 Site 구분이 필요하다("SDK 사용 유저 수 체크 방안"에서 검토한 내용).
  - 서버 연동 시 Custom UI 제공을 위해 별도 SDK를 배포하지 않고 서버에서 직접 반영할 수 있다.

### 제공되는 UI Component
- 지도 레이어 내부 컴포넌트: 마커(출/목/경/높이제한 등), 경로선, 교차로정보, 과속카메라
- 안내 레이어 내부 컴포넌트: 주행속도, TBT, 차선(Laneview), 경로진행도, 안전(Safeview), 과속경고, 복합교차로(ExtendView), 고속도로 뷰(휴게소, TG 등 안내 [HighwayView])

## 개발 항목

### 개발 순서
프로젝트 기본 구조 설계 → 기능별 추상화 모듈 추가 → 엔진 로드 → 지도 로드 → 기본 API 구현(검색, 탐색, 안내) → 1차 회고 → 각 플랫폼별 UI 및 기능별 모듈 완성

### 프로젝트 구조 및 모듈 설계
1. 프로젝트 기본 구조 설계(KMP, Clean Architecture, Multi-Module, DI)
   1. 기본 구조 설계 후 기능별 모듈을 추가하는 방식으로 작업 속도를 높일 수 있게 한다.
   2. 공용/플랫폼별(AOS, iOS) 코드를 분리한다(가능한 공용 모듈에서 비즈니스 로직이 동작하도록 설계).
   3. 유즈케이스, 비즈니스 로직 등 공용 기능을 설계하고 구현한다.
   4. Kotlin Library만 사용해 구현하고, Android/iOS 플랫폼 특화 라이브러리가 필요하면 별도로 구현한다.
2. 멀티 모듈 설계
   1. UI, Utils, Core, Network Module 등.
   2. 각 모듈의 역할/범위를 설정한 뒤 추상화 모듈(껍데기)로 생성해 추가한다.
   3. 이후 투입 인력별로 담당 모듈을 선정해 작업한다.
   4. toml을 활용해 library 관리를 간소화한다.
3. 엔진 로드 — jar/so 등 엔진 로드(AOS/iOS 별도)
4. 네트워크 모듈 작업(kTor)
   1. Auth 처리(인증을 별도 모듈로 구성할지는 작업 중 판단) — SDK 사용량 체크 가능한 구조 검토
   2. 초기 파일 다운로드
   3. API 호출 1차 — 통합검색, 경로탐색, 경로안내
5. 지도 표출 — [3. 엔진 로드]와 [4.2 초기 파일 다운로드] 완료 후 작업 시작
6. API 연동
   1. 지도 컨트롤 기능 연동(터치, 앵글, 주/야간, 줌레벨, 위치 이동 등)
   2. API 호출 2차 — AIR 또는 기존 SDK에서 구현되는 기능 연동(New SDK 기능 범위 상세 정의 필요)
7. UI 개발
   1. Clean Architecture 기반 Presentation Layer로 구현한다.
   2. SDK에 포함되는 공통 UI를 최소화한다.

### 다국어 지원
- 1안: Android, iOS 각 플랫폼 내 리소스 매니저 사용(예: strings.xml)
- 2안: KMP 리소스 라이브러리 사용 검토(예: moko-resources)

### SDK 사용 유저 수 체크 방안
- 기존 패키지명 + private key로는 SDK 사용량 체크가 어렵다.
- 기존 구조에서 각 project별로 발급된 SDK Key를 서버로 전송하면, 서버가 해당 Key가 어떤 Site인지 기본 정보를 포함해 응답하도록 I/F를 추가한다. 예: input(KEY) → output(ENUM) "Ciel_MODBUS" 형태.
- SDK Key 기반 Auth 단계를 추가해, 해당 Auth Key가 invalid가 된 시점부터는 API뿐 아니라 SDK 자체도 사용할 수 없도록 초기 Auth 단계를 둔다.

### CI/CD 구성
- jenkins
- 각 module별 git 별도 관리 검토

## Related
- [[orbis-navisdk-architecture-and-flutter-plan]] — 이 문서의 요약본
- [[kmp-cmp-adoption]] — KMP/CMP 도입 배경
- [[sdk-sprint-initial-setup-architecture-modules-2024-q4]] — 같은 시기 스프린트의 초기 구조 설정
- [[navisdk-ui-state-flow-detail]] — UI 상태 관리 Flow
- [[orbis-sdk]]

## Sources
- Confluence "New NaviSDK Plan" (pageId 511311892) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
