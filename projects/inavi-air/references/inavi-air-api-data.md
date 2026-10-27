---
title: "INAVI AIR API — DATA (AIR)"
category: references
tags: [inavi-air, api, poi, data-object, visibility/internal]
aliases: [DATA (AIR), AIR API 데이터 객체]
relationships:
  - target: "[[inavi-air-api-detail-spec]]"
    type: derived_from
sources: ["url:https://inavisystems.atlassian.net/wiki/spaces/AS/pages/2273214571"]
summary: >-
    AIR API 공용 데이터 정의(Category Code, 방향코드, POI_DATA_A/B, 경로 주변 POI 정보, 전기차 충전소 정보)를 Confluence에서 그대로 옮긴 페이지.
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

# INAVI AIR API — DATA (AIR)

Confluence "INAVI AIR API" > "DATA (AIR)" 페이지들을 요약 없이 그대로 옮긴 것이다. 허브는 [[inavi-air-api-detail-spec]], 제품 개요는 [[inavi-air]]를 본다. 공통 규격은 [[inavi-air-api-common]]에 있다.

## 목차

| 페이지 | page id | 분류 |
| --- | --- | --- |
| [[#DATA (AIR)\|DATA (AIR)]] | 2273214571 | 카테고리 부모 페이지 |
| [[#Category Code]] | 2262305670 | Enum / Code |
| [[#방향코드]] | 2262308039 | Enum / Code |
| [[#POI_DATA_A]] | 2262306399 | Object |
| [[#POI_DATA_B]] | 2262306279 | Object |
| [[#경로 주변 POI 정보]] | 2262306463 | Object |
| [[#전기차 충전소 정보]] | 2262308917 | Object |

## DATA (AIR)
> Confluence page id: 2273214571 · 최종 수정: 10월 06, 2026

### Enum / Code

- [[#Category Code|Category Code]]
- [[#방향코드|방향코드]]

### Object

- [[#POI_DATA_A|POI\_DATA\_A]]
- [[#POI_DATA_B|POI\_DATA\_B]]
- [[#경로 주변 POI 정보|경로 주변 POI 정보]]
- [[#전기차 충전소 정보|전기차 충전소 정보]]

## Category Code
> Confluence page id: 2262305670 · 최종 수정: 10월 06, 2026

#### Category Code

| Catgory code | description |
| --- | --- |
| C0100 | 주유소 |
| C0101 | SK |
| C0102 | S-Oil |
| C0103 | 현대 |
| C0104 | GS |
| C0105 | 농협 |
| C0200 | LPG충전소 |
| C0201 | SK |
| C0202 | S-OIL |
| C0203 | 현대 |
| C0204 | GS |
| C0205 | E1 |
| C0300 | 주차장 |
| C0301 | 유료 |
| C0302 | 무료 |
| C0303 | 무료(시간제) |
| C0400 | 정비소 |
| C0500 | 세차장 |
| C0600 | 아이나비AS |
| C0700 | 관공서 |
| C0800 | 은행 |
| C0899 | 은행.ATM |
| C0900 | 병원 |
| C1000 | 약국 |
| C1100 | 음식점 |
| C1200 | 숙박 |
| C1300 | 휴게소 |
| C1400 | 찜질방 |
| C1500 | 화장실 |
| C1600 | 지하철 |
| C1700 | 할인마트 |
| C1800 | 24시편의점 |
| C1900 | 패밀리레스토랑 |
| C2000 | 패스트푸드 |
| C2100 | 문화예술 |
| C2200 | 현금인출기 |
| C2800 | 병원 |
| C3000 | CCTV |
| C3001 | VMS |
| C4000 | 망고플레이트 |

## POI_DATA_A
> Confluence page id: 2262306399 · 최종 수정: 10월 06, 2026

#### POI\_DATA\_A

| parameter | type | description |
| --- | --- | --- |
| ┣ poiid | Integer | poi id |
| ┣ depth | Integer | poi depth |
| ┣ dpx | Integer | display X좌표(WGS84의 경우 longitude) |
| ┣ dpy | String | display Y좌표(WGS84의 경우 latitude) |
| ┣ routepoints | Array | 탐색용 좌표 리스트 |
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
| ┣ distance | Integer | 좌표와의 거리 (해당시에만) |
| ┣ catecode | String | 분류코드 |
| ┣ catename | String | 분류명칭 |
| ┣ dp\_catecode | String | DP 분류코드 |
| ┣ tel | String | 전화번호 |
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
| ┣ ID | String | 연동 ID |
| ┣ Site | String | 연동 Site |
| ┣ ExtraInfo1 | String | 추가정보1(if exist) |
| ┗ ExtraInfo2 | String | 추가정보2(if exist) |
| ┣ evcstation | Object | [[#전기차 충전소 정보\|📙전기차 충전소 정보]] |

## POI_DATA_B
> Confluence page id: 2262306279 · 최종 수정: 10월 06, 2026

#### POI\_DATA\_B

| parameter | type | description |
| --- | --- | --- |
| poi | Array | POI 검색결과 List |
| ┣ poiid | Integer | poi id |
| ┣ depth | Integer | poi depth |
| ┣ dpx | Integer | display X좌표(WGS84의 경우 longitude) |
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
| ┣ adv\_count | Integer | 광고코드 개수 |
| ┗ AdInfo | Array | 광고제공업체 광고 코드 |
| ┗ ADCODE | Integer | 광고코드 1\~99까지 부여가능(최대99개) |
| ┣ evcstation | Object | [[#전기차 충전소 정보\|📙전기차 충전소 정보]] |

## 경로 주변 POI 정보
> Confluence page id: 2262306463 · 최종 수정: 10월 06, 2026

#### 경로 주변 POI 정보

| parameter | type | description |
| --- | --- | --- |
| ┣ pointtype | Integer | 포인트 타입<br>0 : YR<br>1 : Real Time Road Info Point |
| ┣ poiid | Integer | poi id (pointtype 0일때만 제공) |
| ┣ depth | Integer | poi depth (pointtype 0일때만 제공) |
| ┣ dpx | String | display X좌표(WGS84의 경우 longitude) (pointtype 0일때만 제공) |
| ┣ dpy | String | display Y좌표(WGS84의 경우 latitude) (pointtype 0일때만 제공) |
| ┣ rpx | String | 탐색 X좌표(WGS84의 경우 longitude) (pointtype 0일때만 제공) |
| ┣ rpy | String | 탐색 Y좌표(WGS84의 경우 latitude) (pointtype 0일때만 제공) |
| ┣ name1 | String | 정식명칭 (pointtype 0일때만 제공) |
| ┣ name2 | String | 축약명칭 (pointtype 0일때만 제공) |
| ┣ name3 | String | 확장명칭1 (pointtype 0일때만 제공) |
| ┣ name4 | String | 확장명칭2 (pointtype 0일때만 제공) |
| ┣ admcode | String | 행정코드 (pointtype 0일때만 제공) |
| ┣ address | String | 주소 (pointtype 0일때만 제공) |
| ┣ jibun | String | 지번 (pointtype 0일때만 제공) |
| ┣ roadname | String | 새주소 도로명 (pointtype 0일때만 제공) |
| ┣ roadjibun | String | 새주소 지번 (pointtype 0일때만 제공) |
| ┣ detailaddress | String | 상세주소 (pointtype 0일때만 제공) |
| ┣ catecode | String | 분류코드 |
| ┣ catename | String | 분류명칭 (pointtype 0일때만 제공) |
| ┣ category | String | [[#Category Code\|Category Code]] |
| ┣ distance | Integer | 좌표와의 거리 (해당시에만) |
| ┣ direction | Integer | 0: 경로역방향<br>1: 경로 진행방향 |
| ┣ tel | String | 전화번호 (pointtype 0일때만 제공) |
| ┣ mapid | String | MAP ID |
| ┣ linkid | String | LINK ID |
| ┣ hasdetailinfo | Boolean | 상세정보 존재여부 (pointtype 0일때만 제공) |
| ┣ hassubpoi | Boolean | 하위시설물 존재여부 (pointtype 0일때만 제공) |
| ┣ roadtype | Integer | POI와 매칭된 경로상 link 도로 종별 속성<br>1 : 고속도로<br>2 : 도시고속<br>3 : 국도<br>4 : 지방도<br>5 : 일반도로<br>6 : 자동차 전용도로<br>7 : 탐색불가도로<br>0 : 기타 및 미분류 |
| ┣ id | String | 도로정보 id (pointtype 1일때만 제공) |
| ┣ tpeglinkid | String | tpeg link id (pointtype 1일때만 제공) |
| ┣ type | Integer | Road Info Type (pointtype 1일때만 제공)<br>0 : VVMS<br>1 : 유고 |
| ┣ hasoildata | Boolean | 유가 데이터 존재여부 (pointtype 0일때만 제공) |
| ┣ oildata | Object | 유가 데이터 정보 (pointtype 0일때만 제공) |
| ┣ g\_price | Integer | 휘발유 가격 |
| ┣ g\_least | Integer | 최저 휘발유 가격제공 Flag(0: 아님 1: 맞음) |
| ┣ hg\_price | Integer | 고급휘발유 가격 |
| ┣ hg\_least | Integer | 최저 고급휘발유 가격제공 Flag(0: 아님 1: 맞음) |
| ┣ d\_price | Integer | 경유 가격 |
| ┣ d\_least | Integer | 최저 경유 가격제공 Flag(0: 아님 1: 맞음) |
| ┣ l\_price | Integer | LPG 가격 |
| ┣ l\_least | Integer | 최저 LPG 가격제공 Flag(0: 아님 1: 맞음) |
| ┗ updatetime | String | Update 시간 |
| ┣ hascctvdata | Boolean | CCTV 존재여부 (pointtype 0일때만 제공) |
| ┣ cctvdata | Object | CCTV 정보 (pointtype 0일때만 제공) |
| ┣ cctv\_id | String | CCTV ID |
| ┣ cctv\_name | String | CCTV 명칭 |
| ┣ nosun | String | 도로명 |
| ┣ offer | String | CCTV 데이터 제공처 |
| ┣ thumbnail\_url | String | 썸네일 이미지 URL |
| ┣ stream\_url | String | CCTV Stream URL |
| ┣ time | String | 업데이트 시간 (YYYYMMDDHHMISS) |
| ┗ externallink | Array | 외부연동 ID (pointtype 0일때만 제공) |
| ┣ ID | String | 연동 ID(PLOG일 경우 URL끝에 &app=ktnavi 붙여서 호출) |
| ┣ Site | String | 연동 Site(망고플레이트/PLOG) |
| ┣ ExtraInfo1 | String | 추가정보1(if exist) |
| ┗ ExtraInfo2 | String | 추가정보2(if exist) |
| ┣ evcstation | Object | [[#전기차 충전소 정보\|전기차충전소정보]] |

> 원본 표의 `category`, `evcstation` 링크는 사내 구 위키(내부 서버 주소)를 가리켜 이 페이지의 해당 섹션 링크로 바꿨다.

## 방향코드
> Confluence page id: 2262308039 · 최종 수정: 10월 06, 2026

### Definition

> 대구 신호등 방향 코드를 정의 합니다.

| 방향 | 코드 |
| --- | --- |
| 북 | 10 |
| 동 | 20 |
| 남 | 30 |
| 서 | 40 |
| 북동 | 50 |
| 남동 | 60 |
| 남서 | 70 |
| 북서 | 80 |

## 전기차 충전소 정보
> Confluence page id: 2262308917 · 최종 수정: 10월 06, 2026

#### 전기차 충전소 정보

| parameter | type | description |
| --- | --- | --- |
| agency | String | 충전소기관<br>DE:대구환경공단<br>KN:부산울산경남지역본부<br>GN:지엔텔<br>KT:케이티<br>EV:에버온<br>ST:에스트래픽<br>BG:비긴스<br>JE:제주전기자동차서비스<br>KP:한국전력<br>HE:한국전기차충전서비스<br>PI:포스코ICT<br>SE:서울시<br>PW:파워큐브<br>CT:씨티카<br>ME:환경부<br>CV:대영채비<br>JD:제주도청<br>TM:티맵 |
| station\_id | String | 충전소고유ID |
| fee | String | 충전가격(Kwh) |
| free\_parking | String | 주차비유료여부 |
| operating\_hour | String | 운영시간 |
| opagency | String | 운영기관 |
| opagency\_contact | String | 운영기관연락처 |
| reservation | String | 예약여부 |
| membership | String | 멤버쉽여부 |
| serviceable | String | 사용가능여부 |
| update\_timestamp | String | 업데이트시각 |
| charger\_count | Integer | 전기차 충전기 개수 |
| evcharger | Array | 충전기정보 |
| ┣ chargerid | String | 충전기ID |
| ┣ agency\_mangeid | String | 기관관리 ID |
| ┣ type\_1 | String | 충전기타입\_1<br>01:DC차데모<br>02:AC완속<br>03:DC차데모+AC3상<br>04:DC콤보<br>05:DC차데모+DC콤보<br>06:DC차데모+AC3상+DC콤보<br>07:AC급속3상 |
| ┣ type\_2 | String | 충전기타입\_2(상세타입)<br>ex) a,b<br>a:DC차데모<br>b:AC완속<br>c:DC콤보<br>d:AC급속3상 |
| ┣ status | String | 충전기상태<br>0:알수없음<br>1:통신이상<br>2:충전대기<br>3:충전중<br>4:운영중지<br>5:점검중<br>6:예약중<br>7:표시안함 |
| ┣ fee\_type | String | 충전 유료여부 |
| ┣ cable\_type | String | 케이블여부 |
| ┣ display\_type | String | 표시여부 |
| ┣ update\_timestamp | String | 업데이트 시각 |
| ┣ manufacture | String | 충전기제조사<br>J:일진전기<br>Y:중앙제어<br>C:시그넷<br>H:효성<br>I:LS산전<br>L:LS전선<br>N:LGCNS<br>P:PNE<br>K:코디에스<br>KE:KLINELEX<br>E:이엔테크놀로지<br>D:광명DNC<br>B:보타리에너지<br>PC:피앤씨주식회사<br>AF:주식회사AFT<br>EP:이카플러그<br>JW:제원쏠라<br>DK:대경엔지니어링<br>RV:한국알박<br>PQ:파워큐브<br>DY:대영채비<br>MT:모던텍 |
| type\_1\_info | Array | 충전기 타입\_1 별 정보 |
| ┣ name | String | 충전기 타입 이름<br>01:DC차데모<br>02:AC완속<br>03:DC차데모+AC3상<br>04:DC콤보<br>05:DC차데모+DC콤보<br>06:DC차데모+AC3상+DC콤보<br>07:AC급속3상 |
| ┣ charger\_count | Integer | 전기차 충전기 해당 타입 수량 |
| ┣ charger\_ok\_count | Integer | 충전 가능 수량 |
| type\_2\_info | Array | 충전기 타입\_2(상세타입) 별 정보 |
| ┣ name | String | 충전기 타입 이름<br>a:DC차데모<br>b:AC완속<br>c:DC콤보<br>d:AC급속3상 |
| ┣ charger\_count | Integer | 전기차 충전기 해당 타입 수량 |
| ┣ charger\_ok\_count | Integer | 충전 가능 수량 |
| summary | Object | 전기차 충전소 요약 정보 |
| ┣ charge | Boolean | 충전소 충전 가능 여부.<br>true : 가능<br>false : 불가능 |
| ┣ feetext | String | 충전기 가격 정보.<br>무료<br>유료 |
| ┣ simple | Array | 충전소 충전기 요약 정보. |
| ┣ name | String | 충전소 보유 충전기 이름.<br>(type2 기준 해당 순으로 정렬)<br>a:DC차데모<br>d:AC3상<br>c:DC콤보<br>b:완속 |
| ┗ charge | Boolean | 충전기 충전 가능 여부.<br>true : 가능<br>false : 불가능 |
| ┗ detail | Array | 충전소 충전기 세부 정보. |
| ┣ name | String | 충전소 보유 충전기 이름.<br>(type1 기준 해당 순으로 정렬)<br>06:DC차데모 AC3상 DC콤보<br>03:DC차데모 AC3상<br>05:DC차데모 DC콤보<br>01:DC차데모<br>07:AC3상<br>04:DC콤보<br>02:완속 |
| ┣ charger\_ok\_count | Integer | 충전기 충전 가능 상태 개수 |
| ┗ charger\_total\_count | Integer | 충전기 전체 개수 |

## Sources
- Confluence "INAVI AIR API" > DATA (AIR) (2026-10-27 조회): DATA (AIR) (2273214571), Category Code (2262305670), POI_DATA_A (2262306399), POI_DATA_B (2262306279), 경로 주변 POI 정보 (2262306463), 방향코드 (2262308039), 전기차 충전소 정보 (2262308917)
