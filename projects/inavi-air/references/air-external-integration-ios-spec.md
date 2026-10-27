---
title: >-
    아이나비 에어 iOS 외부 연동 규격
category: references
project: inavi-air
tags: [air, ios, integration, url-scheme, autorunair, visibility/internal]
aliases: [iNavi AIR iOS 연동 규격]
relationships:
  - target: "[[inavi-air]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/305168599
summary: >-
    에어 iOS 외부 연동 규격(v1.3, 2026-09). WGS84 좌표계, autorunair URL 규격, 단순 실행/길 안내/즉시 안내 인자, 앱 내 호출 코드와 연동 제한을 정리.
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

# 아이나비 에어 iOS 외부 연동 규격

iOS에서 다른 앱이나 Safari, SMS/MMS의 URL로 아이나비 에어를 호출하는 규격이다. 마지막 개정은 2026-09-14(v1.3, 경로선택 없이 즉시 안내)이며 페이지 수정일은 2026-10-01이다. Android 규격은 [[air-external-integration-android-spec]], 목차는 [[air-internal-docs-and-integration-hub]]를 본다. 앱 개요는 [[inavi-air]]이다.

## 개정 이력

| 버전 | 날짜 | 내용 |
|---|---|---|
| 1.0 | 2019-05-03 | 아이나비 에어 연동가이드 초안 작성 |
| 1.1 | 2019-05-30 | 외부연동 인입채널 필드 추가 |
| 1.2 | 2024-01-03 | iOS13 Target 정보 변경 |
| 1.3 | 2026-09-14 | 경로선택 화면 없이 즉시 안내 연동 추가 |

## 개요

URL로 등록된 서비스를 호출하는 방식이다. 내장 앱뿐 아니라 Safari의 URL 호출, SMS/MMS로 받은 URL 등 원격 메시지로도 연동 요청을 처리할 수 있어 다양한 환경에 대응한다. 이 방식은 특정 앱에 작업을 요청만 할 수 있으므로, 응답을 받으려면 요청하는 앱도 같은 방식을 구현하고 그 정보를 알려야 한다(응답 대응은 별도 항목).

## 좌표계

경위도 좌표계(GPS 기준 WGS84)를 쓴다. 타원체는 장반경 6,378,137.0 m, 단반경 약 6,356,752.314245 m, 편평도(역수) 298.257223563이다. 자세한 설명은 공개 문서를 참조한다.

## URL 연동 규격

```
어플리케이션식별자://네임스페이스/요청클래스?method=요청메소드&인자1=값1&인자2=값2&....response=응답용어플리케이션식별자
```

| 구성 요소 | 규칙 |
|---|---|
| 인코딩 | URL에서 허용되지 않는 문자는 escape(%16진수) 처리 |
| 어플리케이션 식별자 | 스키마. 항상 `autorunair` (`autorunair://`) |
| 네임스페이스 | 현재 역할 없음. 통상 `thinkware.com` (`autorunair://thinkware.com`) |
| 요청 클래스 | 서비스 내 기본 작업/역할 범주. 끝에 반드시 `.req`를 붙임(request 약어, 상황에 따라 다른 약어 가능). 예: `autorunair://thinkware.com/requestclass.req` |
| 요청 메소드 | `method=요청메소드명`. 예: `...requestclass.req?method=callingmethod` |
| 인자 | `키=값&키=값` 형식. 요청 키 `method`, 응답 키 `callbackclass`, `callbackmethod`는 인자로 쓰면 안 됨. 예: `...?method=callingmethod&name=myname&key=x` |

### 어플리케이션 단순 실행

```
autorunair://
```

### 길 안내 요청

```
autorunair://thinkware.com/navigation.req?method=routesearch
&start=(출발지위도,출발지경도)&startname=출발지명칭&dest=(목적지위도,목적지경도)
&destname=목적지명칭&appid=앱식별ID&appscheme=앱URLScheme&appos=앱OS타입
```

