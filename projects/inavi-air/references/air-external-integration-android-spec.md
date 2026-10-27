---
title: >-
    아이나비 에어 Android 외부 연동 규격
category: references
project: inavi-air
tags: [air, android, integration, broadcast-receiver, url-scheme, visibility/internal]
aliases: [iNavi AIR Android 연동 규격, 에어 외부 연동 규격]
relationships:
  - target: "[[inavi-air]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/305397799
summary: >-
    에어 Android 외부 연동 규격(v1.5, 2026-09). WGS84 좌표계, BroadcastReceiver 규격과 상수, 단순 실행/길 안내/즉시 안내 요청, autorunair Scheme, Geo Scheme를 정리.
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

# 아이나비 에어 Android 외부 연동 규격

외부 앱이 Android용 아이나비 에어(`com.thinkware.inaviair`)를 실행하거나 길 안내를 요청하는 방법을 정의한 규격이다. 마지막 개정은 2026-09-14(v1.5, 경로선택 없이 즉시 안내)이다. iOS 규격은 [[air-external-integration-ios-spec]], 전체 목차는 [[air-internal-docs-and-integration-hub]]를 본다. 앱 개요는 [[inavi-air]]를 참고한다.

## 개정 이력

| 버전 | 날짜 | 내용 |
|---|---|---|
| 1.0 | 2019-05-30 | 아이나비 에어 연동가이드 초안 작성 |
| 1.1 | 2019-05-13 | 어플리케이션 단순 실행 기능 추가, Geo Scheme 연동 추가 ^[ambiguous] 날짜가 1.0보다 앞서 있음 |
| 1.2 | 2019-05-30 | 외부연동 인입채널 필드 추가 |
| 1.3 | 2020-02-10 | 외부연동 사용 I/F 변경 |
| 1.4 | 2024-01-03 | 문서 형태 변경 |
| 1.5 | 2026-09-14 | 경로선택 화면 없이 즉시 안내 연동 추가 |

## 개요

안드로이드 기반 플랫폼에서 구동되는 아이나비 에어와 외부 프로그램의 연동을 기술한다. 에어가 쓰는 좌표계, 제공하는 정보와 기능을 정리해 외부 프로그램이 쉽게 활용하도록 하는 것이 목적이다.

## 좌표계

- 외부 연동은 **WGS84 좌표계**를 쓴다. GPS 신호, 구글 맵 등 다른 위치 기반 서비스와 연동하기 유리하기 때문이다.
- WGS84 지구 타원체: 장반경 6,378,137.0 m, 단반경 약 6,356,752.314245 m, 편평도(역수) 298.257223563.
- 좌표계 자체 설명은 공개 문서(위키피디아)를 참조하도록 하고 본문에는 싣지 않는다.

## BroadcastReceiver 연동 규격

연동하려는 모든 앱은 Broadcast 요청 방식을 써야 한다.

1. **에어 구동**: intent와 sendBroadcast로 특정 동작을 요청하면 에어의 BroadcastReceiver가 action을 받아, 에어가 실행 중이 아니어도 앱을 실행시킨다.
2. Oreo 대응 업데이트로 **암시적 Broadcast는 불가**하다. intent에 실행할 앱의 패키지명과 클래스명(통신사에 따라 다름)을 설정한 **명시적 Broadcast**로 요청해야 한다.

### 상수 정의

