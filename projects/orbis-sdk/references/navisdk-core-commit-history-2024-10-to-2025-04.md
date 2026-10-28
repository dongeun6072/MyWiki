---
title: >-
    NaviSDK_Core 작업 이력 2024-10 ~ 2025-04
category: references
project: orbis-sdk
tags: [orbis-sdk, navisdk, android, kmp, bitbucket, commit-history, visibility/internal]
relationships:
  - target: "[[navisdk-core-commit-history]]"
    type: related_to
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[navisdk-confluence-sprint-timeline-2024-2026]]"
    type: related_to
sources:
  - repo:bitbucket/mobility-tech/navisdk_core
summary: >-
    navisdk_core(글로벌 내비게이션 SDK) 본인 커밋 315건(2024-10 ~ 2025-04)의 주제별 이력. 커밋 메시지 기준이며 diff는 검증하지 않았다.
provenance:
  extracted: 0.85
  inferred: 0.12
  ambiguous: 0.03
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-10-28
tier: supporting
created: 2026-10-28T10:00:00+09:00
updated: 2026-10-28T10:00:00+09:00
snapshots:
  - "[[_raw/_archived/Bitbucket_navisdk_core_커밋목록_dongeun|Bitbucket_navisdk_core_커밋목록_dongeun]]"
---

# NaviSDK_Core 작업 이력 2024-10 ~ 2025-04

본인이 작성한 `navisdk_core` 저장소(글로벌 내비게이션 SDK, 로컬 `global-inavi-navigation-sdk-android`) 커밋 315건(2024-10 ~ 2025-04)을 주제별로 묶은 이력이다. 전체 허브는 [[navisdk-core-commit-history]], 프로젝트 개요는 [[orbis-sdk]], 같은 기간 스프린트 연표는 [[navisdk-confluence-sprint-timeline-2024-2026]]을 본다.

> [!warning] 커밋 메시지 기준, diff 미검증
> 이 페이지는 커밋 메시지만 근거로 한 요약이다. 메시지와 실제 변경이 다를 수 있다. 주제 분류는 메시지 키워드와 이슈 키로 한 1차 분류라 경계 사례가 있고 ^[inferred], 대상을 알 수 없는 커밋은 따로 모았다 ^[ambiguous]. 각 항목의 해시로 `git show <해시>`를 실행해 확인한다. 동기와 효과는 메시지에 있는 것만 적었다. 서버 포트와 숨은 기능 진입 방법 등 보안 대상 값은 원본에서도 가렸다.

## 기간 개요
커밋 메시지 기준으로 2024-10~2025-04에 총 315건이 있다. 월별로는 2024-10 12건, 2024-11 50건, 2024-12 48건, 2025-01 56건, 2025-02 40건, 2025-03 30건, 2025-04 79건이다. 커밋 메시지상 초반(2024-10~12)에는 배포 설정, 네이티브 엔진 모듈 인터페이스, 초기 인증, 권한, 경로 탐색 UseCase 관련 작업이 있고, 2025-01~02에는 MMC/GPS 모듈 공통화, 모의주행, 안내 엔진 연동과 TBT UI 관련 작업이 있다. 2025-03~04에는 서브 모듈 분리, 지도 인터페이스(OrbisMap/TomTom), 경로선택 GUI 관련 작업이 많다. 2024-11·2025-01·2025-04에는 같은 메시지가 해시만 달리 반복된 커밋도 있으며, 모두 별개 건수로 셌다.

