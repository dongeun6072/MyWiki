---
title: >-
    NaviSDK_Core 작업 이력 2025-10 ~ 2026-09
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
    navisdk_core(글로벌 내비게이션 SDK) 본인 커밋 314건(2025-10 ~ 2026-09)의 주제별 이력. 커밋 메시지 기준이며 diff는 검증하지 않았다.
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

# NaviSDK_Core 작업 이력 2025-10 ~ 2026-09

본인이 작성한 `navisdk_core` 저장소(글로벌 내비게이션 SDK, 로컬 `global-inavi-navigation-sdk-android`) 커밋 314건(2025-10 ~ 2026-09)을 주제별로 묶은 이력이다. 전체 허브는 [[navisdk-core-commit-history]], 프로젝트 개요는 [[orbis-sdk]], 같은 기간 스프린트 연표는 [[navisdk-confluence-sprint-timeline-2024-2026]]을 본다.

> [!warning] 커밋 메시지 기준, diff 미검증
> 이 페이지는 커밋 메시지만 근거로 한 요약이다. 메시지와 실제 변경이 다를 수 있다. 주제 분류는 메시지 키워드와 이슈 키로 한 1차 분류라 경계 사례가 있고 ^[inferred], 대상을 알 수 없는 커밋은 따로 모았다 ^[ambiguous]. 각 항목의 해시로 `git show <해시>`를 실행해 확인한다. 동기와 효과는 메시지에 있는 것만 적었다. 서버 포트와 숨은 기능 진입 방법 등 보안 대상 값은 원본에서도 가렸다.

## 기간 개요

커밋 메시지상 2025-10~2026-09 구간에는 총 314건이 있다. 월별 건수는 2025-10 44건, 2025-11 66건, 2025-12 51건, 2026-01 40건, 2026-02 4건, 2026-03 34건, 2026-04 9건, 2026-05 9건, 2026-06 47건, 2026-07 9건, 2026-09 1건이며, 2026-08은 0건이다.
2025-10~2026-01에는 국내향 엔진 제거, iOS 지도·카메라·현위치 구현, TTS, 의존성 업그레이드, v1.0.0/v1.0.1 릴리즈 관련 작업이 많고, 2026-02는 4건으로 줄었다. 2026-03에는 트럭·MapMatch, 네트워크 리팩토링, 빌드·AI 도구 관련 작업이 있고, 2026-06에는 NSDK-739~744 계열(인증 Style, 다국어, 에러 처리 일원화)이 집중되어 있다.

(모든 내용은 커밋 메시지만 근거이며 diff·코드는 확인하지 않았다.)

## 1. 국내향 엔진·Flavor 제거 및 후속 정리 (NSDK-565/566/569) (23건)

- 기간: 2025-10~2025-11

커밋 메시지상 2025-10-30에 NSDK-565로 ProductFlavors, 국내향 엔진(Bank, Smr, Vorbis, 국내향 Mapmatch) 및 so 파일 제거와 Maps 서브모듈로의 Orbis 로직 이관 작업이 집중적으로 있고, 이어 NSDK-566에서 불필요한 Data Class·MMCInfo 변환 로직·공용 UI Data 제거 작업이 있다. NSDK-569에서는 iOS OrbisMapMatcher 주입, 네트워크 응답 gzip 처리, OrbisGuidance 싱글톤 생성 실패 수정 관련 작업이 있다. 그 외 Maps 서브모듈의 Mapmatch 의존성 제거 1건이 있다.

- 이슈 키: [NSDK-565], [NSDK-566], [NSDK-569]

대표 커밋:
- `c3e77950` (2025-10-30) NSDK-565 Orbis 관련 로직을 -> Maps 서브모듈로 이관, Orbis 및 Inavi 서브모듈 삭제 (Maps 서브모듈이 이제 Orbis 모듈 역할을 진행)
- `3a1c86ee` (2025-10-30) NSDK-565 Orbis Maps와 Inavi Maps를 관리하는 ProductFlavors 전체 제거
- `3c75dae0` (2025-10-30) NSDK-565 Core에서 사용한 엔진 전체 제거 (Bank, Smr, Vorbis, 국내향 Mapmatch)
- `eea3bb67` (2025-10-30) NSDK-565 국내향 MapMatch so 제거
- `b8a9e708` (2025-11-03) NSDK-566 불필요한 MMCInfo 변환 로직 전체 제거 (맵매칭에서 받은 데이터 그대로 사용)
- `f7ee95dd` (2025-11-06) NSDK-569 IOS Network 응답 시 content-Encoding 값이 gzip으로 응답받아 String을 못 읽는 문제 수정

