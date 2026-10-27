---
title: >-
    iNavi SDK Android 개발 가이드 SHI(삼성중공업) 사본 차이점
category: references
project: orbis-sdk
tags: [navisdk, android, shi, customer-edition, visibility/internal]
aliases: [iNavi SDK Android 개발 가이드-SHI, 삼성중공업 SDK, 소지번 길찾기, INaviShiMember]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[navisdk-api-coverage-and-domestic-sdk-guide]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/304906843 305430571
summary: >-
    고객사용 SHI 사본과 원본 가이드의 차이: 별도 버전(0.0.1~1.0.8), setShiMember/소지번 길찾기, 관제데이터, 의존성 아티팩트, 문구 차이.
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

# iNavi SDK Android 개발 가이드 SHI(삼성중공업) 사본 차이점

"iNavi SDK Android 개발 가이드-SHI"는 삼성중공업(SHI)에 제공한 고객사용 사본이다. 본문 구조(개요, 세팅, 권한, 시나리오, INaviController/Interface/Structure/Define Reference, 코드 표)는 원본과 같고, SHI 전용 기능과 별도 개정이력이 추가되어 있다. 공통 내용은 [[inavi-sdk-android-setup-and-permissions]] 등 다른 페이지에 한 번만 적었고 여기서는 차이만 정리한다. 허브: [[inavi-sdk-android-guide-hub]]. 원본 개정이력은 [[inavi-sdk-android-revision-history]].

## 1. 개정이력 (SHI 전용 버전 체계)
| 버전 | 날짜 | 변경 |
|---|---|---|
| 0.0.1 | 2023-07-13 | 초안 문서 작성 |
| 1.0.0 | 2023-08-03 | 사용자 정보 입력 인터페이스 추가(`setShiMember`, `INaviShiMember`), 소지번 길찾기 인터페이스 추가(`runShiRoute`, `runSingleShiRoute`) |
| 1.0.1 | 2023-08-11 | 경로탐색 사양 변경(출발지 소지번 ID를 찾지 못했을 경우 현위치 기준 탐색) |
| 1.0.2 | 2023-08-19 | 내부 모듈 안정성 개선 |
| 1.0.3 | 2023-08-31 | POI Data 수정, AndroidX 적용(`playground-service-location` 16.0.0 → 21.0.1, fusedLocationProvider 관련), 음성 안내 수정(4톤 이하 차량 20km 구간 음성 발성 로직 반영), 최초 실행 시 경로탐색 실패하는 문제 수정 |
| 1.0.4 | 2023-10-05 | **SDK 저장소 URL 변경(필수 적용)**, UI 표출 속도와 관제데이터 속도가 안 맞는 문제 수정, 경유지를 가지 않고 경로대로 가는 경우 경유지가 삭제 처리되던 문제 수정, 경로 이탈 후 1회만 관제데이터에 이탈 표시를 전달하도록 수정 |
| 1.0.5 | 2023-10-12 | 중량별 회피탐색 기능 추가 |
| 1.0.6 | 2023-11-10 | 경로 주행 중 동일위치 주행 시 지나간 경로가 다시 그려지는 문제 수정, 차종 승용(00) 설정 시 속도제한이 표시되지 않던 문제 수정 |
| 1.0.7 | 2023-11-22 | 관제데이터 항목 추가(TimeStamp), 과속여부 조건 변경(20 → 21 / 30 → 31) |
| 1.0.8 | 2024-01-11 | 일단정지구역 안내 추가, 관제데이터 전송 시점 변경(20초 → 10초) |

- SHI 사본에는 원본의 0.0.x~0.6.x 개정이력이 들어 있지 않다. SHI 1.x가 원본의 어느 버전을 기반으로 하는지는 문서에 없으나 1.0.3의 AndroidX 적용 시점이 원본 0.6.0과 같은 2023-08-31이다 ^[inferred]
- 관제데이터(차량 운행 정보를 관제 쪽으로 보내는 기능)는 SHI 개정이력에만 등장하며, API 문서에는 상세 설명이 없다(원문에 상세 설명 없음).

