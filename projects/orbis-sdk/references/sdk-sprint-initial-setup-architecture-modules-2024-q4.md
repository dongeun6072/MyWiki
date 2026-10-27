---
title: >-
    신 NaviSDK 스프린트 상세: 초기 환경 구성, Architecture 정의, 초기 모듈 구성 (2024-10~11)
category: references
project: orbis-sdk
tags: [navisdk, sprint, kmp, architecture, visibility/internal]
aliases: [초기 환경 구성 - 스크럼, Architecture 정의 - 리뷰, 초기 모듈 구성 - 스크럼, 초기 모듈 구성 - 리뷰, "[10/23] 초기 환경 구성", "[11/11] Architecture 정의", "[11/13] 초기 모듈 구성", "[11/19] 초기 모듈 구성"]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/567869491
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/608174081
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/612958231
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/615973303
summary: >-
    신 NaviSDK 개발 첫 3개 스프린트(2024-10-23~11-19)의 스크럼/리뷰 상세. 저장소 구성, NaviCore 공개 수준, 통신 라이브러리(ktor 결정)를 다룬다.
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

# 신 NaviSDK 스프린트 상세: 초기 환경 구성, Architecture 정의, 초기 모듈 구성 (2024-10~11)

신 NaviSDK(KMP 기반) 개발의 시작 구간으로, 2024-10-23 "초기 환경 구성", 11-11 "Architecture 정의", 11-13/11-19 "초기 모듈 구성" 페이지를 날짜순으로 옮긴 문서다. 전 기간 요약은 [[sdk-sprints-2024-2025-timeline]], 허브는 [[sdk-sprints-2024-2025-hub]]에 있다. 스프린트 연도는 페이지 수정일(2024-11)과 순서로 판단했다 ^[inferred].

담당자 표기: 앱 개발자 1~3은 스크럼 표의 1~3번 행 담당자를 같은 순서로 부른 것이다(1번 행 앱 개발자 1, 2번 행 앱 개발자 2, 3번 행 앱 개발자 3). 4번 행은 [[이동은]]이다. 스크럼 표 열은 "담당자 / 완료 / 진행중·할것 / 문제 / 후속논의"다.

## [10/23] 초기 환경 구성 - 스크럼

- 목표: 프로젝트 초기 환경 구성 세팅

| 담당 | 완료 | 진행중/할것(티켓) | 문제 |
|---|---|---|---|
| 앱 개발자 1 | - | NSDK-239, NSDK-240, NSDK-248 | PM이 Bitbucket 권한 없음 |
| 앱 개발자 2 | - | NSDK-241, NSDK-242 | git Repo 관리 방안(아래) |
| [[이동은]] | - | NSDK-243, NSDK-244 | - |

Git 저장소 관리 방안(앱 개발자 2 제기):
1. SDK Core(신규): Bitbucket
2. AOS/iOS 테스트용: 기존 테스트용 Repo 사용
3. AOS/iOS Sample: GitHub 사용(차후)

## [11/11] Architecture 정의 - 리뷰

- 참석: 앱 개발자 1~3, [[이동은]]
- 스프린트 목표: SDK Architecture 구성 방안 정의
- 완료 항목: NSDK-240, NSDK-242, NSDK-243, NSDK-250, NSDK-251, NSDK-252
- 다음 스프린트 이관: NSDK-255
- 차기 스프린트 플래닝(목표): 내비게이션 초기 단계 Step 별 개발(2Track)
  - AOS/iOS: 초기 엔진(Static Library) IF 작업
  - 공통: 통신 모듈 개발
- 이슈: NaviCore IF 공개 수준 정리 필요. NaviCore가 3rd Party에 공개되는 수준을 정해야 한다(API만 공개할지, NaviCore까지 공개할지).
- 기타 의견: 없음

## [11/13] 초기 모듈 구성 - 스크럼

- 목표: 내비게이션 초기 단계 Step 별 개발 진행

| 담당 | 완료 | 진행중/할것(티켓) | 문제 | 후속논의 |
|---|---|---|---|---|
| 앱 개발자 1 | NSDK-255 | NSDK-263, NSDK-266 | iOS: 엔진(so)을 1개의 framework으로 묶어 Core에 포함하는 방향으로 진행 | NaviCore IF 공개 수준 및 개발적 공개 범위 정리(3rd Party에 공개할 범위: API 수준 vs NaviCore) |
| 앱 개발자 2 | - | NSDK-261 | 통신 라이브러리: Retrofit + ktor 고민 중(라이선스 검토) | - |
| 앱 개발자 3 | - | NSDK-265 | 다음 스프린트부터 개발 참여 가능 | - |
| [[이동은]] | - | NSDK-264 | - | - |

공통 논의 결과:
- NaviCore IF 공개 범위: Android는 구조상 문제 없음(API만 공개하는 방향). iOS도 API만 공개하는 방향으로 진행.
- SDK 로그 분석용 로그: Header에 추가하는 방향(원문에 추가 항목이 생략되어 있음) ^[ambiguous]

## [11/19] 초기 모듈 구성 - 리뷰

- 참석: 앱 개발자 1~3, [[이동은]]
- 스프린트 목표: 내비게이션 초기 단계 Step 별 개발 진행
- 완료 항목: NSDK-255, NSDK-264, NSDK-265
- 다음 스프린트 이관: NSDK-266, NSDK-263, NSDK-261
- 차기 스프린트 플래닝(목표): 로컬 지도 다운로드 후 지도 표출 및 제스처 동작
- 이슈: 통신 라이브러리 Retrofit + ktor("ktor핏") 조합을 라이선스 검토와 함께 고민했고, **ktor만 사용하는 것으로 정리**했다.
- 기타 의견(정보 공유): iOS에서 header에만 함수를 정의하고 구현체가 없으면 링킹 에러가 발생한다.

## 이 구간의 주요 결정

| 항목 | 최초 등장 | 최종 상태 |
|---|---|---|
| Git 저장소 분리(Core=Bitbucket, 테스트=기존 Repo, Sample=GitHub 차후) | 10/23 | 제안 상태로 기록 |
| NaviCore 공개 수준 | 11/11(이슈) | 11/13에 Android/iOS 모두 API만 공개로 정리 |
| iOS 엔진 구성 | 11/13 | so를 1개 framework으로 묶어 Core에 포함 |
| 통신 라이브러리 | 11/13(Retrofit+ktor, 라이선스 검토) | 11/19에 ktor만 사용으로 결정 |
| NSDK-261(앱 개발자 2의 통신 라이브러리 검토 티켓으로 추정) | 11/13 진행 | 11/19 이관, 11/21 완료 표기, 12/02 리뷰에서 완료 |

## Related
- [[sdk-sprint-initial-map-display-2024-q4]] — 다음 구간(초기 지도 표출)
- [[navisdk-confluence-sprint-timeline-2024-2026]] — 기존 요약 타임라인
- [[orbis-navisdk-architecture-and-flutter-plan]] — Architecture와 Flutter 계획
- [[kmp-cmp-adoption]] — KMP 도입 배경
- [[orbis-sdk]]

## Sources
- Confluence "[10/23] 초기 환경 구성 - 스크럼" (pageId 567869491) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[11/11] Architecture 정의 - 리뷰" (pageId 608174081) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[11/13] 초기 모듈 구성 - 스크럼" (pageId 612958231) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[11/19] 초기 모듈 구성 - 리뷰" (pageId 615973303) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
