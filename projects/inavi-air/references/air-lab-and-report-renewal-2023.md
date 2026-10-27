---
title: >-
    제보하기 ver.2와 에어 연구소 리뉴얼 (2023 여름~가을)
category: references
project: inavi-air
tags: [report, air-lab, renewal, scrum, visibility/internal]
aliases: [제보하기, 제보하기 & 연구소 개선, 제보하기/연구소 리뉴얼, 제보하기/에어 연구소 리뉴얼, 에어연구소 리뉴얼, 스크럼 - 제보하기/에어 연구소 리뉴얼]
relationships:
  - target: "[[inavi-air]]"
    type: related_to
  - target: "[[air-my-places-renewal-2023]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/209027275
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/230522964
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/204865646
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/212959258
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/209158321
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/205062145
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/210174414
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/211353601
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/216104961
summary: >-
    제보하기 기획서 수정 내역 전부, 에어 연구소 리뉴얼(미리보기, 경로 옵션, 이륜차) 기획, 스토어 문구(AOS 03.05.31/iOS 03.05.09), 리소스 배포 표, 스크럼 #1~#4 일지.
provenance:
  extracted: 0.92
  inferred: 0.05
  ambiguous: 0.03
base_confidence: 0.6
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T13:00:00+09:00
updated: 2026-10-26T13:00:00+09:00
---

# 제보하기 ver.2와 에어 연구소 리뉴얼 (2023 여름~가을)

2023년 7~10월 진행된 "제보하기" 신규 기능과 "에어 연구소" 리뉴얼의 기획서 수정 이력, 스토어 문구, 리소스 배포 표, 스크럼 #1~#4 일지이다. 정식 오픈(ver.2)은 [[air-my-places-renewal-2023]]의 AOS 03.05.32 / iOS 03.05.11 릴리즈에 포함됐다. 목차는 [[air-feature-planning-hub]].

## 1. 제보하기 기획서 수정 내역 (pageId 209027275, 2023-10-19)
원본에 최신순으로 쌓여 있어 시간순(오래된 것부터)으로 재배열한다.
1. 기획서 초안 공유.
2. 리뷰 후 수정사항 반영하여 업데이트.
3. 제보하기 작성 중 뒤로가기 선택 시 팝업 제공.
4. 임시저장 썸네일 사양 변경.
5. 제보하기 캐시 제공 조건 변경, 제보 완료 Push 문구 정의 추가.
6. 제보하기 완료 사양 중 "중복" 상태 추가(Cams).
7. 검색 결과가 없는 경우 제보하기 추가.

## 2. 에어 연구소 리뉴얼 기획서 (pageId 209158321, 2023-08-25)
시간순(원본은 최신순):
1. 신규 항목 추가 — 경로 탐색 옵션. 미리보기를 통한 직관적 정보 제공.
2. 경로 옵션 변경 — 차종에서 이륜차를 선택하면 사양 추가.
3. 1차 리뷰 후 수정사항 업데이트.
4. 이륜차 사양 추가 수정.

## 3. 스토어 문구 — "제보하기 & 연구소 개선" (pageId 230522964, 2023-09-13)
### AOS v03.05.31
```
[v03.05.31]
• 제보하기 ver. 2
  - 새로워진 제보하기를 에어 연구소에서 확인해 보세요!
  - 제보하고 캐시 받고! Best 제보로 선정 시 캐시를 드려요!
• 경로 탐색 기본 옵션 변경
  - 내가 원하는 경로를 고정으로 설정해요.
  - 자세한 내용은 공지사항을 참고해 주세요.
최신 버전으로 지금 업데이트 해보세요!
더 좋은 서비스를 위해 에어팀은 항상 귀 기울이고 있습니다.
```
### iOS v03.05.09
동일 문구(이모지 없음).

