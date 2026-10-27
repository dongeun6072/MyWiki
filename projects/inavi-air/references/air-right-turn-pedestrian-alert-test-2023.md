---
title: >-
    우회전 보행자 정보 연계 기능 테스트 시나리오 (2023-10)
category: references
tags: [inavi-air, crosswalk, pedestrian, test, visibility/internal]
aliases: [우회전 보행자 주의, 보행자 정보 연계 테스트, 보행자 주의 알림]
relationships:
  - target: "[[daegu-traffic-light-protocol]]"
    type: related_to
  - target: "[[air-daegu-crosswalk-signal-2023]]"
    type: related_to
sources:
  - ~/Develop/Wiki/_raw/articles/project-air/우회전 보행자 정보 연계기능 테스트시나리오.hwp
  - ~/Develop/Wiki/_raw/articles/project-air/우회전 보행자 정보 연계기능 테스트시나리오_231004.pdf
summary: >-
    2023-10-05 대구 교차로 2곳에서 센터가 수집한 보행자 정보(대기자, 보행자, 무단횡단)를 에어 모의주행으로 검증한 시나리오. 우회전과 직진에서 "보행자 주의" 알림이 뜨는 조건과 이벤트 우선순위를 정리했다.
provenance:
  extracted: 0.9
  inferred: 0.1
  ambiguous: 0.00
base_confidence: 0.5
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T15:00:00+09:00
updated: 2026-10-26T15:00:00+09:00
snapshots:
  - "[[_raw/_archived/우회전 보행자 정보 연계기능 테스트시나리오.hwp|우회전 보행자 정보 연계기능 테스트시나리오.hwp]]"
  - "[[_raw/_archived/우회전 보행자 정보 연계기능 테스트시나리오_231004.pdf|우회전 보행자 정보 연계기능 테스트시나리오_231004.pdf]]"
---

# 우회전 보행자 정보 연계 기능 테스트 시나리오 (2023-10)

대구 신호교차로 연동([[daegu-traffic-light-protocol]])에 2023년 추가된 **보행자 신호등 API**(`/trflightwalker`)의 응답을 에어가 안내에 쓰는지 검증하는 테스트 계획이다. 같은 내용의 HWP 초안과 2023-10-05자 PDF가 있다.

## 방식

- 센터가 수집하는 보행자 정보를 대상 지점에 **가상 정보로 생성**하고, 내비 **모의주행**이 시나리오대로 동작하는지 확인한다.
- 대상은 초등학교 앞과 주거 단지 앞 교차로 2곳(대구)이다. 각 교차로의 횡단보도는 번호(2·3번, 4·5번)로 구분한다.

## 이벤트 타입

| 타입 | 정의 | 안내 |
|---|---|---|
| 대기자 | 횡단보도 신호에 대기자가 있음 | "보행자 주의" |
| 보행자 | 횡단보도 신호에 보행자가 있음(신호 연장도 보행자 이벤트로 간주) | "보행자 주의" |
| 무단횡단 | 무단횡단 보행자가 있음 | "보행자 주의" |

교차로 안에서 이벤트가 겹치면 **보행자 > 무단횡단 > 대기자** 순으로 우선한다. 이는 API 응답의 `signlExtnYn`, `wtrmsCrosngYn`, 좌·우 보행자·대기자 플래그와 대응한다.

## 시나리오 규칙

- **우회전**: 진행 방향 오른쪽의 두 횡단보도(우회전 전후)의 보행자 유무와 그 사이 대기자 유무를 함께 본다. 보행자와 대기자가 모두 없으면 알림 없음. 보행자 또는 대기자가 하나라도 있거나, 모두 없어도 무단횡단 정보가 있으면 알림 표시. 두 지점 각각 7가지 조합을 시험한다.
- **직진**: 횡단보도를 통과하더라도 좌우 대기자와 신호에 맞춘 보행자는 **쓰지 않고**, 무단횡단 정보만 고려한다(교차로 100m 전부터 활용). 무단횡단 없음이면 알림 없음, 있으면 알림.

## 연결

- 에어 AI 횡단보도 스크럼은 [[air-ai-crosswalk-scrums-2023]], 대구 신호 연동 경과는 [[air-daegu-crosswalk-signal-2023]]을 참고한다.
- 시험 결과는 이 문서에 없다. ^[ambiguous]

## Sources

- [[_raw/_archived/우회전 보행자 정보 연계기능 테스트시나리오.hwp]] — 초안
- [[_raw/_archived/우회전 보행자 정보 연계기능 테스트시나리오_231004.pdf]] — 2023-10-05자 판
