---
title: >-
    대구 신호교차로 연동 프로토콜 v0.4
category: references
tags: [inavi-air, traffic-light, api, visibility/internal]
aliases: [대구 신호등 Protocol, 대구 신호교차로, trflight]
relationships:
  - target: "[[inavi-air-api-detail-spec]]"
    type: related_to
sources:
  - ~/Develop/Wiki/_raw/articles/project-air/대구 신호교차로 Protocol_v0.4.docx
  - ~/Develop/Wiki/_raw/articles/project-air/대구신호등목록.xlsx
  - ~/Develop/Wiki/_raw/articles/Outlook_2022.md
summary: >-
    대구 신호등 정보 제공 프로토콜(/trflight, /trftotal)의 요청 방식, 응답 필드, 결과 코드와 신호등 46개 지점 목록의 구성.
provenance:
  extracted: 0.80
  inferred: 0.10
  ambiguous: 0.10
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T09:14:00+09:00
updated: 2026-10-26T15:30:00+09:00
snapshots:
  - "[[_raw/_archived/대구 신호교차로 Protocol_v0.4.docx|대구 신호교차로 Protocol_v0.4.docx]]"
  - "[[_raw/_archived/대구신호등목록.xlsx|대구신호등목록.xlsx]]"
  - "[[_raw/_archived/Outlook_2022|Outlook_2022]]"
  - "[[_raw/_archived/Outlook_2023|Outlook_2023]]"
  - "[[_raw/_archived/(포맷정의서)신호등정보_V.1.1.2.pdf|(포맷정의서)신호등정보_V.1.1.2.pdf]]"
  - "[[_raw/_archived/0620_신호등정보.xlsx|0620_신호등정보.xlsx]]"
  - "[[_raw/_archived/T_LIGHT.TXT|T_LIGHT.TXT]]"
  - "[[_raw/_archived/대구 신호교차로 Protocol_v0.8.docx|대구 신호교차로 Protocol_v0.8.docx]]"
  - "[[_raw/_archived/대구 신호교차로 Protocol_v0.9.docx|대구 신호교차로 Protocol_v0.9.docx]]"
  - "[[_raw/_archived/CTT_list_20250305_2504a.txt|CTT_list_20250305_2504a.txt]]"
---

# 대구 신호교차로 연동 프로토콜 v0.4

선행 개발그룹이 2022년 5~9월에 작성한 신호등 정보 제공 규격이다(v0.1 초안 → v0.4 전체 리스트 API 추가). 앱에는 AIR API의 `/trafficLightList`, `/trafficLightStatus`, `/trafficLightWalker`로 노출된다. ([[inavi-air-api-detail-spec]]) 소속 프로젝트: [[inavi-air]].

## 제공 기능

| 기능 | 방식 | URI |
|---|---|---|
| 신호등 정보 제공 | HTTP POST / JSON | `/trflight` |
| 신호등 전체 리스트 제공 | HTTP POST / JSON | `/trftotal` (요청 body 없음) |

## 요청: Node ID + 방향 코드

요청 값은 `NodeID`(KS ID) 뒤에 방향 코드 두 자리를 붙인 하나의 long 값이다. 예) NodeID `1500005900` + 남(30) = `150000590030`.

| 방향 | 코드 | 방향 | 코드 |
|---|---|---|---|
| 북 | 10 | 북동 | 50 |
| 동 | 20 | 남동 | 60 |
| 남 | 30 | 남서 | 70 |
| 서 | 40 | 북서 | 80 |

## 응답: 신호등 정보

- **운영 정보**: 전이, 감응, 소등, 점멸, 수동
- **이상 정보**: MCU↔SCU 통신 이상, 센터 통신 이상, 모순 이상
- **신호 운영 주기**: 사이클 진행 시간(초)
- **신호등 종류**: 미지정, 직진, 좌회전, 보행자, 자전거, 우회전, 버스, 유턴
- **신호 색상**: 소등, 적색/황색/녹색 점등, 적색/황색/녹색 점멸
- 표출 시간, 잔여 시간(초), 정보가 들어온 시간(Time Stamp)

결과 코드는 `0` 성공, `1` 알 수 없는 NodeID, `2` 유입된 데이터 없음이다. 전체 리스트는 `0` 성공, `1` 데이터 없음이다.

## 전체 리스트 응답 필드

