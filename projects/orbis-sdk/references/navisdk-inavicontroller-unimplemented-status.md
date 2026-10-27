---
title: >-
    NaviSDK INaviController API 적용 현황(미 구현 항목)
category: references
project: orbis-sdk
tags: [navisdk, inavicontroller, api-coverage, unimplemented, overseas, visibility/internal]
aliases: [미 구현 항목 현황 - 지속 업데이트, INaviController Reference 현황]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/973078739
summary: >-
    해외향 Orbis NaviSDK의 미구현 항목과 국내향 INaviController API 전체의 적용 여부·지원 가능 여부 표(2025-08-28), 신규 추가 함수 정리.
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

# NaviSDK INaviController API 적용 현황(미 구현 항목)

2025-08-28 수정본 "미 구현 항목 현황 - 지속 업데이트"를 옮겼다. 개발자별 미구현 항목과, 국내향 SDK의 `INaviController` API가 해외향 SDK 환경에서 호환 가능한지 확인한 표가 핵심이다. 국내 SDK 가이드와의 비교는 [[navisdk-api-coverage-and-domestic-sdk-guide]], 프로젝트 개요는 [[orbis-sdk]], 목차는 [[air-internal-docs-and-integration-hub]]를 본다.

## 개발자(역할)별 미구현 항목

### 안내 담당 SDK 개발자
- **안내**
  - 모의주행: 턴 앞/뒤로 이동하는 로직의 MMC 전달 코드를 확인한 뒤 개발 필요
  - 후방 안내: 음성 안내 미개발. 후방 관련 거리 사양은 개발 완료(m 단위로 설정 가능)
  - 과속 효과음
- **지도**
  - 자차 애니메이션 개선 필요 (완료)
  - 지나간 경로 표출 개선 필요 (완료)
  - 차기/차차기 경로 유도선 개선 필요 (완료)

### 다른 SDK 개발자
- `isDebug` 옵션 변경 필요: NaviSDK가 release 빌드여도 3rd party 앱이 디버그 빌드하면 DEBUG로 판단하는 문제
- SDK 배포 시 코드 난독화 적용 필요

### [[이동은]]
- `INaviController` Reference 현황: 국내향 SDK에서 쓰는 API가 해외향 SDK 환경에서 호환 가능한지 확인하기 위해 사용 현황을 먼저 파악.

## INaviController API 적용 현황

적용 여부: `완료` = 해외향 SDK에 적용됨, `X` = 미적용. 지원 가능 여부: `O` = 지원 가능, `X` = 지원 불가.

### 초기화

| API | 적용 여부 | 지원 가능 여부 |
|---|---|---|
| `loadNaviLibrary` | 완료 | O |
| `initLayout`(MapView Id) | 완료 | O |
| `initLayout`(Parent View) | X | O |
| `setMapStyle` | X | O |
| `setAudioStreamType` | X | O |
| `setEmulatorMode` | X | O |
| `initalizeNavi` | 완료 | O |

### 지도 컨트롤

| API | 적용 여부 | 지원 가능 여부 |
|---|---|---|
| `setMapClickListener` | 완료 | O |
| `setCarCurrentPosition` | 완료 | O |
| `setCarPosition` | 추가 논의 필요: 일반 지도에 제공하고 InaviController API에서는 제공하지 않음 | O |
| `setMapPosition` | 완료 | O |
| `zoomIn` | 완료 | O |
| `zoomOut` | 완료 | O |
| `setMapViewMode` | 완료 | O |
| `getMapViewMode` | 완료 | O |
| `visibleTrafficLine` | X | X |
| `createMapOverlay` | X | X |
| `createMapIcon` | X | X |
| `addMapIcon` | 완료 | O |
| `removeMapIcon` | 완료 | O |
| `removeMapIconAll` | 완료 | O |
| `routeZoomMap` | 추가 논의 필요: 일반지도에서만 제공 | O |
| `routeZoomMapWithPadding` | 추가 논의 필요: 일반지도에서만 제공(위와 동일) | O |
| `setMapPadding` | X | 로직 검토 필요 |
| `clearMapPadding` | X | 로직 검토 필요 |
| `drivingRouteZoomMap` | 추가 논의 필요: 당장 제공하지 않는 것으로 정리 | O |
| `setMapLevel` | 완료 | O |
| `setMapFontSizeType` | X | DP 검토 필요 |
| `getMapFontSizeType` | X | DP 검토 필요 |
| `setMapDayNightMode` | 추가 논의 필요: 당장 제공하지 않는 것으로 정리 | O |
| `getMapDayNightMode` | 추가 논의 필요: 당장 제공하지 않는 것으로 정리 | O |
| `setMapEnableRotate` | 완료 | O |
| `setMapMoveChangedListener` | 완료 | O |
| `forceHideMapComponent` | 완료 | O |
| `setTurnViewTaxiIcon` | 추가 논의 필요: 필요 없는 API | O |
| `setMapRouteColor` | 완료 | O |

### 검색

| API | 적용 여부 | 지원 가능 여부 |
|---|---|---|
| `runSearch` | 완료 | O |
| `runRecommendWord` | X | X |
| `getJibunAddr` | X | X |
| `getFullAddr` | X | O |
| `getCurrentRoadName` | X | O |

### 길찾기