## 2. 경로선·경로선택·경유지·TBT 표출 (29건)

- 기간: 2025-10~2026-01

커밋 메시지상 NSDK-545(안내 시작 후 경유지 추가 모의주행, RoutePtItem 필드 추가), NSDK-552(경로선택 시 경로선 전체 표출·색상 변경), NSDK-563(Route Layer 로직 Factory 이동, 경로 취소/재탐색 시 경로선 애니메이션 정리), NSDK-573(방향성 탐색)과 차기/차차기 TBT·회전교차로·터널 아이콘 대응, 스타일 재설정 시 경로 재표출(NSDK-601) 관련 작업이 있다. 2025-10에 집중되어 있고 2025-12~2026-01에 iOS 재탐색·전체경로 카메라 관련 수정이 일부 있다.

- 이슈 키: [NSDK-545], [NSDK-552], [NSDK-553], [NSDK-563], [NSDK-573], [NSDK-601]

대표 커밋:
- `9dd8e9c7` (2025-10-01) NSDK-545 안내 시작 후 경유지 추가를 이용하여 모의주행 진행 시, 처음 안내 시작 한 경로로 모의주행되는 문제 수정
- `46dc4622` (2025-10-01) NSDK-545 안내시작 후 경유지 추가를 통해 모의주행 시, 기존경로 삭제를 알려주는 팝업 표출
- `9d637a94` (2025-10-13) NSDK-552 경로선택 목적지 부근 표출 사양 제거 및 탐색 결과에 대한 경로선 전체 표출
- `7fd382d8` (2025-10-14) NSDK-552 경로 선택에 따른 경로선 색상 변경 추가
- `ee041109` (2025-11-07) NSDK-573 방향성 탐색 추가 (목적지 방향성 옵션은 항상 적용, 출발지는 재 탐색시에만 적용)
- `cccd257c` (2025-10-27) NSDK-563 경로 취소 시, 이전에 동작하던 경로 Animation 전체 취소. 재탐색 시 지나간 경로 Line 튀는 현상 수정

## 3. 지도 UI·마커·카메라·현위치·제스처 (70건)

- 기간: 2025-10~2026-05

커밋 메시지상 2025-11~12에 NSDK-575(iOS 지도 표출 InvMapFragment), 586(UIController·클릭/롱클릭/이동 리스너·제스처 판단), 574(iOS 현위치 아이콘·TrackingMode), 584(마커), 585(카메라·줌·패딩), 595(Viewmode별 패딩·공용 카메라·현위치 동작) 관련 작업이 이어진다. 이후 NSDK-610 커스텀 CompassView, 스타일 재설정 시 마커 재표출(NSDK-601), iOS heading/tilt/ZoomLevel, 패딩·SafeArea 등 수정이 2026-01까지 있고, 2026-05에 ALL_COMPONENT hide 토글 수정이 1건 있다.

- 이슈 키: [NSDK-574], [NSDK-575], [NSDK-584], [NSDK-585], [NSDK-586], [NSDK-595], [NSDK-601], [NSDK-610]

대표 커밋:
- `b32b52a1` (2025-11-10) NSDK-575 지도 표출을 위한 InvMapFragment 구현, SampleApp 지도 표출 로직 추가
- `5d347c2f` (2025-11-19) NSDK-584 마커 추가 로직 구현
- `41f52415` (2025-11-17) NSDK-574 Custom UserLocationManager 구현
- `9c956acd` (2025-11-20) NSDK-585 CameraController 연결 및 CameraPosition 구현
- `90037f30` (2025-12-01) NSDK-595 지도 이동 시 현위치 아이콘이 따라 움직이는 이슈 수정, 지도 이동 시에는 카메라 동작하지 않도록 수정
- `5d0a2ed0` (2025-12-31) NSDK-610 Custom CompassView 구현

## 4. TTS·효과음 (7건)

- 기간: 2025-12~2025-12

