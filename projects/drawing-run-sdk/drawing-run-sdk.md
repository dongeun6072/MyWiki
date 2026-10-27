---
title: >-
    삼성생명 드로잉런 SDK
category: project
tags: [drawing-run-sdk, sdk, kmp, tracking, visibility/internal]
aliases: [드로잉런 SDK, Drawing Run SDK, 삼성생명 POC]
relationships:
  - target: "[[kmp-cmp-adoption]]"
    type: uses
sources:
  - ~/Develop/Wiki/_raw/articles/inavi/2026_상반기_목표_주요업무_정리.md
  - ~/Develop/Wiki/_raw/articles/inavi/2026_직무 기술서_이동은.docx
  - url:https://inavisystems.atlassian.net/wiki/spaces/2Ozy8QblnTwf/overview
summary: >-
    삼성생명 고객사용 러닝 트래킹 SDK. POC에서 시작해 KMP로 Android/iOS를 동시에 배포한 2026년 프로젝트의 진행 이력.
provenance:
  extracted: 0.88
  inferred: 0.12
  ambiguous: 0.00
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T09:20:33+09:00
updated: 2026-10-27T14:00:00+09:00
snapshots:
  - "[[_raw/_archived/2026_상반기_목표_주요업무_정리|2026_상반기_목표_주요업무_정리]]"
  - "[[_raw/_archived/2026_직무 기술서_이동은.docx|2026_직무 기술서_이동은.docx]]"
---

# 삼성생명 드로잉런 SDK

러닝 트래킹 기능을 제공하는 SDK로, 삼성생명 POC로 시작해 정식 SDK로 이어졌다. Kotlin Multiplatform으로 새로 설계해 Android와 iOS에 모두 배포했다. 개발은 [[이동은]]이 담당했다. 같은 시기 [[orbis-sdk]]도 병행했다.

## 진행 이력 (2026)

| 시점 | 내용 |
|---|---|
| 2026-03 | 삼성생명 POC 시작. 이후 빠른 iOS 대응을 위해 처음부터 KMP 프로젝트로 구성하고 공통 기능은 KMP 라이브러리로 개발 |
| 2026-04 | 요구사항 기능 개발 완료. SDK 배포 구성과 테스트용 내부 배포가 필요했고, 비정상 수치 값에 대한 예외 처리와 튜닝이 남아 있었다. 요구사항 명세를 기반으로 Jira 티켓 자동화도 진행 |
| 2026-05-26 | Android, iOS 배포 완료. 데모 앱은 Compose UI로 배포 |
| 2026-06 | 세션 종료(`stop`)와 일시정지(`pause`)를 분리하고 전체 초기화 `reset()` API를 공통 모듈로 구현. Android/iOS 공통 트래킹 로직 이슈 대응, 인입 이슈 대응 |
| ~2026-07 | 1.0.1 배포, 고객사 연동 가이드 제공 (기간 2026-04-01 ~ 07-01) |

## 상세 문서 (Confluence "삼성생명 드로잉 런" 스페이스 전체 반영)

Confluence 스페이스(20페이지)를 주제별로 정리했다. 2026-02 PoC 검토에서 시작해 04월 론칭 SDK로 범위가 바뀌고, 07월에는 고객사의 건강 중심 피봇 때문에 2차가 보류된 흐름이다.

| 문서 | 내용 |
|---|---|
| [[drawing-run-poc-course-generation-review-2026]] | 코스 생성 PoC 방안 비교와 구현 가능/불가 검토 (2~3월) |
| [[drawing-run-sdk-launch-scope-and-data-items-2026]] | 1차 범위, 역할 분담, 러닝 데이터 항목, 필요 권한과 구현 방법 (4월) |
| [[drawing-run-sdk-scrum-2026-04-to-05]] | 스크럼 4회, 고객사 질의 회신(minSdk 26, iOS 15 등), 일정 연기 |
| [[plus-run-external-tech-review-2026]] | 한화금융 PLUS RUN 외부 관찰 기반 Mapbox·음성안내 추정 |
| [[drawing-run-course-guidance-data-flow-2026]] | GPX → 안내데이터 → SDK 주행 15단계 흐름과 API |
| [[drawing-run-phase2-voice-guidance-and-meetings-2026]] | 2차 개발 항목, 음성 안내 협의, 7월 회의록 |
| [[drawing-run-sdk-release-history-2026]] | 1.0.0 ~ 1.0.2 배포 이력 |
| [[drawing-run-slack-dev-channel-2026]] | 내부 슬랙 채널 연표(2~10월): 범위 변경, 배포, 고객 서비스 오픈과 방향 변경, 후속 수요 |
| [[drawing-run-sdk-integration-qna-2026]] | 고객 연동 문의와 대응: pause/resume 사양, 프로가드, 포그라운드 서비스, iOS 위치 수신, 버전 요건 |

## 특징

- SDK 중심 프로젝트라서 **Compose 경험은 데모/샘플 앱을 Compose UI로 만들며 쌓았다.** CMP 애플리케이션 프로젝트 경험은 부족하다고 스스로 평가했다([[2026-performance-review-selfeval]]).
- KMP 도입 과정과 교훈은 [[kmp-cmp-adoption]]에 정리했다.
- AI 협업 방식은 [[ai-doc-first-development]]를 본다.

## Open Questions

- 고객사 이슈 내용은 슬랙 채널로 확인했다([[drawing-run-sdk-integration-qna-2026]]). 1.0.2 이후 버전 계획은 여전히 없고, 10-13 문의(Kotlin 2.0.0 / AGP 8.7.1 최소 버전, 스탠드얼론 제공)의 회신도 채널에 없다.
- 2차(안내데이터, 음성 안내)는 10-15까지 진행 기록이 없다. 고객사는 2026-08 말 "맞춤형 달리기"(건강정보 연동) 서비스를 오픈해 방향이 바뀌었다. ^[inferred]
- 삼성화재의 GPS 수집·맵매칭 SDK 추가 계획은 9월 초 논의 예정이었으나 결과가 채널에 없다.

## Sources

- [[_raw/_archived/2026_상반기_목표_주요업무_정리.md]] — 월별 체크인
- [[_raw/_archived/2026_직무 기술서_이동은.docx]] — 프로젝트 요약(수행기간)
- 슬랙 `#011_삼성생명_드로잉런_dev` 전체(2026-02-23~10-15) — 2026-10-27 반영, 서버·키·라이선스 키 미수록
- [Confluence 스페이스 삼성생명 드로잉 런](https://inavisystems.atlassian.net/wiki/spaces/2Ozy8QblnTwf/overview) — 가져온 날짜 2026-10-26, 20페이지 전부 반영(상세 문서 7개)
