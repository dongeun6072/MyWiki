---
title: >-
    2026 성과점검 자체 평가 (1분기, 상반기)
category: references
tags: [career, performance-review, goals, visibility/pii]
aliases: [2026 성과점검, 2026 상반기 성과점검, 2026 1분기 성과점검]
relationships:
  - target: "[[2026-goals-and-checkins]]"
    type: derived_from
sources:
  - ~/Develop/Wiki/_raw/articles/inavi/2026_1분기_성과점검_이동은.md
  - ~/Develop/Wiki/_raw/articles/inavi/2026_상반기_성과점검_이동은.md
summary: >-
    2026년 1분기와 상반기 성과점검 자체 평가 내용. 세 성과(고객사 대응, KMP/CMP, AI 도입)별 달성 현황, 잘된 점, 부족한 점, 계획과 팀 리더의 1차 평가 요지.
provenance:
  extracted: 0.88
  inferred: 0.12
  ambiguous: 0.00
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T09:20:33+09:00
updated: 2026-10-26T09:20:33+09:00
snapshots:
  - "[[_raw/_archived/2026_상반기_성과점검_이동은|2026_상반기_성과점검_이동은]]"
  - "[[_raw/_archived/2026_1분기_성과점검_이동은|2026_1분기_성과점검_이동은]]"
---

# 2026 성과점검 자체 평가

[[이동은]]의 2026년 1분기(제출 7/1~7/7)와 상반기 셀프 평가다. 세 성과의 비중은 각 20%이고 목표 진척도는 모두 50%다([[2026-goals-and-checkins]]). 등급과 평가자 이름은 옮기지 않았다.

## 성과 1. 고객사 프로젝트 요구사항 및 일정 준수

| | 1분기 | 상반기 |
|---|---|---|
| 달성 | 해외향 Maps SDK 개발 완료, API 레퍼런스·Demo 앱·IMPS 가이드 | 위 내용에 더해 Navi SDK v1.0.2~1.0.4(예정), Maps SDK v1.0.1(예정), 삼성생명 드로잉런 SDK Android/iOS 배포, Flutter Plugin Step 1 배포 |
| 잘된 점 | 신규 기능·요구사항을 안정적으로 반영 | 같은 점 + 국내향 소스 제거, 공통 로직화 리팩토링으로 대응 속도를 높일 구조 마련 |
| 어려움 | 배포가 Android 서브모듈 → Dokka → iOS XCFramework → SPM으로 복잡 | 공통 배포 프로세스를 정비해 일부 해소, 안정성 개선은 지속 |
| 계획 | 공통 구조와 문서 정비 | 개선한 배포 프로세스 안정화, Phase-2 고도화 |

→ [[orbis-sdk]], [[drawing-run-sdk]]

## 성과 2. KMP/CMP 기반 멀티플랫폼 프로젝트 전환

- 달성: 1분기에는 KMP 프로젝트 유지보수 중심. 상반기에는 삼성생명 POC와 드로잉런 SDK를 KMP로 배포하고, Navi SDK에 `setLanguage` API와 공통 에러 처리 구조 적용
- 잘된 점: KMP/CMP 관점을 우선 고려하는 습관, 공통 모듈화로 유지보수 효율과 상호운용성 개선
- 부족한 점: SDK 중심 경험이라 **CMP 애플리케이션 프로젝트 경험이 부족**
- 계획: 개인 학습으로 CMP 앱 개발 방식 보완, 공통 모듈화 범위 확대

→ [[kmp-cmp-adoption]]

## 성과 3. AI 도입을 통한 업무 생산성 개선

- 달성: 1분기는 팀 플랜 도입 직후라 실무 적용 기반(Team Skills, Claude.md, MCP) 마련에 집중. 상반기에는 Codex·Gemini 활용 개발, Jira 티켓 자동화, 스펙/ADR 선문서화 후 AI 협업, 셀 Wiki 서브모듈로 문서 이관
- 어려움: 팀 공통 Skills와 MCP가 정착되지 않아 개인별 편차(1분기에 상당 부분 해소했다고 기록)
- 계획: AI Team Skill 체계 정비, 공통 워크플로우 구축, 비개발 Jira 티켓 유지보수 자동화와 AI 번역 프로세스 개선

→ [[ai-doc-first-development]]

## 1분기 하향 1차 평가 요지 (셀 리더)

- 성과 1: 도전적인 영역을 끝까지 책임지고 완료한 점을 높이 평가. "배포 프로세스 전문가로 성장하는 것 같다". 쌓인 경험을 조직에 공유해 달라는 요청
- 성과 2: KMP 유지보수와 멀티플랫폼 First 관점을 잘 유지. 다음 CMP 프로젝트에서도 기대
- 성과 3: 다양한 모델을 실험해 작업 시간을 줄인 점이 인상적. AI로 더 적극적인 개발자가 되길 기대

상반기 하향 평가는 문서 작성 시점에 작성 예정이었다.

## 두 분기 비교에서 보이는 흐름

1분기 자체 평가는 "기반 마련"과 "유지보수" 중심이었고, 상반기에는 SDK 배포 실적과 구체 API 이름이 들어갔다. CMP 앱 경험 부족과 배포 복잡도는 두 번 모두 같은 어려움으로 반복해서 적혀 있다. ^[inferred]

## Sources

- [[_raw/_archived/2026_1분기_성과점검_이동은.md]] — 1분기
- [[_raw/_archived/2026_상반기_성과점검_이동은.md]] — 상반기
