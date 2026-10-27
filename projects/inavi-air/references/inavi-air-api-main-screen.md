---
title: "INAVI AIR API — 메인화면-AIR"
category: references
tags: [inavi-air, api, main-screen, weather, visibility/internal]
aliases: [메인화면-AIR]
relationships:
  - target: "[[inavi-air-api-detail-spec]]"
    type: derived_from
sources: ["url:https://inavisystems.atlassian.net/wiki/spaces/AS/pages/2262307665"]
summary: >-
    INAVI AIR 메인화면 API 명세 원문 전사. 통합메인화면(/mainPageData) 응답 전 항목, 날씨정보, 오늘의운세 날짜유효성체크를 담는다.
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

# INAVI AIR API — 메인화면-AIR

Confluence "메인화면-AIR" 페이지들을 요약 없이 그대로 옮긴 원문 전사본이다. 허브는 [[inavi-air-api-detail-spec]], 공통 헤더·결과 코드는 [[inavi-air-api-common]], 서비스 개요는 [[inavi-air]]를 본다.

| API | URL |
| --- | --- |
| [[#날씨정보]] | `/weather` |
| [[#통합메인화면]] | `/mainPageData` |
| [[#오늘의운세 날짜유효성체크]] | `/fortuneBirthCheck` |

## 개요
> Confluence page id: 2262307665 · 최종 수정: 10월 06, 2026

상위 페이지 "메인화면-AIR" 본문은 하위 API 링크 목록이다(원본 순서 그대로).

- 🧭날씨정보
- 🧭통합메인화면
- 🧭오늘의운세 날짜유효성체크

## 날씨정보
> Confluence page id: 2262307707 · 최종 수정: 10월 01, 2026

### Function

> 날씨정보

### URL

> `/weather`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| coordinations | Array |  | 날씨 정보를 받고싶은 위치의 좌표 |
| ┣ x | String | O | 날씨정보를 받고싶은 위치의 x좌표, wgs84 X값 |
| ┗ y | String | O | 날씨정보를 받고싶은 위치의 y좌표, wgs84 Y값 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| weatherList | Array | 날씨정보 |
| ┣x | String | 요청된 wgs84 X값 |
| ┣y | String | 요청된 wgs84 Y값 |
| ┣obs\_time | String | 관측시간 |
| ┣wind\_dir | String | 풍향 (한글표기 16방향) |
| ┣wind\_speed | String | 풍속 (m/s) |
| ┣temperature | String | 현재기온 |
| ┣rel\_humidity | String | 상대습도 |
| ┣ wti\_code | String | 날씨 매칭 코드해당 정보로 아이콘 표출1 맑음 2 구름 많음 3 흐림 4 비5 눈 6 눈비 7 소나기 10 뇌우13 흐리고 비 14 흐리고 눈15 흐리고 눈비 22 미세먼지 |
| ┣wx | String | 현재날씨 |
| ┗precipitation | String | 강수량 |

## 통합메인화면
> Confluence page id: 2262307727 · 최종 수정: 10월 01, 2026

### Function

> 통합메인화면

### URL

> `/mainPageData`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| currentLocX | String | O | 정규화 X값 |
| currentLocY | String | O | 정규화 Y값 |
| oilCateCode | String | O | 사용자의 선호 주유소 catecode(Default:C0100)[[inavi-air-api-data#Category Code\|Category Code]] |
| oilSortopt | String | O | 정렬 옵션1 : 거리순2 : 명칭순3 : 휘발유 가격순(주유소 검색시)4 : 고급휘발유 가격순(주유소 검색시)5 : 경유 가격순(주유소 검색시)6 : LPG 가격순(주유소 검색시)7 : 평점 순 정렬(2016.11월 기준 망고플레이트 데이터에 한함)Default : 3 |
| requestType | Array | O | 요청할 정보들 InterestingPlaceWeather MyAirMileage TodayAccumulateMileage NearHotPlace NearHotPlaces NearLowestOil NearLowestOils MyDrivingScore LastDrivingRecord AirMileU lbsLuckyBox ~~todaysFortune~~ AirCash |
| isWiget | boolean | O | 현재 IOS만 필수값위젯여부 |
| weatherCoordinations | Array |  | 날씨정보 요청할때 추가로 더 보고싶은곳(ex:도착지) 에대한 좌표 |
| ┣ x | String |  | 정규화 X값 |
| ┗ y | String |  | 정규화 Y값 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| nearHotPlaceInfo | Object | 주변 인기장소 (요청되지 않았으면 내려가지 않음) 랜덤하게 내려감 |
| ┣ result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| ┣ result\_msg | String | 결과코드에 따른 메세지 |
| ┣ poi | Object | [[inavi-air-api-data#POI_DATA_A\|POI_DATA_A]] |
| nearHotPlacesInfo | Object | 주변 인기장소'들' (요청되지 않았으면 내려가지 않음) |
| ┣ result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| ┣ result\_msg | String | 결과코드에 따른 메세지 |
| ┣ poi | Array | [[inavi-air-api-data#POI_DATA_A\|POI_DATA_A]] |
| weatherInfoList | Array | 날씨정보 (요청되지 않았으면 내려가지 않음) |
| ┣ result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| ┣ result\_msg | String | 결과코드에 따른 메세지 |
| ┣ x | String | 요청된 정규화 X값 |
| ┣ y | String | 요청된 정규화 Y값 |
| ┣ obs\_time | String | 관측시간 |
| ┣ obs\_timestamp | Long | 관측시간 timestamp |
| ┣ wind\_dir | String | 풍향 (한글표기 16방향) |
| ┣ wind\_speed | String | 풍속 (m/s) |
| ┣ temperature | String | 현재기온 |
| ┣ rel\_humidity | String | 상대습도 |
| ┣ wti\_code | String | 날씨 매칭코드해당정보로 아이콘 표출하면 됨1 맑음 2 구름조금3 흐림 4 비5 눈 6 눈비7 소나기 8 소낙눈9 안개 10 뇌우11 차차 흐려짐12 흐려져 뇌우13 흐려져 비 14 흐려져 눈15 흐려져 눈비 16 흐린 후 갬17 뇌우 후 갬 18 비 후 갬19 눈 후 갬 20 눈비 후 갬21 구름많음 22 황사 |
| ┣ wx | String | 현재날씨 |
| ┣ precipitation | String | 강수량 |
| ┣ precip\_a\_day | String | 일 누적 강수량 |
| ┗ snow\_height | String | 적설량 |
| myAirMileInfo | Object | 나의 에어마일 정보 (요청되지 않았으면 내려가지 않음) |
| ┣ result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| ┣ result\_msg | String | 결과코드에 따른 메세지 |
| ┣ totalMile | String | 나의 총 마일리지 |
| ┣ rankVariance | Integer | 순위변동사항 (하락 : 음수 , 상승 : 양수) |
| ┣ totalMemberCount | Integer | 총 사용자 수 |
| ┣ validity | Integer | 마일리지 유효기간 남은 날짜수로그인사용자의 경우 소멸 안되므로 -1 내려감 |
| ┣ totalMileRank | String | 나의 마일리지 순위 |
| ┗ unit | Integer | 전체 사용자 표출 단위1000, 10000, 1000000, 500000 |
| myAirMileInfoU | Object | 토탈 주간 모두 있는 마일리지 정보 (요청되지 않았으면 내려가지 않음) |
| ┣ result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| ┣ result\_msg | String | 결과코드에 따른 메세지 |
| ┣ totalMileInfo | Object | 전체 마일리지 정보 |
| ┣ mile | String | 나의 총 마일리지 |
| ┣ rankVariance | Integer | 순위변동사항 (하락 : 음수 , 상승 : 양수) |
| ┣ mileRank | String | 총 마일리지 순위 |
| ┣ totalMemberCount | Integer | 총 사용자 수 |
| ┣ validity | Integer | 마일리지 유효기간 남은 날짜수로그인사용자의 경우 소멸 안되므로 -1 내려감 |
| ┗ unit | Integer | 전체 사용자 표출 단위1000, 10000, 1000000, 500000 |
| ┗ weekMileInfo | Object | 전체 마일리지 정보 |
| ┣ mile | String | 주간 마일리지 |
| ┣ rankVariance | Integer | 주간 순위변동사항 (하락 : 음수 , 상승 : 양수) |
| ┣ mileRank | String | 주간 마일리지 순위 |
| ┣ totalMemberCount | Integer | 총 마일리지 순위 |
| ┣ validity | Integer | 마일리지 유효기간 남은 날짜수로그인사용자의 경우 소멸 안되므로 -1 내려감 |
| ┗ unit | Integer | 전체 사용자 표출 단위1000, 10000, 1000000, 500000 |
| todayAccumulateMileInfo | Object | 오늘 적립 에어마일 (요청되지 않았으면 내려가지 않음) |
| ┣ result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| ┣ result\_msg | String | 결과코드에 따른 메세지 |
| ┣ todayMile | Integer | 오늘 적립 마일리지 |
| ┣ todayPlusMile | Integer | 오늘 추가 적립 마일리지 |
| ┣ bonusAllocate | Double | 보너스 배당 |
| ┣ goalDistance | Double | 보너스 목표 거리 |
| ┗ bonusDistanceRate | Double | 거리대비(현재30KM) 주행완료 비율 |
| nearLowestOilInfo | Object | 주변 최저가 주유소 (요청되지 않았으면 내려가지 않음) |
| ┣ result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| ┣ result\_msg | String | 결과코드에 따른 메세지 |
| ┣ poi | Object | [[inavi-air-api-data#POI_DATA_A\|POI_DATA_A]] |
| nearLowestOilsInfo | Object | 주변 최저가 주유소'들' (요청되지 않았으면 내려가지 않음) |
| ┣ result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| ┣ result\_msg | String | 결과코드에 따른 메세지 |
| ┣ poi | Array | [[inavi-air-api-data#POI_DATA_A\|POI_DATA_A]] |
| myDirivingScoreInfo | Object | 나의 운전점수 (요청되지 않았으면 내려가지 않음) |
| ┣ result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| ┣ result\_msg | String | 결과코드에 따른 메세지 |
| ┣ score | String | 점수 |
| ┣ option1 | Object | 운전점수 옵션1 |
| ┣ subject | String | option1 주제(ex: 과속, 급가속, 급감속) |
| ┗ grade | Integer | 등급(0\~4) |
| ┣ option2 | Object | 운전점수 옵션2 |
| ┣ subject | String | option2 주제(ex: 과속, 급가속, 급감속) |
| ┗ grade | Integer | 등급(0\~4) |
| ┗option3 | Object | 운전점수 옵션3 |
| ┣ subject | String | option3 주제(ex: 과속, 급가속, 급감속) |
| ┗ grade | Integer | 등급(0\~4) |
| lastDrivingInfo | Object | 마지막 주행기록 (요청되지 않았으면 내려가지 않음) |
| ┣ result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| ┣ result\_msg | String | 결과코드에 따른 메세지 |
| ┣ distance | String | 주행거리 |
| ┣ startLoc | Object | 출발지정보 |
| ┣ lonx | String | 정규화 좌표x |
| ┣ laty | String | 정규화 좌표y |
| ┣ timestamp | Long | 출발시간 timestamp |
| ┗ addr | String | 주소 |
| ┗ endLoc | Object | 도착지정보 |
| ┣ lonx | String | 정규화 좌표x |
| ┣ laty | String | 정규화 좌표y |
| ┣ timestamp | Long | 도착시간 timestamp |
| ┗ addr | String | 주소 |
| NowMiseInfo | Object | 현재 위치 미세먼지 농도 (요청되지 않았으면 내려가지 않음) |
| ┣ result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| ┣ result\_msg | String | 결과코드에 따른 메세지 |
| ┣ concentration | Object | 미세먼지 농도 정보 |
| ┣ stationName | String | 측정소 위치 |
| ┣ oper | String | 측정소 이름 |
| ┣ addr | String | 측정소 주소 |
| ┣ pm10Value | String | PM10 농도 (지름 10㎛ 이하인 먼지. 거대분진) |
| ┣ pm10Grade | String | 농도 등급 (1:좋음, 2:보통, 3:나쁨, 4:매우나쁨) |
| ┣ pm25Value | String | PM25 농도 (지름 2.5㎛ 이하인 먼지. 초미세먼지) |
| ┣ pm25Grade | String | 농도 등급 (1:좋음, 2:보통, 3:나쁨, 4:매우나쁨) |
| ┗ uptime | Long | timestamp |
| lbsLuckyBox | Object | lbs기반 럭키박스 표출관련 |
| ┣ result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| ┣ result\_msg | String | 결과코드에 따른 메세지 |
| ┗ showBox | boolean | 럭키박스 표출유무 |
| todaysFortune | Object | 오늘의 운세 |
| ┣ result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| ┣ result\_msg | String | 결과코드에 따른 메세지 |
| ┣ fortuneType | String | Y:회원정보 있음N:회원정보 없음 |
| ┣ score | String | 운세 점수(회원정보 없을경우 empty String) |
| ┣ totTxt | String | 간략 운세(회원정보 없을경우 empty String) |
| ┗ url | String | 운세URL(회원정보 없을경우 띠별운세URL) |
| myAirCashInfo | Object | 나의 에어캐시 정보 |
| ┣ result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| ┣ result\_msg | String | 결과코드에 따른 메세지 |
| ┣ totalAirCash | Integer | 나의 총 에어 캐시 |
| ┣ todayDrivingDistance | Integer | 오늘 주행 거리(m) |
| ┣ maxDrivingDistance | Integer | 최대 주행 거리(m) |
| ┣ maxCash | Integer | 최대 적립 캐시 |
| ┗ saveableAirCash | Integer | 적립 가능한 캐시 |
| newCashExists | boolean | 적립 가능 캐시 존재 여부 (에어 캐시 고도화) |
| cashPrsnMsg | String | 캐시 개인화 메시지 (이미지 파일은 “,”로 구분 문구는 “/”로 구분) • **로그인 X**  :  airre\_main\_tooltip\_img\_1 (이미지), 로그인후 첫 주행/+1000캐시 (문구) • **0 \~ 1,599 (캐시범위)** : airre\_main\_tooltip\_img\_2 ,음료쿠폰까지/000캐시 • **1,600 \~ 2,999** : airre\_main\_tooltip\_img\_3 , 편의점 쿠폰까지/000캐시 • **3,000 \~ 4,499** : airre\_main\_tooltip\_img\_4, 커피 쿠폰까지/000캐시 • 4**,500 \~ 4,999 **: airre\_main\_tooltip\_img\_5, 아이스크림 쿠폰까지/000캐시 • **5,000 \~ 10,000** : airre\_main\_tooltip\_img\_6, 주유소 쿠폰까지/000캐시 |

## 오늘의운세 날짜유효성체크
> Confluence page id: 2262307687 · 최종 수정: 10월 01, 2026

### Function

> 오늘의운세 날짜유효성 체크

### URL

> `/fortuneBirthCheck`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| birthday | String | O | 생년월일EX(19881230) -\> YYYYMMDD |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |
| lunar | boolean | 음력날짜 존재여부 |
| sLunar | boolean | 윤달 음력날짜 존재여부 |

## Sources

- Confluence "INAVI AIR API" > 메인화면-AIR (2026-10-27 조회): 메인화면-AIR (2262307665), 날씨정보 (2262307707), 통합메인화면 (2262307727), 오늘의운세 날짜유효성체크 (2262307687)
