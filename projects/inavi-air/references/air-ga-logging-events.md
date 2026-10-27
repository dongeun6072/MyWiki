---
title: >-
    GA Logging (에어 GA 이벤트와 가입 완료 페이지 정의)
category: references
project: inavi-air
tags: [air, ga, logging, analytics, visibility/internal]
aliases: ["GA Logging", 에어 GA 이벤트]
relationships:
  - target: "[[inavi-air]]"
    type: related_to
  - target: "[[air-growth-research-hub]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/653983768
summary: >-
    2024-12-19 수정된 에어 GA 로깅 정의. 앱 최초 실행, SNS 가입, 주행 완료, 캐시 적립 종류별 이벤트 시점과 가입 완료 페이지 이름(AOS/iOS).
provenance:
  extracted: 0.9
  inferred: 0.04
  ambiguous: 0.06
base_confidence: 0.6
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T13:00:00+09:00
updated: 2026-10-26T13:00:00+09:00
---

# GA Logging

로그인 유도 실험([[air-login-induction-experiment-2024-q4]])의 지표를 GA로 측정하기 위해 정의한 이벤트/페이지 로깅 목록이다. 이벤트명과 파라미터는 원문에서 대부분 비어 있거나 `_?`로 미정 상태다. 지표 정의 맥락은 [[air-server-data-analysis-2023-11-2024-11]]의 Private Key·SNS Key 설명, 캐시 종류는 [[air-cash-reward-design-2023-2024]]를 본다.

## 이벤트
| 구분 | 시점 | 이벤트명 | 파라미터 | 비고 |
|---|---|---|---|---|
| 앱 최초 실행 | Private Key 최초 생성 | (미정) | | 초기 약관 동의 시 |
| SNS 회원가입 완료 | SNS Key 최초 생성 | (미정) | | |
| 주행 완료 | 안전주행을 포함한 모든 주행 완료 버튼 클릭 시 | (미정) | | 안전주행은 주행 완료를 알 방법이 없음. 경로 주행만 목적지 도착으로 주행 완료 체크 가능 |
| 캐시 적립 완료 | 캐시가 적립되는 시점 | cash | `_?` | |
| 신규 캐시 적립 완료 | 첫 가입 후 주행 완료 후 500캐시 적립 시점 | cash | `_?` | |
| 룰렛 캐시 적립 완료 | 룰렛 캐시 적립 시 | cash | `_?` | |
| 제보 완료 캐시 적립 | 제보 완료 시 | cash | `_?` | |
| 리워드 캐시 적립 | 리워드 캐시 적립 시 | cash | `_?` | |
| 쿠폰 구매 완료 | 쿠폰 구매 완료 시점 | (미정) | | |

## 페이지
| 페이지명 | Logging | 구분 |
|---|---|---|
| 회원가입 완료 | `ActySettingTutorial` | AOS |
| 회원가입 완료 | `UserInfoTutorialViewController` | iOS |

## Related
- [[air-login-induction-experiment-2024-q4]] — 이 페이지명을 가입 완료 지표로 사용
- [[air-cash-reward-design-2023-2024]] — 캐시 적립 종류
- [[inavi-air]] — 프로젝트 개요
- [[air-growth-research-hub]] — 이 묶음 목차

## Sources
- Confluence "GA Logging" (pageId 653983768) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