`nodeID`, `nodeType`(1 교차로 중심, 2 안내 신호등), `nodeName`, `compassCode`(방향 코드), `longitude`, `latitude`, `Angle`(진입 각도), `mapID`.

## 신호등 목록 (대구신호등목록.xlsx)

- 46개 지점. 열은 NodeID, Node Name, latitude, longitude, 방향, 코드다.
- 이름은 동인네거리, 교동네거리, 대구역앞교차로, 태평네거리, 달성네거리 같은 도심 교차로와 `국가산단01`~`국가산단65`, `구지공단1·2` 같은 산업단지 지점으로 이루어진다.
- 일부 행은 위경도가 대구 범위를 벗어난다(위도 약 35.64~37.33). 목록에 다른 지역 좌표가 섞여 있는지는 확인되지 않았다. ^[ambiguous]

## 2022년 연동 이력 (업무 메일)

| 시기 | 내용 |
|---|---|
| 2022-06-28 | 선행개발 팀이 **대구 신호교차로 개발 서버**를 구축해 서버플랫폼셀에 전달. 호출 방식 POST, JSON, 경로 `/api/trflight`, 요청 `{ "nodeID": 150000650030 }`(NodeID + 방향 코드). **요청 시각보다 1초 전의 데이터**를 찾아 응답. nodeID는 `대구신호등목록.xlsx` 참조 |
| 2022-09-28 | 6월에 받은 자료(프로토콜 v0.3, 신호등 목록)를 모빌리티Tech그룹이 **에어 신호등 연계 실시간 상태 조회 API**의 규격과 테스트 API로 공유 |
| 2022-09-30 | 프로토콜 수정본 **v0.4**(전체 리스트 API 추가) 전달 |
| 2022-10-13 ~ 20 | 신호등 반영 지점 전달 → 신호등 DB 업데이트와 버전 업데이트 요청 → 선행개발 팀이 신규 DB 적용. **AGENT가 1시간마다 신호등 전체 DB를 받아 현행화**하며 개발 서버는 ver0.2(10-19 20시) |

이 연동은 [[이동은]]이 같은 시기(2022-09~10) 맡은 에어 앱의 신호등 안내 업무와 짝이다. ([[inavi-air-feature-history]]) 서버 주소는 적지 않았다. ([[inavi-2022-mail-overview]])

## 2023년 확장

2023년에는 안내 위치가 **90여 건 더 추가**되고(총 91건), **보행자 신호등 프로토콜이 v0.7 → v0.9**로 바뀌며 대구시 AI 횡단보도 연계 테스트가 이어졌다. 상세 경과는 [[air-daegu-crosswalk-signal-2023]]에 있다. 이 페이지의 `v0.4` 규격(교차로 신호)은 그 뒤 보행자 신호 규격(`/trafficLightWalker`)과 별개 흐름이다. ^[inferred]

## 문서와 AIR API의 차이

- 이 프로토콜 표의 변수명이 뜻과 어긋난다: 응답 표에서 `roadType`은 "Time Stamp", `seeTime`은 "신호등 종류"로 적혀 있다. AIR API 명세에서는 `roadType`이 신호등 종류, `seeTime`이 표출 시간, `timeStmp`가 시간이다. 문서 오타로 보이며 AIR 명세 쪽 정의를 따르는 게 안전하다. ^[ambiguous]
- 전체 리스트의 경위도는 이 문서에서 Double, AIR 명세 예시에서는 Integer(예: `272693`)다. 앱에는 변환된 값이 내려가는 것으로 보인다. ^[inferred]
- AIR API에는 이 프로토콜에 없는 **보행자 신호등** 조회(`/trafficLightWalker`)가 있다. 무단 횡단자 존재 여부, 좌우 보행자/대기자 여부, 보행 신호 상태(R, G, GF=녹색 깜빡임)를 준다.

## 프로토콜 v0.9와 보행자 신호등 API (보강)

v0.4 이후 개정 이력(v0.5~0.9)에서 문서가 커졌다.

| 버전 | 시기 | 변경 |
|---|---|---|
| 0.5 | 2022-10 | 신호등 현시 정보에 운영·이상 정보 추가 |
| 0.6~0.7 | 2023-07 | **보행자 신호등** 운영 정보 추가, 호출 방식 변경 |
| 0.8~0.9 | 2023-07~08 | 보행자 신호등 응답 데이터 변경 |

