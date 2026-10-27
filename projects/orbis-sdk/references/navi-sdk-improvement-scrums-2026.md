---
title: >-
    Navi SDK 개선 스크럼 (2026-03~04)
category: references
project: orbis-sdk
tags: [sdk, scrum, flutter, refactoring, visibility/internal]
aliases: [Navi SDK 개선 스크럼]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1813250049
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1836384257
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1851850753
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1868497020
summary: >-
    2026-03~04 Navi SDK 개선 #1~#4. 삼성생명 POC, DP/네트워크/MMC/FileManager 코드 개선, Flutter Step 1 시작과 Plugin 방안 결정.
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

# Navi SDK 개선 스크럼 #1~#4 (2026-03 ~ 2026-04)

2026년 3월 25일부터 4월 15일까지의 "Navi SDK 개선" 스크럼이다. Orbis Navi SDK Truck 서비스, 국내향 Flutter 대응, SDK 유지보수를 한 스프린트에 묶었고, 삼성생명 POC(런 SDK) 작업과 코드 개선이 함께 나온다. 이전은 [[navi-sdk-truck-scrums-2026]], 다음은 [[sdk-maintenance-scrums-2026]]과 [[sdk-flutter-scrums-2026]]이다. 목차는 [[sdk-sprints-2025-2026-hub]].

공통 목표(#1~#4): Orbis Navi SDK Truck 서비스 / 국내향 Flutter 대응 / SDK 유지보수. 접두어/로드맵/TSD-A01/AIR 블록은 이 스프린트부터 스크럼 본문에서 빠진다.

## [3/25] #1 (pageId 1813250049)
- 앱 개발자 1: 삼성생명 POC
- 앱 개발자 4: 삼성생명 POC
- 앱 개발자 2: Flutter 대응 (처음 등장)
- 공통: 호주향 Style.json 1벌(언어, 테마) / 통계 **진행 중**(SDK 사용자 수 - Appkey당 사용자 수, Appkey/UniqueKey(UUID) 전달)
- Todo(이전 "언젠가.."에서 이름 변경): 인증 실패 시 모든 API 사용 불가 예외 처리 / 로그 on/off API(MMC 전달 예정, 탐색은 출력 생기면)

## [4/1] #2 (pageId 1836384257)
- 앱 개발자 1: 삼성생명 POC / DP 코드 개선 (처음 등장)
- 앱 개발자 4: 삼성생명 POC / 네트워크, MMC 코드 개선 (처음 등장)
- 앱 개발자 2: Flutter 대응
  - Step 1: AOS(1), iOS(-) - NaviSDK 전체 Flutter Plugin 1~2주 (괄호 숫자는 원문 그대로, 의미는 담당 단계 표기로 추정 ^[inferred])
  - Step 2: Dart Widget화 - AOS(2), iOS(-)
- 공통: 호주향 Style.json 1벌, 통계 진행 중
- Todo
  - 인증 실패 시 모든 API 사용 불가 예외 처리: **(완료) API 예외 처리**, "인증 실패 시 SDK 종료 -> 지도 로딩보다 인증을 먼저" 방향 (처음 등장)
  - 로그 on/off API

## [4/8] #3 (pageId 1851850753)
- 앱 개발자 1: (완료) DP 코드 개선 / **클로드 md 환경 구성** (처음 등장)
- 앱 개발자 4: (완료) 네트워크, MMC 코드 개선 / FileManager 코드 개선 (처음 등장)
- 앱 개발자 2: Flutter(Step 1) - API 테스트와 Flutter Sample App / Flutter Plugin 배포와 Plugin 테스트 / iOS 지도 표출
- NaviSDK Flutter (별도 블록, 처음 등장)
  - Step 1: AOS(1), iOS(3), NaviSDK 전체 Flutter Plugin 1~2주
  - Step 2: Dart Widget화 - AOS(2), iOS(3)
  - (4/1의 iOS "-"가 3으로 채워짐)
- 삼성생명 런 (앱 개발자 1/4): 클로드 md 환경 구성. 원문에서 "드로잉"에 취소선이 쳐져 있어 "삼성생명 런"으로 이름이 정정된 것으로 보인다 ^[inferred] ([[drawing-run-sdk]] 참고)
- 공통: 호주향 Style.json 1벌, 통계 진행 중
- Todo: 로그 on/off API만 남음 (인증 실패 항목은 사라짐)

## [4/15] #4 (pageId 1868497020)
- 앱 개발자 1: (완료) 클로드 md 환경 구성
- 앱 개발자 4: (완료) FileManager 코드 개선
- 앱 개발자 2
  - Flutter - Step 1: (완료) API 테스트와 Flutter Sample App
  - Flutter Plugin 배포와 Plugin 테스트
    - **이슈**: 초기 Init 시점에 Main Thread를 사용해 Blocking 발생
    - 방안 1(취소선): SDK 수정 + Plugin 발행
    - **결정: 방안 2 - SDK 수정 없음, Plugin 내부에 aar 포함**
  - iOS 지도 표출
  - Flutter - Step 2 (제목만 등장)
- NaviSDK Flutter: Step 1 AOS(1)/iOS(3), 1~2주 / Step 2 Dart Widget화 AOS(2)/iOS(3)
- 공통: 호주향 Style.json 1벌, 통계 진행 중, **상용화 서비스 계획 수립** (처음 등장)
- Todo: 로그 on/off API

## 항목 상태 추적
| 항목 | 처음 | 상태 |
|---|---|---|
| 삼성생명 POC | 3/25 | 4/8 이후 "삼성생명 런"의 클로드 md 환경 구성으로 이어짐 |
| DP 코드 개선 | 4/1 | 4/8 완료 |
| 네트워크/MMC 코드 개선 | 4/1 | 4/8 완료 |
| FileManager 코드 개선 | 4/8 | 4/15 완료 |
| 클로드 md 환경 구성 | 4/8 | 4/15 완료 |
| 인증 실패 시 API 예외 처리 | 3/25 | 4/1 API 예외 처리 완료, 4/8부터 Todo에서 제거 |
| Flutter Step 1 | 3/25 | 4/15 API 테스트와 샘플앱 완료, 배포 방식 결정 |
| Flutter Plugin Init 시 Main Thread Blocking | 4/15 | 방안 2 채택 |
| 통계 | 2/4 | 3/25에 "진행 중" 표시 |
| 상용화 서비스 계획 수립 | 4/15 | 이후 모든 스크럼 공통 항목 |

## Related
- [[sdk-sprints-2025-2026-hub]] — 목차
- [[sdk-scrum-common-items-2026]] — 공통 항목 추적
- [[sdk-flutter-scrums-2026]] — 이어지는 Flutter 대응
- [[drawing-run-sdk]] — 런 SDK
- [[orbis-navisdk-architecture-and-flutter-plan]]
- [[orbis-sdk]]

## Sources
- Confluence "[3/25] Navi SDK 개선 #1 - 스크럼" (pageId 1813250049) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[4/1] Navi SDK 개선 #2 - 스크럼" (pageId 1836384257) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[4/8] Navi SDK 개선 #3 - 스크럼" (pageId 1851850753) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[4/15] Navi SDK 개선 #4 - 스크럼" (pageId 1868497020) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
