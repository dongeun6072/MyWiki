---
title: >-
    NaviSDK Flutter Plugin Plan 상세 (M1~M4 마일스톤)
category: references
project: orbis-sdk
tags: [flutter, plugin, navisdk, milestone, visibility/internal]
aliases: [NaviSDK Flutter Plugin Plan, 국내향/Orbis Flutter 대응, 국내향/Orbis Navi&Map SDK]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1824686148
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1907621958
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1811054618
summary: >-
    국내향 NaviSDK를 Flutter에서 쓰는 플러그인의 구조, Native 의존성, M1(Android)·M2(iOS) 완료 범위, M3 pub.dev 배포 작업 분해, M4 HUD 스트리밍 검토
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

# NaviSDK Flutter Plugin Plan 상세

기존 국내향 NaviSDK를 Flutter에서 사용할 수 있게 하는 Plugin 개발 계획 문서(2026-04-01 초안, 2026-04-22 M1 완료 후 갱신, 마지막 수정 2026-04-23)다. 신규 SDK와 Flutter의 관계는 [[new-navisdk-plan-detail]]의 "Flutter Plugin 구조", 요약은 [[orbis-navisdk-architecture-and-flutter-plan]], 목차는 [[orbis-design-and-review-hub]].

## 수정 내역
- 2026-04-01: 개요, 구조 등 초기 계획 문서 작성
- 2026-04-22: M1 완료 후 전체 구조도 및 검토 필요한 내용 추가

## 개요
기존 국내향 NaviSDK를 Flutter에서 사용할 수 있는 Plugin을 개발한다.

## 기본 구조

```
inavi_navisdk_flutter_plugin/   ← 단일 레포 (모노레포 아님)
├── android/           ← Kotlin (PlatformView, MethodChannel, EventChannel 골격)
├── ios/               ← Swift (FlutterPlugin, PlatformView, MethodChannel)
├── lib/               ← Dart public API
├── example/           ← 데모 앱 (동작 확인 전용)
└── docs/
    ├── plans/         ← 계획 문서
    ├── architecture/  ← 구조 문서
    ├── adr/           ← 구조 설계 이유 기록 문서
    └── integration-guide/ ← 통합 가이드 문서
```

### Native SDK 의존성
**Android**
- Maven 원격 저장소: `<링크 생략>`
- 아티팩트: `com.inavisys.navisdk:inavi-navigation-sdk:0.9.0`
- 런타임 import 패키지: `com.inaviair.sdk`

**iOS**
- CocoaPods: `pod 'inavi-navigation-sdk'`
- 모듈 import: `import iNaviNavigationSdk`
- iOS 13+ 최소 지원

## 주요 마일스톤 요약

| 마일스톤 | 내용 | 상태 |
|---|---|---|
| M1 | Android 플러그인 | 완료 |
| M2 | iOS 플러그인 | 완료 |
| M3 | pub.dev 공개 배포 | 대기 |
| M4 | Flutter HUD · DriveGuide 스트리밍 | 대기 |

## Milestone 1: Android 플러그인 (완료)

### 목표
NaviSDK의 네이티브 View 전체를 단일 PlatformView로 감싸고, Flutter에서 지도 제어/검색/경로 계획/주행 제어/오버레이 등 모든 SDK 기능을 호출할 수 있게 한다.

### 달성 범위 (이전의 Phase 1-1 ~ 1-11 + 1-11-U + Pre-M2 D 통합)
- Android 프로젝트 세팅 + Kotlin PlatformView 스켈레톤
- ActivityLifecycle 완전 연결(onResume/onPause/onStop/onDestroy)
- Dart 데이터 모델 13종 + Enum 16종(NSDK-689 추가 enum 포함)
- Hybrid Composition(`PlatformViewLink` + `AndroidViewSurface`) — Virtual Display 이슈 해결
- 지도 제어 MethodChannel — 위치/줌/모드/컴포넌트/회전/앱상태
- 검색 MethodChannel — 통합검색, 추천어, 역지오코딩(`getAddress`, `getJibunAddress`, `getCurrentRoadName`)
- 경로탐색 MethodChannel — `setRoute`, `setSingleRoute`, `routeZoomMap`, `getRouteSummary`, `getTotalRemainInfo`, `cancelRoute`
- SDK 추가 제어 API — 차종/볼륨/패딩/이벤트/getter/화물차/최적지점(29개 메서드 + `onNaviEvent` 콜백 + enum 2종)
- 지도 오버레이(MapOverlay/MapIcon) — UUID 기반 관리 + `onMapIconClick` 콜백
- 주행/모의주행 MethodChannel — `startNavigation`, `startSimulation`, `finishSimulation`, `getRemainInfo`, `runReRouteChangeVia`
- Example 앱 전체 데모 기능 추가(검색 → 경로 → 모의주행 → 주행 화면 동작)

