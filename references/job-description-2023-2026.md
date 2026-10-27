---
title: >-
    직무기술서 (2023, 2026)
category: references
tags: [career, job-description, android, visibility/pii]
aliases: [직무 기술서, 직무기술서 이동은]
relationships:
  - target: "[[이동은]]"
    type: related_to
sources:
  - ~/Develop/Wiki/_raw/articles/inavi/직무기술_이동은.doc
  - ~/Develop/Wiki/_raw/articles/inavi/2026_직무 기술서_이동은.docx
summary: >-
    2023-06과 2026-09에 작성한 직무기술서 비교. 담당 업무가 에어 앱 유지보수에서 KMP 기반 SDK 개발과 앱 개발로 확장된 과정과 직무 요건을 정리했다.
provenance:
  extracted: 0.90
  inferred: 0.10
  ambiguous: 0.00
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T09:20:33+09:00
updated: 2026-10-26T09:20:33+09:00
snapshots:
  - "[[_raw/_archived/2026_직무 기술서_이동은.docx|2026_직무 기술서_이동은.docx]]"
  - "[[_raw/_archived/직무기술_이동은.doc|직무기술_이동은.doc]]"
---

# 직무기술서 (2023, 2026)

[[이동은]]이 작성한 직무기술서 두 편이다. 학력 같은 인적사항은 옮기지 않았다.

## 2023-06-30 버전 (연구원)

- **소속**: 모빌리티Tech그룹 / 모빌리티개발셀
- **담당 업무**: 아이나비 에어 개발·유지보수, 아이나비 3D Streaming 개발·유지보수
- **언어/지식**: Java, Kotlin, Android 앱 기반, REST API 개발 지식
- **도구**: Android OS, Git, Slack, Jira, Figma, Confluence, Notion
- **주요 수행 직무**: iNavi 에어 Android(2022~현재), iNavi 3D Streaming의 AOS 외부포팅 MXI·아트뷰(2022~2023), iNavi Maps SDK 데모 앱(2022)

## 2026-09-18 버전 (Android 앱 개발)

- **소속**: MX그룹 / 모빌리티개발셀
- **한 줄 정의**: Kotlin·Jetpack Compose로 모바일 앱의 요구사항 분석, 설계, 구현, 테스트, 스토어 배포, 운영 대응까지 수행
- **Top 3 업무**: ① 해외향/국내향 Navi SDK와 Maps SDK를 KMP 기반 멀티플랫폼으로 설계·개발·배포·고객사 이슈 대응 ② 아이나비 에어 정기 업데이트와 유지보수 ③ 삼성생명 드로잉런 SDK, Navi SDK Flutter Plugin, 서울 동행맵 등 요구사항 분석과 일정 준수
- **핵심 산출물**: Navi/Maps SDK 배포 패키지(AAR, XCFramework)와 버전별 릴리즈, 에어 앱 업데이트, SDK 연동 가이드/Reference, 설계 문서(ADR, 아키텍처)

### 요건 자체 평가

| 항목 | 수준 |
|---|---|
| Kotlin/Java | 상 |
| KMP, CMP 아키텍처 이해와 적용 | 상 |
| 지도/내비게이션 SDK 도메인 지식 | 중 |
| Android Studio, Git/GitHub | 상 |
| Jira/Confluence/Slack, Figma | 중 |
| AI Tool 활용 | 3~4단계 ([[ai-doc-first-development]]) |

가장 중요한 역량으로 커뮤니케이션, 문제해결, 협업, 자기주도성, 문서작성을 꼽았다.

### 협업과 업무 방식

- 협업 우선순위: 모빌리티개발셀 리더, PM, 디자인/기획 부서(UX·PRD)
- 일부 업무는 승인이 필요하고 PM과 셀 리더에게 확인한다.
- 조직 성향: 실험·개선 지향, 협업 중심, 자율·위임, 문서화 중심, 프로젝트성 업무가 많음
- 직무 표준화 수준은 "보통"
- 담당자 부재 시 대체자가 알아야 할 것: 셀 공용 Wiki의 ADR·아키텍처 문서, 배포 프로세스, 프로젝트 컨벤션과 운영 규칙
- 리스크: 고객사·파트너사 요구사항과 이슈 대응이 잦고, 단말·도메인 특성상 현장 재현이 불가능한 이슈가 있다.

### 최근 5년 프로젝트

| 프로젝트 | 기간 | 내용 |
|---|---|---|
| 해외향 Navi SDK | 2025-01 ~ 2025-10 | WBS 수립, 검색·경로탐색·TTS·DP 구현, 대만 실주행 테스트, 전시회 대응, KMP 전환 → [[orbis-sdk]] |
| 아이나비 에어 정기 업데이트 | 2022-09 ~ 진행중 | 정기 릴리스, 신규 기능, 유지보수 → [[inavi-air-feature-history]] |
| 해외향 Maps SDK | 2025-12 ~ 2026-03 | MapLibre 기반 지도 SDK 출시 |
| 삼성생명 드로잉런 SDK | 2026-04 ~ 2026-07 | KMP 러닝 트래킹 SDK, 1.0.1 배포 → [[drawing-run-sdk]] |
| Flutter Plugin | 2026-04 ~ 2026-05-26 | 스펙·ADR 선작성 후 Navi/Map Flutter Plugin 배포 |
| 서울 동행맵 앱 | 2026-06 ~ 진행 중 | CMP 단일 코드베이스, 접근성 요구를 화면 단위로 충족 |

## 두 버전의 변화

- 에어 앱 유지보수 한 가지에서 **SDK 설계와 배포, 멀티플랫폼, 신규 앱 개발**로 역할이 넓어졌다.
- 도구 목록에 AI와 KMP/CMP가 들어왔고, 문서화가 대체 업무 인계의 핵심으로 자리 잡았다.

## Sources

- [[_raw/_archived/직무기술_이동은.doc]] — 2023 직무기술서
- [[_raw/_archived/2026_직무 기술서_이동은.docx]] — 2026 직무기술서
