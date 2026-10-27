---
title: "INAVI AIR API — 오르다"
category: references
tags: [inavi-air, api, orda, stamp, visibility/internal]
aliases: [오르다, ORDA API]
relationships:
  - target: "[[inavi-air-api-detail-spec]]"
    type: derived_from
sources: ["url:https://inavisystems.atlassian.net/wiki/spaces/AS/pages/2262308523"]
summary: >-
    Confluence "INAVI AIR API > 오르다"의 [ORDA] 가까운 스탬프 조회 API 명세(요청 좌표, 응답 Stamp 객체)를 원문 그대로 옮긴 페이지.
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

# INAVI AIR API — 오르다

Confluence "오르다" 영역을 원문 그대로 옮긴 것이다. 전체 목록은 [[inavi-air-api-detail-spec]], 공통 Request Header·결과 코드는 [[inavi-air-api-common]], 서비스 개요는 [[inavi-air]]를 본다. 연동 배경은 [[air-orda-stamp-integration-proposal-2025]]에 있다.

| API | URL |
| --- | --- |
| [[#[ORDA] 가까운 스탬프 조회]] | `/orda/stamp` |

## 개요
> Confluence page id: 2262308523 · 최종 수정: 10월 06, 2026

- 🧭\[ORDA\] 가까운 스탬프 조회 → [[#[ORDA] 가까운 스탬프 조회]]

## [ORDA] 가까운 스탬프 조회
> Confluence page id: 2262308541 · 최종 수정: 10월 01, 2026

### Function

> 가까운 스탬프 정보 조회

### URL

> `/orda/stamp`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| 이름 | 타입 | 필수 | 설명 |
| --- | --- | --- | --- |
| x | String | 필수 | APP 현재 위치 X(WGS84) |
| y | String | 필수 | APP 현재 위치 Y(WGS84) |

#### Response

| 이름 | 타입 | Nullable | 설명 |
| --- | --- | --- | --- |
| result\_code | String | false | [[inavi-air-api-common#결과 코드\|📙결과 코드]]<br>0: 성공<br>921: 오르다 서버 연동 오류 |
| result\_msg | String | false | 응답 문구 |
| linkUrl | String | false | Orda 앱연동 백링크 URL |
| stamp | Object | true | Stamp 객체 |

### Stamp 객체

#### Response Parameter

| 이름 | 타입 | Nullable | 설명 |
| --- | --- | --- | --- |
| id | String | false | 스탬프 식별값 |
| tourId | String | false | 투어 ID |
| tourName | String | false | 투어명 |
| name | String | false | 스탬프 이름 |
| address | String | true | 주소 |
| imageUrl | String | true | 스태프 이미지 URL |
| x | String | false | 스탬프 위치 X(WGS84) |
| y | String | false | 스탬프 위치 Y(WGS84) |
| distance | Integer | true | 현재 위치로부터 거리 (단위: M) |

## Sources

- Confluence "INAVI AIR API" > 오르다 (2026-10-27 조회): 오르다 (2262308523), [ORDA] 가까운 스탬프 조회 (2262308541)
