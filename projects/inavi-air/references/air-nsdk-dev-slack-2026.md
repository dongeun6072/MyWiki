---
title: >-
    Slack #001_air_nsdk_dev 개발 대화 (2026)
category: references
project: inavi-air
tags: [inavi-air, slack, navisdk, orbis-map, visibility/internal]
aliases: [에어 NSDK 개발 채널 2026, 001_air_nsdk_dev 2026, Global Navi SDK 채널 2026]
relationships:
  - target: "[[air-nsdk-dev-slack-2025]]"
    type: extends
  - target: "[[inavi-air]]"
    type: related_to
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[air-operations-2026]]"
    type: related_to
sources: ["slack:#001_air_nsdk_dev"]
summary: >-
    에어·NSDK 개발 채널 2026년(1~10월) 정리. Global Navi/Maps SDK 1.0.x 공개 배포, 업체 통합 이슈의 원인과 해결, 국내 NaviSDK 2.0.x·Flutter, AIR 행정구역 개편·고속도로 목적지 팝업·후면카메라·친환경/수소, SDK 비중 축소.
provenance:
  extracted: 0.84
  inferred: 0.13
  ambiguous: 0.03
base_confidence: 0.45
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T16:30:00+09:00
updated: 2026-10-26T18:00:00+09:00
---

# Slack #001_air_nsdk_dev 개발 대화 (2026)

에어·NSDK 앱 개발자 비공개 채널의 2026년 1월~10월 기록이다. 프로젝트 개요는 [[inavi-air]], 앞선 기록은 [[air-nsdk-dev-slack-2025]]를 본다. 상반기에는 대만향(Orbis) Navigation SDK와 Maps SDK를 공개 배포하고 업체 통합을 지원하는 일이 많았고, 7월부터 SDK 업무 비중을 줄이고 신규 사업 쪽으로 무게를 옮겼다. SDK 쪽 상세는 [[orbis-sdk]], [[orbis-taiwan-development-2026]], [[map-sdk-commercialization-scrums-2026]], [[sdk-flutter-scrums-2026]]를, 같은 해 AIR 운영은 [[air-operations-2026]], [[air-app-version-notes-2026]]를 함께 본다.

1~10월 채널 메시지는 약 210건이고, 답글이 달린 스레드 147개를 모두 열어 내용을 반영했다.

## 조직·방향

- **준상용 서버(1월)**: Orbis SDK가 쓰던 개발서버 대신 준상용 서버를 구축하면서 Agent 도메인이 바뀌어 SDK 1.0.1과 샘플앱을 다시 냈다. 부문 회의에서 해외향 인증서버도 새로 만들기로 했다(01-22). MMC 측이 준상용 서버로 테스트할 수 있도록 Android 테스트 프로젝트와 TestFlight 배포를 지원했다(02-02).
- **Flutter 로드맵(01-23)**: 현 구조에서 플러그인 형태로 상반기에 먼저 제공하고, 이후 리팩토링하는 로드맵이 전사 보고에 올라갔다. 4월 말에는 국내 Navi/Map SDK뿐 아니라 해외향 Navi/Map SDK도 Flutter 대응이 필요해졌고, 티맵 수준의 Flutter 지원·가이드를 목표로 했다. 1단계는 네이티브 SDK의 View와 기능 전체(지도 + TBT·차로 안내 View)를 하나의 Dart 뷰로 감싼 플러그인이고, 최종 구조는 지도 렌더링만 네이티브에 두고 안내 View는 Dart 위젯으로 제공하는 것이다. 어느 단계든 외부 개발자는 Dart만으로 쓴다(04-29). 플러그인 패키지 이름 후보로 `inavi_navisdk_flutter_plugin`, `inavi_navisdk_plugin`, `inavi_navigation_plugin`이 나왔다(04-01). 개인 DM으로 들어온 Orbis 문의는 Orbis 공식 채널로 받아 정리해 답하기로 했다(04-08). SDK Flutter 대응 첫 스프린트는 5월 6일 시작했다.
- **SDK 비중 축소(07-14~15)**: 7월부터 국내·해외 SDK 업무 비중을 낮추고 신규 사업 비중을 높인다. 근무 기록(PAMS)에도 SDK 비중을 낮춰 입력한다. SDK 스프린트는 끝내고 AIR처럼 타임라인으로 관리하며, 스크럼 유지 여부는 상황을 보고 정한다.
- **호주향 R&D(06-04)**: 산업부·KIAT 국제공동기술개발 과제 "호주 도로환경 대응 ADAS 연계형 온·오프라인 하이브리드 3D 내비게이션 SW"(TomTom 수요기업, 2026.08~2029.07, 약 42.8억 원)에 회사가 주관기관으로 참여했다. 1차년도는 호주 인프라 분석과 하이브리드 내비 구조·ETA Routing·TbT 설계, 2차년도는 3D DP 엔진(타일링, LOD/Culling)과 핵심 모듈, 3차년도는 안정성과 TomTom 호주 고정밀 지도 기반 검증, 4차년도는 현지 실증이 계획이었다. 선정 평가는 6월 10일이었고, 6월 9일에는 오토모티브 쪽에서 맡을 수도 있다는 언급이 있었다. ^[ambiguous]
- **도구·AI**: 이동은이 Claude Code용 PR 생성 스킬과 Bitbucket MCP 설정 방법을 공유했다(인증 정보는 각자 로컬 환경 변수로 관리, 03-27). 4월에는 NaviSDK 기준 업무 가시화 지표 PDF, 6월에는 AIR API 명세를 Markdown으로 정리한 문서가 공유됐다. 7월에는 SKT 기반 KMP 앱 템플릿 저장소, AX 문서 초안, 자체 AI 챗봇용 LLM 활용 회의(07-01)가 있었다. 회의 요약에 따르면 데모는 배송관리 앱의 버튼 기능을 자연어 챗봇으로 바꾼 것으로, 시스템이 미리 계산한 후보 중에서 LLM이 고르기만 하고(사내 OpenAI 호환 API의 약 23B 모델), LLM 역할을 툴 판단과 답변 문구 생성으로 줄이고 도메인 키워드로 툴 목록을 미리 걸러 토큰을 줄이는 구조였다. 같은 달 공유된 SMR 엔진 다운로드 구조 문서는 공용 위키로 관리하자는 의견이 나왔다. 10월에는 선행 조직이 운영하는 데이터레이크에 제품 로그를 싣는 방향이 공유됐다(10-22).
- **기타**: mapsplatform(iMPS) 사이트와 PAMS가 판교 사무실에서 접속되지 않는 문제를 확인했다(01-08). 2월에는 SK이노베이션에 제안한 NaviSDK 와이어프레임 자료를 내부에만 공유했다.

## Global(대만향) Navigation SDK