## 1. Artifactory 배포 및 appkey 로드 (13건)
- 기간: 2024-10~2025-04
- 요약: Artifactory 게시 Gradle 플러그인, 로컬 Maven 업로드, ArtifactId, README 배포 명령, 초기 appkey 로드 AOS 인터페이스 관련 작업이 있다. 2025-04의 README 아티팩트 경로 수정 1건도 포함했다. 커밋 메시지상 관련 작업이 13건 있다.
- 이슈 키: [NSDK-243], [NSDK-244]
- 대표 커밋:
  - `433f85f` (2024-10-23) NSDK-244 로컬 Maven 저장소에 라이브러리 업로드하는 로직 추가
  - `7da8524` (2024-10-23) NSDK-244 ArtifactoryGradlePlugin 추가
  - `e9483d9` (2024-10-24) NSDK-244 ArtifactId 수정
  - `cbfd7c8` (2024-10-24) NSDK-244 Artifactory 게시 로직 추가
  - `a7a5834` (2024-10-30) NSDK-243 초기 appkey 로드 하는 부분 AOS 인터페이스 구성
  - `5ed2a39` (2025-04-15) README 수정 (아티팩트 경로)

## 2. 네이티브 엔진 모듈 인터페이스 정의 (NSDK-264) (28건)
- 기간: 2024-11~2024-11
- 요약: 커밋 메시지상 SGuidance, NativeAdmin, Natives(MMC), SMR, DP, 음성 모듈의 인터페이스 추가와 Android 구현체 정의, 안내엔진 JNI와 Data Class 구성, NaviBank 인스턴스·경로 변경, jar 이동 관련 작업이 있다. 같은 메시지가 해시만 달리 쌍으로 반복되는 경우가 많다. 커밋 메시지상 관련 작업이 28건 있다.
- 이슈 키: [NSDK-264]
- 대표 커밋:
  - `e1405c6` (2024-11-11) NSDK-264 안내엔진 JNI 추가 및 필요한 Data Class 구성
  - `d6439da` (2024-11-12) NSDK-264 Import 코드정리
  - `20f4c39` (2024-11-12) NSDK-264 Guidance Data Class, Common 영역으로 이동
  - `26f6228` (2024-11-13) NSDK-264 NaviBank 경로 변경
  - `81c43b4` (2024-11-15) NSDK-264 음성 모듈 인터페이스 추가
  - `2d275c4` (2024-11-18) NSDK-264 음성 모듈 인터페이스 Model, Repository 분리

## 3. 초기 인증 플로우 (NSDK-272) (21건)
- 기간: 2024-11~2024-11
- 요약: SDKAuth API 인증, ClauseAgree(이용약관) API, ServiceGate 인터페이스·재요청, InitStatus 콜백, DeviceInfo/DeviceID, 초기화 UseCase 분리 관련 작업이 있다. 커밋 메시지상 관련 작업이 21건 있다.
- 이슈 키: [NSDK-272]
- 대표 커밋:
  - `d8715ab` (2024-11-22) NSDK-272 초기 인증 플로우 진행 시, 에러코드 및 예외 케이스를 위해 InitStatus 추가
  - `de8403e` (2024-11-25) NSDK-272 초기 인증 로직 분리 작업 진행 (UseCase)
  - `76047c1` (2024-11-25) NSDK-272 Network 모듈에서, SDK 인증 요청은 별도로 요청하도록 분리
  - `16ec447` (2024-11-27) NSDK-272 UseCase 매개변수에 요청 파라미터 추가하도록 변경
  - `b9cb1a0` (2024-11-28) NSDK-272 DeviceInfo에 Debug 판단 플래그 추가
  - `1cdd085` (2024-11-29) NSDK-272 초기화 Usecase 분리 (Navi 초기화, SDK 초기화)