커밋 메시지상 2025-12에 NSDK-582(Common 영역 TTS 컨트롤러, 음성 발성 로직, iOS AudioFocus, LanguageCode 기반 음성 설정)와 NSDK-597(효과음 기능 추가), TTS 종료 시 효과음 타이밍 수정 관련 작업이 있다.

- 이슈 키: [NSDK-582], [NSDK-597]

대표 커밋:
- `1406223d` (2025-12-03) NSDK-582 TTS 구현을 위해 Common 영역에 컨트롤러 구현, Android 에서 적용했던 발성 사양 적용
- `0a7f52da` (2025-12-04) NSDK-582 음성 발성 로직 추가
- `4292b0a8` (2025-12-08) NSDK-582 ios AudioFocus 동작 적용
- `3519e819` (2025-12-16) NSDK-597 효과음 기능 추가
- `4cc5c320` (2025-12-18) [iOS] TTS 발성이 끝날때 효과음이 나올때, 효과음 타이밍이 밀리는 현상 수정

## 5. Geocode·검색 요청 (7건)

- 기간: 2025-10~2026-01

커밋 메시지상 NSDK-550에서 Geocode·ReverseGeocode Response Wrapper 클래스를 도입하는 작업이 2025-10에 있고, NSDK-598/599에서 Genesis·Orbis 검색 요청 로직을 추가하거나 검색 타입에 따라 분기하는 작업이 2025-12에 있다. 2026-01에는 SDK 초기화 전 요청 시 Fail을 전달하는 변경이 1건 있다.

- 이슈 키: [NSDK-550], [NSDK-598], [NSDK-599]

대표 커밋:
- `d7755930` (2025-10-02) NSDK-550 Geocode Response Wrapper 클래스 생성
- `66e669f3` (2025-12-09) NSDK-598 Genesis 검색 API 검토를 위해, 요청 로직 추가
- `11851418` (2025-12-09) NSDK-598 키보드 검색 버튼 클릭 시 Genesis 검색, 최근검색어 클릭 시 Orbis 검색 진행
- `cc779d16` (2025-12-22) NSDK-599 검색 타입에 따라, Genesis/Orbis 검색 요청 로직 반영
- `dd79a886` (2026-01-13) RunSearch, RunRoute, Geocode, Reverse Geocode 요청 시 SDK 초기화가 안되어있으면 Fail 전달

## 6. 다국어·이미지 리소스 (9건)

- 기간: 2025-10~2026-03

커밋 메시지상 번역본 리소스 적용, 프로그래스 문구 다국어 적용, 이미지 리소스 추가, 과속 표출 이미지 추가, iOS Localization 국가 추가 등 리소스 관련 작업이 2025-10~12에 있다. 2026-02에 Android UI 모듈의 이미지 참조 이슈 수정, 2026-03에 가이드 이미지 교체·비율 조정(mkdocs) 작업이 있다.

대표 커밋:
- `55fe2869` (2025-11-04) 번역본 리소스 적용 v1.0
- `8983ab79` (2025-11-04) 앱 초기 표출되는 프로그래스 문구 다국어 적용
- `7fbeac1c` (2025-10-16) 과속 속도 표출 이미지 5단위로 추가
- `df36de70` (2025-12-08) [iOS] Localization 국가 추가
- `667e8ca9` (2026-03-11) 가이드 이미지 교체 260311

## 7. SDK 초기화·ServiceGate·헤더·대만향 설정 (23건)

- 기간: 2025-11~2026-07

커밋 메시지상 NSDK-599에서 ServiceGate 요청 로직의 초기화 UseCase 이동과 API Key 요청·DataStore 저장 작업이 있고, 대만향 플래그/설정 변경, SDK 초기화 플래그, 인증 요청의 인자 제거와 AppKey 하드코딩 제거, 도메인·App Key 변경(NSDK-650), serviceType 헤더 추가가 있다. 2026-06~07에는 NSDK-744(요청 헤더 mapVer 추가)와 NSDK-757(공통 헤더 framework_type 추가·flutter 고정) 관련 작업이 있다.

- 이슈 키: [NSDK-575], [NSDK-599], [AIR-599], [NSDK-601], [NSDK-606], [NSDK-647], [NSDK-650], [NSDK-744], [NSDK-757]

