---
title: "INAVI AIR API — SKP 전용 API"
category: references
tags: [inavi-air, api, skp, advertising, visibility/internal]
aliases: [SKP 전용 API, SKP API]
relationships:
  - target: "[[inavi-air-api-detail-spec]]"
    type: derived_from
sources: ["url:https://inavisystems.atlassian.net/wiki/spaces/AS/pages/2262306015"]
summary: >-
    Confluence "INAVI AIR API > SKP 전용 API"의 광고 포인트 기반 에어 캐시 적립(postback) API 명세를 원문 그대로 옮긴 페이지.
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

# INAVI AIR API — SKP 전용 API

Confluence "SKP 전용 API" 영역을 원문 그대로 옮긴 것이다. 전체 목록은 [[inavi-air-api-detail-spec]], 공통 Request Header·결과 코드는 [[inavi-air-api-common]], 서비스 개요는 [[inavi-air]]를 본다.

| API | URL |
| --- | --- |
| [[#광고 포인트 기반 에어 캐시 적립]] | `/event/cash/postback` |

## 개요
> Confluence page id: 2262306015 · 최종 수정: 10월 06, 2026

- 🧭광고 포인트 기반 에어 캐시 적립 → [[#광고 포인트 기반 에어 캐시 적립]]

---

### 삼성중공업 전달 규격서

INAVI\_API\_v1.0.0.xlsx (Confluence 첨부 파일, 위키에는 미수록)

## 광고 포인트 기반 에어 캐시 적립
> Confluence page id: 2262306033 · 최종 수정: 10월 01, 2026

> Planet AD 서버에서 포인트 적립 요청을 받아 에어 캐시로 변경

### URL

> `/event/cash/postback`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| transaction\_id | String | O | transaction ID |
| user\_id | String | O | 유저 키 (EX : 1234) |
| point | int | O | 지급할 포인트 |
| action\_type | String | O | 포인트를 지급 받기 위해 사용자가 취한 액션 타입 |
| title | String | O | 광고 제목 |
| unit\_id | int | O | 광고가 노출 된 지면 ID |
| event\_at | long | O | 포인트 지급 시점 |

#### Response Parameter

| 응답 코드 | HTTP 상태 코드 | description |
| --- | --- | --- |
| 0 | 200 | 성공 |
| 903 | 401 | UNAUTHORIZED (사용자 인증 실패) |
| 980 | 400 | BAD\_REQUEST (다중 캐시 지급 여부 확인) |
| 970 | 500 | INTERNAL\_SERVER\_ERROR (내부 서버 오류) |

## Sources

- Confluence "INAVI AIR API" > SKP 전용 API (2026-10-27 조회): SKP 전용 API (2262306015), 광고 포인트 기반 에어 캐시 적립 (2262306033)
