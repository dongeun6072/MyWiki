---
title: >-
    tech_talk KMP·Android·iOS 소식과 사내 산출물
category: references
tags: [company, kmp, cmp, android, ios, tech-radar, visibility/internal]
aliases: [INAVI Maps Compose 0.4.0, mtech-demo-delivery, iPhone Duo]
relationships:
  - target: "[[entities/모빌리티개발셀]]"
    type: derived_from
  - target: "[[concepts/kmp-cmp-adoption]]"
    type: extends
  - target: "[[references/cell-tech-radar-2023-2026]]"
    type: related_to
summary: >-
    tech_talk 채널의 KMP/CMP·Android·iOS 소식(2026)과 셀이 만든 CMP 지도 SDK 0.4.0 변경점, 표준 아키텍처 데모, Firebase iOS 크래시 이슈 정리.
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0.0
base_confidence: 0.47
lifecycle: draft
lifecycle_changed: 2026-10-27
tier: supporting
created: 2026-10-27
updated: 2026-10-27
sources:
  - "slack:#모빌리티개발셀_tech_talk"
---

# tech_talk KMP·Android·iOS 소식과 사내 산출물

[[entities/모빌리티개발셀]]의 기술 공유 채널에서 2026년에 올라온 내용 중 업무와 직접 닿는 것이다. 2023~2025 동향은 [[references/cell-tech-radar-2023-2026]], 셀의 KMP/CMP 경험은 [[concepts/kmp-cmp-adoption]].

## 사내 산출물

### INAVI Maps SDK for Compose Multiplatform

- 2026-09-17 `inavi-maps-sdk-compose` **0.4.0** 배포(0.1.11 미만 버전은 앱 키 포함 문제로 저장소에서 제거됨 → [[concepts/cell-security-lessons]]).
- 새 기능: 마커 클러스터링, 실내 층 전환, 커스텀 지도 스타일, POI 선택(영역 기준), 경로 진행 지점 관찰(통과 위치·각도), 카메라 위치 복원, 마커 타이틀·정보 창 옵션, 틸트 범위·초점·로고 위치 옵션.
- 브레이킹 체인지: 지속 시간 인자가 밀리초 정수에서 `Duration`으로, 여백이 `EdgeInsets`에서 `PaddingValues`로 바뀌고, `indoorEnabled` 기본값이 false에서 true가 됐다.
- 릴리스 빌드에서 라이브러리 로그를 출력하지 않고, Android 아티팩트를 난독화했으며(공개 API는 유지), 소스 JAR 대신 Dokka javadoc JAR을 제공한다.
- 09-18 외부 배포용 CMP 데모를 공유하고 README·GUIDE 개선 의견을 받았다.

### CMP/KMP 표준 아키텍처 레퍼런스 (2026-07-29)

- 배달 앱을 벤치마킹한 데모 저장소(KMP + CMP, Android·iOS 모두 UI와 로직을 commonMain에 둠).
- Clean Architecture + MVI(Orbit), NIA 스타일 멀티모듈(core 15개, feature 12개). 외부 API는 지도 SDK뿐이고 나머지는 mock이라 오프라인에서도 전 화면이 동작한다.
- 유즈케이스: 지도 SDK 래핑, Material3 격리와 자체 래핑 컴포넌트 + 가변 폰트, Room3 + Paging 3(오프라인 우선), ECDH→AES-GCM 세션 키 핸드셰이크, type-safe Navigation Compose와 탭별 백스택·커스텀 딥링크, Koin DI.
- 활용: 신규 프로젝트의 모듈 구조·컨벤션 템플릿, `checkInvArchitecture` Gradle 작업으로 규칙(Material 격리, feature 간 의존 금지)을 자동 검증한다.

### 기타

- M.Tech Dev Wiki 시작(06-22): [[concepts/claude-code-team-practices]].
- 08-28 M.Tech 데모의 Auth 리팩토링을 동행맵에 참고하도록 공유(timeline 참고).

## KMP·Kotlin·Compose

- Kotlin 2.2.21 → 2.3.0 마이그레이션 때 iOS의 `TextField`에서 링키지 오류가 발생하는 이슈(01-14). KMP의 SPM 가져오기가 experimental로 들어왔고(03-19), 이를 이용한 Firebase 포팅 모듈이 한국 Kotlin 사용자 모임에 올라왔으나 추가 검증이 필요하다(07-29).
- AGP 9.0에서 KMP 포함 빌드 구성이 크게 바뀌었다(03-04). KMP용 AGP 공식 문서가 정리돼 있다(04-15).
- Room은 KMP를 선언한 뒤 2.x 안정 제공, 3.0 알파는 Kotlin First, 코루틴 강화, 웹까지 지원하는 멀티플랫폼 DB로 바뀔 예정(04-15).
- Jetpack Compose 4월 업데이트는 slot table 개선으로 성능이 나아졌고, 실험실 모드로 Flexbox 레이아웃이 들어왔다(04-24).
- View 기반 라이브러리가 공식적으로 유지 관리 모드가 됐고 Compose가 우선이라는 안내(05-20). CMP도 iOS 접근성을 지원하며 Android는 네이티브 Compose라 기본 지원한다(07-09).
- KMP 도입 근거 아티클(의사결정자 설득용), KMP 소식 모음 사이트, JetBrains의 KMP 라이브러리 검색기, CMP 미디어 플레이어 라이브러리가 소개됐다.
- Android 17에서 무선 디버깅(ADB over Wi-Fi) 개선(09-14), 구글이 공개한 실기기 테스트 자동화 도구(에이전트가 MCP로 실기기를 조작, 09-10), AppFunctions(앱 기능을 온디바이스 MCP 서버처럼 에이전트에 노출, 07-29)가 공유됐다.

## iOS

- **iPhone Duo(폴더블)**: 개발 가이드라인 갱신(09-10), CMP 지원 이슈 추적 티켓(09-16), Xcode 27.1 정식에서 듀오 시뮬레이터 사용 가능(10-20), **2027-04부터 iPhone Duo 스크린샷이 필수**로 바뀐다는 공지(10-07). 스토어 제출 준비물에 영향이 있다.
- 2026-08-26 Apple 이메일 가리기 도메인이 바뀌었다(`privaterelay.appleid.com` → `private.icloud.com`). 로그인 서버에서 이 도메인을 허용 목록으로 쓰고 있다면 점검 대상이다. ^[inferred]
- Xcode는 여러 버전을 병행 설치할 수 있다.

## 장애·검사 이슈

- **Firebase iOS Analytics 크래시(2026-09-29)**: 실험 응답을 처리하는 과정에서 "key cannot be nil" 예외로 운영 앱이 크래시했다. 당일 해소된 것으로 보이며, 셀 서비스의 Crashlytics에서는 해당 에러로 보이는 크래시가 서비스별로 수 건~수백 건(커넥티드 306, 하이핀 215 등) 확인됐다. 배포하지 않아도 외부 SDK 때문에 크래시가 날 수 있다는 사례다.
- 2026-09-02 스토어 바이너리 검사에서 **난독화 비율**도 확인한다는 이야기가 커넥티드 프로젝트 스크럼에서 나왔다(SDK 쪽 난독화 적용 배경).
- 05-14 Bitbucket 접속 장애가 한 번 더 있었다.

## Sources

- 슬랙 `#모빌리티개발셀_tech_talk`(2026-01~10).
