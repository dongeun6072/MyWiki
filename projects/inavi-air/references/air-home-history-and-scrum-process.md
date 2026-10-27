---
title: >-
    아이나비 에어 연혁과 스프린트/스크럼 운영 방식
category: references
project: inavi-air
tags: [air, history, scrum-process, sprint, visibility/internal]
aliases: [아이나비 에어, 스프린트/스크럼 보드, 아이나비 에어 Notion (legacy), 미팅 노트, 스크럼, 스페이스의 미팅 메모, 스프린트 Archived(NSDK Renewal)]
relationships:
  - target: "[[inavi-air]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/143458751
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/148275602
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/143589533
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/331645004
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/331776175
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/616824847
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/144637958
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/147423395
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/331710570
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/565248111
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/724008981
summary: >-
    에어 서비스의 2012~2023년 연혁(오픈~에어캐시 사용성 개선)과 에어/NSDK 스크럼 보드의 스프린트 진행 단계, Jira 필수 필드, 요일 규칙, 내용 없는 컨테이너 페이지 목록.
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

# 아이나비 에어 연혁과 스프린트/스크럼 운영 방식

Confluence 스페이스 "아이나비 에어 & NSDK"의 홈 페이지(연혁)와 스프린트/스크럼 보드(운영 규칙), 그리고 본문이 없는 컨테이너 페이지들을 정리한다. 기능 연혁의 상세는 [[inavi-air-feature-history]], 프로젝트 개요는 [[inavi-air]], 목차는 [[air-scrum-records-hub]]다.

## 아이나비 에어 홈: "에어의 탄생부터 현재까지" (수정 2025-01-16)

| 시기 | 내용 |
|---|---|
| 2012년 9월 | 아이나비 에어 오픈 |
| 2013년 9월 | 아이나비 LTE 에어 for Kakao |
| 2016~2018년 | KT내비 → 원내비(KT/LG U+) 통합 서비스로 전환 |
| 2018년 | 원내비 서비스 종료 — KT 내재화, LG U+는 카카오내비로 전환 |
| 2019년 3월 27일 | 아이나비 에어 리뉴얼 오픈 베타(아이나비 LTE 에어 업데이트 버전) |
| 2019년 4월 25일 | 아이나비 에어 리뉴얼 공식 오픈 |
| 2019년 4월 29일 | CarPlay 오픈 |
| 2021년 4월 14일 | Android Auto 오픈 |
| 2022년 5월 24일 | UI 리뉴얼 + 노출 광고 오픈 |
| 2022년 7월 25일 | 에어캐시 리워드 서비스 오픈 |
| 2022년 10월 31일 | 실시간 신호등 정보 시범 서비스 오픈 — 대구광역시 일부 교차로 |
| 2023년 1월 10일 | UI 리뉴얼 2차 + 에어 연구소 오픈 |
| 2023년 5월 16일 | 아바티 캐시버튼(AOS) + what3words 연동 오픈 |
| 2023년 7월 4일 | 에어캐시 사용성 개선 오픈 — 메인화면 에어캐시 버튼 및 9회차 주행 리워드 |

하단에 스토어 링크 항목(Google Play, App Store)이 있으나 링크 값은 미수록이다.

## 아이나비 에어 Notion (legacy) (수정 2023-05-22)

"Notion은 더 이상 업데이트하지 않고, 최신 내용은 CF(Confluence)에 업데이트한다"는 안내와 Notion 링크 1개(링크 생략)만 있다.

## 스프린트/스크럼 보드 (수정 2024-10-14) — 아이나비 에어/NSDK 스크럼 보드

### 진행 단계
1. **스프린트 플래닝(Jira)**: 진행 항목 도출 및 우선순위 논의
   - 스프린트 기간 설정(1~2주)
   - 스프린트 기준 티켓 생성 및 추정치 입력
2. **스크럼(CF)**: 일정 점검 및 진행상황 공유
3. **스프린트 리뷰(CF)**: 목표 달성 여부 판단 및 리뷰
   - 항목 달성 여부 확인 및 이유 논의
   - 항목 백로그 또는 다음 스프린트 이관 논의
4. **스프린트 회고(CF)**: 스프린트 진행 의견 공유 및 개선 포인트 리뷰
   - Good / Bad / Action Item(개선할 것) 기재 후 논의

### Jira 티켓 필수 입력 필드
- 스프린트 플래닝(티켓 생성 시): 추정치, Component 필수
- 티켓 "진행중" 변경 시: startDate, dueDate 필수

### 요일 규칙
- 스프린트 월요일: 스프린트 리뷰 / 스프린트 플래닝
- 매주 수요일: 스크럼 진행
- 스프린트 종료 금요일: 스프린트 회고

(2023년 주제별 스크럼의 "Jira 이슈 진행 프로세스: 시작/완료/최초 추정치 기입, 해결됨 시 실제 기간 명시" 규칙이 이 필수 필드 규칙의 앞 단계다. ^[inferred] [[air-feature-upgrade-scrums-2023]] 참고)

## 내용 없는 컨테이너/링크 전용 페이지

| 페이지 | 비고 |
|---|---|
| 미팅 노트 | 본문 없음(컨테이너) |
| 스크럼 | 본문 없음(컨테이너) |
| 스페이스의 미팅 메모 | 본문 없음 |
| 스프린트 Archived(NSDK Renewal) | 본문 없음 |
| 외부 연동 가이드 | 본문 없음 |
| 에어퀴즈 | 본문 없음 |
| NaviSDK Renewal (NSDK-3) | Jira 링크 1개만(이미지/링크 항목, 내용 없음). 수정 2024-10-10 |
| Orbis Navi&Map SDK (대만향) | Jira 링크 1개만(이미지/링크 항목, 내용 없음). 수정 2026-03-24 |

## Related
- [[air-scrum-records-hub]] — 목차
- [[inavi-air-feature-history]] — 기능 연혁 상세
- [[inavi-air]] — 프로젝트 허브
- [[navisdk-confluence-sprint-timeline-2024-2026]] — NSDK 스프린트 타임라인
- [[air-confluence-scrum-and-voice-2023-2024]] — 스크럼 요약본

## Sources
- Confluence "아이나비 에어" (pageId 143458751) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "아이나비 에어 Notion (legacy)" (pageId 148275602) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "스프린트/스크럼 보드" (pageId 143589533) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "스크럼" (pageId 331645004) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "스페이스의 미팅 메모" (pageId 331776175) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "스프린트 Archived(NSDK Renewal)" (pageId 616824847) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "미팅 노트" (pageId 144637958) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "외부 연동 가이드" (pageId 147423395) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "에어퀴즈" (pageId 331710570) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "NaviSDK Renewal (NSDK-3)" (pageId 565248111) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "Orbis Navi&Map SDK (대만향)" (pageId 724008981) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
