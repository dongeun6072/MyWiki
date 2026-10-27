---
title: "INAVI AIR API — 즐겨찾기"
category: references
tags: [inavi-air, api, favorites, visibility/internal]
aliases: [즐겨찾기]
relationships:
  - target: "[[inavi-air-api-detail-spec]]"
    type: derived_from
sources: ["url:https://inavisystems.atlassian.net/wiki/spaces/AS/pages/2262308976"]
summary: >-
    INAVI AIR API의 즐겨찾기·라벨 추가/수정/삭제, 동기화, 백업, 통합회원 FivePin 즐겨찾기 API 15개의 요청·응답 필드를 Confluence 원문 그대로 옮긴 명세.
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

# INAVI AIR API — 즐겨찾기

Confluence "INAVI AIR API" > "즐겨찾기" 영역을 원문 그대로 옮긴 페이지다. 엔드포인트 색인은 [[inavi-air-api-detail-spec]], 공통 헤더와 결과 코드는 [[inavi-air-api-common]], 소속 프로젝트는 [[inavi-air]]이다.

| API | URL |
|---|---|
| 라벨 데이터 삭제 | `/deleteLabelData` |
| 라벨 데이터 모두 삭제 | `/resetLabel` |
| 라벨 추가 | `/makeLabel` |
| 즐겨찾기 백업 | `/moveRegPoint` |
| 라벨 업데이트 | `/updateLabel` |
| 라벨 삭제 | `/deleteLabel` |
| 라벨 데이터 추가 | `/insertRegToLabel` |
| 즐겨찾기 삭제 | `/regPointDelete` |
| 즐겨찾기 업데이트 | `/regPointUpdate` |
| 즐겨찾기 정보 동기화 | `/regPointsync` |
| 즐겨찾기 추가 | `/regPointInsert` |
| 즐겨찾기삭제 통합회원 FivePin - AIR | `/regPointDeleteUM` |
| 즐겨찾기업데이트 통합회원 FivePin - AIR | `/regPointUpdateUM` |
| 즐겨찾기조회 통합회원 FivePin - AIR | `/airRegpointUM` |
| 즐겨찾기추가 통합회원 FivePin - AIR | `/regPointInsertUM` |

## 개요
> Confluence page id: 2262308976 · 최종 수정: 10월 06, 2026

- 🧭즐겨찾기 추가
- 🧭즐겨찾기 업데이트
- 🧭즐겨찾기 삭제
- 🧭라벨 추가
- 🧭라벨 업데이트
- 🧭라벨 삭제
- 🧭라벨 데이터 추가
- 🧭라벨 데이터 삭제
- 🧭라벨 데이터 모두 삭제
- 🧭즐겨찾기 정보 동기화
- 🧭즐겨찾기 백업
- 🧭즐겨찾기조회 통합회원 FivePin - AIR
- 🧭즐겨찾기추가 통합회원 FivePin - AIR
- 🧭즐겨찾기삭제 통합회원 FivePin - AIR
- 🧭즐겨찾기업데이트 통합회원 FivePin - AIR

## 라벨 데이터 삭제
> Confluence page id: 2262309022 · 최종 수정: 10월 01, 2026

### Function

> 라벨 데이터 삭제

### URL

`/deleteLabelData`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| regPointLabelList | Object | O | 삭제할 라벨안 즐겨찾기 정보 |
| ┣ labelId | String | O | 라벨 ID |
| ┗ regIdList | Array | O | 삭제할 즐겨찾기 ID 리스트 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| agentTs | Integer | 서버 TS |

## 라벨 데이터 모두 삭제
> Confluence page id: 2262309042 · 최종 수정: 10월 01, 2026

### Function

> 라벨 데이터 모두 삭제

### URL

`/resetLabel`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| regPointLabel | Object | O | 삭제할 라벨안 즐겨찾기 정보 |
| ┗ labelId | String | O | 라벨 ID |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| agentTs | Integer | 서버 TS |

## 라벨 추가
> Confluence page id: 2262309062 · 최종 수정: 10월 01, 2026

### Function

> 라벨 추가

### URL

`/makeLabel`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| regPointLabel | Object | O | 라벨정보 |
| ┣ labelName | String | O | 라벨 이름 |
| ┣ labelId | String | O | 라벨 ID(클라이언트 생성 ※default label 은 0 이므로 labelInsert 시에 0이아닌 값으로 만들어줘야함) |
| ┗ labelColor | String | O | 라벨색상 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| agentTs | Integer | 서버 TS |