- **1.0.0 공개(1월)**: Android/iOS Demo 저장소를 공개 GitHub에 만들고 CHANGELOG를 관리한다(01-07). 외부 명칭은 `Global iNavi Navigation SDK`이고 Demo README는 iMPS 문서로 안내한다. iOS SDK 1.0.0을 공식 GitHub에 1차 배포하고 DocC API 문서를 올렸다(01-08). SDK 문서는 iOS 가이드를 추가하고 Demo·API 문서·ChangeLog 링크를 연결해 HTML로 변환해 넘겼다(01-15). CHANGELOG의 최초 배포일은 Android·iOS 모두 2026-01-15로 맞췄다. iOS Demo 작업 중 지도 padding이 AOS와 다른 점이 확인되어 맞춘 뒤 Demo를 마무리했다(01-14). 사업부 담당자를 TestFlight에 초대하면서 이전 빌드에 없던 `1.0.0(1)` 한국어 버전도 함께 열었다(01-20). 01-23에는 Swagger로 인증 API를 부를 때 한쪽 환경에서만 실패하고 다른 API도 access denied가 났다. 다른 API는 Bearer 토큰을 넣지 않은 탓으로 보았고, 토큰을 Authorize에 넣자 TomTomKey API는 정상 응답했다. ^[ambiguous]
- **1.0.1(01-29)**: Android는 JFrog, iOS는 SPM으로 배포했다. ChangeLog는 "Map Data Update, Safety improvements". 신규 지도 `v25270` 적용 전 기존 SDK에 대만·한국 지도를 바꿔 모의주행·로그주행을 해 보니 문제가 없었다(01-23). 샘플앱 U-Map은 Android `1.0.1 (25)`(AppTester), iOS `1.0.1 (3)`으로 냈다가 키 변경이 반영되지 않아 `1.0.1 (5)`로 다시 배포했다(TestFlight). 사업부 계정도 배포 대상에 넣는다. 새 Orbis Admin에서 확인해 보니 업체 키는 그대로이고 개발 키만 바뀌었다(접속 정보는 원본에 있음, 미수록).
- **1.0.2(03-25)**: 차량 제원(vehicle specifications) 옵션을 추가했다(AOS aar, iOS xcframework). Android는 JFrog·ChangeLog·API 레퍼런스까지 올렸다.
- **1.0.3~1.0.4(5~9월)**: 5월 말 Hetone 3999 문의에 1.0.3 사용을 안내했고, Demo의 의존성도 1.0.3으로 명시했다. U-Map은 최신 탐색엔진 테스트용으로 Android `1.0.3 (27)`, iOS `1.0.3 (8)`을 냈다(06-02). 같은 날 사업부 담당자의 iOS U-Map 베타가 만료되어 기존 빌드 `1.0.1 (7)`을 다시 열어 주었다(69일 남음). 그 전에 전시회 영상용으로 검색(초기 화면→검색→결과), 안내 시작(결과→경로 선택→안내), 주행(TBT·안전운행 표출)을 단계별로 영어 화면 녹화와 스크린샷으로 만들어 넘겼다(05-18~19). 9월 8일에는 SDK 1.0.4를 넣은 Android `1.0.4 (28)`, iOS `1.0.3 (9)`를 사업부 테스터까지 배포했고, 타임락을 12월까지로 잡아 10월 ITS 전시회 기간에 쓸 수 있게 했다.
- **지도 엔진 매칭(04-17)**: SDK v1.0.1 = OrbisRouteDataLib 1.0.1.3, 1.0.1.4는 미배포, v1.0.2 = 1.0.1.5(1.0.1.4 속도 개선판).
- **OrbisRouteDataLib 성능(2~3월)**: 1.0.1.4는 서버 반영 전까지 그대로 쓰면 주행이 안 돼 3월 탐색 포트 분기 이후 적용하기로 했다(02-09). 3월 U-Map 테스트에서 탐색 응답은 즉시 오는데 경로 표출이 늦었다. 앱은 탐색 후 경로 전체를 돌며 `GetDataLink`를 부르는데, 1회 호출이 0.001초에서 약 0.2초로 늘었다(401개 링크 기준 평균 91.62ms, 첫 호출 408ms, 같은 링크 재호출 27ms). iOS에서는 같은 현상이 없어 JNI 쪽을 의심했고, 1.0.1.41에서도 같았다. 이어 안전운행 카메라 3,040개 프로젝션을 비교하니 `GetDataLinkNearPt` 총 소요가 1.0.1.3 약 10초, 1.0.1.4 약 6분이었고, 프로젝션이 끝나기 전에 탐색하면 문제가 났다. 원인은 로컬 라이브러리의 `GetDataLinkNearPt` 링크 검색 반경이 의도치 않게 500m에서 15km(서버 기준값)로 바뀐 것이었고, 로컬 반경을 되돌린 `1.0.1.43`에서 고정식 카메라 프로젝션이 약 16초에서 15초로 줄어 정식 배포를 요청했다(03-24). 5월 `1.0.1.6`은 Agent에만 먼저 적용되어 MMC도 같은 버전으로 다시 받아야 모의주행이 맞았다. 6월 대만 새 지도 `26220` 적용에는 문제가 없었고, Agent의 `mapver`를 라이브러리 버전 대신 실제 데이터 버전으로 고쳤다. SDK는 문자열 비교로 업데이트 여부를 판단한다. 상세는 [[orbis-route-data-lib]].
- **MMC**: `orbis-mapmatch 0.6.6.101/103`에서 모의주행이 경로를 벗어나는 문제는 탐색엔진이 아직 1.0.1.6을 적용하지 않은 탓으로 보고 5월 19일 이후 다시 보기로 했다(05-15). 국내 iOS NaviSDK 엔진(DP, MMC, Guidance)은 시뮬레이터 arm64를 지원해야 하며 xcframework로 받는 방안을 권했다(05-12). 5월 말 DP까지 적용해 시뮬레이터 실행을 확인했다.
- **SpeedCamera 캐싱(09-14)**: 지도 버전 기준으로 캐싱하고, 지도 버전이 바뀌면 갱신한다.
- **실차 후속**: 대만 실차에서 나온 "턴 구간 지도 확대 필요"를 다시 점검했지만 커밋 내역상 개선된 것은 없었다(02-11).

### 대만 업체 통합 지원

