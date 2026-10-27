---
title: >-
    New NaviSDK 구조 설계와 Flutter 플러그인 계획
category: references
project: orbis-sdk
tags: [orbis-sdk, kmp, architecture, flutter, visibility/internal]
aliases: [New NaviSDK Plan, NaviSDK Flutter Plugin Plan, 상태 관리 Flow, MapsSDK 엔진 플랫폼 차이]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[kmp-cmp-adoption]]"
    type: implements
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/overview
summary: >-
    기존 국내향 NaviSDK를 제로베이스로 다시 만드는 이유와 KMP 기반 구조, UI 확장 방식, 상태 관리 규칙, AOS/iOS 엔진 API 차이, Flutter 플러그인 마일스톤을 정리했다.
provenance:
  extracted: 0.88
  inferred: 0.12
  ambiguous: 0.00
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T12:05:00+09:00
updated: 2026-10-26T12:05:00+09:00
---

# New NaviSDK 구조 설계와 Flutter 플러그인 계획

[[orbis-sdk]]의 코드 구조를 설명하는 설계 문서 4건(New NaviSDK Plan, 상태 관리 Flow, MapsSDK 엔진 플랫폼 차이점, NaviSDK Flutter Plugin Plan)을 한데 모았다. 일정은 [[navisdk-confluence-sprint-timeline-2024-2026]]에 있다.

## 왜 새로 만들었나 (New NaviSDK Plan)

수정 이력은 2024-11-07, 11-25, 12-17, 2025-03-26이다.

1. 고객사가 원하는 시나리오대로 쓰기 어렵다. 특정 UI를 숨기거나 위치를 바꾸거나 동작에 끼어들 수 없다(예: 휴게소가 있을 때만 TBT를 표시, 사용자 UI가 왼쪽이라 TBT를 오른쪽으로 옮기기).
2. 기존 SDK는 아이나비 에어에서 파생된 프로젝트라 레거시 코드가 많고 확장성을 고려하지 않았다.
3. 고객사의 멀티플랫폼(Flutter) 문의가 늘었다.

그래서 **제로베이스로 새 SDK를 만들고, 완성되면 아이나비 에어도 이 SDK로 리뉴얼**하기로 했다. 에어와 SDK의 정합성이 보장되어 유지보수 비용이 줄 것으로 기대한다. ^[inferred]

## 구조

- **공용 로직은 Kotlin 단일 모듈(KMP)**. Domain Layer에 ViewModel까지 넣어서, 커스텀 UI가 필요하면 Presentation Layer만 따로 만들고 Domain은 재사용한다. 코어는 순수 Kotlin이라 AOS와 iOS에서 같이 쓴다.
- 레이어: UseCase(모든 비즈니스 로직, Repository를 생성자 주입), Repository(로컬/원격 데이터), `NaviMapView`(공용 모듈용 expect 클래스, 실제 지도 뷰는 플랫폼에서 INavi/Orbis flavor별로 구현), `NaviViewParent`(expect/actual 패턴의 View 상위 클래스), `MapViewViewModel`(지도 컨트롤러 인터페이스, 현위치·줌·앵글·하단 뷰), `NaviViewViewModel`(TBT, 차로, 교통정보), Default UI(검색, 경로 선택 같은 페이지 단위 구현체).
- 규칙: NaviController나 ViewModel이 Repository를 직접 참조하지 않는다.
- 멀티 모듈(공통, 기능별). 예를 들어 화물차 전용 기능은 모듈로 분리해 Common SDK와 간섭 없이 만들고, 나중에 Common으로 들어와도 재사용한다. Kotlin 라이브러리만 쓰고 플랫폼 특화가 필요하면 별도 구현한다. 네트워크는 Ktor, 파일 저장은 플랫폼에서 내부 저장소 경로를 주입받아 Okio로 처리한다. 라이브러리는 toml로 관리한다.
- 제공 형태: Android `.aar`, iOS `.xcframework`, Flutter 플러그인.
- 개발 순서: 기본 구조 → 기능별 추상화 모듈 → 엔진 로드 → 지도 로드 → 기본 API(검색, 탐색, 안내) → 1차 회고 → 플랫폼별 UI와 기능 모듈. 기본 안내와 모의주행이 되는 수준에서 Flutter 플러그인을 시작한다.

## UI 확장성

- 모든 컴포넌트(또는 그룹)는 표시/숨김, 배경색 변경, 위치 지정이 된다. 같은 그룹(예: Turnview와 SubTurnView)은 따로 위치를 지정할 수 없다. 다국어를 지원한다.
- 구현 전략: 뷰 속성(`bgColor`, `isVisible` 등)을 JSON 스크립트로 정의해 주입하고, 값이 있으면 ViewModel 로직보다 우선한다. 서버에서 내려받는 방식(지도 데이터처럼 초기 다운로드에 포함)을 검토했다. 이 경우 SDK를 따로 배포하지 않고 서버에서 고객별 UI를 바꿀 수 있다.
- 지도 레이어 컴포넌트: 마커(출/목/경/높이제한), 경로선, 교차로 정보, 과속카메라. 안내 레이어 컴포넌트: 주행 속도, TBT, 차선(Laneview), 경로 진행도, 안전(Safeview), 과속 경고, 복합 교차로(ExtendView), 고속도로 뷰(휴게소, TG).

