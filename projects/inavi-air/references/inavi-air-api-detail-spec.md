---
title: >-
    INAVI AIR API 상세 명세 (허브)
category: references
tags: [inavi-air, api, endpoint, visibility/internal]
aliases: [API 상세명세, INAVI AIR API 상세, INAVI AIR API]
relationships:
  - target: "[[inavi-air-api-overview]]"
    type: derived_from
sources: ["~/Develop/Wiki/_raw/articles/project-air/API 상세명세.md", "url:https://inavisystems.atlassian.net/wiki/spaces/AS/pages/2262305475"]
summary: >-
    Confluence "INAVI AIR API"(API Specification 스페이스)를 영역별 위키 페이지 27개로 원문 그대로 옮긴 허브. API 150개의 URL과 위치를 찾는다.
provenance:
  extracted: 0.95
  inferred: 0.05
  ambiguous: 0.00
base_confidence: 0.75
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: core
created: 2026-10-26T09:14:00+09:00
updated: 2026-10-27T11:00:00+09:00
snapshots:
  - "[[_raw/_archived/API 상세명세|API 상세명세]]"
---

# INAVI AIR API 상세 명세 (허브)

Confluence "API Specification" 스페이스의 "INAVI AIR API" 페이지 아래 문서(공통, API, DATA, 하위 페이지 198개)를 **필드 단위까지 원문 그대로** 영역별 페이지로 옮겼다(2026-10-27 조회). 각 API 절에는 Confluence page id가 있어 원본과 1:1로 대조할 수 있다. 서버 주소, 키, 작성자 이름처럼 보안 규칙상 옮길 수 없는 값만 `[HOST]`, `[URL]`, `[KEY_REMOVED]` 등으로 가렸다. 공통 규칙 요약은 [[inavi-air-api-overview]], 소속 프로젝트는 [[inavi-air]]이다.

## 공통·데이터

| 영역 | 위키 페이지 | 내용 |
|---|---|---|
| 공통 (AIR) | [[inavi-air-api-common]] | 서버연동정보(구조만), Request Header, 결과 코드, 공통 정보, Push 정보, Push Type 정보, Popup 정보(원본 본문 없음) |
| DATA (AIR) | [[inavi-air-api-data]] | Category Code, 방향코드, POI_DATA_A, POI_DATA_B, 경로 주변 POI 정보, 전기차 충전소 정보 |

## API 영역 (25개, API 150개)