- **Hetone(흐통)**
  - `consumer-rules.pro`(05-15): SDK 모든 모듈에 들어 있어 AAR에 자동 포함되고, minify를 켜면 SDK keep 규칙이 자동 적용된다. 주요 keep 패키지는 Maps, utils, mapmatch, orbisroute, guidance model, media sound/tts다.
  - 5월 20일 문의: Android Core는 NDK `arm64-v8a`, `armeabi-v7a`만 빌드하고, iOS x86_64도 지원하지 않는다. 런타임 `setAppKey` API는 없고 AppKey는 AndroidManifest meta-data에서 읽으므로 키가 바뀌면 다시 빌드해야 한다. 초기화 직후 `1007`은 인증 요청의 AppKey가 비었을 때, `runRoute` 즉시 `1999`는 초기화가 끝나지 않았을 때 나는 오류다.
  - 데모앱 경로 요청 `3999`(06-01~04): 1.0.3 적용 후에도 같았고(iOS는 SPM에서 의존성만 바꾸고 Update to Latest Package를 하지 않으면 이전 버전이 남을 수 있음), Agent 로그를 보니 타이베이 특정 출발지에서 도로 확장에 실패한 것이어서 탐색엔진에 문의했다.
  - Navi + Maps SDK 동시 사용(05-25): Android는 두 SDK가 패키지 구조까지 난독화해 `a.a` 같은 같은 이름의 클래스가 생겨 `checkDebugDuplicateClasses`가 실패했다. 두 SDK 모두 `repackageclasses`로 난독화 클래스를 각자 패키지 아래에 두도록 고치기로 했다. iOS는 Navi SDK가 MapLibre를 로컬로 묶어 배포해 SPM 타깃 이름 `MapLibre`가 `maplibre-gl-native-distribution`과 겹쳤다. Maps SDK처럼 MapLibre를 의존성으로 받는 구조로 바꾸면 해결된다.
- **JustXtar(대만 파트너)**: 파트너사 회사명 검색 결과가 없다는 문의(03-30)는 TomTom Fuzzy/POI Search 모두에서 해당 POI가 없었고(Genesis·Orbis 동일, 비슷한 다른 회사만 나옴) TomTom 문의 대상으로 정리됐다. 4월에 전 TomTom 대만 지사장과 파트너 CEO에게 U-Map을 배포했다(TestFlight 빌드는 최대 90일, 연락처 미수록). 7월 6일 JustXtar의 Flutter SDK 테스트 여부를 묻자 Agent에서는 OS만 구분돼 확인할 수 없었고, 요청 헤더에 `framework_type`(기본 `native`, 플러그인은 `flutter`)을 추가하기로 했다. 이동은이 Navi SDK Core와 Global Maps(Android) 작업을 마쳤다.
- **EC912(대만)**: 트럭 경로를 쓰는 회사로, 5월에는 Android/iOS가 아닌 ARM 임베디드 기기 지원을 물었다. SDK는 Android 32/64bit ARM, iOS 기기 ARM, Apple Silicon 시뮬레이터 ARM을 지원하며, 별도 임베디드라면 Core를 linuxArm64로 빌드하는 것까지는 검토할 수 있어도 MapLibre·UI·KMP 모바일 라이브러리 때문에 사실상 불가능하다고 봤다(05-20). 7월에는 국내 업체(모비딕) 테스트 단말에 대만향 Navi SDK 서드파티 데모를 포팅해 보냈다. 스펙 검토 결과 SDK 구동과 지도 렌더링은 문제없지만, GMS 미인증 펌웨어면 TTS 엔진이 없어 음성이 나오지 않을 수 있고, eMMC 16GB 용량, Wi-Fi(b/g/n, 최대 150Mbps), Cortex-A55 쿼드 성능, 원래 국내 지도 기준이던 저장공간 산정을 다시 봐야 했다. 실제 단말에는 `com.google.android.tts`가 있어 Locale 설정 후 앱을 재시작하자 en-US, zh-TW 음성이 나왔다(07-22).
- 기타: 검색 추천어 API는 따로 검토한 적이 없었다. TomTom `Search API Autocomplete`는 카테고리·브랜드 추출용이라 맞지 않고, Fuzzy Search의 `typeahead`는 이미 켜져 있었다(08-10). 웹에서도 TomTom Search/Geocode/R-Geocode가 필요해 자사 API로 감싸기로 했다(05-14). SDK가 쓰는 TomTom API는 Fuzzy Search(ServiceGate `SearchType`에 따라 Genesis/Orbis), Geocode·Reverse Geocode(공개 API), 고정·이동식 Speed Camera(SDK 내부)이고, POI/Category/Nearby Search는 정의만 있고 쓰지 않는다. 키 값은 원본에 있음(미수록). Agent의 TomTom 관련 API 경로(`/api/tomtom/...` safety-camera, search category/fuzzy/genesis/geocode/reverse-geocode/nearby/poi)는 모두 TomTom을 직접 호출하고, 인증·ServiceGate·탐색 API는 TomTom을 부르지 않는다(04-01). TomTom 가격 정책 논의(06-25)에서 Search·Geocoding·Reverse Geocoding은 Non-Tile, Speed Camera는 정보 없음(Non-Tile 추정), Traffic Flow/Incidents는 SDK에서 쓰지 않아 교통정보 담당 확인이 필요하다고 답했다. 우리 Maps가 그리는 지도는 Genesis가 아니라 Orbis 데이터다(06-04). 상세는 [[genesis-vs-orbis-search-api-review-taiwan]].

### TomTom ANA·모트렉스 H/U

- 2월 모트렉스 H/U(TomTom ClientSDK 기반 NaviService 앱)에서 언어를 바꿔도 주소가 바뀐 언어로 갱신되지 않았다. 시스템 LocationManagerService가 GPS의 (0,0) 좌표를 차단해 `onCurrentPosition`의 좌표가 `null`로 들어왔고, 기존 로직은 좌표가 없으면 리버스 지오코딩과 ContentProvider 갱신을 건너뛰었다. 좌표가 없어도 DataStore의 이전 위치로 지오코딩해 언어 변경 같은 강제 갱신 때 주소를 보내도록 M/W를 고쳤다. 목적지가 설정된 상태에서 메인카드에 목적지 주소가 반영되지 않는 것은 모트렉스 메인카드 표출 사양으로 판단했고, 2월 23일 NaviService 앱을 발행했다.
- 3월에는 H/U 네트워크 설정이 다시 동작하지 않았다. 시간 설정은 H/U 일반 설정에서 GPS 시간 적용을 끄면 Android `date` 명령이 먹었고, ping은 Wi-Fi 연결 때만 응답했다. 설정 절차는 원본에 있음(미수록).

## Global Maps SDK (U-Atlas)