## 2. 개발 환경/세팅 차이
| 항목 | 원본 | SHI 사본 |
|---|---|---|
| minSdkVersion 서술 | 21 (Android 5.0) | 21 + "0.0.21 이하 버전: minSdkVersion 19 (Android 4.4, KITKAT OS)" 줄 추가 |
| 저장소 주석 | "기존 저장소 변경, SDK 버전 상관 없이 반드시 해당 URL 적용 필요" | "2023.10.31 이후 기존 저장소 변경, SDK 버전 상관 없이 반드시 아래 URL 적용 필요" (URL 값은 미수록) |
| SDK 의존성 | `com.inavisys.navisdk:inavi-navigation-sdk:version` | `com.inavisys.navisdk:inavi-navigation-sdk-shi:1.0.7` (SHI 전용 아티팩트, 예시 버전 1.0.7) |
| 의존성 주석 | "SDK 의존성" | "SDK 의존성 추가" |
| play-services-location | v0.6.0 이하 16.0.0 / v0.6.0부터 `21.0.01` | v1.0.2 이하 16.0.0 / v1.0.3 이후 `21.0.1` (원본의 `21.0.01`과 표기 차이) |
| `android.useAndroidX=true` | "SDK v0.6.0 부터 필수" | "SDK v1.0.3 부터 필수" |

그 외 Gradle abiFilters, 컴파일 옵션, Manifest(cleartext, apache http legacy, AppKey), proguard, Layout, 권한 목록은 원본과 동일하다([[inavi-sdk-android-setup-and-permissions]]). 개요 문장 끝 어미("기술 문서 이다" → "기술 문서이다"), 일부 코드 주석 들여쓰기 같은 사소한 표기 차이도 있다.

## 3. 시나리오 예시 차이
SHI 사본은 시나리오 번호가 다르다. 원본 1(초기화) 뒤에 SHI 전용 2개가 끼어들어 이후 번호가 2씩 밀린다.

| SHI 번호 | 내용 |
|---|---|
| 1 | 초기화 (원본과 동일) |
| 2 | **삼성중공업 사용자 정보 입력** (SHI 신규) |
| 3 | **삼성중공업 소지번 길찾기 → 안내 시작** (SHI 신규) |
| 4 | 지도 아이콘 표출 및 제거 (원본 2) |
| 5 | 검색 (원본 3) |
| 6 | 길 찾기, 안내시작 (원본 4) |
| 7 | 주행중 경유지 변경 재 탐색 (원본 5) |
| 8 | 안전운행정보 안내 변경 (원본 6) |
| 9 | 화물차 전용 옵션 적용 (원본 7) |
| 10 | 차종 설정 (원본 8) |
| 11 | 지도 여백 적용 (원본 9) |
| 12 | TurnView 배경색 변경 (원본 10) |
| (번호 1) | 확대도 표출 (원본 11; 원문에서 번호가 다시 1로 시작) |
| (번호 1) | 가장 가까운 좌표 얻기 (원본 12) |

### 2번: 사용자 정보 입력 예시
```kotlin
val member = INaviShiMember(userId = "<사용자ID>", drvrTon = "01");
INaviController.setShiMember(member)
```
- 원문 예시는 테스트용 사용자 ID 문자열과 `drvrTon = "01"`을 쓴다. ID 값은 옮기지 않고 자리표시자로 대체했다.

### 3번: 소지번 길찾기 예시
```kotlin
// 출발지, 목적지 소지번
var startPoint:  "정문"
var goalPoint:  "작업장A"
//경유지
var viaList = mutableListOf<String>()
viaList.add("작업장B")
// 부가정보
var extraInfo: RouteExtraInfo
// 안내시작에 사용할 경로
var routeID: String = ""
// 길찾기에 사용할 탐색 옵션
val optionType = mutableListOf<ROUTEOPTIONTYPE>()
optionType.add(ROUTEOPTIONTYPE.HIGHWAYPRIOTY)
optionType.add(ROUTEOPTIONTYPE.MOTOCYCLE)
// 길 찾기 시작 및 결과 Callback 처리
INaviController.runShiRoute( startPoint, goalPoint, viaList, optionType, extraInfo, object : OnRouteMultiListener {
    override fun onSuccess(result : ArrayList<String>, same: Boolean ) {
        // 안내시작에 사용할 경로 ID 저장
        routeID = result[0]
        // 모든 경로에 맞춰 스케일 되며, param 에 맞는 경로는 select 상태가 됨
        INaviController.routeZoomMap(result, routeID)
    }
    override fun onFail(errCode: Int, errMsg: String ) {
        // 길 찾기 실패 처리
    }
})
// 주행 안내 시작
INaviController.runGuidance(routeID)
// 모의 주행 시작
INaviController.startSimulation(routeID)
```
- "소지번"은 사업장(조선소) 내부 구역/지점 명칭 체계를 가리키는 말로 보이며 명칭 문자열로 출발/도착/경유를 지정한다 ^[inferred]

