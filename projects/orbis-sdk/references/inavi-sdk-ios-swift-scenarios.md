---
title: >-
    iNavi SDK iOS 시나리오별 Swift 예시
category: references
project: orbis-sdk
tags: [ios, sdk, swift, examples, visibility/internal]
aliases: [시나리오 별 SDK 예시 ( swift ), iNavi SDK iOS 예시]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[navisdk-api-coverage-and-domestic-sdk-guide]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/305201307
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/305201319
summary: >-
    iOS SDK 가이드의 Swift 시나리오 예시 전부(초기화, 지도 아이콘, 검색, 길 찾기와 안내/모의주행)와 SHI 사본의 추가 예시(사용자 정보 입력, 소지번 길 찾기).
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

# iNavi SDK iOS 시나리오별 Swift 예시

iOS SDK 가이드 끝부분의 "시나리오 별 SDK 예시 ( swift )"를 그대로 옮긴 페이지다. 일반 사본에는 4개, 고객사(SHI) 사본에는 6개 시나리오가 있다. 함수 설명은 [[inavi-sdk-ios-controller-reference]], 설치는 [[inavi-sdk-ios-guide-setup]], 목차는 [[inavi-sdk-ios-guide-hub]]. 국내 SDK 가이드: [[navisdk-api-coverage-and-domestic-sdk-guide]].

예시 코드는 원본의 변수명과 주석을 유지했다. 원본의 일부 값(식별자 예시 문자열, 테스트 사용자 ID)은 실제 값처럼 보여 `<...>` 자리표시자로 바꿨다(보안 규칙).

## 1. SDK 초기화

```swift
// SDK 초기화
override func viewDidLoad() {
    super.viewDidLoad()
    let mapView = INaviMapView(frame: view.bounds)
    view.addSubview(mapView)
    let controller = INaviController.sharedInstance()
    controller.initalizeNavi("<UNIQUE_ID>", target: self)
}
//INaviControllerDelegate
// 인증 성공 후 SDK 모든 기능 동작합니다.
func authResultCode(_ resultCode: Int, message: String?) {
    if resultCode == 0 {
		//인증 성공
    } else {
		//인증 실패
    }
}
```

- 원본의 `initalizeNavi` 인자는 전화번호 형태의 숫자 문자열이었다(미수록). uniqueID는 20자 이하 Alphanumeric 필수값이다.
- `authResultCode(_:message:)`의 `resultCode`는 코드 표([[inavi-sdk-ios-structures-defines-and-codes]])를 따른다. 0이 성공이다.
- 이 Delegate 메서드는 INaviController Reference 본문에는 별도 항목이 없고 예시에만 나온다. ^[ambiguous]

## 2. 지도 아이콘 표출 및 제거

```swift
// 지도 overlay 생성
let overlayMap = INaviMapOverlay.create()
// 지도 아이콘 생성
let mapIcon = INaviMapIcon.createMapIcon(withPostion: INaviPosition(lat: 37.0000,
lng: 127.0000),nomalImage: INaviImage(image: UIImage("testImage")),
anchor: .centerTop)
// 지도 아이콘을 overlay 추가
INaviController.sharedInstance().addMapIcon(with: overlayMap, mapIcon: mapIcon)
// 지도 아이콘 제거
INaviController.sharedInstance().removeMapIcon(with: overlayMap,
mapIcon: mapIcon)
```

## 3. 검색

```swift
// 검색 쿼리
var query = "검색어"
var lat = 37.00000
var lon = 127.0000
// 검색 시작 및 결과 Callback 처리
let curPositon = INaviController.sharedInstance().getCurrentPosition()
INaviController.sharedInstance().runSearch(query, lat: curPositon.lat,
lng: curPositon.lng) { [weak self] (resultItem) in
    //검색 성공 처리
} failHandler: {[weak self]  (code, msg) in
    //검색 실패 처리
}
```

- 현재 위치(`getCurrentPosition()`)를 기준 좌표로 쓰는 패턴이다. 예시에서 `lat`, `lon` 변수는 선언만 되고 실제 호출에는 쓰이지 않는다.

## 4. 길 찾기 -> 안내 시작 (모의 주행 시작)

