---
title: "INAVI AIR API — 공통 (AIR)"
category: references
tags: [inavi-air, api, request-header, result-code, visibility/internal]
aliases: [공통 (AIR), AIR API 공통]
relationships:
  - target: "[[inavi-air-api-detail-spec]]"
    type: derived_from
sources: ["url:https://inavisystems.atlassian.net/wiki/spaces/AS/pages/2273968161"]
summary: >-
    AIR API 공통 규격(서버연동정보 구조, Request Header, 결과 코드, Push/Push Type, Popup, 공통 정보)을 Confluence에서 그대로 옮긴 페이지. 서버 주소는 미수록.
provenance:
  extracted: 1.0
  inferred: 0.0
  ambiguous: 0.0
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-27
tier: supporting
created: 2026-10-27T10:00:00+09:00
updated: 2026-10-27T10:00:00+09:00
---

# INAVI AIR API — 공통 (AIR)

Confluence "INAVI AIR API" > "공통 (AIR)" 페이지들을 요약 없이 그대로 옮긴 것이다. 허브는 [[inavi-air-api-detail-spec]], 제품 개요는 [[inavi-air]]를 본다.

## 목차

| 페이지 | page id | 비고 |
| --- | --- | --- |
| [[#공통 (AIR)\|공통 (AIR)]] | 2273968161 | 카테고리 부모 페이지 |
| [[#서버연동정보\|서버연동정보]] | 2262307959 | 서버 주소는 보안 규칙상 미수록 |
| [[#개발]] | 2262307983 | 본문 없음 |
| [[#상용]] | 2262307999 | 본문 없음 |
| [[#Request Header]] | 2262305999 | |
| [[#결과 코드]] | 2262306687 | |
| [[#Push 정보]] | 2262305900 | |
| [[#Push Type 정보]] | 2262305884 | |
| [[#Popup 정보]] | 2262305868 | 본문 없음 |
| [[#공통 정보]] | 2262307533 | |

## 공통 (AIR)
> Confluence page id: 2273968161 · 최종 수정: 10월 06, 2026

### 공통

- [[#서버연동정보|서버연동정보 (2)]]
- [[#Request Header|Request Header (2)]]
- [[#결과 코드|결과 코드]]
- [[#Push 정보|Push 정보]]
- [[#Push Type 정보|Push Type 정보]]
- [[#Popup 정보|Popup 정보]]
- [[#공통 정보|공통 정보]]

## 서버연동정보
> Confluence page id: 2262307959 · 최종 수정: 10월 06, 2026

> [!warning] 서버 주소는 보안 규칙상 미수록
> 원본 표의 IP, 호스트, 포트, URL은 `[HOST]`로 바꿨다. 경로(context path)와 표 구조만 남겼다.

### 접속 정보

#### 접속 정보

| 구분 | Protocol | KT 접속정보 | LG 접속정보 |
| --- | --- | --- | --- |
| 개발 | HTTP | [HOST]/UnitedInaviKT | [HOST]/UnitedInaviLG<br>[HOST]/UnitedInaviLG (로그전송용 API) |
| 상용 | HTTPS | [HOST]/UnitedInaviKT | [HOST]/UnitedInaviLG<br>[HOST]/UnitedInaviLG (로그전송용 API) |

#### 접속 정보

| 구분 | Protocol | AIR 접속정보 |
| --- | --- | --- |
| [[#개발\|개발]] | HTTP | [HOST]/INaviAir |
| [[#상용\|상용]] | HTTPS | [HOST]/INaviAir |

### 접속 방법

- 모든 Request 및 Response는 JSON을 기반으로 한다.

## 개발
> Confluence page id: 2262307983 · 최종 수정: 10월 01, 2026

(본문 없음 — "서버연동정보 (2)"의 하위 페이지)

## 상용
> Confluence page id: 2262307999 · 최종 수정: 10월 01, 2026

(본문 없음 — "서버연동정보 (2)"의 하위 페이지)

## Request Header
> Confluence page id: 2262305999 · 최종 수정: 10월 06, 2026

#### Request Header

| parameter | type | description | 상태 |
| --- | --- | --- | --- |
| method | String | POST | 운영 |
| Content-Type | String | application/json;charset=UTF-8 | 운영 |
| private\_key | String | 개인키 값 | 운영 |
| auth\_key | String | 인증키 값 | 운영 |
| os\_type | String | {Android / iOS} | 운영 |
| os\_ver | String | 해당 OS 버전 | 운영 |
| app\_ver | String | APP 버전 | 운영 |
| app\_vercode | String | APP 버전코드 | 운영 |
| device | String | 기기 모델명 | 운영 |
| mdn | String | 핸드폰 번호<br>KT보안 이슈로 인한 uk parameter 사용시 해당 값 공백처리 | 운영 |
| uk | String | AES-256으로 암호화된 핸드폰 번호<br>KT보안 이슈로 인한 parameter (KT전용) | 운영 |
| company | String | {KT / SKT / LG / ETC} | 운영 |
| sns\_key | String | SNS KEY값 | 운영 |
| ad\_id | String | Advertising ID값<br>Android : Google Advertising ID<br>iOS : Apple Advertising Identifier ("NONE"으로 입력) | 운영 |
| reg\_flag | String | s : sns privateKey로 즐겨찾기 처리하고자할경우, m : 모바일 프라이빗 키로 처리하고자 할경우<br>즐겨찾기 관련된 인터페이스 호출시 필수값 없으면 902내려감 | 운영 |
| serviceType | String | AIR : AIR3일경우<br>TMONEY : 온다택시 일경우 | 운영 |
| servicePackage | String | SERVICE APP 상세 구분을 위한 PACKAGE 이름 | 운영 |
| tmoney\_status | String | 티머니 헤더 온다택시일때만 보내면됨(동승여부) {0 : DEFAULT, 1 : 승객 위치 길 안내(승객 미 탑승), 2 : 목적지 길 안내(승객 탑승 중) } | 운영 |
| sdkAuthKey | String | SDK AUTH KEY([KEY_REMOVED] : 삼성중공업) | 운영 |
| shiWeightType | String | 삼성 중공업 전용 중량 타입 (1 : 4톤 미만, 2 : 4톤 이상) | 운영 |
| ivi\_flag | String | IVI 사용 여부 (1: 사용, 0: 사용안함) - Apple CarPlay or AndroidAuto | 신규 |

## 결과 코드
> Confluence page id: 2262306687 · 최종 수정: 10월 06, 2026

#### 결과코드

| error code | description | 속성 |
| --- | --- | --- |
| 0 | 성공 | 통합 |
| 1 | 탐색 실패 | 통합 |
| 3 | 목적지가 물리적 섬도로이며, 구축된 페리 항로가 없음 | 탐색 |
| 4 | 출발지가 선택이 안되었거나 잘못된 출발지 | 탐색 |
| 5 | 목적지가 선택이 안되었거나 잘못된 목적지 | 탐색 |
| 6 | 경유지 선택이 안되었거나 잘못된 경유지 | 탐색 |
| 7 | 경유지 또는 목적지가 차량의 높이/중량 제한으로 갈 수 없음 | 탐색 |
| 8 | 경유지 또는 목적지가 시간제 통행금지로 인해 갈 수 없음 | 탐색 |
| 9 | 탐색에 필요한 기본 데이터가 초기화 되어 있지 않다. (회피경로등에 사용) | 탐색 |
| 10 | 출발 또는 목적지가 논리적(교통) 섬이며, 목적지가 2개 이상인 경우 (다중 목적지인 경우 목적지 이동 탐색을 하지 않고 바로 실패) | 탐색 |
| 11 | 공유메모리 관련 실패 | 탐색 |
| 15 | 파일 열기 실패 | 탐색 |
| 16 | 탐색 확장 가능 개수를 넘었다 | 탐색 |
| 17 | 메모리 할당 실패 | 탐색 |
| 19 | 파일 읽기 실패 | 탐색 |
| 20 | 파일 쓰기 실패 | 탐색 |
| 21 | 지도 데이터가 유효하지 않다. | 탐색 |
| 22 | 탐색 요청인자가 유효하지 않다 | 탐색 |
| 23 | projection fail | 탐색 |
| 24 | max thread reached | 탐색 |
| 25 | 탐색파일 저장실패(db) | 탐색 |
| 32 | 탐색 가능 거리 초과(국내의 경우 700km / 도보의 경우 20km / 대중교통의 경우 700km) | 탐색 |
| 35 | 선택하신 지점이 너무 가깝습니다. |  |
| 36 | 지원하지 않는 지점입니다. 목적지 확인 후 다시 시도해 주세요. | 탐색 |
| 39 | 탐색은 성공하지 않았는데 더 이상 확장할 node가 없을 때 | 탐색 |
| 40 | 출발지 또는 경유지 근처의 차량 높이/중량 제한으로 확장 실패 | 탐색 |
| 41 | 출발지 또는 경유지 근처의 시간제 통행금지로 인해 확장 실패 | 탐색 |
| 42 | 시간제 통행금지로 인해 확장 실패 | 탐색 |
| 43 | 페리항로 미구축 지역이라 차량으로 진입할 수 없는 도서지역입니다. 목적지를 확인해주세요. | 탐색 |
| 46 | 출발지 근처 시간제 통행금지로 인해 확장 실패 | 탐색 |
| 47 | 목적지 근처 시간제 통행금지로 인해 확장 실패 | 탐색 |
| 48 | 소켓 연결 실패 | 탐색 |
| 49 | 결과 생성 실패 | 탐색 |
| 96 | 잘못된 route\_id (다중경로 탐색 시 상세 요청에 route\_id가 잘못된 경우) | 탐색 |
| 97 | 체크섬 실패 | 탐색 |
| 98 | 재탐색 체크 라이브러리 실패 | 탐색 |
| 112 | 옵션 파일 Read Error | 탐색 |
| 113 | 옵션파일의 버전이 엔진의 것보다 높은 버전 | 탐색 |
| 114 | 옵션파일이 버전이 엔진의 것보다 낮은 버전 | 탐색 |
| 120 | 현재 안내 경로가 최적경로입니다 ※스마트 재탐색 후 더 좋은 경로가 탐색되지 않은 경우 | 탐색 |
| 121 | 목적지 부근으로 재탐색이 필요하지 않은 경우 | 탐색 |
| 122 | 재탐색 결과가 동일하지만 도착시간 차이가 커서 다시 경로를 내려주는 경우 | 탐색 |
| 200 | 인증된 시리얼 번호가 아닙니다. | HUD |
| 300 | 서비스 미지원 | 통합 |
| 400 | 온에어 수신 상태 | 온에어 |
| 401 | 수신하지 않은 온에어 정보 | 온에어 |
| 402 | 이미 수신 완료한 온에어 정보 | 온에어 |
| 403 | 조회 조건에 해당하는 온에어 음성 정보 미존재 | 온에어 |
| 501 | 잔여 캐시 부족 | 에어 캐시 |
| 502 | 에어 마일 오류 | 에어 캐시 |
| 601 | 통신사(LG) 인증 실패 | LG |
| 602 | 통신사(LG) 부가서비스 미 가입 | LG |
| 603 | 통신사(LG) 부가서비스 가입 실패 | LG |
| 604 | 통신사(LG) 부가서비스 일일 중복 가입 불가 | LG |
| 610 | w3w 단어 검색 파라미터 오류 | w3w |
| 630 | 캐시버튼 연동 오류 | 캐시버튼 |
| 760 | 등록지점 관련 에러 : server보다 최신의 ts 요청(단말에서 초기화 요청 및 file 초기화 필요) | 즐겨찾기 |
| 761 | 등록지점 관련 에러 : server에 없는 data 삭제 요청 | 즐겨찾기 |
| 762 | 즐겨찾기를 더 이상 등록 할 수 없습니다. | 즐겨찾기 |
| 763 | 이미 존재 하는 LabelId 입니다 | 즐겨찾기 |
| 764 | 이미 존재 하는 즐겨찾기 입니다.\\n다른 이름으로 다시 시도해 주세요. | 즐겨찾기 |
| 765 | 즐겨찾기 라벨을 더 이상 등록 할 수 없습니다. | 즐겨찾기 |
| 800 | CDN 파일 저장 에러 | 통합 |
| 888 | SNS로그인 실패 | SNS로그인 |
| 889 | 이미 사용 중인 계정 입니다. | SNS로그인 |
| 900 | 인증 실패 | 통합 |
| 901 | 개인키 오류 | 통합 |
| 902 | 입력 파라미터 오류 | 통합 |
| 903 | 조회결과 없음 | 통합 |
| 904 | 존재하지 않는 파일 | 통합 |
| 905 | DB 연동 에러 | 통합 |
| 907 | RID에 해당하는 탐색 데이타가 없는 경우 | 통합 |
| 910 | 유고 서버 연동 오류 | 유고 |
| 912 | 유가 서버 연동 오류 | 유가 |
| 917 | 안내 서버 연동 오류 | 안내 |
| 918 | 탐색 서버 연동 오류 | 탐색 |
| 919 | 검색 서버 연동 오류 | 검색 |
| 920 | 오류 - 해당 문구로 팝업 메시지 표출 | 검색 |
| 921 | 오르다 서버 연동 오류 |  |
| 930 | 국가 보안시설물 검색 오류 | 검색 |
| 931 | 위/경도 검색 오류 | 검색 |
| 932 | 휴대폰번호 검색 오류 | 검색 |
| 933 | 잘못된 쿼리 오류 | 검색 |
| 934 | POI not in given Admin | 검색 |
| 935 | POI not in given Area | 검색 |
| 936 | POI not in given Category | 검색 |
| 937 | Internal Server Error | 검색 |
| 938 | Neighbor Search Only | 검색 |
| 968 | CAS(LG) 서버 연동 오류 | LG |
| 969 | LBSP(LG) 서버 연동 오류 | LG |
| 970 | 에어 캐시 정합성 체크 실패 (캐시 어뷰징 의심) | 에어 캐시 |
| 971 | 유효하지 않은 캐시 스탬프 date | 에어 캐시 |
| 972 | 에어캐시 스탬프 룰렛 이용권 미존재 | 에어캐시 |
| 980 | 이미 지급한 사용자 |  |
| 665 | 그룹주행방 더이상 존재하지 않음 | AIR |
| 666 | 그룹주행방 가득참 | AIR |
| 999 | 정의되지 않은 오류 | 통합 |

## Push 정보
> Confluence page id: 2262305900 · 최종 수정: 10월 06, 2026

> [!note] 보안 처리
> 원본 예시의 이미지 CDN 주소(`iu`)와 연동 URL(`url`) 값은 `[URL]`로 바꿨다.

### Definition

> Push Notification Message를 정의 합니다.

### 1. 일반 실행형

```
- Android
{
    "nt" : "Notification Title",  // Notification 영역의 제목
    "pt": "Popup Title",         // 팝업 제목
    "pc": "Popup Content",       // 팝업 내용
    "type": "A",                 // A : 일반 실행
		"iu" : "[URL]"   //image url
}

- iOS
{
    "aps" : { "alert" : "Notification Title" },  // Notification 영역의 제목
    "pt": "Popup Title",         // 팝업 제목
    "pc": "Popup Content",       // 팝업 내용
    "type": "A",                 // A : 일반 실행
		"iu" : "[URL]"   //image url
}
```

### 2. 모바일 웹 연동형

```
- Android
{
    "nt" : "Notification Title",  // Notification 영역의 제목
    "pt": "Popup Title",         // 팝업 제목
    "pc": "Popup Content",       // 팝업 내용
    "url": "[URL]",
    "type": "B",                 // B : 외부 브라우저 URL 연동
		"iu" : "[URL]"   //image url
}

- iOS
{
    "aps" : { "alert" : "Notification Title" },  // Notification 영역의 제목
    "pt": "Popup Title",         // 팝업 제목
    "pc": "Popup Content",       // 팝업 내용
    "url": "[URL]",
    "type": "B",                  // B : 외부 브라우저 URL 연동
		"iu" : "[URL]"   //image url
}
```

### 3. 내부 WebView 연동형

```
- Android
{
    "nt" : "Notification Title",  // Notification 영역의 제목
    "pt": "Popup Title",         // 팝업 제목
    "pc": "Popup Content",       // 팝업 내용
    "url": "[URL]", // url 존재 : 전달해준 URL로 웹뷰 연결, url Empty String : 이벤트/공지사항으로 연결
    "type": "D",                   // D : 내부 WebView URL 연동
		"iu" : "[URL]"   //image url
}

- iOS
{
    "aps" : { "alert" : "Notification Title" },  // Notification 영역의 제목
    "pt": "Popup Title",                         // 팝업 제목
    "pc": "Popup Content",                       // 팝업 내용
    "url": "[URL]",              // url 존재 : 전달해준 URL로 웹뷰 연결, url Empty String : 이벤트/공지사항으로 연결
    "type": "D",                                // D : 내부 WebView URL 연동
		"iu" : "[URL]"   //image url
}
```

### 4. 앱 특정 화면 표출형

```
- Android
{
    "nt" : "Notification Title",                  // Notification 영역의 제목
    "pt": "Popup Title",                          // 팝업 제목
    "pc": "Popup Content",                        // 팝업 내용
    "type": "E",                                  // E : 앱 특정 화면 표출
		"iu" : "[URL]",   //image url
    "subtype": "CI"                               // CI : 자정 전 - 캐시정보 조회 화면, 자정 후 - 적립 스탬프 조회 화면 (미 로그인 사용자의 경우 로그인 화면으로 진입)
}

- iOS
{
    "aps" : { "alert" : "Notification Title" },  // Notification 영역의 제목
    "pt": "Popup Title",                         // 팝업 제목
    "pc": "Popup Content",                       // 팝업 내용
    "type": "E",                                 // E : 앱 특정 화면 표출
		"iu" : "[URL]",   //image url
    "subtype": "CI"                             // CI : 자정 전 - 캐시정보 조회 화면, 자정 후 - 적립 스탬프 조회 화면 (미 로그인 사용자의 경우 로그인 화면으로 진입)
}
```

### 5. 티머니onda 목적지 탐색

```
- Android
{
    "nt" : "Notification Title",  // Notification 영역의 제목
    "pt": "Popup Title",         // 팝업 제목
    "pc": "Popup Content",       // 팝업 내용
    "type": "S",
    "callID": "Call Id",        // 사용자 Call ID
    "startLoc": "Start Location",    // 출발지 지점 정보
    "endLoc": "End Location",    // 도착지 지점 정보
    "viaLocs": "Via Locations",    // 경유지 지점 정보
    "status": "Status",    // 승객 탑승 여부(1: 승객 위치 길 안내(승객 미탑승), 2: 목적지 길 안내(승객 탑승 중), 4: 예측 탐색)
    "payType": "Pay Type",    // 지불 타입(A: 자동 결제, D: 직접결제)
    "routeType": "Search Option"   // 탐색 옵션(recommendation : 추천길, time_priority : 최소, real_traffic_freeroad : 무료길)
}

- iOS
{
    "aps" : { "alert" : "Notification Title" },  // Notification 영역의 제목
    "pt": "Popup Title",         // 팝업 제목
    "pc": "Popup Content",       // 팝업 내용
    "type": "S",
    "callID": "Call Id",        // 사용자 Call ID
    "startLoc": "Start Location",    // 출발지 지점 정보
    "endLoc": "End Location",    // 도착지 지점 정보
    "viaLocs": "Via Locations",    // 경유지 지점 정보
    "status": "Status",    // 승객 탑승 여부(1: 승객 위치 길 안내(승객 미탑승), 2: 목적지 길 안내(승객 탑승 중), 4: 예측 탐색)
    "payType": "Pay Type",    // 지불 타입(A: 자동 결제, D: 직접결제)
    "routeType": "Search Option"   // 탐색 옵션(recommendation : 추천길, time_priority : 최소, real_traffic_freeroad : 무료길)
}
```

### 6. 티머니onda 목적지 탐색 취소

```
- Android
{
    "nt" : "Notification Title",  // Notification 영역의 제목
    "pt": "Popup Title",         // 팝업 제목
    "pc": "Popup Content",       // 팝업 내용
    "type": "X",
    "callId": "Call Id",    // 사용자 Call ID
    "status": "Status",    // 승객 탑승 여부(1: 승객 위치 길 안내(승객 미탑승), 2: 목적지 길 안내(승객 탑승 중)
    "cancelType": "Cancel Type"    // 취소 타입(D: 일반 취소, P: 지불 취소, C: 승객 신고)
}

- iOS
{
    "aps" : { "alert" : "Notification Title" },  // Notification 영역의 제목
    "pt": "Popup Title",         // 팝업 제목
    "pc": "Popup Content",       // 팝업 내용
    "type": "X",
    "callId": "Call Id",    // 사용자 Call ID
    "status": "Status",    // 승객 탑승 여부(1: 승객 위치 길 안내(승객 미탑승), 2: 목적지 길 안내(승객 탑승 중)
    "cancelType": "Cancel Type"    // 취소 타입(D: 일반 취소, P: 지불 취소, C: 승객 신고)
}
```

## Push Type 정보
> Confluence page id: 2262305884 · 최종 수정: 10월 06, 2026

### Definition

> Push type 를 정의 합니다.

| Type | Definition |
| --- | --- |
| A | 일반 실행 |
| B | 모바일 웹 연동형 (외부 브라우저 URL 연동) |
| C | 탐색 |
| D | 내부 WebView 연동형 |
| E | 앱 특정 화면 표출 |

## Popup 정보
> Confluence page id: 2262305868 · 최종 수정: 10월 06, 2026

(본문 없음 — 원본 페이지에 빈 문단만 있다. 요약에는 문서 분류 라벨 "AIR API 공통 문서 분류"만 표시된다.)

## 공통 정보
> Confluence page id: 2262307533 · 최종 수정: 10월 06, 2026

> [!note]
> 💡공통 정보로 보내지는 내용은 API 호출 시 보내는 CommonRequestHeader 의 정보를 통해 자동으로 생성되는 정보

#### Request Parameter

| parameter | type | requisite | description | 상태 |
| --- | --- | --- | --- | --- |
| UniqKey | String | 제목 없음 | 사용자 식별을 위한 고유키 | 운영 |
| DeviceName | String | 제목 없음 | 디바이스 명칭 | 운영 |
| Device | String | 제목 없음 | 단말기 OS - Android / iOS / AppleCarplay / AndroidAuto | 변경 |
| ISP | String | 제목 없음 | 통신사 구분 - AIR: AIR3 / TMONEY: 온다 택시 / SDK\_AIR: (SDK\_AIR/고객사Keycode) | 변경 |
| OSVer | String | 제목 없음 | OS Version 구분 | 운영 |
| Category | String | 제목 없음 | 로그종류 식별 문자열 - AirEvent / AirStatEvent / AirExtEvent | 운영 |
| CUR\_X/CUR\_Y | String | 제목 없음 | 현위치 X/Y 좌표 | 운영 |
| Ad-ID | String | 제목 없음 | 안드로이드 Ad-ID (iOS 계열은 NONE으로 고정) | 운영 |
| Op | String | 제목 없음 | 동작구분 | 운영 |
| Time | String | 제목 없음 | 로그가 발생한 시간 | 운영 |
| Log | String | 제목 없음 | 로그 내용 | 운영 |
| AppVer | String | 제목 없음 | App Version 정보 | 운영 |

## Sources
- Confluence "INAVI AIR API" > 공통 (AIR) (2026-10-27 조회): 공통 (AIR) (2273968161), 서버연동정보 (2) (2262307959), 개발 (2262307983), 상용 (2262307999), Request Header (2) (2262305999), 결과 코드 (2262306687), Push 정보 (2262305900), Push Type 정보 (2262305884), Popup 정보 (2262305868), 공통 정보 (2262307533)
