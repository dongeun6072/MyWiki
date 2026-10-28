# Bitbucket navisdk_core 커밋 목록 (본인 작성분)

- 저장소: Bitbucket mobility-tech/navisdk_core (로컬 clone `Android/inavi-navigation-sdk/global-inavi-navigation-sdk-android`)
- 필터: `git log --all --no-merges --author=dongeun`, stash 항목 제외
- 수집일: 2026-10-28, 총      972건, 기간 2024-10-23 ~ 2026-09-08
- 형식: `해시|작성일|커밋 메시지` (최신순). 메시지 원문이며 diff는 검증하지 않았다. 서버 포트 값 1건과 숨은 기능 진입 방법 1건은 가렸다(보안 규칙).

```
a6aeddbb|2026-09-08|aos-playground 앱 버전 업데이트 (1.0.3 -> 1.0.4)
570a34f8|2026-07-15|🔧 v1.0.4 배포 산출물 서브모듈 포인터 업데이트
9950c222|2026-07-15|ReleaseVersion 업데이트 (1.0.3 -> 1.0.4)
33ec3d39|2026-07-14|🔧 Kotlin 2.3.21 증분 네이티브 컴파일 빌드 오류로 비활성화
a00e750c|2026-07-08|📝 wiki 서브모듈 포인터 업데이트
f0fc2211|2026-07-08|♻️ [NSDK-757] setFrameworkType을 flutter 고정으로 단순화
6bff330c|2026-07-08|📝 wiki 서브모듈 포인터 업데이트
9132e646|2026-07-08|✨ [NSDK-757] 공통 헤더에 framework_type 필드 추가
dc8473d3|2026-07-03|📝 wiki 서브모듈 포인터 업데이트
39ca2964|2026-07-03|⬆️ Kotlin 2.3.21 및 주요 의존성 버전 업그레이드
3c346be3|2026-06-26|📝 wiki 서브모듈 포인터 업데이트
4f9f2bea|2026-06-26|📝 [NSDK-744] 헤더 캐시 재생성 조건 주석에 serviceGateDto 반영
a6ae7301|2026-06-26|✨ [NSDK-744] agent 서버 API 요청 헤더에 mapVer 필드 추가
9e9957fb|2026-06-23|🐛 [NSDK-743] 링크 데이터 없을 때 교통색상 경로 사라짐 수정
affe9a8d|2026-06-22|📝 wiki 서브모듈 포인터 업데이트
91fc5ab8|2026-06-22|🔥 [NSDK-743] RouteFragment 미동작 경로색상 코드 제거
2298fd17|2026-06-22|🐛 [NSDK-743] 경로 변경 시 교통색상 미반영 수정
9281616d|2026-06-19|📝 [NSDK-741] navi-global 에러 처리 문서 코드리뷰 후속 반영
fd5634f4|2026-06-19|🎨 [NSDK-741] 지도 다운로드 UseCase 미사용 import 제거
5a732236|2026-06-19|♻️ [NSDK-741] 응답 코드별 InvErrorCode 1:1 매핑으로 세분화
20d27044|2026-06-19|♻️ [NSDK-741] runRoute 반환 타입 non-null화 및 죽은 분기 제거
0b52c420|2026-06-19|♻️ [NSDK-741] 응답 DTO 추출 로직 공용 unwrap 확장으로 통합
9fe93364|2026-06-19|⚡ [NSDK-741] ServiceGate 헤더 캐싱 복원으로 요청마다 재생성 제거
2a4d94c7|2026-06-19|⚡ [NSDK-741] 네트워크 응답 본문 이중 역직렬화 제거
9b54c8e4|2026-06-19|📝 [NSDK-741] navi-global 위키 ADR/architecture 백필 반영
3cd13c70|2026-06-19|🚚 [NSDK-741] 남은 설계 문서를 wiki로 이전하고 docs/ 제거
3d137a27|2026-06-19|🚚 설계 문서를 wiki 서브모듈로 이전
1391b4b8|2026-06-19|🚚 log-drive-picker 설계 문서 파일명/위치 정리
f1b6b40e|2026-06-19|📝 [NSDK-741] 에러 처리 일원화 ADR 추가
5bf6d31b|2026-06-18|♻️ [NSDK-741] 공통 SDK 에러 처리 구조 일원화
a98f7585|2026-06-18|📝 [NSDK-741] 네트워크 에러 처리 재설계 문서 추가
f1fa4654|2026-06-16|♻️ [NSDK-740] 지도 언어 필드 적용 로직 단순화
662e1686|2026-06-15|✨ aos-playground에 지도 모드/언어 변경 버튼 추가
80cf0f62|2026-06-15|🐛 MapTheme 변경 시 차기/차차기 화살표 사라지는 문제 수정
42997de6|2026-06-12|✨ [NSDK-740] iOS InaviController.setLanguage 공개 API 추가
c6997a1e|2026-06-12|🐛 [NSDK-740] AUTO 언어 적용 시 디바이스 언어 live 조회로 수정
fb3d8998|2026-06-12|♻️ [NSDK-740] getLanguageType when 표현식 정리
d06aa75d|2026-06-12|✨ [NSDK-740] 스타일 기반 지도 다국어 적용 및 setLanguage API 추가
de089632|2026-06-12|✨ [NSDK-740] 지도 표기 언어 타입 및 스타일 언어 파서 추가
09fbfbfa|2026-06-12|📝 [NSDK-740] Style 기반 지도 다국어 설계 및 구현 계획 문서 추가
3774ced9|2026-06-11|🔥 [NSDK-739] iOS UI에서 MapHelper 참조 제거, DataStore.currentMapStyle 적용
2a0cfc95|2026-06-11|🎨 [NSDK-739] 인증 Style 검증 코드 포맷 정리
bb7bb414|2026-06-11|✨ [NSDK-739] Style URL 누락 전용 에러코드 AUTH_STYLE_URL_INVALID(1008) 추가
8fa99e78|2026-06-11|🔥 [NSDK-739] MapHelper 제거 및 인증 응답 Style URL 기반 지도 스타일 적용
945905e4|2026-06-11|✨ [NSDK-739] 인증 성공 시 imapsResult 저장 및 ImapsError 초기화 실패 매핑
43fd8eac|2026-06-11|✨ [NSDK-739] 인증 응답에 Style URL 검증 추가
12790d60|2026-06-11|✨ [NSDK-739] DataStore에 imapsResult 보관 및 currentMapStyle getter 추가
6fbe2e77|2026-06-11|✨ [NSDK-739] PException에 ImapsError 타입 추가
a1dee17d|2026-06-11|⬆️ [NSDK-739] orbismap-model 서브모듈 업데이트 (resultDark 필드 추가)
a76f8d85|2026-06-11|docs: Web 기반 인증 Style 적용 구현 계획 추가
745dea9f|2026-06-11|docs: Web 기반 인증 Style 적용 설계 문서 추가
6e5f3084|2026-06-09|✨ [NSDK-738] DevMode 로그주행 파일 선택 기능 구현
7c8f959b|2026-06-09|🔥 [NSDK-738] writeDriveLogToFile 공개 API 및 내장 로그 파일 제거
65019bcb|2026-06-09|🚚 [NSDK-738] 로그주행 설계/계획 문서를 docs/plans로 이관
fc7ea81c|2026-06-05|docs: 로그주행 파일 선택 팝업 구현 계획 추가
d6fb5f80|2026-06-05|docs: 로그주행 파일 선택 팝업 설계 문서 추가
75cce393|2026-06-02|Android Playground 버전 업데이트 (1.0.2 -> 1.0.3, 26 -> 27)
113040ce|2026-05-26|🔧 [NSDK-732] 난독화 시 navisdk 패키지명 유지 설정 추가
ae512300|2026-05-22|Android API reference Sync 1.0.3
3cc15d76|2026-05-22|✨ [NSDK-731] AOS edge-to-edge 대응
e820d8ec|2026-05-22|🔧 [NSDK-731] targetSdk 35 상향 및 versionName 반환타입 수정
1ecc975d|2026-05-19|chore: fullBuild.sh에 --mapmatch-aar-only 옵션 추가
59b5468c|2026-05-15|NSDK-716 [진입 방법 제거] 개발/준상용 서버 전환 알럿 추가
1d28dd7a|2026-05-13|NSDK-716 개발/준상용 서버 전환 기능 추가
1ddb4ab2|2026-05-11|FileManager rootPath 접근제한자를 private에서 val로 변경
97480375|2026-05-11|ALL_COMPONENT hide 토글 시 false 미동작 수정
29f87f47|2026-04-08|NSDK-688 공통 처리 함수 통합 진행
98519815|2026-04-06|NSDK-688 Path 상수 방식으로 변경 및 필요없는 로직 제거
33119443|2026-04-06|NSDK-682 MMCModule 상태 프로퍼티 setter 정리
be4fe915|2026-04-06|NSDK-682 LocationProvider 쪽 필요없는 로직 제거
75b936f1|2026-04-06|NSDK-682 PackageUtil 삭제
5337b21b|2026-04-03|NSDK-682 필요없는 로직 제거
33fc753d|2026-04-02|NSDK-684 스트리밍 다운로드 Ktor로 변경하면서 발생한 iOS 비정상 종료 이슈 수정
01ebf767|2026-04-01|NSDK-684 SDK 초기화 순서 변경 및 UseCase invoke operator fun 적용
a38e3e5b|2026-04-01|null 예외처리 안되어있는 부분 수정
6db4e345|2026-03-31|fix: MCP bb_post 호출 시 null로 응답받는 문제 수정
4fa23164|2026-03-31|code-reviewer Skill 추가
b79b7bfe|2026-03-31|NSDK-679 경로탐색 및 DTO 변환을 처리하는 RouteRepository로 이관
2f81f15c|2026-03-31|NSDK-679 path 문자열은 하드코딩 하도록 수정
739a4234|2026-03-31|NSDK-679 iOS 빌드 안되는 문제 수정
4685b9a3|2026-03-31|NSDK-679 StreamingDownload 공통 로직으로 변경
74dbfc8e|2026-03-31|NSDK-679 필요없는 로직 제거
ec26d950|2026-03-31|NSDK-679 요청 로직만 존재하는 NetworkModule로 리팩토링 진행
366670f1|2026-03-31|NSDK-679 Response 공통 에러 처리함수 추ㄱ
54aef2b6|2026-03-31|NSDK-679 BaseUrl, HttpUrl 주입을 위해 di에서 직접 선언, handler, Mapper 사용하여 공통 함수로 구현
60b19795|2026-03-30|UMap 버전 업데이트 (1.0.1 -> 1.0.2, 25 -> 26)
66d0d9b0|2026-03-27|fix: .claude/settings.json mcp 서버 인식 안되는 문제로 루트에 mcp.json 변경
581e1c98|2026-03-27|add: Bitbucket MCP 추가
0177c822|2026-03-27|docs: claude 폴더 중 Settings.json만 추가 될 수 있도록 수정
6c617fcd|2026-03-27|docs: Claude gitignore 추가
baabecd6|2026-03-27|NSDK-678 ios 전체빌드 시 Docs 문서도 빌드해서 spm에 적용
d3631b8b|2026-03-27|NSDK-678 iOS 배포된 모듈 xcFramework를 spm 서브모듈로 Copy
9e112252|2026-03-27|NSDK-678 iOS Spm repo 서브모듈로 추가
d6334796|2026-03-27|NSDK-678 FullBuild.sh 추가 및 통합 빌드 문서화
7139d5fe|2026-03-27|NSDK-678 api-references 서브모듈 업데이트
901d0172|2026-03-25|Android API 래퍼런스 배포 전 일부 문구 제외 및 수정
b5559cf9|2026-03-25|[AOS] MapMatch 0.6.5 Jfrog 배포
3f59f69b|2026-03-25|[공통] OrbisRouteLib v1.0.1.5 적용
7b150978|2026-03-24|OrbisRouteLib v1.0.1.43 적용
4557dac8|2026-03-19|경로 탐색 엔진 v1.0.1.41 적용
5547f560|2026-03-13|릴리즈 버전 업데이트 (1.0.1 -> 1.0.2)
24913c53|2026-03-13|NSDK-660 차량 제원 옵션은 따로 인터페이스 형태로 제공
6d375813|2026-03-13|NSDK-660 트럭향 Weight, Height, length Request 파라미터 대응
362f8b9b|2026-03-13|NSDK-660 트럭향 서브모듈 업데이트
856304c5|2026-03-12|NSDK-661 OrbisMapMatch.h 새로 추가된 메서드 대응
d01fa0c6|2026-03-12|NSDK-661 iOS MapMatch xcframework 교체 0.6.5
17809b09|2026-03-12|NSDK-661 Android MapMatch aar 교체 0.6.3 -> 0.6.5
1d654176|2026-03-11|docs: mkdocs 비율Extensions 추가, 특정 가이드 이미지 비율 축소 진행
667e8ca9|2026-03-11|가이드 이미지 교체 260311
9a2c2ab6|2026-02-19|누락된 README.md 추가
9d6a18cf|2026-02-19|README.md 추가 작성
e5bb0ac5|2026-02-03|UserMode 세팅 로직 추가
7564ab44|2026-02-03|Android Ui 모듈에서 없는 이미지 참조하는 이슈 수정
abaea3fc|2026-01-29|[공통] serviceType Header 값 추가
d48a79bf|2026-01-29|Submodule Update
90826e29|2026-01-29|UMap 버전 업데이트 (0.1.16 -> 1.0.1, 24 -> 25)
b536be5b|2026-01-29|[AOS] SetMapCenter 함수 변경으로 인해, 애니메이션 적용이 안되는 이슈 수정
f09cf47a|2026-01-29|Release Version 업데이트 v1.0.1
88ab54ba|2026-01-29|SubModule 업데이트
16a170e7|2026-01-29|SDKVersion releaseVersion 필드 변경 안되는 문제 수정
13082ec6|2026-01-29|NSDK-650 도메인 URL 변경, UMap App Key 변경
a089a50e|2026-01-29|NSDK-647 VersionFile을 강제로 소스셋에 포함하는 로직 추가, AppVer 값 적용
5a7975a8|2026-01-23|Android 빌드 안되는 문제 수정
f782ea5c|2026-01-15|iOS 버전 코드 업데이트 (Core 115 -> 116, UI 116 -> 117)
31974616|2026-01-15|[iOS] 주행지도 및 일반지도가 동일한 Padding 값 사용하는 문제 수정
6e485ceb|2026-01-14|TimeManager 제거 (Kotlinx.datetime 라이브러리 사용하도록 변경)
a532a652|2026-01-14|경로선택 AnimatedCamera 호출 시 비정상 종료되는 문제 수정
c94b19a1|2026-01-14|개발자 모드가 아닌 경우에만 LogWriters를 Empty로 변경
dd79a886|2026-01-13|RunSearch, RunRoute, Geocode, Reverse Geocode 요청 시 SDK 초기화가 안되어있으면 Fail 전달
4bfbcad0|2026-01-12|Android 일반 지도에서 애니메이션 시간 적용되지 않는 문제 수정
5759d215|2026-01-08|SDK 초기화 플래그 DataStore에 추가, 일반 지도 추가 시 SDK 초기화되지 않으면 빈 화면 표출
c3d0be2d|2026-01-08|개발 모드 설정에 따라 로그표출 설정, 인증 요청 시 MDN 인자 제거, Core 내부 AppKey 하드코딩 로직 제거
cebe8ff8|2026-01-07|Release 버전 업데이트 v1.0.0
3e910d81|2026-01-07|대만향 플래그로 변경
121d4843|2026-01-07|초기화 실패 후 API 호출 시 동작하지 않도록 플래그 추가
ef058666|2026-01-07|NSDK-614 그 외 Third party 라이브러리 업데이트
45cce768|2026-01-07|NSDK-614 Kotlinx, Multiplatform 관련 라이브러리 업데이트
ead479b3|2026-01-07|NSDK-614 AGP, AndroidX & Jetpack 라이브러리 업데이트 (추후 Target SDK 업데이트 진행 시 업데이트 필요)
5cff8e87|2026-01-07|NSDK-614 중복 선언 할 필요없는 Core 라이브러리 제거
0bb7c7a9|2026-01-06|NSDK-614 Kotlin, Ksp 버전 업데이트 (2.1.0 -> 2.2.20), Skie, moko resource 업데이트 진행
a13f641d|2026-01-06|NSDK-614 사용하지 않는 Compose Compiler 플러그인 제거
12636fcd|2026-01-06|NSDK-614 Bundles 구성 후 추가
1d92af2c|2026-01-06|NSDK-614 의존성 관리 효율화를 위한 Version Catalog 리팩토링
42f07b60|2026-01-06|NSDK-614 사용하지 않는 라이브러리 제거
cbbcd75a|2026-01-06|NSDK-614 XmlUtil 라이브러리 제거 (커스텀 어노테이션 추가로 공용 모델 변경없이 동작하도록 수정)
d52b6f3c|2026-01-06|NSDK-614 iOS MapLibre 버전 업데이트 ("6.19.3" -> "6.22.1")
3423a7aa|2026-01-06|NSDK-614 Android MapLibre 버전 업데이트 ("11.10.1" -> "12.3.1")
0364559c|2026-01-06|Android 나침반 맵버튼 Top Marign 추가
6d1d74fe|2026-01-06|[iOS] SafeArea 존재 시 Top Margin 제거
94b1a2c8|2026-01-05|[iOS] 지도 나침반 회전 갱신 로직 최적화
9c93a965|2026-01-05|NSDK-612 로그 비활성화를 위해  kermit.Logger로 전체 변경
9aaa0929|2026-01-02|NSDK- 612 Debug 빌드가 아닌 경우, LogWriters를 Empty로 변경
629c96ca|2026-01-02|NSDK-610 필요없는 로직 제거
c8db865f|2025-12-31|NSDK-610 지도이동이 될때마다 Compass Transform 갱신되도록 추가
5d0a2ed0|2025-12-31|NSDK-610 Custom CompassView 구현
a04b49a6|2025-12-31|Google-Services 파일 이동
5c43a60f|2025-12-31|[공통] Utils 모듈의 iosSimulatorArm64() 주석 처리
62c0c9dd|2025-12-30|NSDK-606 UMap 앱 추가 설정
074aa772|2025-12-30|NSDK-601 iOS 스타일 재설정 시 경로가 존재하는 경우 다시 표출되도록 변경
ce91d77b|2025-12-29|NSDK-601 iOS 스타일 재설정 시 기존 마커가 존재하는 경우 다시 표출되도록 변경
79553694|2025-12-29|[공통] 지도 초기화 응답 시 바로 MapLibre 속성 및 로고 제거하도록 변경
530e4745|2025-12-29|[공통] 필요없는 라이브러리 및 소스 제거
62469a20|2025-12-24|NSDK-601 스타일 재설정 시 기존 경로가 존재하는 경우 다시 표출되도록 변경
e2ec8dc6|2025-12-23|NSDK-601 스타일 재설정 시 기존 마커가 존재하는 경우 다시 표출되도록 변경
4caba250|2025-12-23|NSDK-601 필요없는 Class 제거
1e709f6d|2025-12-23|NSDK-601 카메라 요청 시 사용하는 Key 값 서버 기반으로 변경
9def74d8|2025-12-23|NSDK-599 소스 정리 및 로직 일부 개선
2e93dc03|2025-12-23|[iOS] 전체경로에서 뒤로가기 시 카메라가 비 정상적으로 적용되는 문제 수정
138825ba|2025-12-22|libOrbisRouteStaticLib.a Push
d8c2b454|2025-12-22|버전코드 업데이트 (0.1.15 -> 0.1.16, 23 -> 24)
08170f93|2025-12-22|[공통] 대만향으로 변경 추가
9e2d2fa8|2025-12-22|[공통] 야간 모드 관련 로직 제외
82f35fa5|2025-12-22|[공통] Moko Permission 모듈별로 의존성 가져오도록 변경 및 버전 업데이트
cc779d16|2025-12-22|NSDK-599 검색 타입에 따라, Genesis/Orbis 검색 요청 로직 반영
86eb0db0|2025-12-19|NSDK-599 SDK 초기화 로직 so TomTom API Key 요청 로직 추가,  DataStore에 해당 키 저장
5d742c97|2025-12-19|AIR-599 ServiceGate 요청 로직 초기화 UseCase 내부로 이동, DataStore에 해당 응답 Dto 저장
e9e9f22d|2025-12-18|[iOS] 지도 이동 및 뷰모드 변경 시 heading이 0으로 되는 문제 수정
970bff4f|2025-12-18|[iOS] 뷰모드 변경 시 tilt 변경 안되는 문제 수정
bee63ffa|2025-12-18|[iOS] 재탐색 시 지나온 경로선이 표출되는 문제 수정
abf5e178|2025-12-18|[공통] UpdateRouteLine시 경로선 애니메이션 Job 취소하는 로직 제거
cc6c0e53|2025-12-18|Country 상태 값 변경
17d990a9|2025-12-18|NSDK-599 Share Module 업데이트 진행
4cc5c320|2025-12-18|[iOS] TTS 발성이 끝날때 효과음이 나올때, 효과음 타이밍이 밀리는 현상 수정
3519e819|2025-12-16|NSDK-597 효과음 기능 추가
11851418|2025-12-09|NSDK-598 키보드 검색 버튼 클릭 시 Genesis 검색, 최근검색어 클릭 시 Orbis 검색 진행
66e669f3|2025-12-09|NSDK-598 Genesis 검색 API 검토를 위해, 요청 로직 추가
9288bea9|2025-12-09|[iOS] 속도에 따라 지도 ZoomLevel 변경되도록 수정
df36de70|2025-12-08|[iOS] Localization 국가 추가
4292b0a8|2025-12-08|NSDK-582 ios AudioFocus 동작 적용
816dd934|2025-12-04|NSDK-582 TTS 음성은 LanguageCode로 세팅하는걸로 적용
6ed6d33c|2025-12-04|NSDK-582 ios 위치 지정 포맷 처리가 정상적으로 되지 않아 임시 수정
0a7f52da|2025-12-04|NSDK-582 음성 발성 로직 추가
1406223d|2025-12-03|NSDK-582 TTS 구현을 위해 Common 영역에 컨트롤러 구현, Android 에서 적용했던 발성 사양 적용
1baa01bc|2025-12-03|NSDK-595 테스트 코드 추가
e9778ff8|2025-12-03|NSDK-595 현위치 패딩 값 일부 수정 (Side dp 수치 조정)
5453b05f|2025-12-03|NSDK-595 removeAllRouteLine, removeAllMarker 구현체 정의
b99cf360|2025-12-03|NSDK-595 MapIF 필요없는 인자 제거
0d19d85d|2025-12-03|NSDK-595 필요없는 MapIF 함수 제거
bc0c5167|2025-12-03|NSDK-595 Viewmode에 따른 패딩 값 재설정
f4c9b4a0|2025-12-02|NSDK-595 경로선 관련 삭제 로직 추가
016756a8|2025-12-02|NSDK-595 소스 정리
9b2ab1e7|2025-12-02|NSDK-595 테스트 코드 추가
be387ece|2025-12-02|NSDK-595 카메라 모드 변경 및 ViewMode 변경 시 현위치 애니메이션 적용되는 문제 수정
90037f30|2025-12-01|NSDK-595 지도 이동 시 현위치 아이콘이 따라 움직이는 이슈 수정, 지도 이동 시에는 카메라 동작하지 않도록 수정
a7810245|2025-11-28|NSDK-595 지도 Gesture 가 비정상적으로 동작하여 판단 조건 및 일부 로직 수정
81dc836a|2025-11-28|NSDK-595 주행 테스트 로직 추가
ac654480|2025-11-28|NSDK-595 Viewmode 변경 시 현위치로 오지 않는 문제 수정
0473b90e|2025-11-28|NSDK-595 공용 카메라 업데이트 로직 추가
91daeaad|2025-11-28|NSDK-595 Android 누락된 부분 수정
ad7a0188|2025-11-27|NSDK-595 Config Class 형태로 사용하기 힘들어 Object로 변경
cd7fb74d|2025-11-27|NSDK-595 Class로 사용하는게 불편해서 Object 형태로 변경
e8a56764|2025-11-27|NSDK-595 공통 패딩 속성을 처리하기 위해 공용 Config 생성
ff6fc643|2025-11-26|NSDK-585 카메라 이동 시 현위치가 움직이지 않는 이슈 수정
b1ec0209|2025-11-25|NSDK-585 boundsAnimatedCamera 구현
372946f5|2025-11-25|NSDK-585 지도 패딩 로직 추가
967666c9|2025-11-24|NSDK-585 getMapAsync 동기화 이슈로 인해 CopyOnWriteArrayList 자체 구현 (자바에서 제공하는 Class)
fe81ad93|2025-11-24|NSDK-585 SetZoomLevel 구현
d814fb17|2025-11-24|NSDK-585 ZoomIn, ZoomOut 구현
b7813d4f|2025-11-24|버전 업데이트 (0.1.14 -> 0.1.15, 22 -> 23)
aa73f3d8|2025-11-24|버전코드 업데이트 (0.1.13 -> 0.1.14 , 21 -> 22)
9da380c0|2025-11-21|NSDK-585 cameraViewModel 로직 구현
8e9784af|2025-11-21|NSDK-585 AnimateCamera 로직 구현, altitude 값 세팅하는 로직 추가
75b7bb31|2025-11-21|NSDK-585 MoveCamera 동작 구현
9c956acd|2025-11-20|NSDK-585 CameraController 연결 및 CameraPosition 구현
c6f44377|2025-11-20|NSDK-584 아이콘 표출안되는 문제 수정
17e6350e|2025-11-19|NSDK-584 마커 생성 시 전달하는 크기 값 제거 (원본 이미지 크기로 세팅)
bceef7c7|2025-11-19|NSDK-584 마커 전체 삭제 로직 추가
9cc24245|2025-11-19|NSDK-584 마커 추가 및 삭제 로직 연결
475a1fd6|2025-11-19|NSDK-584 마커 이미지 추가 로직 개선
d2a5d01a|2025-11-19|NSDK-584 지도 이동 시 손가락을 떼고 난 후 감속도 반응이 Android와 달라, 비슷하게 임시 적용
5d347c2f|2025-11-19|NSDK-584 마커 추가 로직 구현
b64c95fe|2025-11-17|NSDK-574 iOS TrackingMode 세팅 로직 추가
49b8c79e|2025-11-17|NSDK-574 기존 TrackingMode 함수 리팩토링
8857f224|2025-11-17|NSDK-574 현위치 아이콘 위치가 맞지 않는 문제가 있어 수정 (frame 값 재설정)
41f52415|2025-11-17|NSDK-574 Custom UserLocationManager 구현
ea6f68b7|2025-11-14|NSDK-574 UserLocationAnnotationView 생성, 현위치 아이콘 변경 적용
7a343c85|2025-11-14|[iOS] Import 누락된 부분 추가
27d01a86|2025-11-14|NSDK-586 사용자 제스처 판단 로직 변경
a5a53b33|2025-11-13|NSDK-586 지도 이동 Gesture 처리 로직 수정
dcff711e|2025-11-13|NSDK-586 불필요한 Scope 제거
85c9abb6|2025-11-12|NSDK-586 Listener 연동 작업 진행 (MapClick, LongClick, MapMove)
335a75a1|2025-11-12|NSDK-586 지도 클릭 및 롱클릭에 대한 처리를 하는 Handler 구현
2bcc3007|2025-11-11|NSDK-586 UIController 내부로직 구현
1783b0bb|2025-11-11|NSDK-586 MapController는 DI 주입을 받아서 사용 할 수 있도록 변경
692b0b11|2025-11-11|NSDK-575 getMapAsync 호출은 항상 MainScope에서 동작 할 수 있도록 변경
3f6340cb|2025-11-11|NSDK-575 지도 초기화 플래그 추가
e4a85ac1|2025-11-11|NSDK-575 DelegateProtocol 구현을 위해 클래스 생성, Maps 모듈 Export 추가
b32b52a1|2025-11-10|NSDK-575 지도 표출을 위한 InvMapFragment 구현, SampleApp 지도 표출 로직 추가
ee041109|2025-11-07|NSDK-573 방향성 탐색 추가 (목적지 방향성 옵션은 항상 적용, 출발지는 재 탐색시에만 적용)
2dc0cc14|2025-11-07|NSDK-573 Model 서브 모듈 업데이트
94c7916f|2025-11-07|NSDK-569 Model 서브 모듈 업데이트
40af3e47|2025-11-07|NSDK-569 OrbisGuidance 싱글톤 객체 생성 실패하는 문제 수정
7fbc6a82|2025-11-07|NSDK-569 Network ResponseBody gzip 처리 원복
84220af3|2025-11-07|경로 정보 내 리스트 아이콘 대응 (터널, 회전교차로)
53b2ac57|2025-11-07|이미지 리소스 추가 251105
f7ee95dd|2025-11-06|NSDK-569 IOS Network 응답 시 content-Encoding 값이 gzip으로 응답받아 String을 못 읽는 문제 수정
51ee83d3|2025-11-06|NSDK-569 OrbisMapMatcher TODO 구현체 제거
a84b51e3|2025-11-06|NSDK-569 IOS OrbisMapMatcher 주입 안되어있는 문제 수정
154e4abb|2025-11-06|NSDK-569 Android 빌드 안되는 문제 수정
b76a1141|2025-11-06|NSDK-569 Util Simul 빌드 제거
14bc21f1|2025-11-05|차기, 차차기 회전 교차로 이미지 추가, 전체경로 리스트 아이콘은 추후 이미지 전달 받으면 대응 진행
d7a9cb36|2025-11-05|Maps 서브모듈 내 Mapmatch 의존성 제거
08b7b27c|2025-11-05|차차기 TBT 목적지 아이콘 잘못 표출되는 부분 수정
8983ab79|2025-11-04|앱 초기 표출되는 프로그래스 문구 다국어 적용
55fe2869|2025-11-04|번역본 리소스 적용 v1.0
5863ef3d|2025-11-04|NSDK-566 Flavor 변수 제거, 사용하지 않는 필드 일부 제거
c9f28d10|2025-11-04|NSDK-566 국내향, 해외향 공용 UI Data 제거 (NaviTurnInfo, NaviCameraInfo 등)
f2d0dca0|2025-11-03|NSDK-566 필요없는 Data Class 전체 제거
cbb6ced5|2025-11-03|NSDK-566 MMCModule 내 함수 리팩토링
b8a9e708|2025-11-03|NSDK-566 불필요한 MMCInfo 변환 로직 전체 제거 (맵매칭에서 받은 데이터 그대로 사용)
8a3b76f2|2025-10-31|NSDK-566 국내향 Mapmatch 공용 IF 제거, MMCModule 필요없는 로직 제거
1a5b0e7e|2025-10-30|Android 배포 스크립트 수정, 변경된 의존성 수정
4bf85b81|2025-10-30|NSDK-565 소스정리
eea3bb67|2025-10-30|NSDK-565 국내향 MapMatch so 제거
3c75dae0|2025-10-30|NSDK-565 Core에서 사용한 엔진 전체 제거 (Bank, Smr, Vorbis, 국내향 Mapmatch)
3a1c86ee|2025-10-30|NSDK-565 Orbis Maps와 Inavi Maps를 관리하는 ProductFlavors 전체 제거
4dc22e49|2025-10-30|NSDK-565 Invai/orbis 서브모듈 로직 제거
c3e77950|2025-10-30|NSDK-565 Orbis 관련 로직을 -> Maps 서브모듈로 이관, Orbis 및 Inavi 서브모듈 삭제 (Maps 서브모듈이 이제 Orbis 모듈 역할을 진행)
71837fce|2025-10-30|NSDK-565 안내 모듈에서 사용하던 so 파일 삭제
6ccb0b8e|2025-10-30|NSDK-565 안내 서브모듈 내 국내향 로직 제거 및 연관된 영향 코드 정리 (Model은 나중에 전체 삭제 예정)
455a4711|2025-10-30|버전코드 업데이트 (0.1.12 -> 0.12.13, 20 -> 21)
cccd257c|2025-10-27|NSDK-563 경로 취소 시, 이전에 동작하던 경로 Animation 전체 취소. 재탐색 시 지나간 경로 Line 튀는 현상 수정
7e63f110|2025-10-27|NSDK-563 Style FullyLoaded 조건 추가, UpdateLineFeature WithContext 로직 제거
e3f82e00|2025-10-27|NSDK-563 Arrow FeatureCollection 생성 로직 Factory로 이동
a0aa62d0|2025-10-24|NSDK-563 Route Layer 관련 공통 로직 Factory로 이동
37735b5e|2025-10-24|NSDK-563 RemoveRoutes 함수 내 GetStyle 호출이 많아 개선
e86bc7ae|2025-10-22|버전코드 업데이트 (0.1.10 -> 0.1.11, 18 -> 19)
bad46a39|2025-10-22|LastGPS 저장 시 좌표 데이터 유효성 검사 로직 추가
0027c0bb|2025-10-20|NSDK-560 동작 확인을 위해 Utils 서브 모듈 난독화 일부 처리
2848aa29|2025-10-17|버전코드 업데이트 (0.1.9 -> 0.1.10, 17 -> 18), 타임락 변수 수정
23e67116|2025-10-16|버전코드 업데이트 (0.1.8 -> 0.1.9, 16 -> 17)
60029715|2025-10-16|LastGPS 저장 진행 시 Valid 조건 보지 않도록 수정
7fbeac1c|2025-10-16|과속 속도 표출 이미지 5단위로 추가
a69cbcbb|2025-10-16|이미지 리소스 추가 (251016B)
1b1769e7|2025-10-16|버전코드 업데이트 (0.1.7 -> 0.1.8, 15 -> 16)
bc55b9a2|2025-10-15|[AOS] 경로선택 목적지 표출 사양 제거로 인해 리스트 상시 표출
05733553|2025-10-14|[공통] 초기 좌표 세팅 로직 수정 (lastGps가 존재하는 경우 해당 좌표로 세팅, 만약 없는 경우에는 Default 좌표 세팅)
5e319cd0|2025-10-14|NSDK-552 중첩 Post 제거, ZoomToFit Padding 값 일부 수정
7fd382d8|2025-10-14|NSDK-552 경로 선택에 따른 경로선 색상 변경 추가
9d637a94|2025-10-13|NSDK-552 경로선택 목적지 부근 표출 사양 제거 및 탐색 결과에 대한 경로선 전체 표출
c8139028|2025-10-13|NSKD-553 주행 지도 초기화 시, 초기 좌표를 이용하여 카메라 이동
e1f5011e|2025-10-13|경유지 추가 후 전체경로 진입 시 목적지 명이 경유지로 표출되는 문제 수정
2df579f2|2025-10-13|NSDK-550 ReverseGeocode Wrapper 클래스 구현 및 대응
facedcf2|2025-10-13|NSDK-550 Wrapper 클래스 사용 및 내부 필드는 기존 값으로 유지
d7755930|2025-10-02|NSDK-550 Geocode Response Wrapper 클래스 생성
735a1029|2025-10-02|NSDK-545 RoutePtItem내 POI 중앙 좌표도 같이 저장 할 수 있도록 필드 추가
373edbf7|2025-10-01|NSDK-545 임시 Push
67ff0b45|2025-10-01|NSDK-545 RoutePtItem 내 address 필드 추가
46dc4622|2025-10-01|NSDK-545 안내시작 후 경유지 추가를 통해 모의주행 시, 기존경로 삭제를 알려주는 팝업 표출
9f31e726|2025-10-01|NSDK-545 누락된 다국어 Xml 적용
430784b2|2025-10-01|NSDK-545 모의주행 경로취소 다국어 적용
5383a96b|2025-10-01|서브모듈 업데이트
2b568db4|2025-10-01|NSDK-545 전체경로는 목적지 Item이 필요하여 예외처리 진행
9dd8e9c7|2025-10-01|NSDK-545 안내 시작 후 경유지 추가를 이용하여 모의주행 진행 시, 처음 안내 시작 한 경로로 모의주행되는 문제 수정
709fe387|2025-09-30|NSDK-545 안내 상태 변경되는 문제가 있어 수정
051ae13b|2025-09-30|NSDK-545 GUI 가이드 일부 적용, 전체 경로 진입 시 RunGuidance 로직 동작하지 않도록 변경
11af1311|2025-09-30|NSDK-545 이미지 리소스 추가 250930B
9fd83ad5|2025-09-30|NSDK-545 GUI 가이드 적용
118209ba|2025-09-30|NSDK-545 이미지 리소스 추가 250930
a67c0ee9|2025-09-30|NSDK-545 RouteID 기반으로 탐색 데이터 가져올 수 있도록 변경
1b32894b|2025-09-30|NSDK-545 모의주행 시 메인화면으로 안넘어가는 문제 수정
2ffcee5f|2025-09-30|NSDK-545 경로 선택 Title 및 주소 잘리는 이슈 수정
cfb5732a|2025-09-30|NSDK-545 경로선택 화면에서는 RouteStore에서 탐색 요청 진행, 경유지 추가 진행 시 전체경로 닫힘 처리 추가
86deec21|2025-09-30|NSDK-545 재탐색 진행 시에도 경유지 요청 같이 할 수 있도록 변경
cb42505d|2025-09-30|NSDK-545 경유지 요청 로직 추가
b602caa7|2025-09-30|탐색 결과를 Json 형태의 문자열로 변환하여 OrbisRouteInfo 내 필드로 추가, 내부 RouteFilePath에 저장
9ec43c20|2025-09-29|버전 코드 업데이트 (0.1.6 -> 0.1.7, 14 -> 15)
106b026a|2025-09-29|교통정보 토글 버튼 추가 및 동작하도록 수정
d14042b4|2025-09-29|버전코드 업데이트 (0.1.5 -> 0.1.6, 13 -> 14), 대만향 빌드를 위해 플래그 값 수정
517278a1|2025-09-29|한국향 빌드를 위해 플래그 값 수정
d166c834|2025-09-29|버전 업데이트 (0.1.4 -> 0.1.5, 12 -> 13)
9060830e|2025-09-29|NSDK-545 경유지 추가 버튼 클릭 시 검색 및 길찾기 이동 시나리오 추가
e8c8e7be|2025-09-26|최신 서브모듈 적용
1e4aca45|2025-09-26|NSDK-545 안내 데이터 생성 시, 경유지명으로 표출되도록 변경
77a78674|2025-09-26|요청 타임아웃 시간 수정
2b6e4ca4|2025-09-25|도로명 정보가 빈값인 경우도 존재하여 해당 부분 예외처리 진행
9eecabbc|2025-09-25|Orientation 잘못 적용된 부분 수정
7e7d23d6|2025-09-25|전체 Activity 세로모드 고정 적용
ef1ffe46|2025-09-25|인증 요청 시, Android ID의 UUID 고유 값으로 세팅
1dd981a9|2025-09-25|모의주행시 목적지 마커 표출안되는 문제 수정
35439b09|2025-09-25|전체경로 화면에서는 PagerSnapHelper 사용하지 않도록 수정
14aac8a3|2025-09-25|경로 선택 화면 진입 시 중첩 애니메이션으로 인하여 현위치 표출이 이상하게 되는 부분 수정
78b4b339|2025-09-25|인증 실패, App Key Error 결과코드 대응
47a22c8f|2025-09-25|Agent 에러 코드 정의
18688309|2025-09-25|앱 실행할 때마다 개발자 모드가 해제되는 문제 수정
e51780ad|2025-09-24|NSDK-540 소스정리
8d3b7c62|2025-09-24|NSDK-540 서브모듈 최신화
7179475e|2025-09-24|NSDK-540 경로 선택에서 RouteFile을 쓰고있지 않아, 모의주행 시작 시 Write 하도록 변경
fd510822|2025-09-24|NSDK-540 모의주행 동작 로직 개선 (모의주행 초기 세팅 및 시작/중지 로직 분리)
21a9936a|2025-09-24|NSDK-540 다중경로 API 요청 시 Progress 표출
8c4a01ca|2025-09-24|NSDK-540 Event 처리는 ViewModel로 위임
705cba10|2025-09-24|Sample App에서 앱 만료 상태 판단하는 로직 주석 처리 진행
cf0e3f30|2025-09-24|NSDK-540 UI 갱신 시 기존 경로선 및 마커 삭제
d380024e|2025-09-24|NSDK-540 List 형태로 전달받은 다중 경로 데이터 UI 에 표출
042aca51|2025-09-24|NSDK-540 다중 경로 데이터 구성 시 GetDataLink 이슈로 인해 GuidanceAdapter 일부 개선
65f23896|2025-09-24|안내 종료 팝업은 뒤로가기 버튼 허용
041f8878|2025-09-24|공통 팝업에 뒤로가기 버튼 동작 활성/비활성 플래그 추가
6d414f93|2025-09-24|인증 API 요청 시 uniqueKey세팅
5c660769|2025-09-23|버전코드 업데이트 ("0.1.3" -> "0.1.4", 11 -> 12)
a317c6ce|2025-09-23|NSDK-540 재탐색은 경로 결과 요청을 하나만 하도록 변경
3d574a10|2025-09-23|NSDK-540 다중 경로 탐색 리스트를 이용하여 리스트 형태의 구조로 변경
ec9a6308|2025-09-23|NSDK-540 다중경로 API 연동
a4c73d74|2025-09-23|NSDK-540 테스트를 위해 서브모듈 다중 경로 탐색 브랜치로 이동
6a2b6b73|2025-09-23|NSDK-537 경로 순서에 따라 다중경로 Icon 표출
3a2d6235|2025-09-23|NSDK-537 이미지 리소스 적용 250923
b8c0be85|2025-09-23|NSDK-537 GUI 가이드 일부 적용, 소스정리
d0692293|2025-09-23|NSDK-498 ReverseGeocode 에러 코드 추가
de1bc382|2025-09-23|NSDK-498 Tomtom ReverseGeocoding, NaviSDK API로 처리
eb60b362|2025-09-22|NSDK-498 Tomtom Geocoding, NaviSDK API로 처리
11bfeb60|2025-09-22|NSDK-542 TTS Mute 조건 추가
0163bade|2025-09-22|NSDK-542 Config 타입에 따라 볼륨버튼 이미지 변경하도록 수정
a9cf4ad2|2025-09-22|NSDK-542 ButtonType 및 ConfigType 추가
643ef36f|2025-09-22|NSDK-522 기존 인증 요청 객체 제거
3a626092|2025-09-22|NSDK-522 응답받은 AccessToken 값을, Authorization Header 값으로 사용하도록 변경
e1b35d2b|2025-09-22|NSDK-522 공용 인증키로 변경
d7e6ac29|2025-09-22|NSDK-522 기존 IMPS 요청로직 제거
4dbdefd6|2025-09-22|NSDK-522 Usecase 부분 요청 로직 변경
35489ade|2025-09-22|NSDK-522 Agent를 통하여 Auth API 요청하도록 변경 (IMPS 인증 및 JWT 토큰 생성)
79901256|2025-09-22|Unreachable code 에러 수정
8f932710|2025-09-19|NSDK-537 가로모드에서 세로모드 진입 시 Item 간격 안맞는 이슈 수정
38272e69|2025-09-19|NSDK-537 뒤로가기 동작 할 수 있도록 변경
b8480e4f|2025-09-19|NSDK-537 전체경로 시 ZoomToFit 동작하도록 변경
ed10c1b2|2025-09-18|NSDK-537 임시 Push
c8b57de0|2025-09-18|하단 메뉴 버튼 활성화를 위해, Dev 모드 플래그 추가 및 활성화 로직 추가
0343b061|2025-09-18|버전코드 업데이트 (0.1.2 -> 0.1.3, 10 -> 11)
75859d87|2025-09-18|하단 기능 표출하지 않도록 수정
19186cfa|2025-09-18|APP 타임락 날짜 수정
4b1818ef|2025-09-18|지도 다운로드 및 엔진 초기화 문구 중국 번체로 임시 변경 및 텍스트 컬러 변경
31dc3b8e|2025-09-18|데모앱 빌드를 위해 대만향으로 변경
4f6a81e4|2025-09-18|NSDK-473 모의 주행 조건도 제거
8b1753df|2025-09-18|NSDK-473 속도 값 갱신 안되는 이슈로, CurrentPosition 업데이트 시 gpsStatus 판단 로직 제거
091b94b5|2025-09-18|NSDK-473 MMC lib 삭제
bb960a7f|2025-09-18|NSDK-473 MMC Engine update (0.5.5)
38b45a87|2025-09-17|SDK 버전 업데이트
88c9bd67|2025-09-17|ETA 남은시간, 재탐색, 메뉴 버튼 영역 개선
4bf957d2|2025-09-16|NSDK-537 경로 선택 화면 다중 경로 표출을 위하여 중첩 RecyclerView 구조로 변경
10d27ccc|2025-09-16|버전코드 업데이트 ("0.1.1" -> "0.1.2" , 9 -> 10)
36109f4d|2025-09-16|NSDK-536 경로선택 화면 백그라운드에서 포그라운드 진입 시 UI 업데이트 하지 않도록 변경
4bfabfe0|2025-09-15|NSDK-536 loadKoinModule을 통해 의존성 모듈 추가 시, 백그라운드에서 포그라운드 진입 시 타이밍 이슈 존재하여 수정
cfb98a54|2025-09-15|NSDK-536 소스 정리
16b2fe0c|2025-09-15|AIR-536 경로 추가 시, 동일한 Source 및 Layer가 존재하는 경우 추가하지 않도록 예외처리 진행
1683d148|2025-09-12|NSDK-534 속도별 레벨 조정 값 일부 수정
d81173a5|2025-09-12|NSDK-534 속도별 레벨 조정 시 세팅하는 값 Int에서 Double로 변경
2e23129a|2025-09-11|NSDK-534 주행 지도 레벨 조정 (구글 기반)
790d709c|2025-09-11|[공통] 재탐색 발성로직을 TTSUseCase 내부로 이동
023e40ae|2025-09-11|NSDK-531 EtaDisplayMode 모드를 추가하여 도착예정 시간을 해당 모드에 맞게 계산 할 수 있도록 변경
6cb1168c|2025-09-11|NSDK-531 경로취소 버튼 클릭 시 팝업 추가
83a6eb0c|2025-09-11|[AOS] 다크모드에서 흰 배경 표출되는 문제 수정
3eacbbb8|2025-09-10|[AOS] 초기화 실패 시 팝업 추가
feb3e649|2025-09-10|버전코드 업데이트 (8 -> 9)
c4467934|2025-09-10|경유지 거리 계산 개선 부분 적용
fc28e238|2025-09-10|버전코드 업데이트 (0.1.0 -> 0.1.1 , 7 -> 8)
9b786e63|2025-09-10|하단 버튼 임시 활성화
cab3ba11|2025-09-10|공통] 서브모듈 최신화
298a5869|2025-09-09|NSDK-527 경로 재탐색, 이탈 시 시 TTS 발성
e6f4c10f|2025-09-09|NSDK-527 소스 정리
fa77f480|2025-09-09|NSDK-527 TTS 발성 로직 변경 (마지막 요청으로 계속 덮어쓰고, 직렬 실행 방식)
781f9a80|2025-09-09|NSDK-527 재탐색 버튼 클릭 시 애니메이션 추가
43f2e887|2025-09-09|메인화면에서도 뷰모드 동작하도록 변경
77fb238b|2025-09-08|지도 이동 후 뷰모드 변경 버튼 동작 안되는 문제 수정
0803dd46|2025-09-08|초기 지도 데이터 다운로드 및 엔진 초기화 사용자 안내 UI 추가
8e23f233|2025-09-05|NSDK-527 앱 실행 시 아이콘 뒤에 흰 배경 표시되는 이슈 수정
83f74d31|2025-09-05|NSDK-526 지난 카메라 조건 체크 후, 안전운행 종료 효과음 발성
be68a7e7|2025-09-05|NSDK-526 특정 타이밍에 따라서 시간 오차가 약간 있어 수정
4feb3881|2025-09-04|NSDK-526 runGuidance 주기가 1초 이상이라, 효과음 타임 체크 시 1초도 포함되도록 수정
6d99f401|2025-09-04|NSDK-526 카메라 효과음 관련 Usecase 추가, 과속인 경우 과속 효과음 발성
106b10ff|2025-09-04|NSDK-524 효과음 소리가 커서, 임시로 낮게 설정
010db8c2|2025-09-04|NSDK-524 소스 정리
7d6a1db2|2025-09-04|NSDK-524 효과음 발성 조건 추가
72c18df1|2025-09-04|NSDK-524 Wave 파일 일부 추가,  AudioService 초기화 진행 시 정의된 효과음 전체 로드하도록 변경
2d59a1ad|2025-09-04|NSDK-524 과속 효과음 ogg에서 wave 파일로 변경
28d1dfeb|2025-09-04|NSDK-524 SoundPool을 이용한 효과음 발성 로직 임시 구현
d7c909a9|2025-09-03|NSDK-524 공용 오디오 I/F 추가
3f9847f5|2025-09-03|기존 TTS 모듈에서 사용하던 패키지 중 안맞는 부분 수정 (Android, IOS)
75762778|2025-09-03|tts 모듈명을 media로 변경
f6b6c9d2|2025-09-03|NSDK-516 경로 탐색 서비스 데이터 오픈 실패 케이스 추가
a6de5bcc|2025-09-03|NSDK-516 초기화 실패 반환을 위해 Coroutine Scope 리팩토링 진행
fef709f6|2025-09-02|NSDK-516 지도 다운로드 관련 실패 케이스 처리
82139087|2025-09-02|NSDK-516 ServiceGate 데이터 파싱 에러 추가
f694257d|2025-09-02|NSDK-516 공통 데이터 모듈 변경된 클래스로 수정
4f62279f|2025-09-02|NSDK-516 ResourceString -> getLocalString 변경된 함수명으로 수정
ac9a6485|2025-09-02|검색 요청 시, 현재 디바이스 언어 타입에 따라 language 세팅하도록 변경
64d13656|2025-09-02|대만향은, 언어별로 스타일 세팅 하도록 변경
4fd47cf7|2025-09-02|NSDK-516 지도 다운로드 요청 일부 실패 케이스 처리
a52589b6|2025-08-29|NSDK-516 SDK Auth 인증 요청 관련 실패 케이스 처리
2aae67a2|2025-08-29|NSDK-516 초기 시나리오에서 사용하는 ResultEvent 구현
7a6dc7ac|2025-08-29|NSDK-516 Exception 순서 변경
3fda2d3e|2025-08-29|NSDK-516 초기 권한 요청 관련 실패 케이스 처리
eb74ad10|2025-08-28|NSDK-515 경로선택 에러팝업 버튼 클릭 시 액티비티 종료
11f570d2|2025-08-28|NSDK-515 경로선택 화면에서 에러 응답 시 팝업 표출 로직 구현, 에러는 하드코딩 값을 사용
74caff52|2025-08-28|NSDK-515 Common에서 String 값을 전달 받기 위해 함수 구현
455b6b47|2025-08-28|지도 Style Url 변경 (개인 Dropbox -> cdn)
8e2c9f29|2025-08-28|팝업 마진 일부 수정
6a921363|2025-08-28|NSDK-513 버튼이 하나만 존재하는 경우, 색상 변경 필요
07f4d08d|2025-08-28|NSDK-513 팝업 Title 제거
b7787888|2025-08-28|리소스 적용 (250828)
059a2728|2025-08-28|NSDK-513 팝업 버튼에 리플 적용
e9b5936b|2025-08-28|NSDK-513 사용 예시 추가
d65c8df7|2025-08-28|NSDK-513 Builder 형태로 팝업 표출 할 수 있도록 구현
08ba6ae6|2025-08-28|NSDK-513 커스텀 팝업 GUI 구현
8d0ae91a|2025-08-28|NSDK-509 Volume Mute 상태에서는 TTS 발성 안되도록 변경
cc40c9b2|2025-08-28|NSDK-509 볼륨버튼 효과음만 제거, 음소거 관련 ConfigKey 정의 및 세팅
fb9c926d|2025-08-27|기존 Style Layer 제거되면서 LayerBelow 다시 처리 진행
f651982c|2025-08-27|2차 개선된 지도 Style 적용
6594c572|2025-08-27|[공통] 실패 ErrorCode 정의
c9d55eb6|2025-08-26|공통 에러 코드 정의
31c111c3|2025-08-25|NSDK-509 TTSService DI 주입 방식 변경
1711dfb9|2025-08-25|NSDK-489 필요없는 Data class 제외, 일부 상태들 주석 적용
77bff77e|2025-08-22|NSDK-489 필요없는 model 제외
977c90c4|2025-08-22|NSDK-489 NaviUIController 문서화 진행
89ca525d|2025-08-21|버전코드 업데이트 (5 -> 6)
e8332cd1|2025-08-21|VaildMMC 플래그 값 True 하드코딩
201f1b31|2025-08-21|NSDK-489 Navisdk UI 모듈은 NaviUICOntroller만 문서화 되도록 변경 및 문서상 navisdk-aos-ui 모듈명이 이상하여 ui로 변경
1e6cdcd3|2025-08-21|NSDK-489 Navisdk Core 모듈은 NaviController만 문서화 되도록 변경
8525a0a7|2025-08-21|한국지도 앱 발행 위한 버전코드 업데이트 (4 -> 5)
05ce8225|2025-08-21|검색, 경로선택, 전체경로 화면 꺼짐 방지 추가
66ba4fd8|2025-08-21|UIGuideData Default 속도 값이 null이라, 재탐색 시 MapLevel 확대되는 문제 수정
4a01bdbc|2025-08-21|하단 메뉴 기능 임시 제거
68abdd73|2025-08-21|버튼 기능 중 Wrtie Log 4,5는 한국 로그 데이터로 다운받도록 수정
d69e4427|2025-08-21|화면 회전 시 액티비티 재 생성되는 문제로 인해, 모든 화면에 ConfigChanges 속성 추가
d56bf37c|2025-08-21|[공통] DataStore CurrentCountry 값에 따라, 지도 Style, routeUrl, tomtom BaseUrl 등 분기 처리 진행
74a0a5ea|2025-08-21|[공통] Header Country 값은 DataStore의 currentCountry로 변경
62a2caa3|2025-08-21|[공통] Appversion 세팅 값 원복, Header Country 값은 DataStore의 currentCountry로 변경
a7da91ba|2025-08-21|[공통] DataStore의 CurrentCountry 변수를 companion object로 이동
b52ed35f|2025-08-19|NSDK-489 Maps 관련 일부 주석 수정 (오타 및 동기화)
7e28c9f4|2025-08-19|NSDK-489 Maps 관련, 문서에 노출 할 필요없는 Class 및 함수 제거
9e47fb3a|2025-08-19|NSDK-489 지도 컨트롤 인터페이스에 관한 kdoc 주석 설명 추가
b4759f99|2025-08-14|NSDK-489 일반지도 (MapFragment)에 관한 주석 설명 추가
ecfb4c40|2025-08-13|VersionCode 업데이트 (3 -> 4)
25b33316|2025-08-13|VersionCode 업데이트 (3 -> 4)
5c1ec803|2025-08-13|경로 추가 시 같은 MapRouteOption ID인 경우 추가하지 않도록 예외 처리
759eed36|2025-08-13|NSDK-495 주행용 지도 컨트롤에 필요없는 API 제거
68ac8d49|2025-08-13|테스트 로직 제거
ce04a159|2025-08-12|NSDK-495 경로선 색상 변경하는 함수 추가
7b9465cb|2025-08-12|NSDK-495 특정 UI 컴포넌트 숨김 설정하는 함수 추가
1e723f8b|2025-08-12|NSDK-495 지도 컨트롤 미구현 기능 일부 추가 (Map level 및 제어 관련 기능 등 )
2c45b3cc|2025-08-11|NSDK-495 지도 컨트롤 미구현 기능 일부 추가 (MapIcon, ZoomToFit)
76810ac3|2025-08-11|NSDK-491 MapFragment 분리 (주행용은 InvMapFragment, 일반 지도는 MapFragment)
204c2a3b|2025-08-11|NSDK-491 마커 추가 시, FileName 전달 방식과 ResID 전달 방식 지원하도록 추가
e2e51b7f|2025-08-11|NSDK-491 Common용 MapFragment 생성, 각 플랫폼에서 MapController 인터페이스를 이용하여 구현체 구현
eee59e19|2025-08-11|NSDK-491 MapIF 주입 받는 곳이 없어 Module 로드가 안되는 문제 수정
9290317d|2025-08-11|NSDK-491 경로 선택 화면, 기존 MapIF 사용하는 부분에서 MapFragment로 변경
e80ce5fa|2025-08-11|NSDK-491 지도 제어 기능 공개용 인터페이스 생성, 기존 MapIF 에서 구현되었던 기능을 MapFragment 내부로 옮김
1bed22f4|2025-08-08|Tracking Mode 상태일때 ZoomLevel을 변경하는 API 추가
9582b854|2025-08-07|NSDK-491 지도 컨트롤 일부 API 추가
f0a58e50|2025-08-07|NSDK-491 NaviController 함수명 일부 수정
dc151f7a|2025-08-07|NSDK-491 프로퍼티 Scope 수정, Coroutine Scope 일부 수정
b731dd6b|2025-08-07|NSDK-491 NaviController 필요없는 함수 제거, Kdoc 주석 작업 일부 진행
3b31d32e|2025-08-07|NSDK-491 한 파일에 하나의 Inteface로 분리 진행
c4910758|2025-08-06|NSDK-491 NaviController에서 사용하는 Interface를 통합 관리하는 File 하나 생성
43cdff27|2025-08-05|버전코드 업데이트
c69a6993|2025-07-31|수동 앱별 언어 설정 구현
0621c3a9|2025-07-30|MapMatch aar 버전 변경
dc1bc5d3|2025-07-30|다국어 음성 템플릿 변경으로 인해, TTSText args 타입을 List 형태로 변경
fc6bcd13|2025-07-30|경로에서 사용하는 Layer의 Below Id 임시 수정
c022216e|2025-07-30|MapLibre MapStyle 변경
36e3b7b7|2025-07-29|주행더보기 시, UiGuideData 값이 들어올 때 마다 주행 View로 변경되는 문제가 있어 복귀 Timer 추가
3e649bdd|2025-07-29|Speed View Visibility 처리
1a2d9861|2025-07-29|NSDK-483 tts 음성 발화 시 AudioFocus 요청 및 완료 시 해제 로직 추가
9d26dd65|2025-07-28|NSDK-481 코드 개선
e696771d|2025-07-28|NSDK-481 Country 상태 추가, Config에 지도 정보 관련 정보를 List로 저장 할 수 있도록 변경
dfd436bd|2025-07-25|NSDK-481 지도 다운로드 관련, 변경된 Json 규격 대응
e926db04|2025-07-25|NSDK-480 이동식 카메라 관련 심볼 이미지 및 MapIcon 처리
9003a8c1|2025-07-25|NSDK-480 안전 운행 View 수정된 GUI 가이드 적용
bf7f3071|2025-07-24|이미지 리소스 추가 250724
6ea1630b|2025-07-24|NSDK-480 안전운행 심볼 이미지 가져올때,  OverSpeed 조건 적용
29c10f23|2025-07-23|Speed View 아래 안전운행 View 표시하도록 변경
ca337e5a|2025-07-18|경로 탐색 서버 연결정보 변경 (포트 [REMOVED])
237aff7c|2025-07-18|빌드 테스트 코드 추가
999abff2|2025-07-17|Assets에 로그주행 파일 5개 추가하여 내부 저장소에 Write하는 로직 추가 및 Main 테스트 로직 추가
8066d3ad|2025-07-17|TurnPoints 목적지 장소 없는 경우 Default 값 적용
a658acde|2025-07-17|경로 정보에서 사용하는 지점 Data Class 구현, 도착지 도로명 추가
78b5f020|2025-07-17|NSDK-471 Marker Type에 따라 크기 조절 할 수 있도록 변경
d10bc53c|2025-07-16|NSDK-471 카메라가 신호 과속 타입인 경우, 속도 이미지에 Top Margin을 적용하는 로직 추가
e12fe77a|2025-07-16|NSDK-471 CameraType에 따라 심볼 이미지를, 제한속도에 따라 속도 이미지를 가져오는 로직 추가
6eb2b95a|2025-07-16|NSDK-471 이미지 리소스 적용 250716
a91ecd6f|2025-07-16|NSDK-471 속도 표출 시 Unit 텍스트는 SizeSpan을 이용해서 크기 조절
e3acb39c|2025-07-16|NSDK-471 Marker 삭제 Interface 추가, 카메라 Map Icon 표출되도록 구현
d6d3afd2|2025-07-15|NSDK-471 SafeViewModel 생성, UI 연결 작업 진행
8fde599e|2025-07-15|NSDK-471 안전운행 GUI 구현
d104c300|2025-07-15|NSDK-466 Maps 모듈, Publish 설정 시 패키지 맞지 않는 부분 수정
407eff45|2025-07-11|NSDK-466 소스정리
96f4f9a6|2025-07-11|위치 권한 없는 경우 앱 초기 비정상 종료 수정
3ec264b6|2025-07-11|NSDK-466 Maps 모듈 DP aar 포함 안되는 문제 수정
b2eed093|2025-07-10|NSDK-466 빌드 에러 수정
a5b35e8f|2025-07-10|NSDK-466 Guidance, Core aar 배포 로직 추가
197ae49d|2025-07-10|NSDK-466 Maps, Maps Orbis aar 배포 로직 추가
3d9c392d|2025-07-10|NSDK-466 OrbisRoute, MapMatch(Module, AAR) aar 배포 로직 추가
d31602a4|2025-07-10|NSDK-466 Utils, TTS 모듈 aar 배포 로직 추가
7d74ebf7|2025-07-09|NSDK-466 Model 모듈 aar 배포 로직 추가
824ad0e5|2025-07-09|NSDK-468 지도 초기화 및 전달 타이밍 변경 (비동기 로직에서 동작하지 않도록)
2d7a042b|2025-07-07|NSDK-464 모의 주행에서 맵 이동 시 Compass View 안나오는 문제 수정
6bcd3d2b|2025-07-07|NSDK-464 Compass Resource 추가, 맵 버튼에 해당 이미지 적용
e935fe7c|2025-07-02|NSDK-464 MapLibre 내장 Compass View 적용, 나침반 북쪽을 향할 때 Fade 비활성화 되도록 변경
92597d3e|2025-07-01|현재 실행 중인 스레드 상태를 확인하기 위하여 ThreadName 함수 추가
947de1c2|2025-07-01|[AOS] Sample Apk 빌드 시, File Name 변경하도록 수정
1a232d9f|2025-07-01|빌드 에러 발생하는 라이브러리 제거
3ba06962|2025-06-26|위치 권한 허용 전 PositionManager를 사용하여 비정상 종료되는 이슈 수정
64f47ce9|2025-06-26|버전 업데이트 ("0.0.1",  2)
59522e7c|2025-06-25|NSDK-460 마커 전체 삭제 기능 추가 및 지도에 표출중인 전체 요소 제거하는 기능 추가
bb43209a|2025-06-25|NSDK-460 주행화면 출발지 마커 표출되도록 추가
f2f45e08|2025-06-25|경로선택 화면의 경로선 색상 Default 값으로 변경, MapRouteOptions의 필요없는 파라미터 제거
e90022e9|2025-06-25|지도 이동 시 자차 복귀 타이머가 초기화 되지 않는 이슈 수정
800616ba|2025-06-25|대만 일부 지역이 나오지 않아, 지도 Min Zoom 변경 (7.0 -> 6.0)
70c031a2|2025-06-25|지도 MinZoom, MaxZoom 설정 및 CameraController의 ZoomIn, ZoomOut 로직 일부 수정
b54d9413|2025-06-25|TrackingMode 변경 시 Bearing 0.0 값으로 변경하는 문제 수정
780ac444|2025-06-24|NSDK-458 경로선택 및 전체경로 진입 시, 목적지로 애니메이션 없는 카메라 이동 진행
fba06ea6|2025-06-24|NSDK-458 setMapCenter 함수에 Animated 파라미터 추가, 해당 플래그를 이용하여 애니메이션 카메라 이동 여부 확인
148cd6e1|2025-06-24|GuidanceState 값을 이용하여 TrackingMode 세팅하도록 변경
12fa0a27|2025-06-24|NSDK-455 주석 일부 수정, 사용하지 않는 TrackingMode Type 제거
d802f056|2025-06-24|맵 버튼 모의 주행 상태에서 안나오던 문제 수정
b943dd02|2025-06-24|Zoom In, Zoom Out 시 현위치 복귀 타이머가 갱신되도록 추가
583f5b9d|2025-06-24|NSDK-455 맵버튼을 이용하여 뷰모드 변경 시 TrackingMode 변경 할 수 있도록 구현
8568d01e|2025-06-24|NSDK-455 2D 고정형 및 회전형을 구현하기 위해, TrackingMode 타입 추가. Config 값을 이용하여 View 및 Padding 설정
a5c30f07|2025-06-23|NSDK-450 주행일때, 자차 패딩 값 일부 수정
d2cad0fc|2025-06-23|NSDK-450 소스 정리
a6920634|2025-06-23|NSDK-450 TrackingMode 변경에 따라 Padding 값 변경되도록 수정, RenderMode GPS로 변경
35b56a3e|2025-06-19|NSDK-450 CameraController에 ZoomIn, ZoomOut 구현, MapButton 동작하도록 주석 제거
c20800ed|2025-06-19|NSDK-450 빌드 에러 수정
c5621cdc|2025-06-19|NSDK-450 CameraController에 CameraPosition, CamerViewMode 추가 해당 로직을 이용하여 Tracking 하는 함수 구현
b95c8a22|2025-06-19|NSDK-450 플랫폼 Scale 값 받아올 수 있도록 DeviceInfo에 Scale 추가
6291f398|2025-06-19|NSDK-450 UIMode 변경에 따라 CameraMode 변경되도록 수정 (추후 TrackingMode 구현하여 변경할 예정)
7fd647c6|2025-06-19|NSDK-450 지도 제스처 처리를 위해 GestureController 추가, PanningListener를 MapMoveListener로 변경
f0aa7b52|2025-06-19|NSDK-450 TrackingMode 함수명 CameraMode로 변경, 해당 함수 사용하는 부분 전체 제거
dea5e72c|2025-06-18|NSDK-450 경로선택 화면에 Marker 표출
0a65205e|2025-06-18|NSDK-450 Location 활성화 로직을 분리하기 위해, InitLocationSetting 함수 추가
e3a9271a|2025-06-18|NSDK-450 LocationComponent의 forceUpdateLocation을 이용하여 모의주행 동작하도록 구현
8fa1f41b|2025-06-18|NSDK-450 현위치 테스트 마커 추가, LocationComponent 속성 세팅
ea795a8e|2025-06-17|지도 버전 관련 텍스트 파일을 Json 형태로 변경, OrbisMap 전용 ServiceGate로 사용하기 위해 ServiceGateForOrbis Data class 생성
013ce96f|2025-06-17|NSDK-450 LocationController에  CameraMode, RenderMode 기능 추가
c8088281|2025-06-17|NSDK-450 Camera 이동을 위해 MapCameraOptions 구현, 테스트 로직 추가
b920bcb8|2025-06-16|OrbisMapPath Index 파일의 첫번째 줄만 읽도록 예외 처리 진행
c696ee49|2025-06-16|OrbisMap 지도 데이터 저장 시 임시 Unzip 폴더에 파일 저장 후 OrbisMap 폴더로 Copy 하도록 변경
d6218619|2025-06-16|OrbisMap 지도 다운로드 로직 변경 (Index.txt의 경로 파일을 이용)
374beb3e|2025-06-16|NSDK-450 MapFeature -> MapShape 변경 (feature는 GeoJson 업데이트 용)
cf5205b1|2025-06-16|NSDK-450 TurfManager 추가
b01c529d|2025-06-13|NSDK-450 Marker 표출을 위해 MapMarkerOptions 구현 및 마커 추가, 제거 로직 구현
2c51972d|2025-06-13|NSDK-450 UISetting Visible 동작 안하는 부분 수정
bfbed030|2025-06-13|NSDK-450 경로 표출 및 현위치 관련 Controller 추가
0599e8cf|2025-06-13|NSDK-450 Map 상호작용을 위해 Controller 구현, 테스트 로직 추가
757a99da|2025-06-12|NSDK-450 MapLibre를 들고있는 MapFragment 구현, 기존에 사용하던 TomTom API 주석 처리
db97c250|2025-06-12|NSDK-450 MapLibre 의존성 라이브러리 추가
b95dc233|2025-06-09|NSDK-444 음성 발성 스크립트 테스트를 위하여 타입 및 Resource 매칭, 발성 테스트 로직 추가
9778cf6b|2025-06-09|NSDK-444 테스트 로직 추가
f287bcda|2025-06-04|NSDK-444 StringResource를 가공하여 Text String으로 전달받을 수 없어 Data class 생성
45bf5ebb|2025-05-29|NSDK-444 TTS 기본 동작 구현
ae471151|2025-05-29|NSDK-444 TTS 서브 모듈 생성, I/F 구현
ad2583c1|2025-05-26|필요없는 TBT Icon 리소스 제거
b080872d|2025-05-26|차기, 차차기 Turn Image 가져오는 로직 수정
7cf8f265|2025-05-26|이미지 리소스 적용 (250526)
de79b1b0|2025-05-26|OrbisMap 적용
400dc09d|2025-05-23|필요없는 App Icon 제거
096a9410|2025-05-23|Moko-resource에서 mipmap을 지원하지 않아서, 샘플앱에 앱 아이콘 추가
87abae99|2025-05-23|앱 명칭 변경
d4425c8f|2025-05-22|NSDK-436 OrbisStyle 지도 비활성화
f03dae70|2025-05-22|NSDK-436 NaviController에 MapIF 제거
3f4d3f9c|2025-05-22|경로선택 및 전체경로에서 Map Padding 적용 안되는 문제 수정
c63dac1d|2025-05-21|초기화 로직 순서 변경
2ed2e10c|2025-05-21|NSDK-436 MapIF는 Factory로 인스턴스 생성하도록 변경
dccf1a58|2025-05-20|NSDK-436 FeatureToggleController 호출을 위해 InitSetting 함수 생성
68100eda|2025-05-20|NSDK-436 Assets에 Orbis Street Light/Dark Style 추가, 해당 OrbisMap 적용
47fb0742|2025-05-20|NSDK-436 Feature-toggle 의존성 추가, TomTomOrbisMapFeature 활성화
f4f04723|2025-05-19|UiGuideData에 bExistRoute 값 세팅, 나침반 MapButton은 경로가 존재할때 표출하도록 변경
413ef8d0|2025-05-19|UIMode가 Normal일때 TrackingMode를 FOLLOW_NORTH_UP으로 변경
febcb5fb|2025-05-19|MapButton Zoom In, Zoom Out Duration 적용
40728dcd|2025-05-19|TomTom 초기화 로직 변경((지도 준비되면 콜백 먼저 전달하도록) 및 Progress Layout 추가
611e3e74|2025-05-15|필요없는 Test 로직 제거
febdb644|2025-05-15|자차 위치 패딩 변경 (300 -> 500)
ab40b515|2025-05-15|지도 다운로드 로직 추가 (Usecase),  OrbisRoute 엔진에 해당 Path 적용
eea79b68|2025-05-15|tomtomInitialize 로직 원복
e930c226|2025-05-15|지도 스트리밍 로직 임시 Push
88924f01|2025-05-14|빌드에러 수정
da1e24b9|2025-05-14|안내시작 동작 구현 및 MapModeListener 추가
febf0707|2025-05-14|현위치 버튼 동작 구현
d640c76e|2025-05-14|[공통] ZoomIn, ZoomOut 로직 변경 (CameraOptionsFactory.zoomIn)
7e0c5d00|2025-05-14|NSDK-425 소스 정리
8e8da621|2025-05-14|NSDK-425 Angle 값을 실시간으로 받아오기 힘들어서 CompassView는 TomTom API 사용
c0bebd0f|2025-05-13|NSDK-425 Volume Mode 추가 후 클릭에 따라 Mode 변경되도록 적용
5669c834|2025-05-13|NSDK-425 ButtonState와 View 연동 진행
72f66d74|2025-05-13|NSDK-425 ConfigManager 동작을 위해 구현체 추가
e7ae2ccd|2025-05-13|NSDK-425 각 Button Type에 따른 Visibility State 생성
1206b8da|2025-05-13|NSDK-425 Zoom In, Zoom Out 구현
66dcd434|2025-05-13|NSDK-425 현위치 이동 View 추가
b7ec60c8|2025-05-13|NSDK-425 TomTom 축적뷰, Compass 뷰 제거
179b5a41|2025-05-12|NSDK-425 MapButtonViewModel 추가, Component와 연결
134738da|2025-05-12|NSDK-425 ButtonType 추가, Layout View 임시 추가
7609f117|2025-05-09|OrbisRouteOption에 RouteColor 파라미터 추가 후 경로선택 화면은 초록색 경로선으로 표출되도록 변경 (ColorType Model 모듈로 이동)
d46265f4|2025-05-08|NSDK-419 차차기용 Visible State 생성, UIMode 및 Distance조건 추가하여 Visible 변경하는 예시 추가
bb22ef58|2025-05-08|NSDK-419 테스트 로직 원복
dff02f62|2025-05-08|NSDK-419 TurnCode 대응해야하는 부분 추가
68ae35ef|2025-05-08|NSDK-419 AppFlavor 기반 차기, 차차기 이미지 가져오는 로직 추가
a4ec6879|2025-05-08|NSDK-419 DataStore에 AppFlavor 추가
cd2d53ae|2025-05-08|NSDK-419 도로명 데이터가 없는 경우에는 View Gone 처리
bab70364|2025-05-08|NSDK-419 Orbis 차기, 차차기 TBT ViewModel 연동
9098e932|2025-05-08|NSDK-419 Orbis TurnView, NextTurnView GUI 가이드 적용
4e6682c5|2025-05-08|DataStore의 OrbisRouteInfo, SearchItem을 GuidanceStore로 이관
32ce5f05|2025-05-07|[공통] UIGuideData의 mapUIMode 주석 제거
a12e2550|2025-04-30|NSDK-419 Orbis TBT 구현을 위해 RootView 및 TurnView, NextTurnView 컴포넌트 추가
6301804e|2025-04-30|[AOS] 경로선택 플로팅 버튼 Ripple 적용
e33610ab|2025-04-30|NSDK-418 소스정리
956351ef|2025-04-30|NSDK-418 GPSModule, MMCModule, LocationProvider 관련 로직 MapMatch 모듈 내부로 이동
29ed6994|2025-04-30|NSDK-418 Natives MMC 엔진 인터페이스 이동
a98631c9|2025-04-30|NSDK-418 MapMatch 모듈 생성 및 초기화 로직 구현
b20c56c5|2025-04-29|NSDK-418 orbisroute 모듈 생성, 초기화, 인터페이스, So 엔진 전체 해당 모듈 내부로 이동
9ff0037d|2025-04-29|NSDK-418 InaviGuidance -> Guidance 모듈로 이동
d552a056|2025-04-29|NSDK-418 SGuidanceAdapter를 Guidance 모듈 내부로 이동
f5ec7cd7|2025-04-29|NSDK-418 so 엔진 Guidance 모듈로 이동, 초기화 로직도 내부로 이동
13579149|2025-04-28|NSDK-415 경로선택 TextView NotoSans 폰트 적용
923e5a11|2025-04-28|Noto Sans CJK 폰트 추가 (Regular, Medium, Bold)
edd5e440|2025-04-28|NSDK-415 경로 리스트 표출 중, 마지막 아이템이면 Divider를 숨기는 로직 추가
a3ffd826|2025-04-28|NSDK-415 Ripple Button 이미지 적용
dcc55fe3|2025-04-28|NSDK-415 Floating Button 이미지 리소스 적용
708edc0a|2025-04-28|이미지 리소스 적용 (250424)
887396fd|2025-04-25|NSDK-415 동작하지 않던 ZoomToFit 수정
1ea4c747|2025-04-25|NSDK-415 전체경로 테스트 로직 추가
670d8544|2025-04-25|AndroidManifest에 정의된 Activity 일부 이동
b02ca471|2025-04-25|NSDK-406 GUI 일부 로직 처리
4170577c|2025-04-25|NSDK-406 MokoResource Strings 작업 진행
93088756|2025-04-25|NSDK-406 Android Resource에 나인패치 이미지 추가 Background 적용
c1549f6c|2025-04-25|NSDK-406 MokoResource에서 나인패치 이미지 제거
af2e82fb|2025-04-25|이미지 리소스 추가 250424C
13720872|2025-04-25|NSDK-406 RouteViewModel에서 필요없는 로직 제거 및 Fragment 로직 정리
cbe48d5e|2025-04-24|NSDK-406 ViewModel과 RouteFragment 연결
a275adf6|2025-04-24|NSDK-406 소스정리
0c9c8467|2025-04-24|NSDK-406 Search, Route Activity 연결 로직 추가
d06c0444|2025-04-24|NSDK-406 소스정리
12f6274a|2025-04-24|NSDK-406 경로선택 GUI 일부 적용
c973995c|2025-04-24|NSDK-406 Develop Merge
9f468684|2025-04-24|Revert "NSDK-406 경로선택 GUI 일부 적용"
094e9f35|2025-04-24|NSDK-406 경로선택 GUI 일부 적용
6330d08b|2025-04-24|이미지 리소스 추가 250424
f213d6fb|2025-04-23|NSDK-406 일부 UI 작업 진행
2d93e46b|2025-04-22|NSDK-406 ProgressBar 추가 및 UI 동작을 위한 조건 수정
0ccc8aa4|2025-04-22|NSDK-406 AM,PM Format 타입 잘못 정의한 부분 수정
cf2c4625|2025-04-22|NSDK-406 도착시간을 문자열로 표시하는 로직 추가
cf514e79|2025-04-21|NSDK-406 소요시간 및 거리 표출 로직 일부 처리
4934229a|2025-04-21|NSDK-406 RouteStore, GuidanceStore 사용하여 화면 구성하도록 변경
c66baf2b|2025-04-21|NSDK-406 zoomToFit 함수 시그니쳐 변경(호출부에서 직접 패딩 값 설정하도록 변경)
8de924b1|2025-04-21|NSDK-406 경로선 표출 및 지도 패딩 설정
cb233b80|2025-04-18|NSDK-406 한 Fragment에서 경로탐색(선택) 및 전체경로 동작하도록 설계
e1f5b9e9|2025-04-18|NSDK-406 Activity 및 Fragment명 변경
158035bd|2025-04-18|NSDK-460 필요없는 로직 제거
18a79941|2025-04-18|NSDK-406 경로 상세 Recylcerview 구현
1903530f|2025-04-17|NSDK-406 임시 Push
658e7966|2025-04-17|NSDK-406 빌드 안되는 문제 수정 및 테스트 코드 추가
3c543dfe|2025-04-17|NSDK-406 경로 선택 UI 레이아웃 구조 구현
605a354e|2025-04-17|NSDK-406 ViewBinding 추가
31cd3790|2025-04-16|NSDK-406 경로선택 화면 UI 작업을 위해 Fragment 및 Activity 생성
5ed2a39a|2025-04-15|README 수정 (아티팩트 경로)
bb23e1a1|2025-04-15|airmaps.aar 파일 Maps 서브모듈 내부로 이동
b940de0e|2025-04-15|IosMain 부분 Package 변경된 부분 대응
ee0631f5|2025-04-15|Core manifest에 권한 로직 이동
3702e8d4|2025-04-15|Core CommonMain에 기존 로직 이동
763ba61a|2025-04-15|xcframework Build Script output 경로 변경
37caf4ea|2025-04-15|Navisdk-Core(Common) 로직을 Core 서브 모듈 내 전체 이동
2e6923b8|2025-04-15|SDK Project 파일명을 navisdk-core에서 navisdk로 변경
60140503|2025-04-14|소스 정리
38caab63|2025-04-14|Navisdk-Core 폴더명을 navisdk로 변경
08728079|2025-04-14|common 서브 모듈 , Core로 이름 변경
ff6e6800|2025-04-14|Airmaps aar 경로 변경 및 xcframework build output 경로 변경
1123f6d0|2025-04-11|Navisdk-core에 있던 로직 Common 서브모듈로 이동
0eb09138|2025-04-11|Common 서브 모듈 생성
fbc5ada7|2025-04-09|NSDK-400 Network 관련 Model 클래스들을 Model 서브 모듈로 이동
a7306649|2025-04-09|NSDK-400 Common에서 사용하고 있는 Model 클래스들을 Model 서브 모듈로 추가적으로 이동 (Guide)
3285e8eb|2025-04-09|NSDK-400 Common에서 사용하고 있는 Model 클래스들을 Model 서브 모듈로 추가적으로 이동 (Location)
97a6facf|2025-04-08|NSDK-400 Common에서 사용하고 있는 Model 클래스들을 Model 서브 모듈로 추가적으로 이동
ef44cca1|2025-04-08|NSDK-400 Common에서 사용하고 있는 Model 클래스들을 Model 서브 모듈로 일부 이동
5ca04b0a|2025-04-08|NSDK-400 Common에서 사용하는 Util 나머지 부분을 Util 서브 모듈로 이동
68cdd476|2025-04-08|NSDK-400 Common에서 사용하고 있는 Util 클래스 일부 Util 서브 모듈로 이동
ba5f7a4c|2025-04-08|NSDK-393 필요없는 파일 제거
3350eea9|2025-04-02|NSDK-393 소스 정리
efd41a24|2025-04-02|NSDK-393 필요없는 MapIF 함수 제거
983b4bd1|2025-04-01|NSDK-393 NaviMapViewAdapter 내부적으로 사용하는 로직 분리 진행
a1bb4f81|2025-04-01|NSDK-393 OrbisMap 초기화 시 현위치 마커 늦게 표출되는 문제 수정
10be92f7|2025-04-01|NSDK-393 MapIF 인터페이스 구성 시 OrbisMap, Inavi 구분 없이 사용 할 수 있도록 변경
76970c7c|2025-04-01|NSDK-393 Type 세팅 시 Enum 값으로 세팅하도록 변경
a0e90ed7|2025-03-28|NSDK-393 일부 필요한 Interface 추가
2eec7647|2025-03-28|NSDK-393 테스트를 위해 Flavor 별로 호출 분기 처리 진행
30b367cb|2025-03-28|NSDK-393 OrbisMap 전용 IF 추가 및 공통 함수 부분 구현
464268a5|2025-03-28|NSDK-393 SetMapCenter 함수 오버로딩
2dd27a24|2025-03-27|NSDK-393 임시 Push
8d1d4201|2025-03-27|NSDK-393 User Location 기능 추가 및 국내향 MMC을 이용하여 테스트 로직 추가
eb606a8d|2025-03-27|NSDK-393 OrbisMap Interface 로직 일부 구현
2af7289e|2025-03-27|NSDK-393 Map 모듈에서 편리하게 사용하기 위해, Scope 및 Component 구현
375baeaf|2025-03-27|NSDK-393 TomTomMap을 가져오기 위해서는 AppCompat 의존성이 필요 (Fragment)
d7ea13eb|2025-03-26|[공통] data class들 변경되지 않는 패키지명 수정
13818b5a|2025-03-26|[공통] common 영역에 있는 Data 일부 Model 모듈로 이동
316abe5c|2025-03-26|[공통] 버전 적용 안된 부분 추가로 적용
24e8ee91|2025-03-26|[공통] Min, Compile 버전 관리를 위해 변수 생성
e534cd4d|2025-03-26|[공통] 서브모듈에서 사용하는 의존성 정리
3db41ef5|2025-03-26|[공통] Common 모듈에 존재하는 Moko Resource 제거
c2ecd28f|2025-03-20|소스정리
673d0ae2|2025-03-20|Utils 모듈에 ConfigManager 및 FileManager 추가
2ad835a1|2025-03-20|model 모듈 생성, common 및 utils 모듈에 Model 모듈 추가
31227c41|2025-03-20|Common에서 Utils 모듈 참조하도록 변경
9673f398|2025-03-20|변경된 파일 이름 원복
e828c309|2025-03-20|Common -> Utils 서브모듈 이름 변경
bc3be34f|2025-03-20|필요없는 로직 제거
cead64d4|2025-03-20|NaviMapViewAdapter Class 패키지 수정 및 Common 모듈 추가
79bb0904|2025-03-20|Common, Util 서브 모듈 생성 및 Common 서브모듈에 필요한 Class 이동
ddb3bf5c|2025-03-19|테스트 로직 추가 (INaviMapIF, OrbisMapIF 2개로 진행 시)
2d66f2c4|2025-03-19|[AOS] tomtom SDK 추가
0e84c91f|2025-03-18|[공통] navisdk-core 내 maps 서브 모듈 생성
abbf5def|2025-03-18|[공통] 필요없는 로직 제거
59c637db|2025-03-18|[공통] Gradle Plugin 8.9 , Gradle 버전 8.11.1 업데이트 진행
23a67739|2025-03-18|[공통] Voice 관련 로직 제거
86d36ccd|2025-02-26|[공통] MMC 값 늦게 세팅되는 이슈 수정
53456875|2025-02-26|[공통] GPSModule requestLocation 함수 로직 중 잘못 사용하는 부분이 있어 수정
265f5e3e|2025-02-26|NSDK-357 ColorLaneView 표출 테스트를 위해 목적지 변경
c5c5e9aa|2025-02-26|NSDK-357 TBTView에 ColorLaneView 표출되도록 Observe 등록
84b75a69|2025-02-25|NSDK-357 ColorLane 표출을 위해 UiState 상태 파라미터 추가 및 비즈니스 로직 구현
94280d5e|2025-02-25|NSDK-357 안내엔진 초기화 시 Company 값 변경
7bb562fa|2025-02-25|NSDK-358 소스 정리
96c71dc7|2025-02-25|[공통] Moko-Resource Colors Format 상, Alpha 값은 맨 마지막에 추가
44397190|2025-02-25|[공용] Moko-Resources Colors 추가 및 경로선 파란색으로 변경
8eba1380|2025-02-21|NSDK-358 StringExtension 제거, Dist 변환 로직 DistanceParse 폴더로 변경
7971c4ec|2025-02-21|NSDK-358 Extension File에 확장함수 전체 정의하도록 변경
0efe2d84|2025-02-21|NSDK-358 String 관련 처리 로직은 Strings 파일 내 함수로 정의하도록 변경
cafad67f|2025-02-20|[공통] DP 인터페이스 구성에 빠진 부분 추가
e69fe762|2025-02-20|[공통] 검색 정규화에서 아이나비 LonLat 변환 시 값 오류 수정
c6a01068|2025-02-19|NSDK-357 ColorLaneView 상속 구조 제거
bc4cd5bc|2025-02-19|[AOS] Font 가져오는 부분 리팩토링
3a47f8db|2025-02-18|[공통] NaviController에서 사용하던 MapController 제거 후 NaviMapView로 통합 구현
0f839aca|2025-02-18|[AOS] MapComponent 상속 구조 제거
27af66d2|2025-02-17|NSDK-357 차기, 차차기 View에 ColorLaneView 추가
0e267d98|2025-02-17|NSDK-357 LaneColor 이미지 리소스 추가
385a78d4|2025-02-17|[AOS] 필요없는 이미지 리소스 제거
2ffa54e1|2025-02-17|[AOS] 필요없는 폰트 리소스 제거 및 moko resource로 가져온 font 세팅
47b30cfd|2025-02-17|NSDK-355 추후 컴포넌트 클릭 이벤트 처리를 바로 할 수 있도록 인터페이스 추가
f05dad87|2025-02-17|NSDK-355 필요없는 로직 정리
69648efc|2025-02-14|NSDK-355 차기, 차차기 TBT 모의주행 표출 테스트
ba382ad8|2025-02-14|NSDK-355 차차기 TBT UI 구현
c43f63ed|2025-02-14|NSDK-355 임시로 Font 추가하여 Custom TextView 테스트
34fec052|2025-02-14|NSDK-355 차기 TBT UI 구현
a972d079|2025-02-13|NSDK-355 NaviTextView Component 임시 구현
d22b9b4a|2025-02-13|NSDK-355 소스 정리
96c10a54|2025-02-13|NSDK-355 테스트를 위해 임시 TurnView 표출 로직 추가
4e68546c|2025-02-13|NSDK-355 Navisdk-aos-ui 앱모듈을 라이브러리 모듈로 변경, Playground 의존성에 navisdk-aos-ui 모듈 추가
eadb3ad6|2025-02-13|NSDK-346  안내 엔진 코드 추가 연동
31239afb|2025-02-13|NSDK-346 기존 안내 엔진 코드 일부 적용
2677f542|2025-02-13|NSDK-346 차기 차차기 데이터 확인 로직 추가
6f1c3be1|2025-02-11|NSDK-346 DummyGSV 값 수정
2f460343|2025-02-11|NSDK-346 UIGuideDataLogic에 TurnInfo 정보 업데이트 할 수 있도록 값 세팅
c5dc3af3|2025-02-11|NSDK-346 모의주행 시 Turn 정보 값 테스트로 받기 위해 임시 Push
4cff2260|2025-02-11|NSDK-346 헷갈리는 함수명 일부 변경
c0e7df70|2025-02-11|NSDK-346 안내 엔진 통합을 위해 Guidance 파일 생성 및 일부 초기화 로직 구현
8598d0c7|2025-01-23|[공통] 모의주행 스코프 Cancel 로직 제거
4ea990b4|2025-01-23|[공통] PermissionUsecase 소스 정리
6137d5e7|2025-01-23|[공통] 모의주행 종료 로직 변경 및 일부 예외처리 추가
55ca18ea|2025-01-22|NSDK-339 DI 특정 기능에 따라 모듈 분리 처리
1bc77ce8|2025-01-22|NSDK-337 ViewAngle Default 값 세팅
b358acf2|2025-01-22|NSDK-337 뒤로가기 버튼 클릭 시 Item View 제거
35d1b183|2025-01-22|NSDK-337 Intro 영역 추가
668d6470|2025-01-21|NSDK-337 모의주행 취소 로직 추가
e4d14979|2025-01-21|NSDK-337 테스트를 위해 일부 값 변경
d91d80e4|2025-01-21|NSDK-337 모의주행 시 지나온 경로선이 사라지지 않는 문제 수정
ce866d8e|2025-01-21|NSDK-337 AddRouteLine 테스트 로직 추가
4811aa2d|2025-01-21|NSDK-337 MMCInfo가 변경될 때 마다 MapCenter 및 SetCarPos 변경하는 로직 추가
1a82f890|2025-01-21|NSDK-337 NaviController 모의주행 테스트 로직 추가
17c43f96|2025-01-21|NSDK-336 DeviceInfo DI 주입 후 사용
1ccd831e|2025-01-21|NSDK-336 CheckDevice 처리를 위해, 각 OS에서 진행하던 부분을 Common에서 처리 할 수 있도록 변경
53d32333|2025-01-21|NSDK-336 requestLocationUpdates Dispatcher 이슈로 인해 UI 스레드로 호출하도록 변경
7cfe00c6|2025-01-21|NSDK-336 addNmeaListener 등록 시 Dispatcher 이슈로 인해 UI 스레드로 호출하도록 변경
3b99fcf9|2025-01-20|NSDK-336 ReopenLocation 진행 시 LocationManager를 Null로 세팅하여 이후 부터 동작하지 않는 문제 수정
19c47afe|2025-01-17|[공통] MMC Init 사양 Air와 동일하게 변경
c8cd384f|2025-01-17|[공통] GPSModule 누락된 조건 추가
b69ce107|2025-01-16|[공통] 테스트 프로세스 중 필요없는 부분 제거
3e34a74c|2025-01-16|[공통] MMC CheckDevice 판단 로직 구현
ab08eb27|2025-01-16|NSDK-329 일부 로직 Coroutine Dispatchers Main으로 실행
d59ea568|2025-01-15|NSDK-329 원인 분석을 위한 Log 추가
adcf14ea|2025-01-15|NSDK-314 NMEATask Dispatchers 변경
ccbc7089|2025-01-14|NSDK-314 MMCModule 통합 로직 구현
f02949b8|2025-01-14|NSDK-323 변수명 개선 및 필요없는 로직 제거
5de054da|2025-01-13|[공통] String.format 사용을 위해 Expect 함수 구현
e9692f4c|2025-01-13|NSDK-314 MapMatch 모듈 인터페이스 Common DI에 추가
e0f90a25|2025-01-13|NSDK-314 String.format 사용을 위해 Expect 함수 생성, Android 구현체 생성
71e9a0de|2025-01-13|NSDK-314 테스트 코드 원복
5523f26f|2025-01-13|NSDK-314 MMC Info Test 코드 추가
38904636|2025-01-10|NSDK-314 MMC 임시 테스트를 위해 Push
b4815ed3|2025-01-10|NSDK-314 소스정리
763188ca|2025-01-10|NSDK-314 atomicfu Library 사용하여 Synchronized 처리
4f048dbf|2025-01-10|NSDK-314 필요없는 클래스 제거, 디렉토리 분리
51f6b344|2025-01-09|NSDK-314 임시 Push
8272a91b|2025-01-09|NSDK-314 테스트용 코드 추가 및 LocationManager 추가 안된 부분 적용
3e24a314|2025-01-09|NSDK-323 공통 GPSModule 일부 로직 추가
65c65aa1|2025-01-09|NSDK-314 공통 MMCModule 일부 추가
9c2a9a45|2025-01-08|NSDK-322 필요없는 소스 정리 및 일부 클래스 분리
1e1295a6|2025-01-08|NSDK-322 GravityModule Kt 변환
63e953ab|2025-01-08|NSDK-314 GPSModule kt 파일로 변경
7df479d1|2025-01-07|NSDK-314 GravitySensorStatus Kt 변환
4bfbd446|2025-01-07|NSDK-314 MMCOptionManager kt 파일로 변경
c8529d4d|2025-01-07|NSDK-314 MMCSite Kt 파일로 변경
51f804f3|2025-01-07|NSDK-314 GPSModule 추가
9986a2e3|2025-01-07|NSDK-314 GravityModule 추가
f11b8f83|2025-01-07|NSDK-314 오류 발생하지 않는 MMCOptionManager, MMCSite 추가
1b027663|2025-01-07|NSDK-314 MMCOptionManager에 Gson 파싱 부분이 있어 Android Lib 추가
6370913f|2025-01-07|NSDK-314 Java에서 Kotlin Data 클래스로 변경되면서, 인스턴스를 바로 생성 할 수 없어 Default 값 추가
50735205|2025-01-02|NSDK-309 Android 폰트 가져오는 로직 추가 및 DP 세팅
b38f04e6|2025-01-02|NSDK-309 font 이름 변경 및 android 영역에서 commonMain의 Resource 사용을 위해 소스셋 추가
82548922|2025-01-02|[AOS] 사용하지 않는 App 삭제
b75904aa|2025-01-02|NSDK-309 DP 엔진 인터페이스 구현체 IOS와 동일하게 현행화 진행
e4405e33|2025-01-02|[공통] _MMCInfo 필요없는 파라미터 제거
867a9819|2024-12-30|NSDK-305 소스정리
b71e271f|2024-12-24|NSDK-305 RouteBuffer 파싱 로직 UseCase 구현하여 테스트 로직 수정
90f1de47|2024-12-24|NSDK-305 필요없는 로직 제거
311f69c8|2024-12-23|NSDK-305 RouteBuffer 세팅 Test Push
07d4f03e|2024-12-23|[공통] 코어 모듈이름 변경으로 인한 iosBuild 스크립트 수정
5c0b24c6|2024-12-23|[AOS] README 수정
3d8d2b13|2024-12-23|[공통] 모듈 네이밍 변경 ("navisdk_core" -> "navisdk-core", "navisdk_aos_ui" -> "navisdk-aos-ui", "androidsample" -> "aos-playground")
1ae1d6d6|2024-12-20|NSDK-304 NaviController 테스트 코드 추가 및 Sample 테스트 진행
e9f36075|2024-12-19|NSDK-304 샘플 Controller 임시 Push
fcfd853a|2024-12-19|NSDK-304 README 수정
05e49771|2024-12-19|NSDK-304 라이브러리 추가 안되는 부분 수정
792d1990|2024-12-19|NSDK-304 aar 빌드 테스트 중 오류 발생하는 부분 수정 (DeviceInfoObj)
9a52bea9|2024-12-18|NSDK-298 AndroidApp 구현 부분 제거 및 사용하지 않는 library 제거
1f388297|2024-12-18|NSDK-298 사용하지 않는 AndroidApp 제거
f547ee9b|2024-12-18|NSDK-298  테스트 UI 구현 및 일부 기능 로직 추가
6e06be82|2024-12-18|NSDK-298 AndroidSample (Demo App) 모듈 추가
b455d8e5|2024-12-17|[공통] Java Import 추가되어 오류 발생하는 부분 제거 (BufferUseCase)
0fde9f31|2024-12-17|[AOS] navisdk_aos_ui 모듈 추가
53fbdd6d|2024-12-17|[공통] 프로젝트 모듈 명 변경 (navisdk, navisdk_core)
0c9d0dd4|2024-12-17|[공통] JBankInfo 공통 Adapter 구현
0516ae8d|2024-12-17|NSDK-297 Platform, InaviController 제거 및 소스정리
19ae8a11|2024-12-17|NSDK-297 Library Load Usecase 구현 및 실행 테스트용 Controller 구현
5b3e9791|2024-12-17|NSDK-297 소스정리
8ba48707|2024-12-17|NSDK-297 Koin 실행 로직 구현
ea363173|2024-12-17|NSDK-297 DI 관리를 위해 관리 Class 추가
490feea6|2024-12-17|NSDK-297 Koin 실행 및 Library 로드를 각 플랫폼에서 진행하도록 인터페이스 구성
d8e65453|2024-12-16|NSDK-297 Common, AndroidMain 영역으로 So 파일 이동
50aac165|2024-12-16|테스트 코드쪽 검색 좌표 사용하여 탐색 요청하도록 변경
bd0910ec|2024-12-16|NSDK-292 UseCase 분리 (일반경로탐색, RouteBuffer 생성)
cd6115ff|2024-12-16|NSDK-292 RouteBuffer 파싱 로직 추가, DP RouteLine 테스트 로직 구현
8b9987fe|2024-12-16|NSDK-292 BufferDownload 네트워크 요청 로직 추가, httpClient 생성
c8b0d26f|2024-12-13|NSDK-292 응답값중 Null 이 들어오는 경우 파싱이 안되는 문제가 있어 수정
9299e58c|2024-12-12|NSDK-292 일반 경로 탐색 요청 UseCase 제거, RouteBuffer를 가져오는 임시 UseCase 구현
71aa62da|2024-12-12|NSDK-292 테스트 데이터를 이용한 일반 경로 탐색 로직 구현,
70a7576b|2024-12-11|NSDK-292 일반 경로 탐색 Usecase 및 Repository 정의
9e85a416|2024-12-11|NSDK-292 일반 경로 탐색 응답 파라미터 정의
0c443ca2|2024-12-11|NSDK-292 ReqRoute 파일에서 요청 파라미터 전체 정의
333d34d9|2024-12-11|NSDK-292 일반 경로 탐색 요청 파라미터 정의
1bc20fd9|2024-12-10|[공통] IOS Permission Controller 연결
757f93ea|2024-12-05|NSDK-283 Coarse Location 권한은 API 31레벨 미만에서 필요없는것으로 확인
e72026cf|2024-12-05|NSDK-283 AOS 플랫폼에서 PermissionController 연동, 테스트 코드 추가
dc7bff20|2024-12-04|[공통] NaviMap Interface에 MapOverlay 인스턴스를 반환하는 함수 추가
3aa27e21|2024-12-04|NSDK-283 AndroidMain Manifest 생성 후 권한 추가
5f8e0305|2024-12-04|NSDK-259 호출 예시 코드 구현, 조건부 권한 추가
560dd27f|2024-12-03|NSDK-259 PermissionSource를 플랫폼 별 구현 후 주입하는 방식으로 변경
3e2ed81c|2024-12-03|NSDK-259 권한 요청 Usecase 구현, PermissionRepoistory 플랫폼 별 구현체 정의 필요
ac6e62c6|2024-12-03|NSDK-259 Permission Repository 구현 및 Event Class 정의
13c6ac6b|2024-12-03|NSDK-259 Moko Permission 라이브러리 추가
41e2e967|2024-11-29|NSDK-272 검토가 필요한 부분 주석 및 일부 예외처리 추가
9a3760e2|2024-11-29|NSDK-272 서비스게이트 재요청 로직 추가 및 UseCase 일부 변경
1cdd0853|2024-11-29|NSDK-272 초기화 Usecase 분리 (Navi 초기화, SDK 초기화)
b9cb1a07|2024-11-28|NSDK-272 DeviceInfo에 Debug 판단 플래그 추가
e029d99b|2024-11-28|NSDK-272 코드 정리
16ec4473|2024-11-27|NSDK-272 UseCase 매개변수에 요청 파라미터 추가하도록 변경
1ad92038|2024-11-27|NSDK-272 모듈 정보 체크 로직 추가 및 InitStatus 콜백 로직 추가
0543a3a7|2024-11-27|NSDK-272 ServiceGate UseCase 연동 로직 추가
5337d6d5|2024-11-27|NSDK-272 ServiceGate I/F 추가
de8403e2|2024-11-25|NSDK-272 초기 인증 로직 분리 작업 진행 (UseCase)
90c42c37|2024-11-25|NSDK-272 Network 응답 실패 시, ErrorCode 및 ErrorMsg 추가한 부분 원복
bec89c27|2024-11-25|NSDK-272 ClauseAgree API 추가, 이용약관 요청 로직 구현
02bc3d2d|2024-11-25|NSDK-272 Network 응답 실패 시, ErrorCode 및 ErrorMsg 응답 부분이 없어 추가
76047c16|2024-11-25|NSDK-272 Network 모듈에서, SDK 인증 요청은 별도로 요청하도록 분리
741c7d09|2024-11-25|NSDK-272 Android DeviceID 세팅 로직 추가
831751b8|2024-11-25|NSDK-272 DeviceInfo interface 추가
a035a5df|2024-11-25|NSDK-272 DeviceID 인자 값 적용을 위해, Deivce 정보 관련 Actual 생성
d8715ab8|2024-11-22|NSDK-272 초기 인증 플로우 진행 시, 에러코드 및 예외 케이스를 위해 InitStatus 추가
6db79e7a|2024-11-22|NSDK-272 SDKAuth API를 이용한 인증로직 구현
64a6895f|2024-11-22|NSDK-272 SDKAuth API 추가 및 네트워크 요청 파라미터 추가 (Url, QueryParam, forceDecode)
2a658f82|2024-11-22|NSDK-272 초기인증 플로우 구현
6fe83110|2024-11-21|MapView 구조 검토를 위해, NaviMapView, MapViewModel, UIController 생성
2d275c47|2024-11-18|NSDK-264 음성 모듈 인터페이스 Model, Repository 분리
a8af3003|2024-11-18|NSDK-264 음성 모듈 인터페이스 Model, Repository 분리
81c43b4a|2024-11-15|NSDK-264 음성 모듈 인터페이스 추가
3970dc0a|2024-11-15|NSDK-264 음성 모듈 인터페이스 추가
8221a20c|2024-11-15|NSDK-264 DP 모듈 인터페이스 추가, Android 구현체 정의 및 테스트 코드 추가
f6bc5ea7|2024-11-15|NSDK-264 DP 모듈 인터페이스 추가, Android 구현체 정의 및 테스트 코드 추가
fe5e6b25|2024-11-15|NSDK-264 AndroidTarget 이전 로직으로 원복, JvmToolChain 로직 제거
c9f9bf3c|2024-11-15|NSDK-264 AndroidTarget 이전 로직으로 원복, JvmToolChain 로직 제거
1cec5e1f|2024-11-13|NSDK-264 NaviSDK AndroidMain에서 MapView 사용 할 수 있도록 jar 파일 이동
3889dbc6|2024-11-13|NSDK-264 NaviSDK AndroidMain에서 MapView 사용 할 수 있도록 jar 파일 이동
26f6228b|2024-11-13|NSDK-264 NaviBank 경로 변경
71481e79|2024-11-13|NSDK-264 NaviBank 경로 변경
1b31e80c|2024-11-13|NSDK-264 SMR 모듈 인터페이스 추가, Android 구현체 정의
a4cb9ad9|2024-11-13|NSDK-264 SMR 모듈 인터페이스 추가, Android 구현체 정의
bdf3a66a|2024-11-12|NSDK-264 Natives(MMC) 모듈 인터페이스 추가, Android 구현체 정의
877a5655|2024-11-12|NSDK-264 Natives(MMC) 모듈 인터페이스 추가, Android 구현체 정의
d6439da3|2024-11-12|NSDK-264 Import 코드정리
8e536e64|2024-11-12|NSDK-264 Import 코드정리
f0476fd3|2024-11-12|NSDK-264 SGuidance 모듈 인터페이스 추가, Android 구현체 정의
fea7e2d7|2024-11-12|NSDK-264 SGuidance 모듈 인터페이스 추가, Android 구현체 정의
20f4c391|2024-11-12|NSDK-264 Guidance Data Class, Common 영역으로 이동
54fab637|2024-11-12|NSDK-264 Guidance Data Class, Common 영역으로 이동
8504c85f|2024-11-12|NSDK-264 NativeAdmin 모듈 인터페이스 및 Controller 구현
427732c9|2024-11-12|NSDK-264 NativeAdmin 모듈 인터페이스 및 Controller 구현
e1405c6d|2024-11-11|NSDK-264 안내엔진 JNI 추가 및 필요한 Data Class 구성
3d23df61|2024-11-11|NSDK-264 안내엔진 JNI 추가 및 필요한 Data Class 구성
9566e518|2024-11-11|NSDK-264 NaviBank 인스턴스 하나로 유지하도록 변경
30009445|2024-11-11|NSDK-264 NaviBank 인스턴스 하나로 유지하도록 변경
a7a5834e|2024-10-30|NSDK-243 초기 appkey 로드 하는 부분 AOS 인터페이스 구성
5808a9c9|2024-10-30|NSDK-243 초기 appkey 로드 하는 부분 AOS 인터페이스 구성
e9483d97|2024-10-24|NSDK-244 ArtifactId 수정
aad4745f|2024-10-24|NSDK-244 ArtifactId 수정
a9185e98|2024-10-24|NSDK-244 readme 배포 명령어 추가
06e321ec|2024-10-24|NSDK-244 readme 배포 명령어 추가
cbfd7c8a|2024-10-24|NSDK-244 Artifactory 게시 로직 추가
bedcc9ad|2024-10-24|NSDK-244 Artifactory 게시 로직 추가
433f85f9|2024-10-23|NSDK-244 로컬 Maven 저장소에 라이브러리 업로드하는 로직 추가
ae7a781d|2024-10-23|NSDK-244 로컬 Maven 저장소에 라이브러리 업로드하는 로직 추가
7da85247|2024-10-23|NSDK-244 ArtifactoryGradlePlugin 추가
cfc9f979|2024-10-23|NSDK-244 ArtifactoryGradlePlugin 추가
```
