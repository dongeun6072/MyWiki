---
title: >-
    Routing(Neon) 탐색 엔진 프로토콜
category: references
tags: [inavi-air, routing, protocol, visibility/internal]
aliases: [Routing Neon, 경로탐색 프로토콜, Neon]
relationships:
  - target: "[[inavi-mr-smr-network-data]]"
    type: uses
  - target: "[[inavi-air-api-detail-spec]]"
    type: related_to
sources: [~/Develop/Wiki/_raw/articles/project-air/[프로토콜]Routing(Neon)_v2.2.11.docx]
summary: >-
    서버와 경로탐색 엔진(Neon) 사이의 바이너리 요청/응답 규격 v2.2.11. 서비스 코드, 탐색 요청 헤더 비트 필드, 기능 변경 이력을 정리했다.
provenance:
  extracted: 0.80
  inferred: 0.20
  ambiguous: 0.00
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T09:14:00+09:00
updated: 2026-10-26T09:14:00+09:00
snapshots:
  - "[[_raw/_archived/[프로토콜]Routing(Neon)_v2.2.11.docx|[프로토콜]Routing(Neon)_v2.2.11.docx]]"
---

# Routing(Neon) 탐색 엔진 프로토콜

경로기술개발팀이 관리하는 탐색 엔진 프로토콜 문서(v2.2.11, 2026-06-10)다. 서버가 엔진에 바이너리 패킷으로 탐색을 요청하고 결과를 받는 규격이며, 앱이 호출하는 JSON API([[inavi-air-api-detail-spec]]) 뒤쪽에 있는 계층이다. ^[inferred] 엔진은 [[inavi-mr-smr-network-data]]의 MR 포맷 지도를 사용한다. 소속 프로젝트: [[inavi-air]].

## 문서 구성

1. 서비스 별 Protocol: Common Request → 탐색(Request/Response) → 버전 정보 → 관리 → 교통정보 → 부가기능
2. 첨부: Result Error Code 표

## Common Request (통신형만 사용, 8바이트)

| 항목 | 길이 | 설명 |
|---|---|---|
| Service Code | 1 | 아래 표 |
| 부가정보 | 1 | Reserved |
| Reserved | 2 | |
| Body 패킷 크기 | 4 | |

| Service Code | 서비스 | 설명 |
|---|---|---|
| 0 | 탐색 | 탐색 요청 |
| 1 | 버전정보 | 서버가 쓰는 MR 버전 요청(Body 크기 0) |
| 2 | 관리 | 교통정보 검증, 통제 입력과 검증 |
| 3 | 교통정보 | 유고정보, 구간 속도정보 |
| 4 | 부가기능 | 지점 정보 검증 |

## 탐색 Request 기본정보 (64바이트)

탐색옵션(40바이트 문자열), User ID(12), 탐색 시작 시간(4), 경유지 개수(2), 기존 경로 내 현재 위치 Link Index(2), 부가정보1(2), 부가정보2(1), 확장기능 개수(1) 순이다. 지점(출발/경유/도착 좌표)과 지점 명칭, 확장 기능 Header/Body가 뒤따른다.

**부가정보1 (16비트 플래그)**: 탐색 Type(0 일반, 1 재탐색-일반, 2 재탐색-교통, 3 재탐색-이탈), Smart 재탐색, 목적지 방향성 탐색, 회전규제 고려, 경로선 이원화, 요약결과 사용, 도로상 통행 제한지점 강제통과, 실수형 vertex, 추천·최소시간 동시 표출, 기존 탐색 결과 Type, 다중 입구점/목적지/출발지 Type, 출발지 각도 사용 프로젝션 등.

**부가정보2 (8비트 플래그)**: 좌회전/유턴 편의 탐색(다링크 회전 규제), 어린이 보호구역 회피, 출발지 좌표 기준 탐색방향 지정, 골목길 내 일방통행 무시, 출/도착지 좌표 기준 시간제 통행 규제 무시, 출/도착지 프로젝션 제외(고속도로, 자동차전용, 도시고속).

## 기능이 추가된 순서 (변경 이력 요약)

| 시기 | 버전 | 추가된 기능 |
|---|---|---|
| 2017-02 | 1.0 | 프로토콜 초안 |
| 2018 | 1.1~1.3 | 선호도로, 링크별 도로제한 flag, 교통 통제 정보 요청, 최소시간·추천 옵션 고도화 |
| 2019 | 1.4~1.7 | VMS용 구간 속도정보, 멀티 입구점/목적지/출발지 탐색 |
| 2020 | 1.8~2.1.4 | 출발지 각도 프로젝션, 좌회전/유턴 편의 탐색, 커스텀 경로 반영, 어린이 보호구역 회피, 사용자 설정 반영 |
| 2021 | 2.1.5~2.2.0 | 지점 정보 검증, 차량 용도별 탐색, 교통정보 세부 설정, 구간속도 부가정보 |
| 2022 | 2.2.1~2.2.3 | 최초 안내코드, 교차로까지 거리, N요약 탐색, 배민(Baemin) 서비스 |
| 2023~2024 | 2.2.4~2.2.5 | 배민/요기요 경유지 링크매칭, 온다(Onda) 배차실패 코드, User Private Key 확장 기능, 골목길 일방통행 무시, 응급차량 |
| 2025 | 2.2.6~2.2.9 | 출/도착지 시간제 규제 무시, 프로젝션 옵션, 위수지역 회피, DEM(고도) 반영 탐색 |
| 2026 | 2.2.10, 2.2.11 | Rid User Key, 사용자 정보에 차량 연료 종류 |

## 활용 메모

- 탐색 서비스 고객 이름(배민, 요기요, 온다, MXI Where)이 변경 이력에 나온다. 이 엔진은 AIR 앱뿐 아니라 여러 서비스가 공유하는 것으로 보인다. ^[inferred]
- 해외향(TomTom Orbis 데이터) 탐색은 같은 팀의 HTTP/JSON 규격으로 이어진다. 대응 관계는 [[orbis-routing-stack]]에 정리했다. ^[inferred]
- 문서 앞머리에는 버전이 2.2.10으로 적혀 있지만 변경 이력과 파일명은 2.2.11이다. ^[ambiguous]
- 응답 Body(Routing 정보 상세)와 Result Error Code 표는 분량이 커서 원본을 본다.

## Sources

- [[_raw/_archived/[프로토콜]Routing(Neon)_v2.2.11.docx]] — 탐색 엔진 프로토콜 원본
