---
title: >-
    iNavi SDK iOS Structure/Define Reference와 코드 표
category: references
project: orbis-sdk
tags: [ios, sdk, api-reference, enum, error-codes, visibility/internal]
aliases: [SDK Structure Reference, SDK Define Reference, 코드 표, iNavi SDK iOS 코드 표]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[navisdk-api-coverage-and-domestic-sdk-guide]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/305201307
summary: >-
    iOS SDK의 데이터 구조체(INaviPosition 등 8종), enum 정의(INVMapViewMode 등 9종), 실패/성공 코드 표 전체.
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

# iNavi SDK iOS Structure/Define Reference와 코드 표

iOS SDK 가이드의 "SDK Structure Reference", "SDK Define Reference", "코드 표"를 모두 옮겼다. 함수가 받고 돌려주는 타입은 [[inavi-sdk-ios-controller-reference]]에서 참조된다. 목차는 [[inavi-sdk-ios-guide-hub]], 국내 SDK 개요는 [[navisdk-api-coverage-and-domestic-sdk-guide]], [[orbis-sdk]].

## SDK Structure Reference

### 1. INaviPosition

```swift
// 위도 (도 단위)
private(set) var lat:Double
// 경도 (도 단위)
private(set) var lng:Double
// 각도
private(set) var angle:Double
// 속도
private(set) var speed:Double
```

### 2. INaviSearchResult

```swift
// 검색에 사용된 검색어
var query: String
// 검색 결과 리스트
var items: [INaviSearchItem]
```

### 3. INaviSearchItem

```swift
// 지도 위치보기에 사용되는 좌표 포지션
var dpPosition: INaviPosition
// 길 찾기 시에 사용되는 좌표 포지션
var rpPosition: INaviPosition
// 검색 결과 항목 타이틀
var mainTitle: String
// 검색 결과 지번 주소
var addrJibun: String
// 검색 결과 도로 명 주소
var addrRoad: String
// 검색에 사용했던 기준좌표와의 거리
var distance: Int
// 검색 아이템 하위 결과 여부
var isSubItem: Bool
```

### 4. INaviRecommendWord

```swift
// 추천어
var recommendWord: String?
// 추천어 조회 빈도 수
var frequency = 0
```

### 5. INaviRoutePtItem

```swift
// 지점 명칭
var name: String
// 길 찾기 시에 사용되는 좌표 포지션
var dpPosition: INaviPosition
// 지도 위치보기에 사용되는 좌표 포지션
var rpPosition: INaviPosition
```

주의: `INaviSearchItem`은 `dpPosition`을 "지도 위치보기", `rpPosition`을 "길 찾기"용으로 설명한 반면, `INaviRoutePtItem`은 반대로(`dpPosition` = 길 찾기, `rpPosition` = 지도 위치보기) 적혀 있다. 원본 문서 오류로 보이며 의미상 dp = display, rp = route point로 읽는 것이 자연스럽다. ^[inferred]

### 6. INaviRouteSumInfo

```swift
// 길 찾기 시에 사용된 옵션 명칭
optionName : String
// 경로 총 거리
dist : String
// 목적지 도착 예정 시간
time : String
// 톨게이트 총 요금 정보
fee : String
```

### 7. INaviRouteRemainInfo

```swift
// 목적지 까지 남은 시간 ( '초' 단위 )
remainTime : Int
// 목적지 까지 남은 거리 ( 'm' 단위 )
remainDist : Int
// 목적지 까지 남은 요금 ( '원' 단위 ) -> 요금계산 실패시 -1
remainFee : Int
```

### 8. INaviShiMember

```swift
//사용자 ID
userId : NSString
//00(승용) , 01(승합(4톤미만)) , 02 (승합(4톤이상))
drvrTon : NSString
```

이 구조체는 고객사(SHI)용 기능 `setShiMember`와 연결된다. 원본(일반) 가이드에도 구조체 정의가 남아 있으나 `setShiMember` 함수는 SHI 사본에만 있다([[inavi-sdk-ios-guide-shi-edition-differences]]).

### Structure 요약 표

| 구조체 | 필드 |
|---|---|
| INaviPosition | lat, lng, angle, speed (Double, 읽기 전용) |
| INaviSearchResult | query, items |
| INaviSearchItem | dpPosition, rpPosition, mainTitle, addrJibun, addrRoad, distance, isSubItem |
| INaviRecommendWord | recommendWord, frequency |
| INaviRoutePtItem | name, dpPosition, rpPosition |
| INaviRouteSumInfo | optionName, dist, time, fee |
| INaviRouteRemainInfo | remainTime(초), remainDist(m), remainFee(원, 실패 -1) |
| INaviShiMember | userId, drvrTon |

## SDK Define Reference

### 1. INVMapViewMode

```swift
enum INVMapViewMode : Int {
    // 3D 뷰
    case mode3D
    // 2D 회전 뷰 ( 자차가 정북 고정 )
    case mode2D
    // 2D 고정 뷰 ( 지도가 정북 고정 )
    case mode2DFIX
}
```

### 2. INVIconAnchor

```swift
enum INVIconAnchor : Int {
    // 이미지 정중앙이 Mapicon 좌표 위치
    case center
    // 이미지의 정중앙 하단이 Mapicon 좌표 위치 ( 좌표를 중심으로 이미지를 상단으로 이동 )
    case centerTop
    // 이미지의 우측 하단이 Mapicon 좌표 위치 ( 좌표를 중심으로 이미지를 좌측 상단으로 이동 )
    case leftTop
    // 이미지의 좌측 하단이 Mapicon 좌표 위치 ( 좌표를 중심으로 이미지를 우측 상단으로 이동 )
    case rightTop
    // 이미지의 우측 상단이 Mapicon 좌표 위치 ( 좌표를 중심으로 이미지를 좌측 하단으로 이동 )
    case leftBottom
    // 이미지의 좌측 상단이 Mapicon 좌표 위치 ( 좌표를 중심으로 이미지를 우측 상단으로 이동 )
    case rightBottom
}
```