| 영역 | 위키 페이지 | API 수 | URL |
|---|---|---|---|
| 탐색 | [[inavi-air-api-route]] | 10 | `/findMultiRoute`, `/findListRoute`, `/findRouteAgain`, `/findSummaryRoute`, `/findStatRoute`, `/routeRoadEvent`, `/fullRoadEvent`, `/routeOtherInfo`, `/summaryPath`, `/routingEvent` |
| 검색 | [[inavi-air-api-search]] | 18 | `/sire/searchCctv`, `/sire/searchRoad`, `/sire/searchReference`, `/sire/searchPoiDetail`, `/sire/searchSubpoi`, `/sire/searchPoiNumber`, `/sire/searchSQE`, `/sire/searchRouteAroundMulti`, `/multiSearchProposer`, `/sire/searchTism`, `/sire/searchOldAddr`, `/sire/searchPoiAround`, 새 주소 검색(원본 URL 없음), `/sire/revgeocoding`, `/sire/optimalPosition`, `/sire/searchProposer`, `/sire/searchSubAddrRoadName`, `/sire/searchSubAddr` |
| 즐겨찾기 | [[inavi-air-api-favorites]] | 15 | `/regPointInsert`, `/regPointUpdate`, `/regPointDelete`, `/regPointsync`, `/moveRegPoint`, `/makeLabel`, `/updateLabel`, `/deleteLabel`, `/insertRegToLabel`, `/deleteLabelData`, `/resetLabel`, `/airRegpointUM`, `/regPointInsertUM`, `/regPointUpdateUM`, `/regPointDeleteUM` |
| 로그 | [[inavi-air-api-log]] | 4 | `/userEvent`, `/uploadDrivingLog`, `/uploadAiLog`, `/uploadAirlabLog` |
| 이벤트 | [[inavi-air-api-event]] | 7 | `/event`, `/event/cash/earn`, `/event/cash/voucherExchange`, `/luckyBoxOpen`, `/luckyBoxList`, `/getLuckyProductList`, `/getLuckyBoxStatus` |
| 기타 | [[inavi-air-api-etc]] | 31 | SNS 계정(`/snsLogin`, `/snsCheck`, `/snsTransLogin`, `/snsLogout`, `/snsMemberInfoInsert`, `/signout`, `/integratedSignout`), 주행 이력(`/drivingHis*`), `/saveConfig`, `/latelyPoiList*`, `/extendedMap`, `/extendedNewMap`, `/directionVoice`, `/searchOilStation`, `/bridgeList`, `/roadEventDetail`, `/cctvInfo`, `/emergencyDetail`, `/confusionLane`, `/simpleReport`, `/roadAcdntNotiSos`, `/mileageHisInsert`, `/snsInfoMigration*` |
| RRIS | [[inavi-air-api-rris]] | 3 | `/rris/data/currentLoc`, `/rris/data/saveRoute`, `/rris/event/upEmergency` |
| 에어 캐시 | [[inavi-air-api-air-cash]] | 16 | `/cashInfo`, `/cashSave`, `/cashStampInfo`, `/cashStampSave`, `/cashStampRouletteGame`, `/cashStampRouletteTicket`, `/stampHistory`, `/stampComplete`, `/roulette`, `/airCashHistory`, `/productList`, `/productDetail`, `/couponPurchase`, `/couponBox`, `/couponBoxDetail`, `/couponResend` |
| w3w | [[inavi-air-api-w3w]] | 2 | `/w3w/autoSuggest`, `/w3w/wordSearch` |
| 캐시버튼 (Only Android) | [[inavi-air-api-cash-button]] | 1 | `/cashButton/cashConversion` |
| HUD | [[inavi-air-api-hud]] | 1 | `/authSerialNumber` |
| 신호등 | [[inavi-air-api-traffic-light]] | 3 | `/trafficLightList`, `/trafficLightStatus`, `/trafficLightWalker` |
| 음성광고 | [[inavi-air-api-onair-voice-ad]] | 4 | `/onAirListenStart`, `/onAirListenFinish`, `/onAirVoiceFileInfo`, `/onAirDailyCount` |
| 메인화면 | [[inavi-air-api-main-screen]] | 3 | `/mainPageData`, `/weather`, `/fortuneBirthCheck` |
| 그룹주행 | [[inavi-air-api-group-driving]] | 4 | `/makeGroup`, `/groupUpdate`, `/groupDrivingHis`, `/rris/data/currentLoc` |
| 오픈POI | [[inavi-air-api-open-poi]] | 3 | `/makeOpenPoi`, `/getOpenPoi`, `/searchOpenPoi` |
| AIR 서비스 | [[inavi-air-api-air-service]] | 4 | `/serviceGate`, `/clauseAgree`, `/clauseCheck`, `/mapDownloadInfo` |
| AIR 나의주행 | [[inavi-air-api-my-driving]] | 4 | `/weeklyMyHabit`, `/myDailyDrivingList`, `/drivingHabitDetail`, `/monthlyMyDriving` |
| LOG-AIR | [[inavi-air-api-log-air]] | 1 | `/reportLog` |
| 제보하기 | [[inavi-air-api-report]] | 2 | `/report/insert`(상위 페이지 본문), `/report/read` |
| 통계 | [[inavi-air-api-statistics]] | 4 | `/statistics/totalUser`, `/statistics/drivingHistory`, `/statistics/cashedUser`, `/statistics/newUser` |
| 오르다 | [[inavi-air-api-orda]] | 1 | `/orda/stamp` |
| 삼성중공업 전용 API | [[inavi-air-api-shi]] | 3 | `/saveDrivStopInfo`, `/saveTFlimitInfo`, `/saveDisasterInfo` |
| 삼성중공업 SDK | [[inavi-air-api-shi-sdk]] | 5 | `/shiSdk/sendShiGps`, `/shiSdk/getDrivStopInfo`, `/shiSdk/getTFlimitInfo`, `/shiSdk/getStopAreaInfo`, `/shiSdk/getDisasterInfo` |
| SKP 전용 API | [[inavi-air-api-skp]] | 1 | `/event/cash/postback` |

`/findListRoute` 등의 `searchOptions`(`agt_recommend`, `agt_short_time`, `real_traffic_freeroad`, `short_distance_priority`, `highway_priority`, `motorcycle`, `beginner`, `recommendation`, `time_priority`)와 스쿨존 회피 같은 옵션은 탐색 엔진의 확장 기능([[inavi-routing-neon-protocol]])과 대응한다. ^[inferred]

## 원본 상태 메모

- 원본에 본문이 없는 페이지: Popup 정보, 서버연동정보 > 개발·상용, POI 하위시설물 조회의 하위 필드 페이지 5개, 에어연구소 로그의 `result_code`·`result_msg` 하위 페이지. 하단 팝업 배너·팝업 공지 필드는 `/serviceGate` 응답(`banner_list`, `banner_end_list`, `popup_list`, `param_yn`)에 있다([[inavi-air-api-air-service#서비스 메인(AIR)|서비스 메인]]).
- 원본 Request Parameter 표가 빈 API는 각 페이지에 "원본 표가 비어 있음"으로 표시했다. 원본 오타와 열 순서 오류도 고치지 않았다.
- Confluence "참고 문서"의 "스토어 사용자 리뷰", "에어 서비스 활성 지표"(2022년 7~8월 DAU/MAU)는 API 명세가 아니라 옮기지 않았다.
- 이전 Notion 덤프(`_raw/_archived/API 상세명세.md`)는 `/serviceGate` 등 일부 응답 표가 "결과 없음"으로 빠져 있었다. Confluence 판이 기준이다.

## Open Questions

- `새 주소 검색`은 Confluence 원본에도 URL 칸이 비어 있다. ^[ambiguous]
- `/rris/data/currentLoc`는 RRIS와 그룹주행 두 영역에 같은 명세(요청 23행, 응답 19행)로 나온다. 같은 API를 공용으로 쓴다. ^[inferred]

## Sources

- Confluence "API Specification" > "INAVI AIR API" (page id 2262305475), 하위 "공통 (AIR)" 2273968161, "API (AIR)" 2274197535, "DATA (AIR)" 2273214571 (2026-10-27 조회)
- [[_raw/_archived/API 상세명세.md]] — 이전 Notion 덤프(일부 응답 누락)
