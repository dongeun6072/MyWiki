---
title: >-
    신 NaviSDK 개발 스프린트 전 기간 요약 타임라인 (2024-10~2026-05)
category: references
project: orbis-sdk
tags: [navisdk, sprint, timeline, kmp, visibility/internal]
aliases: [NaviSDK 스프린트 타임라인, 신 NaviSDK 스프린트 요약]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/567869491
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/638976150
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/837517343
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1932722177
summary: >-
    신 NaviSDK 스프린트 42개 페이지를 단계별로 묶은 표 형태의 시간순 요약. 각 단계의 목표, 핵심 결정, 상세 페이지 링크.
provenance:
  extracted: 0.88
  inferred: 0.10
  ambiguous: 0.02
base_confidence: 0.6
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T13:00:00+09:00
updated: 2026-10-26T13:00:00+09:00
---

# 신 NaviSDK 개발 스프린트 전 기간 요약 타임라인 (2024-10~2026-05)

신 NaviSDK(KMP 기반) 스프린트 페이지를 단계별로 묶은 요약이다. 세부는 각 단계 문서에 있다. 허브: [[sdk-sprints-2024-2025-hub]]. 기존에 작성된 더 짧은 요약은 [[navisdk-confluence-sprint-timeline-2024-2026]]이다.

## 단계별 타임라인

| 기간 | 단계 | 목표 | 핵심 결정/사건 | 상세 |
|---|---|---|---|---|
| 2024-10-23 | 초기 환경 구성 | 프로젝트 환경 세팅 | Core는 Bitbucket, 테스트용은 기존 Repo, Sample은 차후 GitHub | [[sdk-sprint-initial-setup-architecture-modules-2024-q4]] |
| ~2024-11-11 | Architecture 정의 | SDK Architecture 구성 방안 | NaviCore 3rd Party 공개 수준 이슈 제기 | 같은 문서 |
| 2024-11-13~11-19 | 초기 모듈 구성 | 초기 엔진(Static Lib) IF, 통신 모듈 | API만 공개(Android/iOS), iOS 엔진은 1개 framework, 통신은 ktor만 사용 | 같은 문서 |
| 2024-11-21~12-02 | 초기 지도 표출 | 로컬지도 다운로드 후 표출/제스처 | 통신 모듈 다운로드·unzip(Okio), Lib 통합, 인증 로직 개발 | [[sdk-sprint-initial-map-display-2024-q4]] |
| 2024-12-04~12-16 | 내부 API 설계 | 통합검색, 길찾기, DP 경로선, Core 연동 구조, Auth/권한 | NaviMainThread 필요 여부 논의, Presentation/Core Layer 구조, suspend 미사용 | [[sdk-sprint-internal-api-design-2024-12]] |
| 2025-01-06~02-03 | KMP Base 로직 강화 #1~#4 | NaviMainThread 세분화, SMR/MMC 연동, runRoute | INaviController 역할 정리 완료(1/13) | [[sdk-sprint-kmp-base-logic-2025-01]] |
| 2025-02-05~02-24 | 주행 Feature 및 API 개발 #1~#3 | 주행 컴포넌트(TBT), 검색/길찾기 API | iOS 모의주행 정지 원인(NSTimer), 공통 리소스 관리 검토, orda/tomtom MW 대응 병행 | [[sdk-sprint-driving-feature-api-2025-02]] |
| 2025-02-27 | 개발 진행 현황 | 6단계 로드맵 | 구조 설계 → 데이터 연동 → Base 강화 → Feature → UI → 기타(Flutter, 다국어) | [[sdk-development-progress-board-and-2026-scrums]] |
| 2025-03-04~03-26 | 대만향 개발계획, 구조설계/초기세팅, TomTom API/SDK 검토 | 해외향 개발 구조 결정, TomTom SDK/API 검토 | 구조설계 완료 티켓 7개 | [[sdk-sprint-taiwan-plan-and-structure-2025-03]] |
| 2025-03-31~05-12 | 엔진(지도/검색/탐색) API 연동 #1~#3 | TomTom Maps SDK 컨트롤, 엔진 API 연동, 화면별 GUI | Search API 사용(MapsSDK-Search 미사용), 자차 마커 *.glb, TBT 입력은 메인에서 처리 | [[sdk-sprint-engine-api-integration-2025-03-05]] |
| 2025-05-12~06-09 | 메인상태관리 & 화면구성 #1~#3 | 메인 상태 관리, GUI, 초기 지도 다운로드, IPO 실사 대응 산출물 | 안내(TBT) 완료, OrbisMap 미제공으로 자체 구축/MapLibre 검토, 톰톰 캐싱 정책 보류 | [[sdk-sprint-main-state-and-screens-2025-05-06]] |
| 2025-11-19 | NaviSDK 상품화 #4 | iOS NaviSDK/MapsSDK 서비스 | 25Q4 iOS NaviSDK, 26Q1 MapsSDK 로드맵 | [[sdk-development-progress-board-and-2026-scrums]] |
| 2026-05-14 | SDK Flutter 대응 #2 | Flutter 대응, 1.0.3 준비 | Step 1/2 일정, UniqueKey(UUID) 통계 | 같은 문서 |

## 인원/역할 구성 변화
- 2024-10~12: 앱 개발자 1~3과 [[이동은]]
- 2025-03-26: 스크럼에 번역 담당 등장
- 2025-04-02 이후: 디자이너, 번역 담당이 스크럼에 참여
- 2025-06-04: 앱 개발자 3은 표에서 사라짐(표 3번 행 없음) ^[inferred]

## 반복 이슈 추적
| 이슈 | 시작 | 결과 |
|---|---|---|
| NaviCore 공개 수준 | 2024-11-11 | 11/13 API만 공개 |
| 통신 라이브러리 | 2024-11-13 | 11/19 ktor만 사용 |
| NaviMainThread 필요 여부, 동시성 | 2024-12-04 | 2025-02 현재도 동시성 이슈 확인 항목으로 유지 |
| 공통 리소스 관리(이미지, strings, 컬러) | 2025-02-05 | 2/24 가능 여부 확인 단계 |
| iOS 모의주행 정지 | 2025-02-05 | NSTimer를 Main Thread에서 생성 |
| 톰톰 지도 캐싱/렌더링 속도 | 2025-05-21 | 6/4 보류 |
| 2개 지도 표시 후 뒤로가기 ANR | 2025-05-21 | 6/4에도 이슈로 기록 |

## Related
- [[orbis-navisdk-architecture-and-flutter-plan]] — 아키텍처와 Flutter 계획
- [[orbis-navisdk-poc-prep-2025]] — PoC 준비
- [[orbis-sdk]]

## Sources
- Confluence "[10/23] 초기 환경 구성 - 스크럼" 외 스프린트 41개 페이지 (대표 pageId 567869491, 638976150, 837517343, 1932722177) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
