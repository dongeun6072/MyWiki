---
title: >-
    TSD A-01 유럽향 VR-Navi 연동규격서 (v0.6 ~ v0.93)
category: references
project: tsd-a01
tags: [tsd-a01, vr, android-intent, interface-spec, visibility/internal]
aliases: [VR Navi 연동규격서, ReqShowMap, RequestNaviCommand]
relationships:
  - target: "[[tsd-a01]]"
    type: related_to
  - target: "[[tsd-a01-issue-log-2024]]"
    type: related_to
sources:
  - "[[_raw/_archived/TSD_A01_유럽향_VR_Navi_연동규격서_v0.6.xlsx]]"
  - "[[_raw/_archived/TSD_A01_유럽향_VR_Navi_연동규격서_v0.93.xlsx]]"
summary: >-
    음성인식(VR) 앱과 TomTom 내비 연동 서비스 사이의 Android Intent 기반 명령 규격과 버전별 변경 이력.
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0.0
base_confidence: 0.55
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T14:00:00+09:00
updated: 2026-10-26T14:00:00+09:00
snapshots:
  - "[[_raw/_archived/TSD_A01_유럽향_VR_Navi_연동규격서_v0.93.xlsx|TSD_A01_유럽향_VR_Navi_연동규격서_v0.93.xlsx]]"
  - "[[_raw/_archived/TSD_A01_유럽향_VR_Navi_연동규격서_v0.6.xlsx|TSD_A01_유럽향_VR_Navi_연동규격서_v0.6.xlsx]]"
---

# TSD A-01 유럽향 VR-Navi 연동규격서

CCOS에서 쓰던 VR-Navi 연동 규격을 **Android용으로 전환**(2023-06 v0.1)해 A01 기능을 반영하고 국내향 규격과 비슷한 형태로 맞춘 문서다. 셀바스AI(VR)와 내비 연동 서비스 측이 이 규격으로 맞춘다([[tsd-a01]]).

## 통신 방식

- VR -> Navi: Intent action `REQUEST_NAVI`, extra `Command`에 `RequestNaviCommand` 값을 담고 필요 시 `Value1~3`을 쓴다.
- Navi -> VR: Intent action `RESPONSE_VR`, extra `Command`에 `ResponseNaviCommand` 값을 담는다. 탐색 상태와 목적지 설정 상태는 **값이 바뀔 때마다** VR로 전달한다.

## 주요 명령

| 구분 | 명령 |
|---|---|
| 화면 | 지도 보기(`ReqShowMap`), 전체 경로 보기(`ReqRouteOverview`) |
| 경로 | 경로 취소(`ReqRouteCancel`), 재탐색(`ReqReRoute`, v0.3에서 TomTom 내비 미지원으로 삭제), 목적지 설정(`ReqRouteSelect`, N번째 리스트 / home·office 구분) |
| 조회 | 최근 목적지, 목적지 정보(TTS 재생용), 목적지 설정 여부(`ReqDestinationState`), 우리집/사무실 조회·등록·변경, 즐겨찾기 조회 |
| 경유지 | 등록 경유지 수 조회(`ReqWaypointCount`), 경유지 추가(`ReqAddWaypoint`, 추가 가능하면 주소 전달 후 VR 종료와 경로 재탐색, 불가하면 TTS 후 경로 편집 화면) |
| 응답 | 탐색 중 여부(0 완료/1 탐색 중), 목적지 여부(0/1), 최근 목적지·즐겨찾기·우리집 정보(JSON), 부팅 상태 |

POI 검색(예: "Find Starbucks")은 VR이 넘긴 POI/주소명으로 Navi가 검색해 리스트를 돌려주고 사용자가 N번째를 고르는 흐름이다. 최근 목적지·POI·즐겨찾기가 없으면 빈 값으로 전달한다.

## 변경 이력

| 시기 | 버전 | 변경 |
|---|---|---|
| 2023-06~08 | 0.1~0.32 | 최초 작성, A01 반영, 재탐색 삭제, 빈 값 규칙, 즐겨찾기 nIndex |
| 2023-08 | 0.4 | 주간회의에서 **즐겨찾기 등록 사양 삭제**(`ReqAddFavorites`, 등록 상태 응답 삭제) |
| 2023-08~12 | 0.41~0.44 | `ReqRouteSelect`의 home/work 케이스·index 상세, 목적지 설정 여부 조회, 경유지 index, 우리집 응답에 POI 이름 |
| 2024-01 | 0.6 | `ReqNavibootState`(내비 부팅 상태) 추가 |
| 2024-03 | 0.7~0.81 | `ResDestinationInfo` 보강 |
| 2024-04 | 0.91~0.93 | `ReqAddWaypoint` 수정(2024-05 경유지 추가 규격 확정 메일과 연결) |

v0.6과 v0.93은 같은 구조이며 v0.93이 최종본이다.

## Sources

- [[_raw/_archived/TSD_A01_유럽향_VR_Navi_연동규격서_v0.6.xlsx]]
- [[_raw/_archived/TSD_A01_유럽향_VR_Navi_연동규격서_v0.93.xlsx]]
