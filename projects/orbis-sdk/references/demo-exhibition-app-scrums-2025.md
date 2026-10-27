---
title: >-
    DEMO/전시회 앱 기능 고도화 스크럼 (2025-09~10)
category: references
project: orbis-sdk
tags: [sdk, scrum, demo, exhibition, visibility/internal]
aliases: [DEMO/전시회 앱 기능 고도화 스크럼]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1123745793
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1162641410
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1191346177
summary: >-
    2025년 9~10월 DEMO/전시회 앱 기능 고도화 스크럼. 터널 안내, ETA, 교통정보 갱신, 멀티 경로, 전시회 버전 항목과 상태 추적.
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

# DEMO/전시회 앱 기능 고도화 스크럼 #1~#4 (2025-09 ~ 2025-10)

2025년 9월 17일부터 10월 1일까지의 "DEMO/전시회 앱 기능 고도화" 스프린트 스크럼 기록이다. [[dp-mmc-engine-maplibre-scrums-2025]]의 이월 항목(TomTom 연동, 다중경로, 다국가 앱)을 이어받아 전시회용 시연 버전과 UMap 기능을 다듬는다. 다음 단계는 [[navisdk-commercialization-scrums-2025-2026]], 전체 목차는 [[sdk-sprints-2025-2026-hub]].

## 공통 목표 (#1~#4 동일)
- DEMO/전시회 버전
- UMap 기능 고도화
- 화면별 GUI 구성
- 표 열: 담당자 / 완료 / 진행중·할것 / 비고(비어 있음). 행은 앱 개발자 1~4(4=[[이동은]]).
- #4 페이지(10/1)에는 티켓 표가 없고 영역별 목록만 있다.

## [9/17] #1, #2 스크럼 (pageId 1123745793, 수정일 9/18)

| 담당 | 완료 | 진행중/할것 |
|---|---|---|
| 앱 개발자 1 | NSDK-519 | NSDK-535, NSDK-539 |
| 앱 개발자 2 | - | NSDK-489, NSDK-473, NSDK-533 |
| 앱 개발자 3 | - | NSDK-522 |
| 앱 개발자 4 | NSDK-531, NSDK-534, NSDK-536 | NSDK-537 |

**영역별 진행**
- 앱 개발자 1: 터널 안내 추가 - DEMO 앱 (안내 음성 번역본 추가, 19일까지)
- 앱 개발자 2: MMC 검토 / 가이드 문서 작성 gitbook(개발용 계정에서 운영 계정으로 전환, 계정명 미수록) / ETA 표출 방식 개선 - DEMO 앱
- 앱 개발자 4: 효과음 추가 시 볼륨 버튼은 효과음만 제공하는 기능 / 멀티 경로 기능 추가 / TomTom API Backend 서브모듈 통합 구현 - 인증 API 구현
- Agent: (완료) TomTom API 연동(Search, Safety Camera, Geocoding/Rev.Geocoding), 인증 Token/KeyCode
- 추가: TomTom Geocoding/Rev.Geocoding API의 NaviSDK API화 / 1개 앱 다국가 지원(국가별 앱 출시, 대만향/싱가폴향 빌드 구성)

**전시회 버전 항목 (처음 등장)**
- 경로선 교통정보 표출
- 멀티 경로 UI
- 경유지 UI
- 지도 야간테마
- 지도 초기위치 (0,0) 이슈 개선
- 소스 난독화 - aar 난독화
- (구분선 이하, 확인 중 항목) TBT 이슈(직진인데 좌/우측 안내) - 탐색엔진 확인 중 / 터널 진행 중 자차 UI / 차로정보

## [9/24] #3 스크럼 (pageId 1162641410, 수정일 9/26)

| 담당 | 완료 | 진행중/할것 |
|---|---|---|
| 앱 개발자 1 | NSDK-539, NSDK-535, NSDK-543 | NSDK-541 |
| 앱 개발자 2 | NSDK-533 | NSDK-489, NSDK-473 |
| 앱 개발자 4 | NSDK-542, NSDK-498 | NSDK-537, NSDK-522, NSDK-540 |

(앱 개발자 3 행은 이 페이지에서 사라짐)

**영역별 진행**
- 앱 개발자 1
  - (완료) 터널 안내 추가 - DEMO 앱 (번역본 추가 ~19일)
  - 경로선 교통정보 표출
    - 교통정보 소스: 탐색엔진 링크열 속도정보
    - 교통정보 갱신 방법 논의(탐색 담당과): 교통정보만 갱신하는 API가 없음 -> **결정: 특정 주기(메인 사양 수립)로 재탐색 진행**
  - getDataLink Crash 이슈 확인
- 앱 개발자 2
  - MMC 검토, gitbook 가이드 문서(번역 문구 정리 ~9/30, kdocs를 ChatGPT로 번역)
  - (완료) ETA 표출 방식 개선 - DEMO 앱: 언어 설정에 따라 변경, 24시간제는 중국, 12시간제는 그 외. 참고로 구글은 단말 설정(12/24시간제)을 따름