- **설계(1월)**: Orbis Maps SDK는 MapLibre를 fork하지 않고 의존성(implementation)으로 넣기로 했다(01-15). 그러면 MapLibre 패키지가 외부에 그대로 노출되어 업체가 MapLibre API를 직접 부를 수 있다는 점이 지적됐다. 구현 항목은 지도, 컨트롤, 카메라, 사용자 위치, 마커, 정보창, 도형, 클러스터링, 경로, 이벤트이고, 내부 구조는 Google Maps API를 기준으로 했다. 이동은이 Google Maps SDK 구조를 클래스 다이어그램으로 정리하고(접두어만 바꿈) README 초안과 인증 구현 프로젝트를 만들었다. 클래스 접두어는 `IGMService`, `IgmShape`, `IgmMarker`, `IgmMapView` 등으로 정했고, `IgmMapView`는 카메라·줌·피치·제스처·나침반·축척 바 속성을 XML로 받는다. 인증은 기존 국내향 인증 규격서를 참고했다.
- **문서·데모(2~4월)**: 3월부터 Orbis 디자인 작업을 하기로 디자인 쪽과 이야기가 되어, NaviSDK·MapSDK 가이드 문서에 필요한 이미지를 정리했다(02-19). 도보 탐색 Postman 샘플도 공유받았다(02-23, 링크 미수록). Maps SDK 연동 가이드는 한글로 쓴 뒤 ChatGPT로 번역했다(예시 이미지 교체, API 레퍼런스 연동, Demo·ChangeLog 바로가기, 해외 좌표로 변경). 3월 11일 Maps 문서와 Navigation SDK 문서(해상도 개선 이미지)를 HTML로 빌드했다. iOS Maps SDK는 레퍼런스(DocC), Demo, SPM 저장소를 공개 GitHub에 두었다. 데모앱 이름은 U-Map에 맞춰 U-Atlas로 정하고 아이콘을 바꿔 AppTester·원격 저장소에 다시 배포했다(03-31, 04-03). 대표 보고용 화면은 데모앱으로 디자이너가 직접 캡처했다. 26년 1분기 MapsSDK 서비스 목표의 산출물이다. 상세는 [[map-sdk-commercialization-scrums-2026]].
- **지도 언어·스타일(4~5월)**: Android `IgmMapLanguage`는 `EN`, `ZH`, `AUTO`(기기 언어, 지원하지 않으면 `ZH`)이고 `IgmMapOptions.mapLanguage`의 기본값은 `AUTO`다. iOS는 enum에 하이픈을 쓸 수 없어 `zhTw` 형태로 하고, 주석은 "Traditional Chinese"로 맞췄다. 스타일의 `metadata.language`를 보고 심볼 레이어의 `text-field`/`text-font`를 바꾼다. iOS `IgmMapStyleMode`(`light`/`dark`)는 인증 응답의 light/dark 스타일 URL을 쓰고, dark URL이 없으면 light로 돌아가며 시스템 다크 모드와 연동하지 않는다. 웹 기본 언어는 번체로 안내했고, 글로벌 스타일 운영 시 기본을 영어로 두는 구조를 제안했다(04-10).
- **삼성생명 PoC·Location SDK(3~10월)**: 도형으로 경로 만들기(자유 그리기, 다중 코스 최대 3개, 그린 그림과 코스의 정합성 70%, 거리·시간 표시, GPX 다운로드) 일정은 초안 21일에서 UI·GPX 생성 등을 넣어 40일로 늘었다(03-11). 지도 방위를 도형에 맞추는 것은 당시 불가능했고 고도 정보는 빠졌다. GPX는 다른 앱(오르다)이 쓰는 jpx 라이브러리를 참고했다. 4월에 이동은이 Global Navigation SDK 흐름도를 만들었고, 5월에 Location SDK 저장소가 생겼다. 활동 인식에서 `STILL` 판정이 Confidence 33으로 들어와 60 미만 무시 규칙에 걸리는 것도 확인했다(04-23). 6월 25일 작업분 가이드를 갱신해 배포했다. 10월에는 고객사 요구(Android Kotlin 2.0.0, AGP 8.7.1)로 Kotlin을 2.0.0으로 내린 브랜치에서 iOS 빌드가 깨졌다. coroutines 1.10.2, Room 2.7.2/sqlite 2.5.2가 Kotlin 2.1 이상으로 빌드되어 Kotlin/Native 2.0.0이 읽지 못했기 때문이다(Room은 Kotlin 2.0 빌드 정식판이 없음). Android만 2.0.0으로 내리고 iOS는 2.3.20을 유지하는 쪽이 권장됐고, 우선 AOS만 테스트해 배포하자는 의견이었다(10-16).

## 국내 NaviSDK·고객사

