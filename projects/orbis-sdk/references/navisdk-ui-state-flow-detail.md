---
title: >-
    NaviSDK 상태 관리 Flow 상세 (UIGuideData·UIMode)
category: references
project: orbis-sdk
tags: [navisdk, state-management, stateflow, kotlin, visibility/internal]
aliases: [상태 관리 Flow, UIGuideRepository, UIGuideData]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/789512333
summary: >-
    UIGuideRepository의 StateFlow 기반 상태 관리 규칙, NaviController 단일 변경 주체, UIGuideData 필드와 UIMode enum 전체
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

# NaviSDK 상태 관리 Flow 상세

신규 NaviSDK에서 UI와 엔진 상태를 어떻게 흐르게 하는지 정의한 문서(2025-05-08 수정)다. 구조 전반은 [[new-navisdk-plan-detail]]의 Usecase/Repository/ViewModel 규칙과 연결된다. 요약은 [[orbis-navisdk-architecture-and-flutter-plan]], 목차는 [[orbis-design-and-review-hub]].

## Flow 규칙
1. Repository(`UIGuideRepository`)에서 상태 및 UI 관련 데이터를 포함한 상태값(`UIGuideData`)을 StateFlow로 관리한다.
   1. 상태 관리 로직은 해당 Repository에서만 처리한다.
2. `NaviController`에서만 Repository와 각 내부 엔진에 변화되는 상태를 전달하고 관리한다.
   1. `NaviController`에서만 상태 변경을 요청할 수 있다.
   2. 상태 값 변경에 따른 엔진 변화는 `NaviController`가 담당한다.
3. 각 ViewModel은 Repository의 State를 통해 담당 View의 상태를 변경한다.

구조도는 이미지 항목(내용 없음)이다.

## Data Class

```kotlin
data class UIGuideData(
    val turnInfo: NaviTurnInfo? = null,
    val nextTurnInfo: NaviTurnInfo? = null,
    var speed: Int? = null,
    var isNight: Boolean = false,
    var mapUIMode: UIMode = UIMode.MODE_GUIDE, //상태 값
    var hasRoute: Boolean = false,
    var roadType: Int? = null,
    var roadSpec: Int? = null,
    var timeType: Int? = null,
    var remainTime: Int? = null,
    var arrivalTime: Int? = null,
    var remainFee: Int? = null,
    var remainDist: Int? = null,
    var regionName: String? = null,
    var roadName: String? = null,
    var fullAddr: String? = null,
    var goalName: String? = null,
    var viaName: String? = null,
    var isRouteMenuVisible: Boolean = false,
    var percentOfDist: Float? = null,
    var drivingTotalDist: Float? = null,
    var mapAngle: Int = 0,
    var mapLevel: Int = 0,
    var volumeMute: Boolean = false,
    var simulPercent: Int = 0,
    var linkCnt: Int = 0,
    var curLinkIdx: Int = 0,
    var isLoggingGPS: Boolean = false,
    var forceHide: List<Boolean>? = null
    ...필요시 UI관련 데이터 필드 추가
)

enum class UIMode {
    MODE_NORMAL,
    MODE_GUIDE,
    MODE_MAP_MOVE,
    MODE_ONE_TAP,
    MODE_SIMUL_GUIDE,
    MODE_SIMUL_MAP_MOVE,
    MODE_SIMUL_ONE_TAP;
}
```

## 필드 분류 (원문에 없는 정리, 이해용)
원문은 필드 의미를 설명하지 않는다. 이름으로 보이는 범주만 표로 묶는다. ^[inferred]

| 범주 | 필드 |
|---|---|
| 턴 정보 | `turnInfo`, `nextTurnInfo` (둘 다 `NaviTurnInfo?`, 불변 `val`) |
| 주행 상태 | `speed`, `isNight`, `mapUIMode`, `hasRoute`, `volumeMute`, `isLoggingGPS`, `forceHide` |
| 도로 정보 | `roadType`, `roadSpec`, `regionName`, `roadName`, `fullAddr` |
| 잔여/도착 | `timeType`, `remainTime`, `arrivalTime`, `remainFee`, `remainDist`, `percentOfDist`, `drivingTotalDist` |
| 목적지/경유지 | `goalName`, `viaName` |
| 지도 | `mapAngle`, `mapLevel` |
| 메뉴 | `isRouteMenuVisible` |
| 모의주행/링크 | `simulPercent`, `linkCnt`, `curLinkIdx` |

## UIMode 값

| 값 | 비고 |
|---|---|
| MODE_NORMAL | 일반(경로 없음 상태로 추정) ^[inferred] |
| MODE_GUIDE | 안내 중. `UIGuideData.mapUIMode`의 기본값 |
| MODE_MAP_MOVE | 안내 중 지도 이동 |
| MODE_ONE_TAP | 안내 중 원탭 |
| MODE_SIMUL_GUIDE | 모의주행 안내 |
| MODE_SIMUL_MAP_MOVE | 모의주행 중 지도 이동 |
| MODE_SIMUL_ONE_TAP | 모의주행 중 원탭 |

값별 설명은 원문에 없고 이름에서 추정한 것이다. ^[inferred]

## Related
- [[new-navisdk-plan-detail]] — NaviController/ViewModel/Repository 계층 정의
- [[navisdk-api-coverage-and-domestic-sdk-guide]] — 기존 국내 SDK API 범위
- [[orbis-navisdk-architecture-and-flutter-plan]] — 요약
- [[orbis-sdk]]

## Sources
- Confluence "상태 관리 Flow" (pageId 789512333) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
