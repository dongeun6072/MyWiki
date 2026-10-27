---
title: >-
    한화금융 PLUS RUN 외부 관찰 기반 기술 검토 (2026-05, Confluence)
category: references
project: drawing-run-sdk
tags: [drawing-run-sdk, competitor, mapbox, voice-guidance, visibility/internal]
aliases: [PLUS RUN 분석, 한화금융 PLUS RUN, 여의도 고구마런, Mapbox 사용 추정]
relationships:
  - target: "[[drawing-run-sdk]]"
    type: related_to
  - target: "[[drawing-run-phase2-voice-guidance-and-meetings-2026]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/2Ozy8QblnTwf/pages/1916534800
summary: >-
    한화금융 PLUS RUN 러닝 앱을 외부에서 관찰해 Mapbox 사용 범위, 위치 측정, 음성안내 구현 방식을 추정하고 삼성생명 드로잉런 SDK와 비교한 검토 문서.
provenance:
  extracted: 0.65
  inferred: 0.32
  ambiguous: 0.03
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T15:05:00+09:00
updated: 2026-10-26T15:05:00+09:00
---

# 한화금융 PLUS RUN 외부 관찰 기반 기술 검토 (2026-05-06)

한화/삼성생명 같은 금융사에 비슷한 러닝 제안을 할 때 참고하려고, **공개 앱을 외부에서 관찰한 결과**만으로 지도와 음성안내 기술을 추정한 문서다. 앱 내부를 분석한 것이 아니므로 "확정 불가" 항목이 많다.

## 서비스 개요

| 항목 | 내용 |
|---|---|
| 서비스 | PLUS RUN, 브랜드 러닝 캠페인·이벤트형 서비스 |
| 핵심 코스 | 여의도 고구마런(단일 코스) |
| 핵심 기능 | 같은 코스 기록 비교(전문 러너와 일반 러너), 인증, 이벤트 참여, 자유 러닝 |
| 기술 중심 | 경로 탐색보다 코스 표시, 기록 측정, 인증 |
| 지도 | Mapbox |
| 음성안내 | 서비스 소개에 제공한다고 명시 |

앱 구성: 홈(챌린지 참여, 페이스 기록과 타 도전자 비교), 러닝(위치 상관없는 기록, 기록 **이미지**·**영상** 다운로드), 콘텐츠(러닝 가이드 영상), 기록(주·월·연 기록), 마이. 요구 권한은 신체 활동, 알림, 위치.

## 확인 가능 여부

| 항목 | 판단 | 근거 |
|---|---|---|
| Mapbox 지도, Maps SDK, 지도 UI 모듈(Gestures, Annotations, Location Component) | 확인 | 지도 좌하단 로고, 오픈소스 목록 |
| 음성안내, GPS 러닝 기록 | 확인 | 서비스 소개 |
| Google Location 사용 | 가능성 높음 | `play-services-location` 항목 |
| Mapbox Directions API, Voice Instructions, Map Matching API, Navigation SDK | **확정 불가** | API 호출 여부와 음성 출처를 볼 수 없음 |
| TTS 엔진(Mapbox/OS/자체) | 확정 불가 | |
| 자체 안내 데이터 | 가능성 있음 | 단일 코스 구조와 부합 |

오픈소스 목록에 Mapbox Maps SDK 계열(Base, Common, Android Core, Annotations, Gestures, Location Component, Camera, Compass, Attribution, Logo, Style Extension, Viewport, Telemetry)이 있다. **Navigation Common/Runtime 항목은 Mapbox Navigation SDK라고 단정할 수 없고** Jetpack Navigation일 가능성이 있다.

## 위치 측정과 기록 기능 추정

| 기능 | 추정 기술 |
|---|---|
| 현재 위치 | Google Location + Mapbox Location Component |
| 거리, 경로 | GPS 좌표 누적, 지도 위 라인 표시 |
| 시간, 평균 페이스 | 앱 타이머, 거리/시간 |
| 자동 일시정지 | 위치 변화량 또는 속도 기반 |
| 기록 이미지·영상 | 경로 데이터 + 지도 렌더링/애니메이션 |

기록 기능은 Directions API 없이 **GPS 좌표 누적만으로** 구현할 수 있다.

## 음성안내 구현 시나리오

| 시나리오 | 설명 | 판단 |
|---|---|---|
| A. Mapbox API 기반 | Directions API의 안내 문장/거리 + TTS | 가능하나 사용 여부 미확인 |
| B. 사전 코스 안내 기반 | 단일 코스에 안내 지점과 문구를 미리 등록하고 도달 시 TTS | 단일 코스 특성상 **가능성 높음** |
| C. 혼합형 | 지도 Mapbox, 위치 Google Location, 안내는 자체 데이터와 일부 API | 가능성 높음 |

## 삼성생명 드로잉런 SDK와 비교

| 구분 | PLUS RUN | 삼성 드로잉런 SDK |
|---|---|---|
| 성격 | 단일 코스 이벤트·기록 비교 | 러닝 SDK |
| 지도 | Mapbox Maps SDK | 아이나비 SDK 기반 지도·위치 솔루션 (실제로 지도는 고객사가 그림) |
| 핵심 기능 | 코스 표시, 기록, 이벤트, 음성안내, 경로 이미지·영상 | 주행 데이터 수집, 기록 가공, 경로 이미지 변환 |
| 음성안내 | 제공은 확인, 방식 미확인 | 2차 범위 |
| 경로 탐색 | 미확인 | 2차 범위, **자체 경로탐색 엔진으로 안내 데이터 생성**, 1차는 기록 SDK 중심 |
| 데이터 | 거리, 시간, 평균 페이스 | 거리, 시간, 페이스, 랩, 케이던스, 고도 등 |
| 연동 | 앱 내부 구현 | 앱/어드민과 SDK 역할 분리 |
| 확장 | 이벤트형 캠페인 | **B2B SDK로 재사용·확장** |

2차 음성안내 협의 항목으로 이어진다 → [[drawing-run-phase2-voice-guidance-and-meetings-2026]], [[drawing-run-course-guidance-data-flow-2026]].

## Sources

- [Confluence: 한화금융 PLUS RUN 외부 관찰 기반 기술 검토](https://inavisystems.atlassian.net/wiki/spaces/2Ozy8QblnTwf/pages/1916534800) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
