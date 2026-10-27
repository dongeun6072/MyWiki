---
title: "INAVI AIR API — AIR 서비스"
category: references
tags: [inavi-air, api, service-gate, terms, visibility/internal]
aliases: [AIR 서비스]
relationships:
  - target: "[[inavi-air-api-detail-spec]]"
    type: derived_from
sources: ["url:https://inavisystems.atlassian.net/wiki/spaces/AS/pages/2262305686"]
summary: >-
    INAVI AIR 앱 서비스 API 명세 원문 전사. 서비스 메인(/serviceGate) 응답 전 항목, 이용 약관 조회·동의 및 개인 키 생성, 지도 다운로드 정보 조회를 담는다.
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

# INAVI AIR API — AIR 서비스

Confluence "AIR 서비스" 페이지들을 요약 없이 그대로 옮긴 원문 전사본이다. 허브는 [[inavi-air-api-detail-spec]], 공통 헤더·결과 코드는 [[inavi-air-api-common]], 서비스 개요는 [[inavi-air]]를 본다. 다른 서비스의 serviceGate 구성과 비교하려면 [[orbismap-api-docs]]를 본다.

| API | URL |
| --- | --- |
| [[#이용 약관 조회(AIR)]] | `/clauseCheck` |
| [[#이용 약관 동의 및 개인 키 생성(AIR)]] | `/clauseAgree` |
| [[#지도 다운로드 정보 조회(AIR)]] | `/mapDownloadInfo` |
| [[#서비스 메인(AIR)]] | `/serviceGate` |

## 개요
> Confluence page id: 2262305686 · 최종 수정: 10월 06, 2026

상위 페이지 "AIR 서비스" 본문은 하위 API 링크 목록이다(원본 순서 그대로).

- 🧭이용 약관 조회(AIR)
- 🧭이용 약관 동의 및 개인 키 생성(AIR)
- 🧭지도 다운로드 정보 조회(AIR)
- 🧭서비스 메인(AIR)

## 이용 약관 조회(AIR)
> Confluence page id: 2262305752 · 최종 수정: 10월 01, 2026

### Function

> 이용약관 조회Request Header 중 개인키, 인증키 값 없이 호출

### URL

> `/clauseCheck`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

> 원본 표가 비어 있음

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |
| total\_ver | String | 이용약관 통합 버전 |
| url\_list | Array | 이용약관 리스트 (기존 약관 리스트) |
| ┣ url\_name | String | 이용약관 번호termNew1 : 개인정보 처리방침 \[필수\]termNew2 : 서비스 및 위치정보 이용약관 \[필수\]termNew3 : 개인정보 수집 동의 \[필수\]termNew4 : 만 14세 이상 이용 동의 \[필수\]termNew5 : 정보 및 광고수신 동의 \[선택\] |
| ┗ url\_path | String | 이용약관 URL |
| url\_list\_v2 | Array | 이용약관 리스트 (신규 약관 리스트) |
| ┣ url\_name | String | 이용약관 번호termLatest1 : 서비스 및 위치정보 이용약관 \[필수\]termLatest2 : 개인정보 수집·이용 동의 \[필수\]termLatest3 : 만 14세 이상 이용 동의 \[필수\]termLatest4 : 개인정보 제3자 제공 동의 \[선택\]termLatest5 : 정보 및 광고수신 동의 \[선택\]termLatest6 : 개인정보 처리방침 |
| ┗ url\_path | String | 이용약관 URL |

## 이용 약관 동의 및 개인 키 생성(AIR)
> Confluence page id: 2262305732 · 최종 수정: 10월 01, 2026

### Function

> 이용약관 동의 및 개인키 생성Request Header 중 개인키, 인증키 값 없이 호출

### URL

> `/clauseAgree`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| device\_id | String | O | 단말 고유 값Android : IMEIiOS : UUID |
| ip | String |  | 단말 IP (iOS일 경우만) |
| mymenu\_status | String | O | 마이메뉴 동의 여부0 : 동의안함1 : 동의함 |
| ad\_status | String | O | 광고 수신 동의 여부0 : 동의안함1 : 동의함 |
| prov\_status | String | O | 개인정보 3자 제공 동의 여부0 : 동의안함1 : 동의함 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |
| private\_key | String | 개인키 |
| company | String | 통신사KT / SKT / LGU / ETC |

## 지도 다운로드 정보 조회(AIR)
> Confluence page id: 2262305772 · 최종 수정: 10월 01, 2026

### Function

> 지도 다운로드 정보 조회Request Header 중 인증키 값 없이 호출

### URL

> `/mapDownloadInfo`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| smr\_ver | String |  | SMR Version (Map Version) `SMR : 도로 정보` |
| smdc\_ver | String |  | SMDC Version `SMDC : 배경 dp (타일 별 정보, 새로운 도역 정보)` |
| 제목 없음 |  |  |  |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |
| map\_info | Object | MAP 버전 정보 |
| ┣ map\_status | String | 업데이트 여부"T" : 업데이트 필요"F" : 업데이트 불필요 |
| ┣ smr\_ver | String | 최신 SMR Version(Map Version) |
| ┣ smr\_url | String | SMR 데이터 URL |
| ┣ smdc\_ver | String | SMDC Version |
| ┣ smdc\_url | String | SMDC 데이터 URL |
| ┣ init\_dataSet | String | 초기 데이터 XML |
| ┣ init\_serverUrl | String | 초기 데이터 URL |
| ┣ full\_dataSet | String | 전체 데이터 XML |
| ┗ full\_serverUrl | String | 전체 데이터 URL |
| gp\_info | Object | 안전운행 데이터 정보 |
| ┣ gp\_ver | String | 최신 안전운행 데이터 버전 |
| ┣ gp\_url | String | 안전운행 데이터 URL |
| ┣ gp\_extractPath | String | 안전운행 데이터 압축해제 경로 |
| ┗ gp\_fileSize | String | 안전운행 데이터 파일 크기 |
| aero\_info | Object | 항공 지도 정보 |
| ┣ aero\_url | String | 항공 지도 URL |
| ┣ data\_set | String | 항공 지도 data set |
| ┗ server\_url | String | 항공 지도 server URL |

## 서비스 메인(AIR)
> Confluence page id: 2262305710 · 최종 수정: 10월 01, 2026

### Function

> 서비스 메인 Request Header 중 인증키 값 없이 호출하며, 이후 다른 I/F 호출시 결과로 받은 인증키값 사용

### URL

> `/serviceGate`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| reg\_id | String | O | push id (Android) or device token (iOS) |
| app\_ver | String | O | App Version |
| smr\_ver | String | O | SMR Version (Map Version) |
| smdc\_ver | String | O | SMDC Version |
| gp\_ver | String | O | 안전운행 Version |
| clause\_ver | String | O | 약관 Version |
| channel | String |  | 유입 경로NOR : 정상실행 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |
| auth\_key | String | 인증키 |
| loginInfo | String | 로그인여부T: 로그인상태F: 로그인아님 |
| appver\_info | Object | APP 버전 정보 |
| ┣ idx | Integer | App 버전 인덱스 |
| ┣ appver | String | App 버전 |
| ┣ subject | String | 패치 제목 |
| ┣ url | String | 모바일 웹뷰 URL |
| ┣ compulsion\_patch\_yn | String | 패치 종류 및 팝업 유무Y: 강제 패치N: 선택 패치 팝업 있음X: 선택 패치 팝업 없음 |
| ┣ chk\_option\_yn | String | 선택 패치 시 체크옵션 노출 여부Y: 노출N: 미노출(APP에서 사용안함) |
| ┣ chk\_option\_type | String | 선택 패치 시 체크 옵션 영역01: 하루동안 보지 않기02: 일주일간 보지 않기03: 팝업 다시 보지 않기(APP에서 사용안함) |
| ┗ option\_type | String | 선택 패치 시 옵션 영역01: 나중에하기02: 하루동안 다시 보지 않기03: 일주일간 다시 보지 않기04: 팝업 다시 보지 않기 |
| app\_url | String | 안드로이드일경우 GooglePlay APP 다운로드 URL아이폰일경우 기존과 동일 |
| app\_url\_onestore | String | One store APP 다운로드 URL |
| ctt\_speed\_url | String | CTT 속도 정보 URL(speedsimple.dat) |
| ctt\_idx\_url | String | CTT 인덱스 URL(speedidx.dat) |
| dp\_event\_url | String | DP 이벤트 데이터 URL |
| notice\_LastIdx | Integer | idx number |
| notice\_size | Integer | 공지 개수 |
| notice\_list | Array | 공지 리스트 |
| ┣ idx | Integer | 공지 인덱스 |
| ┣ subject | String | 공지 제목 |
| ┗ board\_type | String | 공지 타입A1: 공지사항A2: 긴급공지A3: 업데이트A4: 이벤트A5: 이벤트 당첨자A6: 이용팁A7: FAQ |
| noticeList\_url | String | 공지사항 리스트 URL호출시 privateKey(개인키 값) 추가 |
| noticeDetail1\_url | String | 공지사항 상세 URL공지 인덱스 번호 URL뒤에 붙여서 호출호출시 privateKey(개인키 값) 추가 |
| noticeDetail2\_url | String | 긴급공지 상세 URL공지 인덱스 번호 URL뒤에 붙여서 호출호출시 privateKey(개인키 값) 추가 |
| noticeDetail3\_url | String | 업데이트 상세 URL공지 인덱스 번호 URL뒤에 붙여서 호출호출시 privateKey(개인키 값) 추가 |
| noticeDetail4\_url | String | 이벤트 상세 URL공지 인덱스 번호 URL뒤에 붙여서 호출호출시 privateKey(개인키 값) 추가 |
| noticeDetail5\_url | String | 이벤트 당첨자 상세 URL공지 인덱스 번호 URL뒤에 붙여서 호출호출시 privateKey(개인키 값) 추가 |
| banner\_list | Array | 배너 리스트 |
| ┣ idx | Integer | 배너 인덱스 |
| ┣ title | String | 배너 제목 |
| ┣ img\_link1 | String | 배너 이미지 Url |
| ┣ link\_url | String | 링크 Url |
| ┣ param\_yn | String | 파라미터 사용여부Y:사용N:미사용 |
| ┣ img\_dis\_yn | String | 이미지URL 사용여부Y:사용N:미사용 |
| ┗ board\_type | String | 배너 타입A1: 공지사항A2: 긴급공지A3: 업데이트A4: 이벤트 공지A5: 이벤트 당첨자A6: 이용팁A9: 이벤트 |
| banner\_end\_list | Array | 배너 리스트 |
| ┣ idx | Integer | 배너 인덱스 |
| ┣ title | String | 배너 제목 |
| ┣ img\_link1 | String | 배너 이미지 Url |
| ┣ link\_url | String | 링크 Url |
| ┣ param\_yn | String | 파라미터 사용여부Y:사용N:미사용 |
| ┣ param\_yn2 | String | 특수조건2 사용 여부Y:사용N:미사용기본값 N, Y일시 external\_link 컬럼 참조 |
| ┣ external\_link | String | externallink 의 site 명칭 |
| ┣ img\_dis\_yn | String | 이미지URL 사용여부Y:사용N:미사용 |
| ┗ board\_type | String | 배너 타입A1: 공지사항A2: 긴급공지A3: 업데이트A4: 이벤트 공지A5: 이벤트 당첨자A6: 이용팁A9: 이벤트 |
| tipList\_url | String | 이용팁 리스트 URL호출시 privateKey(개인키 값) 추가 |
| faq\_url | String | FAQ 리스트 URL호출시 privateKey(개인키 값) 추가 |
| faq2\_url | String | 신규 faq관련 url |
| faq\_new\_url | String | 신규 노션 faq url |
| voc\_main\_url | String | 문의하기 등록 URL호출시 privateKey(개인키 값) 추가 |
| voc\_search\_url | String | 문의하기 검색 실패 URL호출시 privateKey(개인키 값), searchtext(검색어) 추가 |
| smsshare\_url | String | SMS 위치공유 URL호출시 I-Code값 추가 ex)?i=319-494-2013POI ID가 있는 경우 같이 추가 ex)?i=319-494-2013&p=4843221 |
| trafficSummary\_url | String | 교통요약맵 URL[[inavi-air-api-search#교통정보 요약맵 검색\|교통정보 요약맵 검색]] 결과 파라미터 호출시 추가ex)?roadId=00004&bottomLeftX=150139&bottomLeftY=525548&topRightX=151552&topRightY=535460 |
| memberLoginUrl | String | 통합회원 로그인 페이지 URL |
| popup\_size | Integer | 팝업공지 개수 |
| popup\_list | Array | 팝업공지 리스트 |
| ┣ idx | Integer | 팝업공지 인덱스 |
| ┣ subject | String | 팝업공지 제목 |
| ┣ url | String | 팝업공지 내용 URL |
| ┣ call\_url | String | 이동할 URL |
| ┣ noti\_type | String | 타입03: 긴급공지용04: 일반공지 4타입05: 일반공지 5타입06: 일반공지 6타입07: 일반공지 이벤트타입 |
| ┣ popup\_type | String | 팝업공지 타입01: 긴급공지02: 일반공지 |
| ┣ chk\_option\_yn | String | 체크옵션 노출여부(Y:노출, N: 미노출) |
| ┣ chk\_option\_type | String | 체크 옵션 영역01: 하루동안 보지 않기02: 일주일간 보지 않기03: 팝업 다시 보지 않기(APP에서 사용안함) |
| ┗ option\_type | String | 옵션 영역00: 취소01: 나중에하기02: 하루동안 다시 보지 않기03: 일주일간 다시 보지 않기04: 팝업 다시 보지 않기 |
| bb\_flag | String | 블랙박스 사용가능 여부0 : 불가1 : 가능 |
| aa\_flag | String | 단말지원 여부0 : 불가1 : 가능 |
| ai\_flag | String | AI지원 여부0 : 불가1 : 가능 |
| dp\_flag | String | Dptype0 : 저사양1 : 고사양 (default) |
| aero | String | 항공지도 지원 여부0\~4 (0: 미지원, 1\~4: 지원 1\~4GB 캐시용량) |
| cartoon | Integer | 0\~2 (0 : 미지원 1 : 활성화 2 : 비활성화) |
| nature | Integer | 0\~2 (0 : 미지원 1 : 활성화 2 : 비활성화) |
| verify\_flag | String | 검증 여부0 : 검증완료1 : 미검증2 : 사용불가 |
| verify\_msg | String | 검증 메세지 |
| thirdApp\_size | Integer | 3rd party App 리스트 개수 |
| thirdApp\_list | Array | 3rd party App 리스트 |
| ┣ idx | Integer | App 인덱스 |
| ┣ title | String | App 명칭 |
| ┣ icon\_url | String | Icon URL |
| ┗ app\_url\_schema | String | App schema URL |
| event\_flag | String | 이벤트 여부Y: 있음N: 없음 |
| event\_info | Object | 이벤트 정보 |
| ┣ idx | String | 이벤트 번호 |
| ┣ title | String | 이벤트 문구 |
| ┣ link\_url | String | 이벤트 URL |
| ┣ event\_before | String | 단위 : 응모전 |
| ┣ event\_in | String | 단위 : 응모중 |
| ┣ event\_complete | String | 단위 응모완료 |
| ┗ param\_yn | String | 파라미터 사용여부Y:사용N:미사용 |
| sunrise | String | 일출 시간(HH:mm:ss) |
| sunset | String | 일몰 시간(HH:mm:ss) |
| total\_ver | String | 이용약관 통합 버전 |
| mmc\_type | String | MMC mode1: log stop2: info log3: debug log |
| otherData\_ver | String | 대교 데이터 통합 버전 |
| mileage\_rate | String | 마일리지 비율 |
| searchHint | String | 검색어 힌트 |
| seamless\_inside | Array | 심리스 실내 지도 정보 |
| ┣ name | String | 위치 이름 |
| ┣ zone\_id | String | 심리스 PID |
| ┣ x | String | X좌표 |
| ┗ y | String | Y좌표 |
| mig\_url | String | KT 종료 마이그레이션 파일 정보 요청 URL(null or "" 시 요청 하지 않아야 함) |
| disabledFBAnalytics | String | Firebase 로그 전체 사용 안함 Flag1: 사용안함그외: 사용함 |
| disabledFBAnalyticsAgent | String | Firebase 통신로그 사용 안함 Flag1: 사용안함그외: 사용함 |
| isLuckyIng | Boolean | 행운상자 이벤트 진행중 여부 |
| showLuckyBox | Boolean | 럭키박스 표출여부 |
| wasLogin | Boolean | 로그인 한번이라도 했었는지 여부 |
| ad\_unit\_list | Array | 광고 Unit Array |
| ┣ unit | String | 광고 Unit **ex) AD\_MAINCARD** |
| ┣ main\_id | String | main ad Id **ex) /434753748/inavi/inavi\_home\_01** |
| ┗ house\_id | String | house ad Id **ex) /434753748/inavi\_housead/adx\_home\_01** |
| push\_status | String | PUSH 수신 동의 여부 0 : 미동의 1 : 동의 |
| cash\_push\_status | String | 에어 캐시 PUSH 수신 동의 여부 0 : 미동의 1 : 동의 |
| traffic\_light\_ver\_dae\_gu | String | 대구 신호등 전체 리스트 버전 정보 EX) ver0.1 |
| on\_air\_mode | Boolean | 온에어 모드 ON/OFF 적용 여부 true : 온에어 모드 적용 false : 온에어 모드 미적용 |
| sdkType | String | sdkType Default : Empty String 삼성중공업 : SAMSUNG\_SHI |
| inaviAuthKey | String | 아이나비 인증 키 (지도 사용) |
| hud\_open\_type |  | HUD 기능 ON/OFF 적용 여부 true : HUD 기능 적용 (Default) false : HUD 기능 미적용 |
| skp\_ad\_status | Boolean | SKP  광고 활성화 여부 true : 광고 활성화 false : 광고 비활성화 |
| gen\_ai\_flag | Boolean | 생성형 AI 활성화 여부 true: 활성화(default) false: 비활성화 |
| gen\_ai\_max\_token | Integer | 생성형 AI 최대글자수 (default : 500) |
| cp\_hud\_flag | Boolean | CP HUD 활성화 여부 true: 활성화(default) false: 비활성화 |
| gpt\_model | Integer | chatGPT 4o-mini / 4o 모델 0 : 4o-mini (default) 1 : 4o |
| first\_login\_cash | Integer | 최초 로그인 적립 캐시 (default : 500) |
| report\_notice\_url | String | 제보하기 페이지 내 특정 공지사항 URL |
| orda\_flag | Boolean | 오르다 스탬프 활성화 여부 true: 활성화 false: 비활성화 |
| airbotAuthKey | String | AIRBOT 인증 키 |

## Sources

- Confluence "INAVI AIR API" > AIR 서비스 (2026-10-27 조회): AIR 서비스 (2262305686), 이용 약관 조회(AIR) (2262305752), 이용 약관 동의 및 개인 키 생성(AIR) (2262305732), 지도 다운로드 정보 조회(AIR) (2262305772), 서비스 메인(AIR) (2262305710)
