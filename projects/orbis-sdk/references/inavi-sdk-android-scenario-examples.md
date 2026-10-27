---
title: >-
    iNavi SDK Android 시나리오별 예시 코드
category: references
project: orbis-sdk
tags: [navisdk, android, sample-code, kotlin, visibility/internal]
aliases: [iNavi SDK Android 시나리오별 예시, 초기화 예시, 화물차 옵션 예시]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[navisdk-api-coverage-and-domestic-sdk-guide]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/305430571
summary: >-
    iNavi SDK(Android) 가이드의 시나리오별 Kotlin 예시 전부: 초기화(Activity/Fragment), 아이콘, 검색, 길찾기, 경유지 재탐색, 안전운행, 화물차, 차종, 여백, TurnView 색, 확대도.
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

# iNavi SDK Android 시나리오별 예시 코드

iNavi SDK Android 개발 가이드의 "시나리오별 예시" 절의 코드를 전부 옮긴 문서이다. 원문은 번호가 10번 이후 "1., 2."로 다시 시작하는데 여기서는 1~12로 이어 붙였다. 함수 상세는 [[inavi-sdk-android-controller-init-map-search]], [[inavi-sdk-android-controller-route-and-driving]], [[inavi-sdk-android-controller-misc-and-truck]]를 본다. 환경 세팅은 [[inavi-sdk-android-setup-and-permissions]], 허브는 [[inavi-sdk-android-guide-hub]].

## 1. 초기화

필수로 `loadNaviLibrary`, `initLayout`, `initalizeNavi`를 호출해야 하며 **호출 순서가 중요**하다.

### Activity 예시
```kotlin
// SDK 초기화 예시
// 필수적으로 loadNaviLibrary, initLayout, initalizeNavi 가 호출 되어야 함
// 호출 순서 중요
class MainActivity : AppCompatActivity() {
    companion object {
        init {
            // application 초기화 시에 호출 : 필수 호출
            INaviController.loadNaviLibrary()
        }
    }
    override fun onCreate(savedInstanceState: Bundle?) {
        setContentView(R.layout.xxx)
        //OnCreate 에서 호출 : 필수 호출
        INaviController.initLayout(this, R.id.mapAdapter, R.id.mapLayer)
        //지도 스타일 변경
        INaviController.setMapStyle(MAPSTYLE.DEFAULT)
        //음성 Stream 변경
        INaviController.setAudioStreamType(AudioManager.STREAM_MUSIC)
        val phoneNumber = "UniqueID"
        //SDK 엔진 초기화 : 필수 호출
        INaviController.initalizeNavi(this, getRootPath(), phoneNumber,
            object : OnNaviInitListener {
                override fun onSuccess() {
                    // SDK 초기화 성공
                }
                override fun onFail(errCode: Int, errMsg: String) {
                    // SDK 초기화 실패
                }
            })
    }
    private fun getRootPath(): String {
        var strStorageDir: String = ""
        val fRootPath = ContextCompat.getExternalFilesDirs(this, null)
        if (fRootPath.isNotEmpty() && fRootPath[0] != null)
            strStorageDir = fRootPath[0].absolutePath
        return strStorageDir
    }
}
```
- 호출 순서: `loadNaviLibrary`(companion init) → `initLayout`(onCreate) → (선택) `setMapStyle`, `setAudioStreamType`, `setEmulatorMode` → `initalizeNavi`.
- `uniqueID`는 20자 이하 Alphanumeric 필수값이다(위반 시 코드 1004/1005).

### Fragment 예시
```kotlin
class MainActivity : AppCompatActivity() {
    companion object {
        init {
            // application 초기화 시에 호출 : 필수 호출
            INaviController.loadNaviLibrary()
        }
    }
    override fun onCreate(savedInstanceState: Bundle?) {
        setContentView(R.layout.xxx)
        val mapFragment = MapFragment(this)
    }
}
class MapFragment(private val acty: Activity) : Fragment() {
    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View? {
        val rootView = inflater.inflate(R.layout.fragment_xxx, container, false)
        //OnCreateView 에서 호출 : 필수 호출
        INaviController.initLayout(acty, rootView, R.id.mapAdapter, R.id.mapLayer)
        //지도 스타일 변경
        INaviController.setMapStyle(MAPSTYLE.DEFAULT)
        //음성 Stream 변경
        INaviController.setAudioStreamType(AudioManager.STREAM_MUSIC)
        val phoneNumber = "UniqueID"
        //SDK 엔진 초기화 : 필수 호출
        INaviController.initalizeNavi(this, getRootPath(), phoneNumber,
            object : OnNaviInitListener {
                override fun onSuccess() {
                    // SDK 초기화 성공
                }
                override fun onFail(errCode: Int, errMsg: String) {
                    // SDK 초기화 실패
                }
            })
    }
    private fun getRootPath(): String {
        var strStorageDir: String = ""
        val fRootPath = ContextCompat.getExternalFilesDirs(this, null)
        if (fRootPath.isNotEmpty() && fRootPath[0] != null)
            strStorageDir = fRootPath[0].absolutePath
        return strStorageDir
    }
}
```
- Fragment에서는 `parentView`를 받는 `initLayout` 오버로드를 쓴다. 원문 예시에서 `initalizeNavi`의 첫 인자가 `this`(Fragment)로 되어 있으나 시그니처는 Application Context를 요구한다 ^[ambiguous]

