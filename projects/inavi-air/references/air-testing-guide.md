---
title: >-
    아이나비 에어 Testing Guide(공통)
category: references
project: inavi-air
tags: [air, testing, android-auto, carplay, gps-log, push, visibility/internal]
aliases: [Testing Guide(공통), 에어 테스트 가이드]
relationships:
  - target: "[[inavi-air]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/205029553
summary: >-
    에어 앱 테스트 환경 제어 방법. Android Auto DHU 설정과 옵션, CarPlay 실기기/시뮬레이터, GPS 로그 구조와 로그 주행, FCM Push 테스트 구조, 모의주행, 외부연동 길찾기 확인.
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

# 아이나비 에어 Testing Guide(공통)

에어 앱 내부에서 테스트 환경을 제어하는 사양과 방법을 모은 페이지(2024-02-27 수정)다. 원본에는 상용/개발 서버 전환과 개발자 모드 진입 방법도 있으나 숨은 기능 진입 방법이므로 옮기지 않았다(원본에 있음, 미수록). 개발 문서는 [[air-android-ios-developer-docs]], 푸시 일반은 [[air-push-notification]], 목차는 [[air-internal-docs-and-integration-hub]]를 본다.

## 개발자 모드가 필요한 기능

원본은 다음 기능이 개발자 모드를 켠 상태에서만 실행된다고 정리한다(진입 방법 미수록).
- GPS 로그 주행
- 안전운전 화면에서의 서버 변경
- "추가 필요" (미작성)

## Android Auto(에뮬레이터, DHU) 사용

### 초기 세팅
1. 휴대폰 설정의 개발자 옵션에서 `USB 디버깅 사용`을 On.
2. 휴대폰의 Android Auto 설정 화면으로 이동해 오른쪽 상단 버튼으로 개발자 설정을 허용한다(OS 설정에 없으면 앱 설치 필요).
3. Android Studio에서 DHU를 설치한다: SDK Manager > SDK Tools > Android Auto Desktop Head Unit emulator.

### 실행 방법
1. 휴대폰 Android Auto(단말 설정)에서 "내 헤드 유닛 서버 시작"을 실행한다.
2. adb로 개발 머신의 포트 5277 소켓 연결을 Android 기기의 같은 포트로 전달한다: Android SDK `platform-tools`에서 `adb forward tcp:5277 tcp:5277`.
3. Android SDK의 `extras/google/auto` 디렉터리에서 DHU를 실행한다: `./desktop-head-unit`.

### 테스트 옵션
DHU 실행 시 여러 옵션을 줄 수 있다.

| 옵션 | 설명 | 명령 |
|---|---|---|
| Rotary controller | 자동차 중앙 콘솔의 노브와 주변 버튼으로 헤드 유닛을 제어하는 방식 | `./desktop-head-unit -i controller` |
| 해상도 | 구성 파일로 다양한 해상도(wide, 720p, 1080p 등) 테스트 | `./desktop-head-unit -c ./config/default_wide.ini` |

그 외 속성은 구글 공식 DHU 문서에서 확인한다.

## CarPlay

### 실기기
CarPlay는 Siri가 켜져 있어야 사용 가능하다.
1. 전원 케이블을 연결한다.
2. 스위치를 ON.
3. 아이폰을 해당 케이블에 연결한다.
4. CarPlay에서 아이나비 에어를 실행한다.

### 시뮬레이터
1. `Carplay Simulator.app`을 받는다: Xcode용 추가 도구 다운로드 > Xcode 14.3 Tools(작성 시점 최신) > dmg > Hardware 폴더 안. 응용프로그램 폴더로 옮겨 쓴다.
2. 아이폰을 유선 연결한 뒤 실행하면 대시보드와 CarPlay를 확인할 수 있다.

## GPS 로그

위치, 시간, 속도 정보가 txt 파일에 저장된다.
- **시간정보**: GPS 데이터가 수집된 타임스탬프
- **위치정보**: 위도/경도(경우에 따라 고도 포함)
- **속도 및 방향정보**: 이동 속도와 방향

예시 로그 파일명: `(과속)서울 부산2_test3.txt`

### GPS 로그 다운로드
- 내부망에서만 가능하다(모바일 데이터로는 불가).
- 메인 화면 검색창에 로그 다운로드용 숨은 입력어를 넣어 실행한다(입력어 미수록).
- 다운로드할 수 없는 환경이거나 가진 로그를 직접 넣어야 하면 별도 방법을 쓴다. iOS는 [[air-android-ios-developer-docs]]의 "로그파일" 항목(GpsLog 폴더에 직접 복사)을 본다.