## 4. 권한 요청 처리 (NSDK-259, 283) (10건)
- 기간: 2024-12~2025-01
- 요약: Moko Permission 라이브러리 추가, 권한 요청 UseCase와 플랫폼별 Repository/Source, AndroidMain Manifest 권한, Coarse Location 권한 확인, iOS Permission Controller 연결, PermissionUsecase 정리 관련 작업이 있다. 커밋 메시지상 관련 작업이 10건 있다.
- 이슈 키: [NSDK-259], [NSDK-283]
- 대표 커밋:
  - `560dd27` (2024-12-03) NSDK-259 PermissionSource를 플랫폼 별 구현 후 주입하는 방식으로 변경
  - `ac6e62c` (2024-12-03) NSDK-259 Permission Repository 구현 및 Event Class 정의
  - `3aa27e2` (2024-12-04) NSDK-283 AndroidMain Manifest 생성 후 권한 추가
  - `5f8e030` (2024-12-04) NSDK-259 호출 예시 코드 구현, 조건부 권한 추가
  - `e72026c` (2024-12-05) NSDK-283 AOS 플랫폼에서 PermissionController 연동, 테스트 코드 추가
  - `4ea990b` (2025-01-23) [공통] PermissionUsecase 소스 정리

## 5. 경로 탐색 요청 및 RouteBuffer 파싱 (NSDK-292, 305) (16건)
- 기간: 2024-12~2025-02
- 요약: 일반 경로 탐색 요청/응답 파라미터와 UseCase·Repository 정의, RouteBuffer 다운로드·파싱, httpClient 생성, 응답 Null 파싱 수정, 검색 정규화 LonLat 변환 값 오류 수정 관련 작업이 있다. 커밋 메시지상 관련 작업이 16건 있다.
- 이슈 키: [NSDK-292], [NSDK-305]
- 대표 커밋:
  - `70a7576` (2024-12-11) NSDK-292 일반 경로 탐색 Usecase 및 Repository 정의
  - `333d34d` (2024-12-11) NSDK-292 일반 경로 탐색 요청 파라미터 정의
  - `c8b0d26` (2024-12-13) NSDK-292 응답값중 Null 이 들어오는 경우 파싱이 안되는 문제가 있어 수정
  - `cd6115f` (2024-12-16) NSDK-292 RouteBuffer 파싱 로직 추가, DP RouteLine 테스트 로직 구현
  - `b71e271` (2024-12-24) NSDK-305 RouteBuffer 파싱 로직 UseCase 구현하여 테스트 로직 수정
  - `e69fe76` (2025-02-20) [공통] 검색 정규화에서 아이나비 LonLat 변환 시 값 오류 수정

## 6. DI(Koin)·라이브러리 로드·샘플 앱·모듈 구성 (NSDK-297, 298, 304) (24건)
- 기간: 2024-12~2025-01
- 요약: So 파일 이동, Koin 실행·DI 관리 클래스, Library Load UseCase, Android 샘플(Demo) 앱과 navisdk_aos_ui 모듈 추가, aar 빌드 오류 수정, 모듈 이름 변경(navisdk, navisdk-core, navisdk-aos-ui, aos-playground), README와 iosBuild 스크립트 수정 관련 작업이 있다. 커밋 메시지상 관련 작업이 24건 있다.
- 이슈 키: [NSDK-297], [NSDK-298], [NSDK-304]
- 대표 커밋:
  - `d8e6545` (2024-12-16) NSDK-297 Common, AndroidMain 영역으로 So 파일 이동
  - `0516ae8` (2024-12-17) NSDK-297 Platform, InaviController 제거 및 소스정리
  - `ea36317` (2024-12-17) NSDK-297 DI 관리를 위해 관리 Class 추가
  - `6e06be8` (2024-12-18) NSDK-298 AndroidSample (Demo App) 모듈 추가
  - `792d199` (2024-12-19) NSDK-304 aar 빌드 테스트 중 오류 발생하는 부분 수정 (DeviceInfoObj)
  - `8254892` (2025-01-02) [AOS] 사용하지 않는 App 삭제

