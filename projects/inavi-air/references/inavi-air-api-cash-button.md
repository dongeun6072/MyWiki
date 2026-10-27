---
title: "INAVI AIR API — 캐시버튼 (Only Android)"
category: references
tags: [inavi-air, api, cash-button, android, visibility/internal]
aliases: [캐시버튼, 캐시버튼 API]
relationships:
  - target: "[[inavi-air-api-detail-spec]]"
    type: derived_from
sources: ["url:https://inavisystems.atlassian.net/wiki/spaces/AS/pages/2262309418"]
summary: >-
    Confluence "INAVI AIR API > 캐시버튼 (Only Android)"의 에어 캐시 전환 API(캐시버튼 캐시를 에어 캐시로 전환) 명세를 원문 그대로 옮긴 페이지.
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

# INAVI AIR API — 캐시버튼 (Only Android)

Confluence "캐시버튼 (Only Android)" 영역을 원문 그대로 옮긴 것이다. 전체 목록은 [[inavi-air-api-detail-spec]], 공통 Request Header·결과 코드는 [[inavi-air-api-common]], 서비스 개요는 [[inavi-air]]를 본다.

| API | URL |
| --- | --- |
| [[#에어 캐시 전환]] | `/cashButton/cashConversion` |

## 개요
> Confluence page id: 2262309418 · 최종 수정: 10월 06, 2026

- 🧭에어 캐시 전환 → [[#에어 캐시 전환]]

## 에어 캐시 전환
> Confluence page id: 2262309436 · 최종 수정: 10월 01, 2026

### Function

> 에어 캐시 전환 (캐시버튼 캐시 → 에어 캐시 전환)

### URL

> `/cashButton/cashConversion`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| transactionID | String | O | 캐시버튼 SDK에서 전달받은 요청ID |
| basicToken | String | verrsion v3의 호출 시, 필수 | 아바티 API 호출에 필요한 Header 내 Authorization |
| version | String |  | 아바티 호출 API 구분자<br>null: `/shop/exchange/verify`<br>v3: `/shop/exchange/verifyV3` |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]]<br>0 : 성공<br>630 : 캐시버튼 연동 오류<br>970 : 에어 캐시 정합성 체크 실패 (캐시 어뷰징 의심)<br>999 : 정의 되지 않은 오류 |
| result\_msg | String | 결과값에 따른 메세지 |

## Sources

- Confluence "INAVI AIR API" > 캐시버튼 (Only Android) (2026-10-27 조회): 캐시버튼 (Only Android) (2262309418), 에어 캐시 전환 (2262309436)
