---
title: >-
    드로잉런 SDK 1차 개발 완료와 배포 이력 (1.0.0 ~ 1.0.2, 2026-05 ~ 07)
category: references
project: drawing-run-sdk
tags: [drawing-run-sdk, release-notes, aar, xcframework, visibility/internal]
aliases: [1차 개발 완료, 드로잉런 SDK 버전 이력, 산출물]
relationships:
  - target: "[[drawing-run-sdk]]"
    type: related_to
  - target: "[[drawing-run-sdk-launch-scope-and-data-items-2026]]"
    type: derived_from
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/2Ozy8QblnTwf/pages/2002649151
  - url:https://inavisystems.atlassian.net/wiki/spaces/2Ozy8QblnTwf/pages/2003632155
summary: >-
    드로잉런 SDK의 배포 이력. 1.0.0(2026-05-20)에서 러닝 데이터 가공과 경로 이미지 변환, 1.0.1(06-25)의 Pause와 경과시간 리스너, iOS 1.0.2(07-03)의 백그라운드 위치 콜백 수정.
provenance:
  extracted: 0.95
  inferred: 0.04
  ambiguous: 0.01
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T15:20:00+09:00
updated: 2026-10-26T15:20:00+09:00
---

# 드로잉런 SDK 1차 개발 완료와 배포 이력

"산출물" 페이지(본문 없음) 아래의 "1차 개발 완료" 표다. 개인 월간 이력은 [[drawing-run-sdk]]에 있고 여기서는 Confluence 표 그대로 정리한다.

| 배포일 | 버전 | SDK 형식 | 개발 완료 항목 |
|---|---|---|---|
| 2026-05-20 | AOS `1.0.0`, iOS `1.0.0` | AOS `aar`, iOS `xcframework` | **러닝 데이터 가공**(날짜·시간, 거리, 시간, 칼로리, 속도, 페이스, 랩, 걸음 수, 케이던스, 고도 전 항목)과 **주행 코스 경로 이미지 변환**. SDK 가이드와 3rd party 라이선스 문서를 함께 제공 |
| 2026-06-25 | AOS `1.0.1`, iOS `1.0.1` | 동일 | **Pause 기능 구현**: 기존에 `stop`으로 안내됐던 부분은 정정 필요. **경과시간 리스너** 추가: `durationMillis`를 1초 단위로 계속 전달 |
| 2026-07-03 | iOS `1.0.2` (AOS는 변경 없음) | iOS `xcframework` | **백그라운드 스레드에서 SDK를 호출하면 위치 콜백이 오지 않는 문제**를 수정. SDK 가이드 문서 변경 없음 |

- 데이터 항목 구성은 [[drawing-run-sdk-launch-scope-and-data-items-2026]], 고객사 전달 시 SDK 가이드·라이선스 파일명 규칙은 [[drawing-run-sdk-scrum-2026-04-to-05]]에 있다.
- 표에는 **라이선스 키 값**이 적혀 있으나 보안 사유로 옮기지 않았다. 가이드 문서 링크도 옮기지 않았다.
- 1.0.1에서 `stop`과 `pause`를 분리한 것은 [[drawing-run-sdk]]의 2026-06 이력과 일치한다.
- 이후 2차(안내데이터, 음성 안내)는 [[drawing-run-phase2-voice-guidance-and-meetings-2026]]에서 협의 중이며 배포 기록은 아직 없다.

## Sources

- [Confluence: 1차 개발 완료](https://inavisystems.atlassian.net/wiki/spaces/2Ozy8QblnTwf/pages/2002649151), [산출물](https://inavisystems.atlassian.net/wiki/spaces/2Ozy8QblnTwf/pages/2003632155) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음. 라이선스 키는 보안 사유로 미수록