- **버전**: iOS NaviSDK `v1.0.10`과 삼성중공업용 Android SDK에서 4톤 초과 차량 과속 기준을 바꿨다(03-17). 4톤 초과는 25km/h부터, 4톤 이하는 기존대로 30/35km/h 기준이다. 과속 판단은 초기데이터의 `spd_lmt.txt`(mapid·linkid 구간)로 하므로 데이터(atl.zip) 재발행이 필요했고, 음성 "전 야드 25km 운행 구역입니다"도 새로 받아야 해 SDK를 다시 냈다. 기존 20km 음성은 남겨 두었다. 같은 날 야드 지점 명칭(출발·도착 코드)을 이름으로 넘겨 화물차 옵션(`truck1`·`truck2`) 다중 경로를 요청해 보니 두 경로 모두 정상으로 왔다(03-17). 이전 SDK에 새 데이터가 들어가면 Android는 경고 화면만 나오고 음성은 없으며, iOS는 30km 음성이 나온다. 삼성중공업 Android 버전은 `1.10.0` 다음을 `1.2.0`으로 냈다가 숫자 비교상 낮아져 `1.20.0`으로 다시 발행했고, 이후 `1.21.0`~`1.30.0` 형식으로 올린다. 9월 말에는 삼성중공업 추가 요청(제한 구역 진입 로그는 중량 제한 `getTFlimitInfo` API로 전체 진입 불가 처리, 전용 음성 "운행금지 시간", "일단 정지 교차로", "최근 중대 재해 발생 구역", 빨간색 경고는 SDK 수정 필요)을 검토했다.
- **국내 Android SDK 2.0.x(7월)**: 다음 버전을 `0.9.1`과 `2.0.0` 중 삼성중공업 SDK보다 높은 `2.0.0`으로 정했다(07-15, 직전 `0.9.0`). iOS CocoaPods는 2.0.0 podspec에 시뮬레이터 지원 스펙이 남아 있었고 trunk podspec은 다시 올릴 수 없어 `2.0.1`로 올렸다. 7월 24일 고객사에서 `INaviEngine` ANR이 여러 단말에서 났다. 2.0.0에서 메인 스레드 블로킹을 없애려고 초기화를 HandlerThread 비동기로 바꿨는데, 중복 초기화를 막는 보호가 없어 Activity 생명주기에서 두 번 불린 초기화 파이프라인과 내부 worker(초기화·SMR·MMC)가 동시에 돌았다. 고객사 메인 스레드 호출, 경로 제어 스레드, SDK 음성 스레드가 겹치며 이중 monitor 구조에서 deadlock이 났다. 모든 호출을 단일 동기화 경로로 바꾼 `2.0.1`을 발행했다.
- **문서 이전(4월)**: 가이드 페이지가 커져 PDF 추출이 실패했다. 해외향 Navi/Maps SDK는 Markdown을 Bitbucket에서 관리하고 mkdocs로 HTML을 만든다. 국내향은 Confluence에서 Markdown으로 옮겨 기존 Android/iOS 데모 GitHub 저장소에서 관리하고, VitePress로 GitHub Pages를 만들어 main에 push하면 자동 갱신된다(`/docs/index.md`만 고치면 됨). 고객사에는 페이지 링크나 인쇄한 PDF로 준다. Android 샘플도 최신화했고, 이사 보고와 사업부 공유까지 마쳤다(04-24~30). `setMapStyle`이 deprecated됐는데 예시와 API 문서가 현행화되지 않아 국내향·삼성중공업 문서를 고치도록 했다(04-03). 이 함수는 DP 엔진의 Mapbox 로직을 쓰는데 DP 1.2.0에서 호출하면 오류가 나고, AIR는 `mapboxType: 0`으로 하드코딩해 일반 지도만 써서 DP에서 Mapbox 로직을 빼도 문제가 없다고 봤다(iOS는 해당 인터페이스 없음, 03-05~12).
- **안내 음성 끝 음절 잘림(03-06~11)**: 고객사 단말(폴드7, S25 Edge, 퀀텀3)에서 "길 안내를 시작합니다"의 마지막 한두 음절이 잘렸다. 음성 재생이 `AudioTrack.write()` 직후 실제 출력 완료를 기다리지 않고 바로 `stop()`/`release()`하고 있었다. `OnPlaybackPositionUpdateListener`와 마지막 프레임 Marker, `WRITE_BLOCKING` 쓰기, CountDownLatch 대기로 바꿔 해결했고, 오래된 로직이라 저사양·고사양 단말을 시험한 뒤 AIR와 SDK에 함께 넣기로 했다.
- **Flutter 플러그인**: 국내향 Navi SDK Flutter 플러그인 가이드와 배포 준비는 7월 초 끝났고, 네이티브 SDK 배포 후 최종 테스트를 거쳐 pub.dev에 README 형태로 낸다(가이드는 Android, iOS, Flutter 3종). 해외향 플러그인은 5월 22일 pub.dev에 올렸고 해외향 문서에 Flutter 탭(A안)을 추가했다. iOS 국내 SDK의 Flutter 데이터 스트림(`DriveGuidePayload`)에는 진척률, 경로 상세, VMS, 도착 정보 등이 아직 nil이라 Android와 구조를 맞춰야 했다(06-10). 이를 위해 플러그인 작업 브랜치(`feature/dev_sdk_module`, AOS SDK는 로컬 모듈 참조)에 iOS 동등성 마일스톤(M5) 계획과 `DriveGuidePayload`→채널 Map 직렬화 키·타입 계약 문서를 두고, iOS SDK도 같은 방식으로 붙였다(06-11).
- **오믈렛(Flutter)**
  - 백그라운드 TBT 미표출(02-13~24): 영상을 보니 모의주행 상태였다. 백그라운드 TBT는 AIR와 같이 모의주행에서 제공하지 않으며, 실제 주행에서는 정상 표출됐다. 가이드에 이 내용을 추가했다.
  - 하단바 텍스트 미표출(04-10~15, SDK `0.8.1`): 앱 강제 종료 후 높은 확률로 재현되고 홈에 갔다 오면 정상이었다. SDK 렌더러는 정상인데 Flutter 컴포지터가 그 영역을 갱신 대상으로 보지 않는 타이밍 문제로 판단했다. `routeZoomMap` 제거, 안내 시작 지연, View 강제 invalidate는 효과가 없었고, 고객사가 `initalizeNavi`의 `onSuccess`에서 `setApplicatonStatus(FOREGROUND)`를 부르자 정상 동작했다.
  - iOS 26 동작 확인(04-17)은 문제없었다.
  - iOS SDK 2.0.1 종료 문제(08-18): 내비 화면을 닫아도 안내 음성이 계속되고, 다시 들어오면 음성이 나오지 않았다. Android는 `PlatformView.dispose()`에서 `destroyNavi()`를 부르지만 iOS에는 대응 API가 없다. SDK가 단일 controller에 단일 지도를 만들어 지우지 않는 구조이고, `initalizeNavi`에 넘긴 delegate를 strong으로 잡고 있었으며, 안전운행 모드 종료 처리가 없어 안전운행 음성이 이어졌다. iOS에도 `destroyNavi`를 제공하는 쪽으로 검토했다. `runReRouteChangeVia`의 "Invalid goal point"는 SDK 내부 오류로 확인되어 고치기로 했다.
  - 우측 하단 버튼 3개 숨김은 `forceHideMapComponent(BOTTOM_DRIVING_SIDE_BUTTON, true)`로 하며 왼쪽 수동 재탐색 버튼도 함께 숨는다(08-13).
- **두리텍**
  - 메인 메뉴(01-20~02-05): 최초 설치 후 첫 실행은 정상이고 재시작부터 메뉴가 이상하게 나왔다. 고객사는 `NaviSceneHandler.init()`만 불렀고, `onSuccess`에 `setApplicatonStatus(FOREGROUND)`를 넣자 하단 메뉴가 화면을 덮었다. 2월 4일 로그에서는 `onAttachedToWindow`에서 `MapLayer.getTurnView` NPE가 나 `initLayout` 반환값과 초기화 순서를 확인하도록 했다.
  - SurfaceView NPE(03-31): 네이버지도와 같은 XML에서 SurfaceView를 쓰자 `GLSurfaceView.surfaceChanged` NPE가 났다. 고객사가 아이나비 지도는 Activity, 네이버 지도는 Fragment로 나눠 해결했다.
  - 통신 OFF 상태 `initializeNavi()` 크래시(03-26, SDK `0.8.0`): 비통신이면 인증 실패로 `onFail(1000)`이 정상 호출되고 SDK 크래시 로그는 없었다. 앱에서 네트워크 상태를 확인한 뒤 초기화하고, `onFail`이 오면 앱을 종료하도록 권했다.
