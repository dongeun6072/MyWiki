---
title: >-
    INAVI RouteServer for Taiwan API 규격 (v2.0, v2.3)
category: references
tags: [orbis-sdk, routing, api, tomtom, visibility/internal]
aliases: [Taiwan RouteServer API, 대만 경로탐색 API, searchroute]
relationships:
  - target: "[[orbis-routing-stack]]"
    type: related_to
  - target: "[[vehicle-restriction-routing]]"
    type: related_to
sources: []
summary: >-
    TomTom Orbis Maps 대만 데이터를 쓰는 경로탐색 서버의 API 규격 v2.3. searchroute와 searchroutemulti의 요청 파라미터, 응답 필드, 결과 코드, 버전별 변경 이력을 정리했다.
provenance:
  extracted: 0.88
  inferred: 0.12
  ambiguous: 0.00
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T09:25:23+09:00
updated: 2026-10-26T09:25:23+09:00
---

# INAVI RouteServer for Taiwan API 규격

경로기술개발팀이 작성한 대만 지역 경로탐색 API 연동 규격서다. TomTom Orbis Maps의 대만 도로 데이터를 쓰고, 해외향 Navi SDK([[orbis-sdk]])의 탐색 서버 쪽 규격이다. ^[inferred] 전체 구조는 [[orbis-routing-stack]]에 정리했다. v2.0(50쪽)과 v2.3(54쪽, 2026-07-21) 두 버전이 있으며 이 페이지는 최신인 v2.3을 기준으로 하고 v2.0과의 차이를 따로 적었다.

## 서비스 형태

탐색 엔진, 서비스 데이터, 데이터 라이브러리 버전별로 **포트를 분기**해 서비스한다. 문서 시점에는 두 포트가 있었다. 서버 주소는 원본에만 두고 이 페이지에는 적지 않았다.

| 포트 | 엔진 | 서비스 데이터 | 데이터 라이브러리 |
|---|---|---|---|
| 17931 | 2.3 | 26220 | 1.0.1.6 |
| 17932 | 2.0 | 25271 | 1.0.1.4, 1.0.1.5 |

## API

| API | 설명 |
|---|---|
| `/searchroute` | 경로 탐색. 출발지, 목적지, 경유지(N개). GET, POST(form-urlencoded, json) 지원. 모든 좌표는 WGS84 |
| `/searchroutemulti` | 다중 경로 탐색(v1.3, 2025-09 추가). 최적 경로와 대안 경로 |

## 요청 파라미터 (`/searchroute`)

| 파라미터 | 설명 |
|---|---|
| `startX/startY/endX/endY` | 필수. WGS84 |
| `viaList` | 경유지 좌표 JSON 배열 |
| `option` | 사용 안 함. 기본으로 최적 경로 |
| `traffic` | 0 교통정보 미적용(기본), 1 적용 |
| `directionangle` | 출발지 진행 방향 각도. -1 미적용(기본), 0~360은 정북 기준 시계 방향 |
| `sideroadstart`, `sideroadend` | 출발지/목적지 좌표 기준 도로 방향성 탐색. `directionangle`과 동시 적용 불가(출발지) |
| `weight`, `height`, `length`, `width` | 차량 제원(톤, 미터). 통행 불가 도로 회피. 전장과 전폭을 함께 주면 회전 반경 제한 탐색 |
| `hazmat` | 위험물 운송 제한 도로 회피: 0 없음, 1 모든 위험물, 2 폭발물, 3 수질오염물질 |
| `waypointroutingmode` | 경유지 포함 시 0 Strict(법규 우선), 1 Bypass(경로 유형 유지, 기본) |

차량 제원 옵션의 자세한 동작은 [[vehicle-restriction-routing]]에 있다.

## 응답

