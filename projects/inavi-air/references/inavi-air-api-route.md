---
title: "INAVI AIR API — 탐색"
category: references
tags: [inavi-air, api, route, road-event, visibility/internal]
aliases: [탐색]
relationships:
  - target: "[[inavi-air-api-detail-spec]]"
    type: derived_from
sources: ["url:https://inavisystems.atlassian.net/wiki/spaces/AS/pages/2262309456"]
summary: >-
    INAVI AIR 경로 탐색 API 명세 원문 전사. 일반·리스트·재·요약 경로 탐색, 타임머신(시간예측), 경로 내/전체/탐색 유고 정보, 경로 주변 부가 정보, 대중교통 요약 길찾기를 담는다.
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

# INAVI AIR API — 탐색

Confluence "탐색" 페이지들을 요약 없이 그대로 옮긴 원문 전사본이다. 허브는 [[inavi-air-api-detail-spec]], 공통 헤더·결과 코드는 [[inavi-air-api-common]], 서비스 개요는 [[inavi-air]]를 본다.

| API | URL |
| --- | --- |
| [[#일반 경로 탐색]] | `/findMultiRoute` |
| [[#일반 경로 리스트 탐색]] | `/findListRoute` |
| [[#경로 재 탐색]] | `/findRouteAgain` |
| [[#요약결과 경로 탐색]] | `/findSummaryRoute` |
| [[#타임머신(시간예측)]] | `/findStatRoute` |
| [[#경로 내 유고 정보]] | `/routeRoadEvent` |
| [[#전체 유고 정보 조회]] | `/fullRoadEvent` |
| [[#경로 주변 부가 정보]] | `/routeOtherInfo` |
| [[#대중교통 요약 길찾기]] | `/summaryPath` |
| [[#탐색 유고정보 조회]] | `/routingEvent` |

## 개요
> Confluence page id: 2262309456 · 최종 수정: 10월 06, 2026

상위 페이지 "탐색" 본문은 하위 API 링크 목록이다(원본 순서 그대로).

- 🧭일반 경로 탐색
- 🧭일반 경로 리스트 탐색
- 🧭경로 재 탐색
- 🧭요약결과 경로 탐색
- 🧭타임머신(시간예측)
- 🧭경로 내 유고 정보
- 🧭전체 유고 정보 조회
- 🧭경로 주변 부가 정보
- 🧭대중교통 요약 길찾기
- 🧭탐색 유고정보 조회

## 일반 경로 탐색
> Confluence page id: 2262309630 · 최종 수정: 10월 06, 2026

### Function

> 일반 경로 탐색

### URL

> `/findMultiRoute`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| searchOption | String |  | **Agent 탐색 종류** 해당 파라미터 사용 시 searchOptions null로 설정 해야 함  \<일반\> agt\_recommend : 추천경로 (LGU+ 향으로는 “빠른길”) agt\_short\_time : 최소시간 real\_traffic\_freeroad : 무료도로 short\_distance\_priority : 최단거리 highway\_priority : 고속도로우선 motorcycle : 이륜차 이용도로 beginner : 초보자(편한길) (LGU+ 향으로는 “편한길”) recommendation : 엔진기반 추천경로(agt\_recommend 대체) time\_priority : 엔진기반 최소시간(agt\_short\_time 대체) recommendation\_eco: 친환경  \<화물\> truck1 : 실시간 만차 truck1\_freeroad : 실시간 만차 무료 truck2 : 실시간 공차 truck2\_freeroad : 실시간 공차 무료 truck1\_nationalway : 국도 만차 truck2\_nationalway : 국도 공차 truck\_empty: 트럭 공차시 추천 경로 truck\_empty\_freeroad: 트럭 공차시 무료 경로 truck\_empty\_nationalway: 트력 공차시 국도 위주 경로 truck\_full: 트럭 만차시 추천 경로 truck\_full\_freeroad: 트럭 만차시 무료 경로 truck\_full\_nationalway: 트럭 만차시 국도 위주 경로 |
| searchOption2 | String |  | **Agent 탐색 종류2** 해당 파라미터 사용 시 searchOptions null로 설정 해야 함  \<일반\> agt\_recommend : 추천경로 (LGU+ 향으로는 “빠른길”) agt\_short\_time : 최소시간 real\_traffic\_freeroad : 무료도로 short\_distance\_priority : 최단거리 highway\_priority : 고속도로우선 motorcycle : 이륜차 이용도로 beginner : 초보자(편한길) (LGU+ 향으로는 “편한길”) recommendation : 엔진기반 추천경로(agt\_recommend 대체) time\_priority : 엔진기반 최소시간(agt\_short\_time 대체)  \<화물\> truck1 : 실시간 만차 truck1\_freeroad : 실시간 만차 무료 truck2 : 실시간 공차 truck2\_freeroad : 실시간 공차 무료 truck1\_nationalway : 국도 만차 truck2\_nationalway : 국도 공차 truck\_empty: 트럭 공차시 추천 경로 truck\_empty\_freeroad: 트럭 공차시 무료 경로 truck\_empty\_nationalway: 트력 공차시 국도 위주 경로 truck\_full: 트럭 만차시 추천 경로 truck\_full\_freeroad: 트럭 만차시 무료 경로 truck\_full\_nationalway: 트럭 만차시 국도 위주 경로 |
| searchOptions | Array\<String\> |  | **Agent 리스트 탐색 종류** 해당 파라미터 사용 시 searchOption, serchOption2 null로 설정 해야 함  \<일반\> agt\_recommend : 추천경로 (LGU+ 향으로는 “빠른길”) agt\_short\_time : 최소시간 real\_traffic\_freeroad : 무료도로 short\_distance\_priority : 최단거리 highway\_priority : 고속도로우선 motorcycle : 이륜차 이용도로 beginner : 초보자(편한길) (LGU+ 향으로는 “편한길”) recommendation : 엔진기반 추천경로(agt\_recommend 대체) time\_priority : 엔진기반 최소시간(agt\_short\_time 대체)  \<화물\> truck1 : 실시간 만차 truck1\_freeroad : 실시간 만차 무료 truck2 : 실시간 공차 truck2\_freeroad : 실시간 공차 무료 truck1\_nationalway : 국도 만차 truck2\_nationalway : 국도 공차 truck\_empty: 트럭 공차시 추천 경로 truck\_empty\_freeroad: 트럭 공차시 무료 경로 truck\_empty\_nationalway: 트력 공차시 국도 위주 경로 truck\_full: 트럭 만차시 추천 경로 truck\_full\_freeroad: 트럭 만차시 무료 경로 truck\_full\_nationalway: 트럭 만차시 국도 위주 경로 |
| avoidSchoolZone | String |  | 스쿨존 회피(searchOption)0:회피 안함(Default)1:회피 |
| avoidSchoolZone2 | String |  | 스쿨존 회피(searchOption2)0:회피 안함(Default)1:회피 |
| ignoreTimeRestrictedZone | String |  | 시간제 통행 규제 무시 0: 무시안함(Default) 1: 무시 |
| useHighwayProjectionStart | String |  | 출발지 고속도로, 자동차전용, 도시고속 회피 0: 회피 안함(Default) 1: 회피 |
| useHighwayProjectionEnd |  |  | 목적지 고속도로, 자동차전용, 도시고속 회피 0: 회피 안함(Default) 1: 회피 |
| mrVersion | String | O | MR version |
| searchType | String | O | 탐색종류 0: 일반탐색 4: MYWAY(특정대교) 5: 테마도로 6: MYCCTV 7: 통계탐색 |
| directivity | boolean |  | 목적지 방향성 탐색 true : 사용 false : 사용안함(default) |
| rotate | boolean |  | 회전규제 고려 탐색 true : 사용 false : 사용안함(default) |
| dual | boolean |  | 경로선 이원화(가상 분리된 경로선) true : 사용 false : 사용안함(default) |
| forced | boolean |  | 도로상 통행 제한지점 강제통과 true : 사용 false : 사용안함(default) |
| searchString | String |  | 검색어(검색어가 사용되는 기능을 통한 탐색시)(Log) |
| inMethod | INTEGER |  | 경로탐색을 호출한 기능(Log) 0: 통합검색 1: 최근검색어 3: 즐겨찾기 4: 이전목적지 6: 타임머신 7: AI를통한 호출(AI플래그와 타 플래그가 동시에 적용되는 시나리오에서는 구분자 '/'로 같이 보내주어야함) 8: 지도(위치지정) 9: 메인카드 10: 외부연동 11: 주변검색 12: 주소검색 13: 미정의 |
| routeOpt\_sub | String |  | 경로옵션(대교탐색/해안도로/구간비교/주행중탐색 인 경우만)(Log) BRDG 대교탐색 SHORE 해안도로 REROUTE 주행중탐색 |
| routeOpt\_sub\_name | String |  | 대교탐색 인 경우 해당 대교의 이름(Log) |
| curPosType (LogApi = startPosType) | String |  | 출발지가 GPS 3D Fix 시의 위치인지의 여부(Log) GPS GPS 에서 수신된 위치 OTHER GPS 에서 수신된 위치가 아닌 위치를 사용하거나 유저가 출발지를 지정한 경우 |
| category | Array |  | 선호주유소 카테고리 코드 리스트 |
| ┗ val | String |  | [[inavi-air-api-data#Category Code\|Category Code]] C0100 : 주유소(default) |
| oil | String |  | 유종 0: 휘발유 1: 고급휘발유 2: 경유 3: LPG 4: 전기(EV) 5: 수소 |
| baseUrl | String |  | 코드42 요청 URL |
| startloc | Object | O | 출발지 지점 정보 |
| ┣ lonx | String | O | 출발지 경도, 정규화좌표 X값 |
| ┣ laty | String | O | 출발지 위도, 정규화좌표 Y값 |
| ┣ pid | String |  | 위치의 PID(Log) (startPos 에서는 PID 생략 가능) |
| ┣ name | String | O | 출발지 명칭 |
| ┣ mapid | String | O | 출발지 도엽번호 |
| ┣ linkid | String | O | 출발지 링크번호 |
| ┣ nodeid | String | O | 출발지 노드번호 |
| ┣ direction | String | O | 출발지 방향 |
| ┣ angle | String |  | 정북 기준 도로 진행 방향(코드42) |
| ┣ usingName | boolean |  | 지점명칭 사용 true : 사용(default) false : 사용안함 |
| ┣ usingHideViaLoc | boolean |  | 숨김 경유지 true : 사용 false : 사용안함(default) |
| ┣ viaLocStart | boolean |  | 경유도로 시작 true : 사용 false : 사용안함(default) |
| ┗ viaLocEnd | boolean |  | 경유도로 종료 true : 사용 false : 사용안함(default) |
| endloc | Object | O | 도착지 지점 정보 |
| ┣ lonx | String | O | 도착지 경도, 정규화좌표 X값 |
| ┣ laty | String | O | 도착지 위도, 정규화좌표 Y값 |
| ┣ pid | String |  | 위치의 PID(Log) (endloc 에서는 PID 생략 가능) |
| ┣ ctrIdx1 | String |  | 도착지 PID에 대한 CTR 검색 결과 idx1 정보(Log) |
| ┣ ctrIdx2\_1 | String |  | 도착지 PID에 대한 CTR 검색 결과 idx2-1 정보(Log) |
| ┣ ctrIdx2\_2 | String |  | 도착지 PID에 대한 CTR 검색 결과 idx2-2 정보(Log) |
| ┣ ctrSortFlag | String |  | 도착지 PID에 대한 CTR 검색 결과 sort flag 정보(Log) 정렬순서 DIST: 거리순 ACCU: 정확도순 |
| ┣ name | String | O | 도착지 명칭 |
| ┣ mapid | String | O | 도착지 도엽번호 |
| ┣ linkid | String | O | 도착지 링크번호 |
| ┣ nodeid | String | O | 도착지 노드번호 |
| ┣ direction | String | O | 도착지 방향 |
| ┣ usingName | boolean |  | 지점명칭 사용 true : 사용(default) false : 사용안함 |
| ┣ usingHideViaLoc | boolean |  | 숨김 경유지 true : 사용 false : 사용안함(default) |
| ┣ viaLocStart | boolean |  | 경유도로 시작/종료 true : 사용 false : 사용안함(default) |
| ┗ viaLocEnd | boolean |  | 경유도로 종료 true : 사용 false : 사용안함(default) |
| vialocList | Array |  | 경유지 지점 정보 |
| ┣ lonx | String |  | 경유지 경도, 정규화좌표 X값 |
| ┣ laty | String |  | 경유지 위도, 정규화좌표 Y값 |
| ┣ pid | String |  | 위치의 PID(endloc 에서는 PID 생략 가능)(Log) |
| ┣ ctrIdx1 | String |  | 경유지 PID에 대한 CTR 검색 결과 idx1 정보(Log) |
| ┣ ctrIdx2\_1 | String |  | 경유지 PID에 대한 CTR 검색 결과 idx2-1 정보(Log) |
| ┣ ctrIdx2\_2 | String |  | 경유지 PID에 대한 CTR 검색 결과 idx2-2 정보(Log) |
| ┣ ctrSortFlag | String |  | 도착지 PID에 대한 CTR 검색 결과 sort flag 정보(Log) 정렬순서 DIST: 거리순 ACCU: 정확도순 |
| ┣ name | String |  | 경유지 명칭 |
| ┣ mapid | String |  | 경유지 도엽번호 |
| ┣ linkid | String |  | 경유지 링크번호 |
| ┣ nodeid | String |  | 경유지 노드번호 |
| ┣ direction | String |  | 경유지 방향 |
| ┣ usingName | boolean |  | 지점명칭 사용 true : 사용(default) false : 사용안함 |
| ┣ usingHideViaLoc | boolean |  | 숨김 경유지 true : 사용 false : 사용안함(default) |
| ┣ viaLocStart | boolean |  | 경유도로 시작/종료 true : 사용 false : 사용안함(default) |
| ┗ viaLocEnd | boolean |  | 경유도로 종료 true : 사용 false : 사용안함(default) |
| extensionList | Array |  | 확장 리스트 |
| ┣ headerType | String |  | 확장 리스트 타입 1: 다중목적지 최적탐색 2: 지나간 톨게이트 3: 사용자정보 5: 경유도로 6: 유고회피 7: 경로회피 13 : 교통정보 세부 설정 |
| ┣ routepoints | Array |  | 다중목적지 리스트 (when headerType is 1) |
| ┣ rpx | String |  | 목적지 X좌표 |
| ┗ rpy | String |  | 목적지 Y좌표 |
| ┣ tollList | Array |  | 톨게이트 정보 리스트 (when headerType is 2) |
| ┣ tolltype | String |  | 톨게이트 Type |
| ┗ tollidx | String |  | 톨게이트 index |
| ┣ userInput | Object |  | 사용자 입력 정보 (when headerType is 3) |
| ┣ height | String |  | 높이(단위:Cm) |
| ┣ weight | String |  | 중량(단위:kg) |
| ┣ hipass | boolean |  | 하이패스 소지 true: 소지 false: 미소지 |
| ┣ over3 | boolean |  | 3인이상 true: 3인이상 false: 3인이하 |
| ┣ zonelimit | boolean |  | 상수원 보호구역 진입 제한 차량true: 제한false: 미제한 |
| ┣ cartype | String |  | 차종 0: 1종(승용/승합/화물) 1: 2종(승합/화물) 2: 3종(승합/화물) 3: 4종(화물) 4: 5종(화물) 5: 6종 경차 |
| ┣ dishigh | String |  | 고속도로 통행료 할인 0: 없음 1: 50%할인 2: 면제 |
| ┣ carUsage | String |  | 차량 용도 0: 일반(Default) 1: 택시 서비스 1(Onda) 2: 택시 서비스2 (i.M) 3: 타다 서비스 (VCNC) 4: Baemin 서비스(우아한 형제들) 5: Where 서비스(MXI) |
| ┗ disjam | String |  | 혼잡 통행료 할인 0: 없음 1: 50%할인 2: 면제 |
| ┣ viaRoadList | Array |  | 경유도로 리스트 (when headerType is 5) |
| ┣ viaRoadlinkList | Array |  | 경유도로 Link 리스트 |
| ┣ mapid | String |  | 도엽 번호 |
| ┗ linkid | String |  | 링크 번호 |
| ┣ eventList | Array |  | 유고회피 리스트 (when headerType is 6) |
| ┗ eid | String |  | 유고정보 고유번호 |
| ┣ evasList | Array |  | 경로회피 리스트 (when headerType is 7) |
| ┣ mapid | String |  | 도엽 번호 |
| ┣ linkid | String |  | 링크 번호 |
| ┣ nodeid | String |  | 노드 번호 |
| ┣ ext | String |  | 부가 정보 |
| ┗ linkposition | String |  | 링크 포지션 |
| ┣ userSetting | Object |  | 사용자 설정 정보 반영 탐색 (when headerType is 11) |
| ┣ rheightlimit | boolean |  | 도로 통과 높이 제한 기능 사용 true: 사용 false: 미사용 |
| ┣ rweightlimit | boolean |  | 도로 통과 중량 제한 기능 사용 true: 사용 false: 미사용 |
| ┣ zonelimit | boolean |  | 상수원 보호구역 진입 제한 유무 true: 제한 false: 미제한 |
| ┣ sevasion | boolean |  | 좁은길 회피 기능 사용 true: 사용 false: 미사용 |
| ┣ uevasion | boolean |  | 유턴 회피 기능 사용 true: 사용 false: 미사용 |
| ┣ frevasion | boolean |  | 화물차 통행제한 구간 회피 기능 사용 true: 사용 false: 미사용 |
| ┣  mevasion | boolean |  | 위수지역 회피 기능 사용 true: 사용 false: 미사용 |
| ┣ height | String |  | 차량 높이(단위:Cm) |
| ┣ weight | String |  | 차량 중량(단위:kg) |
| ┣ nroadevasion | String |  | 왕복 n 차선 이하 도로 회피 |
| ┗ nuturnevasion | String |  | 왕복 n 차선 이하 유턴 회피 |
| ┗ trafficSetting | Object |  | 교통정보 세부 설정탐색 (when headerType is 13) |
| ┗ trafficUnflag | boolean |  | 교통정보 미사용 여부 true : 미사용 (삼성 중공업) false : 사용 (Default) |
| timestamp | String |  | 로그주행 탐색시작 시간 EX) 1689567848 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| isSame | boolean | 결과가 모두 같은지 여부 true : 같음 false : 다름 |
| routeList | Array | 경로탐색 결과 리스트 \*searchOption2가 입력 된 경우 2개, 입력 되지 않은 경우 1개의 리스트 반환 |
| ┣ rid | String | 경로 ID \*리스트가 다수 인 경우 다른 리스트와 동일한 rid가 응답 될 수 있음 |
| ┣ option\_type | String | **Agent 탐색 종류**  \<일반\> agt\_recommend : 추천경로 (LGU+ 향으로는 “빠른길”) agt\_short\_time : 최소시간 real\_traffic\_freeroad : 무료도로 short\_distance\_priority : 최단거리 highway\_priority : 고속도로우선 motorcycle : 이륜차 이용도로 beginner : 초보자(편한길) (LGU+ 향으로는 “편한길”) recommendation : 엔진기반 추천경로(agt\_recommend 대체) time\_priority : 엔진기반 최소시간(agt\_short\_time 대체)  \<화물\> truck1 : 실시간 만차 truck1\_freeroad : 실시간 만차 무료 truck2 : 실시간 공차 truck2\_freeroad : 실시간 공차 무료 truck1\_nationalway : 국도 만차 truck2\_nationalway : 국도 공차 truck\_empty: 트럭 공차시 추천 경로 truck\_empty\_freeroad: 트럭 공차시 무료 경로 truck\_empty\_nationalway: 트력 공차시 국도 위주 경로 truck\_full: 트럭 만차시 추천 경로 truck\_full\_freeroad: 트럭 만차시 무료 경로 truck\_full\_nationalway: 트럭 만차시 국도 위주 경로 |
| ┣ rdata | String | 경로 Data URI |
| ┣ gdata | String | 안내 Data URI |
| ┣ tdata | String | 교통정보 Data URI |
| ┣ poi | Object | 최저가주유소 검색결과 |
| ┣ catecode | String | 분류코드 |
| ┣ dpx | String | display X좌표(WGS84의 경우 longitude) |
| ┣ dpy | String | display Y좌표(WGS84의 경우 latitude) |
| ┣  oildata | Object | 유가 데이터 정보 |
| ┣ g\_price | Integer | 휘발유 가격 |
| ┣ g\_least | Integer | 최저 휘발유 가격제공 Flag(0: 아님 1: 맞음) |
| ┣ hg\_price | Integer | 고급휘발유 가격 |
| ┣ hg\_least | Integer | 최저 고급휘발유 가격제공 Flag(0: 아님 1: 맞음) |
| ┣ d\_price | Integer | 경유 가격 |
| ┣ d\_least | Integer | 최저 경유 가격제공 Flag(0: 아님 1: 맞음) |
| ┣ l\_price | Integer | LPG 가격 |
| ┣ l\_least | Integer | 최저 LPG 가격제공 Flag(0: 아님 1: 맞음) |
| ┗ updatetime | String | Update 시간 |
| ┣ evcstation | Object | 전기차 데이터 정보 |
| ┣ agency | String | 충전소기관DE:대구환경공단KN:부산울산경남지역본부GN:지엔텔KT:케이티EV:에버온ST:에스트래픽BG:비긴스JE:제주전기자동차서비스KP:한국전력HE:한국전기차충전서비스PI:포스코ICTSE:서울시PW:파워큐브CT:씨티카ME:환경부CV:대영채비JD:제주도청TM:티맵 |
| ┣ station\_id | String | 충전소고유ID |
| ┣ fee | String | 충전가격(Kwh) |
| ┣ free\_parking | String | 주차비유료여부 |
| ┣ operating\_hour | String | 운영시간 |
| ┣ opagency | String | 운영기관 |
| ┣ opagency\_contact | String | 운영기관연락처 |
| ┣ reservation | String | 예약여부 |
| ┣ membership | String | 멤버쉽여부 |
| ┣ serviceable | String | 사용가능여부 |
| ┣ update\_timestamp | String | 업데이트시각 |
| ┣ charger\_count | Integer | 전기차 충전기 개수 |
| ┣ evcharger | Array | 충전기정보 |
| ┣ chargerid | String | 충전기ID |
| ┣ agency\_mangeid | String | 기관관리 ID |
| ┣ type\_1 | String | 충전기타입\_101:DC차데모02:AC완속03:DC차데모+AC3상04:DC콤보05:DC차데모+DC콤보06:DC차데모+AC3상+DC콤보07:AC급속3상 |
| ┣ type\_2 | String | 충전기타입\_2(상세타입)ex) a,ba:DC차데모b:AC완속c:DC콤보d:AC급속3상 |
| ┣ status | String | 충전기상태0:알수없음1:통신이상2:충전대기3:충전중4:운영중지5:점검중6:예약중7:표시안함 |
| ┣ fee\_type | String | 충전 유료여부 |
| ┣ cable\_type | String | 케이블여부 |
| ┣ display\_type | String | 표시여부 |
| ┣ update\_timestamp | String | 업데이트 시각 |
| ┗ manufacture | String | 충전기제조사J:일진전기Y:중앙제어C:시그넷H:효성I:LS산전L:LS전선N:LGCNSP:PNEK:코디에스KE:KLINELEXE:이엔테크놀로지D:광명DNCB:보타리에너지PC:피앤씨주식회사AF:주식회사AFTEP:이카플러그JW:제원쏠라DK:대경엔지니어링RV:한국알박PQ:파워큐브DY:대영채비MT:모던텍 |
| ┣ type\_1\_info | Array | 충전기 타입\_1 별 정보 |
| ┣ name | String | 충전기 타입 이름01:DC차데모02:AC완속03:DC차데모+AC3상04:DC콤보05:DC차데모+DC콤보06:DC차데모+AC3상+DC콤보07:AC급속3상 |
| ┣ charger\_count | Integer | 전기차 충전기 해당 타입 수량 |
| ┗ charger\_ok\_count | Integer | 충전 가능 수량 |
| ┣ type\_2\_info | Array | 충전기 타입\_2(상세타입) 별 정보 |
| ┣ name | String | 충전기 타입 이름a:DC차데모b:AC완속c:DC콤보d:AC급속3상 |
| ┣ charger\_count | Integer | 전기차 충전기 해당 타입 수량 |
| ┗ charger\_ok\_count | Integer | 충전 가능 수량 |
| ┣ summary | Object | 전기차 충전소 요약 정보 |
| ┣ charge | boolean | 충전소 충전 가능 여부.true : 가능false : 불가능 |
| ┣ feetext | String | 충전기 가격 정보.무료유료 |
| ┣ simple | Array | 충전소 충전기 요약 정보. |
| ┣ name | String | 충전소 보유 충전기 이름.(type2 기준 해당 순으로 정렬)a:DC차데모d:AC3상c:DC콤보b:완속 |
| ┗ charge | boolean | 충전기 충전 가능 여부.true : 가능false : 불가능 |
| ┗ detail | Array | 충전소 충전기 세부 정보. |
| ┣ name | String | 충전소 보유 충전기 이름.(type1 기준 해당 순으로 정렬)06:DC차데모 AC3상 DC콤보03:DC차데모 AC3상05:DC차데모 DC콤보01:DC차데모07:AC3상04:DC콤보02:완속 |
| ┣ charger\_ok\_count | Integer | 충전기 충전 가능 상태 개수 |
| ┗ charger\_total\_count | Integer | 충전기 전체 개수 |
| ┣ eventlist\_cnt | Integer | 유고정보 목록 개수 |
| ┣ event\_list | Array | 유고정보 목록 |
| ┣ comment | String | 부가 설명 (이벤트 설명) |
| ┣ latitude | String | 위도(WGS 84좌표, 10micro degree) |
| ┣ longitude | String | 경도(WGS 84좌표, 10micro degree) |
| ┣ rtm\_table\_num | Integer | TPEG RTM Table 번호 |
| ┗ rtm\_code\_num | Integer | TPEG RTM Code 번호 |
| ┣ vvms\_cnt | Integer | VVMS 개수 |
| ┣ vvms\_list | Array | VVMS 리스트 |
| ┣ dpx | String | display X좌표(WGS84의 경우 longitude) |
| ┣ dpy | String | display Y좌표(WGS84의 경우 latitude) |
| ┣ id | String | 도로정보 id |
| ┣ mapid | String | MAP ID |
| ┣ direction | Integer | 0 : 경로역방향1 : 경로 진행방향 |
| ┗ linkid | String | LINK ID |
| ┣ smart\_vvms\_cnt | Integer | VVMS 개수 |
| ┣ smart\_vvms\_list | Array | VVMS 리스트 |
| ┣ id | String | 도로정보 id |
| ┣ type | Integer | VVMS 타입 0:일반 1:홍수 2:산사태 3:호우 |
| ┣ d\_level | String | VVMS 재난 레벨(type이 1,2,3일 때)  01:경보 발령 02:심각단계 발령 |
| ┣ vType | Integer | VVMS 음성 표출 타입0:미표출1:돌발2:사고 |
| ┣ m\_x | String | 메시지 display X좌표 |
| ┣ m\_y | String | 메시지 display Y좌표 |
| ┣ m\_mapid | String | 메시지 MAP ID |
| ┣ m\_linkid | String | 메시지 LINK ID |
| ┣ m\_direction | Integer | 메시지 DIRECTION0 : 경로 역방향1 : 경로 진행방향 |
| ┣ e\_x | String | 이벤트 display X좌표 |
| ┣ e\_y | String | 이벤트 display Y좌표 |
| ┣ e\_mapid | String | 이벤트 MAP ID |
| ┣ e\_linkid | String | 이벤트 LINK ID |
| ┗ e\_direction | Integer | 이벤트 DIRECTION0 : 경로 역방향1 : 경로 진행방향 |

## 일반 경로 리스트 탐색
> Confluence page id: 2262309604 · 최종 수정: 10월 01, 2026

### Function

> 일반 경로 리스트 탐색

### URL

> `/findListRoute`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| searchOptions | List\<String\> | O | Agent 탐색 종류agt\_recommend : 추천경로 (LGU+ 향으로는 “빠른길”)agt\_short\_time : 최소시간real\_traffic\_freeroad : 무료도로short\_distance\_priority : 최단거리highway\_priority : 고속도로우선motorcycle : 이륜차 이용도로beginner : 초보자(편한길) (LGU+ 향으로는 “편한길”)recommendation : 엔진기반 추천경로(agt\_recommend 대체)time\_priority : 엔진기반 최소시간(agt\_short\_time 대체) |
| avoidSchoolZone | String |  | 스쿨존 회피(searchOption)0:회피 안함(Default)1:회피 |
| ignoreTimeRestrictedZone | String |  | 시간제 통행 규제 무시 0: 무시안함(Default) 1: 무시 |
| useHighwayProjectionStart | String |  | 출발지 고속도로, 자동차전용, 도시고속 회피 0: 회피 안함(Default) 1: 회피 |
| useHighwayProjectionEnd | String |  | 목적지 고속도로, 자동차전용, 도시고속 회피 0: 회피 안함(Default) 1: 회피 |
| mrVersion | String | O | MR version |
| searchType | String | O | 탐색종류0: 일반탐색4: MYWAY(특정대교)5: 테마도로6: MYCCTV7: 통계탐색 |
| directivity | boolean |  | 목적지 방향성 탐색true : 사용false : 사용안함(default) |
| rotate | boolean |  | 회전규제 고려 탐색true : 사용false : 사용안함(default) |
| dual | boolean |  | 경로선 이원화(가상 분리된 경로선)true : 사용false : 사용안함(default) |
| forced | boolean |  | 도로상 통행 제한지점 강제통과true : 사용false : 사용안함(default) |
| searchString | String |  | 검색어(검색어가 사용되는 기능을 통한 탐색시)(Log) |
| inMethod | INTEGER |  | 경로탐색을 호출한 기능(Log)0: 통합검색1: 최근검색어3: 즐겨찾기4: 이전목적지6: 타임머신7: AI를통한 호출(AI플래그와 타 플래그가 동시에 적용되는 시나리오에서는 구분자 '/'로 같이 보내주어야함) |
| routeOpt\_sub | String |  | 경로옵션(대교탐색/해안도로/구간비교/주행중탐색 인 경우만)(Log) BRDG 대교탐색SHORE 해안도로REROUTE 주행중탐색 |
| routeOpt\_sub\_name | String |  | 대교탐색 인 경우 해당 대교의 이름(Log) |
| curPosType (LogApi = startPosType) | String |  | 출발지가 GPS 3D Fix 시의 위치인지의 여부GPS(Log)  GPS 에서 수신된 위치 OTHER GPS 에서 수신된 위치가 아닌 위치를 사용하거나 유저가 출발지를 지정한 경우 |
| category | Array |  | 선호주유소 카테고리 코드 리스트 |
| ┗ val | String |  | [[inavi-air-api-data#Category Code\|Category Code]]C0100 : 주유소(default) |
| oil | String |  | 유종 0: 휘발유 1: 고급휘발유 2: 경유 3: LPG 4: 전기(EV) 5: 수소 |
| startloc | Object | O | 출발지 지점 정보 |
| ┣ lonx | String | O | 출발지 경도, 정규화좌표 X값 |
| ┣ laty | String | O | 출발지 위도, 정규화좌표 Y값 |
| ┣ pid | String |  | 위치의 PID(startPos 에서는 PID 생략 가능)(Log) |
| ┣ name | String | O | 출발지 명칭 |
| ┣ mapid | String | O | 출발지 도엽번호 |
| ┣ linkid | String | O | 출발지 링크번호 |
| ┣ nodeid | String | O | 출발지 노드번호 |
| ┣ direction | String | O | 출발지 방향 |
| ┣ usingName | boolean |  | 지점명칭 사용true : 사용(default)false : 사용안함 |
| ┣ usingHideViaLoc | boolean |  | 숨김 경유지true : 사용false : 사용안함(default) |
| ┣ viaLocStart | boolean |  | 경유도로 시작true : 사용false : 사용안함(default) |
| ┗ viaLocEnd | boolean |  | 경유도로 종료true : 사용false : 사용안함(default) |
| endloc | Object | O | 도착지 지점 정보 |
| ┣ lonx | String | O | 도착지 경도, 정규화좌표 X값 |
| ┣ laty | String | O | 도착지 위도, 정규화좌표 Y값 |
| ┣ pid | String |  | 위치의 PID(endloc 에서는 PID 생략 가능)(Log) |
| ┣ ctrIdx1 | String |  | 도착지 PID에 대한 CTR 검색 결과 idx1 정보(Log) |
| ┣ ctrIdx2\_1 | String |  | 도착지 PID에 대한 CTR 검색 결과 idx2-1 정보(Log) |
| ┣ ctrIdx2\_2 | String |  | 도착지 PID에 대한 CTR 검색 결과 idx2-2 정보(Log) |
| ┣ ctrSortFlag | String |  | 도착지 PID에 대한 CTR 검색 결과 sort flag 정보(Log) 정렬순서:DIST 거리순ACCU 정확도순 |
| ┣ name | String | O | 도착지 명칭 |
| ┣ mapid | String | O | 도착지 도엽번호 |
| ┣ linkid | String | O | 도착지 링크번호 |
| ┣ nodeid | String | O | 도착지 노드번호 |
| ┣ direction | String | O | 도착지 방향 |
| ┣ usingName | boolean |  | 지점명칭 사용true : 사용(default)false : 사용안함 |
| ┣ usingHideViaLoc | boolean |  | 숨김 경유지true : 사용false : 사용안함(default) |
| ┣ viaLocStart | boolean |  | 경유도로 시작/종료true : 사용false : 사용안함(default) |
| ┗ viaLocEnd | boolean |  | 경유도로 종료true : 사용false : 사용안함(default) |
| vialocList | Array |  | 경유지 지점 정보 |
| ┣ lonx | String |  | 경유지 경도, 정규화좌표 X값 |
| ┣ laty | String |  | 경유지 위도, 정규화좌표 Y값 |
| ┣ pid | String |  | 위치의 PID(endloc 에서는 PID 생략 가능)(Log) |
| ┣ ctrIdx1 | String |  | 도착지 PID에 대한 CTR 검색 결과 idx1 정보(Log) |
| ┣ ctrIdx2\_1 | String |  | 도착지 PID에 대한 CTR 검색 결과 idx2-1 정보(Log) |
| ┣ ctrIdx2\_2 | String |  | 도착지 PID에 대한 CTR 검색 결과 idx2-2 정보(Log) |
| ┣ ctrSortFlag | String |  | 도착지 PID에 대한 CTR 검색 결과 sort flag 정보(Log) 정렬순서:DIST 거리순ACCU 정확도순 |
| ┣ name | String |  | 경유지 명칭 |
| ┣ mapid | String |  | 경유지 도엽번호 |
| ┣ linkid | String |  | 경유지 링크번호 |
| ┣ nodeid | String |  | 경유지 노드번호 |
| ┣ direction | String |  | 경유지 방향 |
| ┣ usingName | boolean |  | 지점명칭 사용true : 사용(default)false : 사용안함 |
| ┣ usingHideViaLoc | boolean |  | 숨김 경유지true : 사용false : 사용안함(default) |
| ┣ viaLocStart | boolean |  | 경유도로 시작/종료true : 사용false : 사용안함(default) |
| ┗ viaLocEnd | boolean |  | 경유도로 종료true : 사용false : 사용안함(default) |
| extensionList | Array |  | 확장 리스트 |
| ┣ headerType | String |  | 확장 리스트 타입1: 다중목적지 최적탐색2: 지나간 톨게이트3: 사용자정보5: 경유도로6: 유고회피7: 경로회피 13 : 교통정보 세부 설정 |
| ┣ routepoints | Array |  | 다중목적지 리스트 (when headerType is 1) |
| ┣ rpx | String |  | 목적지 X좌표 |
| ┗ rpy | String |  | 목적지 Y좌표 |
| ┣ tollList | Array |  | 톨게이트 정보 리스트 (when headerType is 2) |
| ┣ tolltype | String |  | 톨게이트 Type |
| ┗ tollidx | String |  | 톨게이트 index |
| ┣ userInput | Object |  | 사용자 입력 정보 (when headerType is 3) |
| ┣ height | String |  | 높이(단위:Cm) |
| ┣ weight | String |  | 중량(단위:kg) |
| ┣ hipass | boolean |  | 하이패스 소지true: 소지false: 미소지 |
| ┣ over3 | boolean |  | 3인이상true: 3인이상false: 3인이하 |
| ┣ zonelimit | boolean |  | 상수원 보호구역 진입 제한 차량true: 제한false: 미제한 |
| ┣ cartype | String |  | 차종0: 1종(승용/승합/화물)1: 2종(승합/화물)2: 3종(승합/화물)3: 4종(화물)4: 5종(화물)5: 6종 경차 |
| ┣ dishigh | String |  | 고속도로 통행료 할인0: 없음1: 50%할인2: 면제 |
| ┗ disjam | String |  | 혼잡 통행료 할인0: 없음1: 50%할인2: 면제 |
| ┣ viaRoadList | Array |  | 경유도로 리스트 (when headerType is 5) |
| ┗ viaRoadlinkList | Array |  | 경유도로 Link 리스트 |
| ┣ mapid | String |  | 도엽 번호 |
| ┗ linkid | String |  | 링크 번호 |
| ┣ eventList | Array |  | 유고회피 리스트 (when headerType is 6) |
| ┗ eid | String |  | 유고정보 고유번호 |
| ┣ evasList | Array |  | 경로회피 리스트 (when headerType is 7) |
| ┣ mapid | String |  | 도엽 번호 |
| ┣ linkid | String |  | 링크 번호 |
| ┣ nodeid | String |  | 노드 번호 |
| ┣ ext | String |  | 부가 정보 |
| ┗ linkposition | String |  | 링크 포지션 |
| ┗ trafficSetting | Object |  | 교통정보 세부 설정탐색 (when headerType is 13) |
| ┗ trafficUnflag | boolean |  | 교통정보 미사용 여부 true : 미사용 (삼성 중공업) false : 사용 (Default) |
| timestamp | String |  | 로그주행 탐색시작 시간 EX) 1689567848 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| routeList | Array | 경로탐색 결과 리스트\*searchOption2가 입력 된 경우 2개, 입력 되지 않은 경우 1개의 리스트 반환 |
| ┣ result\_code | String | [[inavi-air-api-common#결과 코드\|결과코드]] |
| ┣ result\_msg | String | 결과코드에 따른 메세지 |
| ┣ rid | String | 경로 ID\*리스트가 다수 인 경우 다른 리스트와 동일한 rid가 응답 될 수 있음 |
| ┣ option\_type | String | Agent 탐색 종류agt\_recommend : 에이전트추천agt\_short\_time : 최소시간real\_traffic\_freeroad : 무료도로short\_distance\_priority : 최단거리highway\_priority : 고속도로우선motorcycle : 이륜차 이용도로recommendation : 엔진기반 추천경로(agt\_recommend 대체)time\_priority : 엔진기반 최소시간(agt\_short\_time 대체)\*주의: 재탐색 시 rdata의 url을 통해 받은 탐색 파일에 명시 되어 있는 탐색 옵션을 재탐색 시 searchOption 항목에 전달 하여야 함 |
| ┣ rdata | String | 경로 Data URI |
| ┣ gdata | String | 안내 Data URI |
| ┣ tdata | String | 교통정보 Data URI |
| ┣ poi | Object | 최저가주유소 검색결과 |
| ┣ catecode | String | 분류코드 |
| ┣ dpx | String | display X좌표(WGS84의 경우 longitude) |
| ┣ dpy | String | display Y좌표(WGS84의 경우 latitude) |
| ┗ oildata | Object | 유가 데이터 정보 |
| ┣ g\_price | Integer | 휘발유 가격 |
| ┣ g\_least | Integer | 최저 휘발유 가격제공 Flag(0: 아님 1: 맞음) |
| ┣ hg\_price | Integer | 고급휘발유 가격 |
| ┣ hg\_least | Integer | 최저 고급휘발유 가격제공 Flag(0: 아님 1: 맞음) |
| ┣ d\_price | Integer | 경유 가격 |
| ┣ d\_least | Integer | 최저 경유 가격제공 Flag(0: 아님 1: 맞음) |
| ┣ l\_price | Integer | LPG 가격 |
| ┣ l\_least | Integer | 최저 LPG 가격제공 Flag(0: 아님 1: 맞음) |
| ┗ updatetime | String | Update 시간 |
| ┣ eventlist\_cnt | Integer | 유고정보 목록 개수 |
| ┣ event\_list | Array | 유고정보 목록 |
| ┣ comment | String | 부가 설명 (이벤트 설명) |
| ┣ latitude | String | 위도(WGS 84좌표, 10micro degree) |
| ┣ longitude | String | 경도(WGS 84좌표, 10micro degree) |
| ┣ rtm\_table\_num | Integer | TPEG RTM Table 번호 |
| ┗ rtm\_code\_num | Integer | TPEG RTM Code 번호 |
| ┣ vvms\_cnt | Integer | VVMS 개수 |
| ┣ vvms\_list | Array | VVMS 리스트 |
| ┣ dpx | String | display X좌표(WGS84의 경우 longitude) |
| ┣ dpy | String | display Y좌표(WGS84의 경우 latitude) |
| ┣ id | String | 도로정보 id |
| ┣ mapid | String | MAP ID |
| ┗ linkid | String | LINK ID |
| ┣ smart\_vvms\_cnt | Integer | VVMS 개수 |
| ┗ smart\_vvms\_list | Array | VVMS 리스트 |
| ┣ id | String | 도로정보 id |
| ┣ type | Integer | VVMS 타입 0:일반 1:홍수 2:산사태 3:호우 |
| ┣ d\_level | String | VVMS 재난 레벨(type이 1,2,3일 때)  01:경보 발령 02:심각단계 발령 |
| ┣ vType | Integer | VVMS 음성 표출 타입0:미표출1:돌발2:사고 |
| ┣ m\_x | String | 메시지 display X좌표 |
| ┣ m\_y | String | 메시지 display Y좌표 |
| ┣ m\_mapid | String | 메시지 MAP ID |
| ┣ m\_linkid | String | 메시지 LINK ID |
| ┣ m\_direction | Integer | 메시지 DIRECTION0 : 경로 역방향1 : 경로 진행방향 |
| ┣ e\_x | String | 이벤트 display X좌표 |
| ┣ e\_y | String | 이벤트 display Y좌표 |
| ┣ e\_mapid | String | 이벤트 MAP ID |
| ┣ e\_linkid | String | 이벤트 LINK ID |
| ┗ e\_direction | Integer | 이벤트 DIRECTION0 : 경로 역방향1 : 경로 진행방향 |
| timestamp | String | 로그주행 탐색시작 시간 EX) 1689567848 |

## 경로 재 탐색
> Confluence page id: 2262309516 · 최종 수정: 10월 01, 2026

### Function

> 경로 재 탐색

### URL

> `/findRouteAgain`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| searchOption | String | O | Agent 탐색 종류agt\_recommend : 에이전트추천agt\_short\_time : 최소시간real\_traffic : 빠르고real\_traffic2 : 편하고real\_traffic\_comfortable : 더편하고real\_traffic\_freeroad : 무료도로short\_distance\_priority : 최단거리highway\_priority : 고속도로우선motorcycle : 이륜차 이용도로beginner : 초보자recommendation : 엔진기반 추천경로time\_priority : 엔진기반 최소시간\* 추천, 최소시간은 스마트재탐색 사용안함으로 설정 |
| searchOptionOrg | String |  | Agent 탐색 종류(사용자가 선택한 추천/최소 탐색 옵션)recommendation : 엔진기반 추천경로(agt\_recommend 대체)time\_priority : 엔진기반 최소시간(agt\_short\_time 대체) |
| avoidSchoolZone | String |  | 스쿨존 회피0:회피 안함(Default)1:회피 |
| ignoreTimeRestrictedZone | String |  | 시간제 통행 규제 무시 0: 무시안함(Default) 1: 무시 |
| useHighwayProjectionStart | String |  | 출발지 고속도로, 자동차전용, 도시고속 회피 0: 회피 안함(Default) 1: 회피 |
| useHighwayProjectionEnd | String |  | 목적지 고속도로, 자동차전용, 도시고속 회피 0: 회피 안함(Default) 1: 회피 |
| mrVersion | String | O | MR version |
| searchType | String | O | 탐색종류1 : 일반재탐색2 : 교통재탐색3 : 이탈재탐색 |
| smart | boolean | O | 스마트재탐색 여부true : 사용false : 사용안함(default) |
| 제목 없음 |  |  |  |
| rid | String | O | 경로파일 ID |
| 제목 없음 |  |  |  |
| remainTime | String | O | 남은시간 (초)smart:true일 경우 remainTime이 일정 시간 이내이면 121(동일경로) 리턴 발생 할 수 있음 |
| remainDistance | String | O | 남은거리 (M) |
| currentPosition | String | O | 경로파일에서 현재위치 링크인덱스 |
| directivity | boolean |  | 목적지 방향성 탐색true : 사용false : 사용안함(default) |
| rotate | boolean |  | 회전규제 고려 탐색true : 사용false : 사용안함(default) |
| dual | boolean |  | 경로선 이원화(가상 분리된 경로선)true : 사용false : 사용안함(default) |
| forced | boolean |  | 도로상 통행 제한지점 강제통과true : 사용false : 사용안함(default) |
| category | Array |  | 선호주유소 카테고리 코드 리스트 |
| ┗ val | String |  | [[inavi-air-api-data#Category Code\|Category Code]]C0100 : 주유소(default) |
| oil | String |  | 유종 0: 휘발유 1: 고급휘발유 2: 경유 3: LPG 4: 전기(EV) 5: 수소 |
| baseUrl | String |  | 코드42 요청 URL |
| startloc | Object | O | 출발지 지점 정보 |
| ┣ lonx | String | O | 출발지 경도, 정규화좌표 X값 |
| ┣ laty | String | O | 출발지 위도, 정규화좌표 Y값 |
| ┣ name | String | O | 출발지 명칭 |
| ┣ mapid | String | O | 출발지 도엽번호 |
| ┣ linkid | String | O | 출발지 링크번호 |
| ┣ nodeid | String | O | 출발지 노드번호 |
| ┣ direction | String | O | 출발지 방향 |
| ┣ angle | String |  | 정북 기준 도로 진행 방향(코드42) |
| ┣ usingName | boolean |  | 지점명칭 사용true : 사용(default)false : 사용안함 |
| ┣ usingHideViaLoc | boolean |  | 숨김 경유지true : 사용false : 사용안함(default) |
| ┣ viaLocStart | boolean |  | 경유도로 시작/종료true : 사용false : 사용안함(default) |
| ┗ viaLocEnd | boolean |  | 경유도로 종료true : 사용false : 사용안함(default) |
| endloc | Object | O | 도착지 지점 정보 |
| ┣ lonx | String | O | 도착지 경도, 정규화좌표 X값 |
| ┣ laty | String | O | 도착지 위도, 정규화좌표 Y값 |
| ┣ name | String | O | 도착지 명칭 |
| ┣ mapid | String | O | 도착지 도엽번호 |
| ┣ linkid | String | O | 도착지 링크번호 |
| ┣ nodeid | String | O | 도착지 노드번호 |
| ┣ direction | String | O | 도착지 방향 |
| ┣ usingName | boolean |  | 지점명칭 사용true : 사용(default)false : 사용안함 |
| ┣ usingHideViaLoc | boolean |  | 숨김 경유지true : 사용false : 사용안함(default) |
| ┣ viaLocStart | boolean |  | 경유도로 시작/종료true : 사용false : 사용안함(default) |
| ┗ viaLocEnd | boolean |  | 경유도로 종료true : 사용false : 사용안함(default) |
| vialocList | Array |  | 경유지 지점 정보 |
| ┣ lonx | String |  | 경유지 경도, 정규화좌표 X값 |
| ┣ laty | String |  | 경유지 위도, 정규화좌표 Y값 |
| ┣ name | String |  | 경유지 명칭 |
| ┣ mapid | String |  | 경유지 도엽번호 |
| ┣ linkid | String |  | 경유지 링크번호 |
| ┣ nodeid | String |  | 경유지 노드번호 |
| ┣ direction | String |  | 경유지 방향 |
| ┣ usingName | boolean |  | 지점명칭 사용true : 사용(default)false : 사용안함 |
| ┣ usingHideViaLoc | boolean |  | 숨김 경유지true : 사용false : 사용안함(default) |
| ┣ viaLocStart | boolean |  | 경유도로 시작/종료true : 사용false : 사용안함(default) |
| ┗ viaLocEnd | boolean |  | 경유도로 종료true : 사용false : 사용안함(default) |
| extensionList | Array |  | 확장 리스트 |
| ┣ headerType | String |  | 확장 리스트 타입1: 다중목적지 최적탐색2: 지나간 톨게이트3: 사용자정보4: 통계탐색5: 경유도로6: 유고회피7: 경로회피 13 : 교통정보 세부 설정 |
| ┣ routepoints | Array |  | 다중목적지 리스트 (when headerType is 1) |
| ┣ rpx | String |  | 목적지 X좌표 |
| ┗ rpy | String |  | 목적지 Y좌표 |
| ┣ tollList | Array |  | 톨게이트 정보 리스트 (when headerType is 2) |
| ┣ tolltype | String |  | 톨게이트 Type |
| ┗ tollidx | String |  | 톨게이트 index |
| ┣ userInput | Object |  | 사용자 입력 정보 (when headerType is 3) |
| ┣ height | String |  | 높이(단위:Cm) |
| ┣ weight | String |  | 중량(단위:kg) |
| ┣ hipass | boolean |  | 하이패스 소지true: 소지false: 미소지 |
| ┣ over3 | boolean |  | 3인이상true: 3인이상false: 3인이하 |
| ┣ zonelimit | boolean |  | 상수원 보호구역 진입 제한 차량true: 제한false: 미제한 |
| ┣ cartype | String |  | 차종0: 1종(승용/승합/화물)1: 2종(승합/화물)2: 3종(승합/화물)3: 4종(화물)4: 5종(화물)5: 6종 경차 |
| ┣ dishigh | String |  | 고속도로 통행료 할인0: 없음1: 50%할인2: 면제 |
| ┗ disjam | String |  | 혼잡 통행료 할인0: 없음1: 50%할인2: 면제 |
| ┣ viaRoadList | Array |  | 경유도로 리스트 (when headerType is 5) |
| ┗ viaRoadlinkList | Array |  | 경유도로 Link 리스트 |
| ┣ mapid | String |  | 도엽 번호 |
| ┗ linkid | String |  | 링크 번호 |
| ┣ eventList | Array |  | 유고회피 리스트 (when headerType is 6) |
| ┗ eid | String |  | 유고정보 고유번호 |
| ┣ evasList | Array |  | 경로회피 리스트 (when headerType is 7) |
| ┣ mapid | String |  | 도엽 번호 |
| ┣ linkid | String |  | 링크 번호 |
| ┣ nodeid | String |  | 노드 번호 |
| ┣ ext | String |  | 부가 정보 |
| ┗ linkposition | String |  | 링크 포지션 |
| ┗ userSetting | Object |  | 사용자 설정 정보 반영 탐색 (when headerType is 11) |
| ┣ rheightlimit | boolean |  | 도로 통과 높이 제한 기능 사용 true: 사용 false: 미사용 |
| ┣ rweightlimit | boolean |  | 도로 통과 중량 제한 기능 사용 true: 사용 false: 미사용 |
| ┣ zonelimit | boolean |  | 상수원 보호구역 진입 제한 유무 true: 제한 false: 미제한 |
| ┣ sevasion | boolean |  | 좁은길 회피 기능 사용 true: 사용 false: 미사용 |
| ┣ uevasion | boolean |  | 유턴 회피 기능 사용 true: 사용 false: 미사용 |
| ┣ frevasion | boolean |  | 화물차 통행제한 구간 회피 기능 사용 true: 사용 false: 미사용 |
| ┣  mevasion | boolean |  | 위수지역 회피 기능 사용 true: 사용 false: 미사용 |
| ┣ height | String |  | 차량 높이(단위:Cm) |
| ┣ weight | String |  | 차량 중량(단위:kg) |
| ┣ nroadevasion | String |  | 왕복 n 차선 이하 도로 회피 |
| ┗ nuturnevasion | String |  | 왕복 n 차선 이하 유턴 회피 |
| ┗ trafficSetting | Object |  | 교통정보 세부 설정탐색 (when headerType is 13) |
| ┗ trafficUnflag | boolean |  | 교통정보 미사용 여부 true : 미사용 (삼성 중공업) false : 사용 (Default) |
| opt | String |  | 재탐색이 발생한 상황(Log) SMRT 스마트재탐색 (예외 시나리오 제외하고는 5분마다 한번씩) SHORE 해안도로 탐색 DIFF 구간비교 탐색 NORM 이탈 PROUTE 이전경로 (경로가 있는 상태에서 앱 종료 후 재시작시) AI AI를통한 호출 CHOPT 주행중 옵션변경 UNDEF 미정의 |
| timestamp | String |  | 로그주행 탐색시작 시간 EX) 1689567848 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| option\_type | String | Agent 탐색 종류agt\_recommend : 에이전트추천agt\_short\_time : 최소시간real\_traffic\_freeroad : 무료도로short\_distance\_priority : 최단거리highway\_priority : 고속도로우선motorcycle : 이륜차 이용도로\*주의: 재탐색 시 rdata의 url을 통해 받은 탐색 파일에 명시 되어 있는 탐색 옵션을 재탐색 시 searchOption 항목에 전달 하여야 함 |
| rid | String | 경로 ID |
| rdata | String | 경로 Data URI |
| gdata | String | 안내 Data URI |
| tdata | String | 교통정보 Data URI |
| poi | Object | 최저가주유소 검색결과 |
| ┣ catecode | String | 분류코드 |
| ┣ dpx | String | display X좌표(WGS84의 경우 longitude) |
| ┣ dpy | String | display Y좌표(WGS84의 경우 latitude) |
| ┗ oildata | Object | 유가 데이터 정보 |
| ┣ g\_price | Integer | 휘발유 가격 |
| ┣ g\_least | Integer | 최저 휘발유 가격제공 Flag(0: 아님 1: 맞음) |
| ┣ hg\_price | Integer | 고급휘발유 가격 |
| ┣ hg\_least | Integer | 최저 고급휘발유 가격제공 Flag(0: 아님 1: 맞음) |
| ┣ d\_price | Integer | 경유 가격 |
| ┣ d\_least | Integer | 최저 경유 가격제공 Flag(0: 아님 1: 맞음) |
| ┣ l\_price | Integer | LPG 가격 |
| ┣ l\_least | Integer | 최저 LPG 가격제공 Flag(0: 아님 1: 맞음) |
| ┗ updatetime | String | Update 시간 |
| eventlist\_cnt | Integer | 유고정보 목록 개수 |
| event\_list | Array | 유고정보 목록 |
| ┣ comment | String | 부가 설명 (이벤트 설명) |
| ┣ latitude | String | 위도(WGS 84좌표, 10micro degree) |
| ┣ longitude | String | 경도(WGS 84좌표, 10micro degree) |
| ┣ rtm\_table\_num | Integer | TPEG RTM Table 번호 |
| ┗ rtm\_code\_num | Integer | TPEG RTM Code 번호 |
| vvms\_cnt | Integer | VVMS 개수 |
| vvms\_list | Array | VVMS 리스트 |
| ┣ dpx | String | display X좌표(WGS84의 경우 longitude) |
| ┣ dpy | String | display Y좌표(WGS84의 경우 latitude) |
| ┣ id | String | 도로정보 id |
| ┣ mapid | String | MAP ID |
| ┣ direction | Integer | 0 : 경로역방향1 : 경로 진행방향 |
| ┗ linkid | String | LINK ID |
| smart\_vvms\_cnt | Integer | VVMS 개수 |
| smart\_vvms\_list | Array | VVMS 리스트 |
| ┣ id | String | 도로정보 id |
| ┣ type | Integer | VVMS 타입 0:일반 1:홍수 2:산사태 3:호우 |
| ┣ d\_level | String | VVMS 재난 레벨(type이 1,2,3일 때)  01:경보 발령 02:심각단계 발령 |
| ┣ vType | Integer | VVMS 음성 표출 타입0:미표출1:돌발2:사고 |
| ┣ m\_x | String | 메시지 display X좌표 |
| ┣ m\_y | String | 메시지 display Y좌표 |
| ┣ m\_mapid | String | 메시지 MAP ID |
| ┣ m\_linkid | String | 메시지 LINK ID |
| ┣ m\_direction | Integer | 메시지 DIRECTION0 : 경로 역방향1 : 경로 진행방향 |
| ┣ e\_x | String | 이벤트 display X좌표 |
| ┣ e\_y | String | 이벤트 display Y좌표 |
| ┣ e\_mapid | String | 이벤트 MAP ID |
| ┣ e\_linkid | String | 이벤트 LINK ID |
| ┗ e\_direction | Integer | 이벤트 DIRECTION0 : 경로 역방향1 : 경로 진행방향 |

## 요약결과 경로 탐색
> Confluence page id: 2262309584 · 최종 수정: 10월 01, 2026

### Function

> 요약결과 경로 탐색

### URL

> `/findSummaryRoute`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| searchOption | String | O | Agent 탐색 종류real\_traffic : 빠르고 |
| avoidSchoolZone | String |  | 스쿨존 회피(searchOption)0:회피 안함(Default)1:회피 |
| ignoreTimeRestrictedZone | String |  | 시간제 통행 규제 무시 0: 무시안함(Default) 1: 무시 |
| useHighwayProjectionStart | String |  | 출발지 고속도로, 자동차전용, 도시고속 회피 0: 회피 안함(Default) 1: 회피 |
| useHighwayProjectionEnd | String |  | 목적지 고속도로, 자동차전용, 도시고속 회피 0: 회피 안함(Default) 1: 회피 |
| mrVersion | String | O | MR version |
| searchType | String | O | 탐색종류0: 일반탐색 |
| directivity | boolean |  | 목적지 방향성 탐색true : 사용false : 사용안함(default) |
| rotate | boolean |  | 회전규제 고려 탐색true : 사용false : 사용안함(default) |
| dual | boolean |  | 경로선 이원화(가상 분리된 경로선)true : 사용false : 사용안함(default) |
| forced | boolean |  | 도로상 통행 제한지점 강제통과true : 사용false : 사용안함(default) |
| startloc | Object | O | 출발지 지점 정보 |
| ┣ lonx | String | O | 출발지 경도, 정규화좌표 X값 |
| ┣ laty | String | O | 출발지 위도, 정규화좌표 Y값 |
| ┣ name | String | O | 출발지 명칭 |
| ┣ mapid | String | O | 출발지 도엽번호 |
| ┣ linkid | String | O | 출발지 링크번호 |
| ┣ nodeid | String | O | 출발지 노드번호 |
| ┣ direction | String | O | 출발지 방향 |
| ┣ usingName | boolean |  | 지점명칭 사용true : 사용(default)false : 사용안함 |
| ┣ usingHideViaLoc | boolean |  | 숨김 경유지true : 사용false : 사용안함(default) |
| ┣ viaLocStart | boolean |  | 경유도로 시작true : 사용false : 사용안함(default) |
| ┗ viaLocEnd | boolean |  | 경유도로 종료true : 사용false : 사용안함(default) |
| endloc | Object | O | 도착지 지점 정보 |
| ┣ lonx | String | O | 도착지 경도, 정규화좌표 X값 |
| ┣ laty | String | O | 도착지 위도, 정규화좌표 Y값 |
| ┣ name | String | O | 도착지 명칭 |
| ┣ mapid | String | O | 도착지 도엽번호 |
| ┣ linkid | String | O | 도착지 링크번호 |
| ┣ nodeid | String | O | 도착지 노드번호 |
| ┣ direction | String | O | 도착지 방향 |
| ┣ usingName | boolean |  | 지점명칭 사용true : 사용(default)false : 사용안함 |
| ┣ usingHideViaLoc | boolean |  | 숨김 경유지true : 사용false : 사용안함(default) |
| ┣ viaLocStart | boolean |  | 경유도로 시작/종료true : 사용false : 사용안함(default) |
| ┗ viaLocEnd | boolean |  | 경유도로 종료true : 사용false : 사용안함(default) |
| vialocList | Array |  | 경유지 지점 정보 |
| ┣ lonx | String |  | 경유지 경도, 정규화좌표 X값 |
| ┣ laty | String |  | 경유지 위도, 정규화좌표 Y값 |
| ┣ name | String |  | 경유지 명칭 |
| ┣ mapid | String |  | 경유지 도엽번호 |
| ┣ linkid | String |  | 경유지 링크번호 |
| ┣ nodeid | String |  | 경유지 노드번호 |
| ┣ direction | String |  | 경유지 방향 |
| ┣ usingName | boolean |  | 지점명칭 사용true : 사용(default)false : 사용안함 |
| ┣ usingHideViaLoc | boolean |  | 숨김 경유지true : 사용false : 사용안함(default) |
| ┣ viaLocStart | boolean |  | 경유도로 시작/종료true : 사용false : 사용안함(default) |
| ┗ viaLocEnd | boolean |  | 경유도로 종료true : 사용false : 사용안함(default) |
| extensionList | Array |  | 확장 리스트 |
| ┣ headerType | String |  | 확장 리스트 타입1: 다중목적지 최적탐색2: 지나간 톨게이트3: 사용자정보5: 경유도로6: 유고회피7: 경로회피 13 : 교통정보 세부 설정 |
| ┣ routepoints | Array |  | 다중목적지 리스트 (when headerType is 1) |
| ┣ rpx | String |  | 목적지 X좌표 |
| ┗ rpy | String |  | 목적지 Y좌표 |
| ┣ tollList | Array |  | 톨게이트 정보 리스트 (when headerType is 2) |
| ┣ tolltype | String |  | 톨게이트 Type |
| ┗ tollidx | String |  | 톨게이트 index |
| ┣ userInput | Object |  | 사용자 입력 정보 (when headerType is 3) |
| ┣ height | String |  | 높이(단위:Cm) |
| ┣ weight | String |  | 중량(단위:kg) |
| ┣ hipass | boolean |  | 하이패스 소지true: 소지false: 미소지 |
| ┣ over3 | boolean |  | 3인이상true: 3인이상false: 3인이하 |
| ┣ zonelimit | boolean |  | 상수원 보호구역 진입 제한 차량true: 제한false: 미제한 |
| ┣ cartype | String |  | 차종0: 1종(승용/승합/화물)1: 2종(승합/화물)2: 3종(승합/화물)3: 4종(화물)4: 5종(화물)5: 6종 경차 |
| ┣ dishigh | String |  | 고속도로 통행료 할인0: 없음1: 50%할인2: 면제 |
| ┗ disjam | String |  | 혼잡 통행료 할인0: 없음1: 50%할인2: 면제 |
| ┣ viaRoadList | Array |  | 경유도로 리스트 (when headerType is 5) |
| ┗ viaRoadlinkList | Array |  | 경유도로 Link 리스트 |
| ┣ mapid | String |  | 도엽 번호 |
| ┗ linkid | String |  | 링크 번호 |
| ┣ eventList | Array |  | 유고회피 리스트 (when headerType is 6) |
| ┗ eid | String |  | 유고정보 고유번호 |
| ┣ evasList | Array |  | 경로회피 리스트 (when headerType is 7) |
| ┣ mapid | String |  | 도엽 번호 |
| ┣ linkid | String |  | 링크 번호 |
| ┣ nodeid | String |  | 노드 번호 |
| ┣ ext | String |  | 부가 정보 |
| ┗ linkposition | String |  | 링크 포지션 |
| ┗ userSetting | Object |  | 사용자 설정 정보 반영 탐색 (when headerType is 11) |
| ┣ rheightlimit | boolean |  | 도로 통과 높이 제한 기능 사용 true: 사용 false: 미사용 |
| ┣ rweightlimit | boolean |  | 도로 통과 중량 제한 기능 사용 true: 사용 false: 미사용 |
| ┣ zonelimit | boolean |  | 상수원 보호구역 진입 제한 유무 true: 제한 false: 미제한 |
| ┣ sevasion | boolean |  | 좁은길 회피 기능 사용 true: 사용 false: 미사용 |
| ┣ uevasion | boolean |  | 유턴 회피 기능 사용 true: 사용 false: 미사용 |
| ┣ frevasion | boolean |  | 화물차 통행제한 구간 회피 기능 사용 true: 사용 false: 미사용 |
| ┣  mevasion | boolean |  | 위수지역 회피 기능 사용 true: 사용 false: 미사용 |
| ┣ height | String |  | 차량 높이(단위:Cm) |
| ┣ weight | String |  | 차량 중량(단위:kg) |
| ┣ nroadevasion | String |  | 왕복 n 차선 이하 도로 회피 |
| ┗ nuturnevasion | String |  | 왕복 n 차선 이하 유턴 회피 |
| ┗ trafficSetting | Object |  | 교통정보 세부 설정탐색 (when headerType is 13) |
| ┗ trafficUnflag | boolean |  | 교통정보 미사용 여부 true : 미사용 (삼성 중공업) false : 사용 (Default) |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| distance | Integer | 경로 길이(단위: M) |
| time | Integer | 예상 소요 시간(단위: 초) |

## 타임머신(시간예측)
> Confluence page id: 2262309698 · 최종 수정: 10월 01, 2026

### Function

> 타임머신(시간예측)

### URL

> `/findStatRoute`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| searchOption | String | O | Agent 탐색 종류real\_traffic : 빠르고 |
| mrVersion | String | O | MR version |
| searchType | String | O | 탐색종류7: 통계탐색 |
| directivity | boolean |  | 목적지 방향성 탐색true : 사용false : 사용안함(default) |
| rotate | boolean |  | 회전규제 고려 탐색true : 사용false : 사용안함(default) |
| dual | boolean |  | 경로선 이원화(가상 분리된 경로선)true : 사용false : 사용안함(default) |
| forced | boolean |  | 도로상 통행 제한지점 강제통과true : 사용false : 사용안함(default) |
| startloc | Object | O | 출발지 지점 정보 |
| ┣ lonx | String | O | 출발지 경도, 정규화좌표 X값 |
| ┣ laty | String | O | 출발지 위도, 정규화좌표 Y값 |
| ┣ pid | String |  | 위치의 PID(startloc 에서는 PID 생략 가능)(Log) |
| ┣ name | String | O | 출발지 명칭 |
| ┣ mapid | String | O | 출발지 도엽번호 |
| ┣ linkid | String | O | 출발지 링크번호 |
| ┣ nodeid | String | O | 출발지 노드번호 |
| ┣ direction | String | O | 출발지 방향 |
| ┣ usingName | boolean |  | 지점명칭 사용true : 사용(default)false : 사용안함 |
| ┣ usingHideViaLoc | boolean |  | 숨김 경유지true : 사용false : 사용안함(default) |
| ┣ viaLocStart | boolean |  | 경유도로 시작/종료true : 사용false : 사용안함(default) |
| ┗ viaLocEnd | boolean |  | 경유도로 종료true : 사용false : 사용안함(default) |
| endloc | Object | O | 도착지 지점 정보 |
| ┣ lonx | String | O | 도착지 경도, 정규화좌표 X값 |
| ┣ laty | String | O | 도착지 위도, 정규화좌표 Y값 |
| ┣ name | String | O | 도착지 명칭 |
| ┣ pid | String |  | 위치의 PID(endloc 에서는 PID 생략 가능)(Log) |
| ┣ mapid | String | O | 도착지 도엽번호 |
| ┣ linkid | String | O | 도착지 링크번호 |
| ┣ nodeid | String | O | 도착지 노드번호 |
| ┣ direction | String | O | 도착지 방향 |
| ┣ usingName | boolean |  | 지점명칭 사용true : 사용(default)false : 사용안함 |
| ┣ usingHideViaLoc | boolean |  | 숨김 경유지true : 사용false : 사용안함(default) |
| ┣ viaLocStart | boolean |  | 경유도로 시작/종료true : 사용false : 사용안함(default) |
| ┗ viaLocEnd | boolean |  | 경유도로 종료true : 사용false : 사용안함(default) |
| vialocList | Array |  | 경유지 지점 정보 |
| ┣ lonx | String |  | 경유지 경도, 정규화좌표 X값 |
| ┣ laty | String |  | 경유지 위도, 정규화좌표 Y값 |
| ┣ name | String |  | 경유지 명칭 |
| ┣ pid | String |  | 위치의 PID(vialocList 에서는 PID 생략 가능)(Log) |
| ┣ mapid | String |  | 경유지 도엽번호 |
| ┣ linkid | String |  | 경유지 링크번호 |
| ┣ nodeid | String |  | 경유지 노드번호 |
| ┣ direction | String |  | 경유지 방향 |
| ┣ usingName | boolean |  | 지점명칭 사용true : 사용(default)false : 사용안함 |
| ┣ usingHideViaLoc | boolean |  | 숨김 경유지true : 사용false : 사용안함(default) |
| ┣ viaLocStart | boolean |  | 경유도로 시작/종료true : 사용false : 사용안함(default) |
| ┗ viaLocEnd | boolean |  | 경유도로 종료true : 사용false : 사용안함(default) |
| extensionList | Array | O | 확장 리스트 |
| ┣ headerType | String | O | 확장 리스트 타입1: 다중목적지 최적탐색2: 지나간 톨게이트3: 사용자정보4: 통계탐색5: 경유도로6: 유고회피7: 경로회피 13 : 교통정보 세부 설정 |
| ┣ routepoints | Array |  | 다중목적지 리스트 (when headerType is 1) |
| ┣ rpx | String |  | 목적지 X좌표 |
| ┗ rpy | String |  | 목적지 Y좌표 |
| ┣ tollList | Array |  | 톨게이트 정보 리스트 (when headerType is 2) |
| ┣ tolltype | String |  | 톨게이트 Type |
| ┗ tollidx | String |  | 톨게이트 index |
| ┣ userInput | Object |  | 사용자 입력 정보 (when headerType is 3) |
| ┣ height | String |  | 높이(단위:Cm) |
| ┣ weight | String |  | 중량(단위:kg) |
| ┣ hipass | boolean |  | 하이패스 소지true: 소지false: 미소지 |
| ┣ over3 | boolean |  | 3인이상true: 3인이상false: 3인이하 |
| ┣ zonelimit | boolean |  | 상수원 보호구역 진입 제한 차량true: 제한false: 미제한 |
| ┣ cartype | String |  | 차종0: 1종(승용/승합/화물)1: 2종(승합/화물)2: 3종(승합/화물)3: 4종(화물)4: 5종(화물)5: 6종 경차 |
| ┣ dishigh | String |  | 고속도로 통행료 할인0: 없음1: 50%할인2: 면제 |
| ┗ disjam | String |  | 혼잡 통행료 할인0: 없음1: 50%할인2: 면제 |
| ┣ statRoute | Object | O | 통계 탐색 (when headerType is 4) |
| ┣ serviceType | String | O | 서비스 구분0: 도착시간예측1: 출발시간예측 |
| ┣ beforeCount | String | O | 기준시간 전시간 탐색 개수 |
| ┣ afterCount | String | O | 기준시간 후시간 탐색 개수 |
| ┣ routeInfoFlag | boolean | O | Response에 경로정보 포함여부true: 포함false: 미포함 |
| ┣ interval | String | O | 60 ≤ Interval (단위 : 초) |
| ┗ targetTime | String | O | 기준 시간(UTC 기준의 TimeStamp)serviceType 0일경우 출발시간serviceType 1일경우 도착시간 |
| ┣ viaRoadList | Array |  | 경유도로 리스트 (when headerType is 5) |
| ┗ viaRoadlinkList | Array |  | 경유도로 Link 리스트 |
| ┣ mapid | String |  | 도엽 번호 |
| ┗ linkid | String |  | 링크 번호 |
| ┣ eventList | Array |  | 유고회피 리스트 (when headerType is 6) |
| ┗ eid | String |  | 유고정보 고유번호 |
| ┣ evasList | Array |  | 경로회피 리스트 (when headerType is 7) |
| ┣ mapid | String |  | 도엽 번호 |
| ┣ linkid | String |  | 링크 번호 |
| ┣ nodeid | String |  | 노드 번호 |
| ┣ ext | String |  | 부가 정보 |
| ┗ linkposition | String |  | 링크 포지션 |
| ┗ `trafficSetting` | Object |  | 교통정보 세부 설정탐색 (when headerType is 13) |
| ┗ `trafficUnflag` | boolean |  | 교통정보 미사용 여부 true : 미사용 (삼성 중공업) false : 사용 (Default) |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| time\_count | Integer | 예측시간 개수 |
| time\_list | Array | 예측시간 리스트 |
| ┣ start\_time | String | 출발시간 (TimeStamp) |
| ┗ end\_time | String | 도착시간 (TimeStamp) |

## 경로 내 유고 정보
> Confluence page id: 2262309492 · 최종 수정: 10월 01, 2026

### Function

> 경로 내 유고 정보

### URL

> `/routeRoadEvent`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| rid | String | O | 경로 ID |
| version | String | O | Map version |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| eventlist\_cnt | Integer | 유고정보 목록 개수 |
| event\_list | Array | 유고정보 목록 |
| ┣ critical\_rate | Integer | 심각도 (0x00: 미확인) |
| ┣ create\_time | Integer | 생성시간 – 메시지 생성시간(UTC) |
| ┣ start\_time | Integer | 시작시간 – 이벤트 시작 시간(UTC) |
| ┣ end\_time | Integer | 종료시간 – 이벤트 종료 시간(UTC) |
| ┣ available\_time | Integer | 유효시간 (없을 경우 0x00) |
| ┣ repeat\_time | Integer | 반복시간 (0\~23 값을 사용, 없을 경우 0xff) |
| ┣ repeat\_minute | Integer | 반복 분(0\~9값을 사용, 없을 경우 0xff) |
| ┣ day\_of\_week | Integer | 요일정보 (월\~일을 1bit단위로 셋팅) |
| ┣ accident\_count | Integer | 사고건수 (사고가 아닌 경우 0x00) |
| ┣ accident\_vehicle\_count | Integer | 사고 차량 수 (사고가 아닌경우 0x00) |
| ┣ speed\_average | Integer | 평균속도 (km/hour 속도) – 유형코드 5번 교통망 상태 이벤트에서 사용 |
| ┣ delay\_time | Integer | 지체시간 (초 단위) – 유형코드 5번 교통망 상태 이벤트에서 사용 |
| ┣ speed\_limit | Integer | 제한속도 (km/hour 속도) – 유형코드 5번 교통망 상태 이벤트에서 사용 |
| ┣ type\_code | Integer | 유고 유형코드 |
| ┣ accident\_name | String | 유고 정보 명칭 |
| ┣ interval | Integer | 구간길이 (100m 단위의 길이) |
| ┣ road\_name | String | 도로명 |
| ┣ road\_interval\_name | String | 도로 구간명 |
| ┣ weather | Integer | 날씨(TPEG RTM 29의 Code값) |
| ┣ lane\_info | Integer | 차선정보 (TPEG RTM 테이블 10의 Code값) |
| ┣ sight\_distance | Integer | 시야 거리(100m 단위) |
| ┣ comment | String | 부가 설명 (이벤트 설명) |
| ┣ tpeg\_link\_id | Long | TPEG 링크 ID |
| ┣ link\_id\_list | Array | 영향 받는 링크 ID리스트 |
| ┗ link\_id | String | 영향 받는 링크 ID |
| ┣ latitude | String | 위도(WGS 84좌표, 10micro degree) |
| ┣ longitude | String | 경도(WGS 84좌표, 10micro degree) |
| ┣ rtm\_table\_num | Integer | TPEG RTM Table 번호 |
| ┣ rtm\_code\_num | Integer | TPEG RTM Code 번호 |
| ┣ mrlinkinfo\_list | Array | MR Link 목록 |
| ┣ mapid | Integer | Map ID |
| ┗ linkid | Integer | Link ID |

## 전체 유고 정보 조회
> Confluence page id: 2262309654 · 최종 수정: 10월 01, 2026

### Function

> 전체 유고 정보 조회

### URL

> `/fullRoadEvent`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| lutst | String |  | 수신한 Last Update Time Stamp 값(기본값: 0) |
| version | String | O | Map version |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| eventlist\_cnt | Integer | 유고정보 목록 개수 |
| event\_list | Array | 유고정보 목록 |
| ┣ critical\_rate | Integer | 심각도 (0x00: 미확인) |
| ┣ create\_time | Integer | 생성시간 – 메시지 생성시간(UTC) |
| ┣ start\_time | Integer | 시작시간 – 이벤트 시작 시간(UTC) |
| ┣ end\_time | Integer | 종료시간 – 이벤트 종료 시간(UTC) |
| ┣ available\_time | Integer | 유효시간 (없을 경우 0x00) |
| ┣ repeat\_time | Integer | 반복시간 (0\~23 값을 사용, 없을 경우 0xff) |
| ┣ repeat\_minute | Integer | 반복 분(0\~9값을 사용, 없을 경우 0xff) |
| ┣ day\_of\_week | Integer | 요일정보 (월\~일을 1bit단위로 셋팅) |
| ┣ accident\_count | Integer | 사고건수 (사고가 아닌 경우 0x00) |
| ┣ accident\_vehicle\_count | Integer | 사고 차량 수 (사고가 아닌경우 0x00) |
| ┣ speed\_average | Integer | 평균속도 (km/hour 속도) – 유형코드 5번 교통망 상태 이벤트에서 사용 |
| ┣ delay\_time | Integer | 지체시간 (초 단위) – 유형코드 5번 교통망 상태 이벤트에서 사용 |
| ┣ speed\_limit | Integer | 제한속도 (km/hour 속도) – 유형코드 5번 교통망 상태 이벤트에서 사용 |
| ┣ type\_code | Integer | 유고 유형코드 |
| ┣ accident\_name | String | 유고 정보 명칭 |
| ┣ interval | Integer | 구간길이 (100m 단위의 길이) |
| ┣ road\_name | String | 도로명 |
| ┣ road\_interval\_name | String | 도로 구간명 |
| ┣ weather | Integer | 날씨(TPEG RTM 29의 Code값) |
| ┣ lane\_info | Integer | 차선정보 (TPEG RTM 테이블 10의 Code값) |
| ┣ sight\_distance | Integer | 시야 거리(100m 단위) |
| ┣ comment | String | 부가 설명 (이벤트 설명) |
| ┣ tpeg\_link\_id | Long | TPEG 링크 ID |
| ┣ link\_id\_list | Array | 영향 받는 링크 ID리스트 |
| ┗ link\_id | String | 영향 받는 링크 ID |
| ┣ latitude | String | 위도(WGS 84좌표, 10micro degree) |
| ┣ longitude | String | 경도(WGS 84좌표, 10micro degree) |
| ┣ rtm\_table\_num | Integer | TPEG RTM Table 번호 |
| ┗ rtm\_code\_num | Integer | TPEG RTM Code 번호 |

## 경로 주변 부가 정보
> Confluence page id: 2262309540 · 최종 수정: 10월 01, 2026

### Function

> 경로 주변 부가 정보

### URL

> `/routeOtherInfo`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| rid | String | O | 경로 ID |
| xpos | String | O | 시작점 정규화 X 좌표 |
| ypos | String | O | 시작점 정규화 Y 좌표 |
| cctvOn | Boolean | O | CCTV 정보true: 사용(default)false: 미사용 |
| oilOn | Boolean |  | 주유소 정보true: 사용(default)false: 미사용 |
| evcOn | Boolean |  | 전기차 중전소 정보true: 사용false: 미사용(default) |
| eventOn | Boolean |  | 유고 정보true: 사용(default)false: 미사용 |
| vvmsOn | Boolean |  | VVMS 정보true: 사용(default)false: 미사용 |
| disasterOn | Boolean |  | 재난 정보true: 사용(default)false: 미사용 |
| disasterCarOn | Boolean |  | 긴급출동 차량 위치 정보true: 사용(default)false: 미사용 |
| category | Array |  | 선호주유소 카테고리 코드 리스트 |
| ┗ val | String |  | [[inavi-air-api-data#Category Code\|Category Code]]C0100 : 주유소(default) |
| oil | String |  | 유종0:ALL (default)1:휘발유2:고급휘발유3:경유4:LPG |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| cctv\_cnt | Integer | CCTV 개수 |
| cctv\_list | Array | CCTV 리스트 |
| ┣ dpx | String | display X좌표(WGS84의 경우 longitude) |
| ┣ dpy | String | display Y좌표(WGS84의 경우 latitude) |
| ┣ mapid | String | 맵 아이디 |
| ┣ linkid | String | 링크 아이디 |
| ┣ direction | Integer | 0 : 경로역방향, 1 : 경로 진행방향 |
| ┣ cctvdata | Object | CCTV 정보 |
| ┣ cctv\_id | String | CCTV ID |
| ┗ cctv\_name | String | CCTV 명칭 |
| oil\_cnt | Integer | 주유소 개수 |
| oil\_list | Array | 주유소 리스트 |
| ┣ name1 | String | 정식명칭 |
| ┣ catecode | String | 분류코드 |
| ┣ dpx | String | display X좌표(WGS84의 경우 longitude) |
| ┣ dpy | String | display Y좌표(WGS84의 경우 latitude) |
| ┣ mapid | String | 맵 아이디 |
| ┣ linkid | String | 링크 아이디 |
| ┣ direction | Integer | 0 : 경로역방향, 1 : 경로 진행방향 |
| ┣ roadtype | String | 도로타입 |
| ┗ oildata | Object | 유가 데이터 정보 |
| ┣ g\_price | Integer | 휘발유 가격 |
| ┣ g\_least | Integer | 최저 휘발유 가격제공 Flag(0: 아님 1: 맞음) |
| ┣ hg\_price | Integer | 고급휘발유 가격 |
| ┣ hg\_least | Integer | 최저 고급휘발유 가격제공 Flag(0: 아님 1: 맞음) |
| ┣ d\_price | Integer | 경유 가격 |
| ┣ d\_least | Integer | 최저 경유 가격제공 Flag(0: 아님 1: 맞음) |
| ┣ l\_price | Integer | LPG 가격 |
| ┣ l\_least | Integer | 최저 LPG 가격제공 Flag(0: 아님 1: 맞음) |
| ┗ updatetime | String | Update 시간 |
| event\_cnt | Integer | 유고 개수 |
| event\_list | Array | 유고 리스트 |
| ┣ dpx | String | display X좌표(WGS84의 경우 longitude) |
| ┣ dpy | String | display Y좌표(WGS84의 경우 latitude) |
| ┣ id | String | 도로정보 id |
| ┣ mapid | String | MAP ID |
| ┣ linkid | String | LINK ID |
| ┗ direction | Integer | 0 : 경로역방향, 1 : 경로 진행방향 |
| vvms\_cnt | Integer | VVMS 개수 |
| vvms\_list | Array | VVMS 리스트 |
| ┣ dpx | String | display X좌표(WGS84의 경우 longitude) |
| ┣ dpy | String | display Y좌표(WGS84의 경우 latitude) |
| ┣ id | String | 도로정보 id |
| ┣ mapid | String | MAP ID |
| ┣ linkid | String | LINK ID |
| ┗ direction | Integer | 0 : 경로역방향, 1 : 경로 진행방향 |
| disaster\_cnt | Integer | 재난정보 개수 |
| disaster\_list | Array | 재난정보 리스트 |
| ┣ dpx | String | display X좌표(WGS84의 경우 longitude) |
| ┣ dpy | String | display Y좌표(WGS84의 경우 latitude) |
| ┣ id | String | 도로정보 id |
| ┣ mapid | String | MAP ID |
| ┣ linkid | String | LINK ID |
| ┗ direction | Integer | 0 : 경로역방향, 1 : 경로 진행방향 |
| disasterCar\_cnt | Integer | 긴출출동 차량 위치 개수 |
| disasterCar\_list | Array | 긴출출동 차량 위치 리스트 |
| ┣ dpx | String | display X좌표(WGS84의 경우 longitude) |
| ┣ dpy | String | display Y좌표(WGS84의 경우 latitude) |
| ┣ id | String | 도로정보 id |
| ┣ mapid | String | MAP ID |
| ┣ linkid | String | LINK ID |
| ┗ direction | Integer | 0 : 경로역방향, 1 : 경로 진행방향 |
| evc\_cnt | Integer | 전기차 충전소 개수 |
| evc\_list | Array | 전기차 충전소 리스트 |
| ┣ name1 | String | 정식명칭 |
| ┣ catecode | String | 분류코드 |
| ┣ dpx | String | display X좌표(WGS84의 경우 longitude) |
| ┣ dpy | String | display Y좌표(WGS84의 경우 latitude) |
| ┣ mapid | String | 맵 아이디 |
| ┣ linkid | String | 링크 아이디 |
| ┣ direction | Integer | 0 : 경로역방향, 1 : 경로 진행방향 |
| ┣ roadtype | String | 도로타입 |
| ┗ evcstation | Object | [[inavi-air-api-data#전기차 충전소 정보\|전기차충전소정보]] |

## 대중교통 요약 길찾기
> Confluence page id: 2262309564 · 최종 수정: 10월 01, 2026

### Function

> 대중교통 요약 길찾기

### URL

> `/summaryPath`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| list | Array |  | 확장 리스트 |
| ┣ startPos | Object |  | 출발지 정보 |
| ┣ dPosX | Double |  | 출발지 좌표 X |
| ┣ dPosY | Double |  | 출발지 좌표 Y |
| ┗ name | String |  | 출발지 명칭 |
| ┣ endPos | Object |  | 도착지 정보 (재탐색시 사용) |
| ┣ dPosX | Double |  | 도착지 좌표 X |
| ┣ dPosY | Double |  | 도착지 좌표 Y |
| ┗ name | String |  | 도착지 명칭(최근검색에서 사용) |
| ┗ coordType | Integer |  | request/response 좌표 타입GEOGRAPHIC = 0(wgs84 고정값 0으로 채워보내시면됨) |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| list | Array | 출발지 정보(요청때 보낸 순서대로 리스트 정렬) |
| ┣ huResult | Integer | 휴빌론으로부터온 응답값(좌표체계 및 좌표값틀릴경우 정상으로안주는 케이스 존재)0 : 정상30 : 대중교통 서버의 서비스 지역이 아닙니다(아래값들 0으로 채워짐)1 : 비정상(비정상일경우 아래 값들 0으로 채워짐) |
| ┣ routeArea | Integer | 0 : 도시 내1 : 도시 간 |
| ┣ routeOpt | Integer | 결과 수단별 타입(0:도보, 1:지하철, 2:버스, 3:버스+지하철, 4:기차, 5:고속버스, 6:항공, 7:시외버스) |
| ┣ totalTime | Integer | 총 소요시간 (분) |
| ┗ totalDistance | Integer | 전체 거리 (m) |

## 탐색 유고정보 조회
> Confluence page id: 2262309678 · 최종 수정: 10월 01, 2026

### Function

> 탐색 유고정보 조회

### URL

> `/routingEvent`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| type | Integer | O | 요청 타입0 : 전체 1 : 특정 링크 |
| mrVersion | String | O | MR version |
| routeEveneList | List | O | ※ 요청 타입이 1인 경우에만 존재 |
| ┣ mapid | Short | O | MAP ID |
| ┣ linkid | Short | O | LINK ID |
| ┗ direction | Short | O | Direction※ 0 : 정 1: 역 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| request\_type | Integer | 요청 타입 |
| info\_count | Integer | 유고정보 개수 |
| link\_count | Integer | 요청링크 개수 |
| resultLink\_data | Object | 요청링크 매칭 정보※ 요청 타입이 1인 경우에만 존재 |
| ┣ mapid | String | MAP ID |
| ┣ linkid | String | LINK ID |
| ┣ direction | String | Direction※ 0 : 정 1: 역 |
| ┣ existence | String | 유고 존재 유무※ 0 : 없음 1: 있음 |
| ┗ seiral\_number | String | 유고 고유 번호 |
| resultInfo\_data | Object | 유고 정보 |
| ┣ type | String | 유고 타입 |
| ┣ seiral\_number | String | 유고 고유 번호 |
| ┣ start\_date | String | 시작시간(Timestamp - GMT) |
| ┣ end\_date | String | 종료시간(Timestamp - GMT) |
| ┣ latitude | String | 경도좌표 |
| ┣ longitude | String | 위도좌표 |
| ┣ roadname | String | 도로명 |
| ┣ subject | String | 제목 |
| ┣ detail\_content | String | 상세 설명 |
| ┣ preparing\_person | String | 작성자 |
| ┣ regulate\_flag | String | 통제유뮤0 : 통제없음 1 : 전면통제 2: 부분통제 |
| ┣ regulate\_day | String | 통제요일start\_date ... end\_date 기간 중 부분 통제 요일※ regulate\_flag 가 부분통제일 경우에만 존재 |
| ┣ regulate\_hour | String | 통제시작 시간start\_date ... end\_date 기간 중 부분 통제 요일 중 통제 시작 시간※ regulate\_flag 가 부분통제일 경우에만 존재 |
| ┣ regulate\_time | String | 통제시간(분)regulate\_hour 시간으로 부터 regulate\_tim(분)만큼 통제※ regulate\_flag 가 부분통제일 경우에만 존재 |
| ┣ addtion\_info | String | 부가정보 (속도)전면통제가 아닌 경우의 링크 속도※ 전면통제의 경우 : 255(고정값) |
| ┣ affect\_count | String | Affect 링크 개수 |
| ┗ affect\_list | List | Affect 링크 #0 ... #N※ Affrect 링크 개수만큼 존재 |

## Sources

- Confluence "INAVI AIR API" > 탐색 (2026-10-27 조회): 탐색 (2262309456), 일반 경로 탐색 (2262309630), 일반 경로 리스트 탐색 (2262309604), 경로 재 탐색 (2262309516), 요약결과 경로 탐색 (2262309584), 타임머신(시간예측) (2262309698), 경로 내 유고 정보 (2262309492), 전체 유고 정보 조회 (2262309654), 경로 주변 부가 정보 (2262309540), 대중교통 요약 길찾기 (2262309564), 탐색 유고정보 조회 (2262309678)