대표 커밋:
- `5d742c97` (2025-12-19) AIR-599 ServiceGate 요청 로직 초기화 UseCase 내부로 이동, DataStore에 해당 응답 Dto 저장
- `86eb0db0` (2025-12-19) NSDK-599 SDK 초기화 로직 so TomTom API Key 요청 로직 추가,  DataStore에 해당 키 저장
- `1e709f6d` (2025-12-23) NSDK-601 카메라 요청 시 사용하는 Key 값 서버 기반으로 변경
- `13082ec6` (2026-01-29) NSDK-650 도메인 URL 변경, UMap App Key 변경
- `9132e646` (2026-07-08) ✨ [NSDK-757] 공통 헤더에 framework_type 필드 추가
- `a6ae7301` (2026-06-26) ✨ [NSDK-744] agent 서버 API 요청 헤더에 mapVer 필드 추가

## 8. 의존성·빌드 환경 업그레이드 (23건)

- 기간: 2025-10~2026-07

커밋 메시지상 NSDK-614로 2026-01 초에 Kotlin·KSP(2.1.0 -> 2.2.20), AGP/AndroidX, Kotlinx, MapLibre(Android 11.10.1 -> 12.3.1, iOS 6.19.3 -> 6.22.1) 업데이트와 Version Catalog/Bundles 리팩토링이 있다. 2026-05에는 targetSdk 35 상향·edge-to-edge 대응(NSDK-731)과 난독화 시 패키지명 유지(NSDK-732), 2026-07에 Kotlin 2.3.21 업그레이드와 증분 네이티브 컴파일 비활성화가 있다. 그 외 Moko Permission 의존성, 불필요한 라이브러리 정리가 있다.

- 이슈 키: [NSDK-560], [NSDK-614], [NSDK-731], [NSDK-732]

대표 커밋:
- `1d92af2c` (2026-01-06) NSDK-614 의존성 관리 효율화를 위한 Version Catalog 리팩토링
- `0bb7c7a9` (2026-01-06) NSDK-614 Kotlin, Ksp 버전 업데이트 (2.1.0 -> 2.2.20), Skie, moko resource 업데이트 진행
- `3423a7aa` (2026-01-06) NSDK-614 Android MapLibre 버전 업데이트 ("11.10.1" -> "12.3.1")
- `d52b6f3c` (2026-01-06) NSDK-614 iOS MapLibre 버전 업데이트 ("6.19.3" -> "6.22.1")
- `e820d8ec` (2026-05-22) 🔧 [NSDK-731] targetSdk 35 상향 및 versionName 반환타입 수정
- `39ca2964` (2026-07-03) ⬆️ Kotlin 2.3.21 및 주요 의존성 버전 업그레이드

## 9. 로그 설정·개발자 모드·서버 전환 (8건)

- 기간: 2026-01~2026-06

커밋 메시지상 NSDK-612에서 Debug 빌드가 아닌 경우 LogWriters를 Empty로 바꾸고 kermit.Logger로 통일하는 작업이 2026-01에 있다. NSDK-716에서 개발/준상용 서버 전환 기능 및 알럿 추가(진입 방법은 미수록)가 2026-05에 있고, NSDK-738에서 DevMode 로그주행 파일 선택 기능과 내장 로그 파일·공개 API 제거가 2026-06에 있다. 서버 주소는 메시지에 없다.

- 이슈 키: [NSDK-612], [NSDK-612], [NSDK-716], [NSDK-738]

대표 커밋:
- `9aaa0929` (2026-01-02) NSDK- 612 Debug 빌드가 아닌 경우, LogWriters를 Empty로 변경
- `c94b19a1` (2026-01-14) 개발자 모드가 아닌 경우에만 LogWriters를 Empty로 변경
- `1d28dd7a` (2026-05-13) NSDK-716 개발/준상용 서버 전환 기능 추가
- `59b5468c` (2026-05-15) NSDK-716 개발/준상용 서버 전환 알럿 추가 (진입 방법 미수록)
- `6e5f3084` (2026-06-09) ✨ [NSDK-738] DevMode 로그주행 파일 선택 기능 구현
- `7c8f959b` (2026-06-09) 🔥 [NSDK-738] writeDriveLogToFile 공개 API 및 내장 로그 파일 제거

## 10. 경로탐색 엔진·MapMatch·트럭 대응 (12건)

- 기간: 2025-12~2026-05