- **오비렛(02-13~24)**: 백그라운드에서 Background TBT가 나오지 않는다는 문의였다. 고객사는 `onStop`에서 `setApplicatonStatus(BACKGROUND)`를, 초기화 때 오버레이 권한 요청·`setDrawBackgroundTBT(true)`·`setBringToFrontListener`를 넣었다. 영상을 보니 모의주행 상태였고, Background TBT는 AIR와 마찬가지로 모의주행에서는 제공하지 않는다. 실제 주행에서는 정상 표출된다는 회신을 받았고, 가이드 문서에 이 내용을 적기로 했다.
- **기타**: 삼성전자 크래시 보고는 선택 업데이트 팝업에서 세션을 닫을 때 올라오는 이벤트로 사용자 영향이 없었다(03-09, POI 명칭 충돌 처리를 위해 DP를 추가한 뒤 `libairmaps.so` 객체 정리 문제 의심). PBV ISA Reconstructor는 알고리즘 데이터를 지도 데이터에서 받아 온라인/오프라인 구분이 없다(01-23). 유모스원 NDA 후 Android SDK 가이드 전달(04-24). 9월에 한진이 AIR App-to-App 길찾기와 경로선택 없이 추천 옵션으로 바로 안내하는 기능을 요청했다. Android에는 `KEY_DIRECT_GUIDE_START`가 있었지만 FCM 푸시·티머니 빌드에서만 동작했고(`IntentParserPush`에만 존재), iOS에는 없어 두 OS 모두 이번 패치에 추가하고 App-to-App 가이드에 "경로선택 화면 없이 즉시 안내"를 먼저 반영했다. 같은 달 다른 업체 요청(좌표열 최대 2,000개로 만드는 커스텀 경로, 이탈 시 지정 경로로 복귀하는 재탐색 옵션)은 약 8일(사업부에는 2주)로 산정했다. 내역은 좌표열 입력·이탈 재탐색 옵션 공개 API(1일), 좌표열→링크열 변환(투영·중복 제거·비연속 구간 보정, 3일), 탐색 요청에 커스텀 경로열 추가(확장기능 10)와 서버 연동 폴백(1일), 경유지 안내 미발생 검증(0.5일), 지정 경로 복귀 재탐색(3.5일), 검증·가이드(2일)였다. 탐색 측은 일부 기능은 탐색 API보다 경로 복원 API가 맞을 수 있고, 이탈 시 복귀는 엔진이 아니라 메인이나 중간 단계에서 제어해야 한다는 의견을 냈다(09-09~11). 요청 업체의 앱은 통학·셔틀버스 운전기사용 앱으로 보였다. ^[inferred] 사업 담당자가 바뀌어 시작일은 정해지지 않았지만, 급히 요청될 가능성이 높아 미리 개발하기로 했다. 동행맵 Maps SDK는 전달받은 AppKey로 바꾸면서 빌드 머신의 키 이름 충돌을 피하려고 키 이름에 접두사를 붙이고 iOS 워크플로도 바꿨다(09-22). 동행맵 맥락은 [[seoul-donghaengmap]].

## AIR 운영

### 배포·패치

- 출시: 1월 말, 2/3, 3/25, 5/1(Android 검증 완료), 5/7 핫픽스, 6월 말~7월 초, 9월 말 목표(9/28), 10월.
- **1월 말 패치**: 출시 과정에서 16KB 경고가 다시 떴는데, `03.05.59` APK에서 MMC `libmapmatch.so`만 16KB 정렬이 안 되어 있었다. 수정된 MMC 엔진으로 다시 빌드해 내부 배포와 스토어 업로드를 다시 했다.
- **3월 패치(3/25)**: DP 엔진 v2.1.0의 렌더 타이밍·로직 개선으로 60fps를 지원하게 되어 고사양 단말에만 적용했다. Android 고사양 판단은 `Build.VERSION.MEDIA_PERFORMANCE_CLASS`(Android 12+)를 먼저 보고, 값이 0이면 RAM 8GB 이상을 2차 조건으로 쓰되 Galaxy S10처럼 RAM이 큰 구형 단말을 걸러낼 API 레벨 조건이 필요할 수 있다고 봤다. iOS는 `UIScreen.main.maximumFramesPerSecond`로 판단할 수 있지만 CarPlay는 FPS를 확인할 API가 없고, 폰과 CarPlay를 모두 60fps로 돌리면 발열·배터리 문제가 있어 iOS 14 이상 Pro/Pro Max만 60fps로 정했다. 에어캐시 적립 기간이 12시간으로 바뀌어(Agent 값 기준) 문구를 고치고, 에어캐시 팝업의 "매일 밤 12시 초기화" 문구를 뺐다. 출시 노트는 "지도 화면이 더욱 부드러워졌어요!(일부 단말)", "CarPlay/Android Auto 개선"이었다. iOS는 App Store 소유자 계정의 계약(유료 업데이트) 동의가 있어야 업로드할 수 있어 임원 승인을 받았다.
- **4월 말 패치(4/29 목표, `03.05.61`)**: DP 성능 개선판, 강남순환고속도로 구간단속 표시 지속 문제(10km 넘는 구간단속, 터널 여러 개; 대표 VoE로 4월 중 수정 보고, 안내엔진 4/24 배포), w3w 호출량 최소화. 수정 내역은 지도 60fps(공통), w3w 통합검색 상세 RGC 호출 제거(공통), iOS 오디오 메모리 누수, AOS 최적지점 API 호출 시 progress bar 미표출이었다. w3w 검색·추천어 실패 처리(`w3w/autoSuggest`, `w3w/wordSearch`)는 양 OS 모두 문제없었다. 출시 노트에서 w3w 종료는 빼고 "모든 단말에서 더 부드러운 지도"로 썼다.
- **5~6월**: 5월 7일 안내엔진만 바꾸는 핫픽스를 냈다(출시 노트는 이전과 동일). 후면 과속카메라와 DP 개선은 6월 항목으로 넘겼다(AIR-2034). 6월 패치(`03.05.63`)는 행정구역 변경 때문에 검증팀 검증을 거쳤고(검증팀에도 AppTester·TestFlight 배포), 출시 노트는 "도착지가 고속도로 혹은 지하차도라면 안전한 주변도로로 안내", "후면 단속카메라는 통과 후에도 잠시 안내 유지", 최근 목적지 고정 풀림 등 안정화였다. iOS 출시 노트(`v03.05.39`)에는 고속도로 도착지 안내가 CarPlay에도 적용된다고 적었다.
- **9월 패치(9/28 목표)**: 포인트홈 개편에 따른 SDK 업데이트, 새 과속 단속 카메라 타입, 새 DP 엔진(발열 개선), Google Play target API 대응, 고속도로 팝업 Projection 재체크, 친환경 경로탐색과 유종 '수소' 추가(수소 충전소 주변검색 기능은 제외). 개선된 맵매칭 엔진은 다음 패치로 미뤘다(10-01). 10월 7일 내부 빌드 후 검증 배포 없이 스토어에 올렸고, 출시 노트는 AOS `v03.05.64`·iOS `v03.05.40`("친환경 경로", "수소차도 함께해요", 신규 단속카메라 안내)이었다. 10월 21일 탐색서버에 친환경 옵션이 들어간 엔진이 반영되어 기존·패치 앱을 다시 확인했다.

### 기능·사양

