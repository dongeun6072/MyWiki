---
title: >-
    iNavi SDK Android Interface, Structure, Define Reference
category: references
project: orbis-sdk
tags: [navisdk, android, api-reference, enum, visibility/internal]
aliases: [SDK Interface Reference, SDK Structure Reference, SDK Define Reference, CARTYPE, ROUTEOPTIONTYPE, MAPCOMPONENT]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[navisdk-api-coverage-and-domestic-sdk-guide]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/305430571
summary: >-
    iNavi SDK(Android)의 Listener 인터페이스 12종, 구조체 10종(NaviLocation 등), enum/상수 14종(ROUTEOPTIONTYPE, MAPCOMPONENT, CARTYPE 등) 정의 전체.
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

# iNavi SDK Android Interface, Structure, Define Reference

iNavi SDK Android 가이드의 "SDK Interface Reference", "SDK Structure Reference", "SDK Define Reference" 절을 모두 옮긴 문서이다. 함수 쪽은 [[inavi-sdk-android-controller-init-map-search]], [[inavi-sdk-android-controller-route-and-driving]], [[inavi-sdk-android-controller-misc-and-truck]]를 보고, 허브는 [[inavi-sdk-android-guide-hub]]이다. SDK 전반 맥락은 [[navisdk-api-coverage-and-domestic-sdk-guide]].

## SDK Interface Reference (Listener)
```kotlin
interface OnNaviInitListener {            // 1
    fun onSuccess()
    fun onFail(errCode: Int, errMsg: String)
}
interface OnNaviEventListener {           // 2
    fun onEvent(e: NaviEvent)
}
interface OnMapClickListener {            // 3
    fun onMapLongClick(lat: Double, lon: Double)
}
interface OnMapMoveChangedListener {      // 4
    fun onStart()
    fun onStop()
}
interface OnSearchListener {              // 5
    fun onSuccess(result: SearchResult)
    fun onFail(errCode: Int, errMsg: String)
}
interface OnRecommendWordListener {       // 6
    fun onSuccess(result : ArrayList<RecommendWord>)
    fun onFail(errCode: Int, errMsg: String)
}
interface OnRouteMultiListener {          // 7
    fun onSuccess(result: ArrayList<String>, same: Boolean)
    fun onFail(errCode: Int, msg: String)
}
interface OnRouteSingleListener {         // 8
    fun onSuccess(result: String)
    fun onFail(errCode: Int, msg: String)
}
interface OnReRouteResultListener {       // 9
    fun onSuccess(result: String)
    fun onFail(errCode: Int, msg: String)
}
interface OnRouteChangedListener {        // 10
    fun onChanged(routeID: String)
}
interface OnDrivingStatusListener {       // 11
    fun onStatus(status: DRIVINGSTATUS)
    fun onArrivalFee(fee: Int)
    fun onArrivalVia(nIndex: Int) // v0.0.29 부터 추가
}
interface OnCarSpeedListener {            // 12
    fun onSpeed(speed: Int)
}
```
- `OnRouteMultiListener.onSuccess`의 `same`의 의미는 원문에 설명이 없다 ^[ambiguous]

## SDK Structure Reference
```kotlin
class NaviLocation {
    var lat: Double     // 위도
    var lon: Double     // 경도
    var angle: Double   // 정북 기준 각도(0.0 ~ 360.0): v0.0.20 부터 Double 사용, v0.0.19 까지는 Int 사용
    var speed: Double   // 속도
}
class SearchResult {
    var query: String                  // 검색어
    var items: ArrayList<SearchItem>?  // 검색 결과 리스트
}
class SearchItem {
    var dpLat: Double          // 지도 위치보기 시에 사용하는 위도 좌표
    var dpLon: Double          // 지도 위치보기 시에 사용하는 경도 좌표
    var rpLat: Double          // 길 찾기 시에 사용하는 위도 좌표
    var rpLon: Double          // 길 찾기 시에 사용하는 경도 좌표
    var mainTitle: String      // 검색 결과 항목 타이틀
    var addrJibun: String      // 검색 결과 지번 주소
    var addrRoad: String       // 검색 결과 도로명 주소
    var distane: Int           // 검색에 사용했던 기준좌표와의 거리
}
class RecommendWord {
    var recommendWord: String     // 추천어
    var frequency: Int            // 추천어 조회 빈도 수
}
class RoutePtItem {
    var name: String        // 지점 명칭
    var rpLat: Double       // 길 찾기 시에 사용하는 위도 좌표
    var rpLon: Double       // 길 찾기 시에 사용하는 경도 좌표
    var dpLat: Double       // 지도 위치보기 시에 사용하는 위도 좌표
    var dpLon: Double       // 지도 위치보기 시에 사용하는 경도 좌표
    var angle: Int          // 길 찾기 시에 사용하는 각도 ( 0 ~ 359 )
}
class RouteSumInfo {
    var optionName: String  // 길찾기 시에 사용된 옵션 명칭
    var dist: String        // 경로 총 거리
    var time: String        // 목적지 도착 예정 시간
    var fee: String         // 총 톨게이트 요금 정보
}
class NaviEvent {
    var eventType: NAVIEVENTTYPE   // 이벤트 타입
}
class RouteRemainInfo {
    var remainTime:Int     // 목적지 까지 남은 시간 ( '초' 단위 )
    var remainDist:Int     // 목적지 까지 남은 거리 ( 'm' 단위 )
    var remainFee:Int      // 목적지 까지 남은 요금 ( '원' 단위 ), 요금 계산 실패시 -1
}
class RouteViaRemainInfo {
    var remainTime: Int    // 경유지 까지 남은 시간 ( '초' 단위 )
    var remainDist: Int    // 경유지 까지 남은 거리 ( 'm' 단위 )
}
class RouteExtraInfo {
    var baseURL: String    //부가정보 외부연동 URL
}
```
- `SearchItem.distane`는 원문 표기 그대로이다(distance 오타로 보임) ^[inferred]
- `RoutePtItem` 생성자 호출 예는 `RoutePtItem("이름", rpLat, rpLon, dpLat, dpLon, angle)` 순서이다.
- `RouteExtraInfo.baseURL`은 부가정보 외부연동 URL이며 값은 문서에 없다.