## 즐겨찾기 백업
> Confluence page id: 2262309082 · 최종 수정: 10월 01, 2026

### Function

> 즐겨찾기 백업

### URL

`/moveRegPoint`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| moveOption | String | O | 이동방향<br>1: 모바일(defaultPrivateKey) -\> SNS(snsPrivateKey)<br>2: SNS(snsPrivateKey) -\> 모바일(defaultPrivateKey)<br>3: 로그아웃시 NO눌럿을경우-\> privateKey 즐겨찾기정보 삭제 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| agentTs | Integer | 서버 TS |

## 라벨 업데이트
> Confluence page id: 2262309102 · 최종 수정: 10월 01, 2026

### Function

> 라벨 업데이트

### URL

`/updateLabel`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| regPointLabel | Object | O | 라벨정보 |
| ┗ labelId | String | O | 라벨 이름 |
| newRegPointLabel | Object | O | 라벨정보 |
| ┣ labelName | String | O | 변경할 라벨 이름 |
| ┗ labelColor | String |  | 변경할 라벨 색상 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| agentTs | Integer | 서버 TS |

## 라벨 삭제
> Confluence page id: 2262309122 · 최종 수정: 10월 01, 2026

### Function

> 라벨삭제(라벨데이터 삭제 + 라벨삭제 (즐겨찾기 데이터는 모두 default 라벨화 됨))

### URL

`/deleteLabel`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| regPointLabel | Object | O | 삭제할 라벨정보 |
| ┗ labelIdList | Array | O | 삭제할 라벨 Id 리스트 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| agentTs | Integer | 서버 TS |

## 라벨 데이터 추가
> Confluence page id: 2262309142 · 최종 수정: 10월 01, 2026

### Function

> 라벨 데이터 추가

### URL

`/insertRegToLabel`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| regPointLabelList | Array | O | 삽입할 라벨안 즐겨찾기 정보 리스트 |
| ┣ labelId | String | O | 라벨 ID |
| ┗ regIdList | Array | O | 삽입할 즐겨찾기 ID 리스트 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| agentTs | Integer | 서버 TS |

## 즐겨찾기 삭제
> Confluence page id: 2262309162 · 최종 수정: 10월 01, 2026

### Function

> 즐겨찾기 삭제

### URL

`/regPointDelete`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| regIdList | Array | O | 삭제할 즐겨찾기ID 리스트 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| agentTs | Integer | 서버 TS |

## 즐겨찾기 업데이트
> Confluence page id: 2262309182 · 최종 수정: 10월 01, 2026

### Function

> 즐겨찾기 업데이트(이름변경)

### URL

`/regPointUpdate`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| regPointData | Object | O | 즐겨찾기 데이터 |
| ┗ regId | String | O | 즐겨찾기 ID |
| newRegPointData | Object | O | 업데이트될 즐겨찾기 데이터 |
| ┣ name | String | O | 즐겨찾기 이름 |
| ┣ type | String | O | 즐겨찾기 타입<br>10 : 집으로<br>20 : 자주가는곳<br>30 : 기본 즐겨찾기 |
| ┣ locationVX | String | O | 위치보기좌표 X |
| ┣ locationVY | String | O | 위치보기좌표 Y |
| ┣ routeX | String | O | 탐색 x좌표 |
| ┣ routeY | String | O | 탐색 y좌표 |
| ┣ ppoi | String |  | parent POI ID(parent POI ID값이 없을 경우 child POI ID값으로 채워줌) |
| ┣ cpoi | String |  | child POI ID |
| ┣ address | String | O | 즐겨찾기 주소 |
| ┣ roadAddress | String |  | 즐겨찾기 도로명 주소 |
| ┗ guideflag | String |  | 음성 발성 여부 |
| regPointLabelList | Array |  | 삽입할 라벨 아이디(라벨 넣지않을거면 안보내도됩니다.) |
| ┣ option | int |  | 삽입 삭제 flag<br>0 : 삭제 1: 삽입 |
| ┣ labelName | String |  | 라벨이름 (LOG)**N** |
| ┗ labelId | String |  | 라벨 ID |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| agentTs | Integer | 서버 TS |

