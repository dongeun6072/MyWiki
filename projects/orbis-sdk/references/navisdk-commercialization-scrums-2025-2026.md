---
title: >-
    NaviSDK 상품화 스크럼 (2025-10~2026-01)
category: references
project: orbis-sdk
tags: [sdk, scrum, commercialization, ios, visibility/internal]
aliases: [NaviSDK 상품화 스크럼, NaviSDK iOS 상품화]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1302790146
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1323433985
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1357119489
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1434976257
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1463222273
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1529643009
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1567425003
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1611792385
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1645674498
summary: >-
    2025-10~2026-01 NaviSDK 상품화 스크럼. iOS KMP, 회전교차로, 야간 지도 일출/일몰, 비정상 종료 대응, 로드맵과 상태 추적.
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

# NaviSDK 상품화 스크럼 (2025-10 ~ 2026-01)

2025년 10월 29일부터 2026년 1월 14일까지의 "NaviSDK 상품화" 스프린트 스크럼 기록이다. iOS NaviSDK 서비스와 Maps SDK 서비스를 상품화하는 단계로, 이전 단계는 [[demo-exhibition-app-scrums-2025]], 다음 단계는 [[map-sdk-commercialization-scrums-2026]]이다. 목차는 [[sdk-sprints-2025-2026-hub]].

이 묶음에 포함된 원본은 #1, #2, #3, #5, #6, #8, #10, #11이다. #4, #7, #9 페이지는 이 묶음에 없다. 모든 페이지의 수정일은 2026-01-21(일괄 수정)로 표시된다. 이 단계부터 스크럼에 티켓 표가 없고 담당 영역별 목록이다.

또한 "Archived ( NaviSDK iOS 상품화 )"(pageId 1645674498)는 내용이 비어 있어 옮길 내용이 없다.

