---
title: >-
    Orbis 설계·검토 상세 문서 허브
category: references
project: orbis-sdk
tags: [orbis, navisdk, hub, design, review, visibility/internal]
aliases: [Orbis 설계 및 검토 허브, 신규 NaviSDK 설계 목차]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/511311892
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/789512333
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/641695841
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1824686148
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/973504759
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1057980417
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/801112442
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1028849674
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1119715398
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/987463744
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/826212376
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/809599362
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/813727747
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/739115034
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/746029545
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/761167886
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1267925062
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1503526933
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/670433348
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1105690655
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1023705106
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1439137813
summary: >-
    신규 NaviSDK 설계, 상태 관리, 엔진 차이, Flutter 플러그인, 지도 스타일, 안내·다국어, TomTom/Route 검토, 대만 현지 평가 상세 페이지 목차
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

# Orbis 설계·검토 상세 문서 허브

Confluence "아이나비 에어 & NSDK" 스페이스의 신규 NaviSDK 설계, OrbisMap 검토, 안내·다국어 사양, 대만 현지 평가 페이지를 압축하지 않고 옮긴 상세 페이지들의 목차다. 기존 요약 페이지는 [[orbis-navisdk-architecture-and-flutter-plan]], [[orbis-guidance-and-voice-spec]], [[taiwan-field-evaluation-2025]], [[orbismap-route-and-tomtom-sdk-review-2025]], [[orbis-navisdk-poc-prep-2025]]이며, 이 허브의 상세 페이지는 각 요약의 원본 수준 확장판이다. 프로젝트 홈은 [[orbis-sdk]].

## 신규 NaviSDK 설계
- [[new-navisdk-plan-detail]] — 제로베이스 신규 SDK 필요성, KMP 구조, 모듈 관계, UI 확장성, 개발 순서, 마일스톤, 수정 이력(요약: [[orbis-navisdk-architecture-and-flutter-plan]])
- [[navisdk-ui-state-flow-detail]] — UIGuideRepository StateFlow 규칙, UIGuideData 필드, UIMode enum 전체
- [[mapssdk-engine-platform-differences]] — DP/MMC 엔진의 AOS vs iOS 함수 비교표 전체
- [[navisdk-flutter-plugin-plan-detail]] — Flutter 플러그인 구조, M1~M4, M3 작업 분해, README 보강 항목, 알려진 제약

## 지도 스타일·표현 분석
- [[orbis-tile-map-style-analysis]] — 아이나비 Orbis vs TomTom Orbis 타일 스타일 1·2차 분석
- [[apple-map-display-comparison]] — 아이나비 vs 애플지도 Display 비교 전 항목과 적용 가능성

## 안내 엔진·다국어
- [[google-navigation-guidance-and-map-level-analysis]] — 구글 안내 사양 13개 항목, 구글 뷰모드(2D Fix/3D) 분석
- [[orbis-guidance-engine-dev-spec]] — 음성 안내 템플릿, 턴 코드 속성, 카메라 판단 규칙
- [[orbis-voice-phrase-combinations]] — 한·영·번체·간체 문구와 audio_* 조각 키 전체, 템플릿 어순
- [[orbis-i18n-units-notation-and-translation-resources]] — 번체/간체 단위·표기 규칙, 번역 리소스 이력
- [[orbis-onesky-translation-process]] — Onesky 번역 절차, Key 작성 규칙, 리소스 추출

## OrbisMap/TomTom 검토
- [[tomtom-maps-sdk-api-review-detail]] — TomTom Maps SDK API 적용 표 전 행, 커스텀 자차 마커(.glb)
- [[orbismap-route-review-detail]] — 도로 종별·maneuver 코드표, Route 응답 JSON 구조
- [[genesis-vs-orbis-search-api-review-taiwan]] — 대만 POI 10건 검색 API 비교
- [[orbismap-navisdk-dev-spec-and-poc-prep]] — 지도 모드 수치, 자동 줌, PoC 사전 준비와 TomTom 지도 데이터 현황

## 현지 평가·기타
- [[taiwan-field-evaluation-detail]] — 2025-10 대만 실차 주행 코스, TC 결과, 개선 항목, 배터리, 총평
- [[orbis-specout-rr-and-misc-pages]] — Specout 목록, R&R(역할), 에어 내부 TC/UI 리소스, 빈 페이지 목록

## Related
- [[navisdk-confluence-sprint-timeline-2024-2026]] — 같은 스페이스의 스프린트 타임라인
- [[kmp-cmp-adoption]] — KMP/CMP 도입 배경

## Sources
- Confluence 스페이스 "아이나비 에어 & NSDK" 내 위 페이지들 (pageId는 각 상세 페이지의 sources 참고) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
