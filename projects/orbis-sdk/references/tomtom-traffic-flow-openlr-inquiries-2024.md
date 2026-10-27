---
title: >-
    TomTom Traffic Flow(OpenLR) 질의응답: OSM ID·길이·offset 매핑
category: references
project: orbis-sdk
tags: [orbis-sdk, tomtom, traffic, openlr, taiwan, visibility/internal]
aliases: [TT traffic flow inquiries, OpenLR OSM ID 매핑]
relationships:
  - target: "[[orbis-route-data-lib]]"
    type: related_to
  - target: "[[taiwan-routeserver-api]]"
    type: related_to
sources:
  - "[[_raw/_archived/TT traffic flow_inquiries_inavi_11thMar2025_tt.xlsx]]"
summary: >-
    TomTom Live Services 교통 흐름(Traffic Flow) 데이터를 Orbis 지도 링크(OSM ID)에 매핑할 때 생긴 질문과 TomTom 답변을 정리했다(2025-03-11 정리본).
provenance:
  extracted: 0.8
  inferred: 0.2
  ambiguous: 0.0
base_confidence: 0.55
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T14:00:00+09:00
updated: 2026-10-26T14:00:00+09:00
snapshots:
  - "[[_raw/_archived/TT traffic flow_inquiries_inavi_11thMar2025_tt.xlsx|TT traffic flow_inquiries_inavi_11thMar2025_tt.xlsx]]"
---

# TomTom Traffic Flow(OpenLR) 질의응답

아이나비 경로 개발 쪽이 TomTom Live Services의 교통 흐름 피드를 [[orbis-route-data-lib]]의 링크(OSM ID)에 붙이는 과정에서 TomTom에 보낸 질문 시트다(한·영 병기, 2024-07~09 확인한 데이터 기준). 각 질문에 참고 이미지, TomTom 답변, 비고 열이 있다.

## 핵심 질문과 답

| 주제 | TomTom 답변 요지 |
|---|---|
| 같은 OSM ID가 여러 개일 때 연결성 | 동일 OSM ID가 모두 연결된다고 보장하지 않으며 확인 중이라고 답했다. 교통정보는 Orbis 지도 기준이고 Orbis는 Overture Maps, 그 바탕은 OSM이라 도로망이 OSM과 매우 비슷하다 |
| 피드의 위치 표현 | **OpenLR** 참조와 `lengthInMeters`로 위치를 준다. OpenLR가 표현하는 도로 전체 길이에서 `startOffsetInMeters`와 `endOffsetInMeters`만큼 앞뒤를 **잘라서(trim)** 써야 한다 |
| 길이 계산 | 링크 길이는 도로 geometry 전체 길이이며 PostGIS의 `ST_Length`로 구할 수 있다 |
| 생성 주기 | 융합 엔진(Fusion Engine)이 약 30초마다 교통정보를 만든다 |
| offset 합이 전체 길이보다 큰 경우 | 회전교차로 외에도 offset 합이 total length를 넘는 사례가 보고됐고, 일부는 융합 엔진과 최신 OSM의 길이 차이 때문이라며 9월 새 버전에서 해결 예정이라고 답했다. 대만 Orbis 지도 갱신 뒤에도 재발해 재오픈됐다 |
| `flowType` | `ff`(free flow)에만 `segmentId` 구간이 포함되고 `nff`에는 없다. 그래서 OpenLR와 OSM ID의 **매핑 테이블**을 두는 편이 낫다고 했다 |
| 매핑 갱신 주기 | 확정은 아니나 지도 업데이트와 연동돼 약 2주 단위. 클라이언트 ID가 바뀌어도 대부분 위치 참조는 바뀌지 않는다 |
| 매핑 테이블 예 | TomTom이 참고용으로 제시: FreeFlow Overview/Details와 OpenLR Mapping 테이블을 만들고, `startOffset` 기준으로 OSM ID별 속도·통행 시간(FreeFlow_OSM_Speed)을 구한 뒤, 빠진 OSM ID를 채워 NonFreeFlow_OSM_Speed를 만든다 |

## 이 페이지의 쓰임

대만 경로 서버의 실시간 교통 반영 설계([[taiwan-routeserver-api]])에서 OpenLR를 링크 시퀀스로 변환할 때 offset 처리와 매핑 테이블 갱신 주기를 판단하는 근거다. ^[inferred]

## Sources

- [[_raw/_archived/TT traffic flow_inquiries_inavi_11thMar2025_tt.xlsx]]
