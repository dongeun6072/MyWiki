---
title: >-
    에어캐시 고도화 기획 이력과 메인 에어캐시(하단 바·툴팁), UI 개선
category: references
project: inavi-air
tags: [air-cash, planning, main-screen, tooltip, visibility/internal]
aliases: [에어캐시 고도화, 에어캐시 고도화_, 기능 고도화, 메인 에어캐시, 에어캐시 메인 레이아웃 개선, AI 횡단보도 & 에어캐시 메인, 에어캐시 UI 개선_25.12, 에어캐시 페이지 광고 추가 건]
relationships:
  - target: "[[inavi-air]]"
    type: related_to
  - target: "[[air-cash-stamp-release-2023]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/158466081
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/149913653
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/169640129
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/186122244
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/198115329
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/190644237
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1507852289
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1494089729
summary: >-
    2023년 6~7월 에어캐시 고도화 기획서 v0.5부터의 수정 이력, 스토어 문구(AOS 03.05.28/iOS 03.05.05), 메인 에어캐시 카드 제거와 하단 바·툴팁, 2025-12 UI 개선 문구.
provenance:
  extracted: 0.92
  inferred: 0.06
  ambiguous: 0.02
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T13:00:00+09:00
updated: 2026-10-26T13:00:00+09:00
---

# 에어캐시 고도화 기획 이력과 메인 에어캐시(하단 바·툴팁), UI 개선

스탬프형 적립([[air-cash-stamp-release-2023]]) 이후 적립과 스탬프를 하나의 "리워드"로 통합하고 룰렛을 붙인 에어캐시 고도화 기획서의 버전 이력, 메인 화면의 에어캐시 카드를 하단 바와 툴팁으로 바꾼 이력, 그리고 2025-12 UI 개선까지를 정리한다. 목차는 [[air-feature-planning-hub]].

## 1. 에어캐시 고도화 기획서 수정 이력 (pageId 158466081, 2023-06-22)
원본 페이지에는 최신 수정이 위에 쌓여 있다. 시간순(오래된 것부터)으로 재배열한다.
1. 중간 공유용 기획서 v0.5 — 컨셉 및 사용자 시나리오 검토 완료.
2. 리뷰 진행했던 기획서 공유. 추가 진행 사항: 메인카드 랜덤 스토리 추가, PUSH 문구 수정.
3. 리뷰 후 수정사항 반영, 룰렛 기능을 함께 고려.
   - 룰렛 제공 사양 변경(스탬프와 별개로 제공)
   - 룰렛 페이지 추가
4. 수정사항: 메인카드 랜덤 스토리 추가, PUSH 문구 수정, 룰렛 내용 추가, 그 외 추가 요청사항 추가.
5. 수정사항: 룰렛 이용권 만료 정책 추가(기획서 p.12).
6. 수정사항: 리워드 스토리 수정, 에어캐시 메인카드 스토리 수정.

"기능 고도화" (pageId 149913653, 보관): 버전 목록만 있고 설명이 없는 페이지. 표기된 버전은 v0.1, v1.1, v1.2, v1.3, v1.4. ^[ambiguous]

## 2. 스토어 문구 — "에어캐시 고도화_" (pageId 169640129, 2023-06-21)
### AOS v03.05.28
```
[v03.05.28]
• 확 달라진 에어캐시!
  - 메인화면에 추가된 에어캐시 버튼 & 스토리!
  - 직관적인 UI로 새로워진 에어캐시를 확인해 보세요!
  - 적립과 스탬프를 하나로 통합해서 리워드로 제공해요!
  - 9회차 주행하고 캐시 룰렛 추가 적립도 놓치지 마세요!
최신 버전으로 지금 업데이트 해보세요!
더 좋은 서비스를 위해 에어팀은 항상 귀 기울이고 있습니다.
```
### iOS v03.05.05
동일 문구(이모지 없음).

