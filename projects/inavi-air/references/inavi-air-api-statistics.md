---
title: "INAVI AIR API — 통계"
category: references
tags: [inavi-air, api, statistics, visibility/internal]
aliases: [통계, 통계 API]
relationships:
  - target: "[[inavi-air-api-detail-spec]]"
    type: derived_from
sources: ["url:https://inavisystems.atlassian.net/wiki/spaces/AS/pages/2262309322"]
summary: >-
    Confluence "INAVI AIR API > 통계" 하위 4개 API(전체 사용자, 월별 신규 가입, 월별 주행이력, 월별 캐쉬 적립 사용자)의 명세를 원문 그대로 옮긴 페이지.
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

# INAVI AIR API — 통계

Confluence "통계" 영역을 원문 그대로 옮긴 것이다. 전체 목록은 [[inavi-air-api-detail-spec]], 공통 Request Header·결과 코드는 [[inavi-air-api-common]], 서비스 개요는 [[inavi-air]]를 본다.

| API | URL |
| --- | --- |
| [[#전체 사용자 조회]] | `/statistics/totalUser` |
| [[#월별 신규 가입 유저]] | `/statistics/newUser` |
| [[#월별 주행이력]] | `/statistics/drivingHistory` |
| [[#월별 캐쉬 적립 사용자]] | `/statistics/cashedUser` |

## 개요
> Confluence page id: 2262309322 · 최종 수정: 10월 06, 2026

- 🧭전체 사용자 조회 → [[#전체 사용자 조회]]
- 🧭월별 신규 가입 유저 → [[#월별 신규 가입 유저]]
- 🧭월별 주행이력 → [[#월별 주행이력]]
- 🧭월별 캐쉬 적립 사용자 → [[#월별 캐쉬 적립 사용자]]

## 전체 사용자 조회
> Confluence page id: 2262309346 · 최종 수정: 10월 01, 2026

### Function

> 전체 사용자 조회

### URL

> `/statistics/totalUser`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| totalLoginUserCount | Integer | 로그인 사용자 수 |
| totalNoLoginUserCount | Integer | 미로그인 사용자 수 |

## 월별 주행이력
> Confluence page id: 2262309364 · 최종 수정: 10월 01, 2026

### Function

> 월별 주행이력

### URL

> `/statistics/drivingHistory`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| year | String | O | 조회하고자 하는 년도 |
| month | String | O | 조회하고자 하는 월 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| monthlyLoginUserDrivingHistoryCount | String | 월별 로그인 사용자 주행 건수 |
| monthlyNoLoginUserDrivingHistoryCount | String | 월별 미로그인 사용자 주행 건수 |

## 월별 캐쉬 적립 사용자
> Confluence page id: 2262309382 · 최종 수정: 10월 01, 2026

### Function

> 월별 캐쉬 적립 사용자

### URL

> `/statistics/cashedUser`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| year | String | O | 조회하고자 하는 년도 |
| month | String | O | 조회하고자 하는 월 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| monthlyCashedUserCount | String | 월별 캐쉬 지급 받은 사용자 수 |

## 월별 신규 가입 유저
> Confluence page id: 2262309400 · 최종 수정: 10월 01, 2026

### Function

> 월별 신규 가입 유저

### URL

> `/statistics/newUser`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| year | String | O | 조회하고자 하는 년도 |
| month | String | O | 조회하고자 하는 월 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| monthlyNewUserCount | String | 월별 건수 |

## Sources

- Confluence "INAVI AIR API" > 통계 (2026-10-27 조회): 통계 (2262309322), 전체 사용자 조회 (2262309346), 월별 주행이력 (2262309364), 월별 캐쉬 적립 사용자 (2262309382), 월별 신규 가입 유저 (2262309400)
