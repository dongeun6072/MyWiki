---
title: >-
    SDK Flutter 대응 스크럼 (2026-05~06)
category: references
project: orbis-sdk
tags: [sdk, scrum, flutter, schedule, visibility/internal]
aliases: [SDK Flutter 대응 스크럼]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1915748658
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1942880273
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1955004556
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1965948960
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1984626690
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/2001141763
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/2015330305
summary: >-
    2026-05~06 SDK Flutter 대응 #1~#8. Flutter Step 1/2 목표일 변화표, Navi 1.0.3/1.0.4, Web 기반 인증, 에어 패치 항목.
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

# SDK Flutter 대응 스크럼 #1~#8 (2026-05 ~ 2026-06)

2026년 5월 6일부터 6월 24일까지의 "SDK Flutter 대응" 스크럼이다. Orbis Navi/Map SDK와 국내향 Navi/Map SDK를 Flutter 플러그인과 Dart 위젯으로 제공하는 작업이며, 목표일 변화와 에어 패치 항목이 함께 적힌다. 이전은 [[sdk-maintenance-scrums-2026]](4/29), 설계 배경은 [[orbis-navisdk-architecture-and-flutter-plan]]이다. 목차는 [[sdk-sprints-2025-2026-hub]].

이 묶음에는 #1, #3, #4, #5, #6, #7, #8이 있고 **#2(5/13 전후)는 포함되어 있지 않다.** 담당 구분은 앱 개발자 1, 4, 2(앱 개발자 2가 Flutter 중심)이다.

## Flutter 일정 변화 한눈에 보기