- 앱 개발자 4
  - (완료) 효과음 추가 시 볼륨 버튼 효과음 전용 기능
  - 멀티 경로 기능 추가 - MMC: 멀티경로 탐색 규격 적용, 멀티경로 포맷만 유지
  - TomTom API Backend 서브모듈 통합 구현 - 인증 API 구현(테스트 중), 멀티 경로 API 구현
  - TomTom Geocoding/Rev.Geocoding API의 NaviSDK API화 - 리턴 객체 변환
- Agent: (완료) TomTom API 연동, (완료) 인증 Token/KeyCode
- 추가: 1개 앱 다국가 지원(대만향/싱가폴향 빌드)

**전시회 버전 항목 변화**
- 지도 야간테마: 디자인 담당 책임에게 위임 (담당 지정)
- 지도 초기위치 (0,0) 이슈 개선 상세: MapLibre 설정 Location의 디폴트 좌표는 불가, MapLibre 카메라 설정의 디폴트 좌표는 "??"(미확인)
- 나머지(경로선 교통정보, 멀티 경로 UI, 경유지 UI, 소스 난독화, TBT 이슈, 터널 중 자차 UI, 차로정보)는 9/17과 동일

## [10/1] #4 스크럼 (pageId 1191346177)
- 앱 개발자 1
  - 교통정보 색상 정리 필요 - 특이사항: 램프는 일반도로로 처리
  - 교통정보 재탐색 주기 개발
- 앱 개발자 2: MMC 검토 / gitbook 가이드(번역 문구 정리 ~9/30, kdocs를 ChatGPT로 번역)
- 앱 개발자 4
  - 멀티 경로 기능 추가 - MMC 멀티경로 탐색 규격 적용(멀티경로 포맷만 유지)
  - TomTom Geocoding/Rev.Geocoding API의 NaviSDK API화 - 리턴 객체 변환
  - 경유지 시나리오 적용 (처음 등장)
- 추가: 1개 앱 다국가 지원 / **구글 픽셀 4a 단말 대여 요청(mmc용)** (처음 등장)
- 전시회 버전
  - 경로선 교통정보 표출 - **완료**
  - 멀티 경로 기능: 도착 시 전체경로 표출, 모든 경로 표출 (처음 등장)
  - 경유지 UI, 지도 야간테마(디자인 담당 책임), 지도 초기위치 (0,0) 이슈(9/24와 동일), 소스 난독화 aar
  - TBT 이슈(직진인데 좌/우측 안내) - 탐색엔진 확인 중: **유턴 관련 내용이 7,7,7,7 연속일 때 첫 번째 7만 사용** (결정/가설, 처음 등장)
  - 터널 진행 중 자차 UI, 차로정보

## 항목 상태 추적

| 항목 | 처음 | 상태 |
|---|---|---|
| 터널 안내(DEMO 앱) | 9/17 | 9/24 완료 |
| ETA 표출 방식 개선 | 9/17 | 9/24 완료 (24시간제 중국, 12시간제 그 외) |
| 효과음 전용 볼륨 버튼 | 9/17(진행) | 9/24 완료 |
| 경로선 교통정보 | 9/17 | 9/24 갱신 방식 논의, 10/1 완료, 색상 정리와 재탐색 주기 개발은 남음 |
| 멀티 경로 | 9/17 | 10/1까지 진행 |
| 경유지 UI/시나리오 | 9/17(UI) | 10/1 시나리오 적용 시작 |
| 소스 난독화 aar | 9/17 | 10/29 NaviSDK 상품화 스크럼에서 "상시 대응"으로 이월 |
| 지도 야간테마 | 9/17 | "상시 대응"으로 이월 |
| 지도 초기위치 (0,0) | 9/17 | 10/1까지 미해결(불가/미확인) |
| TBT 이슈 | 9/17 | 10/1까지 탐색엔진 확인 중 |
| 터널 중 자차 UI, 차로정보 | 9/17 | 미착수, 이후 "차로 안내"가 상시 대응 항목으로 남음 |
| TomTom API 연동 / 인증 | 8/12(DP 스프린트) | 9/17 완료 |

## Related
- [[sdk-sprints-2025-2026-hub]] — 목차
- [[dp-mmc-engine-maplibre-scrums-2025]] — 이전 단계
- [[navisdk-confluence-sprint-timeline-2024-2026]] — 요약본
- [[orbismap-route-and-tomtom-sdk-review-2025]] — TomTom 연동 검토
- [[orbis-sdk]]

## Sources
- Confluence "[9/17] DEMO/전시회 앱 기능 고도화 #1, 2 - 스크럼" (pageId 1123745793) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[9/24] DEMO/전시회 앱 기능 고도화 #3 - 스크럼" (pageId 1162641410) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[10/1] DEMO/전시회 앱 기능 고도화 #4 - 스크럼" (pageId 1191346177) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