경로선택 화면을 표출하는 예:

```
autorunair://thinkware.com/navigation.req?method=routesearch
&start=(33.00,124.00)&startname=판교역&dest=(43.00,132.00)
&destname=서울역&appid=com.inavi&appscheme=runinavi&appos=ios
```

경로선택 화면 없이 즉시 안내를 시작하는 예(`method=directguide`):

```
autorunair://thinkware.com/navigation.req?method=directguide
&start=(33.00,124.00)&startname=판교역&dest=(43.00,132.00)
&destname=서울역&appid=com.inavi&appscheme=runinavi&appos=ios
```

### 인자 설명

| 인자 | 필수 | 형식 | 설명 |
|---|---|---|---|
| `start` | 선택 | `start=(위도,경도)` 예 `(33.00,124.00)` | 출발지 위치. 없으면 현재 GPS 좌표 기준으로 길안내 |
| `startname` | 선택 | `startname=판교역` | 출발지 명칭. 없으면 현재 GPS 좌표 기준으로 출발지명 설정 |
| `dest` | 필수 | `dest=(위도,경도)` 예 `(43.00,132.00)` | 목적지 위치. 없으면 요청 자체를 오류로 처리 |
| `destname` | 선택 | `destname=서울역` | 목적지 명칭. 없으면 목적지 위치 기준으로 명칭 설정 |
| `appid` | 선택 | `appid=com.inavi` | 요청 앱(서비스) 식별 ID. 허가되지 않은 ID는 정책에 따라 연동이 중단될 수 있어 사전에 담당자와 협의 필요 |
| `appscheme` | 선택 | `appscheme=runinavi` | 요청 앱의 URL Scheme. 추후 요청 앱으로 돌아가는 시나리오에서 사용 예정 |
| `appos` | 선택 | `appos=ios` | 요청 앱의 OS 타입(ios, android, web 등) |

원문에는 `method` 인자의 별도 설명 표가 없으나 위 예시에서 `routesearch`와 `directguide` 두 값이 쓰인다. Android 규격([[air-external-integration-android-spec]])의 정의와 같다 ^[inferred]

## 앱 내에서의 연동 사전 작업

SMS/MMS/웹 페이지에서는 URL을 터치하면 연동되지만, 앱에서는 직접 호출해야 한다. 요청 정보 문자열을 만들었다면 다음과 같이 호출한다(`<요청정보문자열>`은 위 규격대로 구성).

```swift
let url = URL.init(string: '<요청정보문자열>')
UIApplication.shared.open(url, options: [], completionHandler: nil)
```

### 연동 기능의 제한

- iOS 13 이상을 지원한다.
- 호출하는 앱의 번들 ID를 호출 시점에 파악해 연동이 허가된 앱인지 판단한다.
- 허가되지 않은 앱은 연동을 제한할 수 있으며, 연동하려면 사전에 에어 담당자와 협의해야 한다.

## Android 규격과 인자명 차이

| 항목 | Android Scheme | iOS |
|---|---|---|
| 요청 클래스 | `navigation.req` (메소드 앞 `/?` 형식도 설명됨) | `navigation.req` |
| 출발지 좌표 | `startCoordinates` | `start` |
| 출발지 명칭 | `startName` | `startname` |
| 목적지 좌표 | `destCoordinates` | `dest` |
| 목적지 명칭 | `destName` | `destname` |
| 앱 요청 타입 | `appscheme`(요청 타입) | `appscheme`(앱 URL Scheme) |

## Related
- [[air-external-integration-android-spec]] — Android BroadcastReceiver/Scheme 규격
- [[inavi-air]] — 에어 앱 프로젝트
- [[air-partner-integrations-2023]] — 제휴사 연동
- [[air-internal-docs-and-integration-hub]] — 이 묶음 목차

## Sources
- Confluence "iNavi AIR iOS 연동 규격" (pageId 305168599) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
