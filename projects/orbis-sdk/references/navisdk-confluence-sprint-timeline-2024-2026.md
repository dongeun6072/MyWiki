---
title: >-
    NaviSDK 개발 스프린트 타임라인 (2024-10 ~ 2026-07)
category: references
project: orbis-sdk
tags: [orbis-sdk, sprint, kmp, timeline, visibility/internal]
aliases: [NaviSDK 스크럼 이력, NSDK 스프린트, 에어의 성장 스프린트 이후 SDK 개발]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[kmp-cmp-adoption]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/overview
summary: >-
    Confluence 아이나비 에어 & NSDK 스페이스의 스크럼·플래닝 페이지 약 130개를 단계별로 묶었다. 신 NaviSDK 구조 설계(2024-10)부터 Flutter 대응과 유지보수(2026-07)까지의 흐름과 결정 사항.
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T12:00:00+09:00
updated: 2026-10-26T12:00:00+09:00
---

# NaviSDK 개발 스프린트 타임라인 (2024-10 ~ 2026-07)

Confluence 스페이스 "아이나비 에어 & NSDK"에는 주 단위 스크럼 페이지와 스프린트 플래닝/리뷰 페이지가 쌓여 있다. 대부분은 Jira 티켓(`NSDK-###`) 링크 목록이라 내용이 얇고, 결정과 이슈는 "후속 논의"와 "이슈" 칸에 있다. 이 페이지는 그 결정만 뽑아 시간순으로 묶었다. 참여자는 개발 4명(이 중 한 명이 [[이동은]]), 디자이너와 번역 담당 각 1명이다. 사람 이름은 적지 않고 역할로 쓴다.

[[orbis-sdk]]의 개요와 2025-03 PoC 사전 검토([[orbis-navisdk-poc-prep-2025]])의 시간축을 채우는 문서다.

## 단계별 흐름

| 시기 | 스프린트 이름 | 목표와 결정 |
|---|---|---|
| 2024-10 | 초기 환경 구성, Architecture 정의 | SDK 구조를 Navigation Core(내비·지도 인터페이스, 통신, 컴포넌트 표출 로직)와 Navigation UI(플랫폼별 GUI)로 나눈다. 구조도 용어 통일(Core와 Common 구분). 개발은 2트랙: 엔진(정적 라이브러리) 인터페이스, 공통 통신 모듈 ^[inferred] |
| 2024-11 | 초기 모듈 구성, 초기 지도 표출 | Core 인터페이스는 API만 공개(Android와 iOS 모두). 로컬 지도를 내려받아 표출하고 제스처 동작까지. 다운로드 압축 해제는 Okio로 공용화. 인증 로직 개발. 파일 쓰기 권한은 iOS는 필요 없고 Android는 필요 |
| 2024-12 | 내부 API 설계 | 통합검색, 길찾기, 지도 경로선 표출까지. 엔진 데이터를 Core(`NaviMainThread`)가 모으는 구조 설계. 이 스레드가 정말 필요한지, 역할을 상태 관리와 엔진 호출 주기로 나눌지, 동시성 문제가 없는지가 쟁점 |
| 2025-01 ~ 02 | KMP Base 로직 강화 | `NaviMainThread`의 역할을 세분화한다. SMR 컨트롤러(Android 파일 쓰기, iOS fetch 중 Crash는 Dispatcher 변경으로 해결), 위치 관리(`PositionManager`), 외부 공개 클래스는 접두어를 쓰고 내부는 쓰지 않는 규칙(Adapter는 엔진 연동, Manager는 내부 관리) |
| 2025-02 | 주행 Feature와 API 개발 | 주행 컴포넌트(TBT 필수)와 검색·길찾기 API. 이미지와 문자열 공통 리소스 관리 방식(공통 vs OS별) 검토. iOS 모의주행이 멈추던 문제는 `NSTimer`가 비동기 컨텍스트에서 동작하지 않아서였고, 타이머를 메인 스레드에서 만들도록 바꿨다 |
| 2025-03 | 대만향 개발계획, 구조 설계, TomTom 검토 | 해외향 개발 구조 결정과 일정. TomTom SDK/API 검토 → [[orbis-navisdk-poc-prep-2025]] |
| 2025-03 ~ 05 | 엔진(지도/검색/탐색) API 연동 | 검색은 TomTom Search API를 쓰고 Maps SDK의 Search 모듈은 쓰지 않는다. 자차 마커는 `.glb` 3D 모델. 탐색 서버에 Content-Type JSON 변경을 요청하고, TBT 입력 방식은 메인에서 처리한다. 회전 타입은 MVP에서 현 상태 유지. 앱 이름 후보를 논의함(후보 3개) |
| 2025-05 | 메인상태관리와 화면구성 | IPO 실사 대응용 산출물(워크플로와 주요 화면 가이드 PPT 1~2장, 구동 가능한 결과물). 두 지도를 띄우고 뒤로 가기 시 ANR이 발생. TomTom 지도 렌더링 속도 문제 |
| 2025-06 ~ 08 | DP 엔진 & MMC 엔진 | **Maps SDK의 OrbisMap이 제공되지 않아 MapLibre로 자체 구축**하기로 방향을 바꿨다(2025-06 이슈 → DP 엔진 개발). 경로선(기본·지나간 경로·화살표·차기/차차기 유도선), 마커, 현위치, 도로명 없을 때 "일반도로"(영어 Surface Road) 표시, 안전운행 API(고정식은 지도 데이터 주기, 이동식은 실행마다 갱신), 오디오 포커스와 전화 상태 대응. 서브모듈 AAR 빌드와 Maven 배포, 가이드 문서 GitBook 작성, Agent의 TomTom 연동(Search, Safety Camera, Geocoding), 다중 경로 UI |
| 2025-10 | DEMO/전시회 앱 고도화 | 교통정보 재탐색 주기(기본 5분), 유턴 사양, 멀티 경로(MMC 멀티경로 규격만 유지), 앱 하나로 다국가(대만, 싱가포르 빌드), aar 난독화, 터널 안 자차 UI와 차로 정보 |
| 2025-10 ~ 2026-01 | NaviSDK 상품화 #1~#11 | 상용화 준비. 상세 항목은 거의 비어 있다 |
| 2026-01 ~ 03 | Map SDK 상품화 #1~#6 | MapLibre 기반 Map SDK: 프로젝트 구성, 인증, 지도 추가, 카메라, 마커, 도형, 사용자 위치, 클러스터링, 좌표 변환(WGS84 → KATEC, TM, UTM-K, GRS80), 이벤트 콜백, 가이드와 데모 앱. 준상용 서버 구축 |
| 2026-03 | Navi SDK Truck향 | 지도 버전 분기, 탐색 라이브러리 연동, MMC 엔진 교체, API 추가 → [[vehicle-restriction-routing]] |
| 2026-03 ~ 04 | Navi SDK 개선 | 삼성생명 POC → [[drawing-run-sdk]]. 네트워크, MMC, DP, FileManager 코드 개선, AI용 `claude md` 환경 구성 → [[ai-doc-first-development]] |
| 2026-04 ~ 06 | SDK Flutter 대응, 유지보수 | 아래 별도 절 |
| 2026-07 | SDK 유지보수 | 탐색 엔진을 대만 데이터 v26220 판으로 교체. 지도 갱신 방식 정리 |

