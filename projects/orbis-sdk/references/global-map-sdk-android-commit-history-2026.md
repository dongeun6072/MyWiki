---
title: >-
    글로벌 지도 SDK Android 작업 이력 2026
category: references
project: orbis-sdk
tags: [orbis-sdk, map-sdk, android, compose, bitbucket, commit-history, visibility/internal]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[map-sdk-commercialization-scrums-2026]]"
    type: related_to
  - target: "[[navisdk-core-commit-history]]"
    type: related_to
sources:
  - repo:bitbucket/mobility-tech/inavi-global-map-sdk-android
summary: >-
    inavi-global-map-sdk-android 본인 커밋 163건(2026-01~07)의 주제별 이력. 커밋 메시지 기준이며 diff는 검증하지 않았다.
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
  - "[[_raw/_archived/Bitbucket_inavi-global-map-sdk-android_커밋목록_dongeun|Bitbucket_inavi-global-map-sdk-android_커밋목록_dongeun]]"
---

# 글로벌 지도 SDK Android 작업 이력 2026

본인이 작성한 `inavi-global-map-sdk-android` 저장소(글로벌 지도 SDK Android) 커밋 163건(2026-01-21 ~ 2026-07-15)을 주제별로 묶은 이력이다. 프로젝트 개요는 [[orbis-sdk]], 같은 시기 상용화 논의는 [[map-sdk-commercialization-scrums-2026]], 내비게이션 SDK 쪽 이력은 [[navisdk-core-commit-history]]를 본다. 월별 건수는 2026-01 24건, 02 74건, 03 37건, 05 14건, 06 2건, 07 13건이다.

> [!warning] 커밋 메시지 기준, diff 미검증
> 이 페이지는 커밋 메시지만 근거로 한 요약이다. 메시지와 실제 변경이 다를 수 있다. 주제 분류는 메시지 키워드와 이슈 키로 한 1차 분류라 경계 사례가 있고 ^[inferred], 대상을 알 수 없는 커밋은 따로 모았다 ^[ambiguous]. 각 항목의 해시로 `git show <해시>`를 실행해 확인한다. 동기와 효과는 메시지에 있는 것만 적었다. 서버 포트와 숨은 기능 진입 방법 등 보안 대상 값은 원본에서도 가렸다.

근거는 커밋 메시지뿐이며 diff와 코드는 확인하지 않았다.

## 기간 개요

커밋 목록은 2026-01-21부터 2026-07-15까지 총 163건이다. 월별로는 2026-01 24건, 2026-02 74건, 2026-03 37건, 2026-04 0건, 2026-05 14건, 2026-06 2건, 2026-07 12건이다. 커밋 메시지상 2~3월에 건수가 몰려 있고, 그중 상당수는 `NSDK-6xx` 이슈 키가 붙은 기능 구현·수정 작업이다. 2026-05 이후에는 언어·스타일 모드 API, framework_type 헤더, 문서·서브모듈 관련 작업이 나타난다.

## 1. 프로젝트 초기 구성·네트워크 기반 (13건)

기간: 2026-01~2026-01

커밋 메시지상 저장소 생성, 라이브러리 플러그인 전환, maplibre·Okhttp 라이브러리 추가, Playground 모듈 추가, 네트워크 모듈·인증 DTO·응답 코드 구성 관련 작업이 13건 있다.

이슈 키: NSDK-624, NSDK-626

- `a3256e9` (2026-01-21) Initial commit
- `29a6ad4` (2026-01-21) 프로젝트 초기화(init project)
- `91697b4` (2026-01-21) SDK 개발을 위해 Application을 library 플러그인으로 변경
- `d6c077d` (2026-01-21) maplibre 라이브러리 추가
- `d3b0759` (2026-01-22) Playground 모듈 추가
- `bc58f62` (2026-01-26) 네트워크 모듈 구성

## 2. 지도 뷰·UI 컨트롤 (24건)

기간: 2026-01~2026-05