| API | 적용 여부 | 지원 가능 여부 |
|---|---|---|
| `runRoute` | 완료 | O |
| `runSingleRoute` | X | O |
| `runReRouteChangeVia` | X | O |
| `makeRouteSumInfo` | X | `OptName` 및 `fee` 검토 필요 |
| `getRoutePtInfo` | X | O |
| `getRoutePtViaInfo` | X | O |
| `getRoutePtRemainViaInfo` | X | 검토 필요(현재 `viaPassed` 관련 처리는 안 하고 있음) |
| `getRouteLinePoints` | X | O |
| `cancelRoute` | 완료 | O |
| `onOptimalRoute` | X | X |

### 주행

| API | 적용 여부 | 지원 가능 여부 |
|---|---|---|
| `runGuidance` | 완료 | O |
| `isSimulation` | X | O |
| `startSimulation` | X | O |
| `finishSimulation` | X | O |
| `getRemainRouteInfo` | X | 요금 데이터는 검토 필요 |
| `getRemainViaRouteInfo` | X | `viaPassed` 처리 검토 필요 |
| `getTotalRemainRouteInfo` | X | 요금 데이터 검토 필요 |
| `setGuidanceSettings` | X | 현재 과속 카메라 안내만 존재 |
| `getGuidanceSettings` | X | 위와 동일 |

### 기타

| API | 적용 여부 | 지원 가능 여부 |
|---|---|---|
| `destroyNavi` | X | O |
| `getNaviSDKVersion` | X | O |
| `setOrientation` | X | O |
| `setNaviVolume` | X | O |
| `getNaviVolume` | X | O |
| `getCurrentPos` | 완료 | O |
| `setNaviEventListener` | X | O |
| `setRouteChangedListener` | X | 검토 필요(현재 `routeID`는 없음) |
| `setDrivingStatusListener` | X | 검토 필요 |
| `setCarSpeedListener` | X | O |
| `setCarType` | X | O |
| `getCarType` | X | O |
| `setTurnViewBackgroundColor` | X | O |
| `getTurnViewBackgroundColor` | X | O |
| `setNextTurnViewBackgroundColor` | X | O |
| `getNextTurnViewBackgroundColor` | X | O |
| `setArrivalViewBackgroundColor` | X | O |
| `getArrivalViewBackgroundColor` | X | O |
| `resetTurnViewsBackgroundColor` | X | O |
| `setVisibleExtendView` | X | O |
| `getVisibleExtendView` | X | O |
| `setDrawBackgroundTBT` | X | O |
| `getDrawBackgroundTBT` | X | O |
| `forceHideBackgroundTBT` | X | O |
| `setBringToFrontListener` | X | O |
| `setLowResolution` | X | O |

### 화물차 옵션

| API | 적용 여부 | 지원 가능 여부 |
|---|---|---|
| `setCarHeight` | X | O |
| `getCarHeight` | X | O |
| `setCarWeight` | X | O |
| `getCarWeight` | X | O |
| `setAvoidUturn` | X | O |
| `getAvoidUturn` | X | O |
| `setAvoidNarrowRoad` | X | O |
| `getAvoidNarrowRoad` | X | O |
| `setAvoidRestriction` | X | O |
| `getAvoidRestriction` | X | O |
| `getNearestVertexIndex` | X | O |
| `getZoneLimit` | X | O |
| `setZoneLimit` | X | O |

## 신규 추가된 함수

| 기능 항목 | API | 설명 |
|---|---|---|
| 초기화 | `applicationInitialize` | Koin 의존성 주입 및 Library 로드 진행 |
| 기타 | `setNaviBottomViewEventListener` | BottomViewEvent 등록 시 자체 제공 동작을 무시하고 3rd Party 앱이 원하는 커스텀 동작으로 대체할 수 있음 |
| 기타 | `removeNaviBottomViewEventListener` | 기존 BottomView 기능을 동작시키기 위해 3rd Party 앱이 등록한 인터페이스를 제거 |

## 요약 집계

- 적용 완료: `loadNaviLibrary`, `initLayout`(MapView Id), `initalizeNavi`, `setMapClickListener`, `setCarCurrentPosition`, `setMapPosition`, `zoomIn`, `zoomOut`, `setMapViewMode`, `getMapViewMode`, `addMapIcon`, `removeMapIcon`, `removeMapIconAll`, `setMapLevel`, `setMapEnableRotate`, `setMapMoveChangedListener`, `forceHideMapComponent`, `setMapRouteColor`, `runSearch`, `runRoute`, `cancelRoute`, `runGuidance`, `getCurrentPos`
- 지원 불가(X): `visibleTrafficLine`, `createMapOverlay`, `createMapIcon`, `runRecommendWord`, `getJibunAddr`, `onOptimalRoute`
- 이 요약은 위 표에서 정리한 것이며 원문에는 없다 ^[inferred]

## Related
- [[navisdk-api-coverage-and-domestic-sdk-guide]] — 국내향 SDK 가이드와 API 범위
- [[orbis-sdk]] — Orbis SDK 프로젝트
- [[orbis-navisdk-architecture-and-flutter-plan]] — 아키텍처
- [[navisdk-confluence-sprint-timeline-2024-2026]] — 스프린트 타임라인
- [[air-internal-docs-and-integration-hub]] — 이 묶음 목차

## Sources
- Confluence "미 구현 항목 현황 - 지속 업데이트" (pageId 973078739) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