### 3. INVMapFontType

```swift
enum INVMapFontType : Int {
    // 기본 사이즈
    case invMapFontNomal
    // 확대 사이즈
    case invMapFontLarge
}
```

### 4. INVMapDayNightMode

```swift
enum INVMapDayNightMode : Int {
    // 시간대별 주/야 자동 변경
    case auto
    // 항상 주간 지도
    case alwaysDay
    // 항상 야간 지도
    case alwaysNight
}
```

### 5. INVRoutePtType

```swift
enum INVRoutePtType : Int {
    // 출발지
    case invRoutePtStart
    // 목적지
    case invRoutePtGoal
}
```

### 6. INVNaviEvent

```swift
enum INVNaviEvent : Int {
    // 하단 바 좌측, 메인 메뉴 버튼
    case eventMain
    // 하단 바 우측, 멀티 메뉴 버튼
    case eventMulti
    // 목적지 도착 하단 바 안내종료 버튼
    case evenGuideCancel
    // 지도이동 시 볼륨 버튼
    case evenVolume
}
```

### 7. INVDrivingStatus

```swift
enum INVDrivingStatus : Int {
    // 주행시작
    case start
    // 목적지 근처( 목적지에서 대략 100m 부근 )
    case nearGoal
    // 주행완료
    case arrival
}
```

### 8. INVRouteOptionType

```swift
enum INVRouteOptionType : Int {
    // 빠른길
    case timePrioty
    // 추천길
    case recommend
    // 무료길
    case freeRoad
    // 편한길
    case beginner
    // 이륜차
    case motorcycle
    // 고속도로우선
    case highwayPrioty
    // 최단거리
    case distancePrioty
}
```

### 9. INVMapComponent

```swift
enum INVMapComponent : Int {
    // 모든 지도 컴포넌트 ( 아래 항목을 한번에 처리할 때 사용 )
    case ALL_COMPONENT
    // 나침반 버튼 ( 지도 이동시 )
    case ANGLE_BTN
    // 현위치로 버튼 ( 지도 이동시 )
    case CUR_ON_BTN
    // 확대/축소 버튼 ( 지도 이동시 )
    case ZOOM_IN_OUT_BTN
    // 지도 하단 뷰 ( 경로 없는 경우 )
    case BOTTOM_NORMAL_VIEW
    // 지도 하단 뷰 ( 경로 존재 하는 경우 )
    case BOTTOM_DRIVING_VIEW
    // 목적지 도착 상단 뷰
    case TOP_ARRIVAL_VIEW
    // 목적지 도착 하단 뷰
    case BOTTOM_ARRIVAL_VIEW
    // 주행중 우측 교통정보 바
    case ROUTE_TRAFFIC_STATUS_BAR
}
```

### Define 메모

- `INVIconAnchor`의 주석은 `leftTop`/`rightTop`/`leftBottom`/`rightBottom` 설명이 이름과 어긋나 보이는 부분이 있으나(예: `leftTop`인데 "이미지의 우측 하단이 좌표 위치") 원문 그대로 옮겼다. 이름은 이미지가 좌표 기준 어느 쪽에 놓이는지를, 주석은 좌표가 이미지의 어느 모서리인지를 말하는 것으로 읽을 수 있다. ^[inferred]
- `INVMapMoveMode`(지도 이동 시작/종료)는 `mapMoveMode` Callback에서 쓰이지만 Define Reference에는 정의가 없다. ^[ambiguous]
- 철자(`Nomal`, `Prioty`, `evenGuideCancel`, `evenVolume`)는 원본 그대로이다.

## 코드 표

실패 코드는 초기화 Delegate, 검색/길 찾기의 `failHandler`(code, msg) 등에서 전달된다.

| 코드값 | 설명 |
|---|---|
| 0 | 성공 |
| 1 | 탐색 실패 |
| 3 | 목적지가 물리적 섬 도로 |
| 32 | 탐색 가능 거리 초과 |
| 35 | 두 지점이 너무 가까운 경우 |
| 120 | 최적경로 (재탐색은 성공했으나 더 좋은 경로가 없는 경우) |
| 121 | 목적지 부근으로 재탐색이 필요 없는 경우 |
| 901 | 인증정보가 변경되어 앱 재시작 필요 |
| 903 | 조회결과 없음 |
| 1000 | 인증 데이터 오류 |
| 1002 | 유효하지 않은 형식으로 인증 요청 |
| 1003 | 인증 데이터가 존재하지 않음 |
| 1004 | 유효하지 않은 Unique Key (필수값인 Unique Key 값이 Null 이거나 Empty 인 경우) |
| 2000 | 처리되지 않은 예외 발생 |
| 2001 | 유효하지 않은 출발지 |
| 2003 | 유효하지 않은 목적지 |
| 2006 | 서버 응답 오류 |
| 3001 | 초기 지도 다운로드 실패 |
| 3006 | 안전운행 다운로드 실패 |
| 3007 | 인증 실패 |
| 4000 | 검색 결과 없음 |
| 4001 | 유효하지 않은 검색어 |

## Related
- [[inavi-sdk-ios-guide-hub]] — iOS 가이드 목차
- [[inavi-sdk-ios-controller-reference]] — 이 타입을 쓰는 함수들
- [[navisdk-api-coverage-and-domestic-sdk-guide]] — 국내 SDK API 범위
- [[orbis-sdk]] — 프로젝트 개요

## Sources
- Confluence "iNavi SDK iOS 개발 가이드" (pageId 305201307) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
