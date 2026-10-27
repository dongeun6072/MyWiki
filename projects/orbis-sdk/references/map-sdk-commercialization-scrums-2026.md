---
title: >-
    Map SDK 상품화 스크럼 (2026-01~03)
category: references
project: orbis-sdk
tags: [sdk, scrum, map-sdk, maplibre, visibility/internal]
aliases: [Map SDK 상품화 스크럼]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1642921987
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1670676481
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1693188097
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1715208193
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1733558273
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1755217925
summary: >-
    2026-01~03 Map SDK 상품화 #1~#6. 프로젝트 구성, 인증, Style.json 통일, 통계, 접두어, 좌표변환, 에어 패치 항목.
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

# Map SDK 상품화 스크럼 #1~#6 (2026-01 ~ 2026-03)

2026년 1월 21일부터 3월 4일까지의 "Map SDK 상품화" 스크럼 기록이다. AOS/iOS Map SDK를 MapLibre 기반으로 새로 구성하고 NaviSDK 유지보수를 병행했다. 이전 단계는 [[navisdk-commercialization-scrums-2025-2026]], 다음 단계는 [[navi-sdk-truck-scrums-2026]]이며 목차는 [[sdk-sprints-2025-2026-hub]]이다. 공통 항목(접두어, 통계, Style.json 등)의 변화는 [[sdk-scrum-common-items-2026]]에 따로 정리했다.

공통 목표: AOS/iOS Map SDK 서비스, NaviSDK 유지보수. 담당 구분은 "앱 개발자 1/4"(두 사람이 함께 Map SDK 담당), 공통, 언젠가.., 로그 on/off API, 로드맵이다. 티켓 표는 없다.

## [1/21] #1 (pageId 1642921987)
- 앱 개발자 1/4
  - (완료) Maps 검토 - 대략적인 일정과 항목
  - Map SDK 프로젝트 구성, 인증 구현, MapLibre 기반 지도 구현
- 공통
  - 준상용서버 구축 - 앱: Agent Domain 변경 여부 확인
  - 인증 (처음 등장)
    - 국내 Navi SDK와 Map SDK 동일
    - 해외 Navi SDK / Map SDK: 지도 스타일 하드코딩
      - Step 1: NaviSDK와 동일하게 CDN 하드코딩 접근
      - Step 2: 해외향 인증 신규 API 추가
  - 접두어 (처음 등장): navisdk = `inv`, mapsdk = `igm` (강조 표시), 명칭 inavi-global navigation sdk / inavi-global map sdk
- 언젠가..: 인증 실패 시 모든 API 사용 불가 예외 처리 / 주야간 변경 비정상 종료(1차 style.json 교체 완료, 1-1 잘못된 참조 Crash와 메모리 부족, 1-2차 flag로 layer 변경 예정)
- 로그 on/off API: MMC는 생성 후 전달, 탐색은 디버그 출력이 생기면 만들어 줌
- 로드맵 (26년 1분기): 1. Map SDK 서비스(~3월 중), 2. Map SDK 가이드 작업(이미지 작업, 마크다운 작업 등), 3. web Map SDK 연동 작업 / 상시 대응(상용서버 전환, 업체 요청사항 대응, 미진한 항목 검토 - 차로 안내, 실차 개선 항목 - 연결로 진입/진출 안내(고가도로, 램프 구간 강화)와 회전구간 안내 강화)

## [1/28] #2 (pageId 1670676481)
- 앱 개발자 1/4: (완료) Map SDK 프로젝트 구성, (완료) 인증 구현 / MapLibre 기반 지도 구현 - 지도 추가하기 기능 / 지도 컨트롤
- 공통
  - 준상용서버 구축(Agent Domain 변경 여부 확인), **NaviSDK 1.0.1 준비** (처음 등장)
  - 인증: **Style.json 4종류 (en-light, en-dark, cn-light, cn-dark)** (처음 등장; 1/21의 "지도 스타일 하드코딩" 구체화)
- 기타: 인증서버에 Navi와 Map 구분 필요 (처음 등장)
- **차주 AIR 패치 (처음 등장)**
  - PlanetAD SDK 업데이트: AOS 최신 1.14.6, iOS 최신 1.14.0 (링크 생략)
  - AOS, iOS 단일 링크 모의주행 MMC 버전 적용 필요
  - 아파트 POI 명칭 충돌 처리하지 않도록 DP 기능 개발: `setAptPoiCollisionIgnored` 파라미터를 false로 세팅
- 언젠가/로그 on/off API/접두어/로드맵: 1/21과 동일 (접두어가 "[ 접두어 ]" 별도 블록으로 분리됨)

## [2/4] #3 (pageId 1693188097)
- 앱 개발자 1/4: (완료) MapLibre 기반 지도 구현(지도 추가하기), (완료) 지도 컨트롤 / 지도 카메라 이동 / 마커
- 공통
  - (완료) 준상용서버 구축 / NaviSDK 1.0.1 준비
  - **Style.json: 1벌로 통일 (언어, 테마)** (4종류에서 1벌로 변경)
  - **통계 (처음 등장)**: SDK 사용자 수 - Appkey당 사용자 수. NaviSDK / MapSDK는 Appkey와 UniqueKey를 전달하며 UniqueKey는 UUID
