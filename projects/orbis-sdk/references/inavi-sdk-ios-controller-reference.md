---
title: >-
    iNavi SDK iOS INaviController Reference (함수 전체)
category: references
project: orbis-sdk
tags: [ios, sdk, api-reference, inavicontroller, visibility/internal]
aliases: [INaviController Reference, iNavi SDK iOS 개발 가이드 INaviController]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[navisdk-api-coverage-and-domestic-sdk-guide]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/305201307
summary: >-
    iOS SDK의 INaviController 싱글턴이 제공하는 초기화, 지도 컨트롤, 통합 검색, 길 찾기, 주행, 기타 영역의 모든 함수/프로퍼티/Delegate의 시그니처, 파라미터, 반환, 설명.
provenance:
  extracted: 0.93
  inferred: 0.04
  ambiguous: 0.03
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T13:00:00+09:00
updated: 2026-10-26T13:00:00+09:00
---

# iNavi SDK iOS INaviController Reference (함수 전체)

iOS SDK의 모든 기능은 `INaviController` 싱글턴(`INaviController.sharedInstance()`)으로 호출한다. 이 페이지는 원본 가이드의 "INaviController Reference" 6개 영역(초기화, 지도 컨트롤, 통합 검색, 길 찾기, 주행, 기타)을 빠짐없이 옮긴 것이다. 설치와 권한은 [[inavi-sdk-ios-guide-setup]], 타입 정의는 [[inavi-sdk-ios-structures-defines-and-codes]], 사용 예는 [[inavi-sdk-ios-swift-scenarios]]. 국내 SDK API 전반은 [[navisdk-api-coverage-and-domestic-sdk-guide]]를 본다. (목차: [[inavi-sdk-ios-guide-hub]])

표기: 원본은 각 함수를 `Description / Param / Return` 형식으로 적었다. 함수명 철자(`initalizeNavi`, `createMapIcon(withPostion:...)`, `nomalImage` 등)는 원본 그대로이며 오타로 보이지만 실제 SDK 심볼일 수 있어 바꾸지 않았다. ^[ambiguous]

## 1. 초기화

### initalizeNavi

```swift
func initalizeNavi(_ uniqueID: String, target: INaviControllerDelegate)
```

- Description: SDK 엔진 초기화. 초기화 결과가 성공인 경우에만 SDK가 정상 동작한다.
- Param
  - `uniqueID`: 유일 식별자 (필수값, 20자 이하 Alphanumeric)
  - `target`: `INaviControllerDelegate` Protocol, 초기화 성공 여부 Callback (실패 코드는 코드 표 참고)
- Return: void
- 초기화 결과는 Delegate의 `authResultCode(_:message:)`로 전달된다(시나리오 예시 참고). 0이면 인증 성공.

## 2. 지도 컨트롤

### didLongTap

```swift
func didLongTap(_ mapView: INaviMapView, position: INaviPosition?)
```

- Description: `INaviControllerDelegate` Protocol. 지도 롱클릭 이벤트 호출
- Param: `mapView` = `iNaviMapView` 객체, `position` = 롱 탭한 위경도 좌표
- Return: void

### setCarCurrentPosition

```swift
func setCarCurrentPosition()
```

- Description: 지도를 GPS 위치로 이동
- Param: void / Return: void

### setCarPosition

```swift
func setCarPosition(_ position: INaviPosition)
```

- Description: 지도와 자차를 특정 위치로 이동
- Param: `position` = `INaviPosition` 객체 / Return: void

### setMapPosition

```swift
func setMapPosition(_ position: INaviPosition)
```

- Description: 지도를 특정 위치로 이동
- Param: `position` = `INaviPosition` 객체 / Return: void

### zoomIn

```swift
func zoomIn()
```

- Description: 지도 현재 레벨 기준으로 한 단계 확대
- Param: void / Return: void

### zoomOut

```swift
func zoomOut()
```

- Description: 지도 현재 레벨 기준으로 한 단계 축소
- Param: void / Return: void

### mapViewMode

```swift
var mapViewMode: INVMapViewMode
```

- Description: 지도 뷰 모드 반환/변경
- Value: `INVMapViewMode` 지도 뷰 모드 (Define Reference 참고)

### visibleTrafficLine

```swift
func visibleTrafficLine(_ show: Bool)
```

- Description: 지도에 교통정보 라인 표출
- Param: `show` = true 표출, false 미표출 / Return: void

### INaviMapOverlay

```swift
class func create() -> INaviMapOverlay
```

