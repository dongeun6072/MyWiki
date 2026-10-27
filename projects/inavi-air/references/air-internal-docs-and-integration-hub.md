---
title: >-
    에어 내부 문서와 외부 연동 허브
category: references
project: inavi-air
tags: [air, hub, integration, developer-docs, testing, visibility/internal]
aliases: [에어 내부 문서 허브, Documents 묶음]
relationships:
  - target: "[[inavi-air]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/305397799
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/305168599
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/304972369
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/305005057
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/205029460
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/205029509
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/205029377
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/205029415
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/205029553
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/973078739
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/984055941
summary: >-
    Confluence 에어/NSDK 스페이스의 내부 문서 묶음(외부 연동 규격, 개발 문서, 테스트 가이드, NaviSDK 미구현 현황, KDoc 가이드) 목차.
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

# 에어 내부 문서와 외부 연동 허브

Confluence "아이나비 에어 & NSDK" 스페이스의 내부 문서 11페이지를 위키로 옮긴 페이지들의 목차다. 앱 개요는 [[inavi-air]], SDK 개요는 [[orbis-sdk]], SDK API 범위는 [[navisdk-api-coverage-and-domestic-sdk-guide]]를 본다.

## 페이지 목록

- [[air-external-integration-android-spec]] — Android 외부 연동 규격(BroadcastReceiver, Scheme, Geo Scheme, 즉시 안내)
- [[air-external-integration-ios-spec]] — iOS `autorunair` URL 연동 규격과 인자
- [[air-android-ios-developer-docs]] — Android/iOS 프로젝트 정보, 라이브러리, 세팅, 기여 가이드, `Documents`와 `API Documentation` 허브 구조
- [[air-testing-guide]] — DHU/CarPlay, GPS 로그, Push, 모의주행 테스트
- [[navisdk-inavicontroller-unimplemented-status]] — Orbis NaviSDK 미구현 항목과 INaviController API 적용 현황
- [[orbis-navisdk-kdoc-and-mkdocs-guide]] — KDoc 문서화와 MkDocs 가이드 작성법

## 원본 페이지와 대응

| 원본 제목 | pageId | 반영 위치 |
|---|---|---|
| iNavi AIR Android 연동 규격 | 305397799 | [[air-external-integration-android-spec]] |
| iNavi AIR iOS 연동 규격 | 305168599 | [[air-external-integration-ios-spec]] |
| iNavi AIR App to App Guide | 304972369 | 제목만 있는 빈 페이지(2023-12-26 수정). 규격은 위 두 연동 규격 참조 |
| iNavi SDK in-App Guide (신규페이지 확인후 제거 예정) | 305005057 | archived, 본문 없음 |
| Android Documentation | 205029460 | [[air-android-ios-developer-docs]] |
| iOS Documentation | 205029509 | [[air-android-ios-developer-docs]] |
| Documents | 205029377 | [[air-android-ios-developer-docs]] |
| API Documentation | 205029415 | 링크뿐인 빈 페이지 |
| Testing Guide(공통) | 205029553 | [[air-testing-guide]] |
| 미 구현 항목 현황 - 지속 업데이트 | 973078739 | [[navisdk-inavicontroller-unimplemented-status]] |
| Orbis NaviSDK API Document 작성 문서 | 984055941 | [[orbis-navisdk-kdoc-and-mkdocs-guide]] |

## 의도적으로 옮기지 않은 항목
서버 전환 방법, 개발자 모드와 로그 다운로드 진입 입력어, FCM 서버 키와 기기 토큰이 든 curl 예시, 저장소/내부 서버 주소, 로컬 PC 경로 (모두 원본에 있음, 미수록).

## Related
- [[inavi-air]] — 에어 앱
- [[orbis-sdk]] — Orbis SDK
- [[navisdk-api-coverage-and-domestic-sdk-guide]] — 국내 SDK 가이드

## Sources
- Confluence 에어 & NSDK 스페이스 내부 문서 11페이지 — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
