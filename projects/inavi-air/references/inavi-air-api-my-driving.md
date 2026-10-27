---
title: "INAVI AIR API — AIR 나의주행"
category: references
tags: [inavi-air, api, driving-history, visibility/internal]
aliases: [AIR 나의주행]
relationships:
  - target: "[[inavi-air-api-detail-spec]]"
    type: derived_from
sources: ["url:https://inavisystems.atlassian.net/wiki/spaces/AS/pages/2262305566"]
summary: >-
    INAVI AIR 나의주행 API 명세 원문 전사. 주간요약바, 일별·월별 주행 리스트, 주행 상세(좌표·운전 습관)를 담는다.
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

# INAVI AIR API — AIR 나의주행

Confluence "AIR 나의주행" 페이지들을 요약 없이 그대로 옮긴 원문 전사본이다. 허브는 [[inavi-air-api-detail-spec]], 공통 헤더·결과 코드는 [[inavi-air-api-common]], 서비스 개요는 [[inavi-air]]를 본다.

| API | URL |
| --- | --- |
| [[#나의주행 주간요약바(AIR)]] | `/weeklyMyHabit` |
| [[#나의주행 일별 리스트(AIR)]] | `/myDailyDrivingList` |
| [[#나의주행 상세(AIR)]] | `/drivingHabitDetail` |
| [[#나의주행 월별 리스트(AIR)]] | `/monthlyMyDriving` |

## 개요
> Confluence page id: 2262305566 · 최종 수정: 10월 06, 2026

상위 페이지 "AIR 나의주행" 본문은 하위 API 링크 목록이다(원본 순서 그대로).

- 🧭나의주행 주간요약바(AIR)
- 🧭나의주행 일별 리스트(AIR)
- 🧭나의주행 상세(AIR)
- 🧭나의주행 월별 리스트(AIR)

## 나의주행 주간요약바(AIR)
> Confluence page id: 2262305610 · 최종 수정: 10월 01, 2026

### Function

> 나의주행 주간요약 바

### URL

> `/weeklyMyHabit`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

> 원본 표가 비어 있음

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |
| weeklyHabitList | List | 최근 1주일간 주행 습관 리스트 |
| ┣ date | String | 년.월.일 |
| ┗ habitList | List | 해당날짜 습관 리스트 |
| ┣ count | String | 일일 발생 갯수 |
| ┗ habit | String | 행위1: 차선이탈10: 전방추돌경고100: 급감속101: 급가속 |

## 나의주행 일별 리스트(AIR)
> Confluence page id: 2262305630 · 최종 수정: 10월 01, 2026

### Function

> 나의주행 일별 리스트

### URL

> `/myDailyDrivingList`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| date | String | O | 조회하고자 하는 날짜(default : 당일) |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |
| drivingList | List | 주행리스트 |
| ┣ drivingId | String | 주행Id |
| ┣ day | String | 주행날짜 |
| ┗ timeRange | String | 시간범위 |

## 나의주행 상세(AIR)
> Confluence page id: 2262305650 · 최종 수정: 10월 01, 2026

### Function

> 나의주행 상세

### URL

> `/drivingHabitDetail`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| drivingId | String | O | 주행ID |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |
| distance | String | 주행거리 |
| timeTaken | String | 주행시간 Min |
| pointList | List | 주행 좌표 리스트 |
| ┣ x | String | x좌표 (TWCoord) |
| ┣ y | String | y좌표 (TWCoord) |
| ┗ habit | Object | 해당주행내 습관 |
| ┣ address | String | 주소 |
| ┣ time | String | 해당좌표 지나갈때 시간 |
| ┣ firstSpeed | String | habit이 급가속 급감속일때만 내려줌 아닐씨 emptyString처음속도 |
| ┣ secondSpeed | String | habit이 급가속 급감속일때만 내려줌 아닐씨 emptyString바뀐속도 |
| ┗ habit | String | 행위1: 차선이탈10: 전방추돌경고100: 급감속101: 급가속 |

## 나의주행 월별 리스트(AIR)
> Confluence page id: 2262305590 · 최종 수정: 10월 01, 2026

### Function

> 나의주행 월별 리스트

### URL

> `/monthlyMyDriving`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| date | String | O | 조회하고자 하는 년월 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |
| monthlyDrivingList | List | 월간 주행 리스트 |
| ┣ x | String | x좌표 (TWCoord) |
| ┣ y | String | y좌표 (TWCoord) |
| ┣ drivingId | String | 주행Id |
| ┣ day | String | 주행날짜 |
| ┗ timeRange | String | 시간범위 |

## Sources

- Confluence "INAVI AIR API" > AIR 나의주행 (2026-10-27 조회): AIR 나의주행 (2262305566), 나의주행 주간요약바(AIR) (2262305610), 나의주행 일별 리스트(AIR) (2262305630), 나의주행 상세(AIR) (2262305650), 나의주행 월별 리스트(AIR) (2262305590)
