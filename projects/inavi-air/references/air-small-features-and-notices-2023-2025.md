---
title: >-
    에어 소형 기능 기록 (w3w, AI 횡단보도, 후면 단속 카메라, 음성 변경, 홍수 경보, 황금티켓 등)
category: references
project: inavi-air
tags: [air-features, release-notes, w3w, crosswalk, voice, visibility/internal]
aliases: [w3w 시나리오, AI횡단보도 안내, 후면 단속 카메라, 길안내 음성 변경, 홍수 경보 & 신규 음성 추가, 황금티켓, 메인 하단 팝업, 쇼핑하기 / 주소 검색 '지하' 표기, 메인 화면 개선, 신규 기능 및 리뉴얼 관련]
relationships:
  - target: "[[inavi-air]]"
    type: related_to
  - target: "[[air-service-stability-release-notes-2023-2026]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/169443388
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/189661185
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/191463440
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/163676406
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/163676395
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/191201281
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/321617921
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/482902097
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/567672850
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/679772303
summary: >-
    2023~2025 에어의 소형 기능 페이지 모음: w3w 시나리오, AI 횡단보도 안내 리소스, 후면 단속 카메라, 하단 팝업, 쇼핑/주소 검색 지하 표기, 홍수 경보와 신규 음성(03.05.40/03.05.18), 음성 변경(03.05.43/03.05.21), 황금티켓.
provenance:
  extracted: 0.93
  inferred: 0.04
  ambiguous: 0.03
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T13:00:00+09:00
updated: 2026-10-26T13:00:00+09:00
---

# 에어 소형 기능 기록 (w3w, AI 횡단보도, 후면 단속 카메라, 음성 변경, 홍수 경보, 황금티켓 등)

단독 문서로 크지 않은 기능 페이지를 시간순으로 모았다. 대부분 "기획서 수정 내역", "스토어 문구", "리소스 배포 표" 중 하나다. 목차는 [[air-feature-planning-hub]]. 이후 정식 릴리즈 흐름은 [[air-service-stability-release-notes-2023-2026]]을 본다.

## 1. 메인 하단 팝업 (pageId 163676406, 2023-06-14)
- 본문은 이미지(팝업 화면)뿐이고 텍스트는 없다. (이미지 항목, 내용 없음)
- 관련 스크럼 항목: 하단 팝업 이미지는 사업부에서 전달([[air-lab-and-report-renewal-2023]] 스크럼 #1 Request), 하단 팝업 아웃링크 연결은 서버/앱 과제로 2023-10 완료([[air-my-places-renewal-2023]]).
- 부모 "메인 화면 개선"(163676395), "신규 기능 및 리뉴얼 관련"(191201281)은 본문 없는 목차 페이지.

## 2. w3w 시나리오 (pageId 169443388, 2023-06-30)
기획서 수정:
- 추천어 축약주소 제공
- Auto/Carplay 검색 결과값에 상세주소 제공
- Auto/Carplay 시나리오 추가

w3w(what3words) 스토어 문구는 [[air-point-home-new-cash-button-2023-2024]]의 1절(AOS v03.05.25 / iOS v03.05.03)에 있다.

## 3. 후면 단속 카메라 (pageId 191463440, 2023-07-13)
- 1차 기획서 배포. (그 외 내용 없음)
- 스토어 문구(AOS v03.05.29 / iOS v03.05.07): "후면 번호판 단속 카메라 안내! 새롭게 시행 중인 교통 법규도 안전하게 지켜주세요." — [[air-cash-advancement-planning-history-2023]] 5절.
- 후면 무인 교통단속 도입에 따른 서비스 검토 요청이 2023-05 캐시 적립 스크럼 이슈로 먼저 올라왔다([[air-cash-accrual-policy-discussion-2023]]).

## 4. AI횡단보도 안내 (pageId 189661185, 2023-07-19) — 리소스 배포 표
날짜는 링크로만 존재. 4행.
| 내용 | 비고 |
|---|---|
| AI횡단보도 안내 디자인 반영 | 메인 화면 리소스 |
| AI횡단보도 안내 디자인 반영 | 안전운전 심볼 추가 |
| AI횡단보도 안내 디자인 반영 | 안전운전 심볼 추가 |
| 스토어 이미지 수정 | 스토어 이미지 |

AI 횡단보도 플랫폼 개발과 이슈 분석 진행은 스크럼 기록([[air-lab-and-report-renewal-2023]], [[air-my-places-renewal-2023]])에 나온다. 대구 신호 연동은 [[air-daegu-crosswalk-signal-2023]].

## 5. 쇼핑하기 / 주소 검색 '지하' 표기 (pageId 321617921, 2024-01-18)
- 리소스 배포 표 1행: 쇼핑하기/주소 검색 리소스 추가.

## 6. 홍수 경보 & 신규 음성 추가 (pageId 482902097, 2024-07-17)
### AOS v03.05.40
```
[v03.05.40]
• 홍수 경보/침수 위험 알림 시작!
  - 주행 중 VMS정보에서 실시간으로 알려드려요!
  - 장마 기간에도 안전운전하세요!
• 부드러운 음성 추가!
  - 새로운 안내 음성이 추가되었어요!
  - 환경설정 > 안내 설정 > 길안내 음성에서 확인해 보세요.
• 자주 묻는 질문 제공!
  - 에어에 대한 주요 궁금증을 해결해드릴게요.
최신 버전으로 지금 업데이트 해보세요!
더 좋은 서비스를 위해 에어팀은 항상 귀 기울이고 있습니다.
```
### iOS v03.05.18
동일 문구(이모지 없음).

## 7. 길안내 음성 변경 (pageId 567672850, 2024-10-11)
### AOS v03.05.43
```
[v03.05.43]
• 발랄한 음성 변경!
  - 환경설정 > 안내 설정 > 길안내 음성에서 확인해 보세요.
• 버그 수정 및 안정성 개선
  - 원활한 서비스 제공을 위해 준비했어요.
최신 버전으로 지금 업데이트 해보세요!
더 좋은 서비스를 위해 에어팀은 항상 귀 기울이고 있습니다.
```
### iOS v03.05.21
동일 문구(이모지 없음).

## 8. 황금티켓 (pageId 679772303, 2025-01-16)
- 리소스 배포 표 1행: 황금티켓 ICON 배포 (날짜는 링크로만 존재).

## 버전 번호 요약
| 기능 | AOS | iOS | 페이지 수정일 |
|---|---|---|---|
| 홍수 경보 & 신규 음성(부드러운 음성) | 03.05.40 | 03.05.18 | 2024-07-17 |
| 길안내 음성 변경(발랄한 음성) | 03.05.43 | 03.05.21 | 2024-10-11 |

## Related
- [[air-service-stability-release-notes-2023-2026]] — 정식 릴리즈 노트
- [[air-confluence-scrum-and-voice-2023-2024]] — 음성 관련 스크럼 내용
- [[air-map-data-and-safety-guidance-2023]] — 안전 안내 데이터
- [[inavi-air]], [[inavi-air-feature-history]]

## Sources
- Confluence "w3w 시나리오" (169443388), "AI횡단보도 안내" (189661185), "후면 단속 카메라" (191463440), "메인 하단 팝업" (163676406), "메인 화면 개선" (163676395, 빈 페이지), "신규 기능 및 리뉴얼 관련" (191201281, 빈 페이지), "쇼핑하기 / 주소 검색 '지하' 표기" (321617921), "홍수 경보 & 신규 음성 추가" (482902097), "길안내 음성 변경" (567672850), "황금티켓" (679772303) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