| 시점 | Step 1 Orbis Navi/Map + 샘플/가이드 | Step 1 국내향 Navi/Map | Step 2 국내향 Navi/Map | Step 2 Orbis Navi/Map |
|---|---|---|---|---|
| 5/20 (#3) | ~5/22 (Risk: 업체 이슈 대응) | ~6/5 (+ 샘플/가이드) | ~6/30 | 미정 |
| 5/27 (#4) | (완료) ~5/22 | ~6/5, 배포 준비는 없음 | ~6/30 | 미정 |
| 6/4 (#5) | (완료) | ~6/5, 배포 준비 없음 | ~6/30 | 미정 |
| 6/10 (#6) | (완료) | (완료), 배포 준비 없음, **국내향 Map SDK 샘플 및 가이드는 "??"(일정 미정)** | 국내향 Navi + 샘플/가이드 ~6/30 | Orbis Navi SDK 미정 |
| 6/17 (#7) | (완료) | (완료), **국내향 Map SDK 샘플/가이드 ~6/30** | 국내향 Navi + 샘플/가이드 ~6/30, **Step 2-1 신설: SDK, Flutter 역할 정의** | Orbis Navi SDK 미정 |
| 6/24 (#8) | (완료) | (완료) | 국내향 Navi ~6/30, Step 2-1 유지 | Orbis Navi SDK 미정 |

- 국내 Step 2 Dart 위젯 현상태(5/20, 5/27): 70% 정도 완료 후 홀딩
- 5/6에는 일정 대신 "WBS 작성" 단계: Orbis Navi SDK/Map SDK, 국내 Navi SDK/Map SDK의 개발 항목, 필요 항목, 대략적 일정

## [5/6] #1 (pageId 1915748658)
- 앱 개발자 1, 4: 항목 없음
- 앱 개발자 2: dart 위젯 - 금주 완료
- Flutter 대응: WBS 작성(Orbis Navi SDK, Map SDK, 국내 Navi SDK, Map SDK) / 개발 항목, 필요 항목, 대략적인 일정
- 공통: 호주향 Style.json 1벌, 통계 진행 중, 상용화 서비스 계획 수립
- Todo: 로그 on/off API

## [5/20] #3 (pageId 1942880273)
- 앱 개발자 1
  - Navi SDK 1.0.3 준비: cocoapods 의존성 연결, (완료) route 1.0.1.6와 MMC 0.0.6 적용
  - Map SDK: 이미지 스케일 보정
- 앱 개발자 2
  - Navi SDK 1.0.3 준비
  - Map SDK: (완료) 데모앱 기능/화면 분석, Flutter 데모앱 개발
  - (완료) pub.dev에 publisher 등록
- 앱 개발자 4
  - Navi SDK 1.0.3 준비: 배포 준비, (완료) route 1.0.1.6와 MMC 0.0.6 적용
  - Map SDK: 사양 비교 테스트
  - (완료) 샘플앱에 서버 전환 기능 추가
- Flutter 일정, 국내 Step 2 Dart 위젯 상태: 위 표 참고
- 공통/Todo 동일

## [5/27] #4 (pageId 1955004556)
- 앱 개발자 1
  - (완료) Navi SDK 1.0.3 준비, (완료) Map SDK 이미지 스케일 보정
  - **Web 기반 인증(Style) 적용** (처음 등장): 다국어, 다크모드
  - **Navi SDK, Map SDK 동시 적용 시 의존성 문제 발생** (처음 등장)
- 앱 개발자 2
  - (완료) Navi SDK 1.0.3 준비, (완료) Map SDK 데모앱 분석, Flutter 데모앱 개발, (완료) pub.dev publisher 등록
  - Dart Widget 개선 및 누락된 Widget 추가 - 국내향 Navi Step 2 (처음 등장)
  - Flutter URL, 개발자 사이트에 추가 (처음 등장)
- 앱 개발자 4
  - (완료) Navi SDK 1.0.3 준비 / (완료) Map SDK 사양 비교 테스트 / (완료) 샘플앱 서버 전환
  - Web 기반 인증(Style) 적용(다국어, 다크모드), Navi/Map 동시 적용 의존성 문제
- Flutter 일정: 위 표
- 공통/Todo 동일

## [6/4] #5 (pageId 1965948960)
- 앱 개발자 1
  - Web 기반 인증(Style) 적용 - 다국어, 다크모드: **Navi 1.0.4, Map 1.0.1**에 포함 예정
  - (완료) Navi SDK, Map SDK 동시 적용 의존성 문제: 1.0.4에 적용
  - (완료) 국내향 SDK xcframework 적용: 차기 배포 시 적용
  - Flutter Guide Stream: 국내향 Step 2 (처음 등장)
- 앱 개발자 2: (완료) Flutter URL, 개발자 사이트 추가 / Map SDK 국내향 Step 1 진행 중 (처음 등장) / Dart Widget 개선 및 누락 Widget 추가(국내향 Navi Step 2)
- 앱 개발자 4: Web 기반 인증(Style) 적용(Navi 1.0.4, Map 1.0.1) / (완료) Navi/Map 동시 적용 의존성 문제: Navi 1.0.3에 적용 완료, Map 1.0.1
- **AIR (처음 등장, 아래 "에어 패치 항목" 참고)**
  - (완료) 후면 카메라 대응(6월): 최근 후면 과속 카메라에서 통과음이 발성되지 않는 이슈(AOS) / 타 내비게이션처럼 후면 카메라 통과 후 약 80m 동안 카메라 안내와 심볼 유지 / 안드로이드 오토 3D 뷰 모드에서 핀치줌 시 조절되는 지도 영역이 2D보다 좁아 보임(24MM 14인치에서 확인, 2D는 정상) - **DP 엔진 확인**
  - (완료) 전남·광주 행정통합 - 지명 및 행정코드 개편: 스텝형 주소검색과 통합검색 지역 필터 표출 방법 변경
  - 배너: 아웃링크 연결 기능 내부 확인(앱 개발자 1과) - Admin은 배너 등록(아웃링크) 타입 필요, Agent는 URL, 앱은 외부 브라우저 연동
  - 고속도로가 목적지인 경우 팝업 표출 - 개발 검토 필요. "아니요(취소)" 선택 시 최적지점 탐색으로 진행
  - 친환경 경로 탐색 - PM 검토: 유종을 탐색엔진에 전달, 유종에 수소 추가(주변 검색, 주행 중 유가 표시와 관련)
- 공통/Todo 동일

## [6/10] #6 (pageId 1984626690, 수정일 6/12)
- 앱 개발자 1: Web 기반 인증(Style)(Navi 1.0.4, **(완료) Map 1.0.1**) / Flutter Guide Stream 국내향 Step 2
- 앱 개발자 2: (완료) Map SDK 국내향 Step 1(원문은 "(완료)...진행중"이 함께 적힘 ^[ambiguous]) / Dart Widget 개선과 누락 Widget 추가
- 앱 개발자 4: Web 기반 인증(Style) (Navi 1.0.4, (완료) Map 1.0.1)
- **(완료) AIR** 제목에 완료 표시
  - (완료) 후면 카메라 대응(6월) - 항목 동일
  - (완료) 전남·광주 행정통합
  - (완료) 배너 - 이미 존재하는 기능 (아웃링크 내부 확인)
  - (완료) 고속도로가 목적지인 경우 팝업
  - (완료) 친환경 경로 탐색 - 현재 유종을 탐색엔진에 전달 (수소 추가는 이 페이지에 없음)
- 공통/Todo 동일

## [6/17] #7 (pageId 2001141763)
- 앱 개발자 1: (완료) Flutter Guide Stream 국내향 Step 2
- 앱 개발자 2: Dart Widget 개선 및 누락 Widget 추가 - 국내향 Navi Step 2
- 앱 개발자 4: **SDK 에러 처리 구조 일원화 - Orbis Navi SDK** (처음 등장)
- Step 2-1: SDK와 Flutter의 역할 정의
- AIR
  - **이번 패치**: 고속도로/지하차도/고가도로가 목적지인 경우 팝업 표출(개발 검토 필요). "아니요(취소)" 선택 시 최적지점 탐색 진행 / 경유지도 팝업 유지 / 문구 변경: "일반 도로"에서 "주변 도로"로 (6/4~6/10의 고속도로 팝업 항목이 구체화됨)
  - **차기 패치**: 지점을 자동 변경하고 인지할 수 있도록 하는 시나리오 - 경로 선택 화면에서 목적지 확대 시 지점 핀 사양 추가, 탐색 지점에서 목적지 핀 LineTo(DP 엔진 논의)

## [6/24] #8 (pageId 2015330305)
- 앱 개발자 1, 2: Dart Widget 개선 및 누락 Widget 추가 - 국내향 Navi Step 2
- 앱 개발자 4: (완료) SDK 에러 처리 구조 일원화 - Orbis Navi SDK / **교통정보 On: 경로 선택, 옵션 선택 시 회색으로 표출** (처음 등장)
- **Orbis - 신규 탐색엔진 적용** (처음 등장)
  - INAVI Route Server Data for Taiwan (v26220)
  - 지도 업데이트: 현재는 서비스 포트에 지도만 변경(Agent 지도 업로드, 탐색엔진 지도 교체, Agent 지도 오픈). 차후에는 SDK가 Agent에 현재 지도 버전을 전달하고 Agent가 SDK의 지도 버전(SDK 앱 버전)에 따라 탐색 포트를 분기
- AIR 차기 패치: 지점 자동 변경 시나리오(6/17과 동일)
- 이후는 [[sdk-maintenance-scrums-2026]]의 7/1로 이어진다.

## 에어 패치 항목 연표 (Flutter 대응 스크럼 내)
| 항목 | 6/4 | 6/10 | 6/17 | 6/24 |
|---|---|---|---|---|
| 후면 카메라 대응(6월) | 진행/완료 표기 | 완료 | - | - |
| 전남·광주 행정통합 | 완료 | 완료 | - | - |
| 배너 아웃링크 | 내부 확인 | 완료(기존 기능) | - | - |
| 고속도로 목적지 팝업 | 개발 검토 | 완료 | 이번 패치 상세 | - |
| 친환경 경로 탐색 | PM 검토 | 완료 | - | - |
| 지점 자동 변경 시나리오 | - | - | 차기 패치 | 차기 패치 |

## Related
- [[sdk-sprints-2025-2026-hub]] — 목차
- [[orbis-navisdk-architecture-and-flutter-plan]] — Flutter 계획과 구조
- [[sdk-scrum-common-items-2026]] — 공통 항목
- [[sdk-maintenance-scrums-2026]] — 이어지는 유지보수
- [[inavi-air]] — 에어 앱
- [[orbis-sdk]]

## Sources
- Confluence "[5/6] SDK Flutter 대응 #1 - 스크럼" (pageId 1915748658) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[5/20] SDK Flutter 대응 #3 - 스크럼" (pageId 1942880273) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[5/27] SDK Flutter 대응 #4 - 스크럼" (pageId 1955004556) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[6/4] SDK Flutter 대응 #5 - 스크럼" (pageId 1965948960) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[6/10] SDK Flutter 대응 #6 - 스크럼" (pageId 1984626690) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[6/17] SDK Flutter 대응 #7 - 스크럼" (pageId 2001141763) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "[6/24] SDK Flutter 대응 #8 - 스크럼" (pageId 2015330305) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