## 즐겨찾기 정보 동기화
> Confluence page id: 2262309202 · 최종 수정: 10월 01, 2026

### Function

> 즐겨찾기 정보 동기화

### URL

`/regPointsync`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| currentTs | Integer | O | 클라이언트 현재 TS |
| justTsFlag | String |  | 서버 TS만 내려받을지 여부<br>0: 규격서에 명시된 리스폰스 다받음<br>1: 서버TS만 내려받음 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| sync | Boolean | false : 동기화 안맞음(서버데이터 내려줌) true : 에이전트와 서버 동기화상태 |
| agentTs | Integer | 서버 TS (요청시 justTsFlag 1 일경우 이것만 내려감) |
| regPointInfo | Array | 즐겨찾기 list (sync가 false 일때만 내려감) |
| ┣ name | String | 즐겨찾기 이름 |
| ┣ ppoi | String | parent POI ID |
| ┣ cpoi | String | child POI ID |
| ┣ address | String | 즐겨찾기 주소 |
| ┣ roadAddress | String | 즐겨찾기 도로명 주소 |
| ┣ routeX | String | 탐색 x좌표 |
| ┣ routeY | String | 탐색 y좌표 |
| ┣ locationVX | String | 위치보기 X좌표 |
| ┣ locationVY | String | 위치보기 Y좌표 |
| ┣ type | String | 즐겨찾기 타입<br>10 : 집으로<br>20 : 자주가는곳<br>30 : 기본 즐겨찾기 |
| ┣ regId | String | 즐겨찾기 ID |
| ┣ guideflag | String | 음성 발성 여부 |
| ┗ labelIdList | Array | 등록되어 있는 라벨아이디<br>0:default |
| labelInfo | Array | 라벨정보 list (sync가 false 일때만 내려감) |
| ┣ labelName | String | 라벨이름 |
| ┣ labelColor | String | 라벨 색상 |
| ┗ labelId | String | 라벨Id |

## 즐겨찾기 추가
> Confluence page id: 2262309222 · 최종 수정: 10월 01, 2026

### Function

> 즐겨찾기 추가

### URL

`/regPointInsert`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| regPointData | Object | O | 즐겨찾기 데이터 |
| ┣ name | String | O | 즐겨찾기 이름 |
| ┣ type | String | O | 즐겨찾기 타입<br>10 : 집으로<br>20 : 자주가는곳<br>30 : 기본 즐겨찾기 |
| ┣ locationVX | String | O | 위치보기좌표 X |
| ┣ locationVY | String | O | 위치보기좌표 Y |
| ┣ routeX | String | O | 탐색 x좌표 |
| ┣ routeY | String | O | 탐색 y좌표 |
| ┣ ppoi | String |  | parent POI ID(parent POI ID값이 없을 경우 child POI ID값으로 채워줌) |
| ┣ cpoi | String |  | child POI ID |
| ┣ address | String | O | 즐겨찾기 주소 |
| ┣ roadAddress | String |  | 즐겨찾기 도로명 주소 |
| ┗ guideflag | String |  | 음성 발성 여부 |
| regPointLabelList | Array |  | 삽입할 라벨 아이디(라벨 넣지않을거면 안보내도됩니다.) |
| ┣ labelName | String |  | 라벨이름 (LOG) |
| ┗ labelId | String |  | 라벨 ID |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| insertRegId | String | 인서트된 즐겨찾기 ID |
| agentTs | Integer | 서버 TS |
| insertLabelList | Array | 삽입된라벨리스트 |

## 즐겨찾기삭제 통합회원 FivePin - AIR
> Confluence page id: 2262309242 · 최종 수정: 10월 01, 2026

### Function

> 즐겨찾기 삭제

### URL

`/regPointDeleteUM`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| regIdList | Array | O | 삭제할 즐겨찾기ID 리스트 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |

## 즐겨찾기업데이트 통합회원 FivePin - AIR
> Confluence page id: 2262309262 · 최종 수정: 10월 01, 2026

### Function

> 즐겨찾기 업데이트(이름변경)

### URL

