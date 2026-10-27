---
title: >-
    SDK 유지보수 스크럼 (2026-04, 2026-07)
category: references
project: orbis-sdk
tags: [sdk, scrum, maintenance, flutter, visibility/internal]
aliases: [SDK 유지보수 스크럼, SDK 유지보수 #1, #2]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1892483073
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1901035535
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/2029879324
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/2047377409
summary: >-
    2026-04 및 07 SDK 유지보수 스크럼. 소스/발행 관리 결정, Flutter 대응 논의, Orbis 신규 탐색엔진 지도 업데이트, 에어 방안 3.
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

# SDK 유지보수 스크럼 (2026-04 ~ 2026-07)

"SDK 유지보수" 이름의 스크럼은 두 시기로 나뉜다. 2026년 4월 22일, 29일의 두 페이지(Flutter Step 2 준비 포함)와 7월 1일(#1), 8일(#2)의 안정화 페이지다. 이전은 [[navi-sdk-improvement-scrums-2026]], 사이에 [[sdk-flutter-scrums-2026]]이 있다. 목차는 [[sdk-sprints-2025-2026-hub]].

## [4/22] SDK 유지보수 (pageId 1892483073, 수정일 4/28)
- 목표: Orbis Navi SDK Truck 서비스 / 국내향 Flutter 대응 / SDK 유지보수
- 앱 개발자 1, 4: 항목 없음(비어 있음)
- 앱 개발자 2: Flutter Step 2
  - 지도
  - 컴포넌트(MapLayer 제거, 컴포넌트 dart)
  - 소스 관리, 발행 관리 검토: 1소스 관리 vs 2소스 관리 (결정 전)
- AIR: **w3w 완전 제거 - 다음 날**
- 공통: 호주향 Style.json 1벌, 통계 진행 중, 상용화 서비스 계획 수립
- Todo: 로그 on/off API

## [4/29] SDK 유지보수 (pageId 1901035535)
- 목표: SDK 유지보수
- 앱 개발자 2: Flutter Step 2
  - 지도, 컴포넌트(MapLayer 제거, 컴포넌트 dart)
  - 소스 관리, 발행 관리 검토: **결정 - 소스는 1벌로 관리, 발행은 별도로 관리**
  - 에뮬레이터: ANR 발생 이슈 개선 (처음 등장)
  - 목표 일정 산정 (처음 등장)
- 국내향 Navi SDK (처음 등장)
  - 가이드 문서 이관 - VitePress
  - 완료: AOS, iOS NaviSDK, SHI는 CF 유지 (SHI = 고객사 이름 약어 ^[inferred])
- **Flutter 대응 필요 (팀 리더와 논의해 정리)** (처음 등장)
  - 티맵/구글과 비교해 Flutter 지원 및 개발 가이드 수준은 유사하게 구성
  - Navi SDK는 이 방식으로 진행하더라도 Map SDK는 메인 Flutter 앱의 위젯 트리에 통합 구성하려면 2단계 방식으로 구현해야 하므로 고민
    - 참고 사례: UMOS(42dot 자회사, 자율주행 DRT 택시/셔틀용 Maps 플랫폼 공급, NDA 체결 완료)
  - WBS 수립: Navi/Map/OS 등
- 공통: 호주향 Style.json 1벌, 통계 진행 중, 상용화 서비스 계획 수립
- Todo: 로그 on/off API

## [7/1] SDK 유지보수 #1 (pageId 2029879324)
- 목표: SDK 유지보수 및 안정화
- **Orbis - 신규 탐색엔진 적용** (6/24에서 이월)
  - INAVI Route Server Data for Taiwan (v26220) ([[taiwan-routeserver-api]] 참고)
  - 지도 업데이트
    - 현재: 서비스 포트에 지도만 변경. Agent 지도 업로드, 탐색엔진 지도 교체, Agent 지도 오픈 순서
    - 차후: SDK가 Agent에 현재 지도 버전을 전달, Agent는 SDK의 지도 버전(SDK 앱 버전)에 따라 탐색 포트를 분기
- AIR: 차기 패치 - 지점을 자동 변경하고 인지할 수 있게 하는 시나리오. 경로 선택 화면에서 목적지 확대 시 지점 핀 사양 추가, 탐색 지점에서 목적지 핀까지 LineTo(DP 엔진 논의)
- 공통: 호주향 Style.json 1벌, 통계 진행 중, 상용화 서비스 계획 수립
- Todo: 로그 on/off API

## [7/8] SDK 유지보수 #2 (pageId 2047377409)
- 목표: SDK 유지보수 및 안정화
- AIR: **방안 3** (처음 등장) - smr 다운로드 상태는 현 사양 유지, smr 미다운로드 상태는 탐색 완료 화면에서 팝업 표출 ([[inavi-smr-format-spec]] 참고. 방안 1, 2의 내용은 이 묶음 페이지에 없음)
- (Orbis 신규 탐색엔진 블록과 6/24~7/1의 AIR 차기 패치 항목은 이 페이지에서 사라짐)
- 공통: 호주향 Style.json 1벌, 통계 진행 중, 상용화 서비스 계획 수립
- Todo: 로그 on/off API

## 항목 상태
| 항목 | 처음 | 상태 |
|---|---|---|
| 소스/발행 관리 방식 | 4/22 | 4/29 결정(소스 1벌, 발행 별도) |
| 가이드 문서 VitePress 이관 | 4/29 | 이후 미언급 |
| w3w 완전 제거(에어) | 3/11 (호출 수 감소) | 4/22 다음 날 제거 예정 |
| Orbis 신규 탐색엔진(v26220) | 6/24 | 7/1 유지, 7/8 제거 |
| AIR 지점 자동 변경 시나리오 | 6/17 | 7/1까지 |
| AIR 방안 3(smr 팝업) | 7/8 | 마지막 상태 |

## Related
- [[sdk-sprints-2025-2026-hub]] — 목차
- [[sdk-flutter-scrums-2026]] — 두 시기 사이의 Flutter 대응
- [[sdk-scrum-common-items-2026]] — 공통/에어 항목
- [[inavi-air]] — 에어 앱
- [[taiwan-routeserver-api]]

## Sources
- Confluence "[4/22] SDK 유지보수 - 스크럼" (pageId 1892483073) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[4/29] SDK 유지보수 - 스크럼" (pageId 1901035535) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[7/1] SDK 유지보수 #1 - 스크럼" (pageId 2029879324) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[7/8] SDK 유지보수 #2 - 스크럼" (pageId 2047377409) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
