---
title: >-
    셀 기술 동향 2023~2026
category: references
tags: [company, kmp, android, ios, tech-radar, visibility/internal]
aliases: [모빌리티개발셀 기술 공유]
relationships:
  - target: "[[entities/모빌리티개발셀]]"
    type: derived_from
  - target: "[[concepts/kmp-cmp-adoption]]"
    type: related_to
summary: >-
    모빌리티개발셀 채널에서 공유된 KMP·Kotlin·Android 정책 변경(target SDK 35, 16KB 페이지), Firebase Dynamic Links 종료, 개발 도구 소식 등 기술 동향 연표.
provenance:
  extracted: 0.9
  inferred: 0.1
  ambiguous: 0.0
base_confidence: 0.47
lifecycle: draft
lifecycle_changed: 2026-10-27
tier: supporting
created: 2026-10-27
updated: 2026-10-27
sources:
  - "slack:#모빌리티개발셀"
---

# 셀 기술 동향 2023~2026

[[entities/모빌리티개발셀]]이 채널에서 공유한 소식 중 업무에 영향을 주는 것만 골랐다. 셀의 KMP/CMP 경험은 [[concepts/kmp-cmp-adoption]].

## 영향이 컸던 플랫폼 변경

| 날짜 | 내용 | 대응 |
|---|---|---|
| 2024-12-23 | Firebase Dynamic Links가 2025-08에 종료, 기존 링크도 동작 중단 | 운영 서비스의 단축 링크 서비스 사용 현황 조사 |
| 2025-07-02 | 8/31부터 앱 업데이트에 target SDK 35 이상 필수, 11월부터 16KB 페이지 크기 지원 필수 | so 파일 담당 파트 대응, AGP 8.5.1 이상이면 경고 표시 |
| 2025-06~07 | Firebase가 KMP를 공식 지원하지 않는 점이 불편, 지원 청원 투표 독려 | 우회 연동 |
| 2025-04-02 | iOS 18.4부터 Apple 지도 국내 정식 지원 | 지도 서비스 경쟁 요소로 참고 |

## KMP·Kotlin

- 2023-05 KotlinConf 23 영상 공개, 2023-11 KMP Stable 공개.
- 2024-05 Google I/O에서 Android 공식 KMP 지원(Room, Paging, ViewModel 등), Kotlin 2.0 정식 출시(K2 기본).
- 2025-06 네이버 캘린더 KMP+CMP 적용 사례, 2025-09 JetBrains 로드맵(iOS 빌드 속도, Swift Export, Navigation 3·Paging 3 멀티플랫폼, Compose Web/Wasm 베타, KMP 플러그인 Windows·Linux), 2025-10 Android 공식 KMP 가이드 리뉴얼.

## 도구

- JetBrains IDE 2024.1·2024.2 출시, AI Assistant 도입(2023-12), GPT-4o 맥 앱(2024-05), VS Code용 Copilot 무료(2024-12).
- 2025-06 IntelliJ 유료 기능이던 HTTP Client가 Android Studio에도 지원(환경 dev/prod/test, 스크립트 시나리오, curl·Postman 변환).
- QuickType(JSON → 언어별 디코더 생성, 2024-06), Chrome Split View(2025-11), Quick Share의 AirDrop 호환(2025-11).

## 운영 이슈 메모

- Bitbucket 불안정(2024-08, 2025-07), PR 이미지 붙여넣기 크기 조절 불가 → 표 안에 넣는 우회(2025-10).
- Play Console 신규 계정의 테스터 12명 요건, 심사용 테스트 로그인(SNS 계정) 방식 질문(2025-05~06, 결론은 스레드).
- 2026-03 글로벌 iNavi Maps SDK 가이드 사이트 오픈. 2026-06 오르다 2.3.9 등 앱 릴리즈 이력은 [[references/mobility-dev-cell-timeline-2023-2026]] 및 서비스별 문서 참고(걸음수 측정에 삼성헬스 연동, Activity Recognition Transition으로 걸음수 누락 개선).

## 2026년 상세

- 2026년 소식과 사내 CMP 산출물은 [[references/mobility-tech-talk-kmp-android-ios]]에 따로 정리했다.

## Sources

- 슬랙 `#모빌리티개발셀`(2023-05~2026-07).