MapView·MapFragment 기본 동작, 속성(attr)·제스처, ScaleBar, 로고·Attribution 뷰, 나침반, 줌 컨트롤, 현위치 버튼과 TrackingMode, uiSettings 관련 작업이 24건 있다. OnMapReadyCallback 콜백 인터페이스 도입과 이후 fun interface 변경도 포함한다.

이슈 키: NSDK-628, NSDK-630, NSDK-638

- `07b1c07` (2026-01-27) MapView, MapFragment 기본 동작 구현
- `5406750` (2026-01-28) ScaleBar 추가
- `ae9819b` (2026-01-30) OnMapReadyCallback 콜백 인터페이스 추가, 기존 람다 함수 제거
- `323b874` (2026-01-30) 지도 상 Logo 및 Attribution Custom View 구현
- `31bee9f` (2026-02-03) 현위치 버튼 추가, TrackingMode 함수 구현
- `934fca2` (2026-05-27) OnMapReadyCallback을 fun interface로 변경

## 3. 카메라·지도 이벤트·Projection (13건)

기간: 2026-02~2026-03

Projection 래퍼, 지도 클릭·롱클릭 리스너, CameraPosition·CameraUpdate·지도 패딩 API, 카메라 이동·변경 콜백, 카메라 위치 변경 로직 수정 관련 작업이 13건 있다.

이슈 키: NSDK-632, NSDK-640, NSDK-653

- `d10ec86` (2026-02-04) Projection Wrapper 클래스 구현
- `f150a92` (2026-02-04) MapClickListener API 추가
- `d0cf617` (2026-02-04) CameraPosition 객체 추가, 카메라 현재 위치 설정·조회 API 추가
- `107a144` (2026-02-04) 카메라 이동 콜백 API 추가
- `54f33f4` (2026-02-19) 카메라 위치 변경 로직 수정
- `753f8e6` (2026-03-04) 카메라 이동 끝났을 때 호출되는 콜백 추가

## 4. 마커·정보창 (15건)

기간: 2026-02~2026-03

마커 추가·삭제, 마커 타이틀 텍스트 필드·textFont 적용, allowOverlapSymbols, 정보창(InfoWindow) 로직, IgmMarker 생성자·오버로드, 유효하지 않은 좌표 예외 처리, 정보창 나인패치 텍스트 영역 수정 관련 작업이 15건 있다.

이슈 키: NSDK-634, NSDK-636

- `d01af93` (2026-02-05) 마커 추가 및 삭제 로직 구현
- `0f46f15` (2026-02-05) Json Style의 textFont를 적용해 마커 타이틀이 세팅 안되는 문제 수정
- `534085e` (2026-02-06) 정보 창 로직 구현
- `9859107` (2026-02-09) 누락된 IgmMarker Overloads 추가
- `f4504cf` (2026-03-06) 마커 유효하지 않은 좌표 예외 처리 로직 변경
- `4a1d798` (2026-03-09) info window background 나인패치 텍스트 영역 수정

## 5. 도형(Shape)·클러스터 (16건)

기간: 2026-02~2026-03

Polygon·Polyline·Circle 도형 구현, Layer·ZIndex 오더링, Turf Manager, 클릭 이벤트 소비, 선 두께 보정, 정렬 문제 수정, Cluster 관련 로직 추가 작업이 16건 있다.

이슈 키: NSDK-636, NSDK-640, NSDK-653

- `d8c232d` (2026-02-09) 폴리곤 도형 구현
- `fd0dea7` (2026-02-09) Polyline 구현
- `b9409e9` (2026-02-10) Circle Shape 추가
- `5515bec` (2026-02-10) Turf Manager 로직 일부 추가
- `2ebf2f3` (2026-02-13) Cluster 관련 로직 추가
- `c963670` (2026-03-05) Shape의 선 두께가 보정 안된 Pixel 형태로 표출되는 문제 수정

## 6. 사용자 위치 컴포넌트 (10건)

기간: 2026-02~2026-05

LocationIcon, 원 색상·반경·스케일, 아이콘 클릭·위치 변경 이벤트, 레이어 Property 기반 이미지 적용, 위치 아이콘 background/shadow 레이어 노출 문제 수정 관련 작업이 10건 있다.