## Milestone 2: iOS 플러그인 (완료)

### 목표
Android에서 확립된 Dart Public API를 iOS에서도 그대로 사용할 수 있도록 Swift FlutterPlugin을 구현하고, iOS SDK를 공개 CocoaPods로 통합한다.

### 달성 범위 (이전의 Pre-M2 C + iOS Milestone Plan + iOS CocoaPods 설계 + P0/P1/P2 보완 통합)
- 공개 CocoaPods 의존성 확정: `s.dependency 'inavi-navigation-sdk'`(iOS 13+)
- Swift 3파일 구조(Android와 1:1 대칭): `INaviNavigationPlugin.swift` / `INaviMapFactory.swift` / `INaviFlutterController.swift`(약 763 라인)
- Dart `inavi_map_view.dart`에 `UiKitView` 분기 추가
- `pubspec.yaml` iOS `pluginClass` 선언
- example 앱 iOS 설정 완료: `Info.plist`의 `INaviAppKey`, `NSLocationWhenInUseUsageDescription`, `NSLocationTemporaryUsageDescriptionDictionary`, `UIBackgroundModes: [audio, location]`
- MethodChannel 핸들러 약 70%+ 커버리지 달성 — 지도/검색/경로/주행/차량 설정/오버레이(UUID 딕셔너리 관리)/TBT 색상(hex↔UIColor 변환)/폰트/확대도/경로 좌표(JSON 파싱)/화물차 정보/최적 경로/SafeArea
- iOS Delegate 콜백 연결: `authResultCode`, `didLongTap`, `mapMoveMode`, `menuTouch`, `drivingStatus`, `carSpeed`, `passedIndex` (원문은 "6종"이라 쓰였으나 나열된 항목은 7개 ^[ambiguous])
- iOS SDK 미제공 항목은 `FlutterError("NOT_SUPPORTED")` 또는 `FlutterMethodNotImplemented`로 명시 반환
- 실기기(iPhone) 빌드 + 맵뷰 렌더링 + `onMapReady` 콜백 수신 확인(2026-04-21)

### 알려진 제약
- **시뮬레이터**: 공개 CocoaPods 배포본에 `arm64-simulator` 슬라이스가 없어 Rosetta 2 에뮬레이션으로 실행된다(성능 30~50% 저하). 성능 검증은 실기기가 필수다. 자세한 내용은 `docs/known-issues.md` §6.
- **SPM 마이그레이션 계획**: 시뮬레이터 네이티브 실행을 위해 SPM 버전(`InaviController.shared` Swift API)으로 전환하는 계획이 `docs/plans/2026-04-20-ios-spm-api-migration.md`에 있다. 현재는 미실행.
- **iOS 전용/미제공 정책**: `setLayoutTopSafeArea` / `setLayoutLeftRightSafeArea`는 iOS 전용이다. Background TBT 계열, `setGuidanceSettings`, `setAvoidEvasion`, `setZoneLimit` 등은 iOS SDK가 제공하지 않는다.

## Milestone 3: pub.dev 공개 배포 (대기)

### 목표
pub.dev에 직접 공개 배포한다. 레포 관리는 Bitbucket 단일 운영을 유지하며 pub.dev `homepage` 필드는 회사 URL을 사용한다. README 보강도 이 Milestone에서 함께 진행한다.

### 참조 문서
`docs/plans/2026-04-09-deployment-strategy.md` (dry-run Phase 3까지 완료, Phase 4 대기)

### 작업 분해