## 4. INaviController Reference 차이

### 4.1 초기화 파트에 추가: setShiMember (8번째 항목)
```kotlin
fun setShiMember(member : INaviShiMember)
```
- 설명: 삼성중공업 사용자 데이터 설정
- Param: `INaviShiMember` 객체 / Return: void

### 4.2 길찾기 파트에 추가: runShiRoute, runSingleShiRoute
```kotlin
fun runShiRoute(start: String?, goal: String, viaList: List<String>?, optionType: List<ROUTEOPTIONTYPE>?, extraInfo: RouteExtraInfo?, listener: OnRouteMultiListener)
```
- 설명: 길 찾기(멀티 경로)

| 파라미터 | 설명 |
|---|---|
| start | 출발지 소지번 명칭(없을 시 현위치 기준 탐색) |
| goal | 목적지 소지번 명칭 |
| viaList | 경유지 소지번 명칭 리스트(최대 100개) |
| optionType | 탐색 옵션 정보(Default 옵션 사용 시 null 입력) |
| extraInfo | 부가정보(필요 없을 시 null 입력) |
| listener | 탐색 결과(경로 ID) 리스트 반환 |
- Return: void

```kotlin
fun runSingleShiRoute(start: String?, goal: String, viaList: List<String>?, optionType: ROUTEOPTIONTYPE, extraInfo: RouteExtraInfo?, listener: OnRouteSingleListener)
```
- 설명: 길 찾기(단일 경로). 파라미터는 `runShiRoute`와 같고 listener는 `OnRouteSingleListener { onSuccess(result: String); onFail(errCode: Int, msg: String) }`로 단일 탐색 결과(경로 ID)를 반환한다. Return: void
- 이 두 함수가 추가되어 이후 길찾기 함수 번호가 밀린다(runReRouteChangeVia 5번 ... cancelRoute 11번).

### 4.3 화물차 옵션 setCarWeight 표기 오류
SHI 사본의 `setCarWeight` 레퍼런스는 파라미터명이 `nHeight`로 잘못 적혀 있다(원본은 `nWeight`).
```kotlin
fun setCarWeight(nHeight: Int) : Boolean   // SHI 사본 표기, 의미는 차량 중량(kg) 0 ~ 60000
```
- 동작은 동일하며 표기 오류로 판단한다 ^[inferred]

## 5. Structure Reference 차이
- `NaviEvent.eventType`의 `NAVIEVENTTYPE` 표기에서 원본은 링크가 걸려 있고 SHI는 링크 없는 텍스트이다(내용 동일).
- SHI에만 있는 11번째 구조체:
```kotlin
class INaviShiMember(
    var userId : String
    var drvrTon : String // 00(승용), 01(승합[4톤미만]), 02(승합[4톤이상])
)
```

| 필드 | 설명 |
|---|---|
| userId | 사용자 ID 문자열 |
| drvrTon | 운전 차량 구분 코드: 00 승용, 01 승합(4톤 미만), 02 승합(4톤 이상) |

- 개정이력 1.0.6의 "차종 승용(00)"은 이 `drvrTon` 값을 가리킨다 ^[inferred]
- 1.0.3의 "4톤이하 차량 20km 구간 음성 발성 로직"과 1.0.5의 "중량별 회피탐색"도 이 차량 구분과 관련된 변경으로 보인다 ^[inferred]

## 6. 그대로 같은 부분
- 개정이력을 제외한 SDK Interface 규칙(생명주기, Singleton, 좌표계), 권한 목록, Interface Reference(Listener 12종), Define Reference(enum 14종), 코드 표 전체는 동일하다([[inavi-sdk-android-interface-structure-define-reference]], [[inavi-sdk-android-error-codes]]).
- SHI 사본에는 원본의 INaviController 전 함수가 그대로 있으며(deprecated 표기 포함) 추가분만 위 4절과 같다.

## Related
- [[inavi-sdk-android-guide-hub]] — 이 가이드 묶음 목차
- [[inavi-sdk-android-revision-history]] — 원본 개정이력
- [[navisdk-api-coverage-and-domestic-sdk-guide]] — 국내 SDK 가이드 개요
- [[orbis-sdk]] — SDK 프로젝트 허브

## Sources
- Confluence "iNavi SDK Android 개발 가이드-SHI" (pageId 304906843) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "iNavi SDK Android 개발 가이드" (pageId 305430571) — 비교 기준 원본, 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
