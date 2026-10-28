---
title: >-
    NaviSDK_Core 작업 이력 2025-05 ~ 2025-09
category: references
project: orbis-sdk
tags: [orbis-sdk, navisdk, android, kmp, bitbucket, commit-history, visibility/internal]
relationships:
  - target: "[[navisdk-core-commit-history]]"
    type: related_to
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[navisdk-confluence-sprint-timeline-2024-2026]]"
    type: related_to
sources:
  - repo:bitbucket/mobility-tech/navisdk_core
summary: >-
    navisdk_core(글로벌 내비게이션 SDK) 본인 커밋 343건(2025-05 ~ 2025-09)의 주제별 이력. 커밋 메시지 기준이며 diff는 검증하지 않았다.
provenance:
  extracted: 0.85
  inferred: 0.12
  ambiguous: 0.03
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-10-28
tier: supporting
created: 2026-10-28T10:00:00+09:00
updated: 2026-10-28T10:00:00+09:00
snapshots:
  - "[[_raw/_archived/Bitbucket_navisdk_core_커밋목록_dongeun|Bitbucket_navisdk_core_커밋목록_dongeun]]"
---

# NaviSDK_Core 작업 이력 2025-05 ~ 2025-09

본인이 작성한 `navisdk_core` 저장소(글로벌 내비게이션 SDK, 로컬 `global-inavi-navigation-sdk-android`) 커밋 343건(2025-05 ~ 2025-09)을 주제별로 묶은 이력이다. 전체 허브는 [[navisdk-core-commit-history]], 프로젝트 개요는 [[orbis-sdk]], 같은 기간 스프린트 연표는 [[navisdk-confluence-sprint-timeline-2024-2026]]을 본다.

> [!warning] 커밋 메시지 기준, diff 미검증
> 이 페이지는 커밋 메시지만 근거로 한 요약이다. 메시지와 실제 변경이 다를 수 있다. 주제 분류는 메시지 키워드와 이슈 키로 한 1차 분류라 경계 사례가 있고 ^[inferred], 대상을 알 수 없는 커밋은 따로 모았다 ^[ambiguous]. 각 항목의 해시로 `git show <해시>`를 실행해 확인한다. 동기와 효과는 메시지에 있는 것만 적었다. 서버 포트와 숨은 기능 진입 방법 등 보안 대상 값은 원본에서도 가렸다.

## 기간 개요

커밋 메시지상 2025-05~09 기간의 커밋은 총 343건이다. 월별로 05월 52건, 06월 48건, 07월 46건, 08월 67건, 09월 130건으로, 05~07월은 40건대 후반 수준이다가 08월 67건으로 늘고 09월에는 130건으로 가장 많다. 05~06월은 지도 버튼·TBT UI, MapLibre 기반 지도 제어와 TTS 모듈 관련 작업이 많고, 07~08월은 안전운전 View, aar 배포, 지도 제어 인터페이스·KDoc 문서화 관련 작업이 보인다. 09월에는 인증, 효과음, 에러 처리, 다중경로·경유지(NSDK-537/540/545) 관련 작업이 집중되어 있고 버전코드 갱신도 여러 번 있다.

## 1. 지도 렌더링·카메라·TrackingMode (MapLibre 기반 지도 제어) (51건)

- 기간: 2025-05~2025-09
- 이슈 키: [NSDK-450], [NSDK-455], [NSDK-458], [NSDK-460], [NSDK-464], [NSDK-468]

MapLibre 의존성 추가와 MapFragment 구현(2025-06)을 시작으로 지도 Controller, 마커·경로선 표출, CameraController(ZoomIn/ZoomOut), GestureController, TrackingMode(2D 고정/회전)와 Padding 변경, 최소 줌 조정, 마커 전체 삭제, 컴퍼스 View 적용 관련 작업이 있다. 주로 NSDK-450, 455, 458, 460, 464 키로 묶여 있다.

- `757a99da` (2025-06-12) NSDK-450 MapLibre를 들고있는 MapFragment 구현, 기존에 사용하던 TomTom API 주석 처리
- `0599e8cf` (2025-06-13) NSDK-450 Map 상호작용을 위해 Controller 구현, 테스트 로직 추가
- `7fd647c6` (2025-06-19) NSDK-450 지도 제스처 처리를 위해 GestureController 추가, PanningListener를 MapMoveListener로 변경
- `8568d01e` (2025-06-24) NSDK-455 2D 고정형 및 회전형을 구현하기 위해, TrackingMode 타입 추가. Config 값을 이용하여 View 및 Padding 설정
- `780ac444` (2025-06-24) NSDK-458 경로선택 및 전체경로 진입 시, 목적지로 애니메이션 없는 카메라 이동 진행
- `59522e7c` (2025-06-25) NSDK-460 마커 전체 삭제 기능 추가 및 지도에 표출중인 전체 요소 제거하는 기능 추가

