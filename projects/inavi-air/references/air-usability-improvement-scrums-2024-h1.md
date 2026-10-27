---
title: >-
    에어 사용성 개선/통계 분석 스크럼 #1~#6 (2024 상반기)
category: references
project: inavi-air
tags: [air, scrum, usability, statistics, visibility/internal]
aliases: ["스크럼 #1 - 에어 사용성 개선/통계 분석", "스크럼 #2", "스크럼 #4", "스크럼 #5", "스크럼 #6", 에어 사용성 개선]
relationships:
  - target: "[[inavi-air]]"
    type: related_to
  - target: "[[air-growth-research-hub]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/365985803
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/371851265
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/401178647
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/405766150
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/409174017
summary: >-
    2024-02~05 주간 스크럼 #1~#6(#3은 이 묶음에 없음)의 공통 안건과 영역별 진행(기획, 디자인, Agent, App, 엔진, SDK, ALL)을 처음 등장일과 마지막 상태로 병합 정리.
provenance:
  extracted: 0.9
  inferred: 0.06
  ambiguous: 0.04
base_confidence: 0.6
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T13:00:00+09:00
updated: 2026-10-26T13:00:00+09:00
---

# 에어 사용성 개선/통계 분석 스크럼 #1~#6

2024년 상반기 에어 팀이 매주(화) 10:30~12:00에 연 스크럼 5개 페이지(#1, #2, #4, #5, #6)를 하나로 합쳤다. 페이지가 거의 같은 구조로 반복되므로 항목별로 "처음 등장 → 마지막 상태"만 적었다. #4는 2024-04-23, #5는 2024-04-30 회의로 표기돼 있고 #1·#2는 2월 중순~3월 말, #6은 5월 초로 추정된다 ^[inferred]. 같은 시기의 더 넓은 스크럼·음성 논의는 [[air-confluence-scrum-and-voice-2023-2024]], 이후 성장 프로젝트는 [[air-growth-sprint-minutes-2024-q4]]를 본다.

## 공통
- 참석: PM, 기획자, 디자이너, 앱 개발자, 서버 개발자, 엔진 담당, 사업 등 약 9명([[이동은]] 포함)
- 안건: 팀원 간 에어 목표·의견 조율 / 에어 사용성 개선 / 통계를 통한 사용자 니즈 분석

## 영역별 진행 (처음 등장 → 마지막 상태)
### 기획
| 항목 | 이력 |
|---|---|
| 에어 퀴즈 2차 | #1: 3/13 목표 → #2부터 "19일 진행" (2023-11 1차 결과는 [[air-quiz-result-analysis]]) |
| 통계가 필요한 사용자 액션 리스트 추출 | #1 진행 → #2 리스트 전달(완료) |
| 하단 Interstitial 팝업 노출 검토 | #1 검토 → #2 개선 검토 → #5·#6 "미 진행" |
| ADAS 데이터를 활용한 서비스 | #1 1차 기획 완료, 엔진 기능 검토 요청 필요 → #2 이후 "e-Horizon Engine core 및 Provider 모듈 일정 후 진행" (마지막까지 동일) |
| InaviMaps 기반 메인 화면 기획 | #1 진행 → #2 "기획 적극 반영" → #5·#6 "미 진행" |
| Notion 에어 페이지 및 FAQ 검토 | #4 신규 → #5·#6 진행 중: 에어 노션에 먼저 제작 후 하이핀과 동일한 그룹 위치로 이동 |
| 공지 팝업 문구 작성, 스토어 문구 작성 (ToDo) | #1~#6 계속 ToDo |

### 디자인
| 항목 | 이력 |
|---|---|
| 주변 검색 아이콘 변경 | #1 진행 → #2 "금주 내 전달 예정" → #4 완료 |
| 경로선 화살표 개선(입체감, 컬러) | #1 진행 중 → #2 앱 테스트 필요 → #4 완료 |
| Notion 에어 페이지·FAQ 검토 | #4 신규 → #6 진행 중 |
| 스토어 메인 이미지 변경 | #5 신규 → #6 진행 중 |
| 공지 팝업 이미지 제작, 스토어 이미지 현행화 (ToDo) | 계속 ToDo |

### Agent(서버)
- 통계 API 기능 검토(기존): #1 일정 확인 필요 → #2 1차 요구사항 상용 반영 완료(이슈 검토 필요), 2차 요구사항 검토 후 전달 → #4부터 "담당자 지정 후 진행"
- 사용자 액션 통계 API 기능 추가: 요구사항 확인 필요(끝까지 동일)

### App
| 항목 | 이력 |
|---|---|
| 하단 Interstitial 팝업 표출 | #1 진행 → #4 이후 제외 |
| AOS 캐시버튼(최신 버전) 적용 검토 | #2 완료(적립 테스트 확인 필요) |
| AOS USIM 변경 보안정책 제거 | #2 완료 |
| AOS aab 변경 검토 | #1 → #2 진행(aab 등록 완료, firebase 설정 진행 중) → #4 완료, 차기 패치에 적용 |
| 사용자 액션에 따른 통계 API 호출 개발 | #1 규격·추출 방식 논의 필요 → #4 이후 제외 |
| AOS Auto 경로 요약바, 고속모드 미표출 이슈 | #6 진행 중 |
| AOS DP Crash 이슈 분석 | #6 진행 중 |

### 엔진과 SDK
- 엔진: 경로선 화살표 개선 #1 진행 → #4 완료
- SDK(#5부터): LG AR SDK 진행 상황 확인 필요(디자인 리소스·컬러 1차 배포 4/30), AOS Target 버전 변경 완료, AOS/iOS 엔진 현행화

### ALL
- 신규 음성 의견 검토(발랄한/차분한 음성 퀄리티 검토): 설 연휴 테스트 후 논의(#1~#6 동일)

### PM / 이슈
- PM ToDo: TC 작성
- 이슈: PM 독일 출장 #1 2/12~3/17, #2 "복귀", #4·#5 5/4(재출장), #6 "복귀"
- Request 칸은 비어 있음

## Related
- [[air-confluence-scrum-and-voice-2023-2024]] — 같은 시기 스크럼·음성 논의
- [[air-quiz-result-analysis]] — 에어 퀴즈 결과
- [[air-hud-integration-2023]] — HUD 연동(관련 이전 작업)
- [[inavi-air]] — 프로젝트 개요
- [[air-growth-research-hub]] — 이 묶음 목차

## Sources
- Confluence "스크럼 #1 - 에어 사용성 개선/통계 분석" (pageId 365985803) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "스크럼 #2 ..." (pageId 371851265), "스크럼 #4 ..." (pageId 401178647), "스크럼 #5 ..." (pageId 405766150), "스크럼 #6 ..." (pageId 409174017)
