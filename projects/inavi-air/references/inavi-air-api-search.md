---
title: "INAVI AIR API — 검색"
category: references
tags: [inavi-air, api, search, poi, visibility/internal]
aliases: [검색, INAVI AIR 검색 API]
relationships:
  - target: "[[inavi-air-api-detail-spec]]"
    type: derived_from
sources: ["url:https://inavisystems.atlassian.net/wiki/spaces/AS/pages/2262306111"]
summary: >-
    INAVI AIR 검색 API(/sire/*) 명세 원문 전사. 주소·좌표·행정계 검색, POI 명칭·상세·주변·하위시설물, SQE 통합검색, 추천어, 경로 주변 다중 카테고리, CCTV, 교통정보 요약맵, 최적 지적 검색을 담는다.
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

# INAVI AIR API — 검색

Confluence "검색" 페이지들을 요약 없이 그대로 옮긴 원문 전사본이다. 허브는 [[inavi-air-api-detail-spec]], 공통 헤더·결과 코드는 [[inavi-air-api-common]], 서비스 개요는 [[inavi-air]]를 본다.

| API | URL |
| --- | --- |
| [[#CCTV 검색]] | `/sire/searchCctv` |
| [[#CCTV용 고속도로 검색]] | `/sire/searchRoad` |
| [[#Reference 주변 검색]] | `/sire/searchReference` |
| [[#POI 상세정보 조회]] | `/sire/searchPoiDetail` |
| [[#POI 하위시설물 조회]] | `/sire/searchSubpoi` |
| [[#POI 명칭 검색]] | `/sire/searchPoiNumber` |
| [[#SQE 통합검색]] | `/sire/searchSQE` |
| [[#경로 주변 다중 카테고리 검색]] | `/sire/searchRouteAroundMulti` |
| [[#대중교통 추천어 초성 검색]] | `/multiSearchProposer` |
| [[#교통정보 요약맵 검색]] | `/sire/searchTism` |
| [[#구 주소 검색]] | `/sire/searchOldAddr` |
| [[#주변 POI 검색]] | `/sire/searchPoiAround` |
| [[#새 주소 검색]] | (원본에 URL 없음) |
| [[#좌표로 주소 검색]] | `/sire/revgeocoding` |
| [[#최적 지적 검색]] | `/sire/optimalPosition` |
| [[#추천어 검색]] | `/sire/searchProposer` |
| [[#하위 행정계 도로명 검색]] | `/sire/searchSubAddrRoadName` |
| [[#하위 행정계 검색]] | `/sire/searchSubAddr` |

## 검색 (상위 페이지)
> Confluence page id: 2262306111 · 최종 수정: 10월 06, 2026

상위 페이지 본문은 하위 API 링크 목록이다(원본 순서 그대로).

- 🧭구 주소 검색
- 🧭새 주소 검색
- 🧭좌표로 주소 검색
- 🧭하위 행정계 검색
- 🧭하위 행정계 도로명 검색
- 🧭POI 명칭 검색
- 🧭SQE 통합검색
- 🧭POI 상세정보 조회
- 🧭주변 POI 검색
- 🧭POI 하위시설물 조회
- 🧭Reference 주변 검색
- 🧭추천어 검색
- 🧭경로 주변 다중 카테고리 검색
- 🧭교통정보 요약맵 검색
- 🧭CCTV용 고속도로 검색
- 🧭CCTV 검색
- 🧭대중교통 추천어 초성 검색
- 🧭최적 지적 검색

## CCTV 검색
> Confluence page id: 2262306163 · 최종 수정: 10월 01, 2026

### Function

> CCTV 검색

### URL

> `/sire/searchCctv`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| keyword | String |  | 검색어<br>검색어가 CCTV 명칭에 exact 매치되거나 partial 매치되는 경우, 매칭된 CCTV 데이터를 제공 |
| road\_id | String |  | 고속도로 노선번호<br>입력 시, 해당 노선번호의 CCTV 데이터 제공(CCTV용 고속도로 검색 결과의 노선번호 입력) |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| total\_count | Integer | CCTV 검색 결과 개수 |
| cctv\_list | Array | CCTV 검색 결과 리스트 |
| ┣ cctv\_id | Integer | CCTV ID |
| ┣ cctv\_name | String | CCTV 명칭 |
| ┣ cctv\_seq | Integer | 동일 고속도로의 CCTV 위치 순서(1\~n)<br>\* 고속도로 정보가 없는 경우 NULL |
| ┣ road\_id | Integer | CCTV가 위치한 고속도로 노선번호<br>\* 고속도로 정보가 없는 경우 NULL |
| ┗ road\_name | String | CCTV가 위치한 고속도로 명칭<br>\* 고속도로 정보가 없는 경우 NULL |

## CCTV용 고속도로 검색
> Confluence page id: 2262306183 · 최종 수정: 10월 01, 2026

### Function

> CCTV용 고속도로 검색

### URL

> `/sire/searchRoad`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| keyword | String |  | 검색어<br>검색어가 고속도로 명칭에 exact 또는 partial 매치되는 경우, 매칭된 CCTV용 고속도로 데이터를 제공<br>\* keyword가 NULL인 경우, 전체 고속도로 데이터 리스트 리턴 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| total\_count | Integer | 고속도로 검색 결과 개수 |
| road\_list | Array | 고속도로 검색 결과 리스트 |
| ┣ road\_id | Integer | 고속도로 노선번호 |
| ┗ road\_name | String | 고속도로 명칭 |

## Reference 주변 검색
> Confluence page id: 2262306203 · 최종 수정: 10월 01, 2026

### Function

> Reference 주변 검색

### URL

> `/sire/searchReference`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| cutflag | String | O | 주소표현구분<br>0 : 정식행정계 주소<br>1 : 단축행정계 주소 |
| coordtype | String | O | 좌표형식<br>0 : 정규화 좌표<br>1 : WGS 84<br>2 : TM |
| startposition | String | O | 시작위치<br>0 : 첫번째 위치<br>ex) 20 -\> 21번째 결과부터 reqcount 만큼 조회 |
| reqcount | String | O | 요청개수 |
| depth | String | O | 하위시설물 요구 depth<br>0 : depth 사용 안함(검색결과 모두 표출) (Default)<br>1 : 1 depth 만 요청(최상위 depth)<br>2 : 2 depth 까지 요청<br>3 : 3 depth 까지 요청 |
| type | String | O | reference type<br>0 : POI<br>1 : 구주소<br>2 : 새주소<br>3 : 가로명<br>4 : 행정계<br>5 : 현위치 |
| id | String |  | reference id (type=3인경우 필수입력) |
| posx | String | O | reference x좌표 (reference posx) |
| posy | String | O | reference y좌표 (reference posy) |
| admcode | String |  | referece admcode |
| keyword | String | △ | 검색 - 명칭 (검색어 - 명칭부분), catecode값이 없는 경우 필수 |
| catecode | String | △ | 검색 - 분류코드 (검색어 - 분류코드), keyword값이 없는 경우 필수 |
| radius | String | O | 검색반경 (meter 단위) |
| curx | String | O | Reference검색의 경우 현위치 X좌표 |
| cury | String | O | Reference검색의 경우 현위치 Y좌표 |
| sortopt | String |  | 정렬option<br>1 : 명칭순 정렬<br>2 : 거리순 정렬<br>3 : 이름매치-\>거리순 정렬<br>4 : 검색어 Weight 정렬 (엔진기준)(Default)<br>5 : 검색어 Weight 정렬 + length(엔진기준) |
| sortoilprice | String |  | 주유소 검색결과 유가순 정렬 option<br>0 : 유가순 정렬 Option 사용안함 (Default)<br>1 : 휘발유순 정렬<br>2 : 고급휘발유순 정렬<br>3 : 경유순 정렬<br>4 : LPG 가격순 |
| evcstatus | String |  | 0 : 전기차 충전소 충전 가능 여부 Filter Option 사용안함(default)<br>1 : 사용중<br>2 : 사용 가능<br>3 : 사용 불가 |
| evctype | Array |  | 전기차 충전소 충전 타입 필터 리스트 |
| ┗ val | String |  | 0 : 전기차 충전소 충전 타입 여부 Filter Option 사용안함(default)<br>1 : DC차데모<br>2 : AC완속<br>3 : DC콤보<br>4 : AC급속3상 |
| sortevcprice | String |  | 0: 전기차 충전소 가격순 정렬 Option 사용안함(default)<br>1: 가격순 정렬 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| totalcount | Integer | POI 전체 검색결과 대상 개수 |
| count | Integer | POI 검색 결과 개수 |
| poi | Array | POI 검색결과 List [[inavi-air-api-data#POI_DATA_A\|POI_DATA_A]] |
| hasgasstation | Boolean | oilprice 정보 제공 여부 |
| oilprice | Object | 유가 정보 |
| ┣ max\_g\_price | Integer | 최고 휘발유 가격 |
| ┣ min\_g\_price | Integer | 최저 휘발유 가격 |
| ┣ avg\_g\_price | Integer | 평균 휘발유 가격 |
| ┣ max\_hg\_price | Integer | 최고 고급 휘발유 가격 |
| ┣ min\_hg\_price | Integer | 최저 고급 휘발유 가격 |
| ┣ avg\_hg\_price | Integer | 평균 고급 휘발유 가격 |
| ┣ max\_d\_price | Integer | 최고 경유 가격 |
| ┣ min\_d\_price | Integer | 최저 경유 가격 |
| ┣ avg\_d\_price | Integer | 평균 경유 가격 |
| ┣ max\_l\_price | Integer | 최고 LPG 가격 |
| ┣ min\_l\_price | Integer | 최저 LPG 가격 |
| ┗ avg\_l\_price | Integer | 평균 LPG 가격 |

## POI 상세정보 조회
> Confluence page id: 2262306225 · 최종 수정: 10월 01, 2026

### Function

> POI 상세정보 조회

### URL

> `/sire/searchPoiDetail`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| cutflag | String | O | 주소표현구분<br>0 : 정식행정계 주소<br>1 : 단축행정계 주소 |
| coordtype | String | O | 좌표형식 0 : 정규화 좌표 |
| startposition | String | O | 시작위치<br>0 : 첫번째 위치<br>ex) 20 -\> 21번째 결과부터 reqcount 만큼 조회 |
| reqcount | String | O | 요청개수 |
| poiid | String | O | poi id<br>구분자 "│"와 함께 입력 (복수개 가능 186개까지)<br>ex) poiid=123│1234│234 |
| simpleRes | String | O | 멀티 입구점 결과만 받음. Y/N |
| w3wYn | String |  | W3W 연동 여부 (Default : N) Y : 연동 N : 미 연동 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| totalcount | Integer | POI 전체 검색결과 대상 개수 |
| count | Integer | POI 검색 결과 개수 |
| poiinfo | Array | POI 검색결과 List |
| ┣ poiid | Integer | poi id<br>simpleRes가 Y인 경우 해당 결과만 반환 됨 |
| ┣ dpx | String | display X좌표(WGS84의 경우 longitude) |
| ┣ dpy | String | display Y좌표(WGS84의 경우 latitude) |
| ┣ rpx | String | 탐색 X좌표(WGS84의 경우 longitude) |
| ┣ rpy | String | 탐색 Y좌표(WGS84의 경우 latitude) |
| ┣ routepoints | Array | 탐색용 좌표 리스트<br>simpleRes가 Y인 경우 해당 결과만 반환 됨 |
| ┣ rpx | String | 탐색 X좌표(WGS84의 경우 longitude) |
| ┗ rpy | String | 탐색 Y좌표(WGS84의 경우 latitude) |
| ┣ name1 | String | 정식명칭 |
| ┣ name2 | String | 축약명칭 |
| ┣ name3 | String | 확장명칭1 |
| ┣ name4 | String | 확장명칭2 |
| ┣ admcode | String | 행정코드 |
| ┣ address | String | 주소 |
| ┣ jibun | String | 지번 |
| ┣ roadname | String | 새주소 도로명 |
| ┣ roadjibun | String | 새주소 지번 |
| ┣ detailaddress | String | 상세주소 |
| ┣ catecode | String | 분류코드 |
| ┣ catename | String | 분류명칭 |
| ┣ dp\_catecode | String | DP 분류코드 |
| ┣ fulladdress | String | 전체주소(행정주소+지번+상세주소) |
| ┣ zip | String | 우편번호 |
| ┣ homepage | String | 홈페이지 url |
| ┣ email | String | E-MAIL |
| ┣ howtogo | String | 교통편 |
| ┣ tel1 | String | 전화번호1 |
| ┣ tel2 | String | 전화번호2 |
| ┣ fax1 | String | 팩스번호1 |
| ┣ fax2 | String | 팩스번호2 |
| ┣ icode | String | ICODE |
| ┣ badgeflag | Boolean | Badge 유무 |
| ┣ imagecount | Integer | poi 이미지 개수 |
| ┣ operation\_value | String | 영업시간 |
| ┣ closing\_flag | Boolean | 당일 휴무일 여부 |
| ┣ parking\_value | String | 주차정보 |
| ┣ etc\_count | Integer | 분류기타항목갯수 |
| ┣ etcinfo | Array | 분류기타항목 |
| ┣ name | String | 분류기타항목설명 |
| ┗ value | String | 분류기타항목내용 |
| ┣ hasoildata | Boolean | 유가 데이터 존재여부 |
| ┣ oildata | Object | 유가 데이터 정보 |
| ┣ g\_price | Integer | 휘발유 가격 |
| ┣ hg\_price | Integer | 고급휘발유 가격 |
| ┣ d\_price | Integer | 경유 가격 |
| ┣ l\_price | Integer | LPG 가격 |
| ┗ updatetime | String | Update 시간 |
| ┣ externallink | Array | 외부연동 ID |
| ┣ ID | String | 연동 ID(PLOG일 경우 URL끝에 &app=ktnavi 붙여서 호출) |
| ┣ Site | String | 연동 Site(망고플레이트/PLOG) |
| ┣ ExtraInfo1 | String | 추가정보1(if exist) |
| ┗ ExtraInfo2 | String | 추가정보2(if exist) |
| ┗ evcstation | Object | [[inavi-air-api-data#전기차 충전소 정보\|전기차 충전소 정보]] |
| w3wWords | String | w3w 단어 (미존재 케이스의 경우 “”) |

## POI 하위시설물 조회
> Confluence page id: 2262306247 · 최종 수정: 10월 01, 2026

### Function

> POI 하위시설물 조회

### URL

> `/sire/searchSubpoi`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| cutflag | String | O | 주소표현구분<br>0 : 정식행정계 주소<br>1 : 단축행정계 주소 |
| coordtype | String | O | 좌표형식<br>0 : 정규화 좌표<br>1 : WGS 84<br>2 : TM |
| startposition | String | O | 시작위치<br>0 : 첫번째 위치<br>ex) 20 -\> 21번째 결과부터 reqcount 만큼 조회 |
| reqcount | String | O | 요청개수 |
| poiid | String | O | POI ID (복수개 지원 안됨) |
| x1 | String |  | 현위치 또는 지도중심좌표. x, y좌표가 모두 NULL또는 0일 경우 거리 계산을 수행하지 않음. |
| y1 | String |  | 현위치 또는 지도중심좌표. x, y좌표가 모두 NULL또는 0일 경우 거리 계산을 수행하지 않음. |

#### Request Parameter

> 원본에서 응답 표의 제목도 "Request Parameter"로 되어 있다(원문 그대로). 필드명은 아래 하위 페이지로 링크되어 있다.

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| totalcount | Integer | POI 전체 검색결과 대상 개수 |
| count | Integer | POI 검색 결과 개수 |
| poi | Array | POI 검색결과 List [[inavi-air-api-data#POI_DATA_B\|POI_DATA_B]] |

[[inavi-air-api-data#POI_DATA_B|POI_DATA_B]]

#### count
> Confluence page id: 2262306297 · 최종 수정: 10월 01, 2026

(본문 없음)

> 원본 표가 비어 있음

#### poi
> Confluence page id: 2262306313 · 최종 수정: 10월 01, 2026

(본문 없음)

> 원본 표가 비어 있음

#### result_code
> Confluence page id: 2262306329 · 최종 수정: 10월 01, 2026

(본문 없음)

> 원본 표가 비어 있음

#### result_msg
> Confluence page id: 2262306345 · 최종 수정: 10월 01, 2026

(본문 없음)

> 원본 표가 비어 있음

#### totalcount
> Confluence page id: 2262306361 · 최종 수정: 10월 01, 2026

(본문 없음)

> 원본 표가 비어 있음

## POI 명칭 검색
> Confluence page id: 2262306377 · 최종 수정: 10월 01, 2026

### Function

> POI 명칭 검색

### URL

> `/sire/searchPoiNumber`

[[inavi-air-api-common#Request Header|Request Header]]

> 원본에 Request Parameter 표가 없음(Response Parameter 표만 있음).

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| totalcount | Integer | 전체 검색결과 대상 개수 |
| count | Integer | 검색 결과 개수 |
| poitotalcount | Integer | Thinkware POI 전체 검색결과 대상 개수 |
| poicount | Integer | Thinkware POI 검색 결과 개수 |
| tel\_poitotalcount | Integer | Tel POI 전체 검색결과 대상 개수 |
| tel\_poicount | Integer | Tel POI 검색 결과 개수 |
| ucp\_poitotalcount | Integer | User POI 전체 검색결과 대상 개수 |
| ucp\_poicount | Integer | User POI 검색 결과 개수 |
| poi | Array | POI 검색결과 List [[inavi-air-api-data#POI_DATA_A\|POI_DATA_A]] |
| tel | Array | Tel POI 검색결과 List [[inavi-air-api-data#POI_DATA_A\|POI_DATA_A]] |
| ucp | Array | User POI 검색결과 List [[inavi-air-api-data#POI_DATA_A\|POI_DATA_A]] |

[[inavi-air-api-data#POI_DATA_A|POI_DATA_A]]

## SQE 통합검색
> Confluence page id: 2262306417 · 최종 수정: 10월 01, 2026

### Function

> SQE 통합검색

### URL

> `/sire/searchSQE`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| cutflag | String | O | 주소표현구분<br>- 0 : 정식행정계 주소<br>- 1 : 단축행정계 주소 |
| coordtype | String | O | 좌표형식<br>- 0 : 정규화 좌표<br>- 1 : WGS 84<br>- 2 : TM |
| startposition | String | O | 시작위치<br>- 0 : 첫번째 위치<br>ex) 20 -\> 21번째 결과부터 reqcount 만큼 조회 |
| reqcount | String | O | 요청개수 |
| depth | String | O | 하위시설물 요구 depth<br>0 : depth 사용 안함(검색결과 모두 표출) (Default)<br>1 : 1 depth 만 요청(최상위 depth)<br>2 : 2 depth 까지 요청<br>3 : 3 depth 까지 요청 |
| mode | String | O | 검색 mode<br>1 : poi 검색<br>2 : adm 검색<br>3 : poi+adm 검색 (Default)<br>4 : poi+adm+tel+ucp 검색<br>5 : tel db 검색<br>6 : ucp 검색<br>7 : poi+tel+adm 검색 (poi, tel 검색결과 Universal 제공) |
| query | String | O | 검색어 |
| subString | String |  | 자동완성어 사용시에 사용자가 입력한 부분(ex : '주'를 입력한 이후 '주유소' 선택시, '주'가 subString)<br>자동완성어/추천어재검색시에만 사용됨<br>추천어재검색시에는 검색 실패한 검색어가 subString이 됨<br>AI연동시에는 uword(AI엔진이 인식한 단어) 가 subString이됨 |
| autoSearchFlag | String |  | 자동완성어 사용여부 flag<br>Y : 사용<br>N : 미사용 |
| spopt | String | O | 공간검색 option<br>0 : 공간검색 사용 안함 (Default)<br>1 : Extent 검색<br>2 : Range 검색<br>3 : K-NN 검색 (x1, y1만 사용함) – 추후 지원 예정 |
| radius | String |  | 반경<br>spopt가 2인 경우 사용 (Meter 단위) |
| admcode | String |  | 행정코드<br>행정코드 조건 검색 |
| x1 | String |  | X좌표<br>- spopt가 0인 경우 기준점 X좌표<br>- spopt가 1인 경우 Extent의 좌상단 X좌표<br>- spopt가 2,3인 경우 기준점 X좌표<br>※ Range검색 및 K-NN의 경우 반드시 필요 |
| y1 | String |  | Y좌표<br>- spopt가 0인 경우 기준점 Y좌표<br>- spopt가 1인 경우 Extent의 좌상단 Y좌표<br>- spopt가 2,3인 경우 기준점 Y좌표<br>※ Range검색 및 K-NN의 경우 반드시 필요 |
| x2 | String |  | X좌표<br>- spopt가 1인 경우 Extent의 우하단 X좌표<br>- spopt가 2,3인 경우 사용 안함 |
| y2 | String |  | Y좌표<br>- spopt가 1인 경우 Extent의 우하단 Y좌표<br>- spopt가 2,3인 경우 사용 안함 |
| sortopt | String | O | 정렬 option<br>- 1 : 명칭순 정렬<br>- 2 : 거리순 정렬 (좌표를 입력한 경우)<br>- 3 : 이름매치 -\> 거리순 정렬 (좌표를 입력한 경우)<br>- 4 : 검색어 Weight 정렬 (엔진기준) (Default)<br>- 5 : 검색어 Weight 정렬 + length (엔진기준)<br>- 6 : 선호카테고리 우선 정렬<br>- 7 : 최신데이터 순 정렬 |
| favcatecode | String |  | 선호카테고리<br>선호카테고리 분류 코드(대/중/소 입력 가능) |
| neighboropt | String |  | 주변검색 결과표현 option<br>- 0 : Reference 정보 - 주변POI를 하위시설물 형태 depth로 표현(Default)<br>- 각 Reference 당 검색되는 POI의 개수는 최대 20개로 제한<br>- 1 : Reference정보+최상위 Reference의 검색결과 제공<br>- Reference정보는 queryParse 파트로 제공<br>- 검색결과는 poi 파트로 제공<br>- Reference검색 결과인 경우 queryParse부분과 count정보등만 제공함 (여러 개의 Reference가 검색되는 경우 queryParse 파트의 첫번째 Reference에 대한 검색결과를 제공한다) |
| sortoilprice | String |  | 주유소 검색결과 유가순 정렬 option<br>- 0 : 유가순 정렬 Option 사용안함 (Default)<br>- 1 : 휘발유순 정렬<br>- 2 : 고급휘발유순 정렬<br>- 3 : 경유순 정렬<br>- 4 : LPG 가격순 |
| sflag | String | O | 음성검색 구분 flag<br>- V : 음성<br>- T : 타이핑<br>- L : 최근검색어<br>- A : AI검색<br>- N : 구분안됨 |
| searchType | String | O | 검색 유형: 통합검색/최근검색어/추천어재검색/위치주변통합검색/에어봇검색<br>- UNITED: 통합검색<br>- RECENT: 최근검색어<br>- SGST: 추천어재검색<br>- NEARBY: 위치주변 통합검색<br>- AIRBOT: 에어봇검색 |
| evcstatus | String |  | 전기차 충전소 충전 가능 여부 Filter Option<br>- 0: 사용안함(default)<br>- 1 : 사용중<br>- 2 : 사용 가능<br>- 3 : 사용 불가 |
| evctype | Array |  | 전기차 충전소 충전 타입 필터 리스트 |
| ┗ val | String |  | 전기차 충전소 충전 타입 여부 Filter Option<br>- 0: 사용안함(default)<br>- 1 : DC차데모<br>- 2 : AC완속<br>- 3 : DC콤보<br>- 4 : AC급속3상 |
| sortevcprice | String |  | 전기차 충전소 가격순 정렬 Option<br>- 0: 사용안함(default)<br>- 1: 가격순 정렬 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| provider | String | 검색결과 제공처<br>SIRE: 검색엔진<br>NAVER: 네이버 |
| type | Integer | 0 : 일반검색, 1 : Reference검색 |
| totalcount | Integer | 전체 검색결과 대상 개수 |
| count | Integer | 검색 결과 개수 |
| poitotalcount | Integer | Thinkware POI 전체 검색결과 대상 개수 |
| poicount | Integer | Thinkware POI 검색 결과 개수 |
| tel\_poitotalcount | Integer | Tel POI 전체 검색결과 대상 개수 |
| tel\_poicount | Integer | Tel POI 검색 결과 개수 |
| ucp\_poitotalcount | Integer | User POI 전체 검색결과 대상 개수 |
| ucp\_poicount | Integer | User POI 검색 결과 개수 |
| admtotalcount | Integer | adm 전체 검색결과 대상 개수 |
| admcount | Integer | adm 검색 결과 개수 |
| reftotalcount | Integer | ref 전체 검색결과 대상 개수 |
| refcount | Integer | ref 검색 결과 개수 |
| recommandQuery | String | 검색결과가 없는 경우 오타보정 결과 제공(NULL가능) |
| res\_type | String | 검색 결과 Type<br>명칭, 카테고리, 주소, 전화번호 순<br>(ex) NYNN: 명칭 No, 카테고리 YES, 주소 NO, 전화번호 NO |
| poi | Array | POI 검색결과 List [[inavi-air-api-data#POI_DATA_A\|POI_DATA_A]] |
| tel | Array | Tel POI 검색결과 List [[inavi-air-api-data#POI_DATA_A\|POI_DATA_A]] |
| ucp | Array | User POI 검색결과 List [[inavi-air-api-data#POI_DATA_A\|POI_DATA_A]] |
| npoi | Array | NAVER POI 검색결과 List(provider가 NAVER일 경우만 존재) |
| ┣ dpx | String | display X좌표(WGS84의 경우 longitude) |
| ┣ dpy | String | display Y좌표(WGS84의 경우 latitude) |
| ┣ routepoints | Array | 탐색용 좌표 리스트 |
| ┣ rpx | String | 탐색 X좌표(WGS84의 경우 longitude) |
| ┗ rpy | String | 탐색 Y좌표(WGS84의 경우 latitude) |
| ┣ rpx | String | 탐색 X좌표(WGS84의 경우 longitude) |
| ┣ rpy | String | 탐색 Y좌표(WGS84의 경우 latitude) |
| ┣ name1 | String | 정식명칭 |
| ┣ address | String | 주소 |
| ┣ roadname | String | 새주소 도로명 |
| ┣ distance | Integer | 좌표와의 거리 (해당시에만) |
| ┗ tel | String | 전화번호 |
| adm | Array | ADM 검색결과 List |
| ┣ type | String | 검색 type |
| ┣ posx | String | X좌표(WGS84의 경우 longitude) |
| ┣ posy | String | Y좌표(WGS84의 경우 latitude) |
| ┣ admcode | String | 행정코드 |
| ┣ address | String | 주소 |
| ┣ jibun | String | 지번 |
| ┣ roadname | String | 새주소 도로명 |
| ┣ roadjibun | String | 새주소 지번 |
| ┣ accuracy | Integer | 지번 정확도<br>0 : 정확 검색<br>1 : 호지번 확장<br>2 : 모지번 확장 |
| ┗ distance | Integer | 거리 |
| queryParse | Object | Reference 검색이면서 neighboropt=1인 경우 제공됨 |
| ┣ ref | Array | reference 정보 |
| ┣ type | Integer | Reference Type(0 : POI, 1 : 구주소, 2 : 새주소, 3 : 가로명, 4 : 행정계, 5 : 현위치) |
| ┣ id | Integer | Reference ID |
| ┣ name | String | Reference 명칭 |
| ┣ dpx | String | display X좌표(WGS84의 경우 longitude) |
| ┣ dpy | String | display Y좌표(WGS84의 경우 latitude) |
| ┣ rpx | String | 탐색 X좌표(WGS84의 경우 longitude) |
| ┣ rpy | String | 탐색 Y좌표(WGS84의 경우 latitude) |
| ┣ admcode | String | 행정코드 |
| ┣ catecode | String | 분류코드 |
| ┣ catename | String | 분류명칭 |
| ┣ address | String | 주소 |
| ┣ jibun | String | 지번 |
| ┣ roadname | String | 가로명 |
| ┣ roadjibun | String | 가로명 지번 |
| ┣ distance | Integer | 현재위치와의 거리 |
| ┗ count | Integer | 검색결과 개수 |
| ┗ srch | Object | 검색어 분석 정보 |
| ┣ keyword | String | 명칭 검색어 |
| ┣ catecode | String | Category 검색 분류코드 |
| ┣ catename | String | Category 명칭 |
| ┗ radius | Integer | 검색 반경 |
| hasgasstation | Boolean | oilprice 정보 제공 여부 |
| oilprice | Object | 유가 정보 |
| ┣ max\_g\_price | Integer | 최고 휘발유 가격 |
| ┣ min\_g\_price | Integer | 최저 휘발유 가격 |
| ┣ avg\_g\_price | Integer | 평균 휘발유 가격 |
| ┣ max\_hg\_price | Integer | 최고 고급 휘발유 가격 |
| ┣ min\_hg\_price | Integer | 최저 고급 휘발유 가격 |
| ┣ avg\_hg\_price | Integer | 평균 고급 휘발유 가격 |
| ┣ max\_d\_price | Integer | 최고 경유 가격 |
| ┣ min\_d\_price | Integer | 최저 경유 가격 |
| ┣ avg\_d\_price | Integer | 평균 경유 가격 |
| ┣ max\_l\_price | Integer | 최고 LPG 가격 |
| ┣ min\_l\_price | Integer | 최저 LPG 가격 |
| ┗ avg\_l\_price | Integer | 평균 LPG 가격 |

## 경로 주변 다중 카테고리 검색
> Confluence page id: 2262306439 · 최종 수정: 10월 01, 2026

### Function

> 경로 주변 다중 카테고리 검색

### URL

> `/sire/searchRouteAroundMulti`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| cutflag | String | O | 주소표현구분<br>0 : 정식행정계 주소<br>1 : 단축행정계 주소 |
| autoFlag | String |  | 자동검색/수동검색 여부<br>A : 자동<br>M : 수동<br>I : AI |
| coordtype | String | O | 좌표형식<br>0 : 정규화 좌표<br>1 : WGS 84<br>2 : TM |
| startposition | String | O | 시작위치<br>0 : 첫번째 위치<br>ex) 20 -\> 21번째 결과부터 reqcount 만큼 조회 |
| reqcount | String | O | 요청개수 |
| xpos | String | O | 시작점 X 좌표 |
| ypos | String | O | 시작점 Y 좌표 |
| category | Array | O | 카테고리 코드 리스트 |
| ┗ val | String | O | [[inavi-air-api-data#Category Code\|Category Code]] |
| rid | String | O | 경로 ID |
| sort | String | O | 정렬<br>0 : 거리순 (default)<br>1 : 휘발유<br>2 : 고급휘발유<br>3 : 경유<br>4 : LPG<br>5 : 명칭순<br>6 : PoiWeight<br>7 : 망고플레이트 평점 |
| direction | String | O | 경로방향<br>0:경로역방향<br>1:경로정방향<br>2:양방향 (default) |
| oil | String |  | 유종<br>0:ALL (default)<br>1:휘발유<br>2:고급휘발유<br>3:경유<br>4:LPG |
| distance | String |  | 경로와 경로의 직교상 POI간의 유효거리 제한값<br>0:default(서버내 정의값)<br>10000보다 크면 default 값으로 설정함 |
| evcstatus | String |  | 0 : 전기차 충전소 충전 가능 여부 Filter Option 사용안함(default)<br>1 : 사용중<br>2 : 사용 가능<br>3 : 사용 불가 |
| evctype | Array |  | 전기차 충전소 충전 타입 필터 리스트 |
| ┗ val | String |  | 0 : 전기차 충전소 충전 타입 여부 Filter Option 사용안함(default)<br>1 : DC차데모<br>2 : AC완속<br>3 : DC콤보<br>4 : AC급속3상 |
| sortevcprice | String |  | 0: 전기차 충전소 가격순 정렬 Option 사용안함(default)<br>1: 가격순 정렬 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| totalcount | Integer | POI 전체 검색결과 대상 개수 |
| count | Integer | POI 검색 결과 개수 |
| poi | Array | POI 검색결과 목록 |
| ┗ |  | [[inavi-air-api-data#경로 주변 POI 정보\|경로 주변 POI 정보]] |

[[inavi-air-api-data#경로 주변 POI 정보|경로 주변 POI 정보]]

## 대중교통 추천어 초성 검색
> Confluence page id: 2262306483 · 최종 수정: 10월 01, 2026

### Function

> 대중교통 추천어 초성 검색

### URL

> `/multiSearchProposer`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| query | String | O | 자동완성/초성문자 |
| coordX | String | O | 버스정류장 검색일경우<br>현위치 중심좌표 x(UTM-K) |
| coordY | String | O | 버스정류장 검색일경우<br>현위치 중심좌표 y(UTM-K) |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| sireResult | Object | sire 추천어 검색 결과(실패일경우 내려주지않음) |
| ┣ count | Integer | 추천 검색어 검색 결과 개수 |
| ┗ keyword | Array | 추천 검색어 결과 List |
| ┣ keyword | String | 검색어 |
| ┗ frequency | Integer | 조회 빈도 |
| seamlessResult | Object | seamless 추천어 검색 결과(실패일경우 내려주지않음) |
| ┣ busList | Array | 버스노선 결과 리스트 |
| ┣ accuracy | Integer | 검색 type |
| ┣ busLineId | String | 버스노선 ID(아로) |
| ┣ locgovLineId | String | 버스노선 ID(지자체) |
| ┣ busLineNo | String | 버스노선명 |
| ┣ busTypeCd | String | 버스 유형 |
| ┣ busCityNm | String | 버스노선 소재지역 |
| ┣ orgNm | String | 버스 기점명 |
| ┗ dstNm | String | 버스 종점명 |
| ┣ stationList | Array | 버스정류소 결과 리스트 |
| ┣ stnId | Integer | 버스 정류소 ID(아로) |
| ┣ stnNo | String | 버스 정류소 번호 |
| ┣ stnNm | String | 버스 정류소 명 |
| ┣ addr | String | 버스 정류소 주소 |
| ┣ x | Integer | X 좌표(UTM-K, 5179) |
| ┣ y | Integer | Y 좌표(UTM-K, 5179) |
| ┣ busNo | String | 정차버스 \\ (일반, 좌석, 마을, 직행좌석, 공항, 간선급행, 외곽, 간선, 지선, 순환, 광역, 급행, 농어촌, 급행간선) |
| ┗ dist | Integer | 거리(미터 단위) |
| ┣ subwayList | Array | 지하철 결과 리스트 |
| ┣ sbwyStnId | String | 지하철 ID |
| ┣ sbwyLineId | String | 지하철 노선종류<br>1(수도권1호선)<br>2(수도권2호선)<br>3(수도권3호선)<br>4(수도권4호선)<br>5(수도권5호선)<br>6(수도권6호선)<br>7(수도권7호선)<br>8(수도권8호선)<br>9(수도권9호선)<br>100(수도권분당선)<br>101(수도권공항철도)<br>103(수도권중앙선)<br>104(수도권경의선)<br>108(수도권경춘선)<br>109(수도권신분당선)<br>21(인천1호선)<br>31(대전1호선)<br>41(대구1호선)<br>42(대구2호선)<br>51(광주1호선)<br>71(부산1호선)<br>72(부산2호선)<br>73(부산3호선)<br>74(부산4호선)<br>79(김해경전철) |
| ┗ stnNm | String | 지하철역명 |
| ┗ totalList | Array | 버스+버스정류장 결과 리스트 |
| ┣ type | String | 버스:1, 버스정류장:2 |
| ┣ id | Integer | ID(아로ID) |
| ┣ name | String | 버스:버스번호<br>버스정류장:정류장명 |
| ┣ stnid | Integer | 버스:없음<br>버스정류장:정류장번호 |
| ┣ sidonm | String | 버스(정류장) 소재지역<br>서울:1<br>2:부산<br>3:대구<br>4:인천<br>5:광주<br>6:대전<br>7:울산<br>8:세종시<br>9:경기도<br>10:강원도<br>11:충청북도<br>12:충청남도<br>13:전라북도<br>14:전라남도<br>15:경상북도<br>16:경상남도<br>17:제주도 |
| ┣ sidocd | String | 버스(정류장) 소재코드<br>서울:1<br>2:부산<br>3:대구<br>4:인천<br>5:광주<br>6:대전<br>7:울산<br>8:세종시<br>9:경기도<br>10:강원도<br>11:충청북도<br>12:충청남도<br>13:전라북도<br>14:전라남도<br>15:경상북도<br>16:경상남도<br>17:제주도 |
| ┣ x | Integer | 버스 : 0(값없음)<br>정류장 : X 좌표(UTM-K, 5179) |
| ┗ y | Integer | 버스 : 0(값없음)<br>정류장 : Y 좌표(UTM-K, 5179) |

## 교통정보 요약맵 검색
> Confluence page id: 2262306503 · 최종 수정: 10월 01, 2026

### Function

> 교통정보 요약맵 검색

### URL

> `/sire/searchTism`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| code | String |  | 코드명<br>"depth1│depth2│depth3"<br>"고속도로│노선별고속도로│울산포항고속도로"<br>"수도권│고속도로│강남순환도시고속도로"<br>code가 NULL: depth1 리스트 제공<br>code가 2자리: code에 일치한 depth1 하위 리스트 제공<br>code가 4자리: code에 일치한 depth2 하위 리스트 제공<br>code가 7자리: code에 일치한 depth3 제공 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| total\_count | Integer | 요약맵 검색 결과 개수 |
| map\_list | Array | 요약맵 검색 결과 리스트 |
| ┣ name | String | 요약맵 명칭 |
| ┣ image\_id | String | 이미지 ID(3-depth에서만 제공 / 1,2-depth는 NULL 리턴) |
| ┣ depth | Integer | depth 분류 단계(1\~3) |
| ┣ code | String | code 명 |
| ┣ x1 | String | Extent X1(3-depth에서만 제공 / 1,2-depth는 NULL 리턴) |
| ┣ y1 | String | Extent Y1(3-depth에서만 제공 / 1,2-depth는 NULL 리턴) |
| ┣ x2 | String | Extent X2(3-depth에서만 제공 / 1,2-depth는 NULL 리턴) |
| ┣ y2 | String | Extent Y2(3-depth에서만 제공 / 1,2-depth는 NULL 리턴) |
| ┣ x3 | String | Extent X3(3-depth에서만 제공 / 1,2-depth는 NULL 리턴) |
| ┣ y3 | String | Extent Y3(3-depth에서만 제공 / 1,2-depth는 NULL 리턴) |
| ┣ x4 | String | Extent X4(3-depth에서만 제공 / 1,2-depth는 NULL 리턴) |
| ┣ y4 | String | Extent Y4(3-depth에서만 제공 / 1,2-depth는 NULL 리턴) |
| ┗ length | Integer | 도로 길이 |

## 구 주소 검색
> Confluence page id: 2262306523 · 최종 수정: 10월 01, 2026

### Function

> 구 주소 검색

### URL

> `/sire/searchOldAddr`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| cutflag | String | O | 주소표현구분<br>0 : 정식행정계 주소<br>1 : 단축행정계 주소 |
| coordtype | String | O | 좌표형식<br>0 : 정규화 좌표<br>1 : WGS 84<br>2 : TM |
| startposition | String | O | 시작위치<br>0 : 첫번째 위치<br>ex) 20 -\> 21번째 결과부터 reqcount 만큼 조회 |
| reqcount | String | O | 요청개수 |
| option | String | O | 검색 option<br>0 : admcode + jibun<br>1 : addr + jibun |
| addr | String |  | 행정명칭 (ex: 서울 서초구 양재동) |
| admcode | String |  | 행정계 코드 (ex: 1165010200) |
| jibun | String | O | 지번 (ex: 650) |
| mode | String | O | 검색 mode<br>1 : 법정동 우선 검색, 결과 없을 경우 행정동 검색<br>2 : 법정동 검색 (행정동 검색 안함)<br>3 : 법정동, 행정동 모두 검색 |
| xpos | String | O | 현재위치 x좌표 |
| ypos | String | O | 현재위치 y좌표 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| totalcount | Integer | 전체 검색결과 대상 개수 |
| count | Integer | 검색 결과 개수 |
| adm | Array | 주소검색결과 List |
| ┣ posx | String | 행정계 X좌표 (WGS84의 경우 longitude) |
| ┣ posy | String | 행정계 Y좌표 (WGS84의 경우 latitude) |
| ┣ jposx | String | 지번 X좌표 (WGS84의 경우 longitude) |
| ┣ jposy | String | 지번 Y좌표 (WGS84의 경우 latitude) |
| ┣ accuracy | Integer | 지번 정확도<br>0 : 정확 검색<br>1 : 호지번 확장<br>2 : 모지번 확장<br>3 : 행정계 |
| ┣ admtype | String | L : 법정동, A : 행정동 |
| ┣ admcode | String | 행정코드 |
| ┣ address | String | 주소 |
| ┣ jibun | String | 지번 |
| ┣ roadname | String | 새주소 도로명 |
| ┣ roadjibun | String | 새주소 지번 |
| ┗ distance | Integer | 거리 |

- 행정계 검색이 되었는데 좌표가 존재 하지 않는 경우 해당 행정계와 매칭되는 법정동의 좌표를 준다.

## 주변 POI 검색
> Confluence page id: 2262306543 · 최종 수정: 10월 01, 2026

### Function

> 주변 POI 검색

### URL

> `/sire/searchPoiAround`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| cutflag | String | O | 주소표현구분<br>0 : 정식행정계 주소<br>1 : 단축행정계 주소 |
| autoFlag | String |  | 자동검색/수동검색 여부<br>A : 자동<br>M : 수동<br>I: AI |
| coordtype | String | O | 좌표형식<br>0 : 정규화 좌표<br>1 : WGS 84<br>2 : TM |
| startposition | String | O | 시작위치<br>0 : 첫번째 위치<br>ex) 20 -\> 21번째 결과부터 reqcount 만큼 조회 |
| reqcount | String | O | 요청개수 |
| depth | String | O | 하위시설물 요구 depth<br>0 : depth 사용 안함(검색결과 모두 표출)<br>1 : 1 depth 만 요청(최상위 depth)<br>2 : 2 depth 까지 요청<br>3 : 3 depth 까지 요청 |
| catecode | String | O | [[inavi-air-api-data#Category Code\|Category Code]] |
| spopt | String | O | 공간검색 option<br>1 : Extent 검색<br>2 : Range 검색<br>3 : K-NN 검색 – 추후 지원 예정<br>4 : Grade 정렬<br>- 정렬 옵션이 유가(휘발유/고급휘발유/경유/LPG)인 경우 거리순 Grade부여.<br>정렬 옵션이 평점순 정렬(망고플레이트)인 경우 평점순 Grade부여.<br>이후 Grade내는 정렬옵션 순 재정렬. 단 Range검색입력 해야 함 |
| windowsize | String |  | Grade당 POI개수(Fetch Count의 N배)<br>- Grade정렬 옵션에서만 적용 됨.<br>N \>= 0인 자연수이며, 0 경우 1과 같이 동작. 파라메터 없는 경우 1로 동작<br>N \>= 1인 경우 Fetch \* N개수 단위로 grade내 Max POI지정 함. |
| x1 | String |  | X좌표<br>spopt가 1인 경우 Extent의 좌상단 X좌표<br>spopt가 2,3인 경우 기준점 X좌표 |
| y1 | String |  | Y좌표<br>spopt가 1인 경우 Extent의 좌상단 Y좌표<br>spopt가 2,3인 경우 기준점 Y좌표 |
| x2 | String |  | X좌표<br>spopt가 1인 경우 Extent의 우하단 X좌표<br>spopt가 2,3인 경우 사용 안함 |
| y2 | String |  | Y좌표<br>spopt가 1인 경우 Extent의 우하단 Y좌표<br>spopt가 2,3인 경우 사용 안함 |
| radius | String |  | 반경<br>spopt가 2인 경우 사용 (Meter 단위) |
| sortopt | String |  | 정렬 option<br>1 : 거리순 (Default)<br>2 : 명칭순<br>3 : 휘발유 가격순 (주유소 검색시)<br>4 : 고급휘발유 가격순 (주유소 검색시)<br>5 : 경유 가격순 (주유소 검색시)<br>6 : LPG 가격순 (주유소 검색시)<br>7 : 망고플레이트 평점순 |
| evcstatus | String |  | 0 : 전기차 충전소 충전 가능 여부 Filter Option 사용안함(default)<br>1 : 사용중<br>2 : 사용 가능<br>3 : 사용 불가 |
| evctype | Array |  | 전기차 충전소 충전 타입 필터 리스트 |
| ┗ val | String |  | 0 : 전기차 충전소 충전 타입 여부 Filter Option 사용안함(default)<br>1 : DC차데모<br>2 : AC완속<br>3 : DC콤보<br>4 : AC급속3상 |
| sortevcprice | String |  | 0: 전기차 충전소 가격순 정렬 Option 사용안함(default)<br>1: 가격순 정렬 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| totalcount | Integer | POI 전체 검색결과 대상 개수 |
| count | Integer | POI 검색 결과 개수 |
| poi | Array | POI 검색결과 List |
| ┣ poiid | Integer | poi id |
| ┣ depth | Integer | poi depth |
| ┣ dpx | String | display X좌표(WGS84의 경우 longitude) |
| ┣ dpy | String | display Y좌표(WGS84의 경우 latitude) |
| ┣ rpx | String | 탐색 X좌표(WGS84의 경우 longitude) |
| ┣ rpy | String | 탐색 Y좌표(WGS84의 경우 latitude) |
| ┣ name1 | String | 정식명칭 |
| ┣ name2 | String | 축약명칭 |
| ┣ name3 | String | 확장명칭1 |
| ┣ name4 | String | 확장명칭2 |
| ┣ admcode | String | 행정코드 |
| ┣ address | String | 주소 |
| ┣ jibun | String | 지번 |
| ┣ roadname | String | 새주소 도로명 |
| ┣ roadjibun | String | 새주소 지번 |
| ┣ detailaddress | String | 상세주소 |
| ┣ distance | Integer | 좌표와의 거리 (해당시에만) |
| ┣ catecode | String | 분류코드 |
| ┣ catename | String | 분류명칭 |
| ┣ tel | String | 전화번호 |
| ┣ istoll | Boolean | 유료 주차창 여부 (주차창일 경우만) |
| ┣ toll\_value | String | 유료 주차창 가격정보 (주차창일 경우만) |
| ┣ hasoildata | Boolean | 유가 데이터 존재여부 |
| ┣ hasdetailinfo | Boolean | 상세정보 존재여부 |
| ┣ hassubpoi | Boolean | 하위시설물 존재여부 |
| ┣ islandmark | Boolean | 랜드마크 여부 |
| ┣ visitscore | String | POI Weight |
| ┣ updateTS | String | 최종변경 일시 (Y4-MM-DD HH:mm:ss) |
| ┣ data\_source | String | poi 생성 정보 구분 (Thinkware/Tel/User) |
| ┣ badgeflag | Boolean | Badge 유무 |
| ┣ userid | String | poi 등록 사용자 ID (UCP인 경우에만) |
| ┣ imagecount | Integer | poi 이미지 개수 |
| ┣ oildata | Object | 유가 데이터 정보 |
| ┣ g\_price | Integer | 휘발유 가격 |
| ┣ hg\_price | Integer | 고급휘발유 가격 |
| ┣ d\_price | Integer | 경유 가격 |
| ┣ l\_price | Integer | LPG 가격 |
| ┣ updatetime | String | Update 시간 |
| ┣ priceinfo | String | 최고, 최저 유가 정보(H:최고, L:최저, X:해당없음)<br>휘발유, 고급휘발유, 경유, LPG 순 |
| ┣ wash | Boolean | 세차시설여부 |
| ┣ fix | Boolean | 정비가능여부 |
| ┗ mart | Boolean | 매점여부 |
| ┣ subpoi | Object | 하위 시설물 정보 |
| ┣ count | Integer | subpoi 개수 |
| ┗ poi | Array | poi 정보와 동일 |
| ┣ adv\_count | Integer | 광고코드 개수 |
| ┣ AdInfo | Array | 광고제공업체 광고 코드 |
| ┗ ADCODE | Integer | 광고코드 1\~99까지 부여가능(최대99개) |
| ┣ externallink | Array | 외부연동 ID |
| ┣ ID | String | 연동 ID(PLOG일 경우 URL끝에 &app=ktnavi 붙여서 호출) |
| ┣ Site | String | 연동 Site(망고플레이트/PLOG) |
| ┣ ExtraInfo1 | String | 추가정보1(if exist) |
| ┗ ExtraInfo2 | String | 추가정보2(if exist) |
| ┗ evcstation | Object | [[inavi-air-api-data#전기차 충전소 정보\|전기차 충전소 정보]] |

## 새 주소 검색
> Confluence page id: 2262306567 · 최종 수정: 10월 01, 2026

### Function

> 새 주소 검색

### URL

> 원본에 URL 값이 비어 있음

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| cutflag | String | O | 주소표현구분<br>0 : 정식행정계 주소<br>1 : 단축행정계 주소 |
| coordtype | String | O | 좌표형식<br>0 : 정규화 좌표<br>1 : WGS 84<br>2 : TM |
| startposition | String | O | 시작위치<br>0 : 첫번째 위치<br>ex) 20 -\> 21번째 결과부터 reqcount 만큼 조회 |
| reqcount | String | O | 요청개수 |
| option | String | O | 검색 option<br>1 : admcode + addr (ex: 26 + 진달래길(도로명 입력))<br>2 : 새주소 명칭 (ex: 부산 진달래길) |
| addr | String | △ | 새 주소명(ex: 부산 진달래길 or 진달래길) |
| admcode | String | △ | 행정계 코드(ex: 26) |
| jibun | String | △ | 지번 (건물번호)<br>ex) 3 (지번 검색하고 싶으면 입력, 없으면 주소검색만) |
| xpos | String | O | 현재위치 x좌표 |
| ypos | String | O | 현재위치 y좌표 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| totalcount | Integer | 전체 검색결과 대상 개수 |
| count | Integer | 검색 결과 개수 |
| adm | Array | 주소검색결과 List |
| ┣ posx | String | 행정계 X좌표 (WGS84의 경우 longitude) |
| ┣ posy | String | 행정계 Y좌표 (WGS84의 경우 latitude) |
| ┣ accuracy | Integer | 지번 정확도<br>0 : 정확 검색<br>1 : 호지번 확장<br>2 : 모지번 확장<br>3 : 행정계 |
| ┣ admcode | String | 행정코드 |
| ┣ address | String | 주소 |
| ┣ jibun | String | 지번 |
| ┣ roadname | String | 새주소 도로명 |
| ┣ roadjibun | String | 새주소 지번 |
| ┗ distance | Integer | 거리 |

## 좌표로 주소 검색
> Confluence page id: 2262306587 · 최종 수정: 10월 01, 2026

### Function

> 좌표로 주소 검색

### URL

> `/sire/revgeocoding`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| cutflag | String | O | 주소표현구분<br>0 : 정식행정계 주소<br>1 : 단축행정계 주소 |
| coordtype | String | O | 좌표형식 0 : 정규화 좌표 |
| startposition | String | O | 시작위치<br>0 : 첫번째 위치<br>ex) 20 -\> 21번째 결과부터 reqcount 만큼 조회 |
| reqcount | String | O | 요청개수 |
| posx | String | O | X좌표 |
| posy | String | O | Y좌표 |
| w3wYn | String |  | W3W 연동 여부 (Default : N) Y : 연동 N : 미 연동 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| admcode | String | 행정코드 |
| x | String | X좌표 (WGS84의 경우 longitude) |
| y | String | Y좌표 (WGS84의 경우 latitude) |
| address | String | 주소 |
| cut\_address | String | 축약 주소 |
| road\_address | String | 도로명 주소 |
| cut\_road\_address | String | 축약 도로명 주소 |
| jibun | String | 지번 |
| bldnum | String | 빌딩번호 |
| address\_type | String | 주소 매핑 타입<br>0 : 행정계<br>1 : 새주소 폴리곤<br>2 : 지적도 폴리곤<br>3 : 인접지번<br>4 : 행정계 |
| w3wWords | String | w3w 단어 (미존재 케이스의 경우 “”) |

## 최적 지적 검색
> Confluence page id: 2262306607 · 최종 수정: 10월 01, 2026

### Function

> 최적 지적 검색

### URL

> `/sire/optimalPosition`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| posx | String | O | 정규화 X좌표 |
| posy | String | O | 정규화 Y좌표 |
| type | Integer | O | 최적 지점 속성<br>• Default : 0<br>• 0 : 전체<br>• 1 : 차량 입구점<br>• 2 : 택시 승하차 지점(건물)<br>• 3 : 택시 승하차 지점(단지)<br>• 4 : 택배 차량 하차 거점<br>• 5 : 보행자 입구점<br>• 6 : 배달 하차점(차량, 오토바이)<br>• 7 : 배달 하차점(자전거, 도보) |
| count | Integer | O | 최대 결과 목록 수 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]]<br>0 : 성공<br>903 : 조회 결과 없음<br>999 : 정의되지 않은 오류 |
| result\_msg | String | 결과코드에 따른 메세지 |
| entrypoints | Array | 최적 지점 좌표 정보 |
| ┣ x | String | 정규화 X좌표 |
| ┣ y | String | 정규화 Y좌표 |
| ┗ type | Integer | EP 좌표 타입<br>• Default : 0<br>• 0 : 미지정<br>• 1 : 차량 입구점<br>• 2 : 택시 승하차 지점(건물)<br>• 3 : 택시 승하차 지점(단지)<br>• 4 : 택배 차량 하차 거점<br>• 5 : 보행자 입구점<br>• 6 : 배달 하차점(차량, 오토바이)<br>• 7 : 배달 하차점(자전거, 도보) |

## 추천어 검색
> Confluence page id: 2262306627 · 최종 수정: 10월 01, 2026

### Function

> 추천어 검색

### URL

> `/sire/searchProposer`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| query | String | O | 검색어<br>한글/영문/숫자 50Byte(한글 25자) |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| count | Integer | 추천 검색어 검색 결과 개수 |
| keyword | Array | 추천 검색어 결과 List |
| ┣ keyword | String | 검색어 |
| ┗ frequency | Integer | 조회 빈도 |

## 하위 행정계 도로명 검색
> Confluence page id: 2262306647 · 최종 수정: 10월 01, 2026

### Function

> 하위 행정계 도로명 검색

### URL

> `/sire/searchSubAddrRoadName`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| cutflag | String | O | 주소표현구분<br>0 : 정식행정계 주소<br>1 : 단축행정계 주소 |
| coordtype | String | O | 좌표형식<br>0 : 정규화 좌표<br>1 : WGS 84<br>2 : TM |
| startposition | String | O | 시작위치<br>0 : 첫번째 위치<br>ex) 20 -\> 21번째 결과부터 reqcount 만큼 조회 |
| reqcount | String | O | 요청개수 |
| admcode | String | O | 행정코드<br>ex) 11650 (구코드 5자리 입력) 세종시는 구가 없음으로 36두자리로 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| totalcount | Integer | 전체 검색결과 대상 개수 |
| count | Integer | 검색 결과 개수 |
| road | Array | Road검색결과 List |
| ┣ cid | Integer | 도로명코드 |
| ┗ roadname | String | 새주소 도로명 |

## 하위 행정계 검색
> Confluence page id: 2262306667 · 최종 수정: 10월 01, 2026

### Function

> 하위 행정계 검색

### URL

> `/sire/searchSubAddr`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| cutflag | String | O | 주소표현구분<br>0 : 정식행정계 주소<br>1 : 단축행정계 주소 |
| coordtype | String | O | 좌표형식<br>0 : 정규화 좌표<br>1 : WGS 84<br>2 : TM |
| option | String | O | 검색 option<br>1 : 행정 코드로 검색<br>2 : 주소로 검색<br>3 : 행정코드 -\> 주소변환 |
| startposition | String | O | 무조건 0입력 |
| reqcount | String | O | 무조건 0입력 |
| addr | String | △ | 주소명칭 (option 값이 2인경우) |
| admcode | String | △ | 행정계 코드 (option 값이 1, 3인경우) |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| totalcount | Integer | 전체 검색결과 대상 개수 |
| count | Integer | 검색 결과 개수 |
| adm | Array | 주소검색결과 List |
| ┣ posx | String | X좌표 (WGS84의 경우 longitude) |
| ┣ posy | String | Y좌표 (WGS84의 경우 latitude) |
| ┣ admname | String | 행정명 |
| ┣ admcode | String | 행정코드 |
| ┣ address | String | 주소 |
| ┗ hassub | Boolean | 하위 행정계 존재여부 |

- query에 "" 혹은 0을 입력하면 광역시도의 정보 조회
- 결과로 리턴+된 admcode를 사용하여 하위행정계 조회하여야 함
- admcode : 광역시도 (2자리) 시,군,구(5자리), 읍면동(8자리) 리(10자리)

## Sources
- Confluence "INAVI AIR API" > 검색 (2026-10-27 조회): 검색 (2) (2262306111), CCTV 검색 (2) (2262306163), CCTV용 고속도로 검색 (2) (2262306183), Reference 주변 검색 (2) (2262306203), POI 상세정보 조회 (2) (2262306225), POI 하위시설물 조회 (2) (2262306247), count (2262306297), poi (2262306313), result_code (2262306329), result_msg (2262306345), totalcount (2262306361), POI 명칭 검색 (2) (2262306377), SQE 통합검색 (2) (2262306417), 경로 주변 다중 카테고리 검색 (2) (2262306439), 대중교통 추천어 초성 검색 (2262306483), 교통정보 요약맵 검색 (2262306503), 구 주소 검색 (2) (2262306523), 주변 POI 검색 (2) (2262306543), 새 주소 검색 (2262306567), 좌표로 주소 검색 (2) (2262306587), 최적 지적 검색 (2) (2262306607), 추천어 검색 (2) (2262306627), 하위 행정계 도로명 검색 (2) (2262306647), 하위 행정계 검색 (2) (2262306667)
