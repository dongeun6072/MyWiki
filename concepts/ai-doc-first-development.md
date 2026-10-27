---
title: >-
    선문서화 후 AI 협업 개발
category: concepts
tags: [ai, documentation, adr, workflow, visibility/internal]
aliases: [문서 먼저 AI 협업, spec-first AI development]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - ~/Develop/Wiki/_raw/articles/inavi/2026_상반기_목표_주요업무_정리.md
  - ~/Develop/Wiki/_raw/articles/inavi/2026_상반기_성과점검_이동은.md
  - ~/Develop/Wiki/_raw/articles/inavi/2026_1분기_성과점검_이동은.md
summary: >-
    AI에게 코드를 바로 요청하던 방식에서 기능 스펙과 ADR을 먼저 문서화하고 AI와 협업하는 방식으로 바꾼 사례와 그 효과, 팀 표준화 과제.
provenance:
  extracted: 0.75
  inferred: 0.25
  ambiguous: 0.00
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T09:20:33+09:00
updated: 2026-10-26T09:20:33+09:00
snapshots:
  - "[[_raw/_archived/2026_상반기_목표_주요업무_정리|2026_상반기_목표_주요업무_정리]]"
  - "[[_raw/_archived/2026_상반기_성과점검_이동은|2026_상반기_성과점검_이동은]]"
  - "[[_raw/_archived/2026_1분기_성과점검_이동은|2026_1분기_성과점검_이동은]]"
---

# 선문서화 후 AI 협업 개발

모빌리티개발셀의 2026년 목표 "AI 도입을 통한 업무 생산성 개선"(진척도 50%)에서 나온 핵심 교훈이다.

## 문제와 전환

| 방식 | 결과 |
|---|---|
| **이전**: AI에 코드 생성을 바로 요청, 문서화 없이 개발 | 코드 패턴이 일관되지 않고 요구사항을 정확히 반영하지 못함 |
| **전환(2026-05, Flutter Plugin 개발부터)**: 기능 스펙과 아키텍처 결정 기록(ADR)을 `docs` 폴더에 사전 작성 → 이를 바탕으로 AI와 협업 | 코드 패턴 일관성과 요구사항 반영 정확도 개선 |

이후 AI 기반 스펙/설계 문서화로 개발 히스토리를 쓰고, 설계 문서와 ADR, 아키텍처 문서를 **셀 공용 Wiki 서브모듈**로 옮겼다. 이 문서화 결과물이 담당자 부재 시 대체 인력에게 전달할 핵심 자료이기도 하다([[job-description-2023-2026]]).

## 활용 사례

- Codex, Gemini, Claude로 Global Maps SDK 개발, 국내향 Java 로직의 Kotlin 전환과 리팩토링, 삼성생명 POC 기능 개발(모듈화 영역 제외)에 활용해 개발 시간 단축 ([[orbis-sdk]], [[drawing-run-sdk]])
- 요구사항 명세를 기반으로 Jira 티켓 자동화
- 직무기술서에는 AI Tool 활용 수준을 3~4단계로 자체 평가

## 팀 차원의 과제

- 1분기: AI Agent 팀 플랜이 도입되면서 단기 성과보다 **실무 적용 기반**(Team Skills, Claude.md, MCP)을 만드는 데 집중
- 도입 초기에는 팀 공통 Skills와 MCP 같은 표준 활용 방식이 없어 개인별 편차가 있었고, 이후 팀 공통 구성을 정비해 상당 부분 해소
- 남은 과제: 신규 도구와 활용 사례의 팀 전체 공유와 정착, 비개발 Jira 티켓 유지보수 자동화, AI 기반 번역 프로세스 개선

## 해석

이 vault 자체(LLM Wiki)도 같은 흐름의 연장선으로 볼 수 있다. 문서화한 지식을 AI가 다시 읽어 일관된 작업을 하게 하는 구조다. ^[inferred]

## Open Questions

- 코드 정확도 개선 정도는 정량 수치 없이 정성 평가만 있다.

## Sources

- [[_raw/_archived/2026_상반기_목표_주요업무_정리.md]] — 목표 2 체크인
- [[_raw/_archived/2026_상반기_성과점검_이동은.md]] — 성과 3 자체 평가
- [[_raw/_archived/2026_1분기_성과점검_이동은.md]] — 1분기 AI 도입 현황