이슈 키: NSDK-638, NSDK-729

- `d8afb5c` (2026-02-11) LocationIcon 구현
- `fe3b5a2` (2026-02-12) Location CircleColor, CircleRadius, Scale 구현
- `0995470` (2026-02-12) 사용자 위치 아이콘 클릭 이벤트 구현
- `eae91aa` (2026-02-13) Tracking, TrackingCompass 이미지를 Layer Property 속성으로 변경
- `02f3c6a` (2026-02-13) gpsDrawable, bearingDrawable이 잘 작동하지 않아 Layer로 변경
- `da1d80b` (2026-05-22) 위치 아이콘 background/shadow 레이어 노출 문제 수정

## 7. 인증·응답 코드·framework_type 헤더 (8건)

기간: 2026-02~2026-07

MapView 내 인증 로직 적용, 준상용 인증 API 대응, 인증 실패 시 에러코드 표출, 좌표 변환 로직, 인증 기반 스타일 URL 로드, Result.code 타입 변경, 인증 요청 공통 헤더의 framework_type 필드 추가와 setFrameworkType 임의 값 주입 방지 관련 작업이 8건 있다.

이슈 키: NSDK-644

- `f9dd55c` (2026-02-11) MapView 내 인증로직 적용
- `ab95da4` (2026-02-04) 준상용 인증 API 대응
- `af2cfca` (2026-02-25) 인증 API 실패 시 정의된 에러코드부터 표출하도록 변경
- `0a19c07` (2026-02-25) 좌표 변환 로직 추가
- `563e35a` (2026-05-27) 인증 기반 스타일 URL 로드 연동
- `5b814c7` (2026-07-08) 인증 요청 공통 헤더에 framework_type 필드 추가
- `8aaebb8` (2026-07-09) setFrameworkType 임의 값 주입 방지(파라미터 제거, flutter 고정)

## 8. 언어 전환·MapStyleMode API (10건)

기간: 2026-05~2026-06

IgmMapLanguage enum 추가와 setLanguage/getLanguage API 변경, playground 언어 전환 버튼, 언어 설계 문서, ZH_TW 관련 수정·주석, setMapStyleMode/getMapStyleMode API 추가와 크래시 수정 관련 작업이 10건 있다.

이슈 키: 없음

- `619d35f` (2026-05-27) 언어 전환 설계 문서 및 구현 계획 추가
- `a7414b5` (2026-05-27) IgmMapLanguage enum 추가
- `96221b5` (2026-05-27) setLanguage/getLanguage API를 IgmMapLanguage enum으로 변경
- `1270791` (2026-05-28) setMapStyleMode / getMapStyleMode API 추가
- `889d68b` (2026-05-28) setMapStyleMode 호출 시 LocationComponent 미활성화 크래시 수정
- `87fcb48` (2026-06-15) IgmMapLanguage ZH_TW metadataKey를 스타일 키와 일치하도록 수정

## 9. 난독화·릴리즈 빌드·배포·버전 (14건)

기간: 2026-02~2026-07

Keep 어노테이션, 필드 난독화 제외, release 빌드 오류·패키지 난독화 충돌, BuildConfig 참조, 원본 소스 노출 문제, Jfrog 배포 로직, 스타일·배포 버전 원복, demo 모듈 연동·제거, 버전 업데이트(1.0.0 -> 1.0.1) 관련 작업이 14건 있다.

이슈 키: NSDK-653

- `9ec2124` (2026-02-04) 누락된 Keep Annotation 추가
- `265ed72` (2026-03-03) Release 빌드 안되는 문제 수정
- `eff379f` (2026-03-03) Jfrog 배포 로직 추가
- `8cc0f8f` (2026-03-04) 난독화되면서 동반객체 필드를 찾지 못하는 이슈 수정
- `6d9d684` (2026-05-26) release 빌드 패키지 난독화 충돌 수정
- `79a1df3` (2026-07-15) 버전 업데이트 (1.0.0 -> 1.0.1)

## 10. Dokka·Kdoc·API 레퍼런스 문서 (21건)