- 제공 기능 3개: 신호등 정보(`/trflight`), 신호등 전체 리스트(`/trftotal`), **보행자 신호등 정보(`/trflightwalker`)**. 모두 HTTP POST/JSON.
- 신호등 정보 요청은 `NodeID + 방향 코드`를 하나의 long 값으로 합쳐 보낸다. 방향 코드는 북 10, 동 20, 남 30, 서 40, 북동 50, 남동 60, 남서 70, 북서 80.
- 응답: 운영 정보(정상, 전이, 감응, 소등, 점멸, 수동), 이상 정보(정상, SCU 통신 이상, 센터 통신 이상, 모순 이상), 운영 주기, 신호등 종류(직진, 좌회전, 보행자, 자전거, 우회전, 버스, 유턴), 표출·잔여 시간, 색상(소등, 적·황·녹 점등, 적·황·녹 점멸), 가변 시간 여부, 타임스탬프.
- **보행자 신호등 요청**은 NodeID만 쓴다. 응답은 노드 ID, 개수, 방향 코드, 이상 정보, **신호 연장 여부, 무단횡단 여부, 좌·우 신호등의 방향 코드와 보행자·대기자 여부**, 잔여 시간, 타임스탬프. 결과 코드는 0 성공, 1 데이터 없음, 2 서버 응답 없음. 이 응답을 쓰는 안내 시나리오는 [[air-right-turn-pedestrian-alert-test-2023]]이다.
- 전체 리스트 응답은 버전, 노드 ID, 노드 형태(1 교차로 중심, 2 안내 신호등), 명칭, 방향 코드, 경도·위도, 진입 각도, MapID.

## 신호등 위치 데이터 파일 (보강)

- **포맷 정의서(신호등정보 V1.1.2)와 `T_LIGHT.TXT`**: Bessel TWCS(통좌표) 신호등 데이터를 쉼표로 구분한 텍스트. 컬럼은 `NODE_ID(10자), NODE_TYP, NODE_NM, COM_CD(방향), X, Y, ANGLE(진입 각도), MAPID(4자)`. 방향 코드는 2자리로 만들어 확장을 고려했고, 음수 예외 코드(-1~-9)는 신호등 정보가 없지만 방향성 체크가 필요한 경우에 진북 기준 시계 방향으로 순차 부여한다. 샘플 파일은 7행(교차로 중심 2, 안내 신호등 6 중 일부)이며 한글 명칭이 인코딩 깨짐으로 보인다.
- **`0620_신호등정보.xlsx`**: 노드 ID, 경도, 위도, 노드 종류, 명칭, 진행 방향(좌회전, 직진 등)을 풀어 놓은 18행짜리 서울 구로 일대 예시 시트. 명칭 열에 방향 문구가 섞여 있어 정리되지 않은 상태다. 대구 외 지역으로 신호 연동을 넓히는 준비로 보인다. ^[inferred]
- **`CTT_list_20250305_2504a.txt`**: `링크 ID(12자리)|구분값` 형식의 약 29만 행 목록(2025-03-05, 25년 4월 a 버전). 구분값은 1, 2, 3, 5, 6, 7, 9이고 6이 약 70%를 차지한다. MR 포맷의 CTT(교통정보 매칭) 계열 테이블 입력으로 보이나 정확한 용도는 문서에 없다. ([[inavi-mr-format-spec]]) ^[ambiguous]

## Sources

- [[_raw/_archived/대구 신호교차로 Protocol_v0.4.docx]] — 프로토콜 원본
- [[_raw/_archived/대구신호등목록.xlsx]] — 신호등 지점 목록
- [[_raw/_archived/대구 신호교차로 Protocol_v0.8.docx]] — v0.8 개정본
- [[_raw/_archived/대구 신호교차로 Protocol_v0.9.docx]] — v0.9 개정본(보행자 신호등)
- [[_raw/_archived/(포맷정의서)신호등정보_V.1.1.2.pdf]] — 신호등 포맷 정의서
- [[_raw/_archived/T_LIGHT.TXT]] — 신호등 샘플 데이터
- [[_raw/_archived/0620_신호등정보.xlsx]] — 신호등 정보 시트
- [[_raw/_archived/CTT_list_20250305_2504a.txt]] — CTT 목록(내용 미수록)