## 공통 항목 (2026-01 이후 매 스크럼에 반복)

- **스타일**: Style.json을 1벌로 통일(언어, 테마). 초기에는 영어/중국어 각각 라이트·다크 4종이었다.
- **통계**: SDK 사용자 수를 AppKey당으로 센다. NaviSDK와 MapSDK가 AppKey와 UniqueKey(UUID)를 서버에 전달한다.
- **접두어**: NaviSDK는 `inv`, MapSDK는 `igm`.
- **미완 항목**: 인증 실패 시 모든 API 막기(2026-04 API 예외 처리 완료, "인증이 지도 로딩보다 먼저"로 정리), 로그 on/off API(MMC는 만들어 주기로 했고, 탐색 엔진은 디버그 출력이 없어 출력이 생기면 만들기로 함).
- **로드맵(2026 1분기)**: Map SDK 서비스(~3월), 가이드 작업, 웹 연동. 상시 대응은 상용 서버 전환, 차로 안내, 연결로 진입/진출과 회전 구간 안내 강화(대만 현지 평가 지적 사항 → [[taiwan-field-evaluation-2025]]).

## Flutter 대응 (2026-04 ~ 06)

[[orbis-navisdk-architecture-and-flutter-plan]]에 구조와 마일스톤을 따로 적었다. 스크럼 기준 일정은 다음과 같다.

| 단계 | 대상 | 목표일 |
|---|---|---|
| Step 1 | Orbis Navi/Map SDK 플러그인, 샘플, 가이드 | 5/22 (완료. 리스크: 업체 이슈 대응) |
| Step 1 | 국내향 Navi/Map SDK | 6/5 (완료, 배포 준비는 없음) |
| Step 2 | 국내향 Navi SDK Dart 위젯 | 6/30. 70% 정도 완료 후 홀딩했다가 재개 |
| Step 2 | Orbis Navi SDK | 미정 |

- 경쟁사(티맵, 구글) 대비 Flutter 지원 수준을 비슷하게 맞추는 방향. Map SDK를 메인 Flutter 앱의 위젯 트리에 넣으려면 2단계 방식이라 고민한다는 기록이 있다. 잠재 고객 한 곳(자율주행 DRT 지도 플랫폼 공급사)과 NDA를 맺었다.
- 소스는 1벌로 관리하고 발행은 별도로 관리한다. pub.dev에 publisher를 등록했다(2026-05).
- Flutter 초기 init에서 메인 스레드가 막히는 문제는 SDK를 고치지 않고 플러그인 안에 aar를 포함하는 방안으로 정했다.
- 2026-05 이후: Navi SDK 1.0.3 준비(route 라이브러리 1.0.1.6, MMC 0.0.6), Web 기반 인증(Style)으로 다국어와 다크 모드 적용, Navi SDK와 Map SDK를 같이 쓸 때 의존성 충돌(1.0.4에 반영), SDK 에러 처리 구조 일원화, 샘플 앱에 서버 전환 기능 추가. 이 버전들은 [[orbis-sdk]]의 버전 이력과 이어진다.

## 에어 쪽 패치 메모 (SDK 스크럼에 섞여 있음)

2026년 SDK 스크럼에는 에어 앱 패치 항목이 같이 적혀 있다. 3월 패치(광고 SDK 업데이트, 캐시룰렛 적립 비율 조정, 신규 광고 유형), 4월 w3w 완전 제거, 6월 목적지가 고속도로·지하차도일 때 최적 지점 안내 등이다 → [[air-service-stability-release-notes-2023-2026]], [[inavi-air-feature-history]].

## Open Questions

- 2025-10부터 2026-01까지 "NaviSDK 상품화" 스크럼은 본문이 비어 있어 이 기간의 결정 사항은 확인되지 않았다.
- MapLibre로 바꾼 뒤 Orbis 지도 스타일을 어떻게 맞췄는지는 이 페이지들만으로는 알 수 없다. ^[ambiguous]

## Sources

- [Confluence 스페이스 아이나비 에어 & NSDK](https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/overview) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음. 스크럼·플래닝·리뷰 페이지 약 130개를 묶어 정리했다.