## 2. 지도 아이콘 표출 및 제거
```kotlin
// 변수 선언
var overlayMap: MapOverlay? = null
var iconEx: MapIcon?= null
// 지도 overlay 생성
overlayMap = INaviController.createMapOverlay()
// 필요하면 overlay에 mapIcon 클릭 이벤트 등록 가능
overlayMap?.setMapIconListener { icon ->
}
// 지도 아이콘 생성
val mapIcon = INaviController.createMapIcon( ... )
// 지도 아이콘을 overlay에 추가
// 정상적으로 overlay에 추가되면 mapIcon이 반환 된다.
iconEx = INaviController.addMapIcon(overlayMap, mapIcon)
// ...
// 지도 아이콘 제거
INaviController.removeMapIcon(overlayMap, iconEx)
iconEx = null
// 지도 overlay 제거
INaviController.removeMapOverlay(overlayMap)
overlayMap = null
```
- `removeMapOverlay`는 함수 레퍼런스 절에는 없고 예시에만 등장한다 ^[inferred]

## 3. 검색
```kotlin
// 검색 쿼리
var query = "검색어"
var lat = 37.00000
var lon = 127.0000
// 검색 시작 및 결과 Callback 처리
INaviController.runSearch( query, lat, lon, object : OnSearchListener {
    override fun onSuccess(result : SearchResult ) {
        // 검색 성공 처리
    }
    override fun onFail(errCode: Int, errMsg: String ) {
        // 검색 실패 처리
    }
})
```

## 4. 길 찾기, 안내시작
```kotlin
// 출발지, 목적지
var startPoint:  RoutePtItem
var goalPoint:  RoutePtItem
//경유지
var viaList = mutableListOf<RoutePtItem>()
viaList.add(
     RoutePtItem( "이름",37.00000, 127.00000, 0.0, 0.0, 0)
)
// 부가정보
var extraInfo: RouteExtraInfo
// 안내시작에 사용할 경로
var routeID: String = ""
// 길찾기에 사용할 탐색 옵션
val optionType = mutableListOf<ROUTEOPTIONTYPE>()
optionType.add(ROUTEOPTIONTYPE.HIGHWAYPRIOTY)
optionType.add(ROUTEOPTIONTYPE.MOTOCYCLE)
// 길 찾기 시작 및 결과 Callback 처리
INaviController.runRoute( startPoint, goalPoint, viaList, optionType, extraInfo, object : OnRouteMultiListener {
    override fun onSuccess(result : ArrayList<String>, same: Boolean ) {
        // 길 찾기 성공 처리
        // 안내시작에 사용할 경로 ID 저장
        routeID = result[0]
        // 지도 화면 경로에 맞게 스케일 조절
        // 모든 경로에 맞춰 스케일 되며, param 에 맞는 경로는 select 상태가 됨
        INaviController.routeZoomMap(result, routeID)
    }
    override fun onFail(errCode: Int, errMsg: String ) {
        // 길 찾기 실패 처리
    }
})
// ...
// 주행 안내 시작
INaviController.runGuidance(routeID)
// 모의 주행 시작
INaviController.startSimulation(routeID)
```
- `RoutePtItem(name, rpLat, rpLon, dpLat, dpLon, angle)` 생성자 순서이다([[inavi-sdk-android-interface-structure-define-reference]]).
- 예시는 `ROUTEOPTIONTYPE.HIGHWAYPRIOTY`(고속도로우선)와 `MOTOCYCLE`(이륜차)을 함께 넣은 목록을 보여 준다.

