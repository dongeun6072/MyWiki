---
title: "INAVI AIR API — w3w"
category: references
tags: [inavi-air, api, w3w, visibility/internal]
aliases: [w3w, what3words, INAVI AIR w3w API]
relationships:
  - target: "[[inavi-air-api-detail-spec]]"
    type: derived_from
sources: ["url:https://inavisystems.atlassian.net/wiki/spaces/AS/pages/2262306051"]
summary: >-
    INAVI AIR w3w(what3words) API 명세 원문 전사. 3단어 추천어 검색(/w3w/autoSuggest)과 w3w 단어 검색(/w3w/wordSearch)을 담는다.
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

# INAVI AIR API — w3w

Confluence "w3w" 페이지들을 요약 없이 그대로 옮긴 원문 전사본이다. 허브는 [[inavi-air-api-detail-spec]], 공통 헤더·결과 코드는 [[inavi-air-api-common]], 서비스 개요는 [[inavi-air]]를 본다.

| API | URL |
| --- | --- |
| [[#3단어 추천어 검색]] | `/w3w/autoSuggest` |
| [[#w3w 단어 검색]] | `/w3w/wordSearch` |

## w3w (상위 페이지)
> Confluence page id: 2262306051 · 최종 수정: 10월 06, 2026

상위 페이지 본문은 하위 API 링크 목록이다(원본 순서 그대로).

- 🧭3단어 추천어 검색
- 🧭w3w 단어 검색

## 3단어 추천어 검색
> Confluence page id: 2262306071 · 최종 수정: 10월 01, 2026

### Function

> 3단어 추천어 검색 (w3w)

### URL

> `/w3w/autoSuggest`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| words | String | O | w3w 추천어 검색을 위한 .으로 구분 된 세 단어<br>**EX)**<br>- 닮은.조언.ㄱ<br>- 닮은.조언.감사 |
| posx | String | O | 현재 위치 정규화 X 좌표<br>EX) 160337 |
| posy | String | O | 현재 위치 정규화 Y 좌표<br>EX) 501885 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]]<br>0 : 성공<br>610 : w3w 추천어 검색 파라미터 오류<br>903 : 조회 결과 없음<br>999 : 정의 되지 않은 오류 |
| result\_msg | String | 결과값에 따른 메세지 |
| autoSuggestList | Array | w3w 추천어 검색 결과 리스트 |
| ┣ words | String | w3w 추천어 |
| ┣ admcode | String | 행정코드 `2023-06-21 패치로 인해 Empty String 리턴` |
| ┣ x | String | 정규화 X 좌표<br>EX) 160337 `2023-06-21 패치로 인해 Empty String 리턴` |
| ┣ y | String | 정규화 Y 좌표<br>EX) 501885 `2023-06-21 패치로 인해 Empty String 리턴` |
| ┣ address | String | 주소 `2023-06-21 패치로 인해 Empty String 리턴` |
| ┣ cut\_address | String | 표출 주소 |
| ┣ road\_address | String | 도로명 주소 `2023-06-21 패치로 인해 Empty String 리턴` |
| ┣ cut\_road\_address | String | 축약 도로명 주소 `2023-06-21 패치로 인해 Empty String 리턴` |
| ┣ jibun | String | 지번 `2023-06-21 패치로 인해 Empty String 리턴` |
| ┣ bldnum | String | 빌딩번호 `2023-06-21 패치로 인해 Empty String 리턴` |
| ┣ address\_type | String | 주소 매핑 타입<br>0 : 행정계<br>1 : 새주소 폴리곤<br>2 : 지적도 폴리곤<br>3 : 인접지번<br>4 : 행정계 `2023-06-21 패치로 인해 Empty String 리턴` |
| ┗ distanceToFocusKm | Integer | 현재 지점에서의 거리 (km) |

## w3w 단어 검색
> Confluence page id: 2262306091 · 최종 수정: 10월 01, 2026

### Function

> w3w 단어 검색

### URL

> `/w3w/wordSearch`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| words | String | O | w3w 추천어 검색을 위한 .으로 구분 완성 된 세 단어<br>**EX)**<br>- 닮은.조언.감사 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]]<br>0 : 성공<br>610 : w3w 단어 검색 파라미터 오류  (EX : 닮.조.감)<br>903 : 조회 결과 없음<br>999 : 정의 되지 않은 오류 |
| result\_msg | String | 결과값에 따른 메세지 |
| admcode | String | 행정코드 |
| x | String | 정규화 X 좌표<br>EX) 160337 |
| y | String | 정규화 Y 좌표<br>EX) 501885 |
| address | String | 주소 |
| cut\_address | String | 축약 주소 |
| road\_address | String | 도로명 주소 |
| cut\_road\_address | String | 축약 도로명 주소 |
| jibun | String | 지번 |
| bldnum | String | 빌딩번호 |
| address\_type | String | 주소 매핑 타입<br>0 : 행정계<br>1 : 새주소 폴리곤<br>2 : 지적도 폴리곤<br>3 : 인접지번<br>4 : 행정계 |

## Sources
- Confluence "INAVI AIR API" > w3w (2026-10-27 조회): w3w (2262306051), 3단어 추천어 검색 (2262306071), w3w 단어 검색 (2262306091)
