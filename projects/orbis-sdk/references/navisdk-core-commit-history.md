---
title: >-
    NaviSDK_Core 작업 이력 허브
category: references
project: orbis-sdk
tags: [orbis-sdk, navisdk, android, kmp, bitbucket, commit-history, hub, visibility/internal]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[navisdk-confluence-sprint-timeline-2024-2026]]"
    type: related_to
sources:
  - repo:bitbucket/mobility-tech/navisdk_core
summary: >-
    navisdk_core(글로벌 내비게이션 SDK) 본인 커밋 972건(2024-10~2026-09)의 구간별 이력 허브. 커밋 메시지 기준이며 diff는 검증하지 않았다.
provenance:
  extracted: 0.80
  inferred: 0.15
  ambiguous: 0.05
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-10-28
tier: supporting
created: 2026-10-28T10:00:00+09:00
updated: 2026-10-28T10:00:00+09:00
snapshots:
  - "[[_raw/_archived/Bitbucket_navisdk_core_커밋목록_dongeun|Bitbucket_navisdk_core_커밋목록_dongeun]]"
---

# NaviSDK_Core 작업 이력 허브

본인이 작성한 `navisdk_core` 저장소(글로벌 내비게이션 SDK, 로컬 `Android/inavi-navigation-sdk/global-inavi-navigation-sdk-android`) 커밋 972건을 구간별로 정리한 페이지의 입구다. 프로젝트 개요는 [[orbis-sdk]], 같은 기간 스프린트 연표는 [[navisdk-confluence-sprint-timeline-2024-2026]], 상용화 논의는 [[navisdk-commercialization-scrums-2025-2026]]을 본다. 지도 SDK 쪽 이력은 [[global-map-sdk-android-commit-history-2026]]이다.

> [!warning] 커밋 메시지 기준, diff 미검증
> 하위 페이지는 모두 커밋 메시지만 근거로 한다. 답변에 쓸 때는 단정하지 말고 해시를 함께 인용한다. 저장소 이름 `NaviSDK_Core`는 Bitbucket 슬러그 `navisdk_core`로 해석했다.

## 수집 조건

- 저장소: Bitbucket `mobility-tech/navisdk_core`, 모든 브랜치(`--all`), merge·stash 제외, 작성자 본인(이름 표기가 2종이라 `--author=dongeun`으로 모았다)
- 총 972건, 2024-10-23 ~ 2026-09-08. 저장소 전체는 약 2,080건이며 본인 작성분은 약 47%다.
- 원본 목록: [[_raw/_archived/Bitbucket_navisdk_core_커밋목록_dongeun]]. 서버 포트 값 1건과 숨은 기능 진입 방법 1건은 보안 규칙에 따라 가렸다.

## 구간별 페이지

| 구간 | 건수 | 페이지 | 주요 주제(메시지 기준) |
|---|---|---|---|
| 2024-10 ~ 2025-04 | 315 | [[navisdk-core-commit-history-2024-10-to-2025-04]] | Artifactory 배포·appkey, 네이티브 엔진 인터페이스(NSDK-264), 초기 인증(NSDK-272), MMC·GPS·Gravity 공통화, 모듈 분리, 경로선택 GUI |
| 2025-05 ~ 2025-09 | 343 | [[navisdk-core-commit-history-2025-05-to-09]] | 지도 렌더링·카메라(MapLibre 기반), Orbis 지도 스타일·다운로드, TBT·지도 버튼 UI, TTS, 다중경로·경유지, 에러 처리 |
| 2025-10 ~ 2026-09 | 314 | [[navisdk-core-commit-history-2025-10-to-2026-09]] | 국내향 엔진·Flavor 제거, 지도 UI·마커, SDK 초기화·ServiceGate, 네트워크 구조 리팩토링, 트럭 대응, 버전·릴리즈 |

세 구간 합계는 315 + 343 + 314 = 972건으로 원본과 일치한다.

## 월별 흐름

- 2025-09가 130건으로 가장 많다. 2025-04 79건, 2025-08 67건, 2025-11 66건이 뒤를 잇는다.
- 2026-02(4건), 2026-04~05(각 9건), 2026-07(9건), 2026-09(1건)는 적다. 2026-06은 47건이다.
- 건수는 메시지 수 기준이며 작업량이나 난이도와는 다르다. ^[inferred]

## 분류 한계

- 주제 분류는 에이전트가 메시지 키워드와 NSDK 이슈 키로 한 1차 분류다. 한 커밋은 한 주제에만 센다. ^[inferred]
- 모호한 커밋은 6건(2024-10~2025-04), 5건(2025-05~09), 5건(2025-10~2026-09)으로 합계 16건이다. ^[ambiguous]
- 같은 메시지가 중복된 커밋(예: 같은 날 같은 이름의 커밋 여러 건)이 있어 건수가 작업 단위와 다르다. ^[inferred]

## Sources

- [[_raw/_archived/Bitbucket_navisdk_core_커밋목록_dongeun]]
- 저장소: Bitbucket `mobility-tech/navisdk_core`