## 7. MMC·GPS·Gravity 모듈 공통화 (NSDK-314, 322, 323, 329, 336) (40건)
- 기간: 2025-01~2025-02
- 요약: GPSModule, MMCModule, GravityModule, MMCOptionManager 등을 Kotlin으로 변환·공통 모듈화하는 작업, atomicfu 동기화, NMEA/위치 업데이트 Dispatcher 이슈 수정, MMC CheckDevice·Init 사양 변경, MMC 값 설정 지연 수정 관련 작업이 있다. 커밋 메시지상 관련 작업이 40건 있다.
- 이슈 키: [NSDK-314], [NSDK-322], [NSDK-323], [NSDK-329], [NSDK-336]
- 대표 커밋:
  - `e4405e3` (2025-01-02) [공통] _MMCInfo 필요없는 파라미터 제거
  - `6370913` (2025-01-07) NSDK-314 Java에서 Kotlin Data 클래스로 변경되면서, 인스턴스를 바로 생성 할 수 없어 Default 값 추가
  - `3890463` (2025-01-10) NSDK-314 MMC 임시 테스트를 위해 Push
  - `71e9a0d` (2025-01-13) NSDK-314 테스트 코드 원복
  - `19c47af` (2025-01-17) [공통] MMC Init 사양 Air와 동일하게 변경
  - `5345687` (2025-02-26) [공통] GPSModule requestLocation 함수 로직 중 잘못 사용하는 부분이 있어 수정

## 8. 모의주행 및 NaviController (NSDK-337, 339) (12건)
- 기간: 2025-01~2025-01
- 요약: NaviController 모의주행 테스트, AddRouteLine, 지나온 경로선 문제 수정, MMCInfo 변경 시 지도 중심·차량 위치 갱신, 모의주행 취소·종료 로직, Intro 영역 추가, DI 모듈 분리 관련 작업이 있다. 커밋 메시지상 관련 작업이 12건 있다.
- 이슈 키: [NSDK-337], [NSDK-339]
- 대표 커밋:
  - `668d647` (2025-01-21) NSDK-337 모의주행 취소 로직 추가
  - `d91d80e` (2025-01-21) NSDK-337 모의주행 시 지나온 경로선이 사라지지 않는 문제 수정
  - `4811aa2` (2025-01-21) NSDK-337 MMCInfo가 변경될 때 마다 MapCenter 및 SetCarPos 변경하는 로직 추가
  - `1bc77ce` (2025-01-22) NSDK-337 ViewAngle Default 값 세팅
  - `35d1b18` (2025-01-22) NSDK-337 Intro 영역 추가
  - `6137d5e` (2025-01-23) [공통] 모의주행 종료 로직 변경 및 일부 예외처리 추가

## 9. DP 인터페이스·폰트·리소스·문자열 정리 (NSDK-309, 358) (13건)
- 기간: 2025-01~2025-02
- 요약: DP 엔진 인터페이스 구현체 현행화, Android 폰트 로드와 Moko Resource 폰트·Colors, 문자열·확장함수·거리 변환 로직 파일 정리, 불필요 리소스 제거 관련 작업이 있다. 커밋 메시지상 관련 작업이 13건 있다.
- 이슈 키: [NSDK-309], [NSDK-358]
- 대표 커밋:
  - `5073520` (2025-01-02) NSDK-309 Android 폰트 가져오는 로직 추가 및 DP 세팅
  - `b75904a` (2025-01-02) NSDK-309 DP 엔진 인터페이스 구현체 IOS와 동일하게 현행화 진행
  - `bc4cd5b` (2025-02-19) [AOS] Font 가져오는 부분 리팩토링
  - `8eba138` (2025-02-21) NSDK-358 StringExtension 제거, Dist 변환 로직 DistanceParse 폴더로 변경
  - `7bb562f` (2025-02-25) NSDK-358 소스 정리
  - `4439719` (2025-02-25) [공용] Moko-Resources Colors 추가 및 경로선 파란색으로 변경