| Phase | 작업 | 완료 기준 | 상태 |
|---|---|---|---|
| M3-1 | pubspec.yaml homepage 기입 | 회사 URL로 업데이트, `dart pub publish --dry-run` 경고 0건 | 대기 |
| M3-2 | example/ 앱키 플레이스홀더 교체 | 모든 앱키를 `YOUR_APP_KEY_HERE`로 교체, 보안 이슈 없음 | 대기 |
| M3-3 | README.md 보강 | 코드 예제 API 정확성 검증, 콜백 예제, Troubleshooting 섹션, 플랫폼 지원 문구 갱신(Android + iOS) | 대기 |
| M3-4 | pub.dev 공개 배포 | `pub.dev/packages/inavi_navisdk_flutter_plugin` 접근 가능 | 대기 |
| M3-5 | Git 태그 생성 | `v1.1.0` 태그를 Bitbucket에 push | 대기 |

### M3-1 세부 (pubspec.yaml)

```yaml
name: inavi_navisdk_flutter_plugin
description: "iNavi Navigation SDK Flutter plugin. Provides map view, route planning, and turn-by-turn navigation for Android and iOS."
version: 1.1.0
homepage: <링크 생략>    # 회사 웹사이트 URL 확정 필요
```

### M3-3 세부 (README 보강 항목)

| # | 항목 | 우선순위 |
|---|---|---|
| 1 | 코드 예제 API 불일치 수정 — `RoutePoint.simple()` factory, `result.selectedRouteId` 사용 | 필수 |
| 2 | 콜백 예제 추가 — `onDrivingStatus`, `onMapLongClick`, `onMapMoveStart/Stop`, `onNaviEvent` | 필수 |
| 3 | Troubleshooting 섹션 — Maven 저장소 미등록, 앱키 미등록, ARM 에뮬레이터 이슈, `MapDayNightMode.day` 미존재 주의 | 필수 |
| 4 | 플랫폼 지원 문구 — "Android / iOS" 명기 | 필수 |
| 5 | pub.dev 뱃지 — pub points, platform, license | 권장 |

### 버전
`1.1.0` — 정식 공개 배포 첫 버전

## Milestone 4: Flutter HUD · DriveGuide 스트리밍 (대기)

### 목표
지도는 PlatformView를 유지하고, 모든 주행 안내 UI를 Dart 위젯으로 교체한다. NaviSDK는 DriveGuide 데이터를 EventChannel로 스트리밍한다.

### 검토 필요한 내용
1. NaviSDK(AOS/iOS) 브랜치 분리 계획 수립
   1. 기본적으로는 develop(메인) 브랜치로 통합해 SDK Core를 동일하게 유지하고 유지보수 비용을 줄인다.
   2. (두 번째 항목은 원문에 비어 있음)

원문의 브랜치 구성 도식:

```
feature/dev_sdk_module  (개발: 공통 SDK + Flutter 브리지 코드 통합)
        │
        │ 검증 후 merge (--no-ff)
        ▼
      develop           (배포 전용 — Maven publish)
```

- `dev_sdk_module`이 Flutter Plugin 지원을 위한 순수 Kotlin/Java 코드(콜백 인터페이스, iNaviFlutterController 등)를 포함해 개발하고, 검증 완료 후 `develop`으로 머지한다. Flutter 플랫폼 코드(EventChannel 등)는 Flutter Plugin 프로젝트에서 처리한다.

2. Flutter Plugin 전용 AOS NaviSDK(aar) 배포 전략
   1. 세부 계획 수립 필요
   2. 별도 넘버링 진행 검토(기존 SDK, 삼성중공업, Flutter Plugin용 SDK로 총 3가지)

## 하위 페이지 (내용 없음)
- "국내향/Orbis Navi&Map SDK" (pageId 1811054618, 2026-03-24 수정) — 제목만 있는 상위 페이지
- "국내향/Orbis Flutter 대응" (pageId 1907621958, 2026-04-29 수정) — 제목만 있는 페이지. 본문 없음.

## Related
- [[new-navisdk-plan-detail]] — Flutter Plugin이 Native SDK를 재사용하는 이유
- [[orbis-navisdk-architecture-and-flutter-plan]] — 요약
- [[navisdk-confluence-sprint-timeline-2024-2026]] — 스프린트 타임라인(NSDK 티켓 맥락)
- [[navisdk-api-coverage-and-domestic-sdk-guide]] — 국내향 SDK API
- [[orbis-sdk]]

## Sources
- Confluence "NaviSDK Flutter Plugin Plan" (pageId 1824686148) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "국내향/Orbis Flutter 대응" (pageId 1907621958) — 본문 없음
- Confluence "국내향/Orbis Navi&Map SDK" (pageId 1811054618) — 본문 없음
