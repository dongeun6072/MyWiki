---
title: >-
    OrbisMap Route 검토 상세 (도로 종별·TBT 코드표·응답 JSON 구조)
category: references
project: orbis-sdk
tags: [orbismap, route-server, taiwan, tbt, json-schema, visibility/internal]
aliases: [OrbisMap Route 검토, Route Server for Taiwan, Route 기능]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/761167886
summary: >-
    대만 Route Server 응답의 도로 종별(0~15)·방향 지시(maneuver) 코드표, 검토 내용, 경로 응답 JSON(177 링크, 382 좌표)의 구조와 통계
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

# OrbisMap Route 검토 상세

대만향 Route Server(TomTom 원도 기반 경로탐색) 응답을 검토한 페이지(2025-04-07 수정)다. 원문은 코드표 두 개, 검토 메모, 그리고 3,500여 줄의 경로 응답 JSON 하나로 이뤄진다. JSON은 구조를 표로 풀고 대표 항목만 남겼다. API 일반은 [[taiwan-routeserver-api]], 요약은 [[orbismap-route-and-tomtom-sdk-review-2025]], Maps SDK 검토는 [[tomtom-maps-sdk-api-review-detail]], 목차는 [[orbis-design-and-review-hub]].

## Route 기능 (Route Server for Taiwan)

### 1. 도로 종별 표출 — `highway` 코드

| 번호 | 도로 유형 | 설명 |
|---|---|---|
| 0 | Motorway | 고속도로 |
| 1 | Motorway Link | 고속도로 연결 링크 |
| 2 | Trunk Road | 간선도로 |
| 3 | Trunk Link | 간선도로 연결 링크 |
| 4 | Primary Road | 주요도로 |
| 5 | Primary Link | 주요도로 연결 링크 |
| 6 | Secondary Road | 2차(보조)도로 |
| 7 | Secondary Link | 2차(보조)도로 연결 링크 |
| 8 | Tertiary Road | 3차(일반)도로 |
| 9 | Tertiary Link | 3차(일반)도로 연결 링크 |
| 10 | Residential Road | 주거용 도로 |
| 11 | Living Street | 생활(이면)도로 |
| 12 | Unclassified Road | 미분류 도로 |
| 13 | Unknown Road | 알 수 없는 도로 |
| 14 | Service Road | 빌딩, 건물 등의 시설 연결 도로 |
| 15 | Track Road | 농로, 임로 등의 길 |

### 2. 링크별 교통정보 속도
1. 실시간 속도
2. 통계 속도
3. 그 외 속도 정보 없음

### 3. TBT
1. 각 링크별 `maneuver` 정보에 턴 정보가 들어 있다.
2. Mapbox(글로벌) TBT 기준으로는 정보가 부족하다. (참고 자료는 이미지 항목)

방향 지시 유형(`maneuver`)

| 번호 | 방향 지시 유형 | 설명 |
|---|---|---|
| 0 | STRAIGHT | 직진 |
| 1 | SLIGHT RIGHT | 약간 우회전 |
| 2 | SLIGHT LEFT | 약간 좌회전 |
| 3 | TURN RIGHT | 우회전 |
| 4 | TURN LEFT | 좌회전 |
| 5 | SHARP RIGHT | 급격한 우회전 |
| 6 | SHARP LEFT | 급격한 좌회전 |
| 7 | U-TURN | 유턴 |
| -1 | UNSPECIFIED | 지정되지 않음 |

## 검토 내용
1. 도로 종별
   1. 도로 종별, pass 타입 등을 구분할 수 있는지 검토가 필요하다.
   2. 도로 종별을 표출하는 사양이 있는지 확인이 필요하다.
2. TBT
   1. 링크별 TBT 속성이 존재한다.
      1. 국내 탐색 기준의 turn 정보 존재 유무에 따른 안내에서 변경이 필요하다.
   2. 도로명 정보
      1. 요청 완료(MapReader에서 진행)
3. TomTom API 연동
   1. 경로 표출 가능
   2. 경로 내 턴 정보 표출 가능

## 결과값 참고 — 경로 응답 JSON 구조
원문은 대만 타이베이 좌표(경도 121.5, 위도 25.0 부근)의 샘플 경로 1건(경유지 1개)을 통째로 붙였다. 아래는 그 키 구조와 의미다. 의미는 값에서 추정한 것이 많다. ^[inferred]

### 최상위 키

| 키 | 타입 | 내용 |
|---|---|---|
| `resultCode` | int | 결과 코드. 샘플은 0 |
| `user_info` | object | 요청 조건 echo |
| `routes` | object | 경로 요약 |
| `links` | array | 경로를 이루는 링크 목록(샘플 177개) |
| `coordinates` | array | 경로 좌표열. `[경도, 위도]` 쌍(샘플 382개) |
| `type` | string | `LineString` (GeoJSON 형식 좌표열) |

### `user_info`

| 키 | 샘플 값 | 의미 |
|---|---|---|
| `start` | `{x: 121.520151, y: 25.035513}` | 출발지 좌표(x 경도, y 위도) |
| `end` | `{x: 121.564532, y: 25.033965}` | 도착지 좌표 |
| `option` | 1 | 탐색 옵션(값 의미는 원문에 없음) |
| `traffic` | 1 | 교통정보 반영 여부로 추정 |
| `viaList` | `[ [121.529796, 25.03169] ]` | 경유지 좌표 목록(1개) |

### `routes`

