# Bitbucket inavi-global-map-sdk-android 커밋 목록 (본인 작성분)

- 저장소: Bitbucket mobility-tech/inavi-global-map-sdk-android (로컬 clone `Android/inavi-maps/inavi-global-map-sdk-android`)
- 필터: `git log --all --no-merges --author=dongeun`, stash 항목 제외
- 수집일: 2026-10-28, 총      163건, 기간 2026-01-21 ~ 2026-07-15
- 형식: `해시|작성일|커밋 메시지` (최신순). 메시지 원문이며 diff는 검증하지 않았다.

```
793d3d0|2026-07-15|chore: dokka 산출물 docs 서브모듈 동기화 태스크 추가
b865763|2026-07-15|chore: settings.gradle에서 demo 모듈 제거
d26b9b1|2026-07-15|chore: docs 서브모듈 추가 (SDK Reference)
4619281|2026-07-15|docs: framework_type getter/setter @suppress 제거로 API 문서 노출
79a1df3|2026-07-15|버전 업데이트 (1.0.0 -> 1.0.1)
a1dc365|2026-07-15|chore: wiki 서브모듈 포인터 갱신 (framework_type setter 설계 변경 문서 반영)
8aaebb8|2026-07-09|fix: setFrameworkType 임의 값 주입 방지 (파라미터 제거, flutter 고정)
ae51ffd|2026-07-09|docs: superpowers 문서 위치·wiki 운영 규칙 CLAUDE.md 추가
281c5e2|2026-07-09|docs: superpowers 문서 wiki 이관에 따라 docs/superpowers 제거
77c3d69|2026-07-08|chore: mtech-wiki 서브모듈 추가
5b814c7|2026-07-08|feat: 인증 요청 공통 헤더에 framework_type 필드 추가
ddc30f2|2026-07-08|docs: framework_type 헤더 설계 문서 및 구현 계획 추가
f514f15|2026-06-15|fix: 언어 라벨 textField를 토큰 문자열로 직접 적용
87fcb48|2026-06-15|fix: IgmMapLanguage ZH_TW metadataKey를 스타일 키와 일치하도록 수정
6358ea7|2026-05-28|docs: IgmMapLanguage ZH_TW 주석을 Chinese (Taiwan)으로 수정
598c49e|2026-05-28|docs: MapStyleMode API 설계 문서 및 구현 계획 추가
f6e3d16|2026-05-28|chore: :demo 모듈 연동 및 flexbox 의존성 추가
889d68b|2026-05-28|fix: setMapStyleMode 호출 시 LocationComponent 미활성화 크래시 수정
1270791|2026-05-28|feat: setMapStyleMode / getMapStyleMode API 추가
619d35f|2026-05-27|docs: 언어 전환 설계 문서 및 구현 계획 추가
489fe19|2026-05-27|feat: playground 언어 전환 버튼 3개 구성
96221b5|2026-05-27|feat: setLanguage/getLanguage API를 IgmMapLanguage enum으로 변경
a7414b5|2026-05-27|feat: IgmMapLanguage enum 추가
934fca2|2026-05-27|refactor: OnMapReadyCallback fun interface로 변경
563e35a|2026-05-27|feat: 인증 기반 스타일 URL 로드 연동
fd97795|2026-05-26|refactor: Result.code 타입을 ResponseCode enum에서 String으로 변경
6d9d684|2026-05-26|fix: release 빌드 패키지 난독화 충돌 수정
da1d80b|2026-05-22|NSDK-729 위치 아이콘 background/shadow 레이어 노출 문제 수정
4a1d798|2026-03-09|fix: info window background 나인패치 텍스트 영역 수정
eb0f7b6|2026-03-06|feat: global maps 전용 이미지 적용
9c81cdb|2026-03-06|fix: 로고 visibility 설정 되도록 수정
f4504cf|2026-03-06|fix: 마커 유효하지 않는 좌표 예외 처리 로직 변경
7c5d5f6|2026-03-06|fix: IgmMarker는 인자없는 생성자 구조여야 함
f83da7c|2026-03-06|fix: 빌드 안되는 문제 수정
c4621a2|2026-03-06|docs: 필요없는 소스 및 주석 제외 처리
a6dc4aa|2026-03-05|docs: packages.md 영어로 변경
3a8267e|2026-03-05|docs: shapes 패키지 Kdoc 주석 영어로 변경
5e4aa6e|2026-03-05|docs: clustering 패키지 Kdoc 주석 영어로 변경
71511a0|2026-03-05|docs: maps 패키지 Kdoc 주석 영어로 변경
f860627|2026-03-05|docs: geometry 패키지 Kdoc 주석 영어로 변경
f374a26|2026-03-05|docs: exceptions 패키지 Kdoc 주석 영어로 변경
803819a|2026-03-05|docs: constants 패키지 Kdoc 주석 영어로 변경
c963670|2026-03-05|NSDK-653 Shape의 선 두께가 보정 안된Pixel 형태로 표출되는 문제 수정
0eabbe5|2026-03-05|NSDK-653 지도 추가 시 무조건 줌 컨트롤 뷰의 확대 버튼이 비활성화 되는 문제 수정
83e6d7a|2026-03-05|NSDK-653 필요없는 로직 제거
44aa4f1|2026-03-05|NSDK-653 필요없는 로직 제거
4202714|2026-03-05|NSDK-653 로고 클릭 이벤트 제거
c6f38da|2026-03-05|NSDK-653 Style Url 변경, 마커 표출안되는 문제 수정
b2b9b79|2026-03-05|NSDK-653 Style, 배포 버전 원복
9bf934a|2026-03-05|NSDK-653 Keep 어노테이션 누락된 부분 수정
f5a974b|2026-03-04|NSDK-653 IgmShape Update 시 정렬이 안되는 문제가 있어 수정
b58a2df|2026-03-04|NSDK-653 MapOptions이 세팅되는경우 Default 위치 세팅 안되는 문제가 있어 수정,
1cb75b1|2026-03-04|NSDK-653 사용하지 않는 인터페이스 제거, 셰이프 클릭 이벤트 소비 로직 구현
2f1d8f9|2026-03-04|NSDK-653 예제 추가 진행 중 동작하지 않는 부분 수정
8cc0f8f|2026-03-04|NSDK-653 난독화 되면서 동반객체 필드 찾지 못하는 이슈 수정
753f8e6|2026-03-04|NSDK-653 카메라 이동 끝났을 때 호출되는 콜백 추가
217b743|2026-03-04|NSDK-653 원본 소스 코드가 보이는 문제 수정
372a024|2026-03-03|fix: 초기 위치 세팅 안되는 문제 수정
eff379f|2026-03-03|NSDK-653 Jfrog 배포 로직 추가
f597c85|2026-03-03|fix: 필드 난독화 제외 진행
7ddea44|2026-03-03|fix: BuildConfig 참조 패키지 수정 및 URL 접근 안되도록 수정
265ed72|2026-03-03|fix: Release 빌드 안되는 문제 수정
4eaef4e|2026-03-03|docs: Dokka module version 정의
759e8fa|2026-03-03|NSDK-658 shapes 모듈 Kdoc 주석 작업 진행
854b3f9|2026-03-03|NSDK-658 maps 모듈 Kdoc 주석 작업 진행
c45f333|2026-02-27|NSDK-658 Geometry 문서화 작업
4fa47c7|2026-02-27|NSDK-658 Package Info에 대한 내용 추가
7dff026|2026-02-27|NSDK-658 Constants 파일 이동
b57c0ca|2026-02-27|NSDK-658 API 래퍼런스 필요없는 패키지 제외
9d2ffec|2026-02-27|NSDK-658 map -> maps로 패키지명 수정
9ecc042|2026-02-27|docs: 최상위 패키지 문서 추가
cb6cadf|2026-02-27|feat: dokka 라이브러리 추가
139f9f0|2026-02-27|fix: 누락된 field value 추가
d78eb3e|2026-02-26|fix: 연동 가이드 기준으로 일부 로직 변경
90aaa39|2026-02-26|fix: 가이드 문서와 맞지 않는 프로퍼티명 수정
af2cfca|2026-02-25|NSDK-644 인증 API 실패 시 정의된 에러코드부터 표출 할 수 있도록 변경
0a19c07|2026-02-25|NSDK-644 좌표 변환 로직 추가
54f33f4|2026-02-19|NSDK-640 카메라 위치 변경 로직 수정
2ebf2f3|2026-02-13|NSDK-640 Cluster 관련 로직 추가
1248ebc|2026-02-13|NSDK-638 필요없는 로직 제거
02f3c6a|2026-02-13|NSDK-638 LocationComponentOptions의 gpsDrawable bearingDrawable이 잘 작동하지 않아 Layer를 통해 변경하도록 수정
eae91aa|2026-02-13|NSDK-638 Tracking, TrackingCompass 이미지가 잘 적용안되는 문제가 있어 Layer의 Property 속성으로 변경
0b4cf5b|2026-02-13|NSDK-638 UiSetting에 누락된 Gesture 추가
8833079|2026-02-12|NSDK-638 Map UI onSaveInstance 대응
209931b|2026-02-12|NSDK-638 LocationIcon 내 DefaultIcon 타입을 DrawableRes 형태로 변경
836f021|2026-02-12|NSDK-638 위치 변경 이벤트 추가
0995470|2026-02-12|NSDK-638 사용자 위치 아이콘 클릭 이벤트 구현
fe3b5a2|2026-02-12|NSDK-638 Location CircleColor, CircleRadius, Scale 구현
d8afb5c|2026-02-11|NSDK-638 LocationIcon 구현
94723ce|2026-02-11|NSDK-638 필요없는 로직 제거
f9dd55c|2026-02-11|MapView 내 인증로직 적용
902059d|2026-02-10|NSDK-636 Layer 순서 적용 시, Location Layer는 제일 상위에 배치되도록 수정
18f3a49|2026-02-10|NSDK-636 Shape Sub Layer에 일부 속성이 적용 안되는 문제 수정
b9409e9|2026-02-10|NSDK-636 Circle Shape 추가
c6d1632|2026-02-10|NSDK-636 Polyline ZIndex 잘못 적용된 값 수정
5515bec|2026-02-10|NSDK-636 Turf Manager 로직 일부 추가
410e6f9|2026-02-09|NSDK-636 폴리라인 두께 설정 변수 Int 타입으로 변경
fd0dea7|2026-02-09|NSDK-636 Polyline 구현
9e2ae0e|2026-02-09|NSDK-636 0 이하의 GlobalZIndex Shape이 오더링되는 조건 추가
4f5169c|2026-02-09|NSDK-636 Shape이 여러 Layer를 가지면 오더링 진행 시, 해당 Shape의 마지막 Layer ID를 세팅해야 함.
8e7bba7|2026-02-09|NSDK-636 Polygon의 LineLayer가 타 Shpae에 영향 받는 문제 수정
a852b9d|2026-02-09|코드 정리
d8c232d|2026-02-09|NSDK-636 폴리곤 도형 구현
9859107|2026-02-09|NSDK-636 누락된 IgmMarker Overloads 추가
766f8be|2026-02-09|NSDK-636 DebugActive 비활성화
1c18f71|2026-02-06|NSDK-634 소스 정리
a38161e|2026-02-06|NSDK-634 InfoWindow 테스트 로직 추가
240b75f|2026-02-06|NSDK-634 Shape ClickListener 동작하도록 구현
534085e|2026-02-06|NSDK-634 정보 창 로직 구현
0fa1df9|2026-02-06|NSDK-634 Global Z Index 디폴트 값 추가
37448c0|2026-02-06|NSDK-634 마커 아이콘 아래 텍스트 필드가 무조건 배치되도록 적요
97273f9|2026-02-06|NSDK-634 allowOverlapSymbols Property 값 세팅 되도록 변경
0f46f15|2026-02-05|NSDK-634 Json Style에서 제공하는 textFont 적용하여 마커 타이틀 세팅 안되는 문제 수정
f4ab2bf|2026-02-05|NSDK-634 IgmShape 부모에서 Source를 Refresh 할 수 있도록 구조 변경
d01af93|2026-02-05|NSDK-634 마커 추가 및 삭제 로직 구현
e5dfba4|2026-02-05|NSDK-634 상위 Shape 구성요소 구현
9ec2124|2026-02-04|누락된 Keep Annotation 추가
ab95da4|2026-02-04|준상용 인증 API 대응
9d51a19|2026-02-04|NSDK-632 소스정리
b86b460|2026-02-04|NSDK-632 카메라 이동 원인 상수로 정의
adddee8|2026-02-04|NSDK-632 카메라 변경 이벤트 API 추가
107a144|2026-02-04|NSDK-632 카메라 이동 콜백 API 추가
2a3e23f|2026-02-04|NSDK-632 CameraUpdate 클래스 정의, 애니메이션 추가
ab3bfde|2026-02-04|NSDK-632 지도 패딩 설정 API 구현
d0cf617|2026-02-04|NSDK-632 CameraPosition 객체 추가, 카메라 현재 위치 설정 및 가져오기 API 추가
e06043a|2026-02-04|NSDK-632 위치 권한 허용 시 TrackingMode 적용 안되는 문제 수정
d9c6d60|2026-02-04|NSDK-632 MapLongClickListener API 추가
f150a92|2026-02-04|NSDK-632 MapClickListener API 추가
d10ec86|2026-02-04|NSDK-632 Projection Wrapper 클래스 구현
8f58cc2|2026-02-03|NSDK-630 필요없는 로직 제거
53a56c7|2026-02-03|NSDK-630 uiSettings 안되는 문제 수정
49e516a|2026-02-03|NSDK-630 ZoomControlVisible API 추가
c9b1676|2026-02-03|NSDK-630 IgmMapView 코드 개선
69e3672|2026-02-03|NSDK-630 소스정리
31bee9f|2026-02-03|NSDK-630 현위치 버튼 추가, TrackingMode 함수 구현
5116def|2026-02-02|NSDK-630 라이브러리 원복
9efbf2c|2026-02-02|NSDK-630 위치 서비스 사용을 위해 Google 라이브러리 추가
e7b5eaa|2026-02-02|NSDK-630 ZoomControlView 추가
d08e52e|2026-02-02|NSDK-630 나침반 표출 및 이미지 설정 로직 추가
9d59b5b|2026-01-30|NSDK-630 테스트를 위해 국내향 SDK 이미지 전체 추가
bc153c8|2026-01-30|NSDK-630 ScaleBar 표출 로직 추가
323b874|2026-01-30|NSDK-630 지도 상 Logo 및 Attribution Custom View 구현
ae9819b|2026-01-30|add: OnMapReadyCallback 콜백 인터페이스 추가, 기존 람다 함수 제거
291f236|2026-01-29|NSDK-628 MapFragment에서 IgmMapOption을 이용하여 지도 표출하는 로직 추가
25f7fb9|2026-01-28|NSDK-628 attr Gesture 추가
8659457|2026-01-28|NSDK-628 attr minPitch, maxPitch 추가
5406750|2026-01-28|NSDK-628 ScaleBar 추가
cbaae12|2026-01-28|NSDK-628 attr 속성에 좌표 추가 시 카메라 이동되도록 적용
6e2010e|2026-01-27|NSDK-628 Constants 정의, 지도 객체 응답을 위한 콜백 함수 추가
07b1c07|2026-01-27|NSDK-628 MapView, MapFragment 기본 동작 구현
2178d0c|2026-01-26|NSDK-626 MapView 및 Service 추가
b94bc61|2026-01-26|NSDK-626 Response Code, Context Util 추가
bc58f62|2026-01-26|NSDK-626 네트워크 모듈 구성
2a3c28e|2026-01-26|NSDK-626 인증 DTO 추가
b1bbc8b|2026-01-23|NSDK-626 Okhttp 라이브러리 추가
5840158|2026-01-23|NSDK-626 SDK 모듈 이름 변경
d3b0759|2026-01-22|NSDK-624 Playground 모듈 추가
eed9b36|2026-01-22|docs: fix readme
d6c077d|2026-01-21|NSDK-624 maplibre 라이브러리 추가
91697b4|2026-01-21|NSDK-624 SDK 개발을 위해 Application을 library 플러그인으로 변경
29a6ad4|2026-01-21|chore: init project
f5d251a|2026-01-21|docs: fix gitignore
a3256e9|2026-01-21|Initial commit
```
