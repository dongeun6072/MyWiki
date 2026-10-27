---
title: >-
    iNavi SDK iOS 개발 가이드 - 개정이력, 개요, 설치, 권한, 레이아웃
category: references
project: orbis-sdk
tags: [ios, sdk, cocoapods, setup, visibility/internal]
aliases: [iNavi SDK iOS 개발 가이드, 아이나비 내비게이션 SDK iOS, inavi-navigation-sdk]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[navisdk-api-coverage-and-domestic-sdk-guide]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/305201307
summary: >-
    아이나비 내비게이션 SDK(iOS) 개발 가이드의 개정이력, 개요, Appkey, 개발 환경, CocoaPods 설치, 필수 권한(plist, Background Mode), 지도 Layout 추가, SDK Interface 규칙을 정리한다.
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

# iNavi SDK iOS 개발 가이드 - 개정이력, 개요, 설치, 권한, 레이아웃

iOS 앱에서 "아이나비 내비게이션 SDK"(이하 SDK)를 연동하기 위한 기술 문서의 앞부분(개정이력 ~ SDK Interface 규칙)이다. 문서는 2020년 12월에 처음 작성되어 2023년 6월에 xcframework로 개편되었고, 이 페이지는 상태가 archived인 원본이다. 함수 상세는 [[inavi-sdk-ios-controller-reference]], 구조체/enum/코드 표는 [[inavi-sdk-ios-structures-defines-and-codes]], 예시는 [[inavi-sdk-ios-swift-scenarios]], 목차는 [[inavi-sdk-ios-guide-hub]]에 있다. 국내 SDK 전반은 [[navisdk-api-coverage-and-domestic-sdk-guide]], [[orbis-sdk]]를 본다.

## 개정이력 (원본)

| 버전 | 날짜 | 내용 |
|---|---|---|
| 0.0.1 | 2020-12-07 | 인증 업데이트 추가 |
| 0.0.2 | 2020-12-18 | 기능 현행화 (기본 폰트 변경 등) |
| 0.0.3 | 2020-12-24 | 상단 TBT 레이아웃 오류 개선, 상단 SafeArea 적용 I/F 추가 |
| 0.0.4 | 2023-06-27 | xcframework 적용, 지도 미표출 오류 수정 |

고객사(SHI)용 사본은 0.0.5 이후 개정이력이 이어진다. [[inavi-sdk-ios-guide-shi-edition-differences]] 참고.

## 개요

- 본 문서는 iOS 기반 플랫폼에서 구동되는 "아이나비 내비게이션 SDK" 연동에 대한 기술 문서이다.

## Appkey 발급

- SDK를 사용하려면 먼저 Appkey 발급이 필요하다. 규격서를 제공하는 제휴 사업 담당자를 통해 별도 요청해야 한다. (Appkey 값 자체는 문서에 없고, 위키에도 수록하지 않는다.)

## 개발 환경

| 항목 | 내용 |
|---|---|
| 개발 도구 | Xcode |
| 개발 언어 | Objective-C, Swift |
| SDK 지원 범위 | iOS Deployment Target: iOS 13 |

## SDK 배포 형식

- CocoaPods

## SDK 적용 방법

### 1. Podfile 구성

SDK는 CocoaPods로 배포되므로 프로젝트의 Podfile에 SDK 의존성을 추가한다. (원본에 CocoaPods 참고 링크가 있으나 생략.)

```ruby
target 'naviSDKSample' do
  pod 'inavi-navigation-sdk'
end
```

### 2. SDK 설치

의존성 설정 후 Terminal에서 프로젝트 경로로 이동해 아래 명령으로 아이나비 지도 SDK를 설치한다.

```
$ pod install –repo-update
```

CocoaPods 캐시 삭제 및 갱신:

```
$ pod cache clean inavi-navigation-sdk
$ pod update inavi-navigation-sdk
```

## SDK 필수 권한

### 1. Background Mode 설정

- Audio, Airplay and picture in picture
- Location updates

### 2. 프로젝트 plist 설정

1. App Transport Security Settings를 `true`로 설정 (http 허용)
2. 인증을 위한 `INaviAppKey` 설정
3. 위치 권한 문구 설정

```xml
<plist version="1.0">
<dict>
...
<key>NSAppTransportSecurity</key>
	<dict>
		<key>NSAllowsArbitraryLoads</key>
		<true/>
	</dict>
<key>INaviAppKey</key>
<string>YOUR_APP_KEY</string>
<key>NSLocationTemporaryUsageDescriptionDictionary</key>
	<dict>
		<key>NaviSDKTemporary</key>
		<string>길 안내를 위해 정확한 GPS를 설정해주세요.</string>
	</dict>
<key>NSLocationWhenInUseUsageDescription</key>
<string>길 안내를 위해 GPS를 ON 하시겠습니까?</string>
...
</dict>
</plist>
```

| plist 키 | 용도 |
|---|---|
| `NSAppTransportSecurity` / `NSAllowsArbitraryLoads` = true | http 통신 허용 |
| `INaviAppKey` | SDK 인증용 Appkey (원문 예시는 `YOUR_APP_KEY` 자리표시자) |
| `NSLocationTemporaryUsageDescriptionDictionary` > `NaviSDKTemporary` | 임시 정확한 위치 권한 문구: "길 안내를 위해 정확한 GPS를 설정해주세요." |
| `NSLocationWhenInUseUsageDescription` | 위치 권한 문구: "길 안내를 위해 GPS를 ON 하시겠습니까?" |

## SDK Layout 추가

### 1. ViewController에서 지도 추가

ViewController에 `INaviMapView`를 서브 뷰로 추가하면 지도가 표출된다.

```swift
override func viewDidLoad() {
	super.viewDidLoad()
	let mapView = INaviMapView(frame: view.bounds)
	view.addSubview(mapView)
}
```

### 2. Interface Builder에서 지도 추가

XIB 또는 Storyboard 등 Interface Builder로도 지도를 표출할 수 있다. UIView를 추가하고 Custom Class를 `INaviMapView`로 설정한다.

## SDK Interface

1. AIR SDK는 `INaviController` 클래스를 통해 SDK의 모든 기능을 활용한다.
   - `INaviController`는 Singleton 객체로 어디에서든 호출할 수 있다.
   - SDK가 제공하는 Delegate와 Block을 추가해 SDK 연동 및 이벤트를 감지한다.
2. 좌표계
   - SDK 호출 시 위경도 좌표를 사용하고, DD(십진수 도) 방식을 쓴다.
   - 예: 서울역 위도 37.553173, 경도 126.972471 (원본에 지도 링크가 있었으나 생략)

## 비고

- 원본 설명에 "AIR SDK"라는 표현이 쓰였다. 아이나비 에어 앱과 같은 SDK 계열을 가리키는 것으로 보인다. ^[inferred]
- Android 가이드와 비교하면, iOS는 CocoaPods 배포와 plist 기반 권한/인증 설정을 쓰고 `INaviController` 싱글턴과 Delegate/Block 패턴으로 이벤트를 받는다는 점이 특징이다. 지도 뷰 생성도 `INaviMapView`를 직접 서브 뷰로 붙이는 방식이다.

## Related
- [[inavi-sdk-ios-guide-hub]] — iOS 가이드 전체 목차
- [[inavi-sdk-ios-controller-reference]] — INaviController 함수 레퍼런스
- [[orbis-sdk]] — Orbis SDK 프로젝트
- [[navisdk-api-coverage-and-domestic-sdk-guide]] — 국내 SDK API 범위와 가이드

## Sources
- Confluence "iNavi SDK iOS 개발 가이드" (pageId 305201307) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
