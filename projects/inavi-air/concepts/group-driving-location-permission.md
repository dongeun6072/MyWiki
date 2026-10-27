---
title: >-
    그룹주행 위치 허용 관계
category: concepts
tags: [inavi-air, group-driving, privacy, visibility/internal]
aliases: [내 위치 허용 규칙, 그룹주행 위치 공유 규칙]
relationships:
  - target: "[[inavi-air-group-driving-design]]"
    type: derived_from
sources: [~/Develop/Wiki/_raw/articles/project-air/아이나비에어 그룹주행 설계서.pdf]
summary: >-
    그룹주행에서 누가 누구의 위치를 볼 수 있는지 정하는 규칙. 위치 허용은 방향성이 있고, 참여자가 직접 동의해야 공개된다.
provenance:
  extracted: 0.75
  inferred: 0.25
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

# 그룹주행 위치 허용 관계

그룹주행의 위치 공개는 **방향이 있는 허용 관계**다. "B가 A의 위치를 본다"와 "A가 B의 위치를 본다"는 따로 동의한다. 화면과 API는 [[inavi-air-group-driving-design]]에 있고, 소속 프로젝트는 [[inavi-air]]이다.

## 규칙

1. **방 생성자(A)는 생성 시점에 모든 참여자에게 자신의 위치를 공개한다.** 그래서 참여자는 처음부터 A의 위치를 볼 수 있다.
2. **참여자는 자기 위치를 직접 동의해야 공개된다.** 동의하지 않으면 그 참여자는 A의 위치를 볼 수 있고, A는 그 참여자의 위치를 볼 수 없다.
3. **나중에 들어온 참여자(C)는 기존 참여자 각각에게 동의한다.** A, B가 있는 방에 C가 들어오면 내 위치 허용 화면에 A, B가 나타나고, C가 동의한 상대에게만 C의 위치가 공개된다. 반대로 C가 B의 위치를 보려면 B가 C에게 위치를 허용해야 한다.
4. **참여자가 제3자(D)에게 방을 공유하면 그 참여자의 위치는 자동으로 공개되지 않는다.** 방 생성자가 공유할 때와 다른 점이다. D는 동의 전에는 방 생성자(A)의 위치만 본다.
5. 새 참여자가 생기면 기존 참여자는 알림을 받고, 내 위치 허용 관리 화면에서 새 참여자에게 위치를 허용할지 정한다.

## 예시 (A 생성, B 참여, C 참여)

| 상황 | 볼 수 있는 위치 |
|---|---|
| B가 참여만 하고 동의하지 않음 | B는 A를 본다. A는 B를 못 본다. |
| B가 A에게 동의 | A와 B가 서로 본다. |
| C가 A, B 모두에게 동의 | A, B 모두 C를 본다. C는 A를 본다. C가 B를 보려면 B의 동의가 따로 필요하다. |

## 구현 단서

현재 위치를 올릴 때 `allowList`(위치를 허용할 상대방의 privateKey 목록)를 항상 최신으로 보내고, 서버는 이 목록으로 누구에게 위치를 내려줄지 정한다. ^[inferred] 내 위치가 조회된 기록은 `/groupDrivingHis`로 최근 1개월분을 볼 수 있다(위치제공사실조회).

## Open Questions

- 규칙 2의 "동의하지 않으면 A는 B를 못 본다"가 현재 앱에서도 같은지 확인이 필요하다(설계서는 2019년 v0.9).

## Sources

- [[_raw/_archived/아이나비에어 그룹주행 설계서.pdf]] — 6번 화면 "그룹주행 위치허용 관계 정리"
