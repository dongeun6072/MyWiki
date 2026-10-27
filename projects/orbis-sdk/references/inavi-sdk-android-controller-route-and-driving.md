---
title: >-
    INaviController Reference 2 - 길찾기, 주행
category: references
project: orbis-sdk
tags: [navisdk, android, api-reference, routing, visibility/internal]
aliases: [INaviController Reference 길찾기, 주행, runRoute, runGuidance, startSimulation]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[navisdk-api-coverage-and-domestic-sdk-guide]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/305430571
summary: >-
    INaviController 함수 레퍼런스 중 길찾기(9)와 주행(9) 파트. runRoute/runSingleRoute/runReRouteChangeVia, 안내/모의주행, 남은 정보, 안전운행 설정.
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

# INaviController Reference 2 - 길찾기, 주행

iNavi SDK Android 가이드 "INaviController Reference" 중 4. 길찾기, 5. 주행 파트이다. 앞 파트는 [[inavi-sdk-android-controller-init-map-search]], 다음 파트는 [[inavi-sdk-android-controller-misc-and-truck]]. 사용 예는 [[inavi-sdk-android-scenario-examples]]의 4~6번, 구조체/enum은 [[inavi-sdk-android-interface-structure-define-reference]], 에러 코드는 [[inavi-sdk-android-error-codes]], 허브는 [[inavi-sdk-android-guide-hub]].

## 4. 길찾기

### 4.1 runRoute
```kotlin
fun runRoute(start: RoutePtItem, goal: RoutePtItem, viaList: List<RoutePtItem>?, optionType: List<ROUTEOPTIONTYPE>?, extraInfo: RouteExtraInfo?, listener: OnRouteMultiListener)
```
- 설명: 길 찾기(멀티 경로)
| 파라미터 | 설명 |
|---|---|
| start | 출발지 정보 |
| goal | 목적지 정보 |
| viaList | 경유지 리스트(최대 100개) |
| optionType | 탐색 옵션 정보(Default 옵션 사용 시 null 입력) |
| extraInfo | 부가정보(필요 없을 시 null 입력) |
| listener | 탐색 결과(경로 ID) 리스트 반환. `OnRouteMultiListener { onSuccess(result: ArrayList<String>, same: Boolean); onFail(errCode: Int, msg: String) }` |
- Return: void
- 이력: 0.0.7 extraInfo 추가, 0.0.22 viaList 추가, 0.0.23 optionType 추가, 0.0.27 경유지 최대 100개 ([[inavi-sdk-android-revision-history]])

### 4.2 runSingleRoute
```kotlin
fun runSingleRoute(start: RoutePtItem, goal: RoutePtItem, viaList: List<RoutePtItem>?, option: ROUTEOPTIONTYPE, extraInfo: RouteExtraInfo?, listener: OnRouteSingleListener)
```
- 설명: 길 찾기(단일 경로)
| 파라미터 | 설명 |
|---|---|
| start | 출발지 정보 |
| goal | 목적지 정보 |
| viaList | 경유지 리스트(최대 100개) |
| optionType | 탐색 옵션 정보(Default 옵션 사용 시 null 입력) |
| extraInfo | 부가정보(필요 없을 시 null 입력) |
| listener | `OnRouteSingleListener { onSuccess(result: String); onFail(errCode: Int, msg: String) }` 단일 탐색 결과(경로 ID) 반환 |
- Return: void
- 시그니처의 파라미터명은 `option`(non-null ROUTEOPTIONTYPE)인데 설명은 `optionType`, "null 입력"으로 되어 있어 불일치한다 ^[ambiguous]

### 4.3 runReRouteChangeVia
```kotlin
fun runReRouteChangeVia(viaList: List<RoutePtItem>?, listener: OnReRouteResultListener)
```
- 설명: 주행중 경유지를 변경하여 재탐색
  - 기존 안내하던 경로가 존재해야 함
  - 기존 안내하던 경유지는 삭제되고 새로운 경유지로 안내
- Param: `viaList` = 경유지 리스트(최대 100개), `listener` = `OnReRouteResultListener { onSuccess(result: String); onFail(errCode: Int, msg: String) }` 재탐색 결과 성공여부 반환
- Return: void

### 4.4 makeRouteSumInfo
```kotlin
fun makeRouteSumInfo(routeID: String): RouteSumInfo
```
- 설명: 경로의 간단한 요약 정보 반환. Param: 경로 ID(String) / Return: RouteSumInfo(경로 요약 정보)