- Description: 지도 아이콘을 관리하는 overlay 생성 및 반환
- Param: void / Return: `INaviMapOverlay`

### INaviMapIcon

```swift
class func createMapIcon(withPostion position: INaviPosition, nomalImage:
INaviImage, selectedImage: INaviImage, anchor: INVIconAnchor, minLevel: Int,
maxLevel: Int, clickable: Bool) -> INaviMapIcon
```

- Description: 지도 아이콘 생성 및 반환
- Param
  - `position`: `INaviPosition` 객체
  - `nomalImage`: 아이콘에 표출할 기본 `INaviImage` 이미지
  - `anchor`: 아이콘 표출 위치 (Define Reference 참고)
  - `minLevel`: 아이콘이 표출되는 최소 지도 레벨
  - `maxLevel`: 아이콘이 표출되는 최대 지도 레벨
  - `clickable`: 클릭 이벤트 동작 여부
  - (원본 Param 설명에는 시그니처의 `selectedImage`에 대한 항목이 빠져 있다.) ^[ambiguous]
- Return: `INaviMapIcon`

```swift
class func createMapIcon(withPostion position: INaviPosition, nomalImage:
INaviImage, anchor: INVIconAnchor)
```

- Description: 지도 아이콘 생성 및 반환 (간단 오버로드)
- Param: `position` = `INaviPosition` 객체, `nomalImage` = 기본 `INaviImage` 이미지, `anchor` = 아이콘 표출 위치
- Return: `INaviMapIcon`

### addMapIcon

```swift
func addMapIcon(with mapOverlay: INaviMapOverlay, mapIcon: INaviMapIcon)
```

- Description: overlay에 지도 아이콘 추가
- Param: `mapOverlay` = 지도 아이콘이 포함된 overlay, `mapIcon` = 추가할 지도 아이콘 / Return: void

### removeMapIcon

```swift
func removeMapIcon(with mapOverlay: INaviMapOverlay, mapIcon: INaviMapIcon)
```

- Description: overlay에서 지도 아이콘 제거
- Param: `mapOverlay`, `mapIcon` = 제거할 지도 아이콘 / Return: void

### removeMapIconAll

```swift
func removeMapIconAll(with mapOverlay: INaviMapOverlay)
```

- Description: overlay에 포함된 모든 지도 아이콘 제거
- Param: `mapOverlay` / Return: void

### routeZoomMap

```swift
func routeZoomMap(withRouteIdList ridList: [String], selectedRID: String)
```

- Description: 탐색 경로 비율에 맞게 지도 스케일 조절
- Param: `ridList` = 탐색 결과 경로 ID Array (`runRoute()`, `runSingleRoute()` I/F에서 획득), `selectedRID` = 활성화할 경로 ID
- Return: void

### mapLevel

```swift
var mapLevel: Int
```

- Description: 지도 레벨 반환/변경
- Value: 변경할 지도 레벨 (유효 범위 1 ~ 13)

### mapFontType

```swift
var mapFontType: INVMapFontType
```

- Description: 지도 주기 폰트 사이즈 타입 반환/변경
- Value: `INVMapFontType` 폰트 사이즈 타입 (Define Reference 참고)

### mapDayNightMode

```swift
var mapDayNightMode: INVMapDayNightMode
```

- Description: 지도 주/야 타입 반환/변경
- Value: `INVMapDayNightMode` 주/야 타입 (Define Reference 참고)

### setMapEnableRotate

```swift
func setMapEnableRotate(_ enable: Bool)
```

- Description: 지도 회전 설정
- Param: `enable` = true 회전 가능, false 회전 불가 / Return: void

### mapMoveMode

```swift
func mapView(_ mapView: INaviMapView, didChanged mapMoveMode: INVMapMoveMode)
```

- Description: 지도 제스처를 통한 지도 이동 Callback
- Param: `mapMoveMode` = 지도 이동 시작/종료 / Return: void
- `INVMapMoveMode`의 정의는 원본 Define Reference에 없다. ^[ambiguous]

### forceHideMapComponent

```swift
fun forceHideMapComponent(componentID: MAPCOMPONENT, hide: Boolean)
```

- Description: 지도 컴포넌트 강제 Hide
- Param: `INVMapComponent` = 지도 컴포넌트 타입 (Define Reference 참고), `Boolean` = true 컴포넌트 미표출, false 컴포넌트 표출
- Return: void
- 원본 시그니처가 Swift가 아니라 Kotlin 형태(`fun`, `Boolean`, `MAPCOMPONENT`)로 적혀 있어 Android 가이드를 복사한 흔적으로 보인다. Swift에서는 `INVMapComponent` 타입을 쓰는 것으로 추정된다. ^[inferred]

