---
title: >-
    INAVI AIR API 개요
category: references
tags: [inavi-air, api, error-code, visibility/internal]
aliases: [API 명세, INAVI AIR API 정리]
relationships:
  - target: "[[inavi-air-api-detail-spec]]"
    type: related_to
sources: [~/Develop/Wiki/_raw/articles/project-air/API 명세.md]
summary: >-
    INAVI AIR API의 서버 접속 구조, 공통 요청 헤더, 결과 코드, 기능 카테고리 목차, 푸시 유형, 전기차 충전소 응답 필드를 정리한 개요 문서.
provenance:
  extracted: 0.92
  inferred: 0.08
  ambiguous: 0.00
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T09:14:00+09:00
updated: 2026-10-26T09:14:00+09:00
snapshots:
  - "[[_raw/_archived/API 명세|API 명세]]"
---

# INAVI AIR API 개요

원본은 Notion의 INAVI AIR API 페이지를 2026-06-09에 정리한 요약본이다. 각 API의 필드 단위 스펙은 [[inavi-air-api-detail-spec]]에 있고, 이 페이지는 공통 규칙만 다룬다. 소속 프로젝트: [[inavi-air]].

## 서버 연동

| 구분 | 프로토콜 | AIR 서버 |
|---|---|---|
| 개발 | HTTP | `[HOST]` |
| 상용 | HTTPS | `[HOST]` |

- 통신사 연동 서버 `UnitedInavi`가 KT용(`.../UnitedInaviKT`)과 LG용(`.../UnitedInaviLG`)으로 나뉜다. LG는 로그 전송용 API가 별도 포트(1442)다. 개발 서버의 IP 주소는 원본에만 두고 이 페이지에는 적지 않았다.
- 모든 Request/Response는 JSON이다.

## 공통 Request Header

| 헤더 | 설명 |
|---|---|
| `method` | `POST` |
| `Content-Type` | `application/json;charset=UTF-8` |
| `private_key`, `auth_key` | 개인키, 인증키 |
| `os_type`, `os_ver`, `app_ver`, `app_vercode`, `device` | 단말/앱 정보 |
| `mdn`, `uk` | 전화번호. KT는 보안 이슈로 `mdn`을 비우고 AES-256으로 암호화한 `uk`를 쓴다. |
| `company` | `KT` / `SKT` / `LG` / `ETC` |
| `sns_key`, `ad_id` | SNS 키, 광고 ID(iOS/Android 각각) |
| `reg_flag` | `s`(SNS 개인키) / `m`(모바일 개인키). 즐겨찾기 호출 시 필수이고 없으면 `902`. |
| `serviceType` | `AIR3`(에어) / `TMONEY`(온다택시) |
| `servicePackage` | 서비스 앱 구분용 패키지명 |
| `tmoney_status` | 온다택시 전용 동승 여부(0 기본, 1 승객 위치 안내, 2 목적지 안내) |
| `sdkAuthKey`, `shiWeightType` | 삼성중공업 SDK 전용 |
| `ivi_flag` | CarPlay/Android Auto 사용 여부(신규) |

## 결과 코드(Error Code) 요약

코드는 숫자 범위로 영역이 나뉜다.

| 범위 | 영역 | 예 |
|---|---|---|
| `0`, `1` | 성공 / 탐색 실패 | `0` 성공 |
| `3`~`49` | 경로탐색 | `4` 출발지 오류, `5` 목적지 오류, `7` 높이·중량 제한, `8` 시간제 통행금지, `32` 탐색 거리 초과(국내 700km, 도보 20km) |
| `96`~`122` | 탐색 부가 | `97` 체크섬 실패, `120` 현재 경로가 최적(스마트 재탐색 개선 없음) |
| `200` | HUD | 인증된 시리얼 번호 아님 |
| `300` | 통합 | 서비스 미지원 |
| `400`~`403` | 온에어 | 수신 상태/미수신/수신 완료/음성 정보 없음 |
| `501`, `502`, `970` | 에어 캐시 | 잔여 캐시 부족, 마일 오류, 정합성 실패(어뷰징 의심) |
| `601`~`604`, `968`, `969` | 통신사(LG) | 인증/부가서비스 가입/연동 오류 |
| `610` | w3w | 단어 검색 파라미터 오류 |
| `760`~`765` | 즐겨찾기 | 등록 한도 초과, 이미 존재하는 항목 |
| `888`, `889` | SNS 로그인 | 로그인 실패, 이미 사용 중인 계정 |
| `900`~`907` | 통합 | `900` 인증 실패, `901` 개인키 오류, `902` 파라미터 오류, `903` 조회결과 없음 |
| `910`~`921` | 외부 서버 연동 | 유고, 유가, 안내, 탐색, 검색, 오르다 |
| `930`~`938` | 검색 | 보안시설 검색, 좌표/쿼리 오류 등 |

전체 코드 표는 원본 `1.3 결과 코드`에 있다.

## 푸시 관련

푸시 Type은 A(일반 실행), B(모바일 웹 연동), C(탐색), D(내부 WebView), E(앱 특정 화면)이고, 메시지 정의에는 온다택시용 S/X 유형도 있다. 자세한 구조는 [[air-push-notification]]에 정리했다.

## 기능 카테고리 목차

탐색, 검색, 즐겨찾기, 로그, 이벤트, 기타, RRIS, 에어 캐시, w3w, 캐시버튼(Android 전용), HUD, 신호등, 음성광고, 메인화면, 그룹주행, 오픈POI, AIR 서비스, 나의주행, LOG-AIR, 삼성중공업 SDK, 제보하기, 통계, 오르다(ORDA). 엔드포인트별 목록은 [[inavi-air-api-detail-spec]]를 본다.

## 전기차 충전소 응답 파라미터

- 충전소 단위: `agency`(운영 기관 코드 18종, 예: ME 환경부, KP 한국전력, TM 티맵), `station_id`, `fee`, `free_parking`, `operating_hour`, `opagency`, `reservation`, `membership`, `serviceable`, `charger_count`
- 충전기 `type_1`: 01 DC차데모, 02 AC완속, 03 DC차데모+AC3상, 04 DC콤보, 05 DC차데모+DC콤보, 06 DC차데모+AC3상+DC콤보, 07 AC급속3상
- 충전기 `status`: 0 알수없음, 1 통신이상, 2 충전대기, 3 충전중, 4 운영중지, 5 점검중, 6 예약중, 7 표시안함

## Open Questions

- 원본은 요약본이라 각 API의 Request/Response는 Notion 원본을 보라고 안내한다. 이 위키의 [[inavi-air-api-detail-spec]]가 그 상세판이다.

## Sources

- [[_raw/_archived/API 명세.md]] — 원본 요약 문서
