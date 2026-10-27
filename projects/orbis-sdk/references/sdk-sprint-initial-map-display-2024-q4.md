---
title: >-
    신 NaviSDK 스프린트 상세: 초기 지도 표출 (2024-11-21~12-02)
category: references
project: orbis-sdk
tags: [navisdk, sprint, map-display, kmp, visibility/internal]
aliases: [초기 지도 표출 - 스크럼, 초기 지도 표출 - 리뷰, "[11/21] 초기 지도 표출", "[12/02] 초기 지도 표출"]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/624623617
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/640909315
summary: >-
    "로컬지도 다운후 지도 표출 및 제스쳐 동작" 스프린트(2024-11-21~12-02)의 스크럼 2회분(같은 페이지 내 두 시점)과 리뷰 상세.
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

# 신 NaviSDK 스프린트 상세: 초기 지도 표출 (2024-11-21~12-02)

로컬 지도를 내려받아 표출하고 제스처를 동작시키는 스프린트다. 스크럼 페이지 하나에 두 시점의 표와 소절이 이어져 있어 시점 1/시점 2로 구분했다(원문에는 날짜가 없다) ^[ambiguous]. 앞 구간은 [[sdk-sprint-initial-setup-architecture-modules-2024-q4]], 다음 구간은 [[sdk-sprint-internal-api-design-2024-12]]이다. 허브: [[sdk-sprints-2024-2025-hub]].

## [11/21] 초기 지도 표출 - 스크럼

- 목표: 로컬지도 다운 후 지도 표출 및 제스처 동작

### 시점 1 (표)

| 담당 | 완료 | 진행중/할것 | 문제 |
|---|---|---|---|
| 앱 개발자 1 | - | NSDK-263, NSDK-266 | - |
| 앱 개발자 2 | NSDK-261 | NSDK-273 | 라이브러리 Retrofit+ktor: **ktor로 결정** |
| 앱 개발자 3 | - | NSDK-271 | - |
| [[이동은]] | - | NSDK-272 | - |

시점 1 담당자별 소절:
- 앱 개발자 2, 통신 모듈
  - 폴더 접근: iOS는 파일 쓰기 권한이 필요 없음. AOS는 권한 필요(임시로 진행, 실제 권한 개발은 차후).
- 앱 개발자 3, static Lib 통합
  - MMC 모듈부터 시작. AIR 소스 확인을 위해 Repo 권한 필요. AOS와 iOS 규격이 달라 AIR 사용법 확인 필요.
  - KMP 통합: 티켓 생성 후 진행 예정.
- 앱 개발자 1, static Lib 통합
  - 안내 KMP 연결을 당일까지 완료 예정(SMR 포함해서 마무리).
  - KMP 통합: MMC, DP 지원 예정.
- [[이동은]]
  - Common Repo로 DP 엔진 IF 개발: 다 같이 진행하는 것으로 정리, 1차 목표 수준까지는 이미 완료.
  - KMP 공통 로직: 인증 로직.

### 시점 2 (표)

| 담당 | 완료 | 진행중/할것 |
|---|---|---|
| 앱 개발자 1 | NSDK-263, NSDK-266, NSDK-274 | NSDK-275 |
| 앱 개발자 2 | NSDK-261 | NSDK-273 |
| 앱 개발자 3 | - | NSDK-271 |
| [[이동은]] | - | NSDK-272 |

시점 2 소절:
- 앱 개발자 1: Lib 통합 완료(앱 개발자 3이 진행하는 MMC, DP는 제외). 빌드 스크립트 작성.
- 앱 개발자 2: 통신 모듈 다운로드 완료. 실패 케이스 오류 리턴 정리. unZip(Okio)은 공용 로직으로 사용 가능(iOS 테스트 필요).
- 앱 개발자 3: MMC, DP Lib 통합.
- [[이동은]]: KMP 공통 로직, 인증 로직 개발.
- 전체: 2차 목표 수준 협의 및 백로그 생성.

## [12/02] 초기 지도 표출 - 리뷰

- 참석: 앱 개발자 1~3, [[이동은]]
- 스프린트 목표: 로컬지도 다운 후 지도 표출 및 제스처 동작
- 완료 항목: NSDK-263, NSDK-266, NSDK-274, NSDK-261, NSDK-273, NSDK-271
- 다음 스프린트 이관: NSDK-272
- 차기 스프린트 플래닝(목표): 내부 API 설계(통합검색, 길찾기, DP 경로선 세팅, 지도에 경로선이 표출되는 상황)
  - Core(메인): 엔진 데이터 연동 구조 설계
  - Auth, 권한
  - 기간 2~3주
- 이슈, 기타 의견: 없음

## 항목별 상태 변화

| 티켓/항목 | 첫 등장 | 변화 |
|---|---|---|
| NSDK-263, NSDK-266 | 11/13 진행 | 11/19 이관, 11/21 진행, 시점 2에서 완료, 12/02 완료 |
| NSDK-274 | 시점 2(완료) | 12/02 완료 |
| NSDK-275 | 시점 2(진행) | 12/04 이후 내부 API 설계 스프린트로 이어짐 |
| NSDK-272 | 11/21 진행([[이동은]]) | 12/02 이관, 12/16 완료 |
| 인증 로직 | 11/21 진행 | 12/04 스크럼에서 완료 |

## Related
- [[navisdk-confluence-sprint-timeline-2024-2026]] — 기존 요약 타임라인
- [[orbis-navisdk-architecture-and-flutter-plan]] — Architecture 계획
- [[orbis-route-data-lib]] — 경로 데이터 라이브러리
- [[orbis-sdk]]

## Sources
- Confluence "[11/21] 초기 지도 표출 - 스크럼" (pageId 624623617) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[12/02] 초기 지도 표출 - 리뷰" (pageId 640909315) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
