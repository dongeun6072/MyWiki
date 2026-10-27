---
title: >-
    INAVI AIR (아이나비에어)
category: project
tags: [inavi-air, navigation, api, routing, visibility/internal]
aliases: [아이나비에어, INAVI AIR, AIR3]
sources: [~/Develop/Wiki/_raw/articles/project-air, ~/Develop/Wiki/_raw/articles/Outlook_2024.md, ~/Develop/Wiki/_raw/articles/Outlook_2025.md]
summary: >-
    아이나비에어(INAVI AIR) 내비게이션 서비스의 서버 API, 경로탐색 프로토콜, 지도 포맷, 그룹주행 설계 문서를 한데 모은 프로젝트 개요.
provenance:
  extracted: 0.80
  inferred: 0.20
  ambiguous: 0.00
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: core
created: 2026-10-26T09:14:00+09:00
updated: 2026-10-26T14:00:00+09:00
snapshots:
  - "[[_raw/_archived/API 명세|API 명세]]"
  - "[[_raw/_archived/API 상세명세|API 상세명세]]"
  - "[[_raw/_archived/Push Curl|Push Curl]]"
  - "[[_raw/_archived/[포맷]MR(X1, 통신향)_v5.0_221123.docx|[포맷]MR(X1, 통신향)_v5.0_221123.docx]]"
  - "[[_raw/_archived/[프로토콜]Routing(Neon)_v2.2.11.docx|[프로토콜]Routing(Neon)_v2.2.11.docx]]"
  - "[[_raw/_archived/sMR_Format_v2_0.doc|sMR_Format_v2_0.doc]]"
  - "[[_raw/_archived/대구 신호교차로 Protocol_v0.4.docx|대구 신호교차로 Protocol_v0.4.docx]]"
  - "[[_raw/_archived/대구신호등목록.xlsx|대구신호등목록.xlsx]]"
  - "[[_raw/_archived/아이나비에어 그룹주행 설계서.pdf|아이나비에어 그룹주행 설계서.pdf]]"
  - "[[_raw/_archived/Outlook_2024|Outlook_2024]]"
  - "[[_raw/_archived/Outlook_2025|Outlook_2025]]"
---

# INAVI AIR (아이나비에어)

아이나비에어는 모바일 앱(Android/iOS)이 JSON 기반 HTTP API로 서버와 통신하는 내비게이션 서비스다. 경로탐색, 검색, 즐겨찾기, 로그, 이벤트, 에어 캐시, 그룹주행 같은 기능을 하나의 API 서버(`INaviAir`)가 제공하고, 경로탐색은 별도의 탐색 엔진(Neon)이 담당한다. ^[inferred]

## 서비스 구성

- **앱 ↔ 서버 API**: 모든 요청과 응답은 JSON이며 `POST`만 사용한다. 개발/상용 서버가 분리되어 있다. → [[inavi-air-api-overview]], [[inavi-air-api-detail-spec]]
- **통신사 연동**: KT, LG(U+)용 `UnitedInavi` 연동 서버가 따로 있고, 헤더의 `company`(KT/SKT/LG/ETC)로 구분한다.
- **서비스 구분**: 헤더 `serviceType`이 `AIR3`(에어)와 `TMONEY`(온다택시 연동)를 구분한다. 삼성중공업용 SDK API(`/shiSdk/*`)도 같은 서버에 있다.
- **경로탐색 엔진 프로토콜**: 서버가 탐색 엔진에 보내는 바이너리 요청/응답 규격. → [[inavi-routing-neon-protocol]]
- **지도(네트워크) 데이터**: 탐색용 MR 포맷과 경량 sMR 포맷. → [[inavi-mr-format-spec]], [[inavi-smr-format-spec]], [[inavi-mr-smr-network-data]]
- **신호등 정보**: 대구 신호교차로 연동. → [[daegu-traffic-light-protocol]]
- **그룹주행**: 위치를 서로 허용한 사람끼리 목적지까지 함께 이동하는 기능. → [[inavi-air-group-driving-design]], [[group-driving-location-permission]]
- **푸시 알림**: FCM 기반 6가지 메시지 유형. → [[air-push-notification]]
- **앱 기능 개발 이력**: 2022~2023년 HUD, 신호등, 음성광고, 에어캐시 스탬프 등과 2026년 월별 정기 업데이트. → [[inavi-air-feature-history]]

## 주요 API 기능 영역

탐색, 검색(SQE 통합검색, POI), 즐겨찾기/라벨, 로그, 이벤트(행운상자), 에어 캐시(스탬프, 쿠폰, 룰렛), 외부 계정 연동(SNS), 주행 이력, w3w(what3words), HUD 시리얼 인증, 신호등, 온에어 음성광고, 그룹주행, 오픈POI, 나의주행, RRIS, 삼성중공업 SDK, 통계, 오르다(ORDA). 엔드포인트 전체 목록은 [[inavi-air-api-detail-spec]]에 있다.

## 읽는 순서 추천

1. [[inavi-air-api-overview]]로 서버·헤더·에러코드 파악
2. [[inavi-air-api-detail-spec]]에서 필요한 엔드포인트 확인
3. 경로탐색 내부를 볼 때 [[inavi-routing-neon-protocol]]와 [[inavi-mr-smr-network-data]]

## 연도별 메일 기록