## SDK Define Reference (enum)

### MAPVIEWMODE
| 값 | 설명 |
|---|---|
| VIEWMODE_3D | 3D 뷰 |
| VIEWMODE_2D | 2D 회전 뷰 |
| VIEWMODE_2D_FIX | 2D 고정 뷰(지도가 정북 고정) |

### ICONGRAVITY
| 값 | 설명 |
|---|---|
| CENTER | 이미지 정중앙이 MapIcon 좌표 위치 |
| CENTER_TOP | 이미지의 정중앙 하단이 MapIcon 좌표 위치(좌표를 중심으로 이미지를 상단으로 이동) |
| LEFT_TOP | 이미지의 우측하단 좌표가 MapIcon 좌표 위치(좌표를 중심으로 이미지를 좌측 상단으로 이동) |
| RIGHT_TOP | 이미지의 좌측하단 좌표가 MapIcon 좌표 위치(좌표를 중심으로 이미지를 우측 상단으로 이동) |
| LEFT_BOTTOM | 이미지의 우측상단 좌표가 MapIcon 좌표 위치(좌표를 중심으로 이미지를 좌측 하단으로 이동) |
| RIGHT_BOTTOM | 이미지의 좌측상단 좌표가 MapIcon 좌표 위치(좌표를 중심으로 이미지를 우측 하단으로 이동) |

### MAPFONTSIZETYPE
| 값 | 설명 |
|---|---|
| NORMAL | 기본 사이즈 |
| LARGE | 확대 사이즈 |

### MAPDAYNIGHTMODE
| 값 | 설명 |
|---|---|
| AUTO | 시간대별 주/야 자동 변경 |
| ALWAYSDAY | 항상 주간 지도 |
| ALWAYSNIGHT | 항상 야간 지도 |

### ROUTEPTTYPE
| 값 | 설명 |
|---|---|
| START | 출발지 |
| GOAL | 목적지 |

### APPSTATUS
| 값 | 설명 |
|---|---|
| BACKGROUND | App이 Background 상태 |
| SCREEN_OFF_BACKGROUND | 스크린 화면이 꺼진 상태 |
| FOREGROUND | App이 Foreground 상태 |

### NAVIEVENTTYPE
| 값 | 설명 |
|---|---|
| NONE | 없음 |
| MAINMENU | 하단바 좌측, 메인메뉴 버튼 |
| MULTIMENU | 하단바 우측, 멀티메뉴 버튼 |
| EXITAPPLICATION | 목적지 도착 하단바, 앱 종료 버튼 |
| VOLUMEMAPBUTTON | 지도이동시 볼륨 버튼 |
| CURRRENTPOSITION | 지도이동시 현위치로 버튼 |
| ALLROUTEVIEW | 전체경로보기 |

### DRIVINGSTATUS
| 값 | 설명 |
|---|---|
| START | 주행 시작 |
| NEARGOAL | 목적지 근처(목적지 근처 대략 100m 부근, `setDrivingStatusListener`의 `nearGoalDist`로 조정) |
| ARRIVAL | 주행 완료 |

### ROUTEOPTIONTYPE
| 값 | 설명 | 비고 |
|---|---|---|
| TIMEPRIOTY | 빠른길 | |
| RECOMMEND | 추천길 | |
| FREEROAD | 무료길 | |
| BEGINNER | 편한길 | |
| MOTOCYCLE | 이륜차 | |
| HIGHWAYPRIOTY | 고속도로우선 | |
| DISTANCEPRIOTY | 최단거리 | |
| TRUCK | 실시간만차 | 0.0.27 화물차 전용 |
| TRUCK_FREEROAD | 실시간만차(무료) | 0.0.27 |
| TRUCK2 | 실시간공차 | 0.0.27 |
| TRUCK2_FREEROAD | 실시간공차(무료) | 0.0.27 |
| TRUCK_NATIONALWAY | 국도만차 | 0.0.27 |
| TRUCK2_NATIONALWAY | 국도공차 | 0.0.27 |

