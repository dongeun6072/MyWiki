---
title: >-
    생성형 AI(w/ ChatGPT) 스크럼 #1, #3, #4 (2024)
category: references
project: inavi-air
tags: [inavi-air, scrum, genai, airbot, visibility/internal]
aliases: [스크럼 #1 - 생성형AI (w/ ChatGPT), 스크럼 #3 - 생성형AI (w/ ChatGPT), 스크럼 #4 - 생성형AI (w/ ChatGPT)]
relationships:
  - target: "[[inavi-air]]"
    type: related_to
  - target: "[[air-confluence-scrum-and-voice-2023-2024]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/516554753
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/538411036
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/549879821
summary: >-
    2024년 8~9월 에어 팀 주간 스크럼(생성형 AI 시기) 3회차 상세: Agenda, Done & Doing, ToDo, Issues와 회차 간 변화.
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

# 생성형 AI(w/ ChatGPT) 스크럼 #1, #3, #4

에어 앱 팀이 생성형 AI(에어봇) 도입 시기에 진행한 회의 페이지 3건(#2 페이지는 이 묶음에 없음)이다. 모두 보관(archived) 상태이며 매회 10:30~12:00. 참석자는 기획/디자인/앱/PM 담당(이름 생략)이다. 앞선 신규 Feature Ideation 스크럼은 [[air-feature-ideation-scrum-2024]], 허브는 [[air-genai-and-ideation-hub]].

## 공통 구조와 반복 항목

- 섹션: Agenda, Done & Doing(기획/디자인/Agent/App/PM), ToDo(기획/디자인/Agent/App/PM/엔진), Issues(기획/디자인/Agent/App/PM/사업), Request(빈 체크박스 `…`).
- **ToDo는 세 회차 모두 동일**(템플릿 잔존): 기획 - 공지 팝업 문구 작성, 스토어 문구 작성 / 디자인 - 공지 팝업 이미지 제작, 스토어 이미지 현행화 / PM - TC 작성.

## 스크럼 #1 (날짜 미기재, 2024-8월경 ^[inferred])

- Agenda: 생성형 AI 타당성 검토 / SKP 광고 Mediation / 음성 DB 교체(발랄한 음성, 성우 이름은 생략) / [AOS] 스토어 aab 출시 / New NaviSDK 검토
- Done & Doing: App - AI 타당성 검토, New NaviSDK 계획 수립. 기획·디자인·Agent·PM은 비어 있음.
- Issues: 없음(항목만 있고 내용 없음).

## 스크럼 #3 (2024-09-11)

- Agenda: 생성형 AI 타당성 검토 / SKP 광고 Mediation 검토 / 음성 DB 교체(발랄한 음성) / [AOS] 스토어 aab 출시 / **DP 엔진 교체 (v0.0.6.4c) - only AOS** (신규) / New NaviSDK 검토
- Done & Doing: App - AI 타당성 검토(**완료**), DP 엔진 교체, New NaviSDK 개발 계획 및 일정 수립.
- Issues: 없음.

## 스크럼 #4 (2024-09-24)

- Agenda: 생성형 AI **서비스 추가**(타당성 검토에서 변경) / 음성 DB 교체(발랄한 음성) / [AOS] 스토어 aab 출시 / DP 엔진 교체 (v0.0.6.4c) - only AOS / New NaviSDK 검토. (SKP 광고 Mediation 항목은 Agenda에서 빠짐)
- Done & Doing: App - AI 타당성 검토(완료), DP 엔진 교체(**완료**), New NaviSDK 개발 계획 및 일정 수립. PM - **AI 품의 진행(완료)**.
- Issues (App):
  - 발랄한 음성으로 교체 후 서비스를 진행하나, 음성 품질 관련해 신규 음성을 받아 재적용(10/11) 예정.
  - SKP 광고 Mediation 검토: 현재 상태를 유지하고, 차후 필요 시 재적용하는 것으로 협의.

## 회차 간 변화 요약

| 항목 | #1 | #3 (9/11) | #4 (9/24) |
|---|---|---|---|
| 생성형 AI | 타당성 검토 | 타당성 검토 완료 | 서비스 추가, AI 품의 완료 |
| DP 엔진 교체(v0.0.6.4c, AOS) | 없음 | 진행 | 완료 |
| SKP 광고 Mediation | Agenda | Agenda(검토) | 현 상태 유지, 필요 시 재적용으로 결정 |
| 발랄한 음성 | Agenda | Agenda | 품질 이슈로 신규 음성 10/11 재적용 예정 |
| New NaviSDK | 계획 수립 | 개발 계획 및 일정 수립 | 동일 |

## Related
- [[air-chatgpt-usecases-and-dev-spec-2024]] — 같은 시기 개발 사양과 v0.5 출시 문구
- [[air-confluence-scrum-and-voice-2023-2024]] — 발랄한 음성/스크럼 전반
- [[air-feature-ideation-scrum-2024]] — 앞선 시기 스크럼
- [[inavi-air]] — 프로젝트 홈

## Sources
- Confluence "스크럼 #1 - 생성형AI (w/ ChatGPT)" (pageId 516554753) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "스크럼 #3 - 생성형AI (w/ ChatGPT)" (pageId 538411036) — 같음
- Confluence "스크럼 #4 - 생성형AI (w/ ChatGPT)" (pageId 549879821) — 같음