### GPS 로그 주행
저장된 로그 파일의 위치, 시간, 속도 정보로 주행한다. 로그 다운로드를 먼저 실행하고 개발자 모드를 켜 둬야 한다.
1. 메인 화면 검색창으로 이동한다.
2. 임의의 장소를 입력해 길찾기를 실행한다.
3. 현위치를 벗어날 때 좌상단에 나타나는 지도 모양 아이콘을 길게 누른다.
4. 주행 리스트에서 원하는 항목을 선택한다.

### GPS 로그 저장
"해당 기능 서술 필요"로 비어 있음.

## Push

FCM Token이 필요하며 앱을 지웠다 다시 설치하면 토큰도 바뀐다. 원본에는 FCM 서버 키와 기기 토큰이 박힌 curl 명령 6종이 있으나 값은 옮기지 않았다(원본에 있음, 미수록). 아래는 요청 구조만 정리한다. 서비스 전반의 푸시 설계는 [[air-push-notification]]을 본다.

### 토큰 얻는 법과 호출 방식
- **Android**: ServiceGate 데이터 서버 요청 시 보내는 파라미터 값(`FBTokenStore.getToken()`)으로 확인한다.
- **iOS**: Xcode에서 앱을 실행하면 나오는 로그의 FCM Token을 사용한다.
- 가져온 값을 curl 명령 마지막 줄 `"to"`의 value로 바꿔 터미널에서 실행한다.
- 요청: FCM 발송 엔드포인트에 `POST`, 헤더 `authorization: key=<서버 키>`, `cache-control: no-cache`, `content-type: application/json;charset=UTF-8`, 본문은 `data`와 `to`.

### 일반 push 본문(`data`)

| 키 | 값 예 | 설명 |
|---|---|---|
| `nt` | `FCM PUSH TITLE` | 알림 제목 |
| `pt` | `popup_title` | 팝업 타이틀 |
| `pc` | `popup_content` | 팝업 내용 |
| `type` | `D` 또는 `E` | 푸시 유형(원본 예시 2종) |
| `subtype` | `CI` | 하위 유형 |
| `url` | 빈 문자열 | 이동 URL |
| `collapskey` | `HJ_TYPE` | collapse key |

iOS 예시는 같은 `data`에 `"notification": {"title": "test D", "body": "New news story available."}`를 함께 보낸다(`type` `E`, `subtype` `CI`).

### 탐색용 push 본문(`data`)

| 키 | 값 예 | 설명 |
|---|---|---|
| `nt`, `pt`, `pc`, `collapskey` | 일반 push와 동일 | |
| `type` | `S`(`payType` `A`) 또는 `X` | 탐색용 유형(원본 예시 2종) |
| `status` | `"4"` | 상태 값 |
| `iu` | (링크 항목) | 이미지 URL ^[ambiguous] |
| `callId` | `"922959"` | 호출 ID |
| `startLoc` | `{x, y, poiid, name}` | 출발지. x `45760675`, y `13463829`, poiid 빈 값, name 회사명 |
| `endLoc` | `{x, y, poiid, name}` | 목적지. x `45731002`, y `13497630`, poiid `4522133`, name 강남역 |
| `viaLocs` | `[{x, y, poiid, name}]` | 경유지 배열(예: x `45765625`, y `13459212`) |

좌표 x/y는 정수 좌표(WGS84 경위도에 큰 배율을 곱한 값으로 보임)이다 ^[inferred]

## 주행

### 모의주행
1. 모의주행할 경로를 선택한다.
2. 경로선택 화면에서 전체경로 버튼으로 전체경로 화면으로 이동한다.
3. 모의주행 버튼을 눌러 실행한다.

### 외부연동 길찾기
1. 에어 메인 화면에서 임의의 장소를 입력하고 공유 버튼(즐겨찾기와 길찾기 사이)을 누른다.
2. 공유 앱 중 메시지를 눌러 저장한다.
3. 추가된 링크를 누르면 에어 길찾기 페이지로 연결되고, 길찾기 버튼 후 나오는 팝업에서 열기를 누른다. 링크 규격은 [[air-external-integration-ios-spec]], [[air-external-integration-android-spec]].

### 자동 안전운행
"작성 필요"로 비어 있음.

## Related
- [[air-android-ios-developer-docs]] — 프로젝트 세팅과 기여 가이드
- [[air-push-notification]] — 푸시 설계
- [[inavi-air]] — 에어 앱 개요
- [[air-internal-docs-and-integration-hub]] — 이 묶음 목차

## Sources
- Confluence "Testing Guide(공통)" (pageId 205029553) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