## 2. Orbis 지도 스타일·지도 데이터 다운로드·국가/언어 분기 (33건)

- 기간: 2025-05~2025-09
- 이슈 키: [NSDK-436], [NSDK-481]

OrbisMap 적용, Orbis Street Light/Dark 스타일 추가(NSDK-436), 지도 데이터 다운로드 로직 변경(Index 파일 경로 사용), 지도 버전 정보 Json 전환, 2차 개선된 지도 Style 적용, 스타일 URL 변경, DataStore CurrentCountry 기반 분기, 앱별 언어 설정, 다운로드 Json 규격 대응(NSDK-481) 관련 작업이 있다.

- `68100eda` (2025-05-20) NSDK-436 Assets에 Orbis Street Light/Dark Style 추가, 해당 OrbisMap 적용
- `de79b1b0` (2025-05-26) OrbisMap 적용
- `d6218619` (2025-06-16) OrbisMap 지도 다운로드 로직 변경 (Index.txt의 경로 파일을 이용)
- `f651982c` (2025-08-27) 2차 개선된 지도 Style 적용
- `d56bf37c` (2025-08-21) [공통] DataStore CurrentCountry 값에 따라, 지도 Style, routeUrl, tomtom BaseUrl 등 분기 처리 진행
- `dfd436bd` (2025-07-25) NSDK-481 지도 다운로드 관련, 변경된 Json 규격 대응

## 3. TBT·지도 버튼 등 주행 UI 컴포넌트 (33건)

- 기간: 2025-05~2025-09
- 이슈 키: [NSDK-419], [NSDK-425]

다음/다다음 턴(TBT) View의 GUI 가이드 적용과 AppFlavor 기반 이미지 선택(NSDK-419), 지도 버튼 ButtonType·ViewModel·가시성 상태·볼륨/줌/현위치 버튼 구현(NSDK-425), 이미지 리소스 적용, 하단 메뉴 및 교통정보 토글 버튼 관련 작업이 있다.

