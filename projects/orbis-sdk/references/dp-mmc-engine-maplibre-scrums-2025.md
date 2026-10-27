---
title: >-
    DP엔진 & MMC 엔진 스크럼 (2025-06~09, MapLibre 자체 구축)
category: references
project: orbis-sdk
tags: [sdk, scrum, maplibre, mmc, dp-engine, visibility/internal]
aliases: [DP 엔진 & MMC 엔진 스크럼 #1~#13, 6/9 플래닝]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1017741313
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1049329665
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1082589185
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/844726273
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/849969153
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/869827406
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/888373249
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/905674753
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/921698305
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/936706049
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/952139777
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/969146369
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/987103233
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/998277121
summary: >-
    2025년 6~9월 DP엔진 & MMC 엔진 스프린트 스크럼(#1~#13). MapLibre 자체 구축, 안전운행, 도로명, TomTom 연동, 티켓과 반복 항목 추적.
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

# DP엔진 & MMC 엔진 스크럼 #1~#13 (2025-06 ~ 2025-09)

2025년 6월 9일부터 9월 3일까지 이어진 "DP엔진 & MMC 엔진" 스프린트의 스크럼 기록이다. Orbis Maps SDK(OrbisMap)가 제공되지 않아 MapLibre 기반으로 지도 표출(DP, Display) 엔진을 자체 구축하고, 탐색 결과를 따라가는 MMC(맵매칭/안내 구동) 엔진을 적용하는 시기다. 이후 단계는 [[demo-exhibition-app-scrums-2025]]와 [[navisdk-commercialization-scrums-2025-2026]]로 이어지며 전체 목차는 [[sdk-sprints-2025-2026-hub]]에 있다.

원본 페이지의 번호는 #1~#13이며(요청 메모의 #10까지가 아니라 #13까지 존재), #1은 "플래닝/리뷰" 페이지와 "스크럼" 페이지가 따로 있다. 모든 스크럼 표의 열은 `담당자 / 완료 / 진행중·할것 / 비고`이고, 비고 열은 전 페이지에서 비어 있다. 담당자 행은 1=앱 개발자 1, 2=앱 개발자 2, 3=앱 개발자 3, 4=앱 개발자 4([[이동은]])로 표기한다.

## 공통 목표 (모든 스크럼 머리말)
- 메인상태 관리
- DP 엔진 개발 및 적용 (MapLibre)
- MMC 엔진 적용
- 화면별 GUI 구성
- #1, #2 스크럼에는 공통 항목이 추가로 있음: "공통 (~5/21)" 아래 "IPO 실사 관련, Orbis map Navi SDK 진행 관련 설명 및 실사 대응", "디자인 포함 workflow와 UI 일부가 포함된 형태의 구동 산출물" (#3부터 사라짐)

## [6/9] #1 플래닝/리뷰 (pageId 844726273)
- 참석: 앱 개발자 1, 2, 3, 4 (앱 개발자 3은 라이선스 미할당 표시)
- 스프린트 목표: DP 엔진 개발 및 적용 / MMC 엔진 적용 / 화면별 GUI 구성
- 스프린트 기간, 완료 항목, 다음 스프린트 이관: 템플릿 그대로 비어 있음
- 차기 스프린트 플래닝 준비: 목표/기간/이슈/기타 의견/요청 사항(지도, 탐색, 검색 세부 항목은 제목만 있고 내용 없음)

## [6/11] #1 스크럼 (pageId 849969153)
**티켓**

| 담당 | 완료 | 진행중/할것 |
|---|---|---|
| 앱 개발자 1 | NSDK-442 | NSDK-446, NSDK-448 |
| 앱 개발자 2 | - | NSDK-447 |
| 앱 개발자 4 | - | NSDK-444, NSDK-449 |

**이슈**: Maps SDK OrbisMap 미제공으로 인한 자체 구축 검토 필요. (결정 흐름: 이 이슈가 이후 MapLibre 기반 DP 엔진 자체 구축의 배경이다.)

**영역별 진행**
- 앱 개발자 1
  - (hold) 안전운행 API 적용: DB 수신 확인 대기 (처음 등장)
  - MapLibre 검토: 개발항목 리스트업
- 앱 개발자 2
  - MMC 엔진 적용: 경로 파일 저장, MMC 연동
  - 스크린내비게이터 (처음 등장)
- 앱 개발자 4
  - (완료) TTS 발성로직
  - MapLibre 검토

## [6/17] #2 스크럼 (pageId 869827406)
**티켓**

| 담당 | 완료 | 진행중/할것 |
|---|---|---|
| 앱 개발자 1 | NSDK-442, NSDK-446, NSDK-451 | NSDK-448 |
| 앱 개발자 2 | - | NSDK-447 |
| 앱 개발자 4 | NSDK-444, NSDK-450, NSDK-449 | NSDK-452 |

**이슈**: Maps SDK OrbisMap 미제공으로 인한 자체 구축 검토 필요 (유지).

**영역별 진행**
- 앱 개발자 1
  - (hold) 안전운행 API 적용 - DB 수신 확인
  - (완료) MapLibre 검토 - 개발항목 리스트업
  - DP: 경로선 (처음 등장)
- 앱 개발자 2
  - (완료) MMC 엔진 적용 - 경로 파일 저장, MMC 연동
  - (완료) Orbis Search API 검토 및 적용 완료
  - MMC: 이탈재탐색 테스트, 안내 연동(모의주행) 검토
  - 스크린내비게이터
- 앱 개발자 4
  - (완료) TTS 발성로직, (완료) MapLibre 검토
  - 지도 초기 다운로드: 버전 파일 형식을 txt에서 json으로 변경
  - DP: (완료) 마커, 현위치

## [6/25] #3 스크럼 (pageId 888373249)
**티켓**

| 담당 | 완료 | 진행중/할것 |
|---|---|---|
| 앱 개발자 1 | NSDK-454 | NSDK-448, NSDK-457 |
| 앱 개발자 2 | NSDK-447, NSDK-453, NSDK-456 | NSDK-459 |
| 앱 개발자 4 | NSDK-452, NSDK-443, NSDK-455 | NSDK-458 |

**영역별 진행**
- 앱 개발자 1
  - (hold) 안전운행 API 적용 - DB 수신 확인
  - DP: (완료) 경로선 - 기본 경로, 지나간 경로, 경로선 내 화살표
  - 차기/차차기 유도선 (처음 등장), 자차 이미지 교체 (처음 등장)
  - 도로명 - 전체경로: 도로명이 없는 경우 "일반도로" 표출, 번역 필요 (처음 등장) / ETA
- 앱 개발자 2
  - MMC: 이탈재탐색 기능만 완료, 연동 미완료
  - 안내 연동(모의주행) 검토, 스크린내비게이터
- 앱 개발자 4
  - DP: (완료) 마커, (완료) 현위치
  - 지도 렌더링 속도 개선 - 전체경로 (처음 등장)

## [7/2] #4 스크럼 (pageId 905674753)
**티켓**

| 담당 | 완료 | 진행중/할것 |
|---|---|---|
| 앱 개발자 1 | NSDK-448, NSDK-457 | NSDK-463 |
| 앱 개발자 2 | - | NSDK-459 |
| 앱 개발자 4 | NSDK-458, NSDK-460 | NSDK-462, NSDK-464 |

**영역별 진행**
- 앱 개발자 1
  - 안전운행 API 적용 - DB 수신 확인 ((hold) 표시가 빠지고 진행 상태로 바뀜)
  - 도로명 - 전체경로: 도로명 없는 경우 확장, 없으면 "일반도로" 표출 - 번역 필요 / 목적지명이 없는 경우 (처음 등장) / ETA
- 앱 개발자 2
  - MMC: 이탈재탐색 기능만 완료(연동 미완료), 안내 연동(모의주행) 검토, 스크린내비게이터
- 앱 개발자 4
  - 비정상 종료 (처음 등장): 앱 실행 후 background / 화면 잠금 상태에서 발생
  - MMC: initmap 호출 시 UI Thread가 5초 holding - 문의
  - UI: MapLibre 교체 - Compass button 구현
- 언어 담당 개발자(표에는 없음): 언어 - 앱별 언어 변경 설정 검토 (처음 등장)

## [7/9] #5 스크럼 (pageId 921698305)
**티켓**

| 담당 | 완료 | 진행중/할것 |
|---|---|---|
| 앱 개발자 1 | NSDK-463 | NSDK-467 |
| 앱 개발자 2 | - | NSDK-459 |
| 앱 개발자 4 | NSDK-462, NSDK-464 | NSDK-466 |

**영역별 진행**
- 앱 개발자 1
  - (완료) 안전운행 API 적용 - DB 수신 확인
    - 갱신주기: 고정식 카메라는 지도데이터 주기, 이동식 카메라는 실행할 때마다 갱신 (결정)
  - 도로명 - 전체경로 & ETA: (완료) 도로명 없는 경우 확장, 없으면 "일반도로" 표출. 한국어 문구는 "Surface Road"로 변경 (결정)
  - 목적지명이 없는 경우 (진행)
  - 안전운행 안내 (처음 등장)
- 앱 개발자 2: MMC 이탈재탐색만 완료/연동 미완료, 안내 연동(모의주행) 검토, 스크린내비게이터
- 앱 개발자 4
  - 비정상 종료 - 앱 실행 후 background / 화면 잠금 상태
  - MMC 메인소스 전달 검토 (처음 등장)
- 언어 담당 개발자: 앱별 언어 변경 설정 검토

## [7/16] #6 스크럼 (pageId 936706049, 수정일 7/23)
앱 개발자 3이 표에 처음 합류(ViewModel/GUI 담당).

| 담당 | 완료 | 진행중/할것 |
|---|---|---|
| 앱 개발자 1 | - | NSDK-467 |
| 앱 개발자 2 | NSDK-459 | NSDK-469 |
| 앱 개발자 3 | - | NSDK-470 |
| 앱 개발자 4 | NSDK-468, NSDK-466 | NSDK-471 |

- 앱 개발자 1
  - 도로명 - 전체경로 & ETA: (완료) 도로명 없는 경우 확장/"일반도로"(한국어 Surface Road), 목적지명 없는 경우 (진행)
  - 안전운행 음성 안내
  - 경로선: 회전(차기, 차차기) 유도선 표출 (처음 등장 시점은 6/25의 차기/차차기 유도선)
- 앱 개발자 2: MMC v0.1.0 검토 (처음 등장), 스크린내비게이터
- 앱 개발자 3: ViewModel 초기 개발(Flow 연동 완료), GUI 개발
- 앱 개발자 4: 안전운행 심볼 (처음 등장)
- 언어 담당 개발자: 앱별 언어 변경 설정 검토

## [7/23] #7 스크럼 (pageId 952139777)

| 담당 | 완료 | 진행중/할것 |
|---|---|---|
| 앱 개발자 1 | NSDK-475 | NSDK-472, NSDK-476 |
| 앱 개발자 2 | - | NSDK-469, NSDK-473 |
| 앱 개발자 3 | - | NSDK-470 |
| 앱 개발자 4 | NSDK-471 | - |

- 앱 개발자 1
  - 도로명: (완료) 전체경로 & ETA, (완료) 도로명 없는 경우 확장/"일반도로"(Surface Road), (완료) 목적지명 없는 경우
  - 다국어 처리 (처음 등장)
  - 안전운행 음성 안내, 경로선 회전(차기/차차기) 유도선 표출
- 앱 개발자 2
  - MMC v0.1.0 검토
  - 서브모듈 AAR 빌드 및 maven 배포: SDK와 서브모듈 버전 관리 (처음 등장)
  - 스크린내비게이터
- 앱 개발자 3: (완료) ViewModel 초기 개발(Flow 연동 완료), GUI 개발 - 이미지 로딩 방식 변경(UI에서 Core로)
- 앱 개발자 4: 안전운행 심볼
- 언어 담당 개발자: 앱별 언어 변경 설정 검토

## [7/30] #8 스크럼 (pageId 969146369)

| 담당 | 완료 | 진행중/할것 |
|---|---|---|
| 앱 개발자 1 | - | NSDK-479, NSDK-482 |
| 앱 개발자 2 | - | NSDK-473, NSDK-485 |
| 앱 개발자 3 | NSDK-477 | - |
| 앱 개발자 4 | NSDK-481 | NSDK-483 |

- 앱 개발자 1: 안전운행 음성 안내 / 지도 - Tile 지도 스타일 검토, 이슈 리스트업 (처음 등장)
- 앱 개발자 2: MMC 검토 / 가이드 문서 작성 - gitbook (처음 등장; 개발용 계정으로 작성한 뒤 운영 계정으로 전환하는 방식이라고 적혀 있고 계정명은 원본에 있음, 미수록)
- 앱 개발자 3: 차기 개발 항목 협의 및 결정, Jira 티켓 생성
- 앱 개발자 4: 오디오 Focus 및 전화 상태 대응 (처음 등장)
- 언어 담당 개발자: 앱별 언어 변경 설정 검토 (마지막 등장)

## [8/6] #9 스크럼 (pageId 987103233)

| 담당 | 완료 | 진행중/할것 |
|---|---|---|
| 앱 개발자 1 | NSDK-482, NSDK-486 | NSDK-490 |
| 앱 개발자 2 | NSDK-485 | NSDK-489, NSDK-473 |
| 앱 개발자 3 | - | NSDK-488 |
| 앱 개발자 4 | NSDK-483 | NSDK-487 |

- 앱 개발자 1: 지도 애니메이션 개선 (처음 등장) - 자차(하드웨어 가속 필요), 지나간 경로, 차기/차차기 화살표
- 앱 개발자 2: MMC 검토, gitbook 가이드 문서 작성
- 앱 개발자 3: Agent 연동 검토 - ServiceGate (처음 등장)
- 앱 개발자 4: API Reference 미개발 현황 리스트업, 우선순위 선정 (처음 등장)

## [8/12] #10 스크럼 (pageId 998277121)

| 담당 | 완료 | 진행중/할것 |
|---|---|---|
| 앱 개발자 1 | NSDK-494, NSDK-490 | NSDK-499 |
| 앱 개발자 2 | NSDK-496 | NSDK-489, NSDK-473 |
| 앱 개발자 3 | NSDK-488 | - |
| 앱 개발자 4 | NSDK-487, NSDK-491 | NSDK-492, NSDK-495 |

- 앱 개발자 1: 지도 애니메이션 개선 - 차기/차차기 화살표
- 앱 개발자 2: MMC 검토, gitbook 가이드 문서 작성
- 앱 개발자 3: Agent 연동 - Servicegate(지도 정보), searchRoute
- 앱 개발자 4: API Reference 미개발 항목 개발 (리스트업에서 개발로 전환)
- Agent(별도 섹션, 처음 등장): TomTom API 연동 - TomTom Search, TomTom Safety Camera, TomTom Geocoding/Rev.Geocoding
- 추가(처음 등장): 다중경로 지원에 따른 UI/UX 변경 / TomTom Geocoding/Rev.Geocoding API의 NaviSDK API화

## [8/20] #11 스크럼 (pageId 1017741313)

| 담당 | 완료 | 진행중/할것 |
|---|---|---|
| 앱 개발자 1 | - | NSDK-499 |
| 앱 개발자 2 | - | NSDK-489, NSDK-473 |
| 앱 개발자 3 | NSDK-497 | NSDK-502 |
| 앱 개발자 4 | NSDK-492, NSDK-495 | NSDK-501 |

- 앱 개발자 1
  - 지도 애니메이션 개선 - 차기/차차기 화살표
  - MMC 주기에 따른 업데이트 (처음 등장): 경로선 애니메이션 업데이트 주기는 "?초"로 미정, 안내요소 업데이트는 1초 / 0.5초
  - 안내사양 정리: 구글과 비교 (처음 등장)
- 앱 개발자 2: MMC 검토, gitbook 가이드 문서 작성, 하단버튼 개선 (처음 등장)
- 앱 개발자 3: Agent 연동 - (완료) Servicegate(지도 정보), searchRoute 진행 / 데이터 모델 관련 Backend 서브모듈 통합 구현 (처음 등장)
- 앱 개발자 4: API Reference 미개발 항목 개발
- Agent: TomTom API 연동(Search, Safety Camera, Geocoding/Rev.Geocoding) 유지 / 인증 - Token, KeyCode (처음 등장) / 신규 API - Key(TomTom) (처음 등장)
- 추가: 다중경로 지원 UI/UX 변경, TomTom Geocoding/Rev.Geocoding의 NaviSDK API화

## [8/27] #12 스크럼 (pageId 1049329665)

| 담당 | 완료 | 진행중/할것 |
|---|---|---|
| 앱 개발자 1 | NSDK-499, NSDK-503, NSDK-508 | NSDK-511 |
| 앱 개발자 2 | - | NSDK-489, NSDK-473, NSDK-510 |
| 앱 개발자 3 | NSDK-505, NSDK-507 | NSDK-502 |
| 앱 개발자 4 | NSDK-501 | NSDK-506, NSDK-509 |

- 앱 개발자 1: 탐색 실패 케이스 처리 (처음 등장)
- 앱 개발자 2: MMC 검토, gitbook 가이드 문서 작성, 검색 실패 케이스 처리 (처음 등장)
- 앱 개발자 3
  - 데이터 모델 관련 Backend 서브모듈 통합 구현
  - **이슈**: 메인소스 머지 규약 필요 (현재 머지 담당은 앱 개발자 3)
- 앱 개발자 4
  - API Reference 문서화 개선 (Kdoc) (처음 등장)
  - 볼륨버튼 동작 구현 (처음 등장): 음소거, 효과음+안내음 제공
- Agent: TomTom API 연동 3종, 인증(Token, KeyCode), 신규 API Key(TomTom)
- 추가
  - 다중경로 UI/UX 변경, Geocoding API의 NaviSDK API화
  - 1개 앱 다국가 지원 (처음 등장): 국가별로 앱 출시, 빌드 구성(대만향, 싱가폴향)
  - 효과음 추가 시 볼륨 버튼으로 효과음만 제공하는 기능 제공 (처음 등장)

## [9/3] #13 스크럼 (pageId 1082589185)

| 담당 | 완료 | 진행중/할것 |
|---|---|---|
| 앱 개발자 1 | NSDK-514 | NSDK-511, NSDK-519 |
| 앱 개발자 2 | NSDK-510 | NSDK-489, NSDK-473, NSDK-517 |
| 앱 개발자 3 | NSDK-502 | - |
| 앱 개발자 4 | NSDK-506, NSDK-509, NSDK-513, NSDK-515 | NSDK-516 |

- 앱 개발자 1: (완료) 탐색 실패 케이스 처리 / 3rd Party 탐색결과 관리 체계 개선 (ID 체계) (처음 등장)
- 앱 개발자 2
  - MMC 검토, gitbook 가이드 문서 작성
  - (완료) 검색 실패 케이스 처리
  - (완료) 검색 파라미터: `countrySet` - 검색 결과를 지정 국가로 제한(임의 지정), `language` - 검색 결과 반환 언어(OS 언어)
  - 샘플앱 타임락 기능 추가: 현재 시간은 Agent Response 시간 기준 (처음 등장)
- 앱 개발자 3: (완료) 데이터 모델 관련 Backend 서브모듈 통합 구현(메인소스 머지 규약 필요 유지) / TomTom API Backend 서브모듈 통합 구현 (처음 등장)
- 앱 개발자 4: (완료) API Reference 문서화 개선(Kdoc), (완료) 볼륨버튼 동작 / 인증/권한/지도/서비스게이트 실패 케이스 처리 (처음 등장) / 효과음 추가 시 볼륨 버튼 효과음만 제공 기능
- Agent: TomTom API 연동 3종, 인증(Token, KeyCode) (신규 API Key(TomTom)은 이 페이지에서 빠짐)
- 추가: 다중경로 UI/UX 변경, Geocoding API의 NaviSDK API화, 1개 앱 다국가 지원(대만향/싱가폴향 빌드)

## 반복 항목 추적 (처음 등장 -> 마지막 상태)

| 항목 | 처음 | 상태 변화 |
|---|---|---|
| Orbis Maps SDK 미제공, 자체 구축 검토 | 6/11 | 6/17까지 이슈 유지, 이후 MapLibre 기반 구축으로 진행 |
| MapLibre 검토(개발항목 리스트업) | 6/11 | 6/17 완료 |
| 안전운행 API 적용 DB 수신 확인 | 6/11 | 6/11, 6/17, 6/25 hold, 7/2 진행, 7/9 완료 (갱신주기 확정) |
| 도로명 "일반도로"(Surface Road) | 6/25 | 7/9 도로명 없는 경우 완료, 7/23 목적지명 없는 경우까지 완료 |
| MMC 이탈재탐색 | 6/17(테스트) | 6/25 기능 완료/연동 미완료, 이후 같은 문구 유지 후 7/16 v0.1.0 검토로 이동 |
| MMC 안내 연동(모의주행) 검토 | 6/17 | 7/9까지 진행, 이후 미언급 |
| 스크린내비게이터 | 6/11 | 7/23까지 진행, 이후 미언급 |
| 앱별 언어 변경 설정 검토 | 7/2 | 7/30까지 진행(완료 표시 없음) |
| 비정상 종료(background/화면 잠금) | 7/2 | 7/9까지, 이후 미언급 |
| gitbook 가이드 문서 | 7/30 | 9/3까지 진행(완료 표시 없음), 이후 DEMO 스크럼으로 이월 |
| TomTom API 연동(Agent) | 8/12 | 9/17 완료 |
| 다중경로 UI/UX | 8/12 | DEMO 스크럼으로 이월 |
| 1개 앱 다국가 지원(대만향/싱가폴향) | 8/27 | 계속 이월 |

## 결정 사항 요약
- 안전운행 카메라 갱신주기: 고정식=지도데이터 주기, 이동식=실행 시마다 (7/9)
- 한국어 문구 "일반도로" 대신 "Surface Road" 사용 (7/9)
- 메인소스 머지 규약 수립 필요 (8/27, 9/3까지 미해결)
- 검색 `language`는 OS 언어, `countrySet`은 임의 지정 (9/3)

## Related
- [[sdk-sprints-2025-2026-hub]] — 이 묶음 전체 목차
- [[demo-exhibition-app-scrums-2025]] — 이어지는 DEMO/전시회 스프린트
- [[navisdk-confluence-sprint-timeline-2024-2026]] — 요약본 타임라인
- [[orbis-sdk]] — 프로젝트 허브
- [[orbis-navisdk-architecture-and-flutter-plan]] — 구조와 Flutter 계획

## Sources
- Confluence "[8/20] DP엔진 & MMC 엔진 #11 - 스크럼" (pageId 1017741313) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[8/27] DP엔진 & MMC 엔진 #12 - 스크럼" (pageId 1049329665) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[9/3] DP엔진 & MMC 엔진 #13 - 스크럼" (pageId 1082589185) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[6/9] DP 엔진 & MMC 엔진 #1 - 플래닝/리뷰" (pageId 844726273) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[6/11] DP엔진 & MMC 엔진 #1 - 스크럼" (pageId 849969153) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[6/17] DP엔진 & MMC 엔진 #2 - 스크럼" (pageId 869827406) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[6/25] DP엔진 & MMC 엔진 #3 - 스크럼" (pageId 888373249) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[7/2] DP엔진 & MMC 엔진 #4 - 스크럼" (pageId 905674753) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[7/9] DP엔진 & MMC 엔진 #5 - 스크럼" (pageId 921698305) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[7/16] DP엔진 & MMC 엔진 #6 - 스크럼" (pageId 936706049) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[7/23] DP엔진 & MMC 엔진 #7 - 스크럼" (pageId 952139777) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[7/30] DP엔진 & MMC 엔진 #8 - 스크럼" (pageId 969146369) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[8/6] DP엔진 & MMC 엔진 #9 - 스크럼" (pageId 987103233) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[8/12] DP엔진 & MMC 엔진 #10 - 스크럼" (pageId 998277121) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
