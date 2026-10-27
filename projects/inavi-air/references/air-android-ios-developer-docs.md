---
title: >-
    아이나비 에어 Android/iOS 개발 문서
category: references
project: inavi-air
tags: [air, android, ios, onboarding, libraries, visibility/internal]
aliases: [Android Documentation, iOS Documentation, Documents, API Documentation, 에어 개발 문서]
relationships:
  - target: "[[inavi-air]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/205029460
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/205029509
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/205029377
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/205029415
summary: >-
    에어 앱 Android/iOS 프로젝트 정보, 라이브러리와 용도, 세팅, 테스트 배포 도구, 기여 가이드(이미지/엔진/파일명/로그파일), 내부 배포 시나리오, 문서 허브 구조 정리.
provenance:
  extracted: 0.90
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T13:00:00+09:00
updated: 2026-10-26T13:00:00+09:00
---

# 아이나비 에어 Android/iOS 개발 문서

2023~2024년에 작성된 에어 앱 개발자용 온보딩 문서 모음이다. Android(2023-08-04 수정), iOS(2024-03-27 수정), 상위 `Documents` 페이지(2026-05-21 수정)를 한 곳에 옮겼다. 테스트 도구 사용법은 [[air-testing-guide]], 앱 개요는 [[inavi-air]], 목차는 [[air-internal-docs-and-integration-hub]]를 본다.

## 상위 Documents 페이지 구조

`Documents`는 개발 문서 허브 역할을 하며 다음 항목을 안내한다.

- **환경 설정**: Android는 Android Studio, JDK, Android SDK. iOS는 최신 Xcode, Swift, iOS SDK. 자세한 방법은 각 플랫폼의 Setting Guide로 연결.
- **기여 가이드라인**: 프로젝트 파일 추가, 코딩 스타일 등은 Contribution Guide(Android/iOS)를 따른다.
- **API 문서**: 프로젝트에서 쓰는 모든 API 설명은 `API Documentation` 페이지로 연결. 그 페이지 본문은 링크 항목뿐이다(내용 없음).
- **테스팅 방법**: 테스트 케이스 실행과 추가 방법은 Testing Guide(공통)를 참조 ([[air-testing-guide]]).
- 하단에 "내부 문서" 레이블별 콘텐츠 매크로 자리표시자가 있다.

그 외 같은 스페이스의 `iNavi AIR App to App Guide`(2023-12-26 수정)와 `iNavi SDK in-App Guide (신규페이지 확인후 제거 예정)`(archived)는 제목 외 본문이 없는 빈 페이지다. 외부 연동 규격은 [[air-external-integration-android-spec]], [[air-external-integration-ios-spec]]를 본다.

## Android

### 프로젝트 정보

| 항목 | 값 |
|---|---|
| TARGET SDK | 33 |
| MIN SDK | 23 |
| 저장소 | Bitbucket(주소 미수록) |
| 의존성 관리 | Gradle |

### 라이브러리

| 라이브러리 | 용도 |
|---|---|
| `CashButton` | 별도 인앱 결제나 추가 광고 지면 없이 리워드 서비스를 제공하는 SDK ([[air-cash-reward-design-2023-2024]]) |
| `Firebase/Analytics`, `Crashlytics`, `Messaging`, `DynamicLinks` | 사용자 분석, 충돌 리포팅, 메시지·알림, 딥 링크 생성 |
| `gson` | 자바 객체를 JSON으로 변환 |
| `KakaoSDKUser` | 카카오 로그인 및 사용자 관리 |
| `KakaoAdfit` | 카카오 광고 시스템(매체 광고 수익 공유) |
| `Lottie-AOS` | JSON 기반 애니메이션 표현 |
| `Glide` | 이미지 로딩 |
| `Junit` | 단위 테스트 |
| `CarApp` | Android Auto 개발용 자동차 앱 라이브러리 |

### 세팅 가이드

1. 저장소에서 코드를 내려받는다(ssh 또는 HTTP로 `git clone`, 주소 미수록).

### 테스트

- 사내 테스트 앱 배포는 **AppTester**를 사용하며, 다른 Android 개발자에게 초대를 요청한다.

### 기여 가이드

**이미지 추가**
- `develop` 브랜치에서 이미지를 추가하고, 이미지가 필요한 브랜치에서 develop을 merge해 가져간다.
- 이미지를 교체할 때는 폴더를 통째로 복사해 붙이지 말고 폴더 안의 파일들을 복사해 붙인다(폴더째 붙이면 이미지가 교체되지 않는 문제가 있음).

**엔진 추가**
- MMC, DP, 안내 등 엔진을 적용하려면 보통 디버그용과 기본용 2개를 적용한다.
- AOS 엔진 적용 순서
  1. 엔진을 배포한 담당자에게 파일을 받는다.
  2. 받은 Obj(디버그) 파일과 libs(기본)를 소스에 적용한다.
     - Obj → `app/src/main/obj/~`
     - libs → `app/src/main/jinLibis/~`
- 디버그/기본 구분이 어렵다면 용량으로 확인한다(Debug가 기본보다 용량이 매우 크다).

### 배포 가이드(내부 배포 시나리오)

Develop 브랜치에 모든 기능 개발이 끝난 상태에서 진행한다.

