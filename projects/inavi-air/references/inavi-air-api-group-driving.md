---
title: "INAVI AIR API — 그룹주행"
category: references
tags: [inavi-air, api, group-driving, visibility/internal]
aliases: [그룹주행, 그룹주행-AIR]
relationships:
  - target: "[[inavi-air-api-detail-spec]]"
    type: derived_from
sources: ["url:https://inavisystems.atlassian.net/wiki/spaces/AS/pages/2262306703"]
summary: >-
    INAVI AIR 그룹주행 API(그룹만들기, 그룹나가기, 위치제공사실조회, 현재 위치 업로드)의 요청·응답 필드를 Confluence 원문 그대로 옮긴 명세.
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

# INAVI AIR API — 그룹주행

Confluence "INAVI AIR API" > "그룹주행-AIR" 영역을 원문 그대로 옮긴 페이지다. 엔드포인트 색인은 [[inavi-air-api-detail-spec]], 공통 헤더와 결과 코드는 [[inavi-air-api-common]], 소속 프로젝트는 [[inavi-air]]이다. 설계 배경은 [[inavi-air-group-driving-design]], 위치 제공 동의는 [[group-driving-location-permission]]을 본다.

| API | URL |
|---|---|
| 그룹만들기 | `/makeGroup` |
| 그룹나가기 | `/groupUpdate` |
| 위치제공사실조회 | `/groupDrivingHis` |
| 현재 위치 업로드 | `/rris/data/currentLoc` |

## 개요
> Confluence page id: 2262306703 · 최종 수정: 10월 06, 2026

- 🧭그룹만들기
- 🧭현재 위치 업로드
- 🧭그룹나가기
- 🧭위치제공사실조회

## 그룹만들기
> Confluence page id: 2262306727 · 최종 수정: 10월 01, 2026

### Function

> 그룹 만들기

### URL

`/makeGroup`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| destiName | String |  | 도착지 이름 |
| destiPoiId | String |  | 도착지 poiId |
| destiX | String | O | 도착 좌표x (정규화) |
| destiY | String | O | 도착 좌표y (정규화) |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| groupId | String | 그룹아이디 |
| shortenURL | String | 숏URL(기능 구현 후 검토 예정) |

## 그룹나가기
> Confluence page id: 2262306747 · 최종 수정: 10월 01, 2026

### Function

> 그룹 나가기

### URL

`/groupUpdate`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| groupId |  |  | 그룹ID |
| status | O | String | 나가기 : E (지금은 나가기만 하기떄문에 E로 전달해주시면됩니다) |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |

## 위치제공사실조회
> Confluence page id: 2262306767 · 최종 수정: 10월 01, 2026

### Function

> 위치제공사실조회

### URL

`/groupDrivingHis`

[[inavi-air-api-common#Request Header|📙Request Header]]

### Request Parameter

> 원본 표가 비어 있음

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |
| his | Array | 위치제공사실조회 이력(최근1달간) |
| ├ positioningMdn | String | 측위자(자신의 위치를 조회 한 사람) 암호화된 MDN |
| ├ startDate | String | 시작시점(YYYYMMDDHHMISS) |
| ├ endDate | String | 종료시점(YYYYMMDDHHMISS) |
| ├ count | String | 측위횟수 |

## 현재 위치 업로드
> Confluence page id: 2262306787 · 최종 수정: 10월 01, 2026

### Function

> 현재 위치 업로드

### URL

`/rris/data/currentLoc`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| x | String | O | X좌표 |
| y | String | O | Y좌표 |
| coordType | String | O | 좌표 타입<br>W : WGS84<br>R : 탐색 좌표<br>S : 검색 좌표 |
| myInfo | Object |  | 그룹주행이 아닐경우 오브젝트 안보내면됨 |
| ├ groupId | String | O | 그룹아이디 |
| ├ remainDistance | String | O | 목적지까지 남은거리 |
| ├ remainTime | String | O | 목적지까지 남은시간<br>단위 : 초 |
| ├ desX | String | O | 목적지 X좌표 (TW index) |
| ├ desY | String | O | 목적지 Y좌표 (TW index) |
| ├ desPoi | String |  | 목적지 POIID |
| ├ desName | String |  | 목적지 이름 |
| ├ snsId | String |  | snsID(sns사용자일 경우) |
| ├ snsType | String |  | snsType<br>g:구글, k:카카오, f:페이스북, n:네이버(sns사용자일 경우) |
| ┗ allowList | List |  | 위치공유를 허용할 상대방의 privateKey리스트 (항상 최신 스냅샷을 보내야함) |
| rrisObject | Object |  | rris Object rris 아닐경우 오브젝트 안보내도됨 |
| ├ mapVer | String | O | 지도 버전 |
| ├ speed | Integer | O | 현재 주행 속도(km/h) |
| ├ bearing | Integer | O | 진행 각도 |
| ┗ link | Object | O | 현재 도로 mr link 정보 |
| ├ mapId | Integer | O | mapId |
| ├ linkId | Integer | O | linkId |
| ├ nodeId | Integer | O | nodeId |
| ┗ direction | Integer | O | direction |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |
| groupId | String | 그룹ID(그룹주행관련한 요청이 아닐경우 안채워짐) |
| groupMembers | Array | 그룹멤버 정보 (그룹주행관련한 요청이 아닐경우 안채워짐) |
| ├ privateKey | String | 그룹멤버 프라이빗키 |
| ├ mdn | String | 암호화된 mdn |
| ├ snsId | String | snsId(sns유저일 경우) |
| ├ snsName | String | snsName(sns유저일 경우) |
| ├ snsImageUrl | String | snsImageUrl(sns유저일 경우) |
| ├ remainDistance | String | 목적지까지 남은거리 |
| ├ remainTime | String | 목적지까지 남은시간 |
| ├ updateTime | String | 최근 수정시간<br>밀리세컨드 |
| ├ status | String | 그룹 참여 상황<br>D:주행중 G: 도착 |
| ├ x | String | 현재X 좌표 |
| ├ y | String | 현재Y 좌표 |
| ├ allowFlag | boolean | 나를 상대방이 허용했는지 여부 (이플래그를보고 좌표,목적지까지 남은거리 남은시간이 없는경우 위치없음인지 허용이 아닌지 판단) |
| ├ iAllowFlag | boolean | 내가 상대방을 허용했는지 Flag |
| ├ isLeader | boolean | 그룹방장 여부 |
| ┗ isMe | boolean | 자기자신인지 여부 |

## Sources

- Confluence "INAVI AIR API" > 그룹주행-AIR (2026-10-27 조회): 그룹주행-AIR (2262306703), 그룹만들기 (2262306727), 그룹나가기 (2262306747), 위치제공사실조회 (2262306767), 현재 위치 업로드 (2262306787)