```java
public static final String PACKAGE_NAME = "com.thinkware.inaviair";
public static final String RECEIVER_NAME = "com.thinkware.inaviair.receiver.NaviReceiver";
public static final String ACTION_AIR_EXTERNAL = "inaviair.external.action.EXTERNAL";
public static final String EXTRA_AIR_EXTERNAL_KIND = "inaviair.external.extra.KIND";
public static final String EXTERNAL_TYPE_APP_LAUNCHING = "APP_LAUNCHING";
public static final String EXTERNAL_TYPE_ROUTE_SEARCH = "ROUTE_SEARCH";
public static final String EXTERNAL_TYPE_DIRECT_GUIDE = "DIRECT_GUIDE";
public static final String EXTRA_AIR_EXTERNAL_START_NAME = "inaviair.external.extra.START_NAME";
public static final String EXTRA_AIR_EXTERNAL_START_COORDINATES = "inaviair.external.extra.START_COORDINATES";
public static final String EXTRA_AIR_EXTERNAL_DEST_NAME  = "inaviair.external.extra.DEST_NAME";
public static final String EXTRA_AIR_EXTERNAL_DEST_COORDINATES = "inaviair.external.extra.DEST_COORDINATES";
public static final String EXTRA_AIR_EXTERNAL_APP_ID     = "inaviair.external.extra.APP_ID";
public static final String EXTRA_AIR_EXTERNAL_APP_SCHEME = "inaviair.external.extra.APP_SCHEME";
public static final String EXTRA_AIR_EXTERNAL_APP_OS     = "inaviair.external.extra.APP_OS";
```

### 요청 종류(KIND)

| KIND 값 | 동작 |
|---|---|
| `APP_LAUNCHING` | 어플리케이션 단순 실행 |
| `ROUTE_SEARCH` | 길 안내 요청(경로선택 화면 표출) |
| `DIRECT_GUIDE` | 경로선택 화면 없이 추천 경로로 즉시 안내(v1.5 추가) |

### 길 안내 요청 인자(Extra)

| Extra | 필수 | 타입 | 설명 |
|---|---|---|---|
| `DEST_NAME` | 선택 | String | 목적지 명칭. 입력하지 않으면 행정동 명칭으로 탐색 |
| `DEST_COORDINATES` | 필수 | double[2] | 목적지 좌표 `[위도, 경도]` |
| `START_NAME` | 선택 | String | 출발지 명칭. 입력하지 않으면 행정동 명칭 |
| `START_COORDINATES` | 선택 | double[2] | 출발지 좌표 `[위도, 경도]`. 지정하지 않으면 현위치에서 출발 |
| `APP_ID` | 선택 | String | 요청한 앱(서비스)의 식별 ID (예: `com.inavi`) |
| `APP_OS` | 선택 | String | 요청한 앱의 OS (예: `android`) |
| `APP_SCHEME` | 선택 | String | 요청한 앱의 요청 타입 (예: `runinavi`) |

경유지 지정은 지원하지 않는다.

### 1) 어플리케이션 단순 실행

패키지와 외부 연동 타입만 넣는다.

```java
Intent intent = new Intent(ACTION_AIR_EXTERNAL);
intent.setClassName(PACKAGE_NAME, RECEIVER_NAME);
intent.putExtra(EXTRA_AIR_EXTERNAL_KIND, EXTERNAL_TYPE_APP_LAUNCHING);
sendBroadcast(intent);
```

### 2) 길 안내 요청

```java
Intent intent = new Intent(ACTION_AIR_EXTERNAL);
intent.setClassName(PACKAGE_NAME, RECEIVER_NAME);
intent.putExtra(EXTRA_AIR_EXTERNAL_KIND, EXTERNAL_TYPE_ROUTE_SEARCH);
//목적지 설정 (필수 항목)
double[] destCoordinates = new double[2];
destCoordinates[0] = 35.1152182;
destCoordinates[1] = 129.0400702;
intent.putExtra(EXTRA_AIR_EXTERNAL_DEST_NAME, "부산역");
intent.putExtra(EXTRA_AIR_EXTERNAL_DEST_COORDINATES, destCoordinates);
// 출발지 설정 (선택 항목)
double[] startCoordinates = new double[2];
startCoordinates[0] = 37.5536109;
startCoordinates[1] = 126.9674308;
intent.putExtra(EXTRA_AIR_EXTERNAL_START_NAME, "서울역");
intent.putExtra(EXTRA_AIR_EXTERNAL_START_COORDINATES, startCoordinates);
// 외부연동 인입 채널 설정 (선택 항목)
intent.putExtra(EXTRA_AIR_EXTERNAL_APP_ID, "com.inavi" );    //요청한 앱(서비스)의 식별 ID
intent.putExtra(EXTRA_AIR_EXTERNAL_APP_OS, "android" );      // 요청한 앱의 OS
intent.putExtra(EXTRA_AIR_EXTERNAL_APP_SCHEME, "runinavi" ); //요청한 앱의 요청 타입
sendBroadcast(intent);
```