### 4.5 getRoutePtInfo
```kotlin
fun getRoutePtInfo(routeID: String, ptType: ROUTEPTTYPE): RoutePtItem
```
- 설명: 경로의 출발지/목적지 정보 반환. Param: `routeID` = 경로 ID, `ptType` = 지점 타입(START/GOAL) / Return: RoutePtItem(지점 정보)

### 4.6 getRoutePtViaInfo
```kotlin
fun getRoutePtViaInfo(routeID: String, viaIndex: Int): RoutePtItem
```
- 설명: 경로 내 특정 경유지 정보 반환. Param: `routeID`, `viaIndex` = 얻고자 하는 경유지의 순서 / Return: RoutePtItem(경유지 정보)

### 4.7 getRoutePtRemainViaInfo
```kotlin
fun getRoutePtRemainViaInfo(): List<RoutePtItem>?
```
- 설명: 주행중인 경로의 지나가지 않은 경유지 정보 반환. Param: void / Return: List<RoutePtItem>

### 4.8 getRouteLinePoints
```kotlin
fun getRouteLinePoints(routeID: String): JSONArray
```
- 설명: 경로 Line 좌표열 반환. Param: `routeID` / Return: JSONArray(경로 Line 좌표열)

### 4.9 cancelRoute
```kotlin
fun cancelRoute()
```
- 설명: 경로 취소. Param, Return: void

## 5. 주행

### 5.1 runGuidance
```kotlin
fun runGuidance(routeID: String): Int
```
- 설명: 주행 시작. 선택된 "경로 ID"를 제외한 나머지 경로는 삭제된다.
- Param: `routeID` / Return: Int 성공 여부(0 성공 / 그 외 실패)

### 5.2 isSimulation
```kotlin
fun isSimulation(): Boolean
```
- 설명: 모의 주행 여부 반환. Return: Boolean(true 모의주행 중 / false 모의주행 아님)

### 5.3 startSimulation
```kotlin
fun startSimulation(routeID: String): Int
```
- 설명: 모의 주행 시작. Param: `routeID` / Return: Int(0 성공 / 그 외 실패)

### 5.4 finishSimulation
```kotlin
fun finishSimulation(): Int
```
- 설명: 모의 주행 종료. Param: void / Return: Int(0 성공 / 그 외 실패)

### 5.5 getRemainRouteInfo
```kotlin
fun getRemainRouteInfo(): RouteRemainInfo
```
- 설명: 주행중 남은거리/시간/요금 정보 반환. 안내시작/모의주행 시작 이후 호출 필요. Return: RouteRemainInfo

### 5.6 getRemainViaRouteInfo
```kotlin
fun getRemainViaRouteInfo(): List<RouteViaRemainInfo>?
```
- 설명: 주행중 지나가지 않은 경유지의 남은거리/시간 정보 반환. 안내시작 이후 호출 필요. Return: RouteViaRemainInfo(경유지의 남은거리/시간)

### 5.7 getTotalRemainRouteInfo
```kotlin
fun getTotalRemainRouteInfo(routeID: String): RouteRemainInfo
```
- 설명: 경로의 총 거리/시간/요금 정보 반환. **안내시작/모의주행 시작 전** 호출 필요. Param: `routeID` / Return: RouteRemainInfo(총 남은거리/시간/요금)

### 5.8 setGuidanceSettings
```kotlin
fun setGuidanceSettings(settings: List<GUIDANCESETTING>?)
```
- 설명: "안전운행정보 안내" 설정 변경
- Param: `settings` = List에 존재하는 값만 설정 On, 나머지 Off. null 입력 시 아이나비 Default 옵션 적용 / Return: void

### 5.9 getGuidanceSettings
```kotlin
fun getGuidanceSettings(): List<GUIDANCESETTING>
```
- 설명: 현재 "안전운행정보 안내" 반환. Return: 현재 On 되어 있는 설정 리스트

## Related
- [[inavi-sdk-android-guide-hub]] — 이 가이드 묶음 목차
- [[inavi-sdk-android-controller-misc-and-truck]] — 다음 파트(기타, 화물차)
- [[orbis-routing-stack]] — 신규 Orbis 쪽 라우팅 구성(대비용)
- [[orbis-sdk]] — SDK 프로젝트 허브

## Sources
- Confluence "iNavi SDK Android 개발 가이드" (pageId 305430571) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
