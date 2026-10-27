---
title: >-
    MapsSDK 엔진 플랫폼 차이점 정리 (AOS vs iOS 함수 비교표)
category: references
project: orbis-sdk
tags: [mapssdk, engine, kmp, aos-ios-diff, visibility/internal]
aliases: [MapsSDK 엔진 플랫폼 차이점 정리, DP OS 간 차이점, MMC OS 간 차이점]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/641695841
summary: >-
    KMP Common IF 기준으로 DP(지도 표시)와 MMC(맵매칭) 엔진의 AOS/iOS 함수 차이, 비고, 확인 결과를 모든 행으로 정리
provenance:
  extracted: 0.90
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T13:00:00+09:00
updated: 2026-10-26T13:00:00+09:00
---

# MapsSDK 엔진 플랫폼 차이점 정리

KMP Common IF에 정의된 함수를 기준으로 AOS와 iOS 엔진 함수의 차이를 정리한 문서(2024-12-24 수정)다. 원문 안내: 색으로 칠해진 부분은 return 타입은 다르지만 iOS에서 변경 후 KMP 통합 구현을 끝낸 함수다(색은 정리본에 남지 않아 어느 행인지는 알 수 없다 ^[ambiguous]). KMP 도입 배경은 [[kmp-cmp-adoption]], 신규 SDK 구조는 [[new-navisdk-plan-detail]], 목차는 [[orbis-design-and-review-hub]]. "-"는 해당 플랫폼에 함수가 없다는 뜻이다. "auto only"는 차량 내장(Auto) 전용이라는 원문 표기다.

## DP(지도 표시 엔진) OS 간 차이점 정리 (완료)

| AOS | iOS | 비고 | 확인 내역(DC 작성) |
|---|---|---|---|
| setDestory(Bool, Bool) | destroy | iOS Native Param 미사용 | 이슈 아님 |
| getErrCod | - | iOS에 없는 기능. AOS에서 반드시 0 return 하도록 구현되어 있음 | 이슈 아님 |
| setFrontLine(int) | - | iOS에 없는 기능(auto only) | 사용 안함 |
| getMapCenter | - | iOS에 없는 기능(auto only) | 사용 안함 |
| zoomIn(int, int) | zoomIn | iOS Native Param 미사용 | setMapLevel로 변경 |
| zoomOut(int, int) | zoomOut | iOS Native Param 미사용 | setMapLevel로 변경 |
| multitouch_auto (float) | - | iOS에 없는 기능(auto only) | 사용 안함 |
| move_auto (float, float) | - | iOS에 없는 기능(auto only) | 사용 안함 |
| setDPI (int) | - | iOS에 없는 기능 | 사용 안함 |
| setGuideColor (int, int) | - | iOS에 없는 기능(auto only) | 사용 안함 |
| getSpeedNType(long) | - | iOS에 없는 기능(auto only) | 사용 안함 |
| removeCarResource → Int | removeCarResource | iOS Void function. AOS 미사용, return 0으로 고정됨 | 사용 안함 |
| setCarResource ( _, _, _… ) | setCarResource ( _, _, _… ) | iOS Void function. AOS 미사용, return 0으로 고정됨 | 사용 안함 |
| addResource (_, _, _, _) | addResource (_, _, _, _) | iOS Void function. AOS return 0으로 고정됨(해당 함수 return 값 사용처가 보이지 않음) | 이슈 아님 |
| updateResource (_, _, _, _) | - | iOS에 없는 기능(auto only) | 사용 안함 |
| enableTrafficData(bool) | - | iOS에 없는 기능(auto only) | 사용 안함 |
| setTrafficColor(int, int, int, int) | - | iOS에 없는 기능(auto only) | 사용 안함 |
| selectUserRoad(double, double) → Point | selectUserRoad(double, double, double, double) | iOS Void function. AOS auto only | 사용 안함 |

## MMC(맵매칭 엔진) OS 간 차이점 정리