커밋 메시지상 2026-03에 NSDK-661(Android MapMatch aar 0.6.3 -> 0.6.5, iOS xcframework 교체, OrbisMapMatch.h 대응), NSDK-660(트럭향 Weight/Height/Length 요청 파라미터, 차량 제원 인터페이스), OrbisRouteLib·경로 탐색 엔진 버전 적용, MapMatch 0.6.5 Jfrog 배포 관련 작업이 있다. 2025-12에 정적 라이브러리 Push 1건, 2026-05에 fullBuild.sh의 mapmatch-aar-only 옵션 1건이 있다.

- 이슈 키: [NSDK-660], [NSDK-661]

대표 커밋:
- `17809b09` (2026-03-12) NSDK-661 Android MapMatch aar 교체 0.6.3 -> 0.6.5
- `856304c5` (2026-03-12) NSDK-661 OrbisMapMatch.h 새로 추가된 메서드 대응
- `6d375813` (2026-03-13) NSDK-660 트럭향 Weight, Height, length Request 파라미터 대응
- `4557dac8` (2026-03-19) 경로 탐색 엔진 v1.0.1.41 적용
- `7b150978` (2026-03-24) OrbisRouteLib v1.0.1.43 적용
- `b5559cf9` (2026-03-25) [AOS] MapMatch 0.6.5 Jfrog 배포

## 11. 네트워크 구조 리팩토링·에러 처리 일원화 (28건)

- 기간: 2026-03~2026-06

커밋 메시지상 2026-03~04에 NSDK-679(NetworkModule 리팩토링, RouteRepository 이관, 공통 에러 처리 함수), 682(불필요 로직 제거), 684(스트리밍 다운로드 Ktor 변경 후 iOS 비정상 종료 수정, 초기화 순서 변경), 688(Path 상수화·공통 함수 통합) 관련 작업이 있다. 2026-06에 NSDK-741로 SDK 에러 처리 일원화, InvErrorCode 1:1 매핑, 응답 이중 역직렬화 제거, ServiceGate 헤더 캐싱 복원, 에러 처리 ADR·문서 추가가 집중되어 있다.

- 이슈 키: [NSDK-679], [NSDK-682], [NSDK-684], [NSDK-688], [NSDK-741]

대표 커밋:
- `ec26d950` (2026-03-31) NSDK-679 요청 로직만 존재하는 NetworkModule로 리팩토링 진행
- `b79b7bfe` (2026-03-31) NSDK-679 경로탐색 및 DTO 변환을 처리하는 RouteRepository로 이관
- `33fc753d` (2026-04-02) NSDK-684 스트리밍 다운로드 Ktor로 변경하면서 발생한 iOS 비정상 종료 이슈 수정
- `5bf6d31b` (2026-06-18) ♻️ [NSDK-741] 공통 SDK 에러 처리 구조 일원화
- `5a732236` (2026-06-19) ♻️ [NSDK-741] 응답 코드별 InvErrorCode 1:1 매핑으로 세분화
- `9fe93364` (2026-06-19) ⚡ [NSDK-741] ServiceGate 헤더 캐싱 복원으로 요청마다 재생성 제거

## 12. 인증 Style 적용·지도 다국어·교통색상 경로 (23건)

- 기간: 2026-06~2026-06

커밋 메시지상 2026-06에 NSDK-739(인증 응답 Style URL 기반 지도 스타일 적용, MapHelper 제거, AUTH_STYLE_URL_INVALID(1008) 추가, imapsResult 저장), NSDK-740(스타일 기반 지도 다국어, setLanguage API, iOS 공개 API), NSDK-743(경로 변경 시 교통색상 미반영·링크 데이터 없을 때 경로 사라짐 수정) 관련 작업이 있다. MapTheme 변경 시 화살표 수정과 playground의 지도 모드/언어 버튼 추가도 포함된다.

- 이슈 키: [NSDK-739], [NSDK-740], [NSDK-743]

대표 커밋:
- `8fa99e78` (2026-06-11) 🔥 [NSDK-739] MapHelper 제거 및 인증 응답 Style URL 기반 지도 스타일 적용
- `43fd8eac` (2026-06-11) ✨ [NSDK-739] 인증 응답에 Style URL 검증 추가
- `bb7bb414` (2026-06-11) ✨ [NSDK-739] Style URL 누락 전용 에러코드 AUTH_STYLE_URL_INVALID(1008) 추가
- `d06aa75d` (2026-06-12) ✨ [NSDK-740] 스타일 기반 지도 다국어 적용 및 setLanguage API 추가
- `c6997a1e` (2026-06-12) 🐛 [NSDK-740] AUTO 언어 적용 시 디바이스 언어 live 조회로 수정
- `2298fd17` (2026-06-22) 🐛 [NSDK-743] 경로 변경 시 교통색상 미반영 수정