## 3. 통합 검색

### runSearch

```swift
func runSearch(_ query: String, lat: Double, lng: Double, successHandler:
@escaping INaviSearchSuccessHandler, failHandler: @escaping INaviFailHandler)
```

- Description: 통합검색 결과 반환
- Param: `query` = 검색어, `lat` = 위도(검색 시 기준 좌표), `lng` = 경도(검색 시 기준 좌표), `successHandler` = 검색 성공 Handler, `failHandler` = 검색 실패 Handler (Structure Reference, 코드 표 참고)
- Return: void

### runRecommendWord

```swift
func runRecommendWord(_ query: String, successHandler: @escaping
INaviRecommendSearchSuccessHandler, failHandler: @escaping INaviFailHandler)
```

- Description: 검색 추천어 반환
- Param: `query` = 검색어, `successHandler` = 추천어 검색 성공 Handler, `failHandler` = 추천어 검색 실패 Handler
- Return: void

### getJibunAddr

```swift
func getJibunAddr(_ position: INaviPosition) -> String?
```

- Description: 축약형 지번 주소 검색
- Param: `position` = `INaviPosition` 객체
- Return: String, 축약형 지번 주소

## 4. 길 찾기

### runRoute

```swift
func runRoute(_ startItem: INaviRoutePtItem?, goalItem: INaviRoutePtItem,
viaList:[INaviRoutePtItem]? , successHandler: @escaping
INaviRouteMultiSuccessHandler, failHandler: @escaping INaviFailHandler)
```

- Description: 길 찾기 (멀티 경로)
- Param: `startItem` = 출발지 정보, `goalItem` = 목적지 정보, `viaList` = 경유지 리스트(최대 100개), `successHandler` = 탐색 성공 Handler, `failHandler` = 탐색 실패 Handler (실패 코드는 코드 표 참고)
- Return: void
- 출발지가 nil이면 현위치 기반 탐색(시나리오 예시 주석).

### runSingleRoute

```swift
func runSingleRoute(_ startItem: INaviRoutePtItem?, goalItem: INaviRoutePtItem,
 viaList:[INaviRoutePtItem]?, routeOption opt: INVRouteOptionType,
 successHandler: @escaping INaviRouteSingleSuccessHandler,
 failHandler: @escaping INaviFailHandler)
```

- Description: 길 찾기 (단일 경로)
- Param: `startItem`, `goalItem`, `viaList`(최대 100개), `opt` = 탐색 옵션 정보(Define Reference의 `INVRouteOptionType`), `successHandler`, `failHandler`
- Return: void

### makeRouteSumInfo

```swift
func makeRouteSumInfo(withRouteID rid: String) -> INaviRouteSumInfo
```

- Description: 경로의 간단한 요약 정보 반환
- Param: `rid` = 경로 ID
- Return: `INaviRouteSumInfo` 경로 요약 정보

### getRoutePtInfo

```swift
func getRoutePtInfo(withRouteID rid: String, routePtType type: INVRoutePtType)
-> INaviRoutePtItem
```

- Description: 경로의 출발지/목적지 정보 반환
- Param: `rid` = 경로 ID, `type` = 지점 타입(Define Reference)
- Return: `INaviRoutePtItem` 지점 정보

### getRouteLinePoints

```swift
func getRouteLinePoints(withRouteID rid: String) -> String
```

- Description: 경로 Line 좌표열 반환
- Param: `rid` = 경로 ID
- Return: String, 경로 Line JSON 형태 좌표 문자열

### cancelRoute

```swift
func cancelRoute()
```

- Description: 경로 취소
- Param: void / Return: void

## 5. 주행

### runGuidance

```swift
func runGuidance(withRouteID rid: String) -> Int
```

- Description: 주행 시작. 선택된 경로 ID를 제외한 나머지 경로는 삭제된다.
- Param: `rid` = 경로 ID
- Return: Int, 성공 여부 (0 성공, 그 외 실패)

### isSimulation

```swift
func isSimulation() -> Bool
```

- Description: 모의 주행 여부 반환
- Param: void
- Return: Bool (true 모의 주행 중, false 모의 주행 아님)

### startSimulation

```swift
func startSimulation(withRouteID rid: String) -> Int
```

- Description: 모의 주행 시작
- Param: `rid` = 경로 ID
- Return: Int, 성공 여부 (0 성공, 그 외 실패)

### finishSimulation

```swift
func finishSimulation() -> Int
```