- `134738da` (2025-05-12) NSDK-425 ButtonType 추가, Layout View 임시 추가
- `66dcd434` (2025-05-13) NSDK-425 현위치 이동 View 추가
- `9098e932` (2025-05-08) NSDK-419 Orbis TurnView, NextTurnView GUI 가이드 적용
- `d46265f4` (2025-05-08) NSDK-419 차차기용 Visible State 생성, UIMode 및 Distance조건 추가하여 Visible 변경하는 예시 추가
- `7609f117` (2025-05-09) OrbisRouteOption에 RouteColor 파라미터 추가 후 경로선택 화면은 초록색 경로선으로 표출되도록 변경 (ColorType Model 모듈로 …
- `106b026a` (2025-09-29) 교통정보 토글 버튼 추가 및 동작하도록 수정

## 4. TTS 음성 안내·음소거·AudioFocus (20건)

- 기간: 2025-05~2025-09
- 이슈 키: [NSDK-444], [NSDK-483], [NSDK-509], [NSDK-527], [NSDK-542]

TTS 서브 모듈 생성과 기본 동작 구현(NSDK-444), 발성 스크립트 테스트, AudioFocus 요청/해제(NSDK-483), 음소거 관련 ConfigKey와 TTS 발성 제한(NSDK-509), 재탐색/이탈 시 발성 로직과 직렬 실행(NSDK-527), 볼륨 버튼 이미지와 TTS Mute 조건(NSDK-542), 다국어 음성 템플릿 대응 관련 작업이 있다.

- `ae471151` (2025-05-29) NSDK-444 TTS 서브 모듈 생성, I/F 구현
- `45bf5ebb` (2025-05-29) NSDK-444 TTS 기본 동작 구현
- `1a2d9861` (2025-07-29) NSDK-483 tts 음성 발화 시 AudioFocus 요청 및 완료 시 해제 로직 추가
- `cc40c9b2` (2025-08-28) NSDK-509 볼륨버튼 효과음만 제거, 음소거 관련 ConfigKey 정의 및 세팅
- `fa77f480` (2025-09-09) NSDK-527 TTS 발성 로직 변경 (마지막 요청으로 계속 덮어쓰고, 직렬 실행 방식)
- `a9cf4ad2` (2025-09-22) NSDK-542 ButtonType 및 ConfigType 추가

## 5. 안전운전(카메라) View·심볼 표출 (13건)

- 기간: 2025-07~2025-07
- 이슈 키: [NSDK-471], [NSDK-480]

안전운전 GUI 구현과 SafeViewModel 연결(NSDK-471), CameraType별 심볼 이미지와 제한속도 이미지 처리, 이동식 카메라 심볼과 MapIcon, 수정된 GUI 가이드 적용(NSDK-480) 관련 작업이 2025-07에 집중되어 있다.

- `8fde599e` (2025-07-15) NSDK-471 안전운행 GUI 구현
- `e12fe77a` (2025-07-16) NSDK-471 CameraType에 따라 심볼 이미지를, 제한속도에 따라 속도 이미지를 가져오는 로직 추가
- `d10bc53c` (2025-07-16) NSDK-471 카메라가 신호 과속 타입인 경우, 속도 이미지에 Top Margin을 적용하는 로직 추가
- `e926db04` (2025-07-25) NSDK-480 이동식 카메라 관련 심볼 이미지 및 MapIcon 처리
- `9003a8c1` (2025-07-25) NSDK-480 안전 운행 View 수정된 GUI 가이드 적용
- `29c10f23` (2025-07-23) Speed View 아래 안전운행 View 표시하도록 변경

## 6. 지도 제어 공개 인터페이스·MapFragment 분리 (18건)

- 기간: 2025-08~2025-08
- 이슈 키: [NSDK-491], [NSDK-495]

NaviController 인터페이스 정리와 지도 제어 공개 인터페이스 생성, 주행용(InvMapFragment)과 일반 지도(MapFragment) 분리(NSDK-491), 지도 컨트롤 미구현 기능 추가와 불필요 API 제거(NSDK-495) 관련 작업이 2025-08에 있다.

- `e80ce5fa` (2025-08-11) NSDK-491 지도 제어 기능 공개용 인터페이스 생성, 기존 MapIF 에서 구현되었던 기능을 MapFragment 내부로 옮김
- `e2e51b7f` (2025-08-11) NSDK-491 Common용 MapFragment 생성, 각 플랫폼에서 MapController 인터페이스를 이용하여 구현체 구현
- `76810ac3` (2025-08-11) NSDK-491 MapFragment 분리 (주행용은 InvMapFragment, 일반 지도는 MapFragment)
- `2c45b3cc` (2025-08-11) NSDK-495 지도 컨트롤 미구현 기능 일부 추가 (MapIcon, ZoomToFit)
- `1e723f8b` (2025-08-12) NSDK-495 지도 컨트롤 미구현 기능 일부 추가 (Map level 및 제어 관련 기능 등 )
- `759eed36` (2025-08-13) NSDK-495 주행용 지도 컨트롤에 필요없는 API 제거

## 7. 공개 API KDoc 문서화 (9건)

- 기간: 2025-08~2025-08
- 이슈 키: [NSDK-489]

NaviController(Core 모듈)와 NaviUIController(UI 모듈)만 문서화되도록 하는 변경, 지도 컨트롤 인터페이스와 MapFragment의 KDoc 주석 추가, 노출 불필요 클래스 제거(NSDK-489) 관련 작업이 2025-08에 있다.

- `1e6cdcd3` (2025-08-21) NSDK-489 Navisdk Core 모듈은 NaviController만 문서화 되도록 변경
- `201f1b31` (2025-08-21) NSDK-489 Navisdk UI 모듈은 NaviUICOntroller만 문서화 되도록 변경 및 문서상 navisdk-aos-ui 모듈명이 이상하여 ui로 변경
- `9e47fb3a` (2025-08-19) NSDK-489 지도 컨트롤 인터페이스에 관한 kdoc 주석 설명 추가
- `b4759f99` (2025-08-14) NSDK-489 일반지도 (MapFragment)에 관한 주석 설명 추가
- `977c90c4` (2025-08-22) NSDK-489 NaviUIController 문서화 진행

## 8. 빌드·aar 배포·버전코드·샘플앱 설정 (38건)

- 기간: 2025-05~2025-09
- 이슈 키: [NSDK-466]

NSDK-466 키로 Model, Utils, TTS, OrbisRoute, MapMatch, Maps, Guidance, Core 모듈의 aar 배포 로직 추가 작업이 2025-07에 있다. 그 외 버전코드/버전 업데이트, 대만향/한국향 플래그 변경, 서브모듈 최신화, 샘플 앱 아이콘·명칭·APK 파일명, 앱 만료 로직 주석 처리 관련 작업이 있다.

- `7d74ebf7` (2025-07-09) NSDK-466 Model 모듈 aar 배포 로직 추가
- `a5b35e8f` (2025-07-10) NSDK-466 Guidance, Core aar 배포 로직 추가
- `197ae49d` (2025-07-10) NSDK-466 Maps, Maps Orbis aar 배포 로직 추가
- `64f47ce9` (2025-06-26) 버전 업데이트 ("0.0.1",  2)
- `8525a0a7` (2025-08-21) 한국지도 앱 발행 위한 버전코드 업데이트 (4 -> 5)
- `947de1c2` (2025-07-01) [AOS] Sample Apk 빌드 시, File Name 변경하도록 수정

## 9. 인증 및 TomTom 지오코딩 API 연동 (12건)

- 기간: 2025-09~2025-09
- 이슈 키: [NSDK-498], [NSDK-522]

Agent를 통한 Auth API 요청, IMPS 요청 로직 제거, 공용 인증키 변경, AccessToken을 Authorization Header로 사용(NSDK-522), TomTom Geocoding/ReverseGeocoding을 NaviSDK API로 처리(NSDK-498), 인증 요청 uniqueKey 설정 관련 작업이 2025-09에 있다. 키 값은 미수록.

- `35489ade` (2025-09-22) NSDK-522 Agent를 통하여 Auth API 요청하도록 변경 (IMPS 인증 및 JWT 토큰 생성)
- `e1b35d2b` (2025-09-22) NSDK-522 공용 인증키로 변경
- `3a626092` (2025-09-22) NSDK-522 응답받은 AccessToken 값을, Authorization Header 값으로 사용하도록 변경
- `eb60b362` (2025-09-22) NSDK-498 Tomtom Geocoding, NaviSDK API로 처리
- `de1bc382` (2025-09-23) NSDK-498 Tomtom ReverseGeocoding, NaviSDK API로 처리
- `ef1ffe46` (2025-09-25) 인증 요청 시, Android ID의 UUID 고유 값으로 세팅

## 10. 커스텀 팝업·에러 코드·실패 케이스 처리 (28건)

- 기간: 2025-08~2025-09
- 이슈 키: [NSDK-513], [NSDK-515], [NSDK-516]

커스텀 팝업 GUI와 Builder 형태 표출(NSDK-513), 경로선택 에러 팝업(NSDK-515), 초기 권한·인증·지도 다운로드·ServiceGate 파싱 등 초기화 실패 케이스 처리(NSDK-516), 공통 에러 코드 정의 관련 작업이 2025-08~09에 있다.

- `08ba6ae6` (2025-08-28) NSDK-513 커스텀 팝업 GUI 구현
- `d65c8df7` (2025-08-28) NSDK-513 Builder 형태로 팝업 표출 할 수 있도록 구현
- `11f570d2` (2025-08-28) NSDK-515 경로선택 화면에서 에러 응답 시 팝업 표출 로직 구현, 에러는 하드코딩 값을 사용
- `3fda2d3e` (2025-08-29) NSDK-516 초기 권한 요청 관련 실패 케이스 처리
- `a52589b6` (2025-08-29) NSDK-516 SDK Auth 인증 요청 관련 실패 케이스 처리
- `6594c572` (2025-08-27) [공통] 실패 ErrorCode 정의

## 11. 효과음(SoundPool)·카메라 과속 효과음 (11건)

- 기간: 2025-09~2025-09
- 이슈 키: [NSDK-524], [NSDK-526]

공용 오디오 I/F 추가(NSDK-524), SoundPool 기반 효과음 임시 구현과 Wave 파일 추가, 효과음 발성 조건 추가, 카메라 효과음과 과속 효과음 UseCase 및 안전운행 종료 효과음(NSDK-526) 관련 작업이 2025-09 초에 있다.

- `28d1dfeb` (2025-09-04) NSDK-524 SoundPool을 이용한 효과음 발성 로직 임시 구현
- `72c18df1` (2025-09-04) NSDK-524 Wave 파일 일부 추가,  AudioService 초기화 진행 시 정의된 효과음 전체 로드하도록 변경
- `6d99f401` (2025-09-04) NSDK-526 카메라 효과음 관련 Usecase 추가, 과속인 경우 과속 효과음 발성
- `83f74d31` (2025-09-05) NSDK-526 지난 카메라 조건 체크 후, 안전운행 종료 효과음 발성
- `7d6a1db2` (2025-09-04) NSDK-524 효과음 발성 조건 추가
- `d7c909a9` (2025-09-03) NSDK-524 공용 오디오 I/F 추가

## 12. 경로 선택·다중경로·경유지·전체경로 (44건)

- 기간: 2025-08~2025-09
- 이슈 키: [AIR-536], [NSDK-536], [NSDK-537], [NSDK-540], [NSDK-545]

경로 선택 화면의 중첩 RecyclerView 구조(NSDK-537), 다중경로 API 연동과 UI 표출(NSDK-540), 경유지 요청 로직과 GUI 가이드 적용(NSDK-545), 백그라운드/포그라운드 진입 타이밍 수정(NSDK-536) 관련 작업이 있다. 2025-09 하순에 집중된다.

- `4bf957d2` (2025-09-16) NSDK-537 경로 선택 화면 다중 경로 표출을 위하여 중첩 RecyclerView 구조로 변경
- `4bfabfe0` (2025-09-15) NSDK-536 loadKoinModule을 통해 의존성 모듈 추가 시, 백그라운드에서 포그라운드 진입 시 타이밍 이슈 존재하여 수정
- `ec9a6308` (2025-09-23) NSDK-540 다중경로 API 연동
- `d380024e` (2025-09-24) NSDK-540 List 형태로 전달받은 다중 경로 데이터 UI 에 표출
- `cb42505d` (2025-09-30) NSDK-545 경유지 요청 로직 추가
- `9fd83ad5` (2025-09-30) NSDK-545 GUI 가이드 적용

## 13. 주행 안내 로직·화면 동작·기타 안정화 (28건)

- 기간: 2025-05~2025-09
- 이슈 키: [NSDK-473], [NSDK-527], [NSDK-531], [NSDK-534]

MMC 엔진 업데이트와 속도 갱신 수정(NSDK-473), ETA 표시 모드와 경로취소 팝업(NSDK-531), 속도별 지도 레벨 조정(NSDK-534), 화면 방향 고정·꺼짐 방지·ConfigChanges 같은 화면 동작, 위치 권한 관련 비정상 종료 수정, 개발자 모드·다크모드 수정 등 개별 안정화 작업이 있다.

- `bb960a7f` (2025-09-18) NSDK-473 MMC Engine update (0.5.5)
- `8b1753df` (2025-09-18) NSDK-473 속도 값 갱신 안되는 이슈로, CurrentPosition 업데이트 시 gpsStatus 판단 로직 제거
- `023e40ae` (2025-09-11) NSDK-531 EtaDisplayMode 모드를 추가하여 도착예정 시간을 해당 모드에 맞게 계산 할 수 있도록 변경
- `2e23129a` (2025-09-11) NSDK-534 주행 지도 레벨 조정 (구글 기반)
- `6cb1168c` (2025-09-11) NSDK-531 경로취소 버튼 클릭 시 팝업 추가
- `d69e4427` (2025-08-21) 화면 회전 시 액티비티 재 생성되는 문제로 인해, 모든 화면에 ConfigChanges 속성 추가

## 모호한 커밋 (5건)

대상을 알 수 없는 메시지(빌드에러 수정, 테스트 로직 제거, 임시 Push 등)이다. 이슈 키는 NSDK-537 한 건만 있고 내용은 "임시 Push"뿐이다.

- `88924f01` (2025-05-14) 빌드에러 수정
- `611e3e74` (2025-05-15) 필요없는 Test 로직 제거
- `68ac8d49` (2025-08-13) 테스트 로직 제거
- `ed10c1b2` (2025-09-18) NSDK-537 임시 Push
- `79901256` (2025-09-22) Unreachable code 에러 수정

## 검산

검산: 주제별 건수 합 = 전체 건수 : 51 + 33 + 33 + 20 + 13 + 18 + 9 + 38 + 12 + 28 + 11 + 44 + 28 + 5 = 343 = 343

## Sources

- 원본 커밋 목록: [[_raw/_archived/Bitbucket_navisdk_core_커밋목록_dongeun]] (해시|날짜|메시지)
- 저장소: Bitbucket `mobility-tech/navisdk_core`, 필터 `--author` 본인, merge·stash 제외
