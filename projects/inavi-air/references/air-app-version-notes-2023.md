---
title: >-
    에어 앱 버전·스토어 문구 2023
category: references
project: inavi-air
tags: [inavi-air, release-notes, store, hud, visibility/internal]
aliases: [HUD 연동_Beta, 서비스 안정화 작업, 에어 스토어 출시 문구 2023]
relationships:
  - target: "[[inavi-air]]"
    type: related_to
  - target: "[[inavi-air-feature-history]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/283312129
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/300810312
summary: >-
    2023년 에어 앱 스토어 출시 문구(HUD 연동 Beta, 12월 서비스 안정화)와 AOS/iOS 버전 번호를 원문 그대로 정리한 문서.
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

# 에어 앱 버전·스토어 문구 2023

2023년에 Confluence에 남은 에어 앱 스토어 출시 문구 페이지는 두 건이다(11월 HUD 연동 Beta, 12월 서비스 안정화). 각 페이지는 AOS/iOS 문구를 코드 블록으로 담고 있고, iOS 문구는 AOS와 달리 이모지가 빠져 있다. 요약본은 [[air-service-stability-release-notes-2023-2026]], 전체 목록은 [[air-release-and-resource-log-hub]]를 본다.

## 버전 요약

| 페이지(제목) | AOS | iOS | 원본 수정일 | 주제 |
|---|---|---|---|---|
| HUD 연동_Beta | v03.05.33 | v03.05.12 | 2023-11-23 | HUD 연동 Beta 시작 |
| 서비스 안정화 작업 | v03.05.34 | v03.05.13 | 2023-12-20 | 검색 추천어 개선, iOS 단축어 지원 시작 |

## HUD 연동 Beta (AOS v03.05.33 / iOS v03.05.12)

AOS 문구:
```
[v03.05.33]
• HUD 연동 Beta버전 시작!🎉
  - 환경설정 > HUD 설정에서 기기를 등록하세요.
  - 에어의 길안내를 HUD에서 편리하게 사용해 보세요.
최신 버전으로 지금 업데이트 해보세요!
더 좋은 서비스를 위해 에어팀은 항상 귀 기울이고 있습니다.😀
```
iOS 문구:
```
[v03.05.12]
• HUD 연동 Beta버전 시작!
  - 환경설정 > HUD설정에서 기기를 등록하세요.
  - 에어의 길안내를 HUD에서 편리하게 사용해 보세요.
최신 버전으로 지금 업데이트 해보세요!
더 좋은 서비스를 위해 에어팀은 항상 귀 기울이고 있습니다.
```
차이점: AOS는 "HUD 설정" 표기 앞에 공백이 있고(`HUD 설정`), iOS는 `HUD설정`으로 붙여 쓴다. HUD 연동 배경은 [[air-hud-integration-2023]]을 참고한다.

## 서비스 안정화 작업 (AOS v03.05.34 / iOS v03.05.13)

AOS 문구:
```
[v03.05.34]
• 검색 시 추천어 개선 🔍
  - 최근장소, 내장소에 대한 검색까지 더욱 꼼꼼하게 찾아드려요.
• 버그 수정 및 안정성 개선 ✅
  - 원활한 서비스 제공을 위해 준비했어요.
최신 버전으로 지금 업데이트 해보세요!
더 좋은 서비스를 위해 에어팀은 항상 귀 기울이고 있습니다.😀
```
iOS 문구:
```
[v03.05.13]
• 단축어 기능 지원 시작!
  - 단축어 기능으로 에어를 더욱 편리하게 사용하세요.
• 검색 시 추천어 개선
  - 최근장소, 내장소에 대한 검색까지 더욱 꼼꼼하게 찾아드려요.
• 버그 수정 및 안정성 개선
  - 원활한 서비스 제공을 위해 준비했어요.
최신 버전으로 지금 업데이트 해보세요!
더 좋은 서비스를 위해 에어팀은 항상 귀 기울이고 있습니다.
```
차이점: "단축어 기능 지원 시작" 항목은 iOS에만 있다(iOS 단축어 위젯 리소스 수정은 [[air-resource-deploy-log-2023-h2]]의 2023.12.12 항목).

## 같은 시기 연관 문서
- 12월 서비스 안정화 스크럼과 HUD 연동 스크럼: [[air-hud-and-stabilization-scrums-2023-12]]
- 스토어 출시 목표일 표: [[air-store-release-target-dates]]
- 다음 해: [[air-app-version-notes-2024]]

## Related
- [[inavi-air]] — 에어 앱 프로젝트 허브
- [[inavi-air-feature-history]] — 기능 이력
- [[air-service-stability-release-notes-2023-2026]] — 요약본
- [[air-hud-integration-2023]] — HUD 연동 배경

## Sources
- Confluence "HUD 연동_Beta" (pageId 283312129) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "서비스 안정화 작업" (pageId 300810312) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
