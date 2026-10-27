---
title: >-
    2026 목표와 주요업무 체크인
category: references
tags: [career, goals, okr, visibility/internal]
aliases: [2026 상반기 목표, 2026 주요업무 정리]
relationships:
  - target: "[[이동은]]"
    type: related_to
sources: [~/Develop/Wiki/_raw/articles/inavi/2026_상반기_목표_주요업무_정리.md]
summary: >-
    2026년 연간 목표 3개와 주요업무 2개의 진척도와 2~6월 체크인 요약. 모빌리티개발셀 상위 목표와의 연결도 포함한다.
provenance:
  extracted: 0.93
  inferred: 0.07
  ambiguous: 0.00
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T09:20:33+09:00
updated: 2026-10-26T09:20:33+09:00
snapshots:
  - "[[_raw/_archived/2026_상반기_목표_주요업무_정리|2026_상반기_목표_주요업무_정리]]"
---

# 2026 목표와 주요업무 체크인

인사평가시스템에 [[이동은]]이 직접 쓴 체크인을 정리한 문서다(기간 2026-01-01 ~ 12-31, 2026-06-24 기준). 체크인 주기는 대략 월 1회다.

## 목표 3개

| 목표 | 상위 목표(모빌리티개발셀) | 진척도 | 궤적 |
|---|---|---|---|
| 1. KMP/CMP 기반 멀티플랫폼 프로젝트 전환 | 프로덕트 상품성 강화 및 R&D | 50% | 15 → 20 → 30 → 40 → 50 |
| 2. AI 도입을 통한 업무 생산성 개선 | 개발/운영 비용 절감 | 50% | 15 → 20 → 30 → 40 → 50 |
| 3. 고객사 프로젝트 요구사항 및 일정 준수 | Partnership SI 사업 수행 | 50% | 15 → 20 → 30 → 40 → 50 |

- 목표 1 상세: 레거시 프로젝트에 KMP 모듈 적용, 비즈니스 로직 일부 통합, Compose 화면 통합 → [[kmp-cmp-adoption]]
- 목표 2 상세: 비개발 JIRA 티켓 유지보수 자동화 검토, AI 번역 프로세스 개선 → [[ai-doc-first-development]]
- 목표 3 상세: 해외향 Navi SDK(Phase-1 1월 iOS SDK 출시, Phase-2 고도화), 국내향 Navi SDK(Phase-1 Flutter 플러그인), 해외향 Maps SDK(Phase-1 출시) → [[orbis-sdk]]

## 주요업무 2개

| 업무 | 진척도 | 내용 |
|---|---|---|
| 1. CMP 역량 강화 | 30% | KMP 역량(프로젝트 유지보수, Global Map SDK KMP 검토), Compose 역량(드로잉런 샘플/데모 앱을 Compose UI로) |
| 2. 아이나비 에어 정기 업데이트 대응 | 45% | 신규 OS, 유지보수·업체 협업, Android Auto 최신 라이브러리 대응. 월별 내용은 [[inavi-air-feature-history]] |

## 월별 핵심 (요약)

| 시점 | 주요 사건 |
|---|---|
| 2월 | Global Maps SDK 기능 개발(좌표 변환과 이벤트 콜백 제외 완료), 국내향 Java → Kotlin 전환 |
| 3월 | 해외향 Maps SDK 출시(IMPS 가이드, Demo 앱), Navi SDK 트럭향 API와 v1.0.2, 삼성생명 POC 시작 |
| 4월 | 드로잉런 SDK 기능 개발 완료, Navi SDK 리팩토링, Jira 티켓 자동화 |
| 5월 | 드로잉런 SDK Android/iOS 배포, Flutter Plugin Step 1 배포, Navi SDK v1.0.3 |
| 6월 | Navi SDK 다국어·`setLanguage`·Web 인증 Style, Maps SDK 웹 인증 Style, KMP 공통 트래킹 이슈 대응, AI 스펙 문서를 셀 Wiki로 이관 |

프로젝트별 상세는 [[drawing-run-sdk]], [[orbis-sdk]]에 있다.

## 해석

세 목표가 [[orbis-sdk]]와 [[drawing-run-sdk]]에서 겹친다. 같은 작업이 "고객사 대응(목표 3)", "KMP 전환(목표 1)", "AI 활용(목표 2)"에 모두 체크인으로 등장한다. ^[inferred]

## Sources

- [[_raw/_archived/2026_상반기_목표_주요업무_정리.md]] — 목표와 체크인 원문
