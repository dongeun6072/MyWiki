---
title: >-
    INaviController Reference 3 - 기타, 화물차 옵션
category: references
project: orbis-sdk
tags: [navisdk, android, api-reference, truck, visibility/internal]
aliases: [INaviController Reference 기타, 화물차 옵션, setCarType, setCarHeight, getNearestVertexIndex]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[navisdk-api-coverage-and-domestic-sdk-guide]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/305430571
summary: >-
    INaviController 함수 레퍼런스 중 기타(24: 종료, 버전, 볼륨, 리스너, 차종, TurnView 색, 확대도)와 화물차 옵션(11) 파트.
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

# INaviController Reference 3 - 기타, 화물차 옵션

iNavi SDK Android 가이드 "INaviController Reference" 중 6. 기타, 7. 화물차 옵션 파트이다. 앞 파트는 [[inavi-sdk-android-controller-route-and-driving]], 처음 파트는 [[inavi-sdk-android-controller-init-map-search]]. 사용 예는 [[inavi-sdk-android-scenario-examples]]의 7~12번, 허브는 [[inavi-sdk-android-guide-hub]]. 화물차 경로 제약 데이터는 [[vehicle-restriction-routing]]을 참고한다.

## 6. 기타

### 6.1 destroyNavi
```kotlin
fun destroyNavi()
```
- 설명: SDK 메모리 해제 및 종료. App 종료 시 호출 필요. Param, Return: void

### 6.2 getNaviVersionName (deprecated, 2020-01-20)
```kotlin
fun getNaviVersionName(): String
```
- 설명: SDK 버전네임 반환. Return: String SDK 버전네임(예 "01.00.00")

### 6.3 getNaviVersionCode (deprecated, 2020-01-20)
```kotlin
fun getNaviVersionCode(): Int
```
- 설명: SDK 버전코드 반환. Return: Int SDK 버전코드

### 6.4 getNaviSDKVersion
```kotlin
fun getNaviSDKVersion(): String
```
- 설명: SDK 버전 반환. Return: String SDK 버전

### 6.5 setApplicationStatus
```kotlin
fun setApplicationStatus(status: APPSTATUS)
```
- 설명: Application 상태 세팅. Param: `status` = App 상태(BACKGROUND / SCREEN_OFF_BACKGROUND / FOREGROUND). Return: void

### 6.6 setOrientation
```kotlin
fun setOrientation(orientation: Int)
```
- 설명: 화면 가로/세로 상태 세팅
| 값 | 의미 |
|---|---|
| 0 | `Configuration.ORIENTATION_UNDEFINED` (단말의 회전 상태 사용, Default) |
| 1 | `Configuration.ORIENTATION_PORTRAIT` (세로 상태 고정) |
| 2 | `Configuration.ORIENTATION_LANDSCAPE` (가로 상태 고정) |
- Return: void

### 6.7 setNaviVolume
```kotlin
fun setNaviVolume(vol: Float)
```
- 설명: 내비게이션 볼륨 세팅. 단말기의 미디어 볼륨과는 별개로 내비게이션에서만 사용하는 음성. Param: `vol` = 0.0 ~ 1.0 / Return: void

### 6.8 getNaviVolume
```kotlin
fun getNaviVolume(): Float
```
- 설명: 내비게이션 볼륨 반환(미디어 볼륨과 별개). Return: Float 0.0 ~ 1.0

### 6.9 getCurrentPos
```kotlin
fun getCurrenPos(): NaviLocation
```
- 설명: 현재 위치 반환. Return: NaviLocation
- 소제목은 `getCurrentPos`, 시그니처는 `getCurrenPos`로 표기가 다르다 ^[ambiguous]

### 6.10 setNaviEventListener
```kotlin
fun setNaviEventListener(listener: OnNaviEventListener)
```
- 설명: 내비게이션 버튼 이벤트 Callback. Param: `OnNaviEventListener { fun onEvent(e: NaviEvent) }` = 버튼 이벤트 전달 / Return: void

