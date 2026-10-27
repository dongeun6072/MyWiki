---
title: >-
    INaviController Reference 1 - 초기화, 지도 컨트롤, 검색
category: references
project: orbis-sdk
tags: [navisdk, android, api-reference, map, visibility/internal]
aliases: [INaviController Reference 초기화, 지도 컨트롤, 검색, loadNaviLibrary, initalizeNavi, runSearch]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[navisdk-api-coverage-and-domestic-sdk-guide]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/305430571
summary: >-
    INaviController 함수 레퍼런스 중 초기화(7), 지도 컨트롤(32), 검색(5) 파트. 시그니처, 파라미터, 반환, 호출 시점과 deprecated 표시 포함.
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

# INaviController Reference 1 - 초기화, 지도 컨트롤, 검색

iNavi SDK Android 가이드의 "INaviController Reference" 중 1. 초기화, 2. 지도 컨트롤, 3. 검색 파트이다. 이어지는 파트는 [[inavi-sdk-android-controller-route-and-driving]](길찾기, 주행), [[inavi-sdk-android-controller-misc-and-truck]](기타, 화물차)이다. 사용 예는 [[inavi-sdk-android-scenario-examples]], 타입 정의는 [[inavi-sdk-android-interface-structure-define-reference]], 허브는 [[inavi-sdk-android-guide-hub]].

`INaviController`는 Singleton이며 초기화 단계 I/F(`loadNaviLibrary`, `initLayout` 등)를 제외한 모든 I/F는 `initalizeNavi` 성공 이후에 호출한다.

## 1. 초기화

### 1.1 loadNaviLibrary
```kotlin
fun loadNaviLibrary()
```
- 설명: SDK에서 사용하는 native lib 로딩
  - Application 초기화 단계에서 호출 필요
  - `initalizeNavi` 호출 전에 호출 필요
- Param: void / Return: void

### 1.2 initLayout (Activity)
```kotlin
fun initLayout(acty: Activity, mapViewID: Int, guideViewID: Int): Boolean
```
- 설명: 지도/주행 뷰 초기화. Root Activity `onCreate`에서 호출 가능, `initalizeNavi` 호출 전에 호출 필요
| 파라미터 | 설명 |
|---|---|
| acty | 지도/주행 뷰를 포함하는 Activity |
| mapViewID | xml에 추가한 지도 리소스 ID |
| guideViewID | xml에 추가한 주행화면 리소스 ID |
- Return: Boolean

### 1.3 initLayout (Fragment 겸용)
```kotlin
fun initLayout(acty: Activity, parentView: View, mapViewID: Int, guideViewID: Int): Boolean
```
- 설명: 지도/주행 뷰 초기화. Root Activity `onCreate` / Fragment `onCreateView`에서 호출 가능, `initalizeNavi` 호출 전에 호출 필요
| 파라미터 | 설명 |
|---|---|
| acty | View(Fragment)를 포함하는 Activity |
| parentView | 지도/주행 뷰의 부모 뷰(Parent View) |
| mapViewID | xml에 추가한 지도 리소스 ID |
| guideViewID | xml에 추가한 주행화면 리소스 ID |
- Return: Boolean

### 1.4 setMapStyle
```kotlin
fun setMapStyle(style: MAPSTYLE)
```
- 설명: 지도 Style 변경. `initalizeNavi` 호출 전에 호출 필요, 미호출 시 Default 지도 사용
- Param: `style` = 지도 style 타입(MAPSTYLE) / Return: void

### 1.5 setAudioStreamType
```kotlin
fun setAudioStreamType(streamType: Int)
```
- 설명: 내비게이션 음성 Stream Type 변경. `initalizeNavi` 호출 전에 호출 필요, 미호출 시 `STREAM_MUSIC` 사용
- Param: `streamType` = 스트림 타입(`AudioManager.STREAM_MUSIC`, `AudioManager.STREAM_NOTIFICATION`) / Return: void

### 1.6 setEmulatorMode
```kotlin
fun setEmulatorMode(emulator: Boolean)
```
- 설명: 타겟 단말 타입 설정. `initalizeNavi` 호출 전에 호출 필요, 미호출 시 "단말기 타입" 사용
- Param: `emulator` = true 에뮬레이터 / false 실제 단말기 / Return: void

