---
title: >-
    국내향 NaviSDK 가이드와 Orbis SDK API 호환 현황
category: references
project: orbis-sdk
tags: [orbis-sdk, api, android, ios, visibility/internal]
aliases: [iNavi SDK 개발 가이드, INaviController Reference, 미 구현 항목 현황, 에어 연동 규격]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[orbis-navisdk-architecture-and-flutter-plan]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/overview
summary: >-
    국내향 iNavi SDK(Android, iOS) 개발 가이드의 구성과 INaviController API, 해외향 SDK에서의 호환·미구현 현황, 에어 앱 외부 연동 규격(Broadcast, 즉시 안내)을 정리했다.
provenance:
  extracted: 0.88
  inferred: 0.10
  ambiguous: 0.02
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T12:20:00+09:00
updated: 2026-10-26T12:20:00+09:00
---

# 국내향 NaviSDK 가이드와 Orbis SDK API 호환 현황

## 국내향 iNavi SDK 개발 가이드

Confluence에 보관된(archived) Android, iOS 가이드와 고객사(SHI)용 사본이 있다. Android 가이드는 개정 이력이 2020-01-17(0.0.1, 인증 업데이트)부터 시작한다. 구성은 다음과 같다.

- 개요, AppKey 발급, 개발 환경, SDK 세팅 방법(Android는 Proguard 난독화 예외 처리 포함), SDK 권한 목록
- 시나리오별 예시(Android는 Java/Kotlin, iOS는 Swift)
- `INaviController` Reference(약 900줄, 전체 문서에서 가장 큰 부분), SDK Interface, Structure, Define Reference, 코드 표
- 이력의 예: 주행 상태 리스너에 목적지 근접 거리 파라미터 추가(0.0.3), 길찾기 인터페이스에 `RouteExtraInfo` 추가(0.0.7), 과속 백그라운드 알림(0.0.8), 차량 속도 콜백(0.0.9), 디버그 로그 제거와 TBT UI 개선(0.0.10)

가이드의 API 영역은 초기화, 지도 컨트롤, 검색, 길찾기, 주행, 기타(볼륨, 방향, 리스너, 색상), 화물차 옵션(차 높이/중량, 유턴·좁은 길·규제 회피, 구역 제한)이다. 이 가이드는 2026-04 스크럼에서 VitePress로 이관하기로 했다 → [[navisdk-confluence-sprint-timeline-2024-2026]].

## 해외향 SDK의 API 호환 현황 (2025-08, 미 구현 항목 현황)

국내향 `INaviController` API가 해외향(Orbis) SDK에서 호환되는지 확인하고 우선순위를 정했다.

| 영역 | 적용 완료 | 아직 아님 / 검토 |
|---|---|---|
| 초기화 | `loadNaviLibrary`, `initLayout`(MapView ID), `initalizeNavi` | `setMapStyle`, `setAudioStreamType`, `setEmulatorMode`, `initLayout`(Parent View) |
| 지도 | 클릭 리스너, 현위치, 지도 위치, 줌, 뷰 모드, 아이콘 추가/삭제, 레벨, 회전, 이동 리스너, 컴포넌트 강제 숨김, 경로색 | 교통선 표시, 오버레이/아이콘 생성 등 일부는 해외향에서 불가. `setMapPadding`은 로직 검토, 폰트 크기와 주야간은 DP 검토 또는 당장 제공하지 않기로 함 |
| 검색 | `runSearch` | 추천어, 지번 주소는 불가. 전체 주소, 현재 도로명은 가능 |
| 길찾기 | `runRoute`, `cancelRoute` | 단일 경로, 경유지 변경 재탐색 등은 가능하지만 미적용. 요금과 `viaPassed` 처리는 검토 필요 |
| 주행 | `runGuidance` | 모의주행 시작/종료, 잔여 정보는 요금 데이터 검토 필요. `setGuidanceSettings`는 현재 과속 카메라 안내만 있음 |
| 기타, 화물차 | `getCurrentPos` | 나머지는 대부분 지원 가능하지만 아직 적용하지 않음 |

