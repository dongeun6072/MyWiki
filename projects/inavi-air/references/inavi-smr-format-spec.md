---
title: >-
    sMR 네트워크 데이터 포맷 v2.0
category: references
tags: [inavi-air, map-data, routing, visibility/internal]
aliases: [sMR 포맷, sMR Format, SMR 엔진 네트워크 데이터]
relationships:
  - target: "[[inavi-mr-format-spec]]"
    type: related_to
sources: [~/Develop/Wiki/_raw/articles/project-air/sMR_Format_v2_0.doc]
summary: >-
    sMR 네트워크 데이터 포맷 v2.0. 도엽 관리/패키지 정보/패키지 데이터 3개 파일과 노드, 링크, 보간점 레코드, 링크 속성 비트 정의를 정리했다.
provenance:
  extracted: 0.88
  inferred: 0.12
  ambiguous: 0.00
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T09:14:00+09:00
updated: 2026-10-26T09:14:00+09:00
snapshots:
  - "[[_raw/_archived/sMR_Format_v2_0.doc|sMR_Format_v2_0.doc]]"
---

# sMR 네트워크 데이터 포맷 v2.0

[[inavi-mr-format-spec]](MR)보다 단순한 네트워크 데이터 포맷이다. 랭크 구분이 없고 도엽(mesh) 하나에 노드, 링크, 보간점이 들어 있다. 두 포맷의 차이는 [[inavi-mr-smr-network-data]]에 정리했다. 소속 프로젝트: [[inavi-air]].

## 파일 구성

| 파일 | 내용 |
|---|---|
| `smrmanage.bin` | 도엽 관리 테이블: 헤더(256바이트) + 도엽 관리 정보 + 도엽 위치 정보 레코드(도엽마다 36바이트) |
| `smrmeshinfo.bin` | 도엽 패키지 정보: 도엽 ID(2), 해당 도엽 데이터 DS(4), 데이터 크기(4) |
| `smrmeshdata.bin` | 도엽 패키지 데이터: 도엽마다 노드, 교차점 노드, 인접 노드, 링크, 보간점 레코드 테이블 |

각 테이블은 맨 앞에 4바이트 Checksum을 둔다.

## 좌표와 단위

- 도엽 경계 좌표는 **0.01초 단위 경위도 정수**다. 헤더에 지도 중심 좌표, 도엽 Width/Height, 전체 영역 좌/하/우/상단이 들어 있다.
- 도엽의 **X축 실거리비** = 도엽 하단 길이(미터) ÷ 도엽 폭(0.01초)에 100000을 곱해 정수로 저장한다.
- 노드의 경위도는 도엽 좌단 경도/하단 위도에서의 offset이고, 보간점은 직전 점에서의 offset(signed short, 음수 가능)이다. 좌표를 작은 offset으로 저장해 용량을 줄이는 방식이다. ^[inferred]

## 레코드 구조

- **도엽 위치 정보**: 도엽 내 노드/링크 개수, X축 실거리비, 좌단 경도, 하단 위도, 그리고 노드·교차점 노드·인접 노드·링크·보간점 테이블 offset
- **노드**: 경도 offset(2), 위도 offset(2), 인접 링크 개수 + 확장 노드 레코드 offset(4). offset의 31번째 비트가 0이면 교차점, 1이면 인접 노드이고, 30번째 비트는 상위 랭크 대응 노드 여부다.
- **교차점 노드**: 링크 ID 목록과 링크별 교차점 통행 코드(0 불가, 1 통행 가능). 일방통행 여부를 반영한 값이며 진북 기준 시계 방향 순서로 나열한다.
- **인접 노드**: 인접 도엽 ID, 인접 도엽의 연결 노드 ID와 링크 ID (도엽 경계를 넘어 이어주는 용도)
- **링크**: 시작/종료 노드 ID, 길이(m), 링크 속성(16비트), 보간점 개수, 보간점 리스트 index

### 링크 속성 비트

| 비트 | 내용 |
|---|---|
| 10~13 | 차선 수 |
| 8~9 | 링크 통행코드: 양방 가능 / 정방향만 / 역방향만 / 양방 불가 |
| 7 | 본선 분리 여부 |
| 5~6 | 링크 종별: 본선, 램프, 연결로, 교차로 내 링크 |
| 2~4 | 링크 속성: 없음, 고가차도, 지하차도, 터널, 톨게이트, 교량, 단지 내 도로, 휴게소 |
| 0~1 | 도로 종별: 없음, 고속도로, 도시고속도로, 기타 |

## Open Questions

- 이 문서는 .doc 파일에서 텍스트를 추출했기 때문에 표의 열 정렬이 깨졌다. 길이/offset 값은 항목 순서로 확인했고, 정확한 바이트 offset이 필요하면 원본 표를 열어 본다. ^[ambiguous]
- 대응하는 `SMR 엔진.md`, `네트워크 데이터 (MR, SMR).md` 문서는 이번 수집 대상에 없다.

## Sources

- [[_raw/_archived/sMR_Format_v2_0.doc]] — sMR 포맷 원본
