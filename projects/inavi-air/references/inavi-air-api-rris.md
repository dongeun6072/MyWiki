---
title: "INAVI AIR API — RRIS"
category: references
tags: [inavi-air, api, rris, visibility/internal]
aliases: [RRIS]
relationships:
  - target: "[[inavi-air-api-detail-spec]]"
    type: derived_from
sources: ["url:https://inavisystems.atlassian.net/wiki/spaces/AS/pages/2262305917"]
summary: >-
    INAVI AIR RRIS API(현재 위치 업로드, 경로 파일 정보 업로드, 이벤트 위치 업로드)의 요청·응답 필드를 Confluence 원문 그대로 옮긴 명세.
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

# INAVI AIR API — RRIS

Confluence "INAVI AIR API" > "RRIS" 영역을 원문 그대로 옮긴 페이지다. 엔드포인트 색인은 [[inavi-air-api-detail-spec]], 공통 헤더와 결과 코드는 [[inavi-air-api-common]], 소속 프로젝트는 [[inavi-air]]이다.

| API | URL |
|---|---|
| 경로 파일 정보 업로드 | `/rris/data/saveRoute` |
| 이벤트 위치 업로드 | `/rris/event/upEmergency` |
| 현재 위치 업로드 | `/rris/data/currentLoc` |

## 개요
> Confluence page id: 2262305917 · 최종 수정: 10월 06, 2026

- 🧭현재 위치 업로드
- 🧭경로 파일 정보 업로드
- 🧭이벤트 위치 업로드

## 경로 파일 정보 업로드
> Confluence page id: 2262305939 · 최종 수정: 10월 01, 2026

### Function

> 경로 파일 정보 업로드

### URL

`/rris/data/saveRoute`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| mapVer | String | O | 지도 버전 |
| rid | String | O | 탐색 파일 ID |
| dataUri | String | O | 탐색 파일 URL |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |

## 이벤트 위치 업로드
> Confluence page id: 2262305959 · 최종 수정: 10월 01, 2026

### Function

> 이벤트 위치 업로드

### URL

`/rris/event/upEmergency`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| eventId | String | O | 이벤트 ID<br>100: 구급차 |
| longitude | String | O | longitude |
| latitude | String | O | latitude |
| coordType | String | O | 좌표 타입<br>W : WGS84 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |

## 현재 위치 업로드
> Confluence page id: 2262305979 · 최종 수정: 10월 01, 2026

### Function

> 재 위치 업로드

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

- Confluence "INAVI AIR API" > RRIS (2026-10-27 조회): RRIS (2262305917), 경로 파일 정보 업로드 (2262305939), 이벤트 위치 업로드 (2262305959), 현재 위치 업로드 (2262305979)
