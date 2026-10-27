---
title: "INAVI AIR API — 삼성중공업 SDK"
category: references
tags: [inavi-air, api, shi, sdk, visibility/internal]
aliases: [삼성중공업 SDK]
relationships:
  - target: "[[inavi-air-api-detail-spec]]"
    type: derived_from
sources: ["url:https://inavisystems.atlassian.net/wiki/spaces/AS/pages/2262307833"]
summary: >-
    삼성중공업 SDK용 API 명세 원문 전사. SHI GPS Data 전송과 운행금지시간·이동불가/출입금지·일단 정지·중대재해 구역 조회 규격을 담는다.
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

# INAVI AIR API — 삼성중공업 SDK

Confluence "삼성중공업 SDK" 페이지들을 요약 없이 그대로 옮긴 원문 전사본이다. 허브는 [[inavi-air-api-detail-spec]], 공통 헤더·결과 코드는 [[inavi-air-api-common]], 서비스 개요는 [[inavi-air]]를 본다.

| API | URL |
| --- | --- |
| [[#이동불가 구역/출입금지 구역 정보 조회]] | `/shiSdk/getTFlimitInfo` |
| [[#운행금지시간 정보 조회]] | `/shiSdk/getDrivStopInfo` |
| [[#중대재해 발생 구역 정보 조회]] | `/shiSdk/getDisasterInfo` |
| [[#SHI GPS Data 전송]] | `/shiSdk/sendShiGps` |
| [[#일단 정지 구역 정보 조회]] | `/shiSdk/getStopAreaInfo` |

## 개요
> Confluence page id: 2262307833 · 최종 수정: 10월 06, 2026

상위 페이지 "삼성중공업 SDK" 본문은 하위 API 링크 목록이다(원본 순서 그대로).

- 🧭이동불가 구역/출입금지 구역 정보 조회
- 🧭운행금지시간 정보 조회
- 🧭중대재해 발생 구역 정보 조회
- 🧭SHI GPS Data 전송
- 🧭일단 정지 구역 정보 조회

## 이동불가 구역/출입금지 구역 정보 조회
> Confluence page id: 2262307899 · 최종 수정: 10월 01, 2026

### Function

> 이동불가 구역/출입금지 구역 정보 조회

### URL

> `/shiSdk/getTFlimitInfo`

[[inavi-air-api-common#Request Header|Request Header]]

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] 0 : 성공 903 : 조회결과 없음 999 : 정의되지 않은 오류 |
| result\_msg | String | 결과코드에 따른 메세지 |
| limitList | Array | 이동불가/출입금지 구역 정보 리스트 |
| ┣ lon | String | WGS 84 경도 (EX : 127.11077678260982) |
| ┣ lat | String | WGS 84 위도 (EX : 37.40219377747615) |
| ┣ nodeid | String | node 아이디 (EX : 1234) |
| ┣ mapid | String | 지도 아이디 (EX : 1234) |
| ┣ linkid | String | 링크 아이디 (EX : 1234) |
| ┣ dir | String | 방향 코드 (EX : 0) |
| ┣ limitStdt | String | 제한시작일자 (EX : 20230630) |
| ┣ limitSttm | String | 제한시작시간 (EX : 0700) |
| ┣ limitFndt | String | 제한종료일자 (EX : 20230630) |
| ┣ limitFntm | String | 제한종료시간 (EX : 0930) |
| ┗ weightType | String | 중량 타입   0 : 중량 상관 없이 회피 탐색 (Default)   1 : 4톤 미만 차량에 대해 회피 탐색   2 : 4톤 이상 차량에 대해 회피 탐색 |

## 운행금지시간 정보 조회
> Confluence page id: 2262307879 · 최종 수정: 10월 01, 2026

### Function

> 운행금지시간 정보 조회

### URL

> `/shiSdk/getDrivStopInfo`

[[inavi-air-api-common#Request Header|Request Header]]

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] 0 : 성공 903 : 조회결과 없음 999 : 정의되지 않은 오류 |
| result\_msg | String | 결과코드에 따른 메세지 |
| stopList | Array | 운행금지시간 정보 리스트 |
| ┣ zoneId | String | 구역 정보 (EX : "zone02\_01" //공장내 운행금지) |
| ┣ limitSttm | String | 제한시작시간 (EX : 0650) |
| ┗ limitFntm | String | 제한종료시간 (EX : 0730) |

## 중대재해 발생 구역 정보 조회
> Confluence page id: 2262307939 · 최종 수정: 10월 01, 2026

### Function

> 중대재해 발생 구역 정보 조회

### URL

> `/shiSdk/getDisasterInfo`

[[inavi-air-api-common#Request Header|Request Header]]

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] 0 : 성공 903 : 조회결과 없음 999 : 정의되지 않은 오류 |
| result\_msg | String | 결과코드에 따른 메세지 |
| disasterList | Array | 중대재해 발생 구역 정보 리스트 |
| ┣ lon | String | WGS 84 경도 (EX : 127.11077678260982) |
| ┣ lat | String | WGS 84 위도 (EX : 37.40219377747615) |
| ┣ mapid | String | 지도 아이디 (EX : 1234) |
| ┣ linkid | String | 링크 아이디 (EX : 1234) |
| ┣ dir | String | 방향 코드 (EX : 0) |
| ┣ etcFlag | String | 중대재해 코드 (EX : 01) (01: 사망 , 02 : 위험 , 03) |
| ┣ viewFlag | String | 화면표시 Y/N (EX : Y) |
| ┗ soundFlag | String | 음향표시 Y/N (EX: Y) |

## SHI GPS Data 전송
> Confluence page id: 2262307859 · 최종 수정: 10월 01, 2026

### Function

> SHI GPS Data 전송

### URL

> `/shiSdk/sendShiGps`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| paramList | ArrayList | O | GPS 정보 리스트 |
| ┣ userId | String | O | 사용자 ID |
| ┣ speed | Integer | O | 속도 |
| ┣ lat | double | O | 위도 |
| ┣ lon | double | O | 경도 |
| ┣ angle | double | O | 정북기준각도 |
| ┣ overSpeedYn | String | O | 속도위반여부 (Y/N) |
| ┣ pathVolnYn | String | O | 경로위반여부 (Y/N) |
| ┣ limitLocEntrYn | String | O | 제한구역진입여부 (Y/N) |
| ┣ mapId | String | O | MapID 해당 위경도에 맞는 실제 ID 값 |
| ┣ linkId | String | O | linkID 해당위경도에 맞는 실제 ID 값 |
| ┣ dir | String | O | 방향코드 |
| ┗ timeStamp | String |  | unix timestamp(초단위) → “2023-11-23 발행 SDK 부터 적용” |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] 0 : 성공 999 : 정의되지 않은 오류 |
| result\_msg | String | 결과코드에 따른 메세지 |

## 일단 정지 구역 정보 조회
> Confluence page id: 2262307919 · 최종 수정: 10월 01, 2026

### Function

> 일단 정지 구역 정보 조회

### URL

> `/shiSdk/getStopAreaInfo`

[[inavi-air-api-common#Request Header|Request Header]]

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] 0 : 성공 903 : 조회결과 없음 999 : 정의되지 않은 오류 |
| result\_msg | String | 결과코드에 따른 메세지 |
| stopAreaList | Array | 일단 정지 구역 정보 리스트 |
| ┣ mapid | String | 맵 ID EX ) 4379 |
| ┣ linkid | String | 링크 ID EX) 64 |
| ┗ dir | String | 방향 코드 EX) 1 |

## Sources

- Confluence "INAVI AIR API" > 삼성중공업 SDK (2026-10-27 조회): 삼성중공업 SDK (2262307833), 이동불가 구역/출입금지 구역 정보 조회 (2262307899), 운행금지시간 정보 조회 (2262307879), 중대재해 발생 구역 정보 조회 (2262307939), SHI GPS Data 전송 (2262307859), 일단 정지 구역 정보 조회 (2262307919)
