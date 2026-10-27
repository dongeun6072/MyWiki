---
title: >-
    iNavi SDK Android 개발 가이드 - 개정이력
category: references
project: orbis-sdk
tags: [navisdk, android, changelog, domestic-sdk, visibility/internal]
aliases: [iNavi SDK Android 개발 가이드, 개정이력, 아이나비 내비게이션 SDK 변경 이력]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[navisdk-api-coverage-and-domestic-sdk-guide]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/305430571
summary: >-
    국내향 iNavi SDK(Android) 공식 가이드의 개정이력 전체. 0.0.1(2020-01)부터 0.6.2(2023-10)까지 버전별 변경, 필수 적용 항목 표시 포함.
provenance:
  extracted: 0.92
  inferred: 0.05
  ambiguous: 0.03
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T13:00:00+09:00
updated: 2026-10-26T13:00:00+09:00
---

# iNavi SDK Android 개발 가이드 - 개정이력

국내향 "아이나비 내비게이션 SDK"(Android) 개발 가이드 원본의 개정이력을 버전 순서대로 모두 옮긴 문서이다. 2020-01-17(0.0.1)부터 2023-10-17(0.6.2)까지 기록되어 있다. 허브: [[inavi-sdk-android-guide-hub]]. SDK 전반은 [[navisdk-api-coverage-and-domestic-sdk-guide]], [[orbis-sdk]] 참고. 삼성중공업(SHI)용 사본은 별도 버전 체계(0.0.1~1.0.8)를 쓰며 [[inavi-sdk-android-shi-edition-diff]]에 정리했다.

원문에서 굵게 "필수 적용 항목"으로 표시된 변경은 아래에서 **[필수]** 로 표시한다.

## 2020년

### 0.0.1 (2020-01-17)
- 인증 업데이트 추가

### 0.0.2 (2020-01-29)
- SDK 적용방법 추가

### 0.0.3 (2020-02-20)
- `setDrivingStatusListener` I/F에 `nearGoalDist` 파라미터 추가

### 0.0.4 (2020-03-23)
- 주행중 특정지점에서 비정상 종료되는 이슈 수정

### 0.0.5 (2020-03-30)
- Proguard 옵션 추가

### 0.0.6 (2020-04-01)
- SDK 난독화 예외처리 추가 (통신 관련)
- App 난독화 가이드 추가

### 0.0.7 (2020-04-07)
- 길 찾기 I/F 파라미터 변경 (`runRoute`, `runSingleRoute`)
  - `RouteExtraInfo` 추가
  - `RoutePtItem`에 `angle` 필드 추가

### 0.0.8 (2020-04-23)
- 과속 백그라운드 알림 추가

### 0.0.9 (2020-05-20)
- 차량 속도 Callback 추가 (`setCarSpeedListener`)

### 0.0.10 (2020-05-28)
- 디버그 로그 제거
- 주행화면 TBT UI 개선 (차기/차차기 높이 및 간격 조정)

### 0.0.11 (2020-06-08)
- 내부 안정성 이슈 개선
- `NaviLocation`에 속도 필드 추가

### 0.0.12 (2020-07-30)
- 주행화면 GUI 개선 (회전정보, 카메라정보, 현위치 버튼 등)
- 길 찾기 실패 코드 추가 (코드표: 5002, 5003, 5004) → [[inavi-sdk-android-error-codes]]

### 0.0.13 (2020-11-02)
- 기본 자차 아이콘 및 폰트 변경
- 주행화면 TBT UI 개선 (형태 및 컬러 변경)
- 주행화면 TBT 출발/도착 아이콘 변경 I/F 추가 (`setTurnViewTaxiIcon`)
- 지도 컴포넌트 Show/Hide I/F 수정 (`forceHideMapComponent`)
- 도로명 주소 I/F 추가 (`getFullAddr`)
- 현재 도로명 I/F 추가 (`getCurrentRoadName`)
- 경유지 정보 I/F 추가 (`getRoutePtViaInfo`)
- 주행정보 요금 필드 추가 (`getRemainRouteInfo`): `RouteRemainInfo`에 `remainFee` 필드 추가
- NaviEvent Callback 추가 (`setNaviEventListener`): 현위치 이동, 전체경로 보기

### 0.0.14 (2020-11-05)
- 주행 속도 레이아웃 오류 개선

### 0.0.15 (2020-11-25)
- Audio Stream Type 변경 I/F 추가 (`setAudioStreamType`)

