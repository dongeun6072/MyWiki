---
title: >-
    포인트홈(뉴캐시버튼)과 w3w/카카오 비즈보드/캐시버튼 출시, 2024 스크럼
category: references
project: inavi-air
tags: [point-home, cash-button, w3w, scrum, visibility/internal]
aliases: [포인트홈(뉴캐시버튼), 스크럼 #1 - 포인트홈(뉴캐시버튼), w3w/카카오 비즈보드/캐시버튼, 캐시 버튼(IOS), 광고 및 외부사업 연계]
relationships:
  - target: "[[inavi-air]]"
    type: related_to
  - target: "[[air-confluence-scrum-and-voice-2023-2024]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/150306826
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/481099799
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/481460247
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/489357336
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/502005858
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/503414803
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/511737857
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/495484984
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/169672768
summary: >-
    2023-05 w3w와 캐시버튼 동시 출시(AOS 03.05.25/iOS 03.05.03)의 스토어 문구, 2024년 7~8월 포인트홈(뉴캐시버튼) 스크럼 #1~#5, iOS 캐시 버튼 아이콘 배포 기록.
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

# 포인트홈(뉴캐시버튼)과 w3w/카카오 비즈보드/캐시버튼 출시, 2024 스크럼

에어에 캐시버튼(버튼을 누르면 포인트가 쌓이는 적립 서비스)이 들어간 2023-05 릴리즈의 스토어 문구와, 2024년 여름 "포인트홈(뉴캐시버튼)" 프로젝트의 스크럼 #1~#5 기록이다. 같은 시기 전체 스크럼 흐름은 [[air-confluence-scrum-and-voice-2023-2024]]를 참조한다. 목차는 [[air-feature-planning-hub]].

## 1. 스토어 문구 — w3w/카카오 비즈보드/캐시버튼 (pageId 150306826, 2023-05-23)
### Android v03.05.25
- 아이나비 에어와 what3words가 만났어요.
  - 모든 지역을 3m x 3m로 나누어 3단어로 표시한 what3words!
  - 원하는 위치를 간편하게 공유하고, 주소로는 애매했던 정확한 장소까지 3단어로 소통해 보세요.
  - 자세한 사용법은 공지사항을 참고해 주세요!
- 주행 거리 외 새로운 적립 서비스를 준비했어요.
  - 에어캐시에서 더 많은 리워드를 받아보세요! 버튼을 누르기만 해도 포인트가 쌓여요!
  - 쌓인 포인트로 에어캐시 전환, 기프티콘을 구매해 보세요!
- 알려진 버그를 수정하고, 안정성을 개선했어요.
- 마무리: 최신 버전으로 지금 업데이트 해보세요! 더 좋은 서비스를 위해 에어팀은 항상 귀 기울이고 있습니다.

### iOS v03.05.03
- what3words 항목(문구 동일)과 "알려진 버그를 수정하고, 안정성을 개선했어요."만 있고, 캐시버튼(적립 서비스) 항목은 없다.

## 2. 포인트홈(뉴캐시버튼) 스크럼 (보관)
모두 10:30~12:00 회의이며 #1~#3의 날짜는 원문에 없고, #4는 2024-08-13, #5는 2024-08-20이다. 참석자는 기획, 디자인, 앱, 서버, PM 담당 7~8명(이름 생략). 부모 페이지 "포인트홈(뉴캐시버튼)"(481099799)은 본문이 없다.

### 스크럼 #1 (pageId 481460247)
- Agenda: 메인화면 리뉴얼, [iOS] CP HUD 연동, [AOS] 스토어 aab 출시
- Done & Doing: 기획—메인화면 기획 완료 / 디자인—메인화면 디자인 / Agent—2년 캐시 완료 작업 예정(7/23) / App—메인화면 리뉴얼 개발 검토
- ToDo: 기획(공지 팝업 문구, 스토어 문구), 디자인(공지 팝업 이미지, 스토어 이미지 현행화), PM(TC 작성), 엔진
- Issues: 디자인—TINA 프로젝트 진행 상황 체크 필요
- Request: 임원 차량에서 카카오내비 HUD가 정상 동작하는지 확인 필요

### 스크럼 #2 (pageId 489357336)
- Agenda: 생성형 AI - 에어 연구소 연동, SKP 광고 Refresh, [iOS] CP HUD 연동, [AOS] 스토어 aab 출시, NaviSDK 초기 세팅 영상 제작
- Done & Doing: 디자인—생성형 AI 디자인 / App—Chat GPT 검토(비용 및 개발 검토)
- Issues: 디자인—TINA 프로젝트 확인 / App—도보/PM SDK 테스트를 위한 소스 공유
- Request 결과: 임원 차량 HUD 확인 완료 → 카카오내비와 T Map 모두 동작하지 않음.
- ToDo는 #1과 동일.

### 스크럼 #3 (pageId 502005858)
- Agenda: 생성형 AI - 에어 연구소 연동, [iOS] CP HUD 연동 - 에어 연구소 연동, SKP 광고 Refresh, [AOS] 스토어 aab 출시, NaviSDK 홍보 영상 제작
- Done & Doing
  - 기획: CP HUD 에어연구소 기획
  - 디자인: 생성형 AI 디자인, CP HUD 에어연구소 디자인
  - Agent: 탐색엔진 private key 전달, AIR 캐시 전환(포인트 홈 포함), 연구소 기능 on/off(AI는 Max Length, CP HUD)
  - App: Chat GPT 검토(비용 및 개발), NaviSDK 홍보 영상 제작(AOS 완료, iOS 진행)
- Issues: App—도보/PM SDK 테스트용 소스 공유, 아바티 → 에어캐시 전환 기능 확인 / PM—CP HUD 가능 차량 수배
- Request: 비어 있음

### 스크럼 #4 (pageId 503414803, 2024-08-13)
- #3과 동일하되 NaviSDK 홍보 영상 제작이 AOS와 iOS 모두 완료.

### 스크럼 #5 (pageId 511737857, 2024-08-20)
- Agenda 순서: [iOS] CP HUD 연동 - 에어 연구소 연동, SKP 광고 Refresh, 생성형 AI - 에어 연구소 연동, [AOS] 스토어 aab 출시, NaviSDK 홍보 영상 제작
- Done & Doing: 생성형 AI 디자인(완료), CP HUD 에어연구소 디자인(완료), 연구소 기능 on/off(완료, AI Max Length와 CP HUD), AIR 캐시 전환(포인트 홈) 진행, Chat GPT 검토(비용 및 개발) 진행
- Issues: App—아바티 → 에어캐시 전환 기능 확인(남은 이슈는 이것 하나)

### 차이점 요약 (#1 → #5)
- 주제가 메인화면 리뉴얼(#1) → 생성형 AI/CP HUD의 에어 연구소 연동과 SKP 광고 Refresh(#2~)로 이동.
- HUD 확인 결과(#2): 카카오내비/T Map 모두 해당 차량에서 동작 안 함 → 이후 CP HUD 가능 차량 수배(#3~#4) 이슈로 이어짐.
- ToDo(공지 팝업/스토어 문구/TC 작성)는 #1~#5 동안 변하지 않는다.

## 3. 리소스 배포 — 캐시 버튼(IOS) (pageId 495484984, 2024-07-30)
- "캐시 버튼 ICON 배포" 1행 (날짜는 링크로만 존재).

## 4. 기타 빈 페이지
- "광고 및 외부사업 연계" (pageId 169672768): 본문 없음(목차용 상위 페이지).

## Related
- [[air-confluence-scrum-and-voice-2023-2024]] — 동일 시기 스크럼 정리
- [[air-genai-airbot-review-2024]] — 생성형 AI 에어 연구소 연동
- [[air-hud-integration-2023]] — HUD 연동
- [[air-lab-and-report-renewal-2023]] — 에어 연구소
- [[inavi-air]]

## Sources
- Confluence "w3w/카카오 비즈보드/캐시버튼" (150306826), "포인트홈(뉴캐시버튼)" (481099799), "스크럼 #1~#5 - 포인트홈(뉴캐시버튼)" (481460247, 489357336, 502005858, 503414803, 511737857), "캐시 버튼(IOS)" (495484984), "광고 및 외부사업 연계" (169672768) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