## 13. 빌드·배포·문서·AI 도구 (26건)

- 기간: 2026-02~2026-07

커밋 메시지상 2026-03에 NSDK-678(FullBuild.sh, iOS SPM 서브모듈 추가, 문서 빌드), Bitbucket MCP·code-reviewer Skill·Claude 설정 관련 작업이 있고, Android API reference 동기화와 README 추가가 있다. 2026-06에는 설계 문서를 wiki 서브모듈로 이전하고 이후 wiki 서브모듈 포인터를 갱신하는 커밋이 반복되며, 로그주행 설계/계획 문서 추가, FileManager rootPath 접근제한자 변경 1건, v1.0.4 배포 산출물 포인터 갱신이 있다.

- 이슈 키: [NSDK-678]

대표 커밋:
- `d6334796` (2026-03-27) NSDK-678 FullBuild.sh 추가 및 통합 빌드 문서화
- `9e112252` (2026-03-27) NSDK-678 iOS Spm repo 서브모듈로 추가
- `581e1c98` (2026-03-27) add: Bitbucket MCP 추가
- `4fa23164` (2026-03-31) code-reviewer Skill 추가
- `3d137a27` (2026-06-19) 🚚 설계 문서를 wiki 서브모듈로 이전
- `ae512300` (2026-05-22) Android API reference Sync 1.0.3

## 14. 버전·릴리즈 업데이트 (21건)

- 기간: 2025-10~2026-09

커밋 메시지상 버전코드(0.1.7 -> 0.1.16 계열)를 반복적으로 올리는 커밋이 2025-10~12에 있고, 2026-01-07 v1.0.0, 2026-01-29 v1.0.1, 2026-03-13 1.0.2, 2026-07-15 1.0.4 릴리즈 버전 업데이트가 있다. UMap·Playground 앱 버전 업데이트와 서브모듈 업데이트, iOS 버전코드(Core/UI) 갱신이 포함된다.

대표 커밋:
- `cebe8ff8` (2026-01-07) Release 버전 업데이트 v1.0.0
- `f09cf47a` (2026-01-29) Release Version 업데이트 v1.0.1
- `90826e29` (2026-01-29) UMap 버전 업데이트 (0.1.16 -> 1.0.1, 24 -> 25)
- `5547f560` (2026-03-13) 릴리즈 버전 업데이트 (1.0.1 -> 1.0.2)
- `9950c222` (2026-07-15) ReleaseVersion 업데이트 (1.0.3 -> 1.0.4)
- `a6aeddbb` (2026-09-08) aos-playground 앱 버전 업데이트 (1.0.3 -> 1.0.4)

## 모호한 커밋 (5건)

대상을 알 수 없는 메시지("Android 빌드 안되는 문제 수정", "null 예외처리 안되어있는 부분 수정", "Import 누락된 부분 추가", "임시 Push" 등)로, 커밋 메시지만으로는 변경 대상을 특정할 수 없다.

- `a38e3e5b` (2026-04-01) null 예외처리 안되어있는 부분 수정
- `5a7975a8` (2026-01-23) Android 빌드 안되는 문제 수정
- `7a343c85` (2025-11-14) [iOS] Import 누락된 부분 추가
- `154e4abb` (2025-11-06) NSDK-569 Android 빌드 안되는 문제 수정
- `373edbf7` (2025-10-01) NSDK-545 임시 Push

검산: 주제별 건수 합 = 23 + 29 + 70 + 7 + 7 + 9 + 23 + 23 + 8 + 12 + 28 + 23 + 26 + 21 + 모호 5 = 314 = 전체 건수 314

## Sources

- 원본 커밋 목록: [[_raw/_archived/Bitbucket_navisdk_core_커밋목록_dongeun]] (해시|날짜|메시지)
- 저장소: Bitbucket `mobility-tech/navisdk_core`, 필터 `--author` 본인, merge·stash 제외
