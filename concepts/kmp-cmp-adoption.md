---
title: >-
    KMP/CMP 도입 경험
category: concepts
tags: [kmp, cmp, multiplatform, kotlin, visibility/internal]
aliases: [Kotlin Multiplatform 도입, Compose Multiplatform 도입, KMP 전환]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[drawing-run-sdk]]"
    type: related_to
sources:
  - ~/Develop/Wiki/_raw/articles/inavi/2026_상반기_목표_주요업무_정리.md
  - ~/Develop/Wiki/_raw/articles/inavi/2026_상반기_성과점검_이동은.md
summary: >-
    모빌리티개발셀이 SDK와 앱을 KMP/CMP로 옮기며 얻은 경험. 공통 모듈화 방식, SDK 중심이라 부족했던 CMP 앱 경험, 배포 복잡도를 정리했다.
provenance:
  extracted: 0.70
  inferred: 0.30
  ambiguous: 0.00
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T09:20:33+09:00
updated: 2026-10-26T09:20:33+09:00
snapshots:
  - "[[_raw/_archived/2026_상반기_목표_주요업무_정리|2026_상반기_목표_주요업무_정리]]"
  - "[[_raw/_archived/2026_상반기_성과점검_이동은|2026_상반기_성과점검_이동은]]"
---

# KMP/CMP 도입 경험

2026년 연간 목표 "KMP/CMP 기반 멀티플랫폼 프로젝트 전환"(진척도 50%)을 수행하며 쌓인 경험이다. Kotlin Multiplatform(KMP)은 비즈니스 로직 공유, Compose Multiplatform(CMP)은 UI 공유를 뜻한다.

## 적용 사례

| 프로젝트 | 적용 방식 |
|---|---|
| [[drawing-run-sdk]] | 처음부터 KMP로 구성해 Android/iOS 동시 배포. `stop`/`pause`/`reset()`을 공통 모듈로 구현 |
| [[orbis-sdk]] (Navi) | 국내향 소스를 걷어내고 플랫폼 로직을 공통 로직으로 이동. `setLanguage` 공개 API와 에러 처리 구조를 Android/iOS 공통화 |
| 삼성생명 POC | 빠른 iOS 대응을 위해 KMP로 시작 |
| 서울 동행맵 앱 | CMP 단일 코드베이스로 Android·iOS 공용 화면 구현(2026-06~, 진행 중) |
| 데모/샘플 앱 | 드로잉런 데모 앱을 Compose UI로 전환해 Compose 역량 확보 |

## 접근 방식

1. **KMP 관점을 먼저 본다.** 프로젝트를 시작하거나 검토할 때 멀티플랫폼으로 만들 수 있는지부터 따진다. 상반기 동안 이 습관이 자리 잡았다고 평가했다.
2. **플랫폼별 로직을 공통 모듈로 끌어올리는 작업을 반복한다.** 유지보수 효율과 플랫폼 간 상호운용성이 좋아진다.
3. **공통 API 설계가 중요하다.** 예: 세션 종료와 일시정지를 분리하고 전체 초기화 API를 별도로 제공.

## 어려움과 보완 계획

- **SDK 중심 경험의 한계**: UI 구성, 구조 설계, 운영 방식 같은 애플리케이션 관점의 CMP 경험이 부족하다. 개인 학습과 샘플 앱 전환으로 보완하는 중이었고, 이후 서울 동행맵 앱이 첫 CMP 앱 프로젝트가 된 것으로 보인다. ^[inferred]
- **배포 복잡도**: Android 서브모듈, Dokka, iOS XCFramework, SPM을 거치는 다단계 배포. 공통 배포 프로세스로 정비했다.

## Open Questions

- 공통 모듈 비율, 빌드 시간 같은 정량 수치는 원본에 없다.

## 관련

- 셀 채널에서 공유된 KMP 동향과 CMP 지도 라이브러리 배포(2026-07-22): [[references/cell-tech-radar-2023-2026]], [[references/cell-dev-infra-and-build-env]]. 조직 맥락은 [[entities/모빌리티개발셀]].

## Sources

- [[_raw/_archived/2026_상반기_목표_주요업무_정리.md]] — 목표 1 체크인
- [[_raw/_archived/2026_상반기_성과점검_이동은.md]] — 성과 2 자체 평가
