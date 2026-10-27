---
title: >-
    MR 지도 데이터 포맷 v5.0
category: references
tags: [inavi-air, map-data, routing, visibility/internal]
aliases: [MR 포맷, MR Data Format, MR(X1, 통신향)]
relationships:
  - target: "[[inavi-smr-format-spec]]"
    type: related_to
  - target: "[[inavi-routing-neon-protocol]]"
    type: related_to
sources: [~/Develop/Wiki/_raw/articles/project-air/[포맷]MR(X1, 통신향)_v5.0_221123.docx]
summary: >-
    경로탐색용 MR 지도·교통정보 바이너리 포맷 v5.0의 파일 구성과 테이블 목록. 랭크(0~2)별 도엽 구조, 요금소, 교통정보 ID, 도로통제 파일을 정리했다.
provenance:
  extracted: 0.82
  inferred: 0.18
  ambiguous: 0.00
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T09:14:00+09:00
updated: 2026-10-26T15:30:00+09:00
snapshots:
  - "[[_raw/_archived/[포맷]MR(X1, 통신향)_v5.0_221123.docx|[포맷]MR(X1, 통신향)_v5.0_221123.docx]]"
  - "[[_raw/_archived/[포맷]MR(X1, 통신향)_v5.1.docx|[포맷]MR(X1, 통신향)_v5.1.docx]]"
  - "[[_raw/_archived/[포맷]MR(X1, 통신향)_v5.2.docx|[포맷]MR(X1, 통신향)_v5.2.docx]]"
---

# MR 지도 데이터 포맷 v5.0

IT개발그룹이 관리하는 경로탐색용 지도 데이터 포맷이다(v5.0, 2022-11-23, 파일명의 `X1, 통신향`은 통신형 탐색용이라는 뜻으로 보인다). ^[inferred] 탐색 엔진 [[inavi-routing-neon-protocol]]이 읽고, 2007년 v2.2부터 약 15년간 개정되어 왔다. 경량판은 [[inavi-smr-format-spec]], 두 포맷의 비교는 [[inavi-mr-smr-network-data]]에 있다. 소속 프로젝트: [[inavi-air]].

## 핵심 구조: 랭크와 도엽

- 지도는 **도엽(mesh, MapID)** 단위로 나뉜다. 도엽은 랭크 0, 1, 2에 걸쳐 있고, 상위 랭크(0, 1)는 넓은 범위의 간선 도로망, **하위 랭크(2)는 상세 도로망**이다. ^[inferred]
- 랭크 0, 1 도엽은 상위 랭크 도엽번호(MapID)와 하위 랭크 대응 레코드를 가진다. 상위에서 탐색하다 하위 랭크로 내려가는 구조에 쓰인다. ^[inferred]
- 파일 헤더에는 볼륨 구조 식별, 시스템 식별, 생성/갱신 일시가 있고, 도엽 위치정보 레코드를 랭크별로 따로 둔 이유는 "랭크마다 필요 없는 도엽 데이터를 버리기 위해서"라고 적혀 있다.

## 파일 구성

| 파일 | 내용 |
|---|---|
| `mrmanage.bin` | 랭크 도엽 관리 테이블(헤더, 랭크별 관리정보, 도엽 위치정보) |
| `mrrank0.bin`, `mrrank1.bin` | 랭크 0, 1: 노드, 링크, 인접 노드, 교차점 노드, 하위 랭크 대응 테이블 |
| `mrrank2.bin` | 랭크 2: 노드, 인접 노드, 교차점 노드, 링크 기본/안내/부가/선형/위치 정보 |
| `mrexguide.bin` | 랭크 2 링크 확장 안내 정보 |
| `mrvertex.bin` | 보간점(링크 모양) 리스트 |
| `mrexinfo.bin` | 부가정보: 차선, 방면, 가로명, 요금소 원본, 도로명, 3D 확대도, 복잡한 출구, 고저, 버스 전용차로, VoiceTurn, 로터리 출구 번호, 차로유도선 방면/색상 |
| `tolltable.bin` | 요금소 테이블(개방/폐쇄, 예외형, 시간대별, 하이패스 예외형 요금) |
| `ctstolltable.bin` | 연속 통행 테이블(v5.0 추가: 시작/도착 요금소, 할인) |

