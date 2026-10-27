---
title: "INAVI AIR API — LOG-AIR"
category: references
tags: [inavi-air, api, logging, visibility/internal]
aliases: [LOG-AIR]
relationships:
  - target: "[[inavi-air-api-detail-spec]]"
    type: derived_from
sources: ["url:https://inavisystems.atlassian.net/wiki/spaces/AS/pages/2262305830"]
summary: >-
    INAVI AIR LOG-AIR 영역의 제보하기 로그전송 API(/reportLog) 요청·응답 필드를 Confluence 원문 그대로 옮긴 명세.
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

# INAVI AIR API — LOG-AIR

Confluence "INAVI AIR API" > "LOG-AIR" 영역을 원문 그대로 옮긴 페이지다. 엔드포인트 색인은 [[inavi-air-api-detail-spec]], 공통 헤더와 결과 코드는 [[inavi-air-api-common]], 소속 프로젝트는 [[inavi-air]]이다.

| API | URL |
|---|---|
| 제보하기 | `/reportLog` |

## 개요
> Confluence page id: 2262305830 · 최종 수정: 10월 06, 2026

- 🧭제보하기

## 제보하기
> Confluence page id: 2262305848 · 최종 수정: 10월 01, 2026

### Function

> 제보하기 로그전송

### URL

`/reportLog`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| category | String | O | 제보하기 화면 카테고리<br>MAP : 지도문제<br>TRAFFIC : 교통<br>CAMERA : 카메라<br>ACCIDENT : 사고<br>PLACE : 장소등록<br>ETC : 기타 |
| index | String | O | 카테고리별 세부항목 (세부항목이 가변적이므로 index 번호로 입력) (0... ) |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |

## Sources

- Confluence "INAVI AIR API" > LOG-AIR (2026-10-27 조회): LOG-AIR (2262305830), 제보하기 (2262305848)
