---
title: >-
    iNavi SDK iOS 개발 가이드 허브
category: references
project: orbis-sdk
tags: [ios, sdk, hub, cocoapods, visibility/internal]
aliases: [iNavi SDK iOS 개발 가이드, iNavi SDK iOS 개발 가이드 - SHI, iOS SDK 가이드 목차]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[navisdk-api-coverage-and-domestic-sdk-guide]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/305201307
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/305201319
summary: >-
    아이나비 내비게이션 SDK iOS 개발 가이드(일반 사본과 SHI 고객사 사본)를 옮긴 위키 페이지들의 목차와 핵심 요약.
provenance:
  extracted: 0.90
  inferred: 0.07
  ambiguous: 0.03
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T13:00:00+09:00
updated: 2026-10-26T13:00:00+09:00
---

# iNavi SDK iOS 개발 가이드 허브

Confluence의 "iNavi SDK iOS 개발 가이드"(pageId 305201307)와 고객사용 "iNavi SDK iOS 개발 가이드 - SHI"(pageId 305201319, 둘 다 archived)를 상세하게 옮긴 페이지 묶음의 목차다. 국내 SDK API 범위는 [[navisdk-api-coverage-and-domestic-sdk-guide]], 프로젝트 전체는 [[orbis-sdk]]를 본다.

## 핵심 요약

- CocoaPods(`inavi-navigation-sdk`)로 배포, iOS 13 이상, Xcode, Objective-C/Swift.
- 시작: plist에 `INaviAppKey` 등록, Background Mode(Audio, Location updates), `INaviMapView`를 서브 뷰로 추가, `INaviController.sharedInstance().initalizeNavi(uniqueID, target:)`로 초기화하고 Delegate의 인증 결과가 0일 때 사용.
- 기능 영역: 초기화, 지도 컨트롤, 통합 검색, 길 찾기, 주행(모의 주행 포함), 기타. 좌표는 위경도 DD.
- 일반 사본은 2020-12 ~ 2023-06(0.0.1~0.0.4, xcframework 적용), SHI 사본은 2023-07 ~ 2024-01(0.0.5~1.0.6).

## 페이지 목록

| 페이지 | 내용 |
|---|---|
| [[inavi-sdk-ios-guide-setup]] | 개정이력, 개요, Appkey, 개발 환경, CocoaPods 설치, 필수 권한, Layout 추가, SDK Interface 규칙 |
| [[inavi-sdk-ios-controller-reference]] | INaviController 전체 함수/프로퍼티/Delegate (6개 영역) |
| [[inavi-sdk-ios-structures-defines-and-codes]] | Structure 8종, Define(enum) 9종, 코드 표 22행 |
| [[inavi-sdk-ios-swift-scenarios]] | Swift 시나리오 예시 전부(일반 4개 + SHI 2개) |
| [[inavi-sdk-ios-guide-shi-edition-differences]] | SHI 사본 개정이력(0.0.5~1.0.6), 전용 Pod, 추가 함수, 일반 가이드와의 차이 |

## 문서에서 눈에 띄는 점

- 일부 함수(예: `forceHideMapComponent`)가 Kotlin 형태 시그니처로 남아 있어 Android 문서를 바탕으로 만든 흔적이 있다. Android 가이드와 iOS 가이드는 같은 기능 목록을 공유하되, 타입 이름은 iOS에서 `INV` 접두(`INVMapViewMode` 등), 이벤트는 Delegate 메서드 형태라는 차이가 있다. ^[inferred]
- 원본의 보안 관련 값(Appkey, 식별자 예시, 테스트 사용자 ID)은 위키에 옮기지 않았다.

## Related
- [[orbis-sdk]] — Orbis SDK 프로젝트
- [[navisdk-api-coverage-and-domestic-sdk-guide]] — 국내 SDK API 범위와 가이드

## Sources
- Confluence "iNavi SDK iOS 개발 가이드" (pageId 305201307) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "iNavi SDK iOS 개발 가이드 - SHI" (pageId 305201319) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