### 3) 길 안내 요청 (경로선택 화면 없이 즉시 안내 시작)

추천 경로로 바로 안내를 시작한다. KIND만 `EXTERNAL_TYPE_DIRECT_GUIDE`로 바꾸고 나머지 인자 규격은 2)와 동일하다.

```java
Intent intent = new Intent(ACTION_AIR_EXTERNAL);
intent.setClassName(PACKAGE_NAME, RECEIVER_NAME);
intent.putExtra(EXTRA_AIR_EXTERNAL_KIND, EXTERNAL_TYPE_DIRECT_GUIDE);   // 이 값만 다르다
//목적지 설정 (필수 항목)
double[] destCoordinates = new double[2];
destCoordinates[0] = 35.1152182;
destCoordinates[1] = 129.0400702;
intent.putExtra(EXTRA_AIR_EXTERNAL_DEST_NAME, "부산역");
intent.putExtra(EXTRA_AIR_EXTERNAL_DEST_COORDINATES, destCoordinates);
// 출발지 설정 (선택 항목)
double[] startCoordinates = new double[2];
startCoordinates[0] = 37.5536109;
startCoordinates[1] = 126.9674308;
intent.putExtra(EXTRA_AIR_EXTERNAL_START_NAME, "서울역");
intent.putExtra(EXTRA_AIR_EXTERNAL_START_COORDINATES, startCoordinates);
// 외부연동 인입 채널 설정 (선택 항목)
intent.putExtra(EXTRA_AIR_EXTERNAL_APP_ID, "com.inavi" );
intent.putExtra(EXTRA_AIR_EXTERNAL_APP_OS, "android" );
intent.putExtra(EXTRA_AIR_EXTERNAL_APP_SCHEME, "runinavi" );
sendBroadcast(intent);
```

유의사항: `EXTERNAL_TYPE_DIRECT_GUIDE` 사용 시 탐색 옵션은 에어 앱 내 기본탐색옵션 설정과 무관하게 항상 **"에어 추천"으로 고정**된다.

## Scheme 연동 규격

모바일 웹에서 호출하는 URL 규격이다. 앱에서 앱으로 연동하는 기본 방식은 위의 BroadcastReceiver이다. 모든 좌표는 위경도 기준이다.

### 기본 형식

```
어플리케이션식별자://네임스페이스/?method=요청메소드&인자1=값1&인자2=값2
```

- URL에서 허용되지 않는 문자는 escape(%16진수) 처리하며 인코딩은 **UTF-8**이다.
- 어플리케이션 식별자(스키마): 항상 `autorunair`. 예: `autorunair://`
- 네임스페이스(네트워크 로케이션): 현재 아무 역할이 없으며 `thinkware.com`으로 적어둔다. 예: `autorunair://thinkware.com`
- 요청 메소드: `method=요청메소드명` 형태. 예: `autorunair://thinkware.com/?method=callingmethod`
- 인자: `키=값&키=값` 형식. 요청 메소드 키 `method`와 응답 규격 키 `callbackmethod`는 인자로 쓰면 안 된다. 예: `autorunair://thinkware.com/navigation.req?method=routesearch&name=myname&key=x`

| Method명 | 설명 |
|---|---|
| `routesearch` | 경로 탐색 요청(경로선택 화면 표출) |
| `directguide` | 경로 탐색 및 즉시 안내 시작 요청(경로선택 화면 미표출) |