| AOS | iOS | 비고 | 확인 내역(DC 작성) |
|---|---|---|---|
| startLiveLogging(str) | startLiveLogging(str) | iOS Bool Return → 0/1 리턴하도록 구현. AOS 미사용 | AOS 미사용, iOS는 잘못 매칭 |
| stopLiveLogging | stopLiveLogging | iOS Bool Return → Void 리턴하도록 구현. AOS 미사용 | AOS 미사용, iOS는 잘못 매칭 |
| setDoingReRoute | - | iOS 없는 기능. AOS 미사용 | 사용 안함 |
| setDoingRoute | - | iOS 없는 기능. AOS 미사용 | 사용 안함 |
| getLogCountDown | - | iOS 없는 기능. AOS 미사용 | 사용 안함 |
| setLogCountDown | - | iOS 없는 기능. AOS 미사용 | 사용 안함 |
| nativeSetMapmatchCheckDevice(int) | - | iOS 없는 기능 | 사용 안함 |
| nativeSetMapmatchLocationMode(bool) | setMapMatchMode(bool) | iOS Bool Return → Void 리턴하도록 구현 | 잘못 매칭, iOS 사용 안함 |
| nativeSetConfigureMMC(bool, bool, bool) | - | iOS 없는 기능(sensor 관련 함수 추정) | 사용 안함 |
| nativeSetDRMString(str) | - | iOS 없는 기능. AOS `setDRMString` 미사용 | 사용 안함 |
| nativeMapMatch(bool, int) | startMapmatch | mapmatch start 기능이 맞는지 확인 필요. iOS Bool Return → Int return으로 구현. AOS 해당 함수 Return 값은 사용하지 않는 것으로 추정 | 잘못 매칭. 추가 확인 필요: iOS startMapmatch와 동일한 부분으로 보이지 않음. stopMapmatch 함수도 추가 필요. `startMapmatch_oniOS`, `stopMapmatch_oniOS` 함수를 추가 |
| nativeSetUseSensorStatus(boot, int) | - | iOS 없는 기능(sensor 관련 함수 추정) | 사용 안함 |
| nativeGetUseSensor | - | iOS 없는 기능(sensor 관련 함수 추정) | 사용 안함 |
| nativeSetNMEAData(str, int) | - | iOS 없는 기능(NMEA) | 사용 안함 |
| nativeSetSensorData(sensorRawData) | - | iOS 없는 기능(sensor 관련 함수 추정) | 사용 안함 |
| nativeGetSensorAction | - | iOS 없는 기능(sensor 관련 함수 추정) | 사용 안함 |
| nativeStartGravity(str, str) | - | iOS 없는 기능 | 사용 안함 |
| nativeStopGravity | - | iOS 없는 기능 | 사용 안함 |
| nativeDebugLog(int, str) | setDebugLogMode(int) | iOS str Param 미사용 | logmsg 불필요 |
| nativeSetLogFileName(int, str) | setDebugLogMode(int, str) | iOS Bool return → Int 리턴하도록 구현 | AOS 모드별 사양 확인 필요 |
| nativeStopLogging | stopLogging | iOS Bool return → Int 리턴하도록 구현 | 이슈 아님 |
| nativeSetRouteTable(byteArr, int) | setRouteTableWithBuffer(char *, int) | 함수 return 타입 차이. iOS Void return → 함수 실행 시 1 리턴하도록 구현. KMP 측에서 byteArr 값이 없으면 0 리턴하도록 구현 | 이슈 아님, 리턴값 사용 안함 |
| nativeSetRouteTableInDirect(str) | - | iOS 없는 기능. AOS `setRouteTableInDirect` 미사용 | 사용 안함 |
| nativeChangeLink | - | iOS 없는 기능 | 사용 안함 |
| nativeSetNetworkCoordinate(float, float) | - | iOS 없는 기능 | 사용 안함 |
| nativeSetNetworkCoordinateByBessel(int, int …) | - | iOS 없는 기능 | 사용 안함 |
| nativeSetBackground(bool) | setBackGround(bool) | iOS Void → 1 return 하도록 구현 | 이슈 아님 |
| nativeSetGuideCode(int, int) | - | iOS 없는 기능 | 사용 안함 |
| _GPSInfo | _GPSInfo | `pressure`가 iOS에는 없음(0.0f로 적용) | `pressure` 사용 안함 |
| nativeGetSATInfo | - | iOS에 없는 Type(SATInfo) | 사용 안함 |
| _MMCInfo | MMCResult | iOS에 없는 Property: `cFastEscapeReady`, `DRMValue`, `fHeading` | AOS 사용처 확인 필요. 사용하지 않는 것으로 보임. AIR 확인 결과 `fHeading`은 없음(제거됨) |
| nativeGetSATInfoArray | - | iOS에 없는 기능 | 이슈 아님 |
| nativeSetSimulatePos(int) | setSimulationPosition(int) | iOS Bool Return → Void 변경 구현 | 이슈 아님 |
| nativeSetSimulatePause | - | iOS에 없는 기능 | 사용 방식에 따라 구현 |
| nativeSetSimulateStartStop | - | iOS에 없는 기능 | 사용 방식에 따라 구현 |
| nativeSetSimulateSpeed(int) | setSimulationSpeed(int) | iOS Bool Return → Void 변경 구현 | 이슈 아님 |
| nativeSetSimulatePercentage(int) | setSimulationPercentage(int) | iOS Bool Return → Void 변경 구현 | 이슈 아님 |
| nativeSetCRoadSkipMode(bool) | setSimulationRoadSkip(bool) | iOS Bool Return → Void 변경 구현 | 이슈 아님 |
| nativeSetSimulateIndex(int, int) | setSimulationIndex(int) | iOS Bool Return → Void 변경 구현. iOS dist param 미사용 | 이슈 아님(AOS도 0 default 셋팅) |
| nativeSetLastPosSavedInZone(bool) | setLastPosSavedInZone(bool) | iOS Bool Return → Void 변경 구현 | 이슈 아님 |
| nativeSetIsEscapeLinkNowFlag(bool) | setEscapingLinkNow(bool) | iOS Bool Return → Void 변경 구현 | 이슈 아님 |

## 요약 관찰 (원문 표에서 읽히는 내용)
- 확인 내역의 대다수가 "사용 안함"이다. iOS에 없는 함수는 auto only 또는 sensor/NMEA 관련 함수가 많다.
- 실제 후속 조치가 적힌 행: `zoomIn`/`zoomOut`은 `setMapLevel`로 대체, `nativeMapMatch`는 iOS용 `startMapmatch_oniOS`/`stopMapmatch_oniOS` 추가, `nativeSetLogFileName`은 AOS 모드별 사양 확인 필요, `nativeSetSimulatePause`/`nativeSetSimulateStartStop`은 사용 방식에 따라 구현.
- 잘못 매칭으로 판정된 행: `startLiveLogging`/`stopLiveLogging`(iOS 쪽), `nativeSetMapmatchLocationMode`, `nativeMapMatch`.

## Related
- [[new-navisdk-plan-detail]] — KMP 공용 모듈과 엔진 로드 단계
- [[kmp-cmp-adoption]] — KMP 도입 배경
- [[inavi-sdk-ios-controller-reference]] — iOS SDK 컨트롤러 참고
- [[orbis-sdk]]

## Sources
- Confluence "📝MapsSDK 엔진 플랫폼 차이점 정리" (pageId 641695841) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
