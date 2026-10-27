---
title: >-
    INAVI AIR API 상세 명세 (엔드포인트 목록)
category: references
tags: [inavi-air, api, endpoint, visibility/internal]
aliases: [API 상세명세, INAVI AIR API 상세]
relationships:
  - target: "[[inavi-air-api-overview]]"
    type: derived_from
sources: [~/Develop/Wiki/_raw/articles/project-air/API 상세명세.md]
summary: >-
    INAVI AIR API 약 140개 엔드포인트를 23개 영역으로 나눠 URL과 용도를 찾아보게 만든 색인. 필드 단위 스펙은 원본을 본다.
provenance:
  extracted: 0.90
  inferred: 0.10
  ambiguous: 0.00
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T09:14:00+09:00
updated: 2026-10-26T09:14:00+09:00
snapshots:
  - "[[_raw/_archived/API 상세명세|API 상세명세]]"
---

# INAVI AIR API 상세 명세 (엔드포인트 색인)

원본(약 10,800줄)은 각 API의 Function, URL, Request Header/Parameter, Response 필드를 모두 담고 있다. 이 페이지는 원본 전체를 옮기지 않고 **엔드포인트 URL과 용도 색인**으로 정리했다. 공통 헤더와 결과 코드는 [[inavi-air-api-overview]], 소속 프로젝트는 [[inavi-air]]이다. 필드 단위가 필요하면 원본의 해당 `##` 제목을 찾는다.

## 1. 탐색 (경로)

| 용도 | URL |
|---|---|
| 일반 경로 리스트 탐색 | `/findListRoute` |
| 일반 경로 탐색 | `/findMultiRoute` |
| 경로 재탐색 | `/findRouteAgain` |
| 요약결과 경로 탐색 | `/findSummaryRoute` |
| 타임머신(시간예측) | `/findStatRoute` |
| 경로 내 유고 / 전체 유고 | `/routeRoadEvent`, `/fullRoadEvent` |
| 경로 주변 부가 정보 | `/routeOtherInfo` |
| 대중교통 요약 길찾기 | `/summaryPath` |
| 탐색 유고정보 조회 | `/routingEvent` |

`/findListRoute`의 `searchOptions`는 `agt_recommend`(추천, LG U+ 향은 "빠른길"), `agt_short_time`(최소시간), `real_traffic_freeroad`(무료도로), `short_distance_priority`(최단거리), `highway_priority`(고속도로 우선), `motorcycle`(이륜차), `beginner`(초보자/편한길), `recommendation`·`time_priority`(엔진 기반, 각각 `agt_recommend`·`agt_short_time`을 대체)를 받는다. 스쿨존 회피(`avoidSchoolZone`), 시간제 통행 규제 무시(`ignoreTimeRestrictedZone`) 같은 옵션도 있다. 이 옵션들은 탐색 엔진의 확장 기능([[inavi-routing-neon-protocol]])과 대응한다. ^[inferred]

## 2. 검색

`/sire/` 아래에 모여 있다: `searchOldAddr`(구 주소), `revgeocoding`(좌표→주소), `searchSubAddr`·`searchSubAddrRoadName`(하위 행정계), `searchPoiNumber`(POI 명칭), `searchSQE`(통합검색), `searchPoiDetail`, `searchPoiAround`, `searchSubpoi`, `searchReference`, `searchProposer`(추천어), `searchRouteAroundMulti`(경로 주변 다중 카테고리), `searchTism`(교통정보 요약맵), `searchRoad`·`searchCctv`(CCTV), `optimalPosition`(최적 지적). 대중교통 추천어 초성 검색은 `/multiSearchProposer`다.

## 3. 즐겨찾기

추가/수정/삭제는 `/regPointInsert`, `/regPointUpdate`, `/regPointDelete`, 라벨은 `/makeLabel`, `/updateLabel`, `/deleteLabel`, `/insertRegToLabel`, `/deleteLabelData`, `/resetLabel`, 동기화·백업은 `/regPointsync`, `/moveRegPoint`다. 통합회원(FivePin-AIR)용은 `/airRegpointUM`, `/regPointInsertUM`, `/regPointDeleteUM`, `/regPointUpdateUM`이다. 헤더 `reg_flag`가 필수다.

## 4~5. 로그, 이벤트

- 로그: `/userEvent`, `/uploadDrivingLog`, `/uploadAiLog`, `/uploadAirlabLog`
- 이벤트: `/event`, 행운상자 `/getLuckyProductList`·`/getLuckyBoxStatus`·`/luckyBoxOpen`·`/luckyBoxList`, 캐시 적립 `/event/cash/earn`, 모바일 교환권 `/event/cash/voucherExchange`