### 6.11 setRouteChangedListener
```kotlin
fun setRouteChangedListener(listener: OnRouteChangedListener)
```
- 설명: 주행 재탐색 성공 이벤트 Callback. Param: `OnRouteChangedListener { fun onChanged(routeID: String) }` = 새로운 경로 RouteID 전달 / Return: void

### 6.12 setDrivingStatusListener
```kotlin
fun setDrivingStatusListener(listener: OnDrivingStatusListener, nearGoalDist: Int)
```
- 설명: 주행 시작/도착 이벤트 및 목적지 도착 시 요금 정보 Callback
  - 목적지 도착 시 요금은 도착이벤트 발생 시에만 호출된다.
  - 목적지 도착 시 요금은 실 주행에서만 계산된다(모의주행 시 무조건 0원).
  - 경유지 도착 알림 인덱스는 0부터 시작하며 안내 시작 시 전달된 경유지 리스트의 순서와 동일하다.
  - 만약 0번째 경유지 → 2번째 → 1번째 순서로 주행한다면 `onArrivalVia` 이벤트도 0 → 2 → 1 순으로 전달된다.
  - 한 번 지나간 경유지에 대해서는 다시 `onArrivalVia`가 호출되지 않는다.
| 파라미터 | 설명 |
|---|---|
| listener | `OnDrivingStatusListener { onStatus(status: DRIVINGSTATUS); onArrivalFee(fee: Int); onArrivalVia(nIndex: Int) }` 주행 시작/종료 이벤트, 도착 후 통행요금, 경유지 도착 정보 전달 |
| nearGoalDist | NEARGOAL STATUS 체크 거리(단위 m, Default 100m) |
- Return: void

### 6.13 setCarSpeedListener
```kotlin
fun setCarSpeedListener(listener: OnCarSpeedListener)
```
- 설명: 차량 속도 Callback. Param: `OnCarSpeedListener { fun onSpeed(speed: Int) }` = 차량 속도 전달 / Return: void

### 6.14 setCarType
```kotlin
fun setCarType(nCarType : CARTYPE)
```
- 설명: 차종 설정(요금 및 경로 안내 시 반영). 차종 설명은 CARTYPE 참조. Param: `nCarType` = 차종 / Return: void

### 6.15 getCarType
```kotlin
fun getCarType() : CARTYPE
```
- 설명: 현재 설정된 차종 반환. Return: CARTYPE

### 6.16 setTurnViewBackgroundColor
```kotlin
fun setTurnViewBackgroundColor(strColor : String) : Boolean
```
- 설명: 차기 turnview 배경색 변경. 사용 가능한 색상명은 시나리오 10번 참고(23개)
- Param: `strColor` = 16진수 컬러값 또는 색상명(`#RRGGBB`, `#AARRGGBB`, "red", "black" ..). 예 "#f21e55f7", "#1e55f7", "red", "black"
- Return: 배경색 적용 여부(Boolean)

### 6.17 getTurnViewBackgroundColor
```kotlin
fun getTurnViewBackgroundColor() : String
```
- 설명: 현재 적용된 차기 turnview 색 문자열 얻기. Return: 배경색 문자열(예 "#f21e55f7", "#1e55f7", "red", "black")

### 6.18 setNextTurnViewBackgroundColor
```kotlin
fun setNextTurnViewBackgroundColor(strColor : String) : Boolean
```
- 설명: 차차기 turnview 배경색 변경. Param/Return은 6.16과 동일

### 6.19 getNextTurnViewBackgroundColor
```kotlin
fun getNextTurnViewBackgroundColor() : String
```
- 설명: 현재 적용된 차차기 turnview 색 문자열 얻기. Return: 배경색 문자열

### 6.20 setArrivalViewBackgroundColor
```kotlin
fun setArrivalViewBackgroundColor(strColor : String) : Boolean
```
- 설명: 목적지 도착 view 배경색 변경. Param/Return은 6.16과 동일

### 6.21 getArrivalViewBackgroundColor
```kotlin
fun getArrivalViewBackgroundColor() : String
```
- 설명: 목적지 도착 view 배경색 string 얻기. Return: 배경색 문자열