## 교통정보 관련

- 교통정보 ID 테이블(`trf_~2.bin`), 하판(랭크 2) 인덱스(`trfidx_~2.bin`), 상판(랭크 0, 1) ID 매칭/인덱스 테이블
- **DARC** Link/Node ID 구성: 링크 종별, 대권역/중권역 행정코드, 고속도로 노선 코드
- TCON 매칭(`trf_tconmatch.bin`), CTT SUM 매칭(`trf_csmatch_y.bin`, `trf_csmatch_m.bin`), 휴일정보(`holiday.bin`)

## 도로 규제 관련

- `roadblocking_vehicle.bin`: 트럭 도로통제(중량 제한 값, 시간대별 통제정보)
- `roadblocking_time.bin`: 시간대별 도로통제
- `dalink.bin`: 다링크 회전제한(랭크 0~2 링크 정보)
- `vr_zoom.bin`: VR 확대도 지점
- `preference_road.bin`: 선호도로

규제 데이터는 [[inavi-routing-neon-protocol]]의 탐색 옵션(시간제 통행 규제, 회전 규제, 선호도로)과 짝을 이룬다. ^[inferred]

## 변경 이력 요약

2007 포맷 문서 분리 → 2010 신규 포맷(3.0) → 2013 회전규제, 고속모드 → 2014 시간대별 통제, 높이/중량 제한 → 2016 다링크 회전규제 → 2017 하이패스 전용, VoiceTurn, VR 확대도, 차로유도선 → 2018 링크 확장 안내, 선호도로 → 2020 트럭 통행 제한, 분리 유턴 대향차선 → 2022 연속 통행 테이블(v5.0).

## Open Questions

- 노드/링크 레코드의 비트 단위 필드 정의는 이 페이지에 옮기지 않았다(원본 1.2 이후). 구현이 필요하면 원본을 보고, [[inavi-smr-format-spec]]의 단순화된 구조와 비교하면 이해가 빠르다.
- 헤더에 NAVTEQ, EURO 같은 문자열이 예시 값으로 남아 있다. 과거 포맷 템플릿의 잔재로 보인다. ^[ambiguous]

## v5.1과 v5.2 변경 (보강)

| 버전 | 일자 | 내용 |
|---|---|---|
| 5.0 | 2022-11-23 | 연속 통행(할인) 테이블 추가 |
| 5.1 | 2023-01-12 | **보호구역 속성** 추가 |
| 5.2 | 2024-01-11 | **도로제한속도 부가정보** 추가 |

- v5.1 본문은 링크 기본 정보의 보호구역 정보(어린이 보호구역 스쿨존, 보호구역 확장 코드 등)를 다룬다. v5.1과 v5.2는 표지 부서명 외에 **부가정보 ID 29(정방향 도로제한속도), 30(역방향)** 항목과 "도로제한속도 데이터"(문자열 1필드) 레코드 정의만 v5.2에 늘었다. 나머지는 같다.
- 문서 후반에는 CTT SUM 매칭 테이블(`trf_csmatch_y/m.bin`)이 있다. 2025년의 CTT 목록 파일은 [[daegu-traffic-light-protocol]]에서 다룬다.
- 2023-10 메일의 v5.1 "도로급수 필드 제거" 논의는 [[air-map-data-and-safety-guidance-2023]]을 본다.

## Sources

- [[_raw/_archived/[포맷]MR(X1, 통신향)_v5.0_221123.docx]] — MR 포맷 원본
- [[_raw/_archived/[포맷]MR(X1, 통신향)_v5.1.docx]] — v5.1(보호구역 속성)
- [[_raw/_archived/[포맷]MR(X1, 통신향)_v5.2.docx]] — v5.2(도로제한속도 부가정보)