1. Air Develop 브랜치에 버전 업데이트를 push한다. Android Studio에서 `build.gradle`의 VersionName, VersionCode를 수정한다. 예: `"03.05.29"` → `"03.05.30"`, `301337` → `301338`.
2. 사내 Jenkins 대시보드에서 에어 릴리즈 업로드(Firebase) 잡 페이지로 이동한다.
3. 구성 페이지의 Branch Specifier가 `*/develop`인지 확인하고 저장한다.
4. Build Now로 빌드한다.
5. 빌드 후 Firebase App Distribution으로 이동한다.
6. 올린 VersionName/VersionCode 항목을 클릭해 테스터와 출시 노트를 작성한다.
7. Slack 에어 채널에 내부 배포 완료를 공유한다.

특정 브랜치 작업을 빌드하려면 Branch Specifier를 바꾼다. 예: `*/feature/AIR-1284-aos-신규폰트-적용`.

"출시 노트 작성 가이드" 소제목은 있으나 본문이 비어 있다.

## iOS

### 프로젝트 정보

| 항목 | 값 |
|---|---|
| MINIMUM DEPLOYMENTS | 13.0 |
| 저장소 | Bitbucket(주소 미수록) |
| 의존성 관리 | CocoaPods. Podfile에서 모든 의존성 확인, `pod install`로 설치 |

### 라이브러리

| 라이브러리 | 용도 |
|---|---|
| DP 엔진, 검색 엔진, MMC 엔진, 안내 엔진 | 에어 내장 네비게이션 엔진 4종(원문에는 이름만 나열) |
| `AFNetworking` | iOS/macOS 네트워킹 |
| `Reachability` | 네트워크 상태 모니터링 |
| `ZipArchive` | zip 압축/해제 |
| `TBXML` | 경량 XML 파서 |
| `Masonry`, `SnapKit` | Auto Layout 프레임워크 |
| `Firebase/Analytics`, `Crashlytics`, `Core`, `Messaging`, `DynamicLinks` | 사용자 분석, 충돌 리포팅, 메시지·알림, 딥 링크 |
| `GoogleSignIn`, `Google-Mobile-Ads-SDK` | Google 로그인, Google 광고 |
| `RxSwift`, `RxCocoa`, `RxGesture`, `ReactorKit` | 리액티브 프로그래밍(이벤트 기반 비동기) |
| `DynamicBlurView` | 뷰 동적 블러 |
| `Alamofire` | Swift HTTP 네트워킹 |
| `BetterCodable` | Codable 사용 편의 |
| `Kingfisher` | 웹 이미지 다운로드/캐시 |
| `lottie-ios` | After Effects 애니메이션 렌더링 |
| `FloatingPanel` | Floating Panel UI |
| `AdFitSDK` | 다음 모바일 광고 네트워크 AdFit |
| `KakaoSDKCommon`, `KakaoSDKAuth`, `KakaoSDKUser` | 카카오 로그인 및 사용자 관리 |

### 세팅 가이드

1. 저장소에서 코드를 내려받는다(ssh 또는 HTTP, 주소 미수록).
2. CocoaPods 라이브러리를 `pod install`로 내려받는다.

### 테스트

- **TestFlight**를 사용하며 다른 iOS 개발자에게 초대를 요청한다.

### 기여 가이드

**파일 추가: 파일명** — 관련 회사명(이니셜)을 접두어로 붙인다. 예: `Inv`(아이나비), `TW`(팅크웨어), `KT`.

**이미지**
- `develop` 브랜치에서 추가하고 필요한 브랜치에서 develop을 merge한다.
- 이미지를 일괄 교체한 뒤 기존 이미지의 `Contents.json`은 commit하지 말고 원상태로 복구(discard)해 신규 이미지의 `Contents.json`만 추가되게 한다.

**로그파일**
- 로그파일을 다운받을 수 없을 때는 가진 로그파일을 앱에 직접 넣는다. iExplorer나 iMazing 같은 macOS 앱을 쓰면 편하다.
- 위치: 아이나비 에어(App) > Documents > inaviair > inavidata > GpsLog 폴더. 폴더가 없으면 앱에서 로그 다운로드를 시도(숨은 기능 입력, 미수록)해 생성한다.

### CarPlay / Dashboard

주행·지도 관련 작업은 앱뿐 아니라 CarPlay와 Dashboard에서도 정상 표출·실행되는지 확인해야 한다. 이미지 해상도나 레이아웃 관련 별도 처리 로직이 있는 부분이 존재한다.

## 원본에 있으나 옮기지 않은 항목

- 저장소 clone 주소, 내부 Jenkins 주소(원본에 있음, 미수록)

## Related
- [[air-testing-guide]] — DHU, CarPlay, GPS 로그, Push 테스트
- [[inavi-air]] — 에어 앱 개요
- [[air-cash-reward-design-2023-2024]] — CashButton 리워드 설계
- [[air-internal-docs-and-integration-hub]] — 이 묶음 목차

## Sources
- Confluence "Android Documentation" (pageId 205029460) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "iOS Documentation" (pageId 205029509) — 동일
- Confluence "Documents" (pageId 205029377) — 동일
- Confluence "API Documentation" (pageId 205029415) — 동일, 링크뿐인 빈 페이지