- `resultCode`, `user_info`(요청 옵션 에코), `routes`(`routeCode`, `distance`(m), `spend_time`(초), `fuel_consumption`(L)), `links`(배열)
- 경로 선형은 GeoJSON LineString, 좌표는 WGS84
- `links`의 필드: `id`(원본 링크 ID), `id_index`(네트워크 변환기가 만든 index), `osm_id`, `highway`(도로 종별 0~15), `speed`(실시간 속도가 없으면 통계 속도, 없으면 0), 남은 거리와 시간, 진행 방향, `maneuver`(TBT 유형), 도로명 ID, `vertex_offset`
- `maneuver`가 `-1`이면 경유지 또는 목적지 도착 링크다. 이 값으로 구간을 나눈다.
- 회전교차로 안내 코드: `ROUNDABOUT_EXIT_CLOCK_1~12`(진출 방향을 시계 시각으로), `ROUNDABOUT_STRAIGHT`, `ROUNDABOUT_EXIT`(N번째 진출 안내 가능), `ROUNDABOUT_ENTRY`(목적지가 회전교차로 안일 때)

### 도로 종별(`highway`)

0 Motorway, 1 Motorway Link, 2 Trunk, 3 Trunk Link, 4 Primary, 5 Primary Link, 6 Secondary, 7 Secondary Link, 8 Tertiary, 9 Tertiary Link, 10 Residential, 11 Living Street, 12 Unclassified, 13 Unknown, 14 Service, 15 Track. OpenStreetMap 분류와 같다.

## 결과 코드

| 코드 | 의미 |
|---|---|
| 0 | 성공 |
| 1 | 도로 확장 실패 |
| 2, 3, 4 | 출발지, 목적지, 경유지 주변에 도로 없음 |
| 11~13 | 출발지/목적지/경유지 주변이 **중량** 제한 |
| 14~16 | 같은 위치가 **높이** 제한 |
| 17~19 | 같은 위치가 **길이** 제한 |
| 20~22 | 같은 위치가 **위험물** 통행 금지 |
| 23 | Strict 모드에서 경유지 주변 일방통행 역주행 제한으로 실패 |

경로 결과 상세 코드(`routeCode`)는 성공했지만 제약이 있을 때만 다르다: `10` 전장/전폭으로 통행하기 어려운 회전 구간 포함, `20` 경유지 주변 역주행이나 특수 회피 경로 포함. 제약이 없으면 `resultCode`와 같다.

## 버전별 변경 이력

| 시기 | 버전 | 변경 |
|---|---|---|
| 2024-06 ~ 10 | 0.1~0.3 | 초기 배포, 교통정보 적용 옵션, OSM ID와 속도, 도로 종별 |
| 2025-03 ~ 06 | 0.4~0.9 | TBT 유형, JSON Content-Type, 도로명 ID, 남은 시간과 진행 방향 |
| 2025-07 | 1.1 | 출발지 방향성 탐색 각도 |
| 2025-09 | 1.3, 1.4 | 다중 경로 탐색, Links Detail |
| 2025-10 ~ 11 | 1.6, 1.8 | 출발지 기준 도로 방향성, maneuver 상세, 포트 분기 정보 |
| 2026-03 | 2.0 | 차량 총중량, 최대 높이, 전체 길이 옵션 |
| 2026-05 | 2.1 | 전폭, 위험물 제한, 실패 코드와 상세 코드 |
| 2026-07 | 2.3 | 경유지 탐색 모드(`waypointroutingmode`), 관련 실패 코드 |

v2.0 문서는 이 중 2.0 이전까지 반영된 판이라 `width`, `hazmat`, `waypointroutingmode`가 없다. ^[inferred] 문서 파일명(v2_0, v2_3)과 포트별 엔진 버전(2.0, 2.3)이 일치한다.

## 활용 메모

- 해외향 Navi SDK의 트럭향 API(v1.0.2, 2026-03)는 이 규격의 2.0 차량 제원 옵션과 시기가 맞는다. ^[inferred] ([[orbis-sdk]] 버전 이력 참고)
- 국내 탐색 엔진 [[inavi-routing-neon-protocol]]은 바이너리 프로토콜이고 이쪽은 HTTP/JSON이다.

## Open Questions

- `/searchroutemulti`의 응답 상세(`geometry`, `properties`)는 이 페이지에서 요약하지 않았다. 원본 3장을 본다.
- `option` 파라미터는 문서에서 "사용 안 함"이다.

## Sources

- INAVI RouteServer for Taiwan API 설명서(탐색 서버 API 규격 v2.0, v2.3) — 서버 주소가 들어 있어 원본 PDF를 보안 사유로 삭제했다 (2026-10-26)