## 상태 관리 Flow

1. `UIGuideRepository`가 상태와 UI 데이터(`UIGuideData`)를 `StateFlow`로 관리한다. 상태 관리 로직은 이 Repository에서만 처리한다.
2. `NaviController`만 Repository와 각 엔진에 상태 변화를 전달하고, 상태 변경도 `NaviController`만 요청한다.
3. 각 ViewModel은 Repository의 상태를 보고 자기 View를 바꾼다.

`UIGuideData`에는 회전 정보(차기/차차기), 속도, 야간 여부, UI 모드, 경로 유무, 도로 종별, 남은 시간·거리·요금, 지역명, 도로명, 목적지/경유지명, 지도 각도/레벨, 모의주행 진행률 등이 있다. UI 모드는 일반, 안내, 지도 이동, 원탭, 모의주행 안내/지도 이동/원탭의 7가지다.

## Maps SDK 엔진 플랫폼 차이점 (AOS vs iOS)

KMP 공통 인터페이스 기준으로 DP(지도 표출) 엔진과 MMC(맵매칭) 엔진 함수를 비교했다. 결론은 "이슈 아님" 또는 "사용 안 함"이 대부분이다.

- iOS에 없는 함수는 대개 auto(Android Auto)용이다: `setFrontLine`, `getMapCenter`, `multitouch_auto`, `move_auto`, `setGuideColor`, `enableTrafficData`, `setTrafficColor`, `selectUserRoad` 등.
- 반환 타입만 다르면 KMP 쪽에서 통일했다(예: iOS가 void인 함수는 AOS에서 0 반환 고정, `zoomIn/zoomOut`은 `setMapLevel`로 대체).
- MMC의 센서, NMEA, 중력 관련 함수는 iOS에 없고 사용하지 않는다. `startLiveLogging`/`stopLiveLogging`은 iOS가 잘못 매칭되어 있었다.

## Flutter 플러그인 (국내향 NaviSDK 대상)

2026-04-01 초안, 04-22 M1 완료 후 갱신. 단일 레포(모노레포 아님)이며 `android/`(Kotlin), `ios/`(Swift), `lib/`(Dart API), `example/`(데모), `docs/`(계획, 구조, ADR, 통합 가이드)로 구성한다. Native SDK는 Flutter 전용이 아니라 이미 개발된 것을 재사용한다. 기존 구조는 UI 결합도가 높고 비즈니스 로직이 흩어져 있어 플러그인으로 옮기기 어려웠다.

| 마일스톤 | 내용 | 상태 |
|---|---|---|
| M1 Android | 네이티브 View 전체를 PlatformView 하나로 감싸고 지도 제어, 검색, 경로 탐색, 주행/모의주행, 오버레이를 MethodChannel로 호출. Hybrid Composition으로 Virtual Display 이슈 해결. 데이터 모델 13종, enum 16종, SDK 추가 제어 API 29개 | 완료 |
| M2 iOS | Android에서 확립한 Dart API를 Swift 플러그인으로 구현, 공개 CocoaPods로 통합(iOS 13+). MethodChannel 핸들러 약 70% 이상. 실기기 렌더링 확인(2026-04-21). iOS SDK에 없는 항목은 `NOT_SUPPORTED`로 반환 | 완료 |
| M3 pub.dev 공개 | pubspec 정리, 예제 앱의 앱키를 플레이스홀더로 교체, README 보강(코드 예제 오류 수정, 콜백 예제, Troubleshooting), 공개 배포, 태그 | 대기 |

알려진 제약: 공개 CocoaPods 배포본에 `arm64-simulator` 슬라이스가 없어 iOS 시뮬레이터는 Rosetta로 돌고 성능이 30~50% 떨어진다. SPM으로 전환하는 계획 문서가 있지만 아직 실행하지 않았다.

## Open Questions

- Flutter M3(pub.dev 공개 배포)의 완료 여부는 이 문서(2026-04-22 기준) 이후 기록이 없다. [[orbis-sdk]]에는 Step 1 배포 완료로 적혀 있다.

## Related

- [[orbis-routing-stack]], [[orbismap-api-docs]], [[ai-doc-first-development]]

## Sources

- [Confluence: New NaviSDK Plan, 상태 관리 Flow, MapsSDK 엔진 플랫폼 차이점 정리, NaviSDK Flutter Plugin Plan](https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/overview) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
