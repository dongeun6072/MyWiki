---
title: >-
    HUD(로드피아) 연동·서비스 안정화 스크럼 2023-11~12
category: references
project: inavi-air
tags: [inavi-air, scrum, hud, skp, visibility/internal]
aliases: [스크럼 #1 - HUD(로드피아) 연동, 스크럼 #2 - HUD(로드피아) 연동, 스크럼 #1 - 서비스 안정화 (23년 12월), 스크럼 #2 - 서비스 안정화 (23년 12월), 스크럼 #3 - 서비스 안정화 (23년 12월)]
relationships:
  - target: "[[inavi-air]]"
    type: related_to
  - target: "[[inavi-air-feature-history]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/280985612
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/284229659
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/289734657
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/296091649
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/300285953
summary: >-
    2023년 11~12월 에어 팀 스크럼 5건(HUD 로드피아 연동 #1~#2, 서비스 안정화 #1~#3)의 영역별 Done/Doing/ToDo와 진행 상태 변화.
provenance:
  extracted: 0.90
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T13:00:00+09:00
updated: 2026-10-26T13:00:00+09:00
---

# HUD(로드피아) 연동·서비스 안정화 스크럼 2023-11~12

스크럼 5건은 모두 보관(archived) 상태이며 10:30~12:00 회의 템플릿(Agenda / Done & Doing / ToDo / Issues / Request)으로 작성되었다. 11월 말 HUD(로드피아) 연동과 SKP 광고 추천 이벤트 스크럼 2건, 12월 서비스 안정화·사용자 편의성 개선·HUD 정식 서비스 스크럼 3건이다. 참석자 명단(이름)은 옮기지 않는다. 같은 시기 리소스는 [[air-resource-deploy-log-2023-h2]], 스토어 문구는 [[air-app-version-notes-2023]], 다른 스크럼은 [[air-confluence-scrum-and-voice-2023-2024]]를 본다.

## A. HUD(로드피아) 연동 스크럼

Agenda: HUD 연동 / SKP 광고 추천 이벤트. 날짜는 원문에 없다(11월 중순~말, HUD Beta 출시 11월 24일 전후 ^[inferred]).

### 스크럼 #1 — 영역별 상태
- 기획: 로드피아 HUD 연동 기획, SKP 광고 추가 기획, 최근장소/내장소 중간 문자열 검색 사양 정의 (상태 미기재)
- 디자인: HUD 연결 디자인, 캐시 화면 SKP 광고 디자인, 오토/카플레이 디자인 현행화(완료)
- Agent(서버): SKP 쿠폰 발행(완료), SKP 앱 정보 연동(완료), SKP 캐시 지급 API 추가(진행)
- App: HUD BT Lib 연동, SKP 광고 연동, 최근장소/내장소 중간 문자열 검색 사양 추가(미정), 최근장소·내장소 검색 시 영어 대소문자 미구분 사양 추가(완료)
- 엔진: DP 엔진 — iOS 주기 겹치는 부분 수정(완료)
- ALL: 신규 음성 테스트 APK 발행(발랄한, 차분한)(완료). 음성 후보 평가는 [[air-new-voice-preference-2023-09]]
- ToDo: 기획 — 공지 팝업 문구 작성, 스토어 문구 작성 / 디자인 — 공지 팝업 이미지 제작, 스토어 이미지 현행화 / PM — TC 작성
- Issues: PM 유럽 출장

### 스크럼 #2 — #1과의 차이점
- 기획: HUD 연동 기획(완료), SKP 광고 추가 기획(완료), 중간 문자열 검색 사양 정의는 취소선 처리되어 "차기"로 이월
- 디자인: HUD 연결 디자인(완료), 캐시 화면 SKP 광고 디자인(완료) — 세부로 "공지사항 쿠폰 지급 안내 디자인", "쿠폰 등록 디자인" 추가. 오토/카플레이 현행화(완료)
- Agent: SKP 쿠폰 발행, 앱 정보 연동, 캐시 지급 API 추가 모두 완료
- App: HUD BT Lib 연동(완료), SKP 광고 연동(완료), 중간 문자열 검색 사양 추가는 "차기"로 취소선, 영어 대소문자 미구분(완료)
- 엔진·ALL: 동일(완료)
- ToDo: 동일하되 PM의 "TC 작성"이 완료로 표시
- Issues: PM 유럽 출장

## B. 서비스 안정화 (23년 12월) 스크럼

Agenda: 서비스 안정화 / 사용자 편의성 개선 / HUD 정식 서비스. #3의 날짜는 2023-12-19(10:30~12:00), #1·#2는 날짜 미기재(12월 초~중순 ^[inferred]).

### 항목별 상태 변화 (#1 → #2 → #3)
| 영역 | 항목 | #1 | #2 | #3 |
|---|---|---|---|---|
| 기획 | 에어퀴즈 결과 분석 | 진행 | 완료 | 완료 |
| 기획 | 최근장소/내장소 검색 문자열 중간어 검색 지원 | 진행 | 완료 | 완료 |
| 기획 | iOS 단축어 | 진행 | 완료 | 완료 |
| 기획 | 내장소 화면 천이 지도 표출 사양 정의 | 진행 | 완료 | 완료 |
| 기획 | HUD 개선 항목(필요시) 지원 | 지원 | 지원 | 지원 |
| 디자인 | SKP 공지 디자인 | 진행 | 완료 | 완료 |
| Agent | SKP 쿠폰 어뷰징 체크 | 진행 | 진행중 | 진행중 |
| App | Auto에 로그저장 기능 추가(임시 테스트 버전 배포) | 완료 | 완료 | 완료 |
| App | 최근장소/내장소 검색 문자열 중간어 검색 지원 | 진행 | 완료 | 완료 |
| App | iOS 단축어 지원 | 진행중 | 진행중 | 완료 |
| App | 경로설정 > 경유지 추가 > 최근목적지 검색 > 바로 길찾기 되는 현상 | 진행중 | 완료 | 완료 |
| App | [iOS] 카플레이 회전 화살표 표시 개선 | 진행중 | 진행중 | 진행중 |
| App | 내장소 추가 및 경유지 변경 시 최근장소 내 정보가 하단으로 치우침 | 완료 | 완료 | 완료 |
| App | 내장소 가로모드 가이드 선 제거 | 완료 | 완료 | 완료 |
| App | 최근장소 삭제 후 페이지 상태 개선 | 완료 | 완료 | 완료 |
| App | 내장소 리스트 우선 표출 | 완료 | 완료 | 완료 |
| App | 내장소 화면 천이 지도 표출 상태 정리 | 검토 | 진행중 | 완료 |
| App | 4,5종 차량의 주말/공휴일 할인에 대해 정상 동작하는 방안 | 검토 | 검토 | 검토 내용 보고 후 진행 |
| App | HUD 검증 이슈 대응 | 진행 | 진행중 | 2차 검증 펌웨어 이슈 해결 후 진행 |
| PM | 유럽 출장 | 진행중 | 진행중(15일 종료 예정) | 종료 |
| ALL | 신규 음성 테스트 APK 발행(발랄한, 차분한) | 완료 | 완료 | 완료 |

표의 "미기재"는 #1 원문에 상태 표기가 없는 항목이다. "지원"은 상태 없이 항목만 있는 HUD 개선 지원이다.

### 세 스크럼 공통 ToDo / Issues
- ToDo: 기획 — 공지 팝업 문구 작성, 스토어 문구 작성 / 디자인 — 공지 팝업 이미지 제작, 스토어 이미지 현행화 / PM — TC 작성 (엔진, Agent, App 칸은 비어 있음)
- Issues: PM 유럽 출장 (사업 칸 등 나머지는 비어 있음)
- Request: 비어 있음

#3(12-19) 기준 마지막 상태: 열려 있는 항목은 카플레이 회전 화살표 표시 개선(iOS), 4·5종 차량 주말/공휴일 할인 방안(검토 후 진행), HUD 검증 이슈(펌웨어 대기), SKP 쿠폰 어뷰징 체크였다. 이 항목들의 결과 문구는 12월 스토어 출시 노트(iOS 단축어, 검색 추천어 개선)에서 확인된다.

## Related
- [[inavi-air]] — 에어 앱 프로젝트 허브
- [[inavi-air-feature-history]] — 기능 이력
- [[air-hud-integration-2023]] — HUD 연동 배경
- [[air-partner-integrations-2023]] — SKP 등 제휴 연동
- [[air-release-and-resource-log-hub]] — 이 묶음 목차

## Sources
- Confluence "스크럼 #1 - HUD(로드피아) 연동" (pageId 280985612) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "스크럼 #2 - HUD(로드피아) 연동" (pageId 284229659) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "스크럼 #1 - 서비스 안정화 (23년 12월)" (pageId 289734657) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "스크럼 #2 - 서비스 안정화 (23년 12월)" (pageId 296091649) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "스크럼 #3 - 서비스 안정화 (23년 12월)" (pageId 300285953) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
