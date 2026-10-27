---
title: >-
    아이나비에어 그룹주행 설계서 v0.9
category: references
tags: [inavi-air, group-driving, ux, visibility/internal]
aliases: [그룹주행 설계서, 그룹주행 화면 설계]
relationships:
  - target: "[[group-driving-location-permission]]"
    type: related_to
  - target: "[[inavi-air-api-detail-spec]]"
    type: related_to
sources: [~/Develop/Wiki/_raw/articles/project-air/아이나비에어 그룹주행 설계서.pdf]
summary: >-
    2019년 그룹주행 화면 설계서(v0.9) 요약. 그룹방 생성과 공유, 메시지로 참여, 주행 중 알림, 전체 경로, 타임라인 화면과 관련 서버 API를 정리했다.
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
  - "[[_raw/_archived/아이나비에어 그룹주행 설계서.pdf|아이나비에어 그룹주행 설계서.pdf]]"
---

# 아이나비에어 그룹주행 설계서 v0.9

2019-06-04 작성, Confidential 표기가 있는 화면 설계서(PDF 9쪽)다. 그룹주행은 여러 사람이 서로 위치를 공유하며 같은 목적지로 이동하는 기능이고, 누가 누구의 위치를 볼 수 있는지 정하는 **위치 허용 규칙**이 핵심이다. 규칙만 따로 [[group-driving-location-permission]]에 정리했다. 소속 프로젝트: [[inavi-air]].

## 화면별 정의

| 번호 | 화면 | 핵심 정의 |
|---|---|---|
| 1 | 탐색 > 그룹주행 > 공유 (방 생성자) | 공유 버튼을 누르면 그룹방이 생성된다. **방 생성자 외 최대 9명, 총 10명**. 생성 시점에 생성자는 참여자 전체에게 위치를 공개한다. |
| 2 | 그룹주행 공유 (제3자) | 참여자가 참여 메시지로 제3자에게 공유할 때는 그 참여자가 별도로 위치를 허용하지 않는다. 개인끼리 동의해야 위치가 공개된다. |
| 3, 3-1 | 메시지로 접속 (참여) | 접속 → 전체 경로 → 내 위치 허용 → 시작하기 → 주행. 내 위치 허용 화면에는 이전 키가 없고, 안내 문구를 바꾸고 "동의" 버튼을 "시작하기"로 바꾼다(기능은 동일, 체크박스 선택 후 누르면 위치 공개). |
| 4 | 그룹주행 중 | 누가 참여하면 VMS 영역에서 바로 위치 허용을 받는다. 동작이 없으면 10초 뒤 사라진다. 기존 참여 토스트는 삭제하고, 참여/탈퇴 시 효과음(예: "띵동")을 낸다. 가로 모드에서도 VMS 영역을 쓴다. 차 아이콘에 그룹주행 상태를 표시하고, 방 상태가 바뀌면 느낌표 뱃지를 단다. |
| 5 | 그룹주행 전체 경로 | 참여자 위치, 남은 거리, 위치 제공 미동의 상태를 보여 준다. 상단/하단 전광판 형태의 현황판을 누르면 타임라인으로 이동한다. |
| 5-1 | 그룹주행 타임라인 | 방 history: 참여/탈퇴, 위치 공개, 목적지까지 거리/시간, 도착 여부 |

## 관련 서버 API

| 기능 | URL | 메모 |
|---|---|---|
| 그룹 만들기 | `/makeGroup` | 도착지 좌표(`destiX`, `destiY`)가 필수, 응답에 `groupId`, `shortenURL` |
| 현재 위치 업로드 | `/rris/data/currentLoc` | `myInfo.groupId`, 남은 거리/시간, `allowList`(위치를 허용할 상대의 privateKey 목록, 항상 최신 스냅샷) |
| 그룹 나가기 | `/groupUpdate` | `status`는 현재 `E`(나가기)만 사용 |
| 위치제공사실조회 | `/groupDrivingHis` | 최근 1개월간 내 위치를 조회한 사람(암호화 MDN)과 횟수 |

`allowList`를 서버가 비교해서 위치를 내려주는 방식으로 위치 허용 관계를 구현한 것으로 보인다. ^[inferred] 엔드포인트 전체 목록은 [[inavi-air-api-detail-spec]]에 있다.

## Open Questions

- 설계서는 2019년 v0.9이고 API 문서는 2026년 정리본이라, 최대 인원이나 UX가 현재도 같은지는 확인되지 않았다.
- 응답의 `shortenURL`은 "기능 구현 후 검토 예정"이라고만 적혀 있다.

## Sources

- [[_raw/_archived/아이나비에어 그룹주행 설계서.pdf]] — 설계서 원본