| 키 | 샘플 값 | 의미 |
|---|---|---|
| `distance` | 6732.38 | 총 거리(m로 추정). 첫 링크의 `distance`와 같다 |
| `spend_time` | 1654 | 소요 시간(초로 추정) |
| `fuel_consumption` | 0.84 | 연료 소모 |

### `links[]` 항목 키 (모든 링크 동일 9개 키)

| 키 | 타입 | 내용 |
|---|---|---|
| `id` | string | 링크 ID |
| `id_index` | string | 링크 인덱스 ID(15자리 수) |
| `osm_id` | string | 원본 OSM way ID. 같은 도로에 속한 링크는 같은 값을 갖는다 |
| `highway` | int | 도로 종별 코드(위 표) |
| `speed` | int | 링크 속도(교통정보 속도). 0이면 속도 정보 없음으로 추정 |
| `distance` | float | 해당 링크 시작 시점의 목적지까지 남은 거리로 보인다. 모든 링크에서 단조 감소(첫 값 6732.38 → 마지막 1.85) ^[inferred] |
| `node_id` | string | 노드 ID |
| `vertex_offset` | int | `coordinates` 배열에서 이 링크가 시작하는 인덱스(0, 3, 5, 7 … 마지막 380). ^[inferred] |
| `maneuver` | int | 이 링크에서의 방향 지시 코드(위 표) |

### 링크 샘플 (앞 3개와 마지막 1개)

| # | id | osm_id | highway | speed | distance | vertex_offset | maneuver |
|---|---|---|---|---|---|---|---|
| 0 | 886101269 | 31127861 | 8 | 26 | 6732.38 | 0 | 0 |
| 1 | 765363820 | 31127861 | 8 | 26 | 6545.30 | 3 | 0 |
| 2 | 454589379 | 31127861 | 8 | 26 | 6513.84 | 5 | 0 |
| 176 | 4259300494 | 544330076 | 14 | 0 | 1.85 | 380 | -1 |

### `coordinates` 샘플
앞 3개: `[121.52019, 25.03549]`, `[121.519357, 25.03408]`, `[121.519314, 25.034006]`. 마지막: `[121.563871, 25.034009]`. 같은 좌표가 연속으로 두 번 반복되는 구간이 많다(링크 경계 중복으로 추정).

### 샘플 응답 통계 (원문 JSON을 집계)
- 링크 177개, 좌표 382개, 서로 다른 `osm_id` 47개
- `highway` 분포: 6(Secondary) 81개, 8(Tertiary) 52개, 10(Residential) 24개, 14(Service) 19개, 7(Secondary Link) 1개. 0~5(고속·간선·주요도로)는 없음
- `maneuver` 분포: 0(직진) 159개, 3(우회전) 7개, 2(약간 좌회전) 4개, 4(좌회전) 3개, 1(약간 우회전) 2개, -1(지정 없음) 2개
- 링크 속도: 가장 많은 값은 16(링크 24개), 그다음 23(20개), 0(정보 없음)은 12개, 최댓값은 30. 속도 0 링크 12개는 모두 `highway` 14(Service)이다.

### `maneuver`가 0이 아닌 링크 전체 (18개)

| 링크 # | maneuver | 의미 | highway | 남은 거리 | speed | vertex_offset |
|---|---|---|---|---|---|---|
| 10 | 3 | 우회전 | 8 | 6199.03 | 16 | 21 |
| 19 | 3 | 우회전 | 10 | 5942.68 | 19 | 41 |
| 22 | 3 | 우회전 | 8 | 5874.60 | 17 | 53 |
| 49 | 2 | 약간 좌회전 | 8 | 4631.56 | 16 | 114 |
| 50 | 1 | 약간 우회전 | 8 | 4622.41 | 16 | 116 |
| 61 | 2 | 약간 좌회전 | 14 | 4351.83 | 15 | 138 |
| 66 | 4 | 좌회전 | 14 | 4203.16 | 0 | 148 |
| 68 | 4 | 좌회전 | 14 | 4172.14 | 18 | 152 |
| 69 | 3 | 우회전 | 14 | 4153.43 | 0 | 154 |
| 70 | -1 | 지정 없음 | 14 | 4059.13 | 0 | 158 |
| 72 | 3 | 우회전 | 14 | 4016.14 | 0 | 162 |
| 81 | 3 | 우회전 | 10 | 3825.81 | 6 | 181 |
| 150 | 2 | 약간 좌회전 | 6 | 840.36 | 15 | 327 |
| 155 | 1 | 약간 우회전 | 6 | 487.23 | 13 | 338 |
| 165 | 3 | 우회전 | 8 | 271.14 | 14 | 358 |
| 166 | 2 | 약간 좌회전 | 6 | 253.86 | 14 | 360 |
| 172 | 4 | 좌회전 | 6 | 70.32 | 14 | 372 |
| 176 | -1 | 지정 없음 | 14 | 1.85 | 0 | 380 |

## Related
- [[taiwan-routeserver-api]] — Taiwan RouteServer API 명세
- [[orbismap-route-and-tomtom-sdk-review-2025]] — Route/TomTom SDK 검토 요약
- [[tomtom-maps-sdk-api-review-detail]] — Maps SDK API 검토
- [[orbis-route-data-lib]] — 경로 데이터 라이브러리
- [[orbis-guidance-engine-dev-spec]] — 턴 코드 속성 규칙
- [[orbis-sdk]]

## Sources
- Confluence "OrbisMap Route 검토" (pageId 761167886) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