- Description: 모의 주행 종료
- Param: void
- Return: Int, 성공 여부 (0 성공, 그 외 실패)

### getRemainRouteInfo

```swift
func getRemainRouteInfo() -> INaviRouteRemainInfo
```

- Description: 주행 중 남은 거리/시간 정보 반환
- Param: void
- Return: `INaviRouteRemainInfo` 주행 남은 시간/거리 (Structure Reference)

## 6. 기타

### getNaviSDKVersion

```swift
var NaviSDKVersionNumber: Double
```

- Description: SDK 버전 반환
- Value: Double, 내비 SDK 버전 넘버 (소제목은 `getNaviSDKVersion`, 실제 심볼은 `NaviSDKVersionNumber`)

### naviVolume

```swift
var naviVolume: Float
```

- Description: 내비게이션 볼륨 반환/세팅 (단말기의 미디어 볼륨과는 별개로 내비게이션에서만 사용하는 음성)
- Value: Float, 내비게이션 볼륨 (0.0 ~ 1.0)

### getCurrentPosition

```swift
func getCurrentPosition() -> INaviPosition
```

- Description: 현재 위치 반환
- Param: void
- Return: `INaviPosition`

### menuTouch

```swift
func mapView(_ mapView: INaviMapView, menuTouch eventType: INVNaviEvent)
```

- Description: `INaviControllerDelegate` Protocol. 아이나비 버튼 클릭 시 호출
- Param: `mapView` = `iNaviMapView` 객체, `eventType` = 클릭 메뉴 타입 (Define Reference의 `INVNaviEvent`)
- Return: void

### route change

```swift
func mapView(_ mapView: INaviMapView, didChanged rid: String?)
```

- Description: `INaviControllerDelegate` Protocol. 주행 재탐색 성공 시 호출
- Param: `mapView`, `rid` = 재탐색 성공 시 RouteID 전달
- Return: void

### drivingStatus change

```swift
func mapView(_ mapView: INaviMapView, didChanged drivingStatus:
INVDrivingStatus)
```

- Description: `INaviControllerDelegate` Protocol. 주행 시작/도착 시 호출
- Param: `mapView`, `drivingStatus` = 주행 시작/종료 타입 (Define Reference의 `INVDrivingStatus`)
- Return: void

### carSpeed

```swift
func mapView(_ mapView: INaviMapView, carSpeed: Int)
```

- Description: `INaviControllerDelegate` Protocol. 차량 속도 호출
- Param: `carSpeed` = 차량 속도 전달
- Return: void

### layoutTopSafeArea

```swift
var layoutTopSafeArea: Bool
```

- Description: Top SafeArea 영역을 지도 컴포넌트에 적용
- Value: True = 상단 영역 SafeArea 적용, False(Default) = 미적용 (개정 0.0.3, 2020-12-24에 추가된 I/F)

## 함수 색인

| 영역 | 항목 |
|---|---|
| 초기화 | initalizeNavi |
| 지도 컨트롤 | didLongTap, setCarCurrentPosition, setCarPosition, setMapPosition, zoomIn, zoomOut, mapViewMode, visibleTrafficLine, INaviMapOverlay, INaviMapIcon, addMapIcon, removeMapIcon, removeMapIconAll, routeZoomMap, mapLevel, mapFontType, mapDayNightMode, setMapEnableRotate, mapMoveMode, forceHideMapComponent |
| 통합 검색 | runSearch, runRecommendWord, getJibunAddr |
| 길 찾기 | runRoute, runSingleRoute, makeRouteSumInfo, getRoutePtInfo, getRouteLinePoints, cancelRoute |
| 주행 | runGuidance, isSimulation, startSimulation, finishSimulation, getRemainRouteInfo |
| 기타 | getNaviSDKVersion(NaviSDKVersionNumber), naviVolume, getCurrentPosition, menuTouch, route change, drivingStatus change, carSpeed, layoutTopSafeArea |

고객사(SHI)용 사본은 위에 더해 `setShiMember`, `runShiRoute`, `runSingleShiRoute`가 추가되어 있다([[inavi-sdk-ios-guide-shi-edition-differences]]).

## Related
- [[inavi-sdk-ios-guide-hub]] — iOS 가이드 목차
- [[inavi-sdk-ios-structures-defines-and-codes]] — 구조체, enum, 코드 표
- [[navisdk-api-coverage-and-domestic-sdk-guide]] — 국내 SDK API 범위
- [[orbis-sdk]] — 프로젝트 개요

## Sources
- Confluence "iNavi SDK iOS 개발 가이드" (pageId 305201307) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