## 10. 안내 엔진 연동과 TBT UI (NSDK-346, 355, 419) (19건)
- 기간: 2025-02~2025-04
- 요약: 안내 엔진 통합용 Guidance 파일 생성, 차기·차차기 TurnInfo 데이터 확인, NaviTextView, 차기/차차기 TBT UI 구현과 모의주행 표출 테스트, aos-ui를 라이브러리 모듈로 변경, 2025-04 Orbis TBT용 RootView·TurnView·NextTurnView 추가 관련 작업이 있다. 커밋 메시지상 관련 작업이 19건 있다.
- 이슈 키: [NSDK-346], [NSDK-355], [NSDK-419]
- 대표 커밋:
  - `6f1c3be` (2025-02-11) NSDK-346 DummyGSV 값 수정
  - `c0e7df7` (2025-02-11) NSDK-346 안내 엔진 통합을 위해 Guidance 파일 생성 및 일부 초기화 로직 구현
  - `96c10a5` (2025-02-13) NSDK-355 테스트를 위해 임시 TurnView 표출 로직 추가
  - `2677f54` (2025-02-13) NSDK-346 차기 차차기 데이터 확인 로직 추가
  - `c43f63e` (2025-02-14) NSDK-355 임시로 Font 추가하여 Custom TextView 테스트
  - `a12e255` (2025-04-30) NSDK-419 Orbis TBT 구현을 위해 RootView 및 TurnView, NextTurnView 컴포넌트 추가

## 11. ColorLaneView 표출 (NSDK-357) (7건)
- 기간: 2025-02~2025-02
- 요약: 차기·차차기 View에 ColorLaneView 추가, LaneColor 이미지 리소스, 상속 구조 제거, UiState 파라미터와 Observe 등록, 안내엔진 Company 값 변경 관련 작업이 있다. 커밋 메시지상 관련 작업이 7건 있다.
- 이슈 키: [NSDK-357]
- 대표 커밋:
  - `27af66d` (2025-02-17) NSDK-357 차기, 차차기 View에 ColorLaneView 추가
  - `0e267d9` (2025-02-17) NSDK-357 LaneColor 이미지 리소스 추가
  - `c6a0106` (2025-02-19) NSDK-357 ColorLaneView 상속 구조 제거
  - `94280d5` (2025-02-25) NSDK-357 안내엔진 초기화 시 Company 값 변경
  - `265f5e3` (2025-02-26) NSDK-357 ColorLaneView 표출 테스트를 위해 목적지 변경
  - `c5c5e9a` (2025-02-26) NSDK-357 TBTView에 ColorLaneView 표출되도록 Observe 등록

## 12. 서브 모듈 분리와 프로젝트 구조 개편 (NSDK-400, 418 등) (42건)
- 기간: 2025-03~2025-04
- 요약: Common·Utils·Model·Core·Maps 서브 모듈 생성과 클래스 이동·이름 변경, 의존성·버전 변수 정리, Voice 로직 제거, Gradle Plugin 8.9/Gradle 8.11.1 업데이트, 프로젝트·폴더명 변경, airmaps.aar 이동, xcframework 출력 경로 변경, 2025-04 orbisroute·MapMatch·Guidance 모듈로 로직 이동(NSDK-418) 관련 작업이 있다. 커밋 메시지상 관련 작업이 42건 있다.
- 이슈 키: [NSDK-400], [NSDK-418]
- 대표 커밋:
  - `0e84c91` (2025-03-18) [공통] navisdk-core 내 maps 서브 모듈 생성
  - `79bb090` (2025-03-20) Common, Util 서브 모듈 생성 및 Common 서브모듈에 필요한 Class 이동
  - `ef44cca` (2025-04-08) NSDK-400 Common에서 사용하고 있는 Model 클래스들을 Model 서브 모듈로 일부 이동
  - `0872807` (2025-04-14) common 서브 모듈 , Core로 이름 변경
  - `2e6923b` (2025-04-15) SDK Project 파일명을 navisdk-core에서 navisdk로 변경
  - `a98631c` (2025-04-30) NSDK-418 MapMatch 모듈 생성 및 초기화 로직 구현

