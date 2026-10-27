---
title: >-
    신 NaviSDK 개발 진행 현황 보드와 2025-2026 후속 스크럼 (상품화 #4, Flutter 대응 #2)
category: references
project: orbis-sdk
tags: [navisdk, sprint, roadmap, flutter, visibility/internal]
aliases: [개발 진행 현황, "[11/19] NaviSDK 상품화 #4 - 스크럼", "[5/14] SDK Flutter 대응 #2 - 스크럼"]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/638976150
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1379696667
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1932722177
summary: >-
    2025-02-27 수정된 "개발 진행 현황"의 6단계 구조(기간 포함)와, 2025-11-19 NaviSDK 상품화 #4, 2026-05-14 SDK Flutter 대응 #2 스크럼 상세.
provenance:
  extracted: 0.90
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T13:00:00+09:00
updated: 2026-10-26T13:00:00+09:00
---

# 신 NaviSDK 개발 진행 현황 보드와 2025-2026 후속 스크럼

"개발 진행 현황" 페이지는 2024-11 이후의 스프린트를 6개 단계로 묶은 로드맵이다. 이 문서는 그 구조를 모두 옮기고, 같은 묶음에 포함된 2025-11-19 "NaviSDK 상품화 #4"와 2026-05-14 "SDK Flutter 대응 #2" 스크럼을 이어서 적었다. 스프린트별 상세는 [[sdk-sprints-2024-2025-hub]]에서 찾을 수 있고, 요약은 [[sdk-sprints-2024-2025-timeline]]에 있다.

## 개발 진행 현황 (페이지 수정일 2025-02-27)

### 1. 구조 설계 및 검토
- KMP 개발 환경 구성
- SDK Architecture 설계
- OS별 엔진 인터페이스 구현
- DI 추가
- 네트워크 엔진 추가
- 초기 인증 구현
- 초기 맵 다운로드 구현
- 지도 표출

### 2. 데이터 연동 (~12.26)
- 통합검색
- 길찾기
- 지도 경로 표출
- 엔진 데이터 연동 구조 설계(Core-MainThread 구조): SMR 엔진 구동

### 3. KMP Base 로직 강화 (~1.23)
- 기존 NaviMainThread 역할을 세분화하여 구조화. 개발 검토 후 결과 확인 필요(동시성 문제 여부). MMC, 안내 Data Flow 정리.
- 구조도와 소스(프로젝트) 구조 정리: INaviController 역할 정리

### 4-1. 기능 Feature 연동 (Orbis Map 공통 부분 먼저) (~2.27)
- 주행 및 안내 컴포넌트 개발: TBT 제공
- 리소스 공통 관리 로직 개발: 이미지, Strings, Color
- API 제공: 검색, 길찾기

### 4-2. 기능 Feature 연동
- 실 주행 및 모의 주행 로직: 안내 엔진, mmc, 요금, 거리
- 주행 UI

### 5. Feature별 UI 연동
- 검색 UI
- 경로선택 UI

### 6. 기타
- Flutter Plug-In
- 다국어

각 단계에 대응하는 스프린트: 1단계는 [[sdk-sprint-initial-setup-architecture-modules-2024-q4]]와 [[sdk-sprint-initial-map-display-2024-q4]], 2단계는 [[sdk-sprint-internal-api-design-2024-12]], 3단계는 [[sdk-sprint-kmp-base-logic-2025-01]], 4-1단계는 [[sdk-sprint-driving-feature-api-2025-02]] ^[inferred].

## [11/19] NaviSDK 상품화 #4 - 스크럼 (페이지 수정일 2026-01-21)

원문 날짜가 "11/19"이고 로드맵이 "25년 4분기"를 가리키므로 2025-11-19 스크럼으로 판단했다 ^[inferred].

- 목표: iOS NaviSDK 서비스, MapsSDK 서비스
- 앱 개발자 1: 탐색 Lib 연동, RouteController 구현
- 앱 개발자 2: 구글 SDK API 비교, 회전교차로 사양 적용(탐색), minsdk 21 대응(타임락은 sdk에서 sampleApp으로 이동)
- [[이동은]]: MarkerController 구현
- 상시 대응: 야간 테마 적용 사양(OS 주/야간 체크 로직 확인), 영어/중국어 주간/야간

Roadmap

| 시기 | 항목 |
|---|---|
| 25년 4분기 | iOS NaviSDK 서비스 |
| 26년 1분기 | MapsSDK 서비스 |
| 상시 대응 | 상용 서버 전환 |
| 상시 대응 | 업체 요청 사항 대응 |
| 상시 대응 | 미진한 항목 검토 및 개발: 차로 안내 |
| 상시 대응 | 실차 개선 항목 검토 및 개발: 연결로 진입/진출 안내 필요(특히 고가도로, 램프 구간 안내 강화), 회전 구간 안내 강화 |

## [5/14] SDK Flutter 대응 #2 - 스크럼 (페이지 수정일 2026-05-14)

- 목표: SDK Flutter 대응
- 앱 개발자 1: 1.0.3 준비, 해외 Navi SDK Flutter, 해외 Map SDK Flutter
- [[이동은]]: 1.0.3 준비, 해외 Navi SDK Flutter, 해외 Map SDK Flutter, 샘플앱에 서버 전환 기능 추가
- 앱 개발자 2: 국내 Step2 Dart 위젯(약 70% 완료 후 홀딩), (완료) 해외 NaviSDK Flutter, 해외 Map SDK Flutter 진행

Flutter 일정

| 단계 | 범위 | 기한 |
|---|---|---|
| Step 1 | Orbis Navi/Map SDK + 샘플 및 가이드 | ~5/22 (Risk: 업체 이슈 대응) |
| Step 1 | 국내향 Navi/Map SDK + 샘플 및 가이드 | ~6/5 |
| Step 2 | 국내향 Navi/Map SDK + 샘플 및 가이드 | ~6/30 |
| Step 2 | Orbis Navi/Map SDK + 샘플 및 가이드 | 미정 |

공통:
- 호주향 Style.json: 1벌로 통일(언어, 테마)
- 통계(진행 중): SDK 사용자 수를 Appkey당 사용자 수로 집계. NaviSDK/MapSDK에서 Appkey와 UniqueKey(UUID)를 전달함.
- 상용화 서비스 계획 수립

Todo:
- 로그 on/off API: MMC는 생성 후 전달해 주기로 함. 탐색은 현재 디버그 출력이 없으며, 출력이 생기면 on/off API를 만들어 주기로 함.

## Related
- [[navisdk-confluence-sprint-timeline-2024-2026]] — 기존 요약 타임라인
- [[orbis-navisdk-architecture-and-flutter-plan]] — Flutter 계획 배경
- [[navisdk-api-coverage-and-domestic-sdk-guide]] — API 범위와 국내 SDK 가이드
- [[orbis-sdk]]

## Sources
- Confluence "개발 진행 현황" (pageId 638976150) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[11/19] NaviSDK 상품화 #4 - 스크럼" (pageId 1379696667) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[5/14] SDK Flutter 대응 #2 - 스크럼" (pageId 1932722177) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
