---
title: >-
    드로잉런 SDK 스크럼 #1~#4 (2026-04-16 ~ 2026-05-21, Confluence)
category: references
project: drawing-run-sdk
tags: [drawing-run-sdk, scrum, customer-qna, schedule, visibility/internal]
aliases: [드로잉런 SDK 스크럼, 260416 드로잉런 SDK #1, 260423 드로잉런 SDK #2, 260429 드로잉런 SDK #3, 260514 드로잉런 SDK #4, 스크럼 보드]
relationships:
  - target: "[[drawing-run-sdk]]"
    type: related_to
  - target: "[[drawing-run-sdk-launch-scope-and-data-items-2026]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/2Ozy8QblnTwf/pages/1873051652
  - url:https://inavisystems.atlassian.net/wiki/spaces/2Ozy8QblnTwf/pages/1873215490
  - url:https://inavisystems.atlassian.net/wiki/spaces/2Ozy8QblnTwf/pages/1894875180
  - url:https://inavisystems.atlassian.net/wiki/spaces/2Ozy8QblnTwf/pages/1907130396
  - url:https://inavisystems.atlassian.net/wiki/spaces/2Ozy8QblnTwf/pages/1915224141
summary: >-
    삼성생명 협의 기반 주간 스크럼 4회분. SDK 전달 희망일, 고객사 질의와 회신(OS 버전, 헬스 데이터, 고도 N/A, 랩 페이스 단위), 오픈 일정 연기, SDK 용량, 전달물 이름 규칙.
provenance:
  extracted: 0.92
  inferred: 0.06
  ambiguous: 0.02
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T15:00:00+09:00
updated: 2026-10-26T15:00:00+09:00
---

# 드로잉런 SDK 스크럼 #1~#4 (2026-04-16 ~ 05-21)

"스크럼 보드" 페이지(본문 없음) 아래에 격주~주간으로 쌓인 4개의 스크럼이다. 회차마다 Overview(기간, 범위, 논의 사항), Issue, To-do list 형식이다. 범위 칸은 비어 있다.

## 회차별 요약

| 회차 | 기간 | 핵심 |
|---|---|---|
| #1 (04-16) | 04-16 ~ 04-22 | SDK 전달 희망 일정 **5월 2주차(~5/15) 이내**, 일정 조정 1~2주 협의. 요구사항 상세(규격/포맷) 정의가 이슈 |
| #2 (04-23) | 04-23 ~ 04-29 | **기본 기능만 갖춰 모니모 앱과 연동 가능한 형태로 선제공 후 추가 업데이트**로 합의. 고객사 질의 회신 |
| #3 (04-29) | 04-30 ~ 05-07 | **오픈 일정 6월 중 → 6월 말** 연기. 오픈 서비스가 모니모인지 더헬스인지 논의 중. 앱 아이콘 제작 요청, SDK 용량 확인 |
| #4 (05-14) | 05-14 ~ 05-21 | 기획안 전달 일정 미정, **SDK 전달 요청일 ~5/20**. SDK 전달 후 플래닝(Phase 1 후속, Phase 2 검토) |

## #1 이슈와 할 일

- 요구사항 상세 정의: 데이터 전달 방식, **이미지 형식**(색상, 포함 항목, 크기, 배경을 투명/흰색/지도 중 무엇으로 할지, 커스텀 여부), 전달 후 연동 단계에서 업데이트 가능 여부.
- 데이터 계산: 헬스 앱 연동으로 몸무게와 키 등을 수집할지.
- 고객사 확인 요청: API 명세와 수집 필요 항목(초안) 전달, 일정 조정 협의, **OS 버전 확인**, 오픈소스 라이브러리 라이선스 고지 항목 확인.
- 다음 주부터 AOS/iOS 테스트 계정 전달, 다음 주 할 일은 Jira 일정 재조정(계정 정보는 옮기지 않음).

## #2 고객사 질의와 회신

| 분류 | 질문 | 회신 |
|---|---|---|
| API 명세 | 데이터 전달 규격/포맷 | 가이드 초안대로 진행 |
| 수집 데이터 | SDK 초기화 시 키와 몸무게 등 헬스 데이터 수집 가능 여부, 권한 획득 | 옵션으로 제공 데이터가 있으면 쓰고 **없으면 표준 칼로리 기준으로 계산** |
| 경로 이미지 규격 | 크기, 선 두께, 색상, 배경 | 가이드 초안대로 |
| OS 버전 | | **Android minSdk 26, iOS 15** |
| 오픈소스 라이선스 | 고지 필요 항목 | 모니모 쪽에 확인할 예정, 미리 주면 전달 |
| 일정 | 기본 기능 선제공 후 업데이트 | 선제공 후 업데이트 진행 |
| 권한 획득 | 앱에서 하는지 | **앱에서 확인해 진행** |
| 고도 | 센서 없는 단말 표시 | 센서가 없으면 N/A 또는 `-` 형태 |
| 랩 페이스 | 제공 단위 | **min/km (예: 8'12")** |
| 시나리오/기획안 | 제공 일정 | 다음 주 중 회신 |

할 일: 테스트 계정 전달(iOS, Android 각 1건), 미회신 항목 재문의.

## #3 이슈

- 앱 아이콘 제작 요청 → Android 크기 변형으로 전달.
- SDK 용량: **iOS xcframework 기준 32MB, Android aar 기준 326KB**. 빌드 후 확인해 삼성생명에 전달.
- 권한 획득 주체를 앱으로 재확인(Y).

## #4 이슈와 할 일

- 고객사 SDK 전달물: 샘플 앱 내용 추가, SDK 가이드, 오픈소스 라이선스 목록.
- **이름 규칙**: 가이드는 "삼성 라이브 로케이션 SDK 개발 가이드 + 버전명", 라이선스 파일은 "삼성 라이브 로케이션 오픈소스 라이브러리 + 전달 날짜". (고객사 쪽에서는 SDK를 "삼성 라이브 로케이션"으로 부른다.) ^[inferred]
- Phase 2 검토: 일정 확인, 개발 내용 확정, 기획안 요청.

실제 1.0.0 전달은 2026-05-20이었다 → [[drawing-run-sdk-release-history-2026]].

## Sources

- [Confluence: 스크럼 보드](https://inavisystems.atlassian.net/wiki/spaces/2Ozy8QblnTwf/pages/1873051652), [260416 #1](https://inavisystems.atlassian.net/wiki/spaces/2Ozy8QblnTwf/pages/1873215490), [260423 #2](https://inavisystems.atlassian.net/wiki/spaces/2Ozy8QblnTwf/pages/1894875180), [260429 #3](https://inavisystems.atlassian.net/wiki/spaces/2Ozy8QblnTwf/pages/1907130396), [260514 #4](https://inavisystems.atlassian.net/wiki/spaces/2Ozy8QblnTwf/pages/1915224141) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음. 테스트 계정(메일 주소)은 보안 사유로 옮기지 않음
