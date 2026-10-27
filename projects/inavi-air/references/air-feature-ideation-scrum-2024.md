---
title: >-
    신규 Feature Ideation 스크럼 #1~#8 (2024 상반기)
category: references
project: inavi-air
tags: [inavi-air, scrum, feature-ideation, planning, visibility/internal]
aliases: [스크럼 #1 - 신규 Feature Ideation, 스크럼 #2 - 신규 Feature Ideation, 스크럼 #3 - 신규 Feature Ideation, 스크럼 #4 - 신규 Feature Ideation, 스크럼 #5 - 신규 Feature Ideation, 스크럼 #6 - 신규 Feature Ideation, 스크럼 #7 - 신규 Feature Ideation, 스크럼 #8 - 신규 Feature Ideation, 신규 Feature Ideation]
relationships:
  - target: "[[inavi-air]]"
    type: related_to
  - target: "[[air-confluence-scrum-and-voice-2023-2024]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/422248502
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/422019076
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/428310531
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/436666369
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/443711489
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/451215361
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/458064105
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/466747393
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/473595905
summary: >-
    2024년 5~7월경 에어 팀 스크럼 8회차 상세: 신규 Feature 기획, 외부 요구사항 대응, 통계 기반 needs 분석. 기획/디자인/Agent/App/엔진/LG SDK/TomTom 진행 상태 변화.
provenance:
  extracted: 0.88
  inferred: 0.10
  ambiguous: 0.02
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T13:00:00+09:00
updated: 2026-10-26T13:00:00+09:00
---

# 신규 Feature Ideation 스크럼 #1~#8

"신규 Feature Ideation" 상위 페이지(본문 없음) 아래의 주간 스크럼 8건이다. 모두 보관 상태, 10:30~12:00. 날짜가 명시된 것은 #3(2024-06-04)과 #4, #5(2024-06-11 표기)뿐이고 나머지는 본문 단서로 추정했다. 이후 시기의 생성형 AI 스크럼은 [[air-genai-scrum-2024]], 허브는 [[air-genai-and-ideation-hub]].

## 공통 구조

- Agenda(8회 동일): 신규 Feature 기획 / 외부 요구사항 대응 / 통계를 통한 사용자 needs 분석
- 섹션: Done & Doing(기획/디자인/Agent/App/PM/엔진/ALL/LG 도보·자전거·내비 SDK/TomTom), ToDo, Issues, Request(빈 체크박스).
- ToDo는 전 회차 동일한 템플릿: 기획 - 공지 팝업 문구 작성, 스토어 문구 작성 / 디자인 - 공지 팝업 이미지 제작, 스토어 이미지 현행화 / PM - TC 작성.
- Issues(PM, #2부터): 독일 출장 6/3 출발(한국), 7/5 출발(독일) - 7/6 도착(한국). #8에만 7/8~11 휴가 추가.
- 참석자: 기획/디자인/Agent/App/PM 등 7명(#1~#6), 1명 추가되어 8명(#7, #8). 이름 생략.

## 회차별 상세

### 스크럼 #1 (날짜 미기재, 5월 하순경 ^[inferred])

- 기획: LLM AI 활용 UseCase / InaviMaps 기반 메인 화면 기획 - 미진행(기획 적극 반영) / Notion 에어 페이지 및 FAQ 검토 - 진행 중(에어 노션에 먼저 제작한 뒤 하이핀과 동일한 그룹 위치로 이동) / 음성 제공 시나리오 결정(성우 결정 필요).
- 디자인: Notion 에어 페이지 및 FAQ 검토 / 스토어 메인 이미지 변경 - 진행 중.
- Agent(담당자 지정 후 진행): 통계 API 기능 검토(기존) - 1차 요구사항 상용 반영 완료(이슈 검토 필요), 2차 요구사항 검토 후 전달 / 사용자 액션 통계 API 기능 추가 - 요구사항 확인 필요.
- App: 하단 Interstitial 팝업 표출 - 제외 / 사용자 액션에 따른 통계 API 호출 기능 개발 - 제외(규격 정의 및 추출 방식 논의 필요) / AOS DP Crash 이슈 분석 - 진행 중.
- 엔진: 경로선 화살표 개선.
- LG 도보/자전거/내비 SDK: DP/안내 ~5/29, AOS·iOS 엔진 현행화.
- Issues: 없음(독일 출장 항목은 #2부터).

### 스크럼 #2 (날짜 미기재, 5월 말~6월 초 ^[inferred])

- #1과 동일하되 Issues(PM)에 독일 출장 일정이 추가됨. LG SDK 항목이 ALL 하위로 재배치됨.

### 스크럼 #3 (2024-06-04)

- 기획: LLM AI 활용 UseCase / InaviMaps 기반 메인 화면 기획 - 진행 중(리뷰 완료) / Notion 에어 페이지 및 FAQ - 공유 완료 / 음성 제공 시나리오 - 진행 중(성우 결정, **부드러운 음성 반영 여부 결정 필요**, 사용해보고 피드백) / **TomTom 매뉴얼 제작** - 진행 중(폰트 적용 이슈는 시니어 공유 후 피드백, 1차 6/5, 최종 6/19).
- 디자인: Notion 에어 페이지 및 FAQ - 완료 / 스토어 메인 이미지 변경 - 완료(6/4 전달).
- Agent: 통계 API 기능 검토(기존) 상태 유지 / 사용자 액션 통계 API 기능 추가 - **제외** / **신규 음성 반영** - 진행 중(개발서버 반영 완료).
- App: Interstitial 팝업, 사용자 액션 통계 API - 제외 유지 / AOS DP Crash 이슈 분석 - **완료** / **SK Feed Unit id 변경** - 진행 중 / 신규 음성 반영 검토 - 진행 중.
- 엔진: 경로선 화살표 개선 - **완료**.
- LG 도보/자전거/내비 SDK: DP/안내 ~5/29 - **1차 배포 완료** / AOS·iOS 엔진 현행화 및 **테스트 앱 배포(차주 또는 차차주)** / 디자인 - 도보용 TBT 이미지 추가(이미지 코드표 참조해 전달 요청).
- TomTom: 응원 문구만 있음.

### 스크럼 #4 (2024-06-11)

- 기획: InaviMaps 기반 메인 화면 - 1차 리뷰 완료, **2차 리뷰 12일 예정** / Notion 페이지·FAQ - **환경설정에 에어 페이지, FAQ 노출 검토** 추가 / TomTom 매뉴얼 - **11일 완료**, 폰트 이슈 **해결**, 최종 일정 6/19에서 11일로 변경, 이후 피드백 후 필요 시 추가 진행.
- 나머지는 #3과 동일(Agent 신규 음성 진행 중, App SK Feed Unit id 변경·신규 음성 검토 진행 중).

### 스크럼 #5 (2024-06-11 표기, #4의 갱신본 ^[ambiguous])

- 기획: 환경설정 에어 페이지/FAQ 노출 - 검토 중 / **웹페이지를 구글·네이버에서 검색 가능하도록 제작** - 검토 중.
- Agent: 신규 음성 반영 - **검토 완료**(개발서버 반영 완료).
- App: **SK Feed Unit id 변경 - 완료**, 신규 음성 반영 검토 - **검토 완료**.

### 스크럼 #6 (날짜 미기재, 6월 중하순경 ^[inferred])

- 기획 신규: TomTom 매뉴얼 - **추가 진행사항 확인 필요(25일 완료)** / **기관시스템(홍수통제소, 수자원공사) - 민관합동 내비 고도화**.
- Agent 신규: 기관시스템(홍수통제소, 수자원공사) - 민관합동 내비 고도화.
- App 신규: 기관시스템 - 민관합동 내비 고도화 / **아바타 신규 SDK 검토 - 검토 중**(원문 표기 "아바티").
- 나머지는 #5와 동일.

### 스크럼 #7 (날짜 미기재, 6월 하순경 ^[inferred])

- 내용은 #6과 사실상 동일. 참석자 1명 추가만 변화.

### 스크럼 #8 (날짜 미기재, 7월 초 ^[inferred])

- 기획: 환경설정 에어 페이지/FAQ 노출 - **완료** / 구글·네이버 검색용 웹페이지 - **전달 완료** / 음성 제공 시나리오 - **부분 완료**.
- 디자인 신규: **환경설정 자주 묻는 질문 아이콘** - 진행 중.
- Agent: 신규 음성 반영 - 진행 중(방면 음성 누락 여부 검토 중, **12일 배포 예정**) / 기관시스템 - 민관합동 내비 고도화 - 진행 중 / **서비스게이트 자주 묻는 질문 추가** - 진행 중.
- App: 신규 음성 반영 검토 - 진행 중 / 기관시스템 - 진행 중 / 아바타 신규 SDK - 검토 중 / **HUD 개선 - 완료** / **환경설정 자주 묻는 질문 추가** - 진행 중.
- TomTom: "완료!!!!????"(완료 여부 물음표).
- Issues(PM): 독일 출장 일정과 7/8~11 휴가.

## 항목별 추이 (처음 등장 → 마지막 상태)

| 항목 | 처음 | 마지막 상태 |
|---|---|---|
| 사용자 액션 통계 API(App/Agent) | #1 | 제외(규격 정의·추출 방식 논의 필요) |
| 하단 Interstitial 팝업 | #1 | 제외 |
| AOS DP Crash 이슈 분석 | #1 진행 중 | #3 완료 |
| 경로선 화살표 개선(엔진) | #1 | #3 완료 |
| 스토어 메인 이미지 변경 | #1 진행 중 | #3 완료(6/4 전달) |
| Notion 에어 페이지·FAQ | #1 | 공유 완료 → 환경설정 노출 #8 완료 |
| 신규 음성 반영 | #3 | #8 진행 중(12일 배포 예정) |
| SK Feed Unit id 변경 | #3 | #5 완료 |
| TomTom 매뉴얼 | #3 | #8 완료 여부 불확실 |
| LG 도보/자전거/내비 SDK | #1 | 1차 배포 완료, 테스트 앱 배포 대기 |
| 기관시스템 민관합동 내비 고도화 | #6 | #8 진행 중 |
| 아바타 신규 SDK 검토 | #6 | #8 검토 중 |
| HUD 개선 | #8 | 완료 |

## Related
- [[air-genai-scrum-2024]] — 이후 생성형 AI 스크럼
- [[air-confluence-scrum-and-voice-2023-2024]] — 스크럼과 음성 작업 전반
- [[air-chatgpt-usecases-and-dev-spec-2024]] — "LLM AI 활용 UseCase"의 결과물
- [[inavi-air]] — 프로젝트 홈

## Sources
- Confluence "신규 Feature Ideation" (pageId 422248502, 본문 없음)
- Confluence "스크럼 #1 ~ #8 - 신규 Feature Ideation" (pageId 422019076, 428310531, 436666369, 443711489, 451215361, 458064105, 466747393, 473595905) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