- 언젠가/로그 on/off/접두어/로드맵: 동일

## [2/11] #4 (pageId 1715208193)
- 앱 개발자 1/4
  - (완료) 지도 카메라 이동, (완료) 마커, (완료) 지도 도형(폴리곤, 멀티라인 등) (처음 등장)
  - 지도 사용자 위치 구성 - 자차: 자차 이미지 변경, 자차 스케일, 바운더리 color setting / color clear (처음 등장)
  - 마커 클러스터링 (처음 등장)
- 공통: Style.json 1벌 통일(언어, 테마), 통계(Appkey당 사용자 수, UniqueKey=UUID) / **지도 버전 분기 - 탐색엔진 분기** (처음 등장)
- 언젠가: 인증 실패 시 API 차단 예외 처리, 로그 on/off API(MMC 전달 예정, 탐색은 출력 생기면) (주야간 비정상 종료 항목은 이 페이지부터 사라짐)
- **[TSD-A01] 블록 (처음 등장)**: 이슈 - Map 카드 메뉴의 장소가 언어 변경에 따라 변경되지 않음. step1 로그 확인, step2 MW 수정 또는 펌웨어 요청 ([[tsd-a01]], [[tsd-a01-issue-log-2024]] 참고)
- 접두어, 로드맵 동일

## [2/25] #5 (pageId 1733558273)
- 앱 개발자 1/4
  - (완료) 지도 사용자 위치 구성 - 자차(이미지, 스케일, 바운더리 color), (완료) 마커 클러스터링
  - 좌표변환 API: wgs84에서 katec / tm / Utm-K / Grs80 (처음 등장)
  - 컴포넌트 이벤트 콜백 (처음 등장)
  - 가이드 문서 작성 (처음 등장), 샘플 소스/데모앱(샘플앱) (처음 등장)
- 공통: Style.json 1벌, 통계, 지도 버전 분기(탐색엔진 분기)
- 언젠가, TSD-A01 이슈(2/11과 동일), 접두어, 로드맵

## [3/4] #6 (pageId 1755217925)
- 앱 개발자 1/4: (완료) 좌표변환 API, (완료) 컴포넌트 이벤트 콜백 / 가이드 문서 작성 / 샘플 소스, 데모앱(샘플앱)
- 공통: Style.json 1벌, 통계, 지도 버전 분기(탐색엔진 분기)
- 언젠가, TSD-A01 이슈, 접두어, 로드맵: 동일 (이후 [[navi-sdk-truck-scrums-2026]]의 3/11에서 가이드와 샘플이 완료 표시됨)

## 항목 상태 추적

| 항목 | 처음 | 상태 변화 |
|---|---|---|
| Map SDK 프로젝트 구성 / 인증 구현 | 1/21 | 1/28 완료 |
| MapLibre 기반 지도 구현(지도 추가하기) | 1/21 | 2/4 완료 |
| 지도 컨트롤 | 1/28 | 2/4 완료 |
| 카메라 이동 / 마커 | 2/4 | 2/11 완료 |
| 지도 도형 | 2/11 | 2/11 완료 |
| 자차 구성, 마커 클러스터링 | 2/11 | 2/25 완료 |
| 좌표변환 API, 컴포넌트 이벤트 콜백 | 2/25 | 3/4 완료 |
| 가이드 문서, 샘플/데모앱 | 2/25 | 3/11 완료 (Truck 스크럼) |
| 준상용서버 구축 | 1/21 | 2/4 완료 |
| Style.json | 1/21(하드코딩) / 1/28(4종류) | 2/4 1벌 통일 |
| 통계 | 2/4 | 이후 계속 진행 |
| 지도 버전 분기 | 2/11 | 3/11 Truck에서 구현 항목으로 연결 |

## Related
- [[sdk-sprints-2025-2026-hub]] — 목차
- [[sdk-scrum-common-items-2026]] — 공통/에어 패치 항목
- [[navisdk-confluence-sprint-timeline-2024-2026]] — 요약본
- [[orbis-sdk]]
- [[tsd-a01]] — TSD-A01 이슈 맥락

## Sources
- Confluence "[1/21] Map SDK 상품화 #1 - 스크럼" (pageId 1642921987) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[1/28] Map SDK 상품화 #2 - 스크럼" (pageId 1670676481) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[2/4] Map SDK 상품화 #3 - 스크럼" (pageId 1693188097) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[2/11] Map SDK 상품화 #4 - 스크럼" (pageId 1715208193) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[2/25] Map SDK 상품화 #5 - 스크럼" (pageId 1733558273) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[3/4] Map SDK 상품화 #6 - 스크럼" (pageId 1755217925) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