### 0.0.16 (2020-12-04)
- 지도 Style 변경 I/F 추가 (`setMapStyle`)
- 도착예정시간 초기화 및 갱신 타이밍 개선

### 0.0.17 (2020-12-16)
- 총 주행정보 I/F 추가 (`getTotalRemainRouteInfo`)
- `getRemainRouteInfo`의 Distance 갱신 로직 개선
- `forceHideMapComponent` 지도 컴포넌트 타입 추가: `MAPCOMPONENT.ROUTE_TRAFFIC_STATUS_BAR`

## 2021년

### 0.0.18 (2021-02-05)
- Layout 초기화 I/F 추가 (`initLayout`)
- 기존 `initLayout` I/F에, 지도/주행의 부모 뷰 추가 (Fragment용 오버로드)

### 0.0.19 (2021-02-09)
- SurfaceView Activity Casting 오류 개선

### 0.0.20 (2021-03-03)
- **[필수] SDK 저장소 변경**: Bintray에서 Artifactory로 변경
- **[필수] NaviLocation 자료형 변형**: `angle` 필드 자료형을 Double로 변경 (0.0.19까지는 Int)
- 화면회전 세팅 I/F 수정 (`setOrientation`): `ORIENTATION_UNDEFINED` 추가

### 0.0.21 (2021-03-17)
- 내부적으로 사용하던 TimeZone 제거

### 0.0.22 (2021-04-21)
- **[필수] minSdkVersion 19에서 21로 변경**
- 경유지 기능 추가
  - 기존 길찾기 I/F에 경유지 Param 추가: `runRoute`, `runSingleRoute`
  - 남은 경유지 정보 I/F 추가: `getRoutePtRemainViaInfo`, `getRemainViaRouteInfo`
  - 경유지 변경 재탐색 I/F 추가: `runReRouteChangeVia`
- 에뮬레이터 지원: 에뮬레이터 모드 I/F 추가 (`setEmulatorMode`)

### 0.0.23 (2021-08-06)
- 안내종료거리 튜닝
- 길찾기 I/F에 탐색옵션 Param 추가: `runRoute`
- 안전운행정보 변경 기능 추가
  - 안내설정 I/F 추가 (`setGuidanceSettings`, `getGuidanceSettings`)
  - `GUIDANCESETTING` 추가

### 0.0.24 (2021-11-29)
- 안내종료거리 2차 튜닝
- 내부 모듈 안정성 개선
- 주행 경로선 색상 변경 기능 추가
  - 경로선 색상 변경 I/F 추가 (`setMapRouteColor`)
  - `MAPROUTECOLOR` 추가

### 0.0.25 (2021-12-22)
- 내부 모듈 안정성 개선
- 주행중 전체 경로보기 기능 추가: 전체 경로보기 I/F 추가 (`drivingRouteZoomMap`)

## 2022년

### 0.0.26 (2022-03-31)
- 목적지 도착시 요금 반환 기능 추가
  - 목적지 도착시 요금 반환 I/F 추가: `onArrivalFee` (`OnDrivingStatusListener`)
  - `setDrivingStatusListener` 설명 추가: `onArrivalFee` 사양 설명 추가

### 0.0.27 (2022-11-11)
- 경유지 사양 확대 (최대 100개까지 설정 가능)
- `forceHideMapComponent` 지도 컴포넌트 타입 추가
  - `MAPCOMPONENT.BOTTOM_NORMAL_SIDE_BUTTON`
  - `MAPCOMPONENT.BOTTOM_DRIVING_SIDE_BUTTON`
  - `MAPCOMPONENT.BOTTOM_ARRIVAL_LEFT_BUTTON`
- 화물차 설정 및 전용 탐색 옵션 추가
  - 차량 높이/중량/U-turn 도로폭/좁은길 도로폭/통행제한구간 회피 설정 옵션 추가
    - `setCarHeight`, `getCarHeight`
    - `setCarWeight`, `getCarWeight`
    - `setAvoidUturn`, `getAvoidUturn`
    - `setAvoidNarrowRoad`, `getAvoidNarrowRoad`
    - `setAvoidRestriction`, `getAvoidRestriction`
  - 화물차 전용 탐색 옵션 추가: **`ROUTEOPTIONTYPE` 수정** (TRUCK 계열 추가, [[inavi-sdk-android-interface-structure-define-reference]])

## 2023년

