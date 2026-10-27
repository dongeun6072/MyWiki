---
title: >-
    Orbis Route Data Library 레퍼런스 v1.0.1.4
category: references
tags: [orbis-sdk, routing, library, tomtom, visibility/internal]
aliases: [OrbisRouteDataLib, RouteDataLib, orbisroute]
relationships:
  - target: "[[orbis-routing-stack]]"
    type: related_to
  - target: "[[taiwan-routeserver-api]]"
    type: related_to
sources: [~/Develop/Wiki/_raw/articles/project-sdk/global-navigation/INAVI_RouteServer_for_Taiwan_RouteDataLib_Guide_And_Reference_v1_0_1_4.pdf]
summary: >-
    TomTom Orbis Maps 도로 네트워크 데이터(링크, 노드, 회전 제한)를 읽는 C++/Android 라이브러리의 메서드와 구조체 정리. 버전 1.0.1.4(2026-02).
provenance:
  extracted: 0.88
  inferred: 0.12
  ambiguous: 0.00
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T09:25:23+09:00
updated: 2026-10-26T14:30:00+09:00
snapshots:
  - "[[_raw/_archived/INAVI_RouteServer_for_Taiwan_RouteDataLib_Guide_And_Reference_v1_0_1_4.pdf|INAVI_RouteServer_for_Taiwan_RouteDataLib_Guide_And_Reference_v1_0_1_4.pdf]]"
  - "[[_raw/_archived/INAVI_RouteServer_for_Taiwan_RouteDataLib_Guide_And_Reference_v1_0_0_2.pdf|INAVI_RouteServer_for_Taiwan_RouteDataLib_Guide_And_Reference_v1_0_0_2.pdf]]"
---

# Orbis Route Data Library 레퍼런스 v1.0.1.4

경로 탐색 서비스 데이터의 **링크와 노드 상세 정보**를 앱이나 서버에서 읽기 위한 라이브러리 가이드다(25쪽, 경로기술개발팀, Confidential). 탐색 API 응답의 링크 ID로 상세 속성을 찾을 때 쓴다. ^[inferred] 전체 구조는 [[orbis-routing-stack]], 탐색 API는 [[taiwan-routeserver-api]]에 있다.

## 제공 형태

| 환경 | 파일 |
|---|---|
| Windows | `OrbisRouteDataLib.lib` (정적) |
| Linux | `libOrbisRouteDataLib.a` (정적) |
| Android | `liborbisroute.so` (패키지 `com.inavi.orbisroute`, 클래스 `OrbisRouteNative`) |

문서의 `[J]` 표시는 Android Java 쪽 이름과 자료형이 다를 때의 설명이다.

## 데이터 파일

`OpenOrbisNetwork(dirname)`이 아래 파일이 있는 디렉터리를 연다. 파일은 **Orbis Road Network Converter**가 생성한다.

| 파일 | 내용 |
|---|---|
| `GenNetLink.gem` | 링크 |
| `GenNetNode.gem` | 노드 |
| `RoadTurnInfo.dat` | 회전 제한(진입 링크 기준, To) |
| `RoadTurnInfoB.dat` | 회전 제한(출발 링크 기준, From) |

## 메서드

| 분류 | 메서드 |
|---|---|
| 열기/닫기 | `OpenOrbisNetwork`, `CleanOrbisNetwork` |
| 조회 | `GetDataLink`, `GetDataNode`(인덱스로), `GetDataLinkNearPt`, `GetDataNodeNearPt`(좌표 근처 최소 거리), `GetDataLinkRect`, `GetDataNodeRect`(사각형 영역) |
| 회전 제한 | `isTurnInfo`, `GetListTurnInfoTo`, `GetListTurnInfoFrom` |
| 범위 | `GetExtentLink`, `GetExtentNode`, `GetDataLinkID`, `GetDataNodeID`(ID 최소/최대) |
| 계산 | `CalcTurnAngle`(진입/진출 링크 사이 회전 각도) |
| 부가 | `GetRoadNameByNameID`, `GetRoadNameByLinkIndex`, `GetMapVersion` |

## 구조체

**`stOrbisLink`** (Java `OrbisLink`): 링크 ID와 시작/종료 노드 index, OSM ID, 도로 종별(`_road_rank` 0~15, OSM 분류), 차로 수, 제한속도(10km/h 단위, 12 = 120km/h), 경로 레벨(0~5, TomTom Orbis가 설정), 다리/터널 여부, 회전교차로 여부(0 기타, 1 회전 교차로, 2 회전 교차로 연결 링크), 교차로 내 도로 여부, 링크 종별, 도로명 ID, 링크 길이, 차량 **최대 무게/높이/길이 제한**(1.0.1.4에 추가). 링크 각도 계산 예제도 있다.

**`stOrbisNode`**: 노드 정보(위치와 연결 링크).

링크와 노드의 ID index는 **원본 데이터의 ID가 아니라 변환기가 만든 index**다. 원본 ID는 `[J]linkID` 같은 별도 필드에 있다.

## 초기 버전(1.0.0.2, 2025-02-19) 참고

초기 배포본 가이드는 최초 1.0.0.1(02-18)에 이어 `GetExtentLink()`, `GetExtentNode()`(링크·노드 extent 조회)를 추가한 1.0.0.2였다. 당시 메서드는 네트워크 열기·정리(`OpenOrbisNetwork`, `CleanOrbisNetwork`), ID/근접점/사각형 영역으로 링크·노드 조회, 회전 제한 확인·목록(`isTurnInfo`, `GetListTurnInfo`)까지 12개였고, 도로명·`CalcTurnAngle`·`GetMapVersion`은 이후 버전에서 늘었다. 작성은 경로기술개발팀이다.

## 버전 이력 요약

| 시기 | 버전 | 변경 |
|---|---|---|
| 2025-02 | 1.0.0.1~1.0.0.5 | 최초 배포, extent·좌표(vertex), 회전 제한 조회, 영역 조회, `CalcTurnAngle` |
| 2025-04 | 1.0.0.6 | Android 라이브러리, 도로명 조회 |
| 2025-06 | 1.0.0.7 | 링크 속성(도로명 ID, 길이), 링크 각도 예제 |
| 2025-07 | 1.0.0.8 | `GetMapVersion` |
| 2026-02 | 1.0.1.4 | 차량 최대 무게/높이/길이 제한 속성 |

[[taiwan-routeserver-api]]의 서비스 데이터 라이브러리 버전(1.0.1.4 ~ 1.0.1.6)이 이 문서 버전과 같은 계열이다. 1.0.1.5와 1.0.1.6은 이 문서에 이력이 없다. ^[inferred]

## Open Questions

- 구조체 필드 중 링크 종별, 도로명 ID 등 세부 값 정의는 원본 4장에 있다. 이 페이지에는 요약만 옮겼다.

## Sources

- [[_raw/_archived/INAVI_RouteServer_for_Taiwan_RouteDataLib_Guide_And_Reference_v1_0_1_4.pdf]] — 라이브러리 가이드 원본
- [[_raw/_archived/INAVI_RouteServer_for_Taiwan_RouteDataLib_Guide_And_Reference_v1_0_0_2.pdf]] — 초기 버전(1.0.0.2) 가이드
- [[tomtom-traffic-flow-openlr-inquiries-2024]] — 교통 흐름 OpenLR와 OSM ID 매핑 질의
