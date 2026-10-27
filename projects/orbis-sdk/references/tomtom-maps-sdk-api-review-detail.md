---
title: >-
    TomTom Maps SDK API 검토 상세 (OrbisMap 적용 API 표·커스텀 자차 마커)
category: references
project: orbis-sdk
tags: [tomtom, maps-sdk, orbismap, api-review, visibility/internal]
aliases: [TomTom Maps SDK API 검토]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/746029545
summary: >-
    TomTom Maps SDK 가이드의 API를 OrbisMap에 적용하기 위해 기능별로 검토한 표 전 행과 Custom location marker(.glb) 검토 내용
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

# TomTom Maps SDK API 검토 상세

TomTom Maps SDK 가이드 문서의 API를 검토해 OrbisMap에 적용할 API를 기능별로 정리한 페이지(2025-04-01 수정)다. 가이드 문서 링크는 `<링크 생략>`. 요약은 [[orbismap-route-and-tomtom-sdk-review-2025]], Route 응답 검토는 [[orbismap-route-review-detail]], 목차는 [[orbis-design-and-review-hub]].

## 기능별 적용 가능 API

| Feature | 적용 가능한 Maps SDK API | Description |
|---|---|---|
| 현위치 | 1. `Markers` 2. `User Location` 3. `Custom Location Provider` 4. `Custom Location Markers` | **Markers**: 마커로 현위치를 표출하면 마커를 지우고 다시 만드는 과정을 반복해야 자차 위치가 갱신되어 UI가 반짝거린다(Marker 내부 속성이 불변 타입이라 가변적으로 바꿀 수 없음). **User Location**: LocationInterceptor를 이용해 MMC에서 전달받은 데이터를 TomTom Location Provider에 세팅할 수 있는지 검토가 필요하다. **Custom Location Provider**: LocationProvider를 직접 구현한 뒤 TomTom Maps SDK에 적용할 수 있다. **Custom Location Markers**: TomTom이 기본 제공하는 현위치 마커(주행 시 자차 마커, 미주행 시 원형) 외에 Custom Marker를 특정 asset 형태로 제작하면 적용할 수 있다. |
| 현위치 이동 | `CameraPosition` | 현위치 좌표를 세팅해 이동할 수 있다. |
| 2D 고정/회전 및 3D 회전 | 1. `CameraPosition` 2. `CameraTrackingMode` | **CameraPosition**: `Tilt`(기울이기) 속성으로 2D/3D 효과를 적용할 수 있다. **CameraTrackingMode**: Route의 `Instruction`을 따라가게 적용할 수 있다(주행/모의주행 시). |
| 경로선 | 1. `addRoute(Routes)` 2. `Polygons` | **Add Route**: 경로셋을 세팅하면 경로선이 표출된다. `Instruction` 속성을 이용하면 경로선에 차기·차차기 화살표를 표출할 수 있을 것으로 판단한다. **Polygons**: 경로셋을 세팅하면 `Polygon`이 그려진다. 추가 검토 필요. |
| Zoom To Fit | `ZoomToRoutes` | `addRoute`로 경로를 그린 뒤 해당 경로에 대해 Zoom To Fit이 일어난다. `Padding`(콘텐츠와 안전영역 테두리 사이 간격)을 설정할 수 있다. `addRoute`가 되어 있지 않은 상태에서 `ZoomToRoutes`를 실행하면 `Exception`이 발생한다. |
| 교통정보 | `ShowTrafficFlow` | (설명 없음) |
| 교통사고 | `ShowTrafficIncidents` | (설명 없음) |
| 차량제한 | `showVehicleRestrictions` | (설명 없음) |
| 저공해 구역 | `loadStyle(StandardStyles.VEHICLE_RESTRICTIONS, …)` | 저공해 구역은 차량이 배출하는 오염 물질의 양에 따라 차량의 접근을 제한하는 구역이다. |
| 지도 캐싱 | `MapOptions(…, onlineCachePolicy)` | TomTom 지도 SDK는 온라인에서 지도를 가져올 때 캐시 정책을 적용해 네트워크 요청을 줄이고 성능을 최적화한다. `onlineCachePolicy` 속성으로 HTTP 캐시 동작을 제어할 수 있다. Default는 10MB. |
| 지도 FPS(새로 고침 빈도) | `setFrameRate` | Default는 60. |
| 지도 스타일 | `setStyleMode`, `loadStyle` | **Style Mode**: `Dark`, `Main` 2가지 모드. **Load Style**: 탐색(`BROWSING`), 주행(`DRIVING`), 위성(`SATELLITE`) 적용 가능. |
| 언덕 음영 | `showHillShading` | (설명 없음) |
| 지도 Gesture | `Listener` | 드래그, 투탭, 롱클릭, 패닝 상태 응답이 가능하다. |
| 기본 제공 UI | `visibilityPolicy`, `icon` | 로고, 축적, 현위치, 나침반 기본 제공 UI를 제거할 수 있다. 아이콘은 변경할 수 있으나 외부 원 아이콘은 변경이 불가능해 보인다. |

## Custom location markers 검토
자차 Custom 이미지 변경을 검토한 내용이다(TomTom 문서 링크 생략).

### 검토 내용
- 지도 모듈에서 Custom 자차 이미지를 쓰려면 `.glb` 형식의 모델을 제공해야 한다.
- `LocationMarkerOption`의 `CustomModel` 속성에 `.glb` 파일 경로를 설정해 적용할 수 있다.
- `.glb` 파일은 프로젝트 내부 assets 폴더에 저장해야 하며, 모델 경로는 `asset://file.glb` 형식으로 제공해야 하는 것으로 확인되었다.

### GLB 파일이란
GLB 파일은 3D 모델과 씬을 저장하는 파일 형식이다. 모델 자체, 텍스처, 머티리얼, 애니메이션, 조명 등 3D 에셋을 구성하는 모든 데이터를 담는 컨테이너다.

### 검토 결과
- Moko-Resource를 이용해 Assets 폴더를 만들고 내부에 테스트용 `.glb` 파일을 추가했다.
- `LocationMarkerOption`의 `CustomModel` 속성을 아래 값으로 세팅했다(`Resources.getAssetImage().path`는 테스트용 `.glb`를 가져오는 코드).

```kotlin
customModel = "asset://${Resources.getAssetImage().path}".toUri()
```

### 결과
원문의 "[결과]" 항목은 비어 있다(이미지 항목으로 추정). ^[inferred]

## Related
- [[orbismap-route-and-tomtom-sdk-review-2025]] — 요약
- [[orbismap-route-review-detail]] — OrbisMap Route 응답 검토
- [[orbis-navisdk-poc-prep-2025]] — PoC 사전 준비
- [[orbis-tile-map-style-analysis]] — 타일 스타일 분석
- [[orbis-sdk]]

## Sources
- Confluence "TomTom Maps SDK API 검토" (pageId 746029545) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
