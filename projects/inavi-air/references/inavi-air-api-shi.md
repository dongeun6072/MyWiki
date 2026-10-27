---
title: "INAVI AIR API — 삼성중공업 전용 API"
category: references
tags: [inavi-air, api, shi, restricted-zone, visibility/internal]
aliases: [삼성중공업 전용 API]
relationships:
  - target: "[[inavi-air-api-detail-spec]]"
    type: derived_from
sources: ["url:https://inavisystems.atlassian.net/wiki/spaces/AS/pages/2262307751"]
summary: >-
    삼성중공업 전용 수신 API 명세 원문 전사. 운행금지시간, 이동불가/출입금지 구역, 중대재해 발생 구역 정보 수신 규격을 담는다.
provenance:
  extracted: 1.0
  inferred: 0.0
  ambiguous: 0.0
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-27
tier: supporting
created: 2026-10-27T10:00:00+09:00
updated: 2026-10-27T10:00:00+09:00
---

# INAVI AIR API — 삼성중공업 전용 API

Confluence "삼성중공업 전용 API" 페이지들을 요약 없이 그대로 옮긴 원문 전사본이다. 허브는 [[inavi-air-api-detail-spec]], 공통 헤더·결과 코드는 [[inavi-air-api-common]], 서비스 개요는 [[inavi-air]]를 본다.

| API | URL |
| --- | --- |
| [[#이동불가 구역/출입금지 구역 정보 수신]] | `/saveTFlimitInfo` |
| [[#운행금지시간 정보 수신]] | `/saveDrivStopInfo` |
| [[#중대재해 발생 구역]] | `/saveDisasterInfo` |

## 개요
> Confluence page id: 2262307751 · 최종 수정: 10월 06, 2026

상위 페이지 "삼성중공업 전용 API" 본문은 하위 API 링크 목록이다(원본 순서 그대로).

- 🧭이동불가 구역/출입금지 구역 정보 수신
- 🧭운행금지시간 정보 수신
- 🧭중대재해 발생 구역

---

#### 삼성중공업 전달 규격서

INAVI\_API\_v1.0.0.xlsx (Confluence 첨부 파일, 위키에는 미수록)

## 이동불가 구역/출입금지 구역 정보 수신
> Confluence page id: 2262307793 · 최종 수정: 10월 01, 2026

### Function

> 이동불가 구역/출입금지 구역 정보 수신

### URL

> `/saveTFlimitInfo`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| limitList | ArrayList | O | 이동불가/출입금지 구역 정보 리스트 |
| ┣ lon | String | O | WGS 84 경도 (EX : 127.11077678260982) |
| ┣ lat | String | O | WGS 84 위도 (EX : 37.40219377747615) |
| ┣ nodeid | String | O | node 아이디 (EX : 1234) |
| ┣ mapid | String | O | 지도 아이디 (EX : 1234) |
| ┣ linkid | String | O | 링크 아이디 (EX : 1234) |
| ┣ dir | String | O | 방향 코드 (EX : 0) |
| ┣ limitStdt | String | O | 제한시작일자 (EX : 20230630) |
| ┣ limitSttm | String | O | 제한시작시간 (EX : 0700) |
| ┣ limitFndt | String | O | 제한종료일자 (EX : 20230630) |
| ┗ limitFntm | String | O | 제한종료시간 (EX : 0930) |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] 0 : 성공 999 : 정의되지 않은 오류 |
| result\_msg | String | 결과코드에 따른 메세지 |

## 운행금지시간 정보 수신
> Confluence page id: 2262307773 · 최종 수정: 10월 01, 2026

### Function

> 운행금지시간 정보 수신

### URL

> `/saveDrivStopInfo`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| stopList | ArrayList | O | 운행금지시간 정보 리스트 |
| ┣ zoneId | String | O | 구역 정보 (EX : "zone02\_01" //공장내 운행금지) |
| ┣ limitSttm | String | O | 제한시작시간 (EX : 0650) |
| ┗ limitFntm | String | O | 제한종료시간 (EX : 0730) |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] 0 : 성공 999 : 정의되지 않은 오류 |
| result\_msg | String | 결과코드에 따른 메세지 |

## 중대재해 발생 구역
> Confluence page id: 2262307813 · 최종 수정: 10월 01, 2026

### Function

> 중대재해 발생 구역 정보 수신

### URL

> `/saveDisasterInfo`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| disasterList | ArrayList | O | 중대재해 발생 구역 정보 리스트 |
| ┣ lon | String | O | WGS 84 경도 (EX : 127.11077678260982) |
| ┣ lat | String | O | WGS 84 위도 (EX : 37.40219377747615) |
| ┣ mapid | String | O | 지도 아이디 (EX : 1234) |
| ┣ linkid | String | O | 링크 아이디 (EX : 1234) |
| ┣ dir | String | O | 방향 코드 (EX : 0) |
| ┣ etcFlag | String | O | 중대재해 코드 (EX : 01) (01: 사망 , 02 : 위험 , 03) |
| ┣ viewFlag | String | O | 화면표시 Y/N (EX : Y) |
| ┗ soundFlag | String | O | 음향표시 Y/N (EX: Y) |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] 0 : 성공 999 : 정의되지 않은 오류 |
| result\_msg | String | 결과코드에 따른 메세지 |

## Sources

- Confluence "INAVI AIR API" > 삼성중공업 전용 API (2026-10-27 조회): 삼성중공업 전용 API (2262307751), 이동불가 구역/출입금지 구역 정보 수신 (2262307793), 운행금지시간 정보 수신 (2262307773), 중대재해 발생 구역 (2262307813)
