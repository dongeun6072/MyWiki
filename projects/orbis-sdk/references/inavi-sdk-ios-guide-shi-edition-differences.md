---
title: >-
    iNavi SDK iOS 개발 가이드 SHI 사본과 원본의 차이점
category: references
project: orbis-sdk
tags: [ios, sdk, shi, customer-edition, visibility/internal]
aliases: [iNavi SDK iOS 개발 가이드 - SHI, 삼성중공업 SDK iOS, inavi-navigation-sdk-shi]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[navisdk-api-coverage-and-domestic-sdk-guide]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/305201319
summary: >-
    삼성중공업(SHI)용 iOS SDK 가이드가 일반 가이드와 다른 점: 0.0.5~1.0.6 개정이력(2023-07~2024-01), 전용 CocoaPods, setShiMember/runShiRoute/runSingleShiRoute 추가, 예시 2개 추가.
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

# iNavi SDK iOS 개발 가이드 SHI 사본과 원본의 차이점

"iNavi SDK iOS 개발 가이드 - SHI"는 고객사(약어 SHI, 문서에서 "삼성중공업 멤버 데이터"로 풀이됨)에 제공한 iOS SDK 가이드 사본이다. 본문 대부분이 일반 가이드와 같고, 아래 차이만 있다. 공통 본문은 [[inavi-sdk-ios-guide-setup]], [[inavi-sdk-ios-controller-reference]], [[inavi-sdk-ios-structures-defines-and-codes]]에 한 번만 적었다. 목차: [[inavi-sdk-ios-guide-hub]]. SDK 전반: [[navisdk-api-coverage-and-domestic-sdk-guide]], [[orbis-sdk]].

## 1. 개정이력 (SHI 사본)

일반 가이드의 0.0.1~0.0.4 이력은 SHI 사본에 없고, 0.0.5부터 시작한다(0.0.4까지는 일반 가이드에 기록된 이력과 같은 SDK 계보로 보인다). ^[inferred]

| 버전 | 날짜 | 내용 |
|---|---|---|
| 0.0.5 | 2023-07-12 | SHI 전용 CocoaPods 추가, SHI 인증 기능 적용 |
| 1.0.0 | 2023-08-03 | 사용자 정보 입력 인터페이스 추가(`setShiMember`, `INaviShiMember`), 소지번 명칭 탐색 인터페이스 추가(`runShiRoute`, `runSingleShiRoute`), 길찾기 경유지 입력 추가 |
| 1.0.0 | 2023-08-25 | 초기화 성공 여부 callback 시나리오 예시 추가 (버전 번호 동일, 원본 그대로) |
| 1.0.1 | 2023-08-31 | 음성 안내 수정(4톤 이하 차량 20km 구간 음성 발성 로직 반영), 최초 실행 시 경로탐색 실패 문제 수정 |
| 1.0.2 | 2023-10-05 | 경유지를 가지 않고 경로대로 가는 경우 경유지가 삭제 처리되던 문제 수정, 경로 이탈 후 1회만 관제데이터에 이탈 표시를 전달하도록 수정 |
| 1.0.3 | 2023-10-12 | 중량별 회피탐색 기능 추가 |
| 1.0.4 | 2023-11-10 | 경로 주행 중 동일 위치를 주행할 경우 지나간 경로가 다시 그려지는 문제 수정 |
| 1.0.5 | 2023-11-22 | 관제데이터 항목 추가(TimeStamp), 과속 여부 조건 변경(20 -> 21, 30 -> 31), 지도 주기 겹치는 현상 수정 |
| 1.0.6 | 2024-01-11 | 일단정지구역 안내 추가, 관제데이터 전송 시점 변경(20초 -> 10초) |

개정 이력에서 알 수 있는 SHI 기능 특성: 차량 톤수 구분(`drvrTon`)에 따른 음성/회피탐색, 관제 서버로 보내는 관제데이터(이탈 표시, TimeStamp, 전송 주기), 구내 소지번 명칭 기반 경로 탐색, 일단정지구역 안내. 과속 판정 임계값이 20 -> 21, 30 -> 31로 바뀐 것은 "초과"를 엄밀히 적용한 변경으로 보인다. ^[inferred]

## 2. CocoaPods 이름

| 항목 | 일반 | SHI |
|---|---|---|
| Podfile | `pod 'inavi-navigation-sdk'` | `pod 'inavi-navigation-sdk-shi'` |
| 캐시 삭제 | `pod cache clean inavi-navigation-sdk` | `pod cache clean inavi-navigation-sdk-shi` |
| 업데이트 | `pod update inavi-navigation-sdk` | `pod update inavi-navigation-sdk-shi` |

`pod install –repo-update`는 동일하다. 개발 환경(Xcode, Objective-C/Swift, iOS 13), 필수 권한(Background Mode, plist), Layout 추가 방법도 동일하다.

