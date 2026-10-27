---
title: >-
    에어 AOS 작업 이력 허브
category: references
project: inavi-air
tags: [inavi-air, android, bitbucket, commit-history, hub, visibility/internal]
relationships:
  - target: "[[inavi-air]]"
    type: related_to
  - target: "[[inavi-air-feature-history]]"
    type: related_to
sources:
  - repo:bitbucket/mobility-tech/inaviair_aos
summary: >-
    에어 AOS 앱(Bitbucket inaviair_aos) 본인 커밋 2,054건(2022-07~2026-10)의 연도별 이력 허브. 커밋 메시지 기준이며 diff는 검증하지 않았다.
provenance:
  extracted: 0.80
  inferred: 0.15
  ambiguous: 0.05
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-10-27
tier: supporting
created: 2026-10-27T15:00:00+09:00
updated: 2026-10-27T15:00:00+09:00
snapshots:
  - "[[_raw/_archived/Bitbucket_inaviair_aos_커밋목록_dongeun|Bitbucket_inaviair_aos_커밋목록_dongeun]]"
---

# 에어 AOS 작업 이력 허브

본인이 작성한 iNavi AIR Android 앱(Bitbucket `inaviair_aos`) 커밋 2,054건을 기간별로 정리한 페이지의 입구다. 서비스 전반은 [[inavi-air]], 기능 연표는 [[inavi-air-feature-history]]를 본다.

> [!warning] 커밋 메시지 기준, diff 미검증
> 모든 하위 페이지는 커밋 메시지만 근거로 한다. 메시지와 실제 변경이 다를 수 있으므로 답변에 쓸 때는 단정하지 말고 해시를 함께 인용한다. 정확도가 중요한 항목은 `git show <해시>`로 확인한 뒤 `lifecycle`을 올린다.

## 수집 조건

- 저장소: Bitbucket `mobility-tech/inaviair_aos`(로컬 clone `Android/inavi-air/Air`), 모든 브랜치(`--all`), merge 커밋 제외
- 필터: 작성자 본인(`--author`), 총 2,054건, 2022-07-07 ~ 2026-10-06
- 원본 목록: [[_raw/_archived/Bitbucket_inaviair_aos_커밋목록_dongeun]] (해시|날짜|메시지)
- 저장소 전체 커밋은 약 14,000건이며 본인 작성분은 약 15%다.

## 기간별 페이지

| 기간 | 건수 | 페이지 | 주요 주제(메시지 기준) |
|---|---|---|---|
| 2022-07 ~ 12 | 236 | [[air-aos-commit-history-2022]] | 에어캐시 화면·Lottie, 신호등 안내(AIR-633), 음성 광고(AIR-694), 경로설정·전체경로 화면(AIR-567) |
| 2023-01 ~ 06 | 451 | [[air-aos-commit-history-2023-h1]] | OnAir 음성광고, 전체경로 화면, what3words, Kakao 로그인 SDK, 에어캐시 스탬프·룰렛 |
| 2023-07 ~ 12 | 601 | [[air-aos-commit-history-2023-h2]] | 제보·에어연구소, HUD(로드피아) 연결, 보행자 신호등·AI 횡단보도, 에어퀴즈, Android Auto |
| 2024-01 ~ 12 | 399 | [[air-aos-commit-history-2024]] | 에어봇·생성형 AI, SKP·Google 광고, 캐시버튼·포인트홈, 로그인 유도, 안내엔진 |
| 2025-01 ~ 2026-10 | 367 | [[air-aos-commit-history-2025-2026]] | 안내·지도 엔진 갱신, 오르다 스탬프, 시간제 통행규제, 카메라 안내, 수소·친환경 할인 |

## 월별 흐름

- 2023-09 ~ 11이 가장 많다(월 123~158건). 2023년이 연간 1,052건으로 전체의 절반 정도다.
- 2024-04~06은 월 5~16건으로 가장 적다. 2025년부터 월 6~34건대로 줄고, 2026-06에 68건으로 한 번 늘어난다.
- 건수 흐름은 메시지 수 기준이며 작업량이나 난이도와는 다르다. ^[inferred]

## 분류 한계

- 주제 분류는 메시지 키워드와 Jira 키로 한 1차 분류다. 한 커밋은 한 주제에만 센다. ^[inferred]
- "수정", "fix"처럼 대상을 알 수 없는 커밋은 각 페이지의 "모호한 커밋" 섹션에 모았다. 합계 41건 안팎이다. ^[ambiguous]
- 사람 이름, 서버 주소, 키는 메시지에서 옮기지 않았다(미수록).

## Sources

- [[_raw/_archived/Bitbucket_inaviair_aos_커밋목록_dongeun]]
- 저장소: Bitbucket `mobility-tech/inaviair_aos`
