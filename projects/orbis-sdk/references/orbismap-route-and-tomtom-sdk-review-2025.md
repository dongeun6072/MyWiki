---
title: >-
    OrbisMap Route와 TomTom Maps SDK 검토 (2025-03~04)
category: references
project: orbis-sdk
tags: [orbis-sdk, tomtom, route, maps-sdk, visibility/internal]
aliases: [OrbisMap Route 검토, TomTom Maps SDK API 검토, Route Server for Taiwan 검토]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[taiwan-routeserver-api]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/761167886
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/746029545
summary: >-
    대만 탐색 서버(OrbisMap Route)의 도로 종별과 TBT 정보, TomTom Maps SDK의 현위치·경로선·교통·캐싱·스타일 API를 Orbis에 적용하기 위해 검토한 결과.
provenance:
  extracted: 0.90
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T12:25:00+09:00
updated: 2026-10-26T12:25:00+09:00
---

# OrbisMap Route와 TomTom Maps SDK 검토 (2025-03~04)

[[orbis-navisdk-poc-prep-2025]] 이후 엔진 연동 스프린트([[navisdk-confluence-sprint-timeline-2024-2026]])에서 쓴 두 검토 문서다. 서버 규격 자체는 [[taiwan-routeserver-api]]에 있다.

## OrbisMap Route 검토 (2025-04-07)

대만 탐색 서버("Route Server for Taiwan")가 주는 정보와, 국내 탐색과 다른 점을 확인했다.

- **도로 종별 16종**: 0 Motorway(고속도로), 1 Motorway Link, 2 Trunk, 3 Trunk Link, 4 Primary, 5 Primary Link, 6 Secondary, 7 Secondary Link, 8 Tertiary, 9 Tertiary Link, 10 Residential, 11 Living Street, 12 Unclassified, 13 Unknown, 14 Service, 15 Track. 링크별로 실시간 속도, 통계 속도, 속도 정보 없음이 구분된다.
- **TBT**: 링크별 `maneuver`에 턴 정보가 있다(-1 미지정, 0 직진, 1 약간 우회전, 2 약간 좌회전, 3 우회전, 4 좌회전, 5 급우회전, 6 급좌회전, 7 U턴). 글로벌 지도 기준이라 국내 탐색 대비 정보가 부족해, 국내 기준의 "turn 정보 유무에 따른 안내"를 바꿔야 한다.
- **검토 결과**: 도로 종별과 pass 타입을 구분할 수 있는지 확인이 필요하고, 도로명은 MapReader 쪽에 요청을 마쳤다. TomTom API 연동으로 경로 표출과 경로 내 턴 정보 표출이 가능했다.
- 문서 후반은 응답 JSON 예시(경로 좌표 등)가 길게 붙어 있다.

## TomTom Maps SDK API 검토 (2025-04)

TomTom 가이드의 API를 훑어 OrbisMap에 쓸 것을 정리했다.

| 기능 | 쓸 API | 메모 |
|---|---|---|
| 현위치 | Markers, User Location, Custom Location Provider/Markers | 마커로 그리면 지우고 다시 만드는 과정 때문에 깜빡인다(마커 속성이 불변) |
| 2D/3D, 회전 | `CameraPosition`(Tilt), `CameraTrackingMode` | Tilt로 2D/3D 효과 |
| 경로선 | `addRoute(Routes)`, Polygons | Instruction 속성으로 차기·차차기 화살표 가능 |
| 줌 투 핏 | `ZoomToRoutes` | `addRoute` 전에 호출하면 예외 발생. 패딩 설정 가능 |
| 교통 | `ShowTrafficFlow`, `ShowTrafficIncidents`, `showVehicleRestrictions` | 저공해 구역은 `loadStyle(VEHICLE_RESTRICTIONS)` |
| 캐싱 | `MapOptions(onlineCachePolicy)` | 기본 10MB |
| FPS | `setFrameRate` | 기본 60 |
| 스타일 | `setStyleMode`(Dark/Main), `loadStyle`(탐색/주행/위성) | |
| 기본 UI | `visibilityPolicy`, `icon` | 로고, 축적, 나침반 제거 가능. 위치 아이콘의 바깥 원은 변경 불가로 보임 |

- **자차 커스텀 이미지**: 커스텀 위치 마커는 `.glb`(3D 모델) 형식만 받고 `LocationMarkerOption`의 `CustomModel`에 `asset://` 경로로 지정한다. 프로젝트 assets에 두어야 하고, Moko-Resource로 assets 폴더를 만들어 시험했다.
- 이후(2025-06) OrbisMap Maps SDK가 제공되지 않는 문제가 생겨 MapLibre 기반으로 바꿨다 → [[navisdk-confluence-sprint-timeline-2024-2026]].

## Sources

- [Confluence: OrbisMap Route 검토](https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/761167886), [TomTom Maps SDK API 검토](https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/746029545) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
