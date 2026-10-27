---
title: >-
    iNavi SDK Android 개발 가이드 허브
category: references
project: orbis-sdk
tags: [navisdk, android, hub, domestic-sdk, visibility/internal]
aliases: [iNavi SDK Android 가이드 목차, 국내 SDK Android 가이드 인덱스]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[navisdk-api-coverage-and-domestic-sdk-guide]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/305430571 304906843
summary: >-
    국내향 iNavi SDK(Android) 개발 가이드(원본, SHI 사본)를 옮긴 위키 페이지 목차. 개정이력, 세팅, 예시, 함수 레퍼런스, 타입, 코드 표, SHI 차이.
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

# iNavi SDK Android 개발 가이드 허브

국내향 iNavi SDK(Android) 공식 개발 가이드(Confluence 2페이지: 원본 "iNavi SDK Android 개발 가이드", 고객사용 "iNavi SDK Android 개발 가이드-SHI")를 거의 그대로 옮긴 페이지들의 목차이다. 원본 문서는 2020-01(0.0.1)부터 2023-10(0.6.2)까지 갱신되었다. 이 SDK를 신규 SDK 전환 맥락에서 보는 문서는 [[navisdk-api-coverage-and-domestic-sdk-guide]], [[orbis-sdk]], [[orbis-navisdk-architecture-and-flutter-plan]]이다.

## 페이지 목록
| 페이지 | 내용 |
|---|---|
| [[inavi-sdk-android-revision-history]] | 개정이력 0.0.1~0.6.2 전체, 필수 적용 항목, 기능별 도입 버전 |
| [[inavi-sdk-android-setup-and-permissions]] | 개요, Appkey 발급 절차, 개발 환경, Gradle/Manifest/Layout 세팅, 권한, 난독화, 생명주기/좌표계 |
| [[inavi-sdk-android-scenario-examples]] | 시나리오별 Kotlin 예시 12개(초기화~가장 가까운 좌표) 전체 |
| [[inavi-sdk-android-controller-init-map-search]] | INaviController 초기화(7), 지도 컨트롤(32), 검색(5) 함수 |
| [[inavi-sdk-android-controller-route-and-driving]] | 길찾기(9), 주행(9) 함수 |
| [[inavi-sdk-android-controller-misc-and-truck]] | 기타(24), 화물차 옵션(11) 함수 |
| [[inavi-sdk-android-interface-structure-define-reference]] | Listener 12종, 구조체 10종, enum 14종 |
| [[inavi-sdk-android-error-codes]] | 코드 표(0 ~ 6000) 전체 |
| [[inavi-sdk-android-shi-edition-diff]] | SHI(삼성중공업) 사본과 원본의 차이: 별도 버전 1.0.x, 소지번 길찾기, `INaviShiMember` |

## 한눈에 보는 핵심
- 모든 기능은 Singleton `INaviController`로 호출하며 비동기는 Callback 제공. 좌표는 WGS84 십진수 도.
- 필수 호출 순서: `loadNaviLibrary` → `initLayout` → `initalizeNavi`(성공 시에만 이후 I/F 사용 가능), 종료 시 `destroyNavi`. 앱 실행당 1회.
- 최소 환경: minSdkVersion 21, targetSdkVersion 28, Kotlin, ABI arm64-v8a/armeabi-v7a, AndroidX(0.6.0부터).
- 함수 총계: 초기화 7 + 지도 32 + 검색 5 + 길찾기 9 + 주행 9 + 기타 24 + 화물차/기타 11 = 97개 항목(deprecated 3개, 오버로드 포함).
- 화물차 지원: 높이/중량/유턴/좁은길/통행제한 회피 + TRUCK 계열 탐색 옵션(0.0.27~).

## Related
- [[navisdk-api-coverage-and-domestic-sdk-guide]] — 국내 SDK 가이드 개요와 커버리지
- [[orbis-sdk]] — SDK 프로젝트 허브
- [[orbis-navisdk-architecture-and-flutter-plan]] — NaviSDK 구조와 Flutter 계획
- [[inavi-hybrid-navi]] — 하이브리드 내비 엔진 배경

## Sources
- Confluence "iNavi SDK Android 개발 가이드" (pageId 305430571) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "iNavi SDK Android 개발 가이드-SHI" (pageId 304906843) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
