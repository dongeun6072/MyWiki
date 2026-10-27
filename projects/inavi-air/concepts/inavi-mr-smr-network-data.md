---
title: >-
    MR과 sMR 네트워크 데이터 비교
category: concepts
tags: [inavi-air, map-data, routing, visibility/internal]
aliases: [MR vs sMR, 탐색용 지도 데이터]
relationships:
  - target: "[[inavi-mr-format-spec]]"
    type: derived_from
  - target: "[[inavi-smr-format-spec]]"
    type: derived_from
sources:
  - ~/Develop/Wiki/_raw/articles/project-air/[포맷]MR(X1, 통신향)_v5.0_221123.docx
  - ~/Develop/Wiki/_raw/articles/project-air/sMR_Format_v2_0.doc
summary: >-
    경로탐색용 지도 데이터 두 종류의 차이. MR은 랭크 0~2와 교통, 요금, 규제 정보를 담은 본 포맷이고, sMR은 도엽 단위의 단순한 네트워크 포맷이다.
provenance:
  extracted: 0.55
  inferred: 0.45
  ambiguous: 0.00
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T09:14:00+09:00
updated: 2026-10-26T09:14:00+09:00
snapshots:
  - "[[_raw/_archived/[포맷]MR(X1, 통신향)_v5.0_221123.docx|[포맷]MR(X1, 통신향)_v5.0_221123.docx]]"
  - "[[_raw/_archived/sMR_Format_v2_0.doc|sMR_Format_v2_0.doc]]"
---

# MR과 sMR 네트워크 데이터 비교

탐색 엔진([[inavi-routing-neon-protocol]])이 쓰는 도로 네트워크 데이터에는 두 포맷 문서가 있다. 같은 도로망(노드, 링크, 보간점)을 표현하지만 담는 범위가 다르다. 소속 프로젝트: [[inavi-air]].

## 비교

| 항목 | MR ([[inavi-mr-format-spec]]) | sMR ([[inavi-smr-format-spec]]) |
|---|---|---|
| 버전 | v5.0 (2022-11) | v2.0 |
| 랭크 | 0, 1, 2 (상위 랭크로 넓은 범위, 하위로 상세) | 없음 (도엽 하나가 전부) |
| 파일 | 도로망, 부가정보, 요금소, 연속통행, 교통정보 ID, 도로통제 등 20여 종 | `smrmanage`, `smrmeshinfo`, `smrmeshdata` 3개 |
| 안내 정보 | 링크 안내, 확장 안내, 방면, 차로유도선, 3D 확대도, VoiceTurn | 없음 |
| 규제/요금 | 시간대별 통제, 트럭 중량 제한, 다링크 회전제한, 요금소 | 링크 속성 비트(통행 코드, 터널/교량 등)와 교차로 통행 코드 |
| 교통정보 | DARC Link/Node ID 매칭, 구간 속도 | 없음 |
| 좌표 | 도엽 기준 offset | 0.01초 단위 정수, 도엽 기준 offset |

## 해석

- MR은 **서버 탐색과 안내에 필요한 모든 정보**를 담은 본 포맷으로 보이고, sMR은 **경로 계산에 필요한 최소한의 위상(topology)** 만 담은 단순 포맷으로 보인다. 정확한 용도 구분(어느 엔진이 sMR을 쓰는지)은 문서에 없다. ^[inferred]
- 둘 다 링크 속성에 도로 종별(고속도로/도시고속/기타), 터널·교량 같은 구조 속성을 둔다. 탐색 옵션의 "고속도로 우선", "무료도로", "초보자(편한길)" 같은 선택이 이 속성을 이용하는 것으로 보인다. ^[inferred] ([[inavi-air-api-detail-spec]]의 탐색 옵션 참고)
- sMR의 `smrmanage.bin`은 MR의 `mrmanage.bin`과 대응하는 도엽 관리 파일이다. ^[inferred]

## Open Questions

- sMR이 SMR 엔진 문서(`SMR 엔진.md`)에서 어떤 역할인지는 이번 수집 대상에 없어서 확인하지 못했다.

## Sources

- [[_raw/_archived/[포맷]MR(X1, 통신향)_v5.0_221123.docx]] — MR 포맷
- [[_raw/_archived/sMR_Format_v2_0.doc]] — sMR 포맷