```swift
let controller = INaviController.sharedInstance()
// 출발지 nil이면 현위치기반 탐색
let startPoint:INaviRoutePtItem? //nil이면 현위치기반 탐색
// 목적지
let goalPoint = INaviRoutePtItem()
goalPoint.name = "목적지"
goalPoint.dpPosition = INaviPosition(lat: 37.0, lng: 127.0)
goalPoint.rpPosition = INaviPosition(lat: 37.0, lng: 127.0)
// 안내시작에 사용할 경로
var routeId = ""
// 길 찾기 시작 및 결과 처리
controller.runRoute(startPoint, goalItem: goalPoint, successHandler:
{[weak self] (dataAry, isSame) in
    //길 찾기 성공 처리
    let ary = dataAry as? [String] ?? []
    routeId = ary?.firstObject ?? ""
    controller.routeZoomMap(withRouteIdList: ary, selectedRID: routeId)
}) { (code, msg) in
    //길 찾기 실패 처리
}
…
…
…
// 주행 안내 시작
controller.runGuidance(withRouteID: routeId)
// 모의 주행 시작
controller.startSimulation(withRouteID: routeId)
```

- 성공 Handler는 `(dataAry, isSame)` 두 인자를 받는다. `dataAry`는 경로 ID 배열이다.
- 원본 예시는 `viaList` 인자를 생략하고 `runRoute`를 호출한다(Reference 시그니처에는 `viaList`가 있음). SHI 사본 개정 1.0.0(2023-08-03)에서 "길찾기 경유지 입력 추가"가 기록되어 있어 시기별 시그니처 차이일 가능성이 있다. ^[inferred]
- `routeId = ary?.firstObject ?? ""`는 `[String]`에 옵셔널 체이닝과 `firstObject`(NSArray API)를 쓴 원본 표기이며 컴파일 가능한 코드가 아닐 수 있다. 예시로서 흐름만 참고한다. ^[ambiguous]
- 중간의 `…` 세 줄은 원본에서 사용자가 경로를 고르는 등의 과정이 생략된 표시다.
- `runGuidance`는 선택한 경로 ID를 제외한 나머지 경로를 삭제한다. 실제 주행과 모의 주행 중 하나를 호출한다.

## SHI 사본에만 있는 추가 시나리오

### 5. 삼성중공업 사용자 정보 입력

```swift
let member = INaviShiMember()
member.userId = "<사용자 ID>"
member.drvrTon = "01" //00(승용) , 01(승합(4톤미만)) , 02 (승합(4톤이상))
controller.setShiMember(member)
```

- 원본 예시의 `userId`는 테스트 계정 형태 문자열이었다(미수록). `drvrTon`은 차량 구분 코드이다.

### 6. 삼성중공업 소지번 길 찾기 -> 안내 시작 (모의 주행 시작)

```swift
// 길 찾기 시작 및 결과 처리
controller.runShiRoute("건물I", goalItem: "건물A", viaList: ["건물B","건물C","건물D"],
successHandler: {[weak self] (dataAry, isSame) in
    //길 찾기 성공 처리
    let ary = dataAry as? [String] ?? []
    routeId = ary?.firstObject ?? ""
    controller.routeZoomMap(withRouteIdList: ary, selectedRID: routeId)
}) { (code, msg) in
    //길 찾기 실패 처리
}
…
…
…
// 주행 안내 시작
controller.runGuidance(withRouteID: routeId)
// 모의 주행 시작
controller.startSimulation(withRouteID: routeId)
```

- 출발지/목적지/경유지를 좌표가 아니라 소지번 명칭 문자열로 전달한다("건물I" -> "건물A", 경유지 "건물B","건물C","건물D").
- 호출은 `runShiRoute(_:goalItem:viaList:...)`로 쓰였으나 Reference의 시그니처 라벨은 `goalName:`이다. 원본 내부 불일치. ^[ambiguous]
- 함수 설명은 [[inavi-sdk-ios-guide-shi-edition-differences]].

## Related
- [[inavi-sdk-ios-guide-hub]] — iOS 가이드 목차
- [[inavi-sdk-ios-controller-reference]] — 예시에서 호출하는 함수의 정의
- [[orbis-sdk]] — 프로젝트 개요
- [[navisdk-api-coverage-and-domestic-sdk-guide]] — 국내 SDK 가이드

## Sources
- Confluence "iNavi SDK iOS 개발 가이드" (pageId 305201307) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "iNavi SDK iOS 개발 가이드 - SHI" (pageId 305201319) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
