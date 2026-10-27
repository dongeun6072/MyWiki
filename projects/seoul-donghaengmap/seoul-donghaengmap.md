---
title: >-
    서울동행맵 고도화 사업
category: project
tags: [seoul-donghaengmap, accessibility, cmp, public-sector, visibility/internal]
aliases: [서울동행맵, 서울동행맵 고도화, 동행맵, 서울시 교통약자지원 통합플랫폼]
relationships:
  - target: "[[kmp-cmp-adoption]]"
    type: uses
sources:
  - ~/Develop/Wiki/_raw/articles/project-seoul/README.md
  - ~/Develop/Wiki/_raw/articles/project-seoul/Repo 구조도/동행맵 Repo 구조도.png
summary: >-
    서울시 교통약자 이동 지원 앱 서울동행맵을 AI 음성 안내, 교통약자 맞춤 경로, 저상버스 예약, 지하철 실내 내비로 고도화하는 12개월 사업(2026-06~2027-06)의 허브 페이지.
provenance:
  extracted: 0.80
  inferred: 0.20
  ambiguous: 0.00
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: core
created: 2026-10-26T09:31:30+09:00
updated: 2026-10-27T15:30:00+09:00
snapshots:
  - "[[_raw/_archived/README|README]]"
  - "[[_raw/_archived/동행맵 Repo 구조도.png|동행맵 Repo 구조도.png]]"
---

# 서울동행맵 고도화 사업

서울시 교통약자지원 통합플랫폼(서울동행맵)의 앱과 서버를 고도화하는 사업이다. 고령자와 장애인 등 교통약자의 **대중교통 접근성과 이동 편의**를 높이는 것이 목적이고, 기존 앱 위에 AI 음성 안내, 교통약자 맞춤 경로 탐색, 저상버스 예약, 시각장애인 전용 모드, 지하철 역사 실내 내비게이션을 얹는다. 개발 담당 중 앱 쪽은 [[이동은]]이 맡고 있다(CMP 단일 코드베이스, 2026-06~). ([[job-description-2023-2026]])

## 사업 개요

| 항목 | 내용 |
|---|---|
| 발주 | ㈜티머니 (서울시 미래첨단교통과 감독) |
| 수행 | 아로정보기술 컨소시엄 (아이나비시스템즈, LBS테크 참여) |
| 기간 | 착수일부터 12개월. WBS 기준 2026-06-23 ~ 2027-06-22 |
| 예산 | 23억 원(VAT 별도) |
| 단계 | 1단계 개발 후 시범 서비스(2026-07~2027-01), 2단계 구현·검증(2027-01~06) |
| 앱 기반 | 기존 서울동행맵(Flutter, 카카오맵) 위에 새로 만든다. ([[seoul-donghaengmap-existing-app-v2]]) |

## 문서 지도

| 주제 | 페이지 |
|---|---|
| 과업 범위와 요구사항 | [[seoul-donghaengmap-rfp]] |
| 기술협상 결과, 착수보고 | [[seoul-donghaengmap-negotiation-kickoff]] |
| 기존 앱 분석 (v2.2.1 실기기 탐색) | [[seoul-donghaengmap-existing-app-v2]] |
| 기능명세(62건), 백엔드/SDK 요구 | [[seoul-donghaengmap-functional-spec]] |
| 화면 기획서 v1.0, 메뉴 구조 | [[seoul-donghaengmap-screen-design]] |
| 디자인 컨셉, 디자인 가이드 | [[seoul-donghaengmap-design-system]] |
| 앱서버 개발 환경, DB 테이블 | [[seoul-donghaengmap-backend-env]] |
| LBS테크 협업(보행 경로 서버, 내비 SDK) | [[seoul-donghaengmap-lbs-collaboration]] |
| 일정(WBS) | [[seoul-donghaengmap-wbs]] |
| 지하철역 실내내비 난이도 등급 | [[seoul-subway-station-grade]] |
| 테스트 케이스 512건 | [[seoul-donghaengmap-testcases]] |
| 설계단계 감리 결과 | [[seoul-donghaengmap-design-audit]] |
| 앱 보안 취약점 진단 | [[seoul-donghaengmap-app-vulnerability-reports]] |
| 관련 법령·지침(접근성, 모바일 전자정부) | [[korean-public-mobile-app-compliance]] |

- 2026년 메일(수주, 컨소시엄 R&R, 앱 이관, 실내 내비 역 확정): [[seoul-donghaengmap-mail-2026]]

### 슬랙 채널 (2026-07~10, 2026-10-27 반영)

| 채널 | 페이지 |
|---|---|
| `#005_서울동행맵_dev` (내부 개발) | [[seoul-donghaengmap-dev-slack-process-2026]] (AI-flow, 저장소 구조, WBS·Jira, 감리, 스토어·계정, 정책 결정), [[seoul-donghaengmap-dev-slack-tech-2026]] (CMP 스택, OpenAPI·인증·암호화, 시연 연동 29개 API) |
| `#10_prj-서울동행맵고도화` (PM·기획) | [[seoul-donghaengmap-pm-slack-2026]] (서울시 협의 연표, 기획서 v0.7~v1.0, 백엔드 협업 방식, Mapxus) |
| `#ext-서울동행맵-컨소시엄-협업` | [[seoul-donghaengmap-consortium-slack-2026]] (LBS테크 SDK·음성 규격, 브로디언 DB·API·역할 분담, 감리 문서) |
| `#ext-서울동행맵-파파야-협업` | [[seoul-donghaengmap-papaya-slack-2026]] (측위 SDK·Fusion SDK, 판교역 테스트 이슈, 시청역 시연 대비) |