### 1.7 initalizeNavi
```kotlin
fun initalizeNavi(context: Context, rootPath: String, uniqueID: String, listener: OnNaviInitListener)
```
- 설명: SDK 엔진 초기화. 초기화 단계 I/F를 제외한 모든 I/F는 `initalizeNavi` 이후에 호출 가능하며, 결과가 성공인 경우에만 SDK가 정상 동작한다.
| 파라미터 | 설명 |
|---|---|
| context | Application Context |
| rootPath | Application 폴더 경로 |
| uniqueID | 유일 식별자(필수값, 20자 이하 Alphanumeric) |
| listener | `OnNaviInitListener { onSuccess(); onFail(errCode: Int, errMsg: String) }` 결과 성공/실패 Callback |
- Return: void
- 실패 코드 후보: 1004/1005(uniqueID 오류), 3xxx(인증/지도/엔진 초기화) 등 → [[inavi-sdk-android-error-codes]]

## 2. 지도 컨트롤

### 2.1 setMapClickListener
```kotlin
fun setMapClickListener(listener: OnMapClickListener)
```
- 설명: 지도 롱 클릭 Listener 등록
- Param: `OnMapClickListener { fun onMapLongClick(lat: Double, lon: Double) }` = 지도 롱 클릭 위치 좌표[WGS84] 반환 Callback / Return: void

### 2.2 setCarCurrentPosition
```kotlin
fun setCarCurrentPosition()
```
- 설명: 지도와 자차를 GPS 위치로 이동. Param/Return: void

### 2.3 setCarPosition
```kotlin
fun setCarPosition(lat: Double, lon: Double, angle: Double)
```
- 설명: 지도와 자차를 특정 위치로 이동
| 파라미터 | 설명 |
|---|---|
| lat | 위도 (이동 시킬 좌표의 y값 [WGS84]) |
| lon | 경도 (이동 시킬 좌표의 x값 [WGS84]) |
| angle | 각도 |
- Return: void

### 2.4 setMapPosition
```kotlin
fun setMapPosition(lat: Double, lon: Double, angle: Double)
```
- 설명: 지도를 특정 위치로 이동 (파라미터는 setCarPosition과 동일: lat, lon [WGS84], angle) / Return: void

### 2.5 zoomIn
```kotlin
fun zoomIn()
```
- 설명: 현재 레벨에서 한 단계 확대 / Param, Return: void

### 2.6 zoomOut
```kotlin
fun zoomOut()
```
- 설명: 현재 레벨에서 한 단계 축소 / Param, Return: void

### 2.7 setMapViewMode
```kotlin
fun setMapViewMode(mode: MAPVIEWMODE)
```
- 설명: 지도 뷰 모드 변경. Param: `mode` = 지도 뷰 모드 / Return: void

### 2.8 getMapViewMode
```kotlin
fun getMapViewMode(): MAPVIEWMODE
```
- 설명: 현재 지도 뷰 모드 반환. Param: void / Return: MAPVIEWMODE

### 2.9 visibleTrafficLine
```kotlin
fun visibleTrafficLine(show: Boolean)
```
- 설명: 지도에 교통정보 라인 표출. Param: `show` = true 표출 / false 미표출 / Return: void

### 2.10 createMapOverlay
```kotlin
fun createMapOverlay(): MapOverlay?
```
- 설명: 지도 아이콘(MapIcon)을 관리하는 Overlay 생성 및 반환. Param: void / Return: MapOverlay

### 2.11 createMapIcon (전체 옵션)
```kotlin
fun createMapIcon(lat: Double, lon: Double, normalResID: Int, selectedResID: Int, gravity: ICONGRAVITY, minLevel: Int, maxLevel: Int, clickable: Boolean): MapIcon?
```
- 설명: 지도 아이콘(MapIcon) 생성 및 반환
| 파라미터 | 설명 |
|---|---|
| lat | 위도 (아이콘을 표출할 좌표 y값 [WGS84]) |
| lon | 경도 (아이콘을 표출할 좌표 x값 [WGS84]) |
| normalResID | 아이콘에 표출할 기본 리소스 ID |
| selectedResID | 아이콘이 선택된 상태일 때 표출할 리소스 ID |
| gravity | 아이콘 표출 위치 (ICONGRAVITY) |
| minLevel | 아이콘이 표출될 최소 지도 레벨 |
| maxLevel | 아이콘이 표출될 최대 지도 레벨 |
| clickable | 클릭 이벤트 동작 여부 |
- Return: MapIcon

### 2.12 createMapIcon (간단)
```kotlin
fun createMapIcon(lat: Double, lon: Double, normalResID: Int, gravity: ICONGRAVITY): MapIcon?
```
- 설명: 지도 아이콘(MapIcon) 생성 및 반환. 파라미터: lat, lon, normalResID, gravity (의미는 2.11과 동일) / Return: MapIcon

### 2.13 addMapIcon
```kotlin
fun addMapIcon(overlay: MapOverlay, mapIcon: MapIcon): MapIcon?
```
- 설명: MapOverlay에 지도 아이콘 추가. Param: `overlay` = 아이콘이 추가될 MapOverlay, `mapIcon` = 추가할 MapIcon / Return: MapOverlay에 정상적으로 추가된 MapIcon