### MAPCOMPONENT
| 값 | 설명 | 추가 버전 |
|---|---|---|
| ALL_COMPONENT | 모든 지도 컴포넌트(아래 모든 항목을 한 번에 처리할 때 사용) | |
| ANGLE_BTN | 나침반 버튼(지도 이동시) | |
| CUR_ON_BTN | 현위치로 버튼(지도 이동시) | |
| ZOOM_IN_OUT_BTN | 확대/축소 버튼(지도 이동시) | |
| BOTTOM_NORMAL_VIEW | 지도 하단 뷰(경로 없는 경우) | |
| BOTTOM_DRIVING_VIEW | 지도 하단 뷰(경로 존재 하는 경우) | |
| TOP_ARRIVAL_VIEW | 목적지 도착 상단 뷰 | |
| BOTTOM_ARRIVAL_VIEW | 목적지 도착 하단 뷰 | |
| ROUTE_TRAFFIC_STATUS_BAR | 주행중 우측 교통정보 바 | 0.0.17 |
| BOTTOM_NORMAL_SIDE_BUTTON | 지도 하단 뷰 버튼(경로 없는 경우) | 0.0.27 |
| BOTTOM_DRIVING_SIDE_BUTTON | 지도 하단 뷰 버튼(경로 존재 하는 경우) | 0.0.27 |
| BOTTOM_ARRIVAL_LEFT_BUTTON | 목적지 도착 하단바 좌측 버튼 | 0.0.27 |

### MAPSTYLE
| 값 | 설명 |
|---|---|
| DEFAULT | 아이나비 지도 |
| MAPBOX | Mapbox Style 지도 |

### GUIDANCESETTING (안전운행정보 안내)
| 값 | 설명 |
|---|---|
| MOVE_OVERSPEED | 이동식 과속 단속 카메라 주의안내 |
| MOVE_BOX_OVERSPEED | 박스형 과속 단속 카메라 주의안내 |
| INTERRUPT | 끼어들기 단속 주의안내 |
| OVERLOAD | 과적단속 주의안내 |
| FIX_TRAFFIC | 교통정보수집 카메라 안내 |
| CURVE | 급커브 구간 주의안내 |
| ACCIDENT | 사고다발 구간 주의안내 |
| SPEED_BUMP | 과속방지턱 주의안내 |
| SCHOOL_ZONE | 스쿨존/실버존 주의안내 |
| WILDANIMAL | 야생동물 출현 주의안내 |
| TRAIN_TRACK | 철도건널목 주의안내 |
| ROAD_DROP | 낙석구간 주의안내 |
| GREEN_AREA | 녹색교통지역 진입 안내 |

### MAPROUTECOLOR
| 값 | 설명 |
|---|---|
| TRAFFIC | 실시간 교통정보 |
| RED | 빨간색 |
| ORANGE | 주황색 |
| YELLOW | 노란색 |
| GREEN | 초록색 |
| BLUE | 파란색(Default) |
| INDIGO | 군청색 |

### CARTYPE
```kotlin
enum class CARTYPE(val value : Int){
    TYPE_1(0),  TYPE_2(1),  TYPE_3(2),  TYPE_4(3),
    TYPE_5(4),  TYPE_6(5),  TYPE_7(6);
    companion object {
        fun from(findValue: Int): CARTYPE = values().first { it.value == findValue }
        fun getTitle(value : CARTYPE): String = when(value){ ... }
        fun getDescription(value : CARTYPE): String = when(value){ ... }
    }
}
```
| 값 | int | 제목(getTitle) | 설명(getDescription) |
|---|---|---|---|
| TYPE_1 | 0 | 1종(소형차) | 일반승용, 승합16인 이하, 화물2.5톤 미만 |
| TYPE_2 | 1 | 2종(중형차) | 승합32인 이하, 화물5.5톤 이하 |
| TYPE_3 | 2 | 3종(대형차) | 승합33인 이상, 화물10톤 미만 |
| TYPE_4 | 3 | 4종(대형화물차) | 화물20톤 미만 |
| TYPE_5 | 4 | 5종(특수화물차) | 화물20톤 이상 |
| TYPE_6 | 5 | 경차 | 1종 : 통행료 할인 적용 |
| TYPE_7 | 6 | 이륜차 | (빈 문자열) |
- 원문 주석에서 TYPE_6은 `"경차(1종 : 통행료 할인 적용)"`로, `getTitle`은 "경차"로 반환한다.
- 기본값은 TYPE_1이다.

## Related
- [[inavi-sdk-android-guide-hub]] — 이 가이드 묶음 목차
- [[inavi-sdk-android-error-codes]] — 에러/상태 코드 표
- [[navisdk-api-coverage-and-domestic-sdk-guide]] — 국내 SDK 가이드 개요
- [[orbis-sdk]] — SDK 프로젝트 허브

## Sources
- Confluence "iNavi SDK Android 개발 가이드" (pageId 305430571) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