### 어플리케이션 단순 실행

```
autorunair://
```

### 길 안내 요청

```
autorunair://thinkware.com/navigation.req?method=요청메소드&destName=목적지명칭&destCoordinates=(목적지위도,목적지경도)&startName=출발지명칭&startCoordinates=(출발지위도,출발지경도)&appid=앱식별ID&appscheme=앱요청타입&appos=앱OS타입
```

예시(경로선택 화면 표출):

```
autorunair://thinkware.com/navigation.req?method=routesearch&destName=부산역&destCoordinates=(35.1152182,129.0400702)&startName=서울역&startCoordinates=(37.5536109,126.9674308)&appid=com.inavi&appscheme=runinavi&appos=android
```

예시(즉시 안내):

```
autorunair://thinkware.com/navigation.req?method=directguide&destName=부산역&destCoordinates=(35.1152182,129.0400702)&startName=서울역&startCoordinates=(37.5536109,126.9674308)&appid=com.inavi&appscheme=runinavi&appos=android
```

### 인자 설명

| 인자 | 필수 | 형식 | 설명 |
|---|---|---|---|
| `method` | 필수 | `method=routesearch` / `method=directguide` | `routesearch`는 경로 탐색 후 경로선택 화면을 표출(사용자가 경로를 골라야 안내 시작). `directguide`는 추천 경로로 즉시 안내. 두 메소드의 나머지 인자 규격은 동일 |
| `destName` | 선택 | `destName=부산역` | 목적지 이름 |
| `destCoordinates` | 필수 | `destCoordinates=(위도, 경도)` 예 `(36.45, 125.25)` | 목적지 위치. 없으면 요청 자체를 오류로 처리 |
| `startName` | 선택 | `startName=서울역` | 출발지 이름 |
| `startCoordinates` | 선택 | `startCoordinates=(위도, 경도)` | 출발지 위치. 원문 형식 설명에 "목적지 위도, 목적지 경도"라고 적혀 있으나 출발지 좌표를 뜻한다 ^[ambiguous] |
| `appid` | 선택 | `appid=com.inavi` | 요청 앱(서비스) 식별 ID. 허가되지 않은 ID는 정책에 따라 연동이 중단될 수 있어 사전에 담당자와 협의 필요 |
| `appscheme` | 선택 | `appscheme=runinavi` | 요청 앱의 요청 타입. 추후 요청 앱으로 돌아가는 시나리오에서 사용 예정 |
| `appos` | 선택 | `appos=android` | 요청 앱의 OS 타입(ios, android, web 등) |

## Geo Scheme 외부 연동

Android Google Maps에서 쓰는 Geo Scheme으로 에어와 연동한다. 안드로이드 개발자 사이트의 외부 연동 내용을 발췌한 것이다.

```
geo:0,0?q=my+street+address
- Show the location for "my street address" (may be a specific address or location query).
Example: "geo:0,0?q=1600+Amphitheatre+Parkway%2C+CA"
Note: All strings passed in the geo URI must be encoded. For example, the string 1st & Pike, Seattle should become 1st%20%26%20Pike%2C%20Seattle. Spaces in the string can be encoded with %20 or replaced with the plus sign (+).
```

주소·명칭 통합검색은 `geo:0,0?q=검색어` 형식으로 요청한다.

```java
Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse("geo:0,0?q=서울역"));
intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
startActivity(intent);
```

## Related
- [[air-external-integration-ios-spec]] — iOS URL scheme 규격(같은 `autorunair` 스키마, 인자명이 다름)
- [[inavi-air]] — 에어 앱 프로젝트 개요
- [[air-partner-integrations-2023]] — 제휴사 연동 사례
- [[air-internal-docs-and-integration-hub]] — 이 묶음 목차

## Sources
- Confluence "iNavi AIR Android 연동 규격" (pageId 305397799) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