### 0.0.28 (2023-01-10)
- 지도 여백(Padding) 설정 I/F 추가: `routeZoomMapWithPadding`, `setMapPadding`, `clearMapPadding`
- 차종 설정 I/F 추가: `setCarType`, `getCarType`
- `enum class CARTYPE` 추가

### 0.0.29 (2023-01-20)
- 경유지 도착 알림 I/F 추가
  - **[필수]** `OnDrivingStatusListener` 수정 (`onArrivalVia` 추가) - 인터페이스 구현체는 반드시 이 메서드를 구현해야 컴파일됨 ^[inferred]
- TBT(TurnView) Custom Background Color 설정 I/F 추가
  - `setTurnViewBackgroundColor`, `getTurnViewBackgroundColor` (차기 TurnView)
  - `setNextTurnViewBackgroundColor`, `getNextTurnViewBackgroundColor` (차차기)
  - `setArrivalViewBackgroundColor`, `getArrivalViewBackgroundColor` (목적지 도착 view)
  - `resetTurnViewsBackgroundColor` (기본값으로 초기화)
- 확대도 표출 기능 및 표출 여부 I/F 추가: `setVisibleExtendView`, `getVisibleExtendView`

### 0.5.0 (2023-03-22)
- 내부 모듈 안정성 개선

### 0.5.1 (2023-05-04)
- 경유지 도착 알림 I/F 사양 변경
- 탐색열에서 진행방향으로 현 위치에서 가장 가까운 좌표 인덱스 반환 I/F 추가: `getNearestVertexIndex`

### 0.5.2 (2023-05-15)
- 내부 모듈 안정성 개선

### 0.6.0 (2023-08-31)
- 내부 엔진 수정
- AndroidX 적용
  - `playground-service-location` 버전 16.0.0 → 21.0.1 로 수정 (fusedLocationProvider 관련 내용 적용)
  - 이에 따라 `gradle.properties`의 `android.useAndroidX=true`가 0.6.0부터 필수 ([[inavi-sdk-android-setup-and-permissions]])

### 0.6.1 (2023-09-05)
- 경로탐색 실패 처리 사양 변경: 경유지가 포함된 경우 출발지-목적지 간 거리 체크를 하지 않도록 변경

### 0.6.2 (2023-10-17)
- **[필수] SDK 저장소 URL 변경** (SDK 버전과 무관하게 새 URL 적용 필요)
- 화물차 전용옵션 로직 개선

## 요약: 필수 적용 항목 한눈에 보기

| 버전 | 날짜 | 필수 적용 내용 |
|---|---|---|
| 0.0.20 | 2021-03-03 | 저장소 Bintray → Artifactory |
| 0.0.20 | 2021-03-03 | `NaviLocation.angle` Int → Double |
| 0.0.22 | 2021-04-21 | minSdkVersion 19 → 21 |
| 0.0.29 | 2023-01-20 | `OnDrivingStatusListener.onArrivalVia` 추가 |
| 0.6.0 | 2023-08-31 | AndroidX 필수, play-services-location 21.0.1 |
| 0.6.2 | 2023-10-17 | SDK 저장소 URL 변경 |

## 기능별 도입 버전 색인

| 기능 | 도입 버전 |
|---|---|
| 차량 속도 Callback | 0.0.9 |
| 도로명 주소/현재 도로명/경유지 정보 조회 | 0.0.13 |
| 지도 Style 변경 | 0.0.16 |
| 총 주행정보 | 0.0.17 |
| 경유지(최대 100개로 확대는 0.0.27), 에뮬레이터 모드 | 0.0.22 |
| 안전운행정보 안내 설정 | 0.0.23 |
| 경로선 색상 변경 | 0.0.24 |
| 주행중 전체 경로보기 | 0.0.25 |
| 목적지 도착 요금 | 0.0.26 |
| 화물차 옵션 | 0.0.27 |
| 지도 여백, 차종 | 0.0.28 |
| 경유지 도착 알림, TurnView 배경색, 확대도 | 0.0.29 |
| 가장 가까운 좌표 인덱스 | 0.5.1 |

## Related
- [[inavi-sdk-android-guide-hub]] — 이 가이드 묶음 목차
- [[navisdk-api-coverage-and-domestic-sdk-guide]] — 국내 SDK 가이드 개요
- [[orbis-sdk]] — SDK 프로젝트 허브
- [[orbis-navisdk-architecture-and-flutter-plan]] — SDK 구조와 Flutter 계획

## Sources
- Confluence "iNavi SDK Android 개발 가이드" (pageId 305430571) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
