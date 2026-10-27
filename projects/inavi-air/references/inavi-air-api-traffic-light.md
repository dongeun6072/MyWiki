---
title: "INAVI AIR API — 신호등"
category: references
tags: [inavi-air, api, traffic-light, visibility/internal]
aliases: [신호등]
relationships:
  - target: "[[inavi-air-api-detail-spec]]"
    type: derived_from
sources: ["url:https://inavisystems.atlassian.net/wiki/spaces/AS/pages/2262308015"]
summary: >-
    INAVI AIR 신호등 API 명세 원문 전사. 대구 전체 신호등 정보 조회, 신호등 상태 조회, 보행자 신호등 정보 조회 규격을 담는다.
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

# INAVI AIR API — 신호등

Confluence "신호등" 페이지들을 요약 없이 그대로 옮긴 원문 전사본이다. 허브는 [[inavi-air-api-detail-spec]], 공통 헤더·결과 코드는 [[inavi-air-api-common]], 서비스 개요는 [[inavi-air]]를 본다. 대구 신호등 연동 프로토콜은 [[daegu-traffic-light-protocol]]을 본다.

| API | URL |
| --- | --- |
| [[#전체 신호등 정보 조회]] | `/trafficLightList` |
| [[#신호등 상태 조회]] | `/trafficLightStatus` |
| [[#보행자 신호등 정보 조회]] | `/trafficLightWalker` |

## 개요
> Confluence page id: 2262308015 · 최종 수정: 10월 06, 2026

상위 페이지 "신호등" 본문은 하위 API 링크 목록이다(원본 순서 그대로).

- 📙방향코드
- 🧭전체 신호등 정보 조회
- 🧭신호등 상태 조회
- 🧭보행자 신호등 정보 조회

## 전체 신호등 정보 조회
> Confluence page id: 2262308097 · 최종 수정: 10월 01, 2026

### Function

> 전체 신호등 정보 조회

### URL

> `/trafficLightList`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| 제목 없음 |  |  |  |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] 0 : 성공 |
| result\_msg | String | 결과값에 따른 메세지 |
| ver | String | 대구 신호등 전체 리스트 버전 정보 ex) ver0.1 |
| info\_list | Array | 대구 신호등 전체 리스트 JSON 데이터 |
| ┣ nodeID | Long | 신호등 Node ID ex) 1570062500 |
| ┣ nodeType | Byte | Node 형태 1 : 교차로 중심 2 : 안내 신호등 |
| ┣ nodeName | String | Node 명칭 ex) “국가산단04” |
| ┣ compassCode | Byte | [[inavi-air-api-data#방향코드\|방향코드]] |
| ┣ longitude | Integer | 경도 ex) 272693 |
| ┣ latitude | Integer | 위도 ex) 306482 |
| ┣ angle | Integer | 진입 각도 EX) 0 |
| ┗ mapID | Integer | Map ID ex) 4101 |

## 신호등 상태 조회
> Confluence page id: 2262308055 · 최종 수정: 10월 01, 2026

### Function

> 신호등 상태 조회

### URL

> `/trafficLightStatus`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| nodeID | String | O | 신호등 Node Id (Node ID) |
| compassCode | String | O | 신호등 방향 코드 (compassCode) [[inavi-air-api-data#방향코드\|방향코드]] |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] 0 : 성공 |
| result\_msg | String | 결과값에 따른 메세지 |
| info\_list | Array | 신호등 상태 정보 리스트 |
| ┣ operationInfo | String | 신호등 운영 정보 **EX) 정상, 전이, 감응, 소등, 점멸, 수동** |
| ┣ wrongInfo | String | 신호등 이상 정보 **EX) 정상, SCU 통신 이상, 센터 통신 이상, 모순 이상** |
| ┣ opIdx | Integer | 신호등 운영 주기  (신호등 운영 사이클에 대한 진행 시간을 초로 표기한 값) 진행 시간 : 초 |
| ┣ roadType | String | 신호등의 종류 **EX) 미지정, 직진, 좌회전, 보행자, 자전거, 우회전, 버스, 유턴** |
| ┣ seeTime | Integer | 신호 상태 표출 시간 |
| ┣ remainTime | Integer | 신호 상태 잔여 시간 |
| ┣ color | String | 신호등 색상 **EX) 소등, 적색 점등, 황색 점등, 녹색 점등, 적색 점멸, 황색 점멸, 녹색 점멸** |
| ┣ varTime | String | 신호등 시간의 가변 유무 |
| ┗  timeStmp | Integer | 정보가 들어온 시간 Time Stamp |
| 제목 없음 |  |  |

## 보행자 신호등 정보 조회
> Confluence page id: 2262308077 · 최종 수정: 10월 01, 2026

### Function

> 보행자 신호등 정보 조회

### URL

> `/trafficLightWalker`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| nodeID | String | O | 신호등 Node Id (Node ID) |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | Byte | [[inavi-air-api-common#결과 코드\|결과 코드]] 0 : 성공 1 : 데이터 없음 2 : 서버 응답 없음 |
| result\_msg | String | 결과값에 따른 메세지 |
| nodeID | Long | 요청한 NodeID |
| listCnt | Integer | 보행자 신호등 정보 리스트 개수 |
| info\_list | Array | 신호등 상태 정보 리스트 |
| ┣ bearingCode | Integer | 방향 코드 |
| ┣ trafLighAnomInfo | Integer | 신호등 이상 정보 **EX) 정상, SCU 통신 이상, 센터 통신 이상, 모순 이상** |
| ┣ signlExtnYn | Integer | 신호 상태의 연장 여부 |
| ┣ wtrmsCrosngYn | Integer | 무단 횡단자 존재 여부 |
| ┣ leftBearingCode | Integer | 왼쪽 신호등 방향 코드 |
| ┣ leftWalkerYN | Integer | 왼쪽 신호등의 보행자 여부 |
| ┣ leftAwaiteYN | Integer | 왼쪽 신호등 대기자 여부 |
| ┣ rightBearingCode | Integer | 오른쪽 신호 |
| ┣ rightWalkerYN | Integer | 오른쪽 신호등 보행자 여부 |
| ┣ rightAwaiterYN | Integer | 오른쪽 신호등 대기자 여부 |
| ┣ remainingTime | Integer | 신호 상태 잔여 시간 |
| ┣ pedSignalState | String | 신호등 색상 R: 적색등 G: 녹색등 GF : 녹색 깜빡임 |
| ┗  timeStmp | Integer | 정보가 들어온 시간 EX) 1689560090 |
| 제목 없음 |  |  |

## Sources

- Confluence "INAVI AIR API" > 신호등 (2026-10-27 조회): 신호등 (2262308015), 전체 신호등 정보 조회 (2262308097), 신호등 상태 조회 (2262308055), 보행자 신호등 정보 조회 (2262308077)
