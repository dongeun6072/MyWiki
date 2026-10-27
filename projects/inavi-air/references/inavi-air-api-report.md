---
title: "INAVI AIR API — 제보하기"
category: references
tags: [inavi-air, api, report, visibility/internal]
aliases: [제보하기]
relationships:
  - target: "[[inavi-air-api-detail-spec]]"
    type: derived_from
sources: ["url:https://inavisystems.atlassian.net/wiki/spaces/AS/pages/2262308933"]
summary: >-
    INAVI AIR 사용자 제보하기 등록(/report/insert)과 제보하기 조회(/report/read) API의 요청·응답 필드를 Confluence 원문 그대로 옮긴 명세.
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

# INAVI AIR API — 제보하기

Confluence "INAVI AIR API" > "제보하기" 영역을 원문 그대로 옮긴 페이지다. 엔드포인트 색인은 [[inavi-air-api-detail-spec]], 공통 헤더와 결과 코드는 [[inavi-air-api-common]], 소속 프로젝트는 [[inavi-air]]이다. 상위 페이지 "제보하기" 자체가 등록 API 명세를 담고 있어 `## 개요`에 옮겼다.

| API | URL |
|---|---|
| 제보하기 (사용자 제보하기 등록) | `/report/insert` |
| 제보하기 조회 | `/report/read` |

## 개요
> Confluence page id: 2262308933 · 최종 수정: 10월 06, 2026

### Function

> 사용자 제보하기 등록

### URL

`/report/insert`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| posx | String | O | X좌표 |
| posy | String | O | Y좌표 |
| mainCategory | String | O | 대분류 |
| subCategory | String | O | 소분류 |
| reportingPoint | String | O | 제보지점 |
| posName | String |  | 장소명 |
| detailsInfo | String |  | 상세내용 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]]<br>0 : 성공<br>903 : 조회결과 없음<br>999 : 정의되지 않은 오류 |
| result\_msg | String | 결과코드에 따른 메세지 |

🧭제보하기 조회 → [[#제보하기 조회]]

## 제보하기 조회
> Confluence page id: 2262308956 · 최종 수정: 10월 01, 2026

### Function

> 사용자 제보하기 조회

### URL

`/report/read`

[[inavi-air-api-common#Request Header|📙Request Header]]

> 원본에 Request Parameter 표가 없음

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| reportHistory\_list | Array | 제보 내역 전체 리스트 |
| ┣ date | String | 날짜 및 시간 |
| ┣ progressType | String | 진행상황 코드<br>1 : 접수중<br>2 : 처리중<br>3 : 완료<br>5 : 기반영<br>6 : 확인불가 |
| ┣ cashInfo | String | 캐시 제공 정보 |
| ┣ mainCategory | String | 제보 유형 |
| ┣ posName | String | 장소명 |
| ┗  reportingPoint | String | 제보지점 |
| notification | String | 안내사항 |
| 제목 없음 |  |  |

## Sources

- Confluence "INAVI AIR API" > 제보하기 (2026-10-27 조회): 제보하기 (2262308933), 제보하기 조회 (2262308956)