기간: 2026-02~2026-07

dokka 라이브러리·모듈 버전 추가, 패키지 문서(Package Info, 최상위 패키지), 패키지별 Kdoc 주석 작성과 영어 변경, 패키지명·Constants 정리, API 레퍼런스 제외 패키지 조정, docs 서브모듈 추가와 동기화 태스크 관련 작업이 21건 있다.

이슈 키: NSDK-658

- `cb6cadf` (2026-02-27) dokka 라이브러리 추가
- `4fa47c7` (2026-02-27) Package Info에 대한 내용 추가
- `854b3f9` (2026-03-03) maps 모듈 Kdoc 주석 작업 진행
- `71511a0` (2026-03-05) maps 패키지 Kdoc 주석 영어로 변경
- `d26b9b1` (2026-07-15) docs 서브모듈 추가 (SDK Reference)
- `793d3d0` (2026-07-15) dokka 산출물 docs 서브모듈 동기화 태스크 추가

## 11. 위키·설계 문서·프로젝트 규칙 (5건)

기간: 2026-07~2026-07

framework_type 헤더 설계 문서·구현 계획, wiki 서브모듈 추가와 포인터 갱신, 문서 위치·wiki 운영 규칙(CLAUDE.md) 추가, docs/superpowers 제거 관련 작업이 5건 있다.

이슈 키: 없음

- `ddc30f2` (2026-07-08) framework_type 헤더 설계 문서 및 구현 계획 추가
- `77c3d69` (2026-07-08) mtech-wiki 서브모듈 추가
- `281c5e2` (2026-07-09) superpowers 문서 wiki 이관에 따라 docs/superpowers 제거
- `ae51ffd` (2026-07-09) superpowers 문서 위치·wiki 운영 규칙 CLAUDE.md 추가
- `a1dc365` (2026-07-15) wiki 서브모듈 포인터 갱신

## 12. 연동 가이드 정합·NSDK-653 마무리 수정 (9건)

기간: 2026-02~2026-03

연동 가이드 기준 로직·프로퍼티명 수정, 로고 visibility·클릭 이벤트 제거, 줌 컨트롤 확대 버튼 비활성 문제, global maps 전용 이미지 적용, Style Url 변경과 마커 미표출 수정, MapOptions 설정 시 기본 위치 문제, 초기 위치 설정 문제 관련 작업이 9건 있다.

이슈 키: NSDK-653

- `90aaa39` (2026-02-26) 가이드 문서와 맞지 않는 프로퍼티명 수정
- `d78eb3e` (2026-02-26) 연동 가이드 기준으로 일부 로직 변경
- `b58a2df` (2026-03-04) MapOptions가 세팅되는 경우 Default 위치 세팅 안되는 문제 수정
- `372a024` (2026-03-03) 초기 위치 세팅 안되는 문제 수정
- `c6f38da` (2026-03-05) Style Url 변경, 마커 표출안되는 문제 수정
- `eb0f7b6` (2026-03-06) global maps 전용 이미지 적용

## 13. 모호한 커밋 (5건)

대상이 메시지만으로는 불분명한 커밋이 5건 있다.

- `139f9f0` (2026-02-27) fix: 누락된 field value 추가
- `a852b9d` (2026-02-09) 코드 정리
- `83e6d7a` (2026-03-05) NSDK-653 필요없는 로직 제거
- `44aa4f1` (2026-03-05) NSDK-653 필요없는 로직 제거
- `2f1d8f9` (2026-03-04) NSDK-653 예제 추가 진행 중 동작하지 않는 부분 수정

## 검산

주제별 건수 합 = 전체 건수: 13 + 24 + 13 + 15 + 16 + 10 + 8 + 10 + 14 + 21 + 5 + 9 + 5 = 163

## Sources

- 원본 커밋 목록: [[_raw/_archived/Bitbucket_inavi-global-map-sdk-android_커밋목록_dongeun]] (해시|날짜|메시지)
- 저장소: Bitbucket `mobility-tech/inavi-global-map-sdk-android`, 필터 `--author` 본인, merge·stash 제외
