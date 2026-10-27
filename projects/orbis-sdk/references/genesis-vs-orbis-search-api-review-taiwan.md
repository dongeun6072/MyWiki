---
title: >-
    Genesis 검색 API 검토 (대만 POI, Genesis vs Orbis)
category: references
project: orbis-sdk
tags: [search-api, genesis, orbis, taiwan, poi, visibility/internal]
aliases: [Genesis 검색 API 검토]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1503526933
summary: >-
    대만 지역에서 Genesis와 Orbis 검색 API를 한국어·영어·번체로 비교한 POI 10건 테스트와 검토 결과
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

# Genesis 검색 API 검토 (대만 POI)

대만 서비스를 위한 검색 API로 Genesis와 Orbis(TomTom 기반 API)를 비교한 검토(2025-12-11 수정)다. 대만 현지 평가는 [[taiwan-field-evaluation-detail]], Taiwan RouteServer는 [[taiwan-routeserver-api]], 목차는 [[orbis-design-and-review-hub]].

## 테스트 조건
- 요청 파라미터: `CountrySet: TW`, `Language: ko-KR`
- 검색 결과 비교 대상: Genesis / Orbis API
- POI 테스트: `CountrySet: TW`, `Language: zh-TW`
- 스크린샷 순서: Genesis 검색(첫 번째 항목) / Orbis 검색(첫 번째 항목) / 실제 POI 위치(구글지도). 스크린샷은 이미지 항목이라 옮기지 않았다.

## POI별 결과

| # | POI | 결과 |
|---|---|---|
| 1 | Elephant Mountain (象山) | Genesis는 전망대 POI가 표출된다. Orbis는 두 번째 항목에서 정식 POI 명칭이 표출된다. |
| 2 | Fo Guang Shan Buddha Museum (佛光山佛陀紀念館) | 동일한 목적지 POI 명이지만 목적지 좌표와 주소가 다르다. |
| 3 | Ximending (西門町) | 동일한 목적지 POI 명이고 주소가 다르게 표출된다(Orbis는 `StreetNumber`가 없다). |
| 4 | Raohe Street Night Market (饒河街 觀光夜市) | Genesis는 두 번째 항목이 정식 POI 명칭이다. |
| 5 | Chimei Museum (奇美博物館) | Orbis와 Genesis 모두 의도한 목적지가 나오지 않는다(번체로 검색하면 정상). Orbis는 두 번째 항목에서 奇美博物館이 표출되고, Genesis는 해당 POI 항목이 나오지 않는다. |
| 6 | Shilin Night Market (士林夜市) | Orbis의 POI 명칭이 다르다. |
| 7 | Taipei City mall (台北地下街) | 둘 다 의도한 목적지가 나오지 않는다. 번체로 테스트하면 정상. |
| 8 | PX MART Yuanhuan Store (全聯福利中心 圓環店) | 둘 다 의도한 목적지가 나오지 않는다. 번체로 검색하면 Genesis는 두 번째 항목, Orbis는 네 번째 항목에서 표출된다. |
| 9 | 國立故宮博物院 (국립고궁박물원) | Orbis는 두 번째 항목에서 정식 POI 명칭이 표출된다. |
| 10 | 臺灣桃園國際機場 (타이완 타오위안 국제공항) | 원문에 결과 기술 없음. |

## 검토 결과
- **한국어 검색 결과**: Genesis API로 한국어 검색 시 제공하는 POI가 Orbis보다 적다. 예: `타이페이`로 검색하면 Genesis에서는 아무것도 표출되지 않는다.
- **검색 결과 특성**
  - Orbis API: 검색 결과의 주소와 POI명이 한글과 영어 형태로 많이 표시된다.
  - Genesis API: 검색 결과가 간체/번체 중국어 형태로 많이 표시된다.
- **일치도**: 목적지 자체는 대체로 양 API 모두 같은 위치를 반환한다. 예: Starbucks로 검색하면 동일한 POI가 5개 정도 존재하는 것을 확인했다.

## Related
- [[taiwan-routeserver-api]] — 대만 경로 서버 API
- [[orbismap-api-docs]] — OrbisMap API
- [[taiwan-field-evaluation-detail]] — 현지 평가 상세
- [[orbis-sdk]]

## Sources
- Confluence "Genesis 검색 API 검토" (pageId 1503526933) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
