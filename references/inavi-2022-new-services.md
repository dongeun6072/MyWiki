---
title: >-
    2022년 신규 서비스 소식: 오르다(ORDA), Connected 관제, 온보딩 프로그램
category: references
tags: [orda, connected, fms, onboarding, visibility/internal]
aliases: [오르다, ORDA 베타, 아이나비 Connected 관제서비스, 온보딩 프로그램]
relationships:
  - target: "[[inavi-air-map-style-upgrade-2022]]"
    type: related_to
sources: [~/Develop/Wiki/_raw/articles/Outlook_2022.md]
summary: >-
    2022년 사내에 공지된 오르다(ORDA) 등산 소모임 서비스 베타(04-18~05-08), 아이나비 Connected 차량 관제서비스 Beta(06-09), 신규 입사자 온보딩 프로그램(GPX 산책 코스 앱) 진행 기록.
provenance:
  extracted: 0.92
  inferred: 0.08
  ambiguous: 0.00
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: peripheral
created: 2026-10-26T09:40:56+09:00
updated: 2026-10-26T09:40:56+09:00
snapshots:
  - "[[_raw/_archived/Outlook_2022|Outlook_2022]]"
---

# 2022년 신규 서비스 소식

2022년 업무 메일([[inavi-2022-mail-overview]])에 나온 신규 서비스 소식과 신규 입사자 온보딩이다.

## 오르다(ORDA) — 등산 소모임 서비스

| 항목 | 내용 |
|---|---|
| 개요 | 자사의 **숲길 에셋**(등산로 데이터)으로 만든 서비스. 서비스명 "오르다(ORDA)", 부제 "등산편" |
| 콘셉트 | "내 주변에 멋진 사람들을 발견하고 함께하는 액티비티 테마 소모임", "함께 오르는 즐거움". 등산을 공통 관심사로 동네에서 가볍게 소모임을 만들고 교류. 맛집 탐방, 사진 촬영, 클린 하이킹, 플로깅, 챌린지 등 |
| 사용 상황 | 주변에 활동적으로 할 것이 없을 때, 밴드·카페 가입이 부담스러운 1회성 모임, 코스·출발지·이동 정보를 찾아 계획하기 어려울 때 |
| 사내 베타 | **2022-04-18 ~ 05-08**, Android만(iOS 예정). 의견 제출은 중복 가능, 종료 후 추첨 경품(100만 원 상당). 베타 기간 중 최소 반나절 크루 모임을 부서에 요청 |
| 확장 계획 | 등산편 이후 자전거 등 다양한 액티비티 |
| 이후 | 7월 에어 지도에 오르다용 등산로·들머리 레이어를 추가하기로 했다. ([[inavi-air-map-style-upgrade-2022]]) 에어 서버 API에 `/orda/stamp`(가까운 스탬프 조회)가 있다. ([[inavi-air-api-detail-spec]]) |

## 아이나비 Connected 차량 관제서비스 Beta (2022-06-09)

팅크웨어 커넥티드서비스부가 출시한 **외부 연동 서비스**로, 아이나비 Connected 사용자에게 등록 차량 통합 모니터링을 제공한다.

- 기능: 차량 운행 요약 대시보드(평균 운행시간, 운행거리, 안전운행점수), 지도에서 모든 차량의 현재 위치와 주행/주차 상태, 주행 중 경로 조회, 이벤트 알람(주차 중 충격, 주행 중 큰 충격)과 이미지(LTE 모델은 영상), **국세청 양식 차량운행기록부 내보내기**(업무용 승용차 세법 개정 대응)
- 지원 요금제: Connected PRO+, Standard+, LTE. PRO는 통신 동글 펌웨어 1.3.5 이상 필요
- 사용 방법: 앱의 환경설정 > 회원정보에서 "INAVI FMS 연결하기"로 사용 승인(개인정보 제3자 제공 동의 필수), 웹 관제 사이트는 같은 계정 사용

## 신규 입사자 온보딩 프로그램 (2022-03)

[[이동은]]의 온보딩 프로젝트다(상세 업무 실적은 [[inavi-air-feature-history]]).

- 앱: **GPX 파일과 iNavi Maps API를 쓰는 산책 코스 추천 프로그램**
- 기능: 추천 코스 목록(우선 백운호수 코스만), 코스 총 거리, 지도 내 산책 경로, 현위치 버튼과 마커
- 진행: 주 1회 리뷰로 피드백 반영, 저장소는 비트버킷, 코드 리뷰용 브랜치 공유. 기획 리뷰 03-22, 리뷰 03-25(흐름), 03-31(`[Good Route]` 개발 항목과 일정)
- 실적에는 2022-03-28 ~ 04-28, 달성률 100%로 기록되어 있다. ([[inavi-air-feature-history]])

## Sources

- [[_raw/_archived/Outlook_2022.md]] — 2022 업무 메일