## 13. 지도 인터페이스(MapIF)와 OrbisMap/TomTom 연동 (NSDK-393) (22건)
- 기간: 2024-11~2025-04
- 요약: MapIF 인터페이스를 OrbisMap/Inavi 구분 없이 구성, OrbisMap 전용 IF와 User Location 기능, TomTom SDK·TomTomMap 의존성, Flavor별 호출 분기, NaviMapView 통합과 MapComponent 상속 제거, NaviMap Interface MapOverlay 반환 함수 관련 작업이 있다. 커밋 메시지상 관련 작업이 22건 있다.
- 이슈 키: [NSDK-393]
- 대표 커밋:
  - `6fe8311` (2024-11-21) MapView 구조 검토를 위해, NaviMapView, MapViewModel, UIController 생성
  - `ddb3bf5` (2025-03-19) 테스트 로직 추가 (INaviMapIF, OrbisMapIF 2개로 진행 시)
  - `eb606a8` (2025-03-27) NSDK-393 OrbisMap Interface 로직 일부 구현
  - `30b367c` (2025-03-28) NSDK-393 OrbisMap 전용 IF 추가 및 공통 함수 부분 구현
  - `10be92f` (2025-04-01) NSDK-393 MapIF 인터페이스 구성 시 OrbisMap, Inavi 구분 없이 사용 할 수 있도록 변경
  - `ba5f7a4` (2025-04-08) NSDK-393 필요없는 파일 제거

## 14. 경로선택 화면 GUI (NSDK-406, 415, 460) (42건)
- 기간: 2025-04~2025-04
- 요약: 경로선택 화면 Fragment/Activity와 ViewModel 연결, 경로 상세 RecyclerView, 경로선 표출·지도 패딩·zoomToFit, 소요시간·도착시간 표시, MokoResource 문자열·나인패치 이미지, 이미지 리소스·Ripple 버튼·Noto Sans 폰트 적용, 전체경로 테스트 관련 작업이 있다. 커밋 메시지상 관련 작업이 42건 있다.
- 이슈 키: [NSDK-406], [NSDK-415], [NSDK-460]
- 대표 커밋:
  - `31cd379` (2025-04-16) NSDK-406 경로선택 화면 UI 작업을 위해 Fragment 및 Activity 생성
  - `18a7994` (2025-04-18) NSDK-406 경로 상세 Recylcerview 구현
  - `f213d6f` (2025-04-23) NSDK-406 일부 UI 작업 진행
  - `6330d08` (2025-04-24) 이미지 리소스 추가 250424
  - `af2e82f` (2025-04-25) 이미지 리소스 추가 250424C
  - `6301804` (2025-04-30) [AOS] 경로선택 플로팅 버튼 Ripple 적용

## 15. 모호한 커밋 (6건)
대상을 알 수 없는 메시지("소스정리", "필요없는 로직 제거" 등) 6건이다.
- `b69ce10` (2025-01-16) [공통] 테스트 프로세스 중 필요없는 부분 제거
- `abbf5de` (2025-03-18) [공통] 필요없는 로직 제거
- `c2ecd28` (2025-03-20) 소스정리
- `9673f39` (2025-03-20) 변경된 파일 이름 원복
- `bc3be34` (2025-03-20) 필요없는 로직 제거
- `6014050` (2025-04-14) 소스 정리

## 검산
주제별 건수 합 = 전체 건수: 13 + 28 + 21 + 10 + 16 + 24 + 40 + 12 + 13 + 19 + 7 + 42 + 22 + 42 + 6 = 315 = 315 (원본 행 315)

## Sources

- 원본 커밋 목록: [[_raw/_archived/Bitbucket_navisdk_core_커밋목록_dongeun]] (해시|날짜|메시지)
- 저장소: Bitbucket `mobility-tech/navisdk_core`, 필터 `--author` 본인, merge·stash 제외