## 3. 메인 에어캐시 (pageId 186122244, 2023-07-19) — 기획서 수정 항목
- 툴팁 사양 추가: 5초 이전 선택 시 툴팁 제거
- 팝업 사양 수정
- 미적립 캐시에 대한 툴팁 안내 추가
- 중앙 팝업(이어가기, Push 등)에 대한 툴팁 사양 추가
- 리뷰 후 기획서 업데이트
- 메인화면 에어캐시 카드 제거
- 탭바(하단 바)의 에어캐시 중요도 상향
- 툴팁 제공(개인화 + 캐시 알림 표시)

## 4. 에어캐시 메인 레이아웃 개선 (pageId 198115329, 2023-07-19)
- 2023-07-19: 메인 화면 GUI 변경 반영 — 에어캐시 카드 제거, 하단 바 + 툴팁 추가.

## 5. 스토어 문구 — "AI 횡단보도 & 에어캐시 메인" (pageId 190644237, 2023-07-26)
### AOS v03.05.29
```
[v03.05.29]
• 친절해진 에어캐시!
  - 주행 후 메인화면에서 캐시 적립 안내를 제공해요.
  - 주기적으로 다음 쿠폰까지 남은 캐시를 알려드려요.
• 후면 번호판 단속 카메라 안내!
  - 새롭게 시행 중인 교통 법규도 안전하게 지켜주세요.
최신 버전으로 지금 업데이트 해보세요!
더 좋은 서비스를 위해 에어팀은 항상 귀 기울이고 있습니다.
```
### iOS v03.05.07
같은 문구(이모지 없음). 후면 단속 카메라는 [[air-small-features-and-notices-2023-2025]]에서 이어진다.

## 6. 에어캐시 UI 개선 25.12 (pageId 1507852289, 2025-12-17)
### AOS v03.05.57
```
[v03.05.57]
• 에어캐시 UI 개선
  - 캐시를 받을 수 있는 방법이 추가되어 확장된 보상 기능을 한눈에 볼 수 있도록 UI를 개선했어요.
    다양한 방법으로 캐시를 적립해 보세요.
• Android Auto 가독성 및 사용성 향상
  - 배경색에 따라 글자색이 바뀌어 잘 보이지 않던 문제를 개선했어요.
  - 집/회사 소요시간과 거리 정보가 더 선명하게 보이도록 시인성을 높였어요.
• 앱 안정성 개선
  - 일부 오류를 수정하고 전반적인 성능을 최적화했어요.
최신 버전으로 지금 업데이트 해보세요!
더 좋은 서비스를 위해 에어팀은 항상 귀 기울이고 있습니다.
```
### iOS v03.05.34
에어캐시 UI 개선과 앱 안정성 개선 두 항목(Android Auto 항목 없음), 문구는 AOS와 동일.

## 7. 에어캐시 페이지 광고 추가 건 (pageId 1494089729, 2025-12-09)
- 리소스 배포 표 1행: "이미지 리소스 배포" (날짜는 링크로만 존재).

## Related
- [[air-cash-reward-design-2023-2024]] — 정책 요약
- [[air-cash-welcome-mission-table-2024]] — 신규 사용자 웰컴 미션
- [[air-cash-stamp-release-2023]], [[air-cash-accrual-policy-discussion-2023]]
- [[air-service-stability-release-notes-2023-2026]] — 이후 안정화 릴리즈 노트
- [[inavi-air]], [[inavi-air-feature-history]]

## Sources
- Confluence "에어캐시 고도화" (158466081), "기능 고도화" (149913653), "에어캐시 고도화_" (169640129), "메인 에어캐시" (186122244), "에어캐시 메인 레이아웃 개선" (198115329), "AI 횡단보도 & 에어캐시 메인" (190644237), "에어캐시 UI 개선_25.12" (1507852289), "에어캐시 페이지 광고 추가 건" (1494089729) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