## 3. 추가된 INaviController 함수

SHI 사본은 INaviController Reference의 영역 번호가 하나씩 밀린다: 1 초기화, **2 사용자 정보 등록(신규)**, 3 지도 컨트롤, 4 통합 검색, 5 길 찾기, 6 주행, 7 기타. 길 찾기 영역에서도 `runShiRoute`, `runSingleShiRoute`가 3, 4번으로 끼어들어 `makeRouteSumInfo` 이후 번호가 +2 된다. 나머지 함수의 시그니처와 설명은 일반 가이드와 동일하다.

### setShiMember

```swift
func setShiMember(_ member: INaviShiMember)
```

- Description: 삼성중공업 멤버 데이터 설정
- Param: `member` = `INaviShiMember` 객체
- Return: void
- `INaviShiMember` 필드: `userId`(NSString, 사용자 ID), `drvrTon`(NSString, 00 승용 / 01 승합(4톤 미만) / 02 승합(4톤 이상)). 구조체 정의는 [[inavi-sdk-ios-structures-defines-and-codes]].

### runShiRoute (소지번 명칭 멀티 경로)

```swift
func runRoute(_ startName: String?, goalName: String, viaList:[String]? ,
successHandler: @escaping INaviRouteMultiSuccessHandler, failHandler:
@escaping INaviFailHandler)
```

- Description: 길 찾기 (멀티 경로)
- Param: `startName` = 출발지 소지번 명칭, `goalName` = 목적지 소지번 명칭, `viaList` = 경유지 소지번 명칭 리스트(최대 100개), `successHandler` = 탐색 성공 Handler, `failHandler` = 탐색 실패 Handler (실패 코드는 코드 표 참고)
- Return: void
- 소제목은 `runShiRoute`이지만 코드 블록의 함수명은 `runRoute`로 적혀 있다(원본 표기 불일치). 오버로드로 구분하는 것인지 실제 심볼명이 `runShiRoute`인지 원문만으로는 확정할 수 없다. ^[ambiguous]

### runSingleShiRoute (소지번 명칭 단일 경로)

```swift
func runSingleRoute(_ startItem: String?, goalItem: String, viaList:[String]?,
routeOption opt: INVRouteOptionType, successHandler: @escaping
INaviRouteSingleSuccessHandler, failHandler: @escaping INaviFailHandler)
```

- Description: 길 찾기 (단일 경로)
- Param: `startName` = 출발지 소지번 명칭, `goalName` = 목적지 소지번 명칭, `viaList` = 경유지 소지번 명칭 리스트(최대 100개), `opt` = 탐색 옵션 정보(`INVRouteOptionType`), `successHandler`, `failHandler`
- Return: void
- 마찬가지로 소제목 `runSingleShiRoute`와 코드 블록 `runSingleRoute`가 다르고, Param 설명의 이름(`startName`, `goalName`)과 시그니처 라벨(`startItem`, `goalItem`)도 어긋난다. ^[ambiguous]

## 4. 추가된 시나리오 예시

일반 가이드의 시나리오 1~4(초기화, 지도 아이콘, 검색, 길 찾기)에 더해 다음 2개가 추가된다. 코드는 [[inavi-sdk-ios-swift-scenarios]]에 있다.

5. 삼성중공업 사용자 정보 입력 (`INaviShiMember` 생성, `userId`, `drvrTon`, `setShiMember`)
6. 삼성중공업 소지번 길 찾기 -> 안내 시작(모의 주행 시작) (`runShiRoute`에 "건물I" -> "건물A", 경유지 3개 전달 후 `routeZoomMap`, `runGuidance`, `startSimulation`)

## 5. 같은 점 (확인 사항)

- 개요, Appkey 발급 안내, 개발 환경, 배포 형식(CocoaPods), SDK 필수 권한, Layout 추가, SDK Interface 규칙(싱글턴, Delegate/Block, 위경도 DD), Structure/Define Reference, 코드 표는 일반 가이드와 동일하다.
- 일반 가이드의 `INaviShiMember` 구조체는 원래부터 일반 가이드의 Structure Reference에도 정의되어 있다.
- 일반 가이드에만 있고 SHI 사본에서 빠진 내용은 개정이력 0.0.1~0.0.4뿐이다.

## Related
- [[inavi-sdk-ios-guide-hub]] — iOS 가이드 목차
- [[inavi-sdk-ios-controller-reference]] — 공통 함수 정의
- [[orbis-sdk]] — 프로젝트 개요
- [[navisdk-api-coverage-and-domestic-sdk-guide]] — 국내 SDK 가이드

## Sources
- Confluence "iNavi SDK iOS 개발 가이드 - SHI" (pageId 305201319) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- 공통 본문 비교 기준: Confluence "iNavi SDK iOS 개발 가이드" (pageId 305201307)