### 2.14 removeMapIcon
```kotlin
fun removeMapIcon(overlay: MapOverlay, mapIcon: MapIcon)
```
- 설명: MapOverlay에서 지도 아이콘 제거. Param: `overlay`, `mapIcon` / Return: void

### 2.15 removeMapIconAll
```kotlin
fun removeMapIconALL(overlay: MapOverlay)
```
- 설명: MapOverlay에 포함된 모든 지도 아이콘 제거. Param: `overlay` / Return: void
- 소제목은 `removeMapIconAll`, 시그니처는 `removeMapIconALL`로 표기가 다르다 ^[ambiguous]

### 2.16 routeZoomMap (deprecated, 2020-01-16)
```kotlin
@deprecated
fun routeZoomMap(rid: String)
```
- 설명: 탐색 경로 비율에 맞게 지도 스케일 조절. `OnRouteMultiListener`/`OnRouteSingleListener` 성공 시에만 호출 가능
- Param: `rid` = 활성화 시킬 경로 ID(`runRoute`/`runSingleRoute`에서 획득) / Return: void

### 2.17 routeZoomMap
```kotlin
fun routeZoomMap(ridList: ArrayList<String>?, selectedRID: String)
```
- 설명: 탐색 경로 비율에 맞게 지도 스케일 조절. `OnRouteMultiListener`/`OnRouteSingleListener` 성공 시에만 호출 가능
- Param: `ridList` = 탐색결과 경로 ID Array, `selectedRID` = 활성화 시킬 경로 ID / Return: void

### 2.18 routeZoomMapWithPadding
```kotlin
fun routeZoomMapWithPadding(ridList: ArrayList<String>?, selectedRID: String, fPaddingRect: android.graphics.RectF)
```
- 설명: 탐색 경로 비율에 Padding 값을 추가로 적용한 지도 스케일 조절. 성공 Listener 이후에만 호출 가능. `fRectPadding`의 left, top, right, bottom 값은 **DP 단위**
- Param: `ridList`, `selectedRID`, `fPaddingRect` = 추가로 적용할 지도의 상하좌우 여백값 / Return: void

### 2.19 setMapPadding
```kotlin
fun setMapPadding(fPaddingRect : android.graphics.RectF)
```
- 설명: 지도에 Padding 값 적용. left, top, right, bottom 값은 DP 단위. **경로안내/모의주행 시 해당 여백값은 초기화**되며 안내 사양에 따른 여백값이 적용된다.
- Param: `fPaddingRect` = 적용할 지도의 상하좌우 여백값 / Return: void

### 2.20 clearMapPadding
```kotlin
fun clearMapPadding()
```
- 설명: 지도에 적용한 Padding 값 초기화. Param, Return: void

### 2.21 drivingRouteZoomMap
```kotlin
fun drivingRouteZoomMap()
```
- 설명: 주행 경로 비율에 맞게 지도 스케일 조절
  - 안내시작 이후에만 호출 가능
  - 약 7초 후 자동 현위치 복귀(사용자 인터랙션 발생 시 7초 Reset)
  - 전체경로보기 중 현위치 I/F 호출 시 바로 현위치 복귀
- Param, Return: void

### 2.22 setMapLevel
```kotlin
fun setMapLevel(level: Int): Boolean
```
- 설명: 지도 레벨 변경. Param: `level` = 변경할 지도 레벨(1 ~ 13)
- Return: 원문에는 "void"로 적혀 있으나 시그니처는 Boolean이다 ^[ambiguous]

### 2.23 setMapFontSizeType
```kotlin
fun setMapFontSizeType(type: MAPFONTSIZETYPE)
```
- 설명: 지도 주기 폰트 사이즈 타입 변경. Param: `type` = 폰트 사이즈 타입 / Return: void

### 2.24 getMapFontSizeType
```kotlin
fun getMapFontSizeType(): MAPFONTSIZETYPE
```
- 설명: 지도 주기 폰트 사이즈 타입 반환. Return: MAPFONTSIZETYPE

### 2.25 setMapDayNightMode
```kotlin
fun setMapDayNigthMode(mode: MAPDAYNIGHTMODE)
```
- 설명: 지도 주/야 타입 변경. Param: `mode` = 지도 주/야 타입 / Return: void
- 소제목은 `setMapDayNightMode`, 시그니처는 `setMapDayNigthMode`(오타 형태)로 적혀 있다 ^[ambiguous]

