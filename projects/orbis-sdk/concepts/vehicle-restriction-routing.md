---
title: >-
    차량 제원 기반 경로탐색 (트럭 탐색)
category: concepts
tags: [orbis-sdk, routing, truck, vehicle-restriction, visibility/internal]
aliases: [트럭 탐색, 차량 통행 제한 탐색, 차량 제원 옵션]
relationships:
  - target: "[[taiwan-routeserver-api]]"
    type: derived_from
  - target: "[[orbis-route-data-lib]]"
    type: related_to
sources:
  - ~/Develop/Wiki/_raw/articles/project-sdk/global-navigation/INAVI_RouteServer_for_Taiwan_RouteDataLib_Guide_And_Reference_v1_0_1_4.pdf
summary: >-
    차량 총중량, 높이, 길이, 전폭, 위험물 옵션으로 통행 불가 도로를 피하는 탐색 방식. 실패 코드 구조(출발/도착/경유 × 제한 종류)와 경유지 Strict/Bypass 모드를 정리했다.
provenance:
  extracted: 0.80
  inferred: 0.20
  ambiguous: 0.00
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T09:25:23+09:00
updated: 2026-10-26T09:25:23+09:00
snapshots:
  - "[[_raw/_archived/INAVI_RouteServer_for_Taiwan_RouteDataLib_Guide_And_Reference_v1_0_1_4.pdf|INAVI_RouteServer_for_Taiwan_RouteDataLib_Guide_And_Reference_v1_0_1_4.pdf]]"
---

# 차량 제원 기반 경로탐색 (트럭 탐색)

차량의 크기와 적재물을 요청에 넣으면 그 차량이 지나갈 수 없는 도로를 피해 탐색한다. [[taiwan-routeserver-api]] v2.0~2.3에 단계적으로 추가됐고, 해외향 Navi SDK의 트럭향 API([[orbis-sdk]], v1.0.2)와 연결된다. ^[inferred]

## 옵션

| 옵션 | 단위 | 효과 |
|---|---|---|
| `weight` | 톤(화물 포함 총중량) | 중량 제한 도로 회피 |
| `height` | m(전고) | 높이 제한 도로 회피 |
| `length` | m(전장) | 길이 제한 도로 회피 |
| `width` | m(전폭) | 전폭과 전장을 **함께** 주면 **회전 반경 제한 탐색**: 차량 크기에 비해 좁아서 회전이 어려운 도로를 최대한 피함 |
| `hazmat` | 0~3 | 1 모든 위험물, 2 폭발물, 3 수질오염물질 운송 제한 도로 회피 |

제한 정보의 출처는 도로 데이터의 링크 속성이다. [[orbis-route-data-lib]]의 링크 구조에 차량 **최대 무게, 높이, 길이 제한** 필드가 있고, 이 필드는 1.0.1.4(2026-02)에서 추가됐다. 규격의 2.0(2026-03) 차량 제원 옵션과 같은 시기다.

## 실패 코드 구조

결과 코드는 "**어디**(출발지, 목적지, 경유지) × **무엇**(제한 종류)"의 격자로 짜여 있다.

| 제한 종류 | 출발지 | 목적지 | 경유지 |
|---|---|---|---|
| 중량 | 11 | 12 | 13 |
| 높이 | 14 | 15 | 16 |
| 길이 | 17 | 18 | 19 |
| 위험물 | 20 | 21 | 22 |

해당 위치 주변 도로가 모두 그 제한에 걸려 **경로를 시작할 수 없을 때** 반환한다. 옵션을 입력했을 때만 적용된다. 이 구조 덕분에 앱은 코드만 보고 "목적지 근처가 높이 제한이라 갈 수 없습니다" 같은 메시지를 고를 수 있다. ^[inferred] 국내 에어 API의 결과 코드 `7`(경유지/목적지 높이·중량 제한)과 `40`(출발/경유지 근처 확장 실패)과 같은 발상이다. ([[inavi-air-api-overview]])

## 성공했지만 제약이 있을 때

경로 결과 상세 코드(`routeCode`):
- **10**: 설정한 전장/전폭으로 통행하기 어려운 회전 구간이 포함됨
- **20**: 경유지 주변에서 역주행이나 특수 회피 경로가 포함됨

제약이 없으면 `routeCode`는 `resultCode`와 같다. 즉 클라이언트는 `resultCode == 0`이어도 `routeCode`를 확인해 경고를 띄울 수 있다.

## 경유지 처리 모드 (`waypointroutingmode`, v2.3)

| 모드 | 동작 | 결과 |
|---|---|---|
| 0 Strict(법규 우선) | 경유지 주변 일방통행 역주행 등을 엄격히 제한 | 위반 시 실패, 코드 **23** |
| 1 Bypass(경로 유형 유지, 기본) | 경유지에 닿기 위해 필요하면 역주행이나 특수 회피를 허용 | 성공, 상세 코드 **20** |

트럭이나 위험물 차량은 법규를 우선해야 하므로 Strict, 일반 차량은 Bypass(기본)를 쓰는 식으로 나눌 수 있다. ^[inferred]

## 국내 탐색과의 차이

국내 탐색 엔진은 차량 용도별 탐색(2021), 응급차량(2023) 등을 **탐색 옵션 비트**로 지정한다([[inavi-routing-neon-protocol]]). 해외 규격은 **수치 제원(톤, m)** 을 직접 받는다. ^[inferred]

## Open Questions

- 제원 옵션을 입력하지 않으면 회피 탐색이 아예 수행되지 않는 것으로 읽힌다("옵션 입력 여부에 따라"). 기본값이 없는지 확인이 필요하다. ^[ambiguous]
- ORBISMAP Swagger([[orbismap-api-docs]])에는 `width`, `hazmat`이 아직 없다.

## Sources

- INAVI RouteServer for Taiwan API 설명서(탐색 서버 API 규격 v2.3) — 서버 주소가 들어 있어 원본 PDF를 보안 사유로 삭제했다 (2026-10-26)
- [[_raw/_archived/INAVI_RouteServer_for_Taiwan_RouteDataLib_Guide_And_Reference_v1_0_1_4.pdf]] — 링크 제한 속성
