---
title: "INAVI AIR API — 음성광고"
category: references
tags: [inavi-air, api, onair, voice-ad, visibility/internal]
aliases: [음성광고, 온에어]
relationships:
  - target: "[[inavi-air-api-detail-spec]]"
    type: derived_from
sources: ["url:https://inavisystems.atlassian.net/wiki/spaces/AS/pages/2262308731"]
summary: >-
    INAVI AIR 음성광고(온에어) API 4개(수신 시작, 수신 완료, 음성 파일 조회, 하루 최대 수신 광고 수)의 요청·응답 필드를 Confluence 원문 그대로 옮긴 명세.
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

# INAVI AIR API — 음성광고

Confluence "INAVI AIR API" > "음성광고" 영역을 원문 그대로 옮긴 페이지다. 엔드포인트 색인은 [[inavi-air-api-detail-spec]], 공통 헤더와 결과 코드는 [[inavi-air-api-common]], 소속 프로젝트는 [[inavi-air]]이다.

| API | URL |
|---|---|
| 온에어 수신 시작 | `/onAirListenStart` |
| 온에어 수신 완료 | `/onAirListenFinish` |
| 온에어 음성 파일 조회 | `/onAirVoiceFileInfo` |
| 하루 최대 수신 광고 수 | `/onAirDailyCount` |

## 개요
> Confluence page id: 2262308731 · 최종 수정: 10월 06, 2026

- 🧭하루 최대 수신 광고 수
- 🧭온에어 음성 파일 조회
- 🧭온에어 수신 시작
- 🧭온에어 수신 완료

## 온에어 수신 시작
> Confluence page id: 2262308755 · 최종 수정: 10월 01, 2026

### Function

> 온에어 수신 시작

### URL

`/onAirListenStart`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| onAirId | String | O | 수신 시작 음성 파일 고유 ID |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]]<br>0 : 성공 |
| result\_msg | String | 결과값에 따른 메세지 |
| onAirTrid | String | 트랜잭션 ID |

## 온에어 수신 완료
> Confluence page id: 2262308775 · 최종 수정: 10월 01, 2026

### Function

> 온에어 수신 완료

### URL

`/onAirListenFinish`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| onAirId | String | O | 수신 완료 된 음성 파일 고유 ID |
| onAirTrid | String | O | 수신 시작 시 응답 받은 트랜잭션 ID |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]]<br>0 : 성공<br>401 : 수신하지 않은 온에어 정보<br>402 : 이미 수신 완료한 온에어 정보<br>970 : 에어 캐시 정합성 체크 실패 (캐시 어뷰징 의심) |
| result\_msg | String | 결과값에 따른 메세지 |

## 온에어 음성 파일 조회
> Confluence page id: 2262308795 · 최종 수정: 10월 01, 2026

### Function

> 온에어 음성 파일 조회

### URL

`/onAirVoiceFileInfo`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| hashTag | String |  | URL 인코딩 된 해시 태그 EX) %ED%95%B4%EC%8B%9C%ED%83%9C%EA%B7%B8 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]]<br>0 : 성공<br>403 : **조회 조건에 해당하는 온에어 음성 정보 미존재** |
| result\_msg | String | 결과값에 따른 메세지 |
| todayAdPlayable | Boolean | 당일 광고 재생 가능 여부<br>true : 재생 가능<br>false : 재생 불가 (하루에 들을수 있는 최대 광고 갯수 초과) |
| onAirFile | Object | 온에어 음성파일 정보 |
| ┣ url | String | 온에어 음성 파일 URL |
| ┣ playTime | Integer | 재생 시간 |
| ┣ onAirId | String | 음성 파일 고유 ID |
| ┗  onAirHashId | Integer | 음성 파일 해시 값 |

## 하루 최대 수신 광고 수
> Confluence page id: 2262308815 · 최종 수정: 10월 01, 2026

### Function

> 하루 최대 수신 광고 수

### URL

`/onAirDailyCount`

[[inavi-air-api-common#Request Header|📙Request Header]]

> 원본에 Request Parameter 표가 없음

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]]<br>0 : 성공 |
| result\_msg | String | 결과값에 따른 메세지 |
| count | Integer | 당일 광고 재생 가능 수 (0인 경우 당일 수신 가능한 광고 모두 수신 한 상태) |

## Sources

- Confluence "INAVI AIR API" > 음성광고 (2026-10-27 조회): 음성광고 (2262308731), 온에어 수신 시작 (2262308755), 온에어 수신 완료 (2262308775), 온에어 음성 파일 조회 (2262308795), 하루 최대 수신 광고 수 (2262308815)