- **행정구역 개편(5~9월)**: 전남광주통합특별시와 인천 개편으로 데이터는 6/25, AIR 서비스 적용은 7/1(스텝형 주소검색, 통합검색 지역 필터)로 잡혔고, PND·KGM/TMC 쪽 일정과 컨버터 검토도 데이터 측에서 공유됐다. 통합특별시 주소검색 축약은 4자리는 그대로, 5자리 이상은 앞 4자리만 쓴다(05-29). Android 주소검색 시/도 목록은 서버 응답 `admname`을, 검색결과 지역 필터는 `address`를 써서 서로 달랐다. 하위 행정계 API(`/sire/searchSubAddr`) 결과를 그대로 그리므로, 전남광주(행정코드 12)를 서울 다음에 둘지는 서버가 순서를 바꿔 주거나 앱이 재정렬해야 했다. 7월 초 검색엔진이 축약명 '전남광주'를 '광주특별시'로 바꾸려 하자, Android는 표출 원천을 `admname`에서 `address`로 바꿔 둔 상태라 앱 재빌드가 필요했다(4글자면 1·3번째 글자로 약어를 만드는 로직도 있음). 네이버·티맵은 '전남광주', 카카오는 전체 명칭을 쓴다. 최종적으로 9월 3일 RGC 서버 패치에서 축약명이 다시 '전남광주'로 정리됐고, 경로 주변 검색에서 '광주특별시'로 나오던 부분도 서버 재패치로 해결됐다. 행정계 순서(서울 다음 전남광주, 또는 티맵처럼 가나다순)는 이번에는 명칭만 바꾸고 나중에 하기로 했다(07-31).
  - 6월 검증 이슈(MAP-639~647): 위치지정 화면 하단 주소는 RGC 결과를 그대로 써서 이전 행정구역이 내려오는 것은 Agent 문의 대상이었다. 경로 유무에 따라 주소 체계가 달랐던 것은 `searchPoiAround`가 단축 행정계, `searchRouteAroundMulti`가 정식 행정계로 응답해서였다(둘 다 `cutflag=1`, 서버 수정 필요). 중구→영종구는 atl.zip의 admin 데이터(26.07a) 문제로 앱 재설치 후 정상이었다. iOS GUI 배경색 오류와 MAP-645는 iOS 버그였다.
- **고속도로·고가 목적지 팝업(6~9월)**: 목적지가 고속도로/지하차도/고가도로이면 주변 일반도로로 바꿀지 묻는 팝업을 띄운다. AIR/Hybrid는 차기 패치, KGM은 9월 MR, TMC는 8월 SU#2에 반영한다. '예'를 고르면 최적지점 API로 지점을 바꾼다. 최적지점 속성은 0 전체, 1 차량 입구점, 2 택시 승하차(건물), 3 택시 승하차(단지)이고 AIR는 1로 요청해 고속도로에서도 가장 가까운 입구점을 찾는다. 최종 문구는 "선택하신 도착지가 고속도로에 있습니다. 안전한 도착을 위해 주변 일반도로로 변경하시겠습니까?"(일반도로 변경 / 도착지 유지), 실패 시 "일반도로 변경에 실패했습니다.(에러코드)" 토스트이고, 경유지 팝업은 필수가 아니어서 개발 공수에 따라 정하기로 했다. 도착 핀을 DP 좌표에 두고 RP 좌표까지 점선으로 잇는 방식(티맵·네이버)은 DP에 선 그리기 함수가 필요해 이후 DP 엔진과 논의하기로 했다. 최초 1회 팝업이 누락되는 문제는 SMR 다운로드 타이밍 때문이었다(07-07). 길찾기 전에 Projection을 미리 돌리는 안(통합검색 선택·롱탭 시점)과 탐색 완료 후 체크하는 안을 비교했고, 기존 사전 체크를 유지하되 Projection이 실패할 때만 탐색 후 다시 체크하는 하이브리드안을 차기 패치에 넣었다. 이와 관련해 SMR 엔진의 다운로드 구조(0.8초 주기 fetch 스레드, 한 배치 최대 50 메시, 읽기 실패가 다운로드 트리거, 체크섬 실패 시 재다운로드)를 문서로 정리했다.
- **후면 과속카메라(5~6월)**: 통과음이 안 나던 것은 Android가 카메라 통과 판단에서 후면 카메라 타입을 체크하지 않아 처음부터 발성되지 않은 것이었다. KGM 사양(통과 후 80m까지 심볼 유지, 거리는 숨김, 과속 체크, 다른 카메라보다 우선)을 따라 메인 작업만으로 반영했다. 목적지 없는 안전운전에서 안전운행구간 통과 직전 안내가 나오던 것은 카메라 정보가 30m 남았을 때부터 들어오고 있었다. Android Auto 3D 핀치줌 범위 문제는 단말이 없어 시뮬레이터로 보기로 했다(05-07).
- **유종·친환경**: 수소 유종은 6월에는 추가하지 않고 서비스 중인 유종만 탐색엔진에 넘기기로 했다(06-08). Android는 내 차 정보의 유종(EV 포함)을 경로 탐색 요청에 넣고 있어 Agent에 규격서 현행화를 요청했다. 9월에 수소를 다시 넣으며, 최저가 주유소 메인카드와 고속도로 휴게소는 휘발유 기준이 기본이지만 수소이면 '주변 최저가' 메인카드와 고속 모드 요금을 표출하지 않고, Android Auto 주변 검색은 수소 충전소 카테고리 코드를 쓰되 가격 데이터가 없어 '정보 없음' 대신 [충전소명 + 거리]만 보이며, 환경설정 유종에서 수소를 고르면 '선호 주유소 및 충전기 타입'을 숨기고, 튜토리얼 연료 설정에도 수소를 추가하기로 했다(09-10~16). 친환경 경로 옵션은 경로 선택·다른 경로·기본 옵션 변경 모두에서 3번째 위치("에어추천, 가장빠름, 친환경")에 "친환경"으로 표시한다. 재탐색은 RouteHeader의 `optionName`으로 하는데, 친환경도 에어추천·가장빠름처럼 `real_traffic2`로 응답되고 이 두 옵션은 재탐색 때 `searchOptionOrg`로 따로 보내고 있어 탐색 측이 공유한 `recommendation_eco` 방식과 맞춰야 했다. 로그 `routeOpt`와 `/saveConfig`의 `defaultRouteOption`에도 친환경 규격을 추가하도록 Agent와 협의했다(09-21). iOS만 유종이 전기일 때 경로상 주유소 검색 결과가 비던 문제는, 전기 선택 시 iOS가 정의되지 않은 sort 값 100을 보내고 있어서였고 전기충전소 외 카테고리는 거리순으로 요청하도록 고쳤다(07-07).
- **어린이 보호구역 마커(09-17)**: 경로 탐색 응답의 안내 데이터(gdata)를 받아 안내엔진에 넣으면, 엔진이 경로 위 스쿨존 좌표 목록(링크 ID, 경위도)을 `JSchoolInfo` 배열로 주고 앱이 경로를 고를 때마다 마커를 그린다.
- **신규 안전운행 음성(09-15)**: AIR·KGM/TMC 안전운행 데이터 통합으로 받은 음성 중 '발랄한 음성'에서만 새 음성이 어색하게 들렸고, 수정된 음성으로 바꾼 뒤 정상이었다.
- **가변 제한속도 카메라(01-13)**: 1월 1차 지도(1/6)부터 AIR.zip에 시간대별 가변 제한속도 카메라 DB(`camera_exc.txt`)가 들어갔다. 단말 시간을 바꿔 보니 현재 시간 30km, 20시 1분 50km로 정상이었다.
- **전기차 통행료 할인(01-02)**: AOS·iOS 모두 2024년 50%, 2025년 40%, 2026년 30%, 2027년 20%를 하드코딩했고 2028년부터는 할인이 0이다.
- **최근목적지 핀(06-08)**: 핀 설정이 유지되지 않는 문제를 6월 패치에서 고쳤다. 고정 키는 좌표 x, y와 이름을 이어 붙여 만든다.
- **검색 상세 카테고리(04-13)**: AOS는 `dp_catecode`가 비었거나 000/360이면 숨기고 아니면 `catename`을 표시한다. iOS는 닫혀 있을 때는 `dp_catecode`, 펼쳤을 때는 `catename`을 그대로 써서 AOS 방식으로 맞추기로 했다.
- **요약 탐색(05-12)**: `/findSummaryRoute`는 메인 화면(App/Auto)의 집/자주가는곳에서만 쓰고, iOS는 위젯의 집/자주가는곳 등록에서도 쓴다.
- **경로 주변 CCTV(C3000)(07-15)**: 탐색 측이 관리하지 않는 데이터라 쓰지 않으면 제공을 끊겠다고 물었다. Android는 쓰지 않았고, iOS는 C3000 요청 코드는 없지만 교통정보를 켜면 플래그로 경로 주변 CCTV를 받는 API가 있어 Agent 사용 여부를 확인했다.
- **기타**:
  - 위치보기에서 위치를 바다로 옮기면 iOS가 죽었다(05-06). w3w 제거와는 무관하고, 2023년 AOS 사양에 맞추면서 iOS에서 903 오류의 nil 예외 처리를 빠뜨린 탓이었다.
  - Auto 연결 시 속도가 화면 중앙에 뜨는 스토어 리뷰 지적(`03.05.60 (301449)`, 04-02)이 있었다.
  - THINKWARE 멤버십 사이트에서 뒤로 가면 iOS가 죽었다(04-15~16). 신규 로그인은 ServiceGate `memberLoginUrl`을 쓰지만 통합회원 전환은 고정 URL을 쓰고 있었고, 크래시는 메모리 누수였다. 함께 수정했다.
  - 배너 아웃링크는 Admin 이벤트 타입 A9를 배너에 연결하면 외부 브라우저로 연다(06-04).
  - HUD 등록 VOC(05-11)는 사양대로였다. 인증 버튼은 시리얼이 `IHA`/`IHT`로 시작하고 영문·숫자 6~7자리일 때만 활성화되며, 해당 사용자의 시리얼은 처음부터 지원 대상이 아니었다. iOS HUD BluetoothLibrary는 2025-10-02에 받은 것이 최신이다(06-19). HUD 이력은 [[air-image-hud-review-2025]].
  - 핀크럭스 게임 멀티미션 광고는 핀크럭스가 확인한 뒤 열어야 해 회신을 기다렸다(04-02).