## 5. 주행중 경유지 변경 재탐색
```kotlin
// 주행중 지나가지 않은 경유지 정보 확인 ( 남은시간, 남은거리 )
var remainViaInfo: List<RouteViaRemainInfo>? = INaviController.getRemainViaRouteInfo()
// 주행중 지나가지 않은 경유지 정보 확인 ( 좌표 )
var rVia: List<RoutePtItem>? = INaviController.getRoutePtRemainViaInfo()
// 새로운 경유지 정보 생성
var viaList = mutableListOf<RoutePtItem>()
viaList.add(
     // 기존 경유지 정보를 추가
     RoutePtItem( rVia[0].name, rVia[0].rpLat, rVia[0].rpLon, 0.0, 0.0, 0)
)
viaList.add(
     // 새로운 지점을 추가
     RoutePtItem( "이름",37.00000, 127.00000, 0.0, 0.0, 0)
)
// 경유지 변경 재 탐색
INaviController.runReRouteChangeVia(viaList, object: OnReRouteResultListener {
    override fun onSuccess() {
        // 재탐색 성공
        // 새로운 경로로 자동 안내시작 됨
    }
    override fun onFail(errCode: Int, msg: String) {
        // 재탐색 실패
    }
})
```
- 원문 예시의 `onSuccess()`에는 인자가 없으나 인터페이스 정의는 `onSuccess(result: String)`이다 ^[ambiguous]

## 6. 안전운행정보 안내 변경
```kotlin
// 현재 설정 값을 가져옴
var settings = INaviController.getGuidanceSettings().toMutableList()
// 과속방지턱 안내가 없다면, 추가
val exist = settings.find { it == GUIDANCESETTING.SPEED_BUMP }
if( exist == null ) {
    settings.add(GUIDANCESETTING.SPEED_BUMP)
}
// 교통정보 수집카메라 안내가 존재하면, 삭제
settings.find { it == GUIDANCESETTING.FIX_TRAFFIC }?.let { item ->
    settings.remove(item)
}
// SDK에 현재 설정 적용
INaviController.setGuidanceSettings(settings)
```

## 7. 화물차 전용 옵션 적용
원문 주석에 적힌 동작 규칙:
- 설정 값은 재실행 시에도 유지되며, 앱 삭제 시 초기화된다.
- 회피옵션을 설정하였더라도 해당 경로가 유일한 경로일 경우에는 제한구역을 포함하는 경로로 안내될 수 있다.
- 각각의 설정값은 별개의 사양으로 동작한다. 예)
  1. 높이값만 설정 시 → 좁은길, 유턴도로, 중량제한 적용 안 됨
  2. 좁은길, 유턴도로만 회피 설정 시 → 높이, 중량제한 적용 안 됨
  3. 높이제한을 설정했으나 높이제한구역을 포함하는 경로가 '유일한' 경로일 때 → 해당 구역을 포함하여 안내

```kotlin
var nHeight : Int = INaviController.getCarHeight() // (default : 0)
var nWeight : Int = INaviController.getCarWeight() // (default : 0)
var nAvoidNarrow : Int = INaviController.getAvoidNarrowRoad() // (default : 0)
var nAvoidUturn : Int = INaviController.getAvoidUturn() // (default : 0)
var bIsAvoidRestriction : Boolean = INaviController.getAvoidRestriction() // (default : false)
/** 도로통과 높이 제한 기능 설정 (cm) **/
// 0 ~ 1000cm [10m]
val nValue = value.toIntOrNull()
if(nValue != null){
    // 제한구역을 통과하는 경로가 유일한 경로일 경우에는 해당 경로로 안내 될 수 있음.
    INaviController.setCarHeight(nValue)
}
/** 도로통과 중량 제한 기능 설정 (kg) **/
// 0 ~ 60000kg [60t]
val nValue = value.toIntOrNull()
if(nValue != null){
    // 제한구역을 통과하는 경로가 유일한 경로일 경우에는 해당 경로로 안내 될 수 있음.
    INaviController.setCarWeight(nValue)
}
/** 왕복 n차선 이하 유턴 회피 **/
val nValue = value.toIntOrNull()
if(nValue != null){
    INaviController.setAvoidUturn(nValue)
}
/** 왕복 n차선 이하 도로 회피 **/
val nValue = value.toIntOrNull()
if(nValue != null){
    INaviController.setAvoidNarrowRoad(nValue)
}
/** 화물차 통행제한구간 회피 **/
val bVal = value.toBoolean()
INaviController.setAvoidRestriction(bVal)
```
- 화물차 경로 제약의 데이터 측 배경은 [[vehicle-restriction-routing]] 참고.