## 6. 기타

- 외부 계정(SNS): `/snsLogin`, `/snsCheck`, `/snsTransLogin`, `/snsLogout`, `/snsMemberInfoInsert`, `/signout`, 통합 탈퇴 `/integratedSignout`
- 지도/안내: `/extendedMap`, `/extendedNewMap`(확대도), `/directionVoice`(방면 음성), `/searchOilStation`, `/bridgeList`
- 사용자 데이터: `/saveConfig`, `/latelyPoiListSelect`, `/latelyPoiListInsert`, 주행 이력 `/drivingHis*`(`GroupList`, `DayList`, `DayListDetail`, `Delete`, 통합회원용 `...UM`), `/mileageHisInsert`
- 도로 상황: `/roadEventDetail`, `/cctvInfo`, `/emergencyDetail`, `/confusionLane`
- 제보/긴급: `/simpleReport`, `/roadAcdntNotiSos`(AIR SOS)
- KT 서비스 종료 마이그레이션: `/snsInfoMigrationFile`, `/snsInfoMigrationData`

## 7. RRIS

위치와 경로를 서버로 올리는 API: `/rris/data/currentLoc`(현재 위치, 그룹주행과 공용), `/rris/data/saveRoute`(경로 파일), `/rris/event/upEmergency`(이벤트 위치).

## 8. 에어 캐시

`/cashInfo`, `/cashSave`, `/productList`, `/productDetail`, `/couponPurchase`, `/couponBox`, `/couponBoxDetail`, `/couponResend`, `/airCashHistory`, `/roulette`, `/stampHistory`, `/stampComplete`, `/cashStampSave`, `/cashStampInfo`, `/cashStampRouletteGame`, `/cashStampRouletteTicket`

## 9~11. w3w, 캐시버튼, HUD

- w3w: `/w3w/autoSuggest`(3단어 추천어), `/w3w/wordSearch`
- 캐시버튼(Android 전용): `/cashButton/cashConversion`
- HUD: `/authSerialNumber`(시리얼 인증)

## 12. 신호등

`/trafficLightList`(전체 목록), `/trafficLightStatus`(신호 상태), `/trafficLightWalker`(보행자 신호). 방향 코드는 북 10, 동 20, 남 30, 서 40, 북동 50, 남동 60, 남서 70, 북서 80이다. 연동 규격은 [[daegu-traffic-light-protocol]]을 본다.

## 13~16. 음성광고, 메인화면, 그룹주행, 오픈POI

- 온에어 음성광고: `/onAirDailyCount`, `/onAirVoiceFileInfo`, `/onAirListenStart`, `/onAirListenFinish`
- 메인: `/weather`, `/mainPageData`, `/fortuneBirthCheck`
- 그룹주행: `/makeGroup`, `/rris/data/currentLoc`, `/groupUpdate`, `/groupDrivingHis` → [[inavi-air-group-driving-design]]
- 오픈POI: `/makeOpenPoi`, `/getOpenPoi`, `/searchOpenPoi`

## 17~20. AIR 서비스, 나의주행, 제보

- 서비스: `/clauseCheck`(약관 조회), `/clauseAgree`(약관 동의와 개인키 생성), `/mapDownloadInfo`(지도 다운로드 정보), `/serviceGate`(서비스 메인)
- 나의주행: `/weeklyMyHabit`, `/myDailyDrivingList`, `/drivingHabitDetail`, `/monthlyMyDriving`
- 제보: `/reportLog`

## 21~23. 삼성중공업 SDK, 통계, 오르다

- `/shiSdk/getTFlimitInfo`(이동불가/출입금지 구역), `/shiSdk/getDrivStopInfo`(운행금지시간), `/shiSdk/getDisasterInfo`(중대재해 구역), `/shiSdk/sendShiGps`(GPS 전송), `/shiSdk/getStopAreaInfo`(일단 정지 구역)
- 통계: `/statistics/totalUser`, `newUser`, `drivingHistory`, `cashedUser`
- 오르다: `/orda/stamp`(가까운 스탬프 조회)

## Open Questions

- 원본에서 `새 주소 검색`은 URL 칸이 비어 있어 위 표에서도 뺐다. ^[ambiguous]
- `/rris/data/currentLoc`는 RRIS와 그룹주행 두 영역에 모두 나온다. 같은 API를 공용으로 쓰는 것으로 보인다. ^[inferred]

## Sources

- [[_raw/_archived/API 상세명세.md]] — 엔드포인트별 상세 스펙 원본
