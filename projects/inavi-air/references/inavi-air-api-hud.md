---
title: "INAVI AIR API — HUD"
category: references
tags: [inavi-air, api, hud, visibility/internal]
aliases: [HUD]
relationships:
  - target: "[[inavi-air-api-detail-spec]]"
    type: derived_from
sources: ["url:https://inavisystems.atlassian.net/wiki/spaces/AS/pages/2262305792"]
summary: >-
    INAVI AIR HUD 영역의 S/N 인증 API(/authSerialNumber) 요청·응답 필드를 Confluence 원문 그대로 옮긴 명세.
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

# INAVI AIR API — HUD

Confluence "INAVI AIR API" > "HUD" 영역을 원문 그대로 옮긴 페이지다. 엔드포인트 색인은 [[inavi-air-api-detail-spec]], 공통 헤더와 결과 코드는 [[inavi-air-api-common]], 소속 프로젝트는 [[inavi-air]]이다.

| API | URL |
|---|---|
| S/N 인증 | `/authSerialNumber` |

## 개요
> Confluence page id: 2262305792 · 최종 수정: 10월 06, 2026

- 🧭S/N 인증

## S/N 인증
> Confluence page id: 2262305810 · 최종 수정: 10월 01, 2026

### Function

> S/N 인증

### URL

`/authSerialNumber`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| serialNumber | String | O | 시리얼 번호 |
| hudType | String |  | hudType (null인 경우 iHUD, 신규 앱인경우 해당 값을 채워 전송) EX) `air` |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]]<br>0 : 성공<br>200 : 인증되지 않은 시리얼 번호 |
| result\_msg | String | 결과값에 따른 메세지 |

## Sources

- Confluence "INAVI AIR API" > HUD (2026-10-27 조회): HUD (2262305792), S/N 인증 (2262305810)
