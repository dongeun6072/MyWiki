---
title: >-
    아이나비에어 앱 기능 개발 이력 (2022~2026)
category: references
tags: [inavi-air, android, feature-history, visibility/internal]
aliases: [에어 앱 개발 이력, 에어 정기 업데이트]
relationships:
  - target: "[[inavi-air]]"
    type: related_to
sources:
  - ~/Develop/Wiki/_raw/articles/inavi/개인업무수행실적입력양식(2022).xlsx
  - ~/Develop/Wiki/_raw/articles/inavi/개인업무수행실적입력양식(2023).xlsx
  - ~/Develop/Wiki/_raw/articles/inavi/2026_상반기_목표_주요업무_정리.md
summary: >-
    아이나비에어 Android 앱에 2022~2023년에 추가된 기능(HUD, 신호등, 음성광고, 에어캐시 스탬프, w3w 등)과 2026년 월별 정기 업데이트 내용.
provenance:
  extracted: 0.90
  inferred: 0.10
  ambiguous: 0.00
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T09:20:33+09:00
updated: 2026-10-26T09:20:33+09:00
snapshots:
  - "[[_raw/_archived/2026_상반기_목표_주요업무_정리|2026_상반기_목표_주요업무_정리]]"
  - "[[_raw/_archived/개인업무수행실적입력양식(2022).xlsx|개인업무수행실적입력양식(2022).xlsx]]"
  - "[[_raw/_archived/개인업무수행실적입력양식(2023).xlsx|개인업무수행실적입력양식(2023).xlsx]]"
  - "[[_raw/_archived/Outlook_2022|Outlook_2022]]"
  - "[[_raw/_archived/Outlook_2023|Outlook_2023]]"
---

# 아이나비에어 앱 기능 개발 이력 (2022~2026)

[[inavi-air]]의 서버 API와 프로토콜은 다른 페이지에 있고, 이 페이지는 **Android 앱 쪽에서 어떤 기능이 언제 추가됐는지**를 정리한다. 담당은 [[이동은]]이며 2022-09부터 정기 업데이트를 맡고 있다([[job-description-2023-2026]]).

## 2022년

| 기간 | 업무 | 내용 |
|---|---|---|
| 03~04 | 온보딩 프로그램 | GPX 산책 코스를 파싱해 경로와 총 시간을 보여 주는 앱 (INavi Maps API 사용) |
| 05~06 | AOS 외부포팅(MXI, 아트뷰) | 과속 경고 환경설정 메뉴(UI)와 안내엔진, 데이터 절약 설정 |
| 07~08 | HUD 연동 | 에어 규격 정리와 샘플 앱 |
| 08~09 | 에어캐시 화면 리뉴얼 | 디자인 변경, lottie 애니메이션(프로그레스바, 동전) |
| 09~10 | 신호등 안내 | 신호등 UI, I/F, 신호등 안내엔진 → 서버 규격은 [[daegu-traffic-light-protocol]] |
| 11 | 음성 광고 POC | UI 작업 |

## 2023년

| 기간 | 업무 | 내용 |
|---|---|---|
| 01~03 | 음성광고 서비스 | 캐시 적립을 원하는 사용자를 위한 **참여형 오디오 광고** |
| 03~04 | 리뉴얼 완성도 | 주행 화면의 전체 경로 화면을 경로 선택 화면과 같은 룩으로 맞춤 |
| 04~05 | what3words | 3단어 입력으로 검색과 길찾기 |
| 05 | 캐시 적립 경험(GUI) | 캐시가 0시에 사라지는 문제를 캘린더 형식 스탬프 적립으로 해결 |
| 05~06 | 에어캐시 페이지 리뉴얼 | 주행 적립+스탬프, 적립 스탬프 고도화, Kakao API v2 마이그레이션. 주행 캐시 대비 적립률이 낮아 UI를 바꿈 |
| 06~07 | 메인화면 에어캐시 | 관심도를 높이기 위한 레이아웃 개선 |
| 07~09 | AI 안전통합 횡단보도 | 운전 중에도 쉬운 제보와 보상, 교차로 내 보행자 주의 안내, 제보하기와 에어연구소 리뉴얼 |
| 09~10 | 내장소 개선 | 메인화면에서 내장소를 표출해 접근성 개선 |
| 11 | HUD 연동 적용 | 외부 라이브러리로 블루투스 연결, 실시간 주행 데이터를 HUD에 표출 |
| 11~12 | 서비스 안정화 | HUD 정식 서비스를 위한 검증 이슈 정리 |

2023년 메일 기록: HUD 연동 라이브러리(외주)와 1차 시험 → [[air-hud-integration-2023]], 대구 보행자 신호등/AI 횡단보도 → [[air-daegu-crosswalk-signal-2023]], 후면 단속과 요금 할인 데이터 → [[air-map-data-and-safety-guidance-2023]], 제휴·광고·쿠폰 → [[air-partner-integrations-2023]], 플랫폼 마감 → [[inavi-platform-deadlines-2023]].

2022-07-05부터 **매주 화요일 정기 "아이나비 에어 스크럼"** 회의가 12월까지 이어졌다. ([[inavi-2022-mail-overview]]) 2022-07 지도 스타일 고도화는 [[inavi-air-map-style-upgrade-2022]], 같은 시기 외부포팅 업무는 [[inavi-hybrid-navi]]에 있다.

API 쪽 대응: 음성광고(`/onAirDailyCount` 등), HUD 시리얼 인증(`/authSerialNumber`), 에어 캐시 스탬프(`/stampHistory` 등)는 [[inavi-air-api-detail-spec]]에 있다.

## 2026년 정기 업데이트 (월별)

| 월 | 내용 |
|---|---|
| 2월 | 단일링크 모의주행 MMC 적용, 아파트 POI 명칭 충돌 처리, SKP SDK 최신 버전 업데이트 |
| 3월 | 음성 발성 로직 개선, 포인트 홈 SDK 업데이트, DP 엔진 업데이트 |
| 4월 | **w3w 사양 제거**, DP fps 활성화 조건 제거, 안내엔진 적용(강남순환고속도로 구간단속 이슈) |
| 5월 (핫패치) | 안전운행 구간 통과 후 안내가 나오는 이슈를 안내엔진 교체로 해결 |
| 6월 | 목적지 고속도로·지하차도·고가도로 안내 팝업 수정, 고속도로 목적지 최적 지점 탐색 후 안내, 후방 카메라 통과 후 80m 안내 지속 표시 개선, 검색결과 지역 필터 행정구역 축약 |

그 밖에 Android Auto 최신 라이브러리 대응과 신규 OS 대응이 연간 업무에 포함되어 있다.

## 메모

- 2023년 추가된 w3w가 2026-04에 제거됐는데, API 문서([[inavi-air-api-overview]])에는 w3w 오류 코드(610)와 엔드포인트가 아직 남아 있다. 서버 API가 앱 사양 제거 후에도 유지되는 것으로 보인다. ^[inferred]
- 안내엔진 교체/적용이 4월과 5월에 반복됐다. 구간단속 안내 이슈가 원인이었다.

## Sources

- [[_raw/_archived/개인업무수행실적입력양식(2022).xlsx]] — 2022 업무 실적
- [[_raw/_archived/개인업무수행실적입력양식(2023).xlsx]] — 2023 업무 실적
- [[_raw/_archived/2026_상반기_목표_주요업무_정리.md]] — 2026 월별 체크인