`/regPointUpdateUM`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| regPointData | Object | O | 즐겨찾기 데이터 |
| ┗ regId | String | O | 즐겨찾기 ID |
| newRegPointData | Object | O | 업데이트될 즐겨찾기 데이터 |
| ┣ name | String | O | 즐겨찾기 이름 |
| ┣ type | String | O | 즐겨찾기 타입<br>10 : 집으로<br>20 : 자주가는곳<br>30 : 기본 즐겨찾기 |
| ┣ locationVX | String | O | 위치보기좌표 X |
| ┣ locationVY | String | O | 위치보기좌표 Y |
| ┣ routeX | String | O | 탐색 x좌표 |
| ┣ routeY | String | O | 탐색 y좌표 |
| ┣ ppoi | String |  | parent POI ID(parent POI ID값이 없을 경우 child POI ID값으로 채워줌) |
| ┣ cpoi | String |  | child POI ID |
| ┣ address | String | O | 즐겨찾기 주소 |
| ┣ roadAddress | String |  | 즐겨찾기 도로명 주소 |
| ┗ guideflag | String |  | 음성 발성 여부 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |

## 즐겨찾기조회 통합회원 FivePin - AIR
> Confluence page id: 2262309282 · 최종 수정: 10월 01, 2026

### Function

> 아이나비 통합회원 FivePin AIR즐겨찾기 조회

### URL

`/airRegpointUM`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| memCode | String | O | 아이나비 통합회원 memberCode |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| regPointInfo | Array | 즐겨찾기 list (sync가 false 일때만 내려감) |
| ┣ name | String | 즐겨찾기 이름 |
| ┣ ppoi | String | parent POI ID |
| ┣ cpoi | String | child POI ID |
| ┣ address | String | 즐겨찾기 주소 |
| ┣ roadAddress | String | 즐겨찾기 도로명 주소 |
| ┣ routeX | String | 탐색 x좌표 |
| ┣ routeY | String | 탐색 y좌표 |
| ┣ locationVX | String | 위치보기 X좌표 |
| ┣ locationVY | String | 위치보기 Y좌표 |
| ┣ type | String | 즐겨찾기 타입<br>10 : 집으로<br>20 : 자주가는곳<br>30 : 기본 즐겨찾기 |
| ┣ regId | String | 즐겨찾기 ID |
| ┗ guideflag | String | 음성 발성 여부 |

## 즐겨찾기추가 통합회원 FivePin - AIR
> Confluence page id: 2262309302 · 최종 수정: 10월 01, 2026

### Function

> 즐겨찾기 추가

### URL

`/regPointInsertUM`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| regPointDataList | List | O | 즐겨찾기 데이터 |
| ┣ name | String | O | 즐겨찾기 이름 |
| ┣ type | String | O | 즐겨찾기 타입<br>10 : 집으로<br>20 : 자주가는곳<br>30 : 기본 즐겨찾기 |
| ┣ locationVX | String | O | 위치보기좌표 X |
| ┣ locationVY | String | O | 위치보기좌표 Y |
| ┣ routeX | String | O | 탐색 x좌표 |
| ┣ routeY | String | O | 탐색 y좌표 |
| ┣ ppoi | String |  | parent POI ID(parent POI ID값이 없을 경우 child POI ID값으로 채워줌) |
| ┣ cpoi | String |  | child POI ID |
| ┣ address | String | O | 즐겨찾기 주소 |
| ┣ roadAddress | String |  | 즐겨찾기 도로명 주소 |
| ┗ guideflag | String |  | 음성 발성 여부 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| insertRegId | String | 인서트된 즐겨찾기 ID |

## Sources

- Confluence "INAVI AIR API" > 즐겨찾기 (2026-10-27 조회): 즐겨찾기 (2262308976), 라벨 데이터 삭제 (2262309022), 라벨 데이터 모두 삭제 (2262309042), 라벨 추가 (2262309062), 즐겨찾기 백업 (2262309082), 라벨 업데이트 (2262309102), 라벨 삭제 (2262309122), 라벨 데이터 추가 (2262309142), 즐겨찾기 삭제 (2262309162), 즐겨찾기 업데이트 (2262309182), 즐겨찾기 정보 동기화 (2262309202), 즐겨찾기 추가 (2262309222), 즐겨찾기삭제 통합회원 FivePin - AIR (2262309242), 즐겨찾기업데이트 통합회원 FivePin - AIR (2262309262), 즐겨찾기조회 통합회원 FivePin - AIR (2262309282), 즐겨찾기추가 통합회원 FivePin - AIR (2262309302)
