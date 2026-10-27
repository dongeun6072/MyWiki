---
title: >-
    ORBISMAP API 문서 (Swagger)
category: references
tags: [orbis-sdk, api, tomtom, swagger, visibility/internal]
aliases: [ORBISMAP API, orbismap, Orbis Swagger]
relationships:
  - target: "[[orbis-routing-stack]]"
    type: related_to
  - target: "[[taiwan-routeserver-api]]"
    type: related_to
sources: [~/Develop/Wiki/_raw/articles/project-sdk/global-navigation/ORBISMAP API DOCS (Agent, Swagger).md]
summary: >-
    해외향 SDK가 호출하는 ORBISMAP 서버의 OpenAPI 3.0 명세. JWT 인증, 서비스 게이트, 경로탐색, TomTom 검색·안전카메라 프록시 17개 엔드포인트를 정리했다.
provenance:
  extracted: 0.90
  inferred: 0.10
  ambiguous: 0.00
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T09:25:23+09:00
updated: 2026-10-26T09:25:23+09:00
snapshots:
  - "[[_raw/_archived/ORBISMAP API DOCS (Agent, Swagger)|ORBISMAP API DOCS (Agent, Swagger)]]"
---

# ORBISMAP API 문서 (Swagger)

OpenAPI 3.0.1 형식(파일은 `.md`지만 내용은 JSON)으로 된 `ORBISMAP API DOCS` 1.0이다. 서버는 `[HOST]`이고 모든 호출은 JWT Bearer 인증을 쓴다. 해외향 SDK([[orbis-sdk]])가 서버와 통신하는 창구로 보인다. ^[inferred] 전체 구조는 [[orbis-routing-stack]]에 있다.

## 엔드포인트 (17개)

| 태그 | URL | 설명 |
|---|---|---|
| Auth | `POST /api/auth` | imaps 인증과 JWT 발급. 요청 `appKey`, `pkgName`, `uniqueKey` → 응답 `accessToken`와 지도 스타일 JSON URL(라이트/다크) |
| System | `POST /api/serviceGate` | 초기 구동 정보. 맵 버전, 지도 데이터 CDN URL, 국가 코드, TomTom 검색 타입(0 Genesis, 1 Orbis) |
| Route | `POST /api/searchRoute` | 경로 탐색(최적 경로) |
| Route | `POST /api/searchRoute/multi` | 다중 경로(최적 경로 포함 **최대 3개**, 대안이 없으면 더 적게) |
| TomTom | `POST /api/tomtom/search/{geocode, reverse-geocode, poi, nearby, fuzzy, category}` | Orbis 검색 |
| TomTom | `POST /api/tomtom/search/genesis/{geocode, reverse-geocode, fuzzy}` | Genesis 검색 |
| TomTom | `POST /api/tomtom/safety-camera/{fixed, mobile}` | 고정식, 이동식 안전카메라 |
| TomTom | `GET /api/tomtom/key` | TomTom 키 전달 전용 |
| Common | `GET /api/health` | AWS 로드밸런서 헬스체크 |

TomTom 검색은 서버가 TomTom API를 중계(프록시)하는 구조다. 검색 요청 필드는 TomTom 검색 API와 같다: `query`, `lat`, `lon`, `radius`, `language`, `view`(지정학적 견해), `typeahead`, `categorySet`, `brandSet`, EV 충전 필터(`connectorSet`, `minPowerKW`, `maxPowerKW`) 등. ^[inferred]

## 호출 흐름

1. **`/api/auth`**로 `appKey`, 패키지명, 고유키를 보내 `accessToken`(JWT)과 지도 스타일 URL을 받는다.
2. **`/api/serviceGate`**로 맵 버전과 지도 데이터 URL, 검색 타입을 받는다. (요청 필드 `smr_ver`, `smdc_ver`, `gp_ver`, `clause_ver` 등은 국내 에어 앱의 `serviceGate`와 같은 형태다. [[inavi-air-api-detail-spec]])
3. 이후 검색과 경로탐색 API를 Bearer 토큰으로 호출한다.

## 경로탐색 요청 (`/api/searchRoute`)

필수는 `startX`, `startY`, `endX`, `endY`, `traffic`이다. 그 밖에 `viaList`, `directionangle`, `sideroadstart`, `sideroadend`, 차량 제원 `weight`, `height`, `length`를 받는다. 다중 경로는 `routecount`(요청 경로 수)가 추가된다. 응답은 단일 경로가 `routes`와 `links`, 다중 경로가 GeoJSON `features` 배열이다. 이 Swagger에는 [[taiwan-routeserver-api]] v2.3의 `width`, `hazmat`, `waypointroutingmode` 옵션이 아직 없다. ^[inferred] 규격 쪽이 먼저 진화한 것으로 보인다.

## 메모

- 서비스 게이트의 `smr_ver`는 국내의 sMR 포맷([[inavi-smr-format-spec]])을 가리키는 값으로 보인다. 해외향 서버가 국내 에어 앱의 게이트 구조를 재사용했을 가능성이 있다. ^[inferred]
- 인증 응답에 지도 스타일 JSON URL이 포함되어 있어, SDK 지도 다국어/스타일 연동(웹 인증 기반 Style)과 이어진다. ([[orbis-sdk]] v1.0.4 항목) ^[inferred]

## Open Questions

- 응답 스키마 72개 중 TomTom 검색 응답 상세는 TomTom 공식 문서와 같다고 가정하고 옮기지 않았다.
- 운영 서버와 개발 서버 구분은 이 문서에 없다(servers 항목이 하나뿐).

## Sources

- [[_raw/_archived/ORBISMAP API DOCS (Agent, Swagger).md]] — OpenAPI 명세 원본