### 2.26 getMapDayNightMode
```kotlin
fun getMapDayNightMode(): MAPDAYNIGHTMODE
```
- 설명: 지도 주/야 타입 반환. Param: void / Return: MAPDAYNIGHTMODE

### 2.27 setMapEnableRotate
```kotlin
fun setMapEnableRotate(enable: Boolean)
```
- 설명: 지도 회전 가능 여부 설정. Param: `enable` = true 회전 가능 / false 회전 불가 / Return: void

### 2.28 setMapMoveChangedListener
```kotlin
fun setMapMoveChangedListener(listener: OnMapMoveChangedListener)
```
- 설명: 지도 제스처를 통한 지도 이동 이벤트 전달
- Param: `OnMapMoveChangedListener { fun onStart(); fun onStop() }` = 지도 이동 시작/종료 Callback / Return: void

### 2.29 forceHideMapComponent (deprecated, 2020-10-14)
```kotlin
@deprecated
fun forceHideMapComponent()
```
- 설명: 주행 지도 컴포넌트 강제 Hide. Param, Return: void

### 2.30 forceHideMapComponent
```kotlin
fun forceHideMapComponent(componentID: MAPCOMPONENT, hide: Boolean)
```
- 설명: 주행 지도 컴포넌트 강제 Hide
- Param: `componentID` = 지도 컴포넌트 타입(MAPCOMPONENT, 값 목록은 [[inavi-sdk-android-interface-structure-define-reference]]), `hide` = true 미표출 / false 표출 / Return: void

### 2.31 setTurnViewTaxiIcon
```kotlin
fun setTurnViewTaxiIcon(showTaxiIcon: Boolean)
```
- 설명: 주행화면 TBT 아이콘 변경(출발/도착 → 탑승/하차). Param: `showTaxiIcon` = true 탑승/하차 아이콘 / false 출발/도착 아이콘 / Return: void

### 2.32 setMapRouteColor
```kotlin
fun setMapRouteColor(color: MAPROUTECOLOR)
```
- 설명: 주행화면 경로선 색상 변경. Param: `color` = 경로선 색상 타입 / Return: void

## 3. 검색

### 3.1 runSearch
```kotlin
fun runSearch(query: String, lat: Double, lon: Double, listener: OnSearchListener)
```
- 설명: 통합검색 결과 반환
| 파라미터 | 설명 |
|---|---|
| query | 검색어 |
| lat | 위도 (검색에 사용되는 기준 좌표 y) |
| lon | 경도 (검색에 사용되는 기준 좌표 x) |
| listener | `OnSearchListener { onSuccess(result: SearchResult); onFail(errCode: Int, errMsg: String) }` 검색 성공 여부 및 결과 반환 |
- Return: void

### 3.2 runRecommendWord
```kotlin
fun runRecommendWord(query: String, listener: OnRecommendWordListener)
```
- 설명: 추천어 검색
- Param: `query` = 검색어, `listener` = `OnRecommendWordListener { onSuccess(result: ArrayList<RecommendWord>); onFail(errCode: Int, errMsg: String) }` / Return: void

### 3.3 getJibunAddr
```kotlin
fun getJibunAddr(lat: Double, lon: Double): String
```
- 설명: 축약형 지번주소 반환. Param: 위도(Double), 경도(Double) / Return: String 축약형 지번 주소

### 3.4 getFullAddr
```kotlin
fun getFullAddr(lat: Double, lon: Double, roadAddrType: Boolean): String
```
- 설명: 전체 주소 반환. 도로명 주소 요청의 경우 도로명 주소가 없으면 지번주소를 반환한다.
| 파라미터 | 설명 |
|---|---|
| lat | 위도 (주소를 얻어올 위치의 좌표 y [WGS84]) |
| lon | 경도 (주소를 얻어올 위치의 좌표 x [WGS84]) |
| roadAddrType | 주소 타입 (true 도로명 주소 / false 지번 주소) |
- Return: String 전체 주소

### 3.5 getCurrentRoadName
```kotlin
fun getCurrentRoadName(): String
```
- 설명: 현재 위치 도로명 반환. 경로가 존재하고 현재위치(자차)가 경로 위에 존재하는 경우에만 도로명을 반환한다.
- Param: void / Return: String 도로명

## Related
- [[inavi-sdk-android-guide-hub]] — 이 가이드 묶음 목차
- [[inavi-sdk-android-controller-route-and-driving]] — 다음 파트(길찾기, 주행)
- [[navisdk-api-coverage-and-domestic-sdk-guide]] — 국내 SDK 가이드 개요
- [[orbis-sdk]] — SDK 프로젝트 허브

## Sources
- Confluence "iNavi SDK Android 개발 가이드" (pageId 305430571) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