## 진행 현황 요약 (2026-10-27 기준, 슬랙)

- 일정: 서울시 시연용 앱 통합 11-13, 단위 기능 개발 완료 목표 12-18, 교통과장 보고 11월 3주차, 시청역 사전 점검 11-11~12, 2차 앱스토어 등록 2027-06-14~16으로 변경.
- 감리: 설계 단계 1차 감리를 10-7~15에 진행했고 최종 결과 보고서가 10-26에 나왔다.
- 앱: Compose Multiplatform(Kotlin 2.4, AGP 9.3), Android 10/iOS 16 이상, 지도는 사내 iNavi Maps SDK. 가로 모드는 삭제, 1:1 문의는 '의견 보내기'(수집 전용)로 복원.
- 서버: 백엔드 협력사(브로디언)와 역할을 나눠 앱은 아이나비 App Server만 호출한다. 시연은 29개 API 중 14개 실연동, 11개 목업, 나머지 구현 대기.
- 실내 내비: 파파야 측위·경로탐색 API로 판교역을 시험 중이며 위치 오차, 층 전환 지연, 승강장 POI 부재가 남아 있다. 서울시에 "Android만 가능한 이유" 설명이 필요하다.

## 협업 저장소 구조

팀은 **위키를 중심에 두고 각자의 AI(Claude)가 위키를 읽어 역할별 산출물을 만드는 방식**으로 일한다. 저장소 구조도(`동행맵 협업 Repo 구조`)는 다음과 같다.

- **위키 층**: `projects/`(프로젝트 허브), `specs/`(상세 사양·운영), `entities/`(고객사·기술), `concepts/`(개념), `queries/`(Q&A 아카이브), 그리고 `index.md`, `log.md`, `ingested-files.md`
- **산출물 층(역할별)**: PRD, UX, Design, `Appsource`(앱), `Svrsource`(서버)
- **외부 자료**: `Documents/` — 외부에서 받은 원본이며 읽기 전용이다. 수정하지 않고 위키로 ingest하는 원본으로만 쓴다. 이 vault의 `_raw/articles/project-seoul/`이 그 사본이다.
- **원칙**: 코드는 ingest 대상이 아니고, 설계·구현 결정은 ADR로 위키에 기록한다. 규칙의 단일 원본은 `CLAUDE.md`, 브랜치는 `develop` 하나만 쓰고 작업 전 `git pull`을 먼저 한다. 커밋과 푸시는 명시 요청이 있을 때만 한다.
- **도구**: `.claude/skills/`(위키 ingest·query·lint·adr, git push·commit·pr·review), `scripts/`

이 방식은 [[ai-doc-first-development]]에서 정리한 "선문서화 후 AI 협업"을 팀 단위로 확장한 구조다. ^[inferred]

## 핵심 쟁점 (감리·착수보고 기준)

- 실내지도: RFP는 10개 역 시범 후 전 역사 확대였으나, 1단계 평가 후 2단계 범위를 정한다. ([[seoul-subway-station-grade]])
- 외부 연계 일정: 서울시 데이터센터 입주, 하드웨어(GPU) 가격, 티머니GO 마일리지, 3기 BMS 연계가 미해결 이슈다. ([[seoul-donghaengmap-design-audit]])
- 접근성: 모바일 접근성 인증마크 획득을 협상에서 수용했다. ([[seoul-donghaengmap-negotiation-kickoff]], [[korean-public-mobile-app-compliance]])

## Open Questions

- 시연 직결 쟁점: 경로탐색·통합검색 API 규격, 3사 POI ID 체계 통일, 대중교통 구간 안내 주체(SDK 대 앱), 외부망 접속과 HTTPS. 상세는 [[seoul-donghaengmap-dev-slack-tech-2026]].
- 서울시 10-28 미팅 결과(설계 변경안, 추가 구축 역사 15개 여부, 2027-01 시범 서비스 범위)는 슬랙에 아직 없다.
- 이 vault는 `_raw/articles/project-seoul/`의 일부(핵심 프로젝트 문서)만 정리했다. 대형 규정집과 화면기획서 구버전은 아직 수집하지 않았다.

## Sources

- [[_raw/_archived/Outlook_2026.md]] — 2026 업무 메일(동행맵 수주·진행)
- [[_raw/_archived/README.md]] — 외부 전달 자료 폴더 안내
- [[_raw/_archived/동행맵 Repo 구조도.png]] — 협업 저장소 구조도
- 슬랙 `#005_서울동행맵_dev`, `#10_prj-서울동행맵고도화`, `#ext-서울동행맵-컨소시엄-협업`, `#ext-서울동행맵-파파야-협업` 전체(2026-07~10-27) — 2026-10-27 반영. 서버·계정·키·토큰·링크 미수록