해외향에서 새로 추가한 함수는 `applicationInitialize`(Koin 의존성 주입과 라이브러리 로드)와 `setNaviBottomViewEventListener`/`removeNaviBottomViewEventListener`(하단 뷰 이벤트를 고객 앱의 커스텀 동작으로 대체)다.

같은 페이지의 다른 담당 항목:
- **안내**: 모의주행의 턴 앞/뒤 이동 로직(MMC 전달 코드 확인 필요), 후방 안내 음성(거리 사양은 m 단위로 개발 완료), 과속 효과음. 자차 애니메이션, 지나간 경로, 차기/차차기 경로 유도선은 개선 완료.
- **배포**: `isDebug` 판정 문제(SDK가 릴리즈 빌드여도 고객 앱이 디버그 빌드면 DEBUG로 판단), 배포 시 코드 난독화 필요.

## 에어 앱 외부 연동 규격 (Android)

아이나비 에어 앱을 외부 앱이 실행하거나 길안내를 요청하는 규격이다. 개정 이력은 1.0(2019-05-30 초안), 1.1(단순 실행, Geo Scheme), 1.2(인입 채널 필드), 1.3(2020-02, 사용 인터페이스 변경), 1.4(2024-01 문서 형태 변경), 1.5(2026-09-14, **경로 선택 화면 없이 즉시 안내**)다.

- 좌표계는 **WGS84**를 쓴다(GPS 신호와 구글 맵 같은 위치 기반 서비스와 연동하기 쉬워서).
- Android 8(Oreo) 이후 암시적 브로드캐스트가 막혀서, 통신사별로 대상 앱의 패키지명과 리시버 클래스명을 지정하는 **명시적 BroadcastReceiver 요청**을 쓴다.
- 요청 종류(`KIND`): `APP_LAUNCHING`(실행만), `ROUTE_SEARCH`(경로 검색), `DIRECT_GUIDE`(즉시 안내). 경로 요청에는 출발지/목적지의 이름과 좌표, 호출 앱 ID, 앱 스킴, 앱 OS를 담는다.
- iOS도 별도 연동 규격이 있다(App to App 가이드).

## 앱 내부 개발 문서 (에어 Android/iOS Documentation)

에어 앱 자체의 개발 문서다. Android는 target SDK 33, min SDK 23, Gradle로 의존성을 관리하고 사용 라이브러리는 캐시 버튼 SDK, Firebase(Analytics, Crashlytics, Messaging, DynamicLinks), 카카오 로그인과 광고(AdFit), Lottie, Glide, Android Auto용 CarApp이다. iOS는 최소 13.0, CocoaPods, RxSwift/ReactorKit 계열, Alamofire, Kingfisher, Lottie, FloatingPanel, 카카오 SDK와 AdFit, 엔진 4종(DP, 검색, MMC, 안내)이다. 엔진은 보통 디버그용과 기본용 2개를 함께 적용한다. 이미지는 `develop` 브랜치에서 추가하고 필요한 브랜치가 merge하며, 교체할 때는 폴더째 붙여넣지 말고 파일을 복사한다(교체가 안 되는 문제가 있어서).

테스트 가이드에는 상용↔개발 서버 전환, 개발자 모드 켜기/끄기, GPS 로그 주행, Android Auto 에뮬레이터(DHU) 설정 방법이 있다. 서버 전환과 개발자 모드 진입 방법은 값을 옮기지 않았다.

## Related

- [[inavi-air]], [[inavi-air-api-overview]], [[orbis-sdk]]

## Sources

- [Confluence: iNavi SDK Android/iOS 개발 가이드, 미 구현 항목 현황, iNavi AIR Android 연동 규격, Android/iOS Documentation, Testing Guide](https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/overview) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