- 2023년: [[air-hud-integration-2023]], [[air-daegu-crosswalk-signal-2023]], [[air-partner-integrations-2023]], [[air-map-data-and-safety-guidance-2023]]
- 2024년: HUD 출시, 서버 flag, 광고, 서울시 보행자 PoC, 확대도·구간단속 오류 → [[air-operations-2024]]
- 2025년: 스토어 정책, 파트너 SDK, 오르다 연계, HUD 외부포팅, 도엽 오류 → [[air-operations-2025]], 공통 기능 변경 → [[nav-service-features-2025]]
- 2026년: 통합회원 분리, 크래시, 포인트홈 SDK, 안전운행 데이터(CameraGuidePoint) → [[air-operations-2026]]

## 서비스 기획과 운영 기록 (Confluence 스페이스 아이나비 에어 & NSDK)

- 스페이스 구성, 에어 연혁, 주제별 스크럼(2023~2024)과 신규 음성 선정: [[air-confluence-scrum-and-voice-2023-2024]]
- 에어캐시 적립 설계(스탬프, 룰렛, 웰컴 미션, 광고): [[air-cash-reward-design-2023-2024]]
- 성장 프로젝트: 사용자 지표, PRD, 로그인 유도 실험, 경쟁 조사, 원내비 종료 대응: [[air-growth-strategy-and-metrics-2024]]
- 에어봇(생성형 AI) 검토: [[air-genai-airbot-review-2024]]
- 버전별 출시 노트와 서비스 안정화 패치(2023-05 ~ 2026-09): [[air-service-stability-release-notes-2023-2026]]
- SDK 쪽 개발 기록은 [[orbis-sdk]]에서 이어진다.
- 개발 Slack 채널(#001_air_nsdk_dev) 대화: [[air-nsdk-dev-slack-2022]] → [[air-nsdk-dev-slack-2023-h1]] → [[air-nsdk-dev-slack-2023-h2]] → [[air-nsdk-dev-slack-2024-h1]] → [[air-nsdk-dev-slack-2024-h2]] → [[air-nsdk-dev-slack-2025]] → [[air-nsdk-dev-slack-2026]]
- 에어 앱 채널(#01_inavi_air) 대화: [[air-channel-slack-2022]] → [[air-channel-slack-2023-h1]] → [[air-channel-slack-2023-h2]] → [[air-channel-slack-2024-h1]] → [[air-channel-slack-2024-h2]] → [[air-channel-slack-2025-h1]] → [[air-channel-slack-2025-h2]] → [[air-channel-slack-2026]]
- 에어 프로젝트 채널(#10_prj-inaviair) 대화: [[air-prj-slack-2022]] → [[air-prj-slack-2023-h1]] → [[air-prj-slack-2023-h2]] → [[air-prj-slack-2024-h1]] → [[air-prj-slack-2024-h2]] → [[air-prj-slack-2025-h1]] → [[air-prj-slack-2025-h2]] → [[air-prj-slack-2026]]

## 상세 문서 (Confluence 전체 반영)

요약 페이지의 상세판이다. 원본 Confluence 페이지를 압축하지 않고 옮겼다(2026-10-26 가져옴).

- [[air-internal-docs-and-integration-hub]] — 에어 외부 연동 규격, 개발 문서, 테스트 가이드
- [[air-growth-research-hub]] — 성장 프로젝트: 데이터 분석, PRD, 가설, 로그인 유도 실험, 경쟁·앱테크 조사, 퀴즈, 리뷰
- [[air-feature-planning-hub]] — 에어캐시, 내장소, 제보하기, 에어 연구소 등 기능 기획 이력
- [[air-scrum-records-hub]] — 주제별 스크럼 회의록과 에어 연혁, 이미지 HUD 검토
- [[air-genai-and-ideation-hub]] — 생성형 AI 조사, 에어봇, 신규 Feature Ideation
- [[air-release-and-resource-log-hub]] — 연도별 버전 문구, 업데이트 목표일, 리소스 배포 로그, 2025 계획

## Open Questions

- 앱 클라이언트 코드와 이 API 문서가 같은 버전인지(문서 정리일 2026-06-09)는 확인되지 않았다.
- 그룹주행 설계서는 2019년 v0.9라서 현재 동작과 다를 수 있다.

## Sources

- [[_raw/_archived/API 명세.md]] — API 개요
- [[_raw/_archived/API 상세명세.md]] — 엔드포인트 상세
- [[_raw/_archived/[프로토콜]Routing(Neon)_v2.2.11.docx]] — 탐색 엔진 프로토콜
- [[_raw/_archived/[포맷]MR(X1, 통신향)_v5.0_221123.docx]] — MR 포맷
- [[_raw/_archived/sMR_Format_v2_0.doc]] — sMR 포맷
- [[_raw/_archived/대구 신호교차로 Protocol_v0.4.docx]], [[_raw/_archived/대구신호등목록.xlsx]] — 신호등
- [[_raw/_archived/Outlook_2024.md]] — 2024 업무 메일
- [[_raw/_archived/Outlook_2025.md]] — 2025 업무 메일
- [[_raw/_archived/Outlook_2026.md]] — 2026 업무 메일
- [[_raw/_archived/아이나비에어 그룹주행 설계서.pdf]] — 그룹주행 설계
- [[_raw/_archived/Push Curl.md]] — 푸시 메시지 예시