## 4. 리소스 배포 표 — "제보하기/연구소 리뉴얼" (pageId 212959258, 2023-10-10)
12행, 날짜는 링크로만 존재.
| 순서 | 내용 |
|---|---|
| 1 | 주변 검색 / 모의 주행 배속 수정 |
| 2 | 주변 검색 리소스 수정(Carplay) |
| 3 | 에어연구소 리소스 추가-1 |
| 4 | 에어연구소 리소스 추가-2 |
| 5 | 에어연구소 / 환경설정 리소스 수정 |
| 6 | 에어연구소 / 환경설정 리소스 수정 |
| 7 | 제보하기 리소스 수정 |
| 8 | 폰트 변경 적용 관련 리소스 현행화 |
| 9 | 리소스 수정(속도, 안전운행 폰트 변경 적용) |
| 10 | 에어 연구소 리소스 수정 |
| 11 | 폰트 변경 적용 관련 리소스 수정(안전운행) |
| 12 | 리소스 용량 개선(30~50% 감소) |

부모 페이지 "제보하기/에어 연구소 리뉴얼"(pageId 204865646)은 본문 없음.

## 5. 스크럼 #1~#4 — 제보하기/에어 연구소 리뉴얼 (보관)
10:30~12:00 회의, 참석자 10명 내외(이름 생략). #4는 2023-08-22, 나머지는 날짜 없음(8월 초중순 ^[inferred]).

### 항목별 진행
| 항목 | 첫 등장 | 마지막 상태 |
|---|---|---|
| 에어 연구소 리뉴얼(미리보기 기능, 탐색옵션 고정으로 인한 불편 개선) | #1 Agenda | #4까지 진행. 기획 시나리오 정리, 디자인 가이드(#3~), Agent/App 개발 |
| 메인화면 하단 버튼 사용성 개선 | #1 | #1 ToDo(App)에서만 등장 |
| 제보하기 (Agenda 범위: #2 카메라/POI/사용자 의견 → #3 이후 도로정보 추가) | #2 | 시나리오 정리, 프로세스 정리(PM), 신규 제보하기 기능 추가(Agent/App) 진행 |
| AI 안전통합 횡단보도 플랫폼 개발(Agent/App) | #1 | Agent는 #3에서 완료, App은 #4까지 진행 |
| 캐시버튼 최신버전 SDK 검토(App/Agent) | #1 ToDo | #2 완료 |
| 교통정보 품질개선 앱 지원(only AOS) | #2 | #4까지 진행 |
| MMC 엔진 안정성 개선 | #1 ToDo(엔진) | #2 Android 완료, iOS ~8.8, #3 iOS 완료 |
| 가로모드 노치영역 개선(only iOS) | #1 ToDo | #4까지 ToDo/진행 |
| 신규 폰트 적용 검토(디자인/App) | #3 | #4까지 |
| 웹(이벤트페이지)에서 캐시적립 I/F 개발(Agent) | #4 | 진행 |
| 내장소 리뉴얼(기획) | #3 ToDo | #4 ToDo |

### 회차별 특이사항
- #1 Request(모두 체크 완료): 횡단보도 delay 영향도 검토, 하단 팝업 이미지 전달(사업부), 8월 이벤트 룰렛 횟수 변경 결정, 이벤트 공지.
- #2: Agenda 이름이 "사용성 개선"으로 바뀌며 제보하기가 추가되고 교통정보 품질개선 앱 지원(only AOS)이 등장.
- #3 사업 이슈: 이벤트 페이지에서 버튼 클릭 시 캐시 지급 여부 확인.
- #4(2023-08-22) Request: 교통정보 서버 — AI 횡단보도 데이터를 실제 데이터와 연동하는 일정 확인.
- 공통 ToDo: 공지 팝업 문구/이미지, 스토어 문구/이미지 현행화, TC 작성.

## Related
- [[air-my-places-renewal-2023]] — 함께 정식 오픈한 내 장소 리뉴얼
- [[air-confluence-scrum-and-voice-2023-2024]] — 동일 시기 스크럼 정리
- [[air-daegu-crosswalk-signal-2023]] — AI 횡단보도 관련
- [[air-cash-welcome-mission-table-2024]] — 웰컴 미션의 에어 연구소 항목
- [[inavi-air]], [[inavi-air-feature-history]]

## Sources
- Confluence "제보하기" (209027275), "제보하기 & 연구소 개선" (230522964), "제보하기/에어 연구소 리뉴얼" (204865646, 빈 페이지), "제보하기/연구소 리뉴얼" (212959258), "에어연구소 리뉴얼" (209158321), "스크럼 #1~#4 - 제보하기/에어 연구소 리뉴얼" (205062145, 210174414, 211353601, 216104961) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