## 8. 차종 설정
설정 값은 재실행 시에도 유지되며 앱 삭제 시 초기화된다.
```kotlin
/**
  *  type (value[int]) : title / description
  *  TYPE_1 (0) = 1종(소형차) / 일반승용, 승합16인 이하, 화물2.5톤 미만
  *  TYPE_2 (1) = 2종(중형차) / 승합32인 이하, 화물5.5톤 이하
  *  TYPE_3 (2) = 3종(대형차) / 승합33인 이상, 화물10톤 미만
  *  TYPE_4 (3) = 4종(대형화물차) / 화물20톤 미만
  *  TYPE_5 (4) = 5종(특수화물차) / 화물20톤 이상
  *  TYPE_6 (5) = 경차 / 1종 : 통행료 할인 적용
  *  TYPE_7 (6) = 이륜차 / ""
  * */
// 차종 값 불러오기 ( default : TYPE_1 )
val curType = INaviController.getCarType()
// 차종 제목
val carTypeTitle = CARTYPE.getTitle(curType) // "1종(소형차)"
// 차종 설명
val carTypeDescription = CARTYPE.getDescription(curType) // "일반승용, 승합16인 이하, 화물2.5톤 미만"
// 차종 설정
INaviController.setCarType(CARTYPE.TYPE_1)
// int to CARTYPE 변환하여 차종 설정 예시
// 위 setCarType(CARTYPE.TYPE_1)과 같은 결과가 적용된다.
INaviController.setCarType(CARTYPE.from(0))
```

## 9. 지도 여백(Padding) 적용
```kotlin
// 사용자가 설정한 패딩 값은 안내 사양에 따라 초기화 될 수 있다.
// e.g) 주행 시작시 설정값 초기화
// RectF 생성 파라메터는 left,top,right,bottom 순서
// 1. 경로선택 화면 지도에 하단 60dp 만큼의 패딩을 추가로 적용 예시
INaviController.routeZoomMapWithPadding(rIdList, selectedRid, android.graphics.RectF(0f,0f,0f,60f))
// 2. 기본지도에 패딩 적용 예시(경로안내/모의주행이 아닐 때)
INaviController.setMapPadding(android.graphics.RectF(0f,0f,0f,60f))
//지도에 적용한 패딩값 초기화
INaviController.clearMapPadding()
```

## 10. TurnView(차기, 차차기, 목적지 도착 view) 배경색 변경
```kotlin
// 설정 값은 재실행 시에도 유지되며, 앱 삭제 시 초기화
// 현재 적용된 차기 turnview bg 얻어오기
val strCurTurnBg = INaviController.getTurnViewBackgroundColor()
/* 사용 가능한 색상명
 red, blue, green, black, white, gray, cyan, magenta, yellow,
 lightgray, darkgray, grey, lightgrey, darkgrey, aqua,
 fuchsia, lime, maroon, navy, olive, purple, silver,teal.
*/
// 차기 turnview에 색상명으로 배경값 적용
INaviController.setTurnViewBackgroundColor("black")
// 차차기 turnview에 16진수 String으로 배경값 적용 "#AARRGGBB"
INaviController.setNextTurnViewBackgroundColor("#f21e55f7")
// 목적지 도착 view에 16진수 String으로 배경값 적용 "#RRGGBB"
INaviController.setArrivalViewBackgroundColor("#1e55f7")
// 적용한 Custom background color 초기화
INaviController.resetTurnViewsBackgroundColor()
```
- 사용 가능한 색상명 23개: red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray, darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy, olive, purple, silver, teal.

## 11. 확대도 표출
```kotlin
// 설정 값은 재실행 시에도 유지되며, 앱 삭제 시 초기화
// 현재 적용된 확대도 표출 여부 가져오기 (default : false)
val bIsShowExtendView = INaviController.getVisibleExtendView()
// 확대도 표출하도록 적용
INaviController.setVisibleExtendView(true)
```
- 원문에는 "확대도 표출 사양(가로모드)", "확대도 표출 사양(세로모드)" 두 항목이 있으나 이미지 항목이라 내용이 없다(이미지/링크 항목, 내용 없음).

## 12. 현위치에서 진행방향으로 탐색열에서 가장 가까운 좌표 얻기
```kotlin
// 엔진초기화 또는 경로가 설정되지 않았을 경우 -1 반환
// 현재 선택한 경로의 RouteID 필요
// 경로 Line 좌표열 얻기
var routeLinePoints = INaviController.getRouteLinePoints(strRouteId)
// 현위치에서 진행방향으로 경로 Line 좌표열 내에서 가장 가까운 index 얻기
var nIdx = INaviController.getNearestVertexIndex()
```

## Related
- [[inavi-sdk-android-guide-hub]] — 이 가이드 묶음 목차
- [[inavi-sdk-android-setup-and-permissions]] — 호출 전 환경 세팅
- [[navisdk-api-coverage-and-domestic-sdk-guide]] — 국내 SDK 가이드 개요
- [[orbis-sdk]] — SDK 프로젝트 허브

## Sources
- Confluence "iNavi SDK Android 개발 가이드" (pageId 305430571) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