- **위치기반서비스 실태점검(02-23)**: 3월 말 위치기반서비스 사업자 서면 실태점검이 아이나비 에어를 대상으로 예정됐다.
- **통계(03-20)**: AIR 통계를 CAMS 대신 BigQuery 배치 + Grafana로 옮겼다(일별 매일 0시 10분, 월별 매월 1일 1시, 당일·당월 UV 조회 불가). 접속 정보는 원본에 있음(미수록). 4월 1일 Orbis Admin 통계 회의에는 이동은이 참석했다.

### 라이브러리·플랫폼

- **포인트홈**: 2월에 Android 포인트홈 최신 버전을 넣은 테스트 APK(`03.05.60`)를 업체에 전달했다. 9월 개편 때 Android `2.1.6`→`3.4.0` 중 권장 의존성인 AppLovin `13.6.3`이 minSdk 24를 요구해 빌드가 실패했고(13.6.2까지는 23), 업체 회신으로 AppLovin을 `13.6.2`로 낮췄다(09-15). iOS 포인트홈 `3.1.2`는 SPM 13.0 이상, CocoaPods 14.0 이상이라 SPM으로 가고, SPM을 지원하지 않는 UnityAds 미디에이션은 뺐다.
- **iOS 최소 OS**: AIR 최소 OS는 AOS minSdk 23(Android 6.0), iOS 13.0이다(05-08, 07-16 재확인). Xcode 27부터 최소 배포 타깃이 15.0 이상이라 9월 패치는 26.6으로 내고 다음 빌드부터 15.0 상향을 결정해야 한다(Apple 권고 시한 2027년 4월, 10-06).
- **26.05 지도(4월)**: AIR 5월 지도(2605a)에 페리 항로용 Mesh가 추가됐다(03-27). 개발서버에서 26.05 지도로 모의·로그 주행이 오프로드로만 됐는데, `smrmanage.bin`의 mesh 개수(5668)와 `smrcacheinfo.bin` 크기 검사가 맞지 않아 SMR 초기화 유효성 검사가 실패한 것이었다. 최신 cache 파일을 쓰면 정상이었고, 임의로 만든 파일은 iOS에서는 동작했지만 AOS는 일부만 받다 멈췄다(SMR so 로그가 없어 원인 분석 어려움).
- **Firebase(03-18)**: 공용 계정으로 Firebase API 키에 Android 앱 제한을 추가했고, FCM·App Distribution·Remote Config에 영향이 없음을 확인했다. ^[inferred]
- **기타**: 개발서버 이용약관 웹뷰의 SSL 인증서 만료(03-11, 이후 정상화), 개선된 맵매칭 엔진 반영 여부(10-01, 다음 패치로), Google Search Console 권한 추가(10-20).

## Open Questions

- 호주향 KIAT 과제 선정 결과와 팀 참여 여부는 확인되지 않는다.
- iOS 최소 배포 타깃 15.0 상향 결정은 10월 현재 미정이다.
- 삼성생명 Location SDK의 Kotlin 대응안(Android만 2.0.0) 최종 배포 결과가 채널에 없다.
- 오믈렛 iOS `destroyNavi` 제공, Hetone 두 SDK 동시 사용(`repackageclasses`, MapLibre 의존성 전환), Hetone 3999(특정 출발지 도로 확장 실패)의 최종 반영 버전은 채널에 없다.
- 행정계 표출 순서(서울 다음 전남광주, 가나다순) 변경은 보류 상태다.

## Sources

- Slack 비공개 채널 `#001_air_nsdk_dev`, 2026-01-01 ~ 2026-10-26 메시지와 답글 스레드 147개(2026-10-26 조회). 원본은 `_raw/`에 저장하지 않았다. 참여자·외부 인사 이름, 메일 주소, 전화번호, 계정·비밀번호, API 키·토큰, 서버 주소, 저장소·공유 링크, 단말 시리얼은 옮기지 않았다.