## 공통 머리말
- 목표 (#1~#8): iOS NaviSDK 서비스 / MapsSDK 서비스
- 목표 (#10, #11): iOS Navi SDK 서비스 / AOS·iOS Map SDK 서비스

## 로드맵 블록 (#1~#11 거의 동일, 아래는 처음 등장 #1의 내용)
- 25년 4분기: 1. iOS NaviSDK 서비스
- 26년 1분기: 1. MapsSDK 서비스
- 상시 대응
  1. 상용서버 전환
  2. 업체 요청사항 대응
  3. 미진한 항목 검토 및 개발: (1) 차로 안내
  4. 실차 개선 항목 검토 및 개발: (1) 연결로 진입/진출 안내 필요(특히 고가도로, 램프 구간 안내 강화), (2) 회전구간 안내 강화
- #10, #11에서도 같은 로드맵이 유지되며, [[map-sdk-commercialization-scrums-2026]]의 1/21부터 26년 1분기 항목이 Map SDK 서비스(~3월 중), Map SDK 가이드 작업, web Map SDK 연동 작업으로 다시 쓰인다.

## [10/29] #1 (pageId 1302790146)
- 앱 개발자 1: 유턴 사양 적용(안내, DP)
- 앱 개발자 2: 구글 SDK(비교), 검색 시나리오 개선
- 앱 개발자 4: setGeoJson 로직 개선
- 상시 대응: 지도 야간테마(디자인 담당 책임), 소스 난독화 aar, 터널 진행 중 자차 UI
- 로드맵 블록 포함

## [11/5] #2 (pageId 1323433985)
- 앱 개발자 1: (완료) 유턴 사양 적용(안내, DP) / iOS KMP 환경 구성 (처음 등장)
- 앱 개발자 2: 구글 SDK API 비교 / 검색 시나리오 개선 / 실차 이슈 대응(처음 등장) / 소스 난독화 aar 상태 확인
- 앱 개발자 4: (완료) setGeoJson 로직 개선 - 재탐색 시 maplibre source-layer 동기화 / 탐색 연동 - 경유지 링크 진행 설정 / 불필요한 국내향 코드 제거 (처음 등장)
- 상시 대응: 지도 야간테마(디자인 담당 책임)

## [11/12] #3 (pageId 1357119489)
- 앱 개발자 1: (완료) iOS KMP 환경 구성 / iOS 주행화면 (처음 등장)
- 앱 개발자 2
  - 구글 SDK API 비교, 실차 이슈 대응
  - (완료) 검색 시나리오 개선 - 검색 API를 제공
  - (완료) 소스 난독화 aar 상태 확인
  - 회전교차로 사양 적용(탐색) (처음 등장)
  - 경유지 통과 시 MMC 이슈 (처음 등장)
- 앱 개발자 4: (완료) 불필요한 국내향 코드 제거 / iOS 제스처 & UI 컨트롤러 (처음 등장)
- 상시 대응: 지도 야간테마(디자인 담당 책임)

## [11/26] #5 (pageId 1434976257)
- 앱 개발자 1: (완료) 탐색 Lib 연동 / RouteController 구현 (처음 등장)
- 앱 개발자 2
  - 구글 SDK API 비교, 회전교차로 사양 적용(탐색)
  - minsdk 21 대응 (처음 등장): 메인은 MapLibre의 OpenGL 3.0 사용, 6.0 또는 7.0으로 올리는 안, MMC 5.0 대응 진행 상황
  - (완료) 타임락: sdk에서 sampleApp으로 이동
- 앱 개발자 4
  - (완료) MarkerController 구현
  - UserLocationAnnotation 자차 컨트롤: AOS는 MapLibre API 사용, iOS는 기본(트래킹 모드)이며 ZoomIn/ZoomOut 동작 시 이상 동작 (이슈, 처음 등장)
- 상시 대응: 야간테마 적용 사양 - OS 주야간 체크 로직 확인, 영어/중국어 주간/야간 (사양 구체화)

## [12/3] #6 (pageId 1463222273)
- 앱 개발자 1: 검색 화면 구성 (처음 등장)
- 앱 개발자 2
  - 회전교차로 사양 적용(탐색): (완료) 비즈니스 로직, 음성 추가
  - 야간 지도 적용: OS가 일출/일몰 시간을 주는 API가 없음 -> **결정: 로컬 로직으로 좌표 기반 일출/일몰 계산 적용**
- 앱 개발자 4: (완료) MarkerController 구현 / (완료) UserLocationAnnotation 자차 컨트롤(AOS는 MapLibre API, iOS는 ZoomIn/Out 시 이상 동작 이슈를 같은 문구로 유지)

## [12/17] #8 (pageId 1529643009)
- 앱 개발자 1: 경로 선택 화면 / CES 시연용 세팅 (처음 등장)
- 앱 개발자 4
  - 효과음 기능 추가
  - Genesis Search API 대체 검토 (12/16까지 마무리 필요): Key 값을 서버에서 수신하여 처리하는 구조 (처음 등장)
  - **이슈**: 경로가 존재할 때 주야간 변경 타이밍에 비정상 종료 (처음 등장)
- ~1월 말: iOS 출시에 맞춰 AOS도 버전과 가이드 업데이트 필요 - 버전 1.0.0, 버전 이력(Release Note 항목 추가) (처음 등장)
- 국내 실차: 다음 날(18일) 실차 예정

## [1/7] #10 (pageId 1567425003)
- 앱 개발자 1: 개발자 가이드 작성 / 샘플 소스
- 앱 개발자 4: 라이브러리 버전 업데이트 / 샘플 소스
- 앱 개발자 2: 개발자 가이드 작성
- ~1월 중: iOS 출시에 맞춰 AOS 버전/가이드 업데이트(버전 1.0.0, Release Note, 라이선스 공지 확인 - 내용만 확인) / (완료) AOS AppTester 배포
- "언젠가.." 목록 (처음 등장)
  - 인증 실패 시 모든 API 사용하지 못하도록 예외 처리
  - 경로 존재 시 주야간 변경 타이밍에 비정상 종료: (완료) 1차 style.json 교체 - 1-1 style 교체 시 소스/레이어가 삭제되며 잘못된 참조로 Crash 발생, style 교체 시 메모리 부족 / 1-2차 flag로 layer 변경(style.json 1개) 예정
- 이슈 확인: iOS background 상태에서 위치 갱신이 안 됨(MMC 또는 메인)

## [1/14] #11 (pageId 1611792385)
- 앱 개발자 1: (완료) 개발자 가이드 작성 / 샘플 소스 / Maps 검토 - 대략적인 일정과 항목
- 앱 개발자 4: (완료) 라이브러리 버전 업데이트 / 샘플 소스 / Maps 검토
- 앱 개발자 2: 개발자 가이드 작성
- ~1월 중: iOS 출시에 맞춘 AOS 버전/가이드 업데이트(1.0.0, Release Note, 라이선스 공지) / (완료) AOS AppTester 배포
- 언젠가: 인증 실패 시 API 차단 예외 처리, 주야간 변경 비정상 종료(1차 완료/1-2차 예정)
- 이슈: (완료) iOS background 상태 위치 갱신 안 됨
- **로그 on/off API** (처음 등장): MMC는 생성 후 전달하기로 함, 탐색은 현재 디버그 출력이 없어 출력이 생기면 on/off API를 만들어 주기로 함
- 다음 주 스크럼부터 본사 회의 장소에서 진행하기로 함(장소명 미수록)

## 항목 상태 추적

| 항목 | 처음 | 상태 변화 |
|---|---|---|
| 유턴 사양(안내, DP) | 10/29 | 11/5 완료 |
| setGeoJson 로직 개선 | 10/29 | 11/5 완료 |
| 검색 시나리오 개선 | 10/29 | 11/12 완료(검색 API 제공) |
| 소스 난독화 aar | 9/17 (DEMO) | 10/29 상시 대응, 11/12 상태 확인 완료 |
| 불필요한 국내향 코드 제거 | 11/5 | 11/12 완료 |
| iOS KMP 환경 | 11/5 | 11/12 완료 |
| 회전교차로 사양(탐색) | 11/12 | 12/3 비즈니스 로직 완료, 음성 추가 진행 |
| MarkerController | 11/26 | 11/26 완료 |
| 자차 컨트롤 iOS 이상 동작 | 11/26 | 12/3 완료 표시이나 iOS 이상 동작 문구 유지 ^[ambiguous] |
| 구글 SDK API 비교 | 10/29 | 11/26까지 진행, 이후 미언급 |
| 지도 야간테마 | 9/17 | 12/3에 로컬 일출/일몰 계산 결정 |
| 주야간 변경 시 비정상 종료 | 12/17 | 1/7 1차 완료, 1-2차 대기 |
| AOS 1.0.0 및 가이드 | 12/17 | 1/14 AppTester 배포 완료, 나머지 진행 |
| 로그 on/off API | 1/14 | 이후 모든 스크럼에서 Todo로 유지 |

## Related
- [[sdk-sprints-2025-2026-hub]] — 목차
- [[sdk-scrum-common-items-2026]] — 공통 항목(로드맵, Style.json, 통계 등) 추적
- [[demo-exhibition-app-scrums-2025]] — 이전 단계
- [[navisdk-confluence-sprint-timeline-2024-2026]] — 요약본
- [[orbis-sdk]]

## Sources
- Confluence "[10/29] NaviSDK 상품화 #1 - 스크럼" (pageId 1302790146) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[11/5] NaviSDK 상품화 #2 - 스크럼" (pageId 1323433985) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[11/12] NaviSDK 상품화 #3 - 스크럼" (pageId 1357119489) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[11/26] NaviSDK 상품화 #5 - 스크럼" (pageId 1434976257) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[12/3] NaviSDK 상품화 #6 - 스크럼" (pageId 1463222273) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[12/17] NaviSDK 상품화 #8 - 스크럼" (pageId 1529643009) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[1/7] NaviSDK 상품화 #10 - 스크럼" (pageId 1567425003) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[1/14] NaviSDK 상품화 #11 - 스크럼" (pageId 1611792385) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "Archived ( NaviSDK iOS 상품화 )" (pageId 1645674498) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