### 6.22 resetTurnViewsBackgroundColor
```kotlin
fun resetTurnViewsBackgroundColor()
```
- 설명: 차기, 차차기, 목적지 도착 view 배경색을 아래 기본값으로 초기화
| 항목 | 기본값 |
|---|---|
| TURN (차기) | `#f21e55f7` |
| NEXT_TURN (차차기) | `#f2122672` |
| ARRIVAL (목적지 도착) | `#f21e55f7` |
- Param, Return: void

### 6.23 setVisibleExtendView
```kotlin
fun setVisibleExtendView(bIsShow : Boolean)
```
- 설명: 확대도 표출 여부 설정. **확대도는 모의주행/안내시작 후 표출**된다. Param: `bIsShow` = true 표출 / false 표출 안 함(Default) / Return: void

### 6.24 getVisibleExtendView
```kotlin
fun getVisibleExtendView() : Boolean
```
- 설명: 적용된 확대도 표출 여부. Return: 표출 여부

## 7. 화물차 옵션

공통: 설정 값은 재실행 시에도 유지되며 앱 삭제 시 초기화된다. 회피옵션이어도 해당 경로가 유일하면 제한구역을 포함해 안내될 수 있고, 각 설정은 별개 사양으로 동작한다([[inavi-sdk-android-scenario-examples]] 7번).

| 함수 | 범위/Default | 설명 |
|---|---|---|
| `setCarHeight(nHeight: Int): Boolean` | 0 ~ 1000 cm [10m] | 차량 높이 설정, 설정 시 높이제한구역 회피안내. Return 적용 성공 여부 |
| `getCarHeight(): Int` | default 0 | 현재 설정된 차량 높이(cm) |
| `setCarWeight(nWeight: Int): Boolean` | 0 ~ 60000 kg [60t] | 차량 중량 설정, 설정 시 중량제한구역 회피안내. Return 적용 성공 여부 |
| `getCarWeight(): Int` | default 0 | 현재 설정된 차량 중량(kg) |
| `setAvoidUturn(nAvoidUturn: Int): Boolean` | 차선 수, default 0 | 왕복 n차선 이하 유턴 회피 설정. Return 적용 성공 여부 |
| `getAvoidUturn(): Int` | default 0 | 현재 설정된 유턴회피 차선 |
| `setAvoidNarrowRoad(nAvoidNarrowRoad: Int): Boolean` | 차선 수, default 0 | 왕복 n차선 이하 도로 회피여부 설정. Return 적용 성공 여부 |
| `getAvoidNarrowRoad(): Int` | default 0 | 현재 설정된 n차선 이하 도로 회피 차선 |
| `setAvoidRestriction(bIsAvoidRestriction: Boolean)` | default false | 화물차 통행제한구간 회피여부 설정(true 구간 회피 / false 회피 안 함). Return void |
| `getAvoidRestriction(): Boolean` | default false | 현재 설정된 통행제한구간 회피 여부 |
| `getNearestVertexIndex(): Int` | 미설정 시 -1 | 현위치에서 진행방향으로 탐색 좌표리스트 내 가장 가까운 좌표 인덱스 반환 |

- 각 함수의 Param은 위 표의 인자 1개(set 계열) 또는 void(get 계열)이다.
- `getNearestVertexIndex`는 원문 레퍼런스에서 화물차 옵션 번호(7.11)로 묶여 있으나 화물차와 무관한 경로 좌표 조회 함수이다. 엔진 초기화 전이거나 경로가 없으면 -1을 반환하며, 현재 선택한 경로의 RouteID와 `getRouteLinePoints`로 얻은 좌표열이 필요하다.
- 전용 탐색 옵션(TRUCK 계열)은 `ROUTEOPTIONTYPE` enum 참조([[inavi-sdk-android-interface-structure-define-reference]]).

## Related
- [[inavi-sdk-android-guide-hub]] — 이 가이드 묶음 목차
- [[inavi-sdk-android-controller-route-and-driving]] — 길찾기/주행 파트
- [[vehicle-restriction-routing]] — 화물차 제한 경로 데이터 배경
- [[orbis-sdk]] — SDK 프로젝트 허브

## Sources
- Confluence "iNavi SDK Android 개발 가이드" (pageId 305430571) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
