---
title: "INAVI AIR API — 오픈POI-AIR"
category: references
tags: [inavi-air, api, poi, open-poi, visibility/internal]
aliases: [오픈POI-AIR]
relationships:
  - target: "[[inavi-air-api-detail-spec]]"
    type: derived_from
sources: ["url:https://inavisystems.atlassian.net/wiki/spaces/AS/pages/2262308835"]
summary: >-
    INAVI AIR 오픈POI API 명세 원문 전사. 오픈POI 만들기, 상세조회, 검색 규격을 담는다.
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

# INAVI AIR API — 오픈POI-AIR

Confluence "오픈POI-AIR" 페이지들을 요약 없이 그대로 옮긴 원문 전사본이다. 허브는 [[inavi-air-api-detail-spec]], 공통 헤더·결과 코드는 [[inavi-air-api-common]], 서비스 개요는 [[inavi-air]]를 본다.

| API | URL |
| --- | --- |
| [[#오픈POI만들기]] | `/makeOpenPoi` |
| [[#오픈POI 상세조회]] | `/getOpenPoi` |
| [[#오픈POI 검색]] | `/searchOpenPoi` |

## 개요
> Confluence page id: 2262308835 · 최종 수정: 10월 06, 2026

상위 페이지 "오픈POI-AIR" 본문은 하위 API 링크 목록이다(원본 순서 그대로).

- 🧭오픈POI만들기
- 🧭오픈POI 상세조회
- 🧭오픈POI 검색

## 오픈POI만들기
> Confluence page id: 2262308877 · 최종 수정: 10월 01, 2026

### Function

> 오픈POI만들기

### URL

> `/makeOpenPoi`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| mode | String | O | 오픈POI이름 접속경로POI : 장소검색등록SHARE : 위치공유등록 |
| name | String | O | 오픈POI이름 |
| ilon | String | O | 출발지 경도, 정규화좌표 X값 |
| ilat | String | O | 출발지 위도, 정규화좌표 Y값 |
| private\_key | String | O | 오픈POI만드는 유저의 private\_key |
| start\_dt | String | O | OPENPOI 표시 시작시간 |
| end\_dt | String | O | OPENPOI 표시 종료시간 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| openPoiId | String | 오픈Poi아이디 |

## 오픈POI 상세조회
> Confluence page id: 2262308897 · 최종 수정: 10월 01, 2026

### Function

> 오픈POI상세조회

### URL

> `/getOpenPoi`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| name | String | O | 오픈POI이름 |
| openPoiId | String | O | 오픈Poi아이디 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| openPoi | Object | 오픈Poi정보 |
| ┣ name | String | 오픈POI이름 |
| ┣ ilon | String | 출발지 경도, 정규화좌표 X값 |
| ┣ ilat | String | 출발지 위도, 정규화좌표 Y값 |
| ┣ start\_dt | String | OPENPOI 표시 시작시간 |
| ┣ end\_dt | String | OPENPOI 표시 종료시간 |
| ┗ openPoiId | String | 오픈Poi 아이디 |

## 오픈POI 검색
> Confluence page id: 2262308857 · 최종 수정: 10월 01, 2026

### Function

> 오픈POI 검색

### URL

> `/searchOpenPoi`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| query | String | O | 검색하고자 하는 OPENPOI이름(초성검색 안됨) |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| openPoi | Array | openPoi정보 |
| ┣ name | String | 검색 결과이름 |
| ┗ openPoiId | String | 오픈Poi 아이디 |

## Sources

- Confluence "INAVI AIR API" > 오픈POI-AIR (2026-10-27 조회): 오픈POI-AIR (2262308835), 오픈POI만들기 (2262308877), 오픈POI 상세조회 (2262308897), 오픈POI 검색 (2262308857)
