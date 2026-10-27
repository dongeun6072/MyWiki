---
title: >-
    AIR 푸시 알림 메시지 구조
category: concepts
tags: [inavi-air, push, fcm, visibility/internal]
aliases: [AIR 푸시, FCM 푸시 메시지]
relationships:
  - target: "[[inavi-air-api-overview]]"
    type: derived_from
sources:
  - ~/Develop/Wiki/_raw/articles/project-air/API 명세.md
  - ~/Develop/Wiki/_raw/articles/project-air/Push Curl.md
summary: >-
    AIR 앱이 받는 FCM 푸시 메시지의 data 필드와 6가지 type(A, B, D, E, S, X). 테스트용 curl 예시의 구조만 정리했고 키와 토큰은 옮기지 않았다.
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0.00
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T09:14:00+09:00
updated: 2026-10-26T09:14:00+09:00
snapshots:
  - "[[_raw/_archived/API 명세|API 명세]]"
  - "[[_raw/_archived/Push Curl|Push Curl]]"
---

# AIR 푸시 알림 메시지 구조

AIR 앱의 푸시는 Firebase Cloud Messaging(FCM)으로 전달되고, 앱이 해석하는 값은 `data` 객체 안에 있다. 정의 원문은 [[inavi-air-api-overview]]의 "Push 관련" 절이고, 소속 프로젝트는 [[inavi-air]]이다.

## 공통 필드

| 필드 | 설명 |
|---|---|
| `nt` | 알림(Notification) 제목 |
| `pt` | 팝업 제목 |
| `pc` | 팝업 내용 |
| `iu` | 이미지 URL |
| `type` | 메시지 유형(아래 표) |
| `subtype` | 유형별 세부 값 |
| `url` | 연결할 URL |
| `collapskey` | 같은 키의 알림을 하나로 합치는 collapse 키 |

iOS는 `aps.alert`를 쓴다.

## type 정의

| type | 이름 | 동작 | 추가 필드 |
|---|---|---|---|
| A | 일반 실행 | 앱 실행 | |
| B | 모바일 웹 연동 | 외부 브라우저로 URL 열기 | `url` |
| C | 탐색 | 길 안내 시작 | |
| D | 내부 WebView | `url`이 있으면 그 웹뷰, 빈 문자열이면 이벤트/공지사항 | `url` |
| E | 앱 특정 화면 | 지정한 화면 표시 | `subtype`(예: `CI` = 자정 전에는 캐시 정보, 자정 후에는 적립 스탬프 조회 화면) |
| S | 티머니 온다 목적지 탐색 | 승객 호출 목적지 안내 | `callID`, `startLoc`, `endLoc`, `viaLocs`, `status`(1/2/4), `payType`(A/D), `routeType` |
| X | 티머니 온다 목적지 탐색 취소 | 호출 취소 | `callId`, `status`(1/2), `cancelType`(D 일반, P 지불, C 승객 신고) |

`startLoc`, `endLoc`, `viaLocs`는 `x`, `y`(정규화 좌표), `poiid`, `name`을 가진다. `routeType`은 `recommendation`, `time_priority`, `real_traffic_freeroad` 중 하나다.

## 테스트용 curl 예시의 구성

`Push Curl.md`에는 일반 푸시(type D, E)와 탐색용 푸시(type S, X)를 FCM 레거시 엔드포인트(`fcm.googleapis.com/fcm/send`)로 보내는 curl 예시가 있다. 헤더(`authorization: key=...`, `content-type: application/json;charset=UTF-8`)와 본문(`data`, `to`) 구성을 확인하는 용도다. ^[inferred]

> **주의**: 원본 curl 예시에는 FCM 서버 키와 기기 토큰이 그대로 들어 있다. 이 페이지에는 옮기지 않았다. 원본 파일을 저장소에 올리면 키가 노출되므로 올리기 전에 지우거나 키를 폐기하는 것을 권장한다.

## Open Questions

- 예시가 레거시 FCM API(서버 키 방식)다. 현재 운영도 같은 방식인지는 확인되지 않았다. ^[ambiguous]
- type C(탐색)의 필드는 정의 문서에 따로 나오지 않는다.

## Sources

- [[_raw/_archived/API 명세.md]] — Push Type, 메시지 정의
- [[_raw/_archived/Push Curl.md]] — 테스트 curl 예시(키/토큰 제외)
