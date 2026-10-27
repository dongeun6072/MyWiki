---
title: "INAVI AIR API — 기타"
category: references
tags: [inavi-air, api, sns-login, driving-history, visibility/internal]
aliases: [AIR API 기타]
relationships:
  - target: "[[inavi-air-api-detail-spec]]"
    type: derived_from
sources: ["url:https://inavisystems.atlassian.net/wiki/spaces/AS/pages/2262306807"]
summary: >-
    INAVI AIR API "기타" 카테고리 31개 API(외부 계정 연동, 확대도·방면 음성, 주행 이력, 최근 목적지, 환경 설정 저장, SOS 등)의 요청·응답 명세를 Confluence 원문 그대로 옮긴 페이지.
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

# INAVI AIR API — 기타

Confluence "INAVI AIR API" > "기타" 카테고리 페이지들을 원문 그대로 옮긴 것이다. 허브는 [[inavi-air-api-detail-spec]], 공통 헤더·결과 코드는 [[inavi-air-api-common]], 서비스 개요는 [[inavi-air]]를 본다.

| API | URL |
| --- | --- |
| [[#AIR SOS]] | `/roadAcdntNotiSos` |
| [[#KT 종료 마이그레이션 정보 조회]] | `/snsInfoMigrationData` |
| [[#CCTV 상세 조회]] | `/cctvInfo` |
| [[#KT 종료 마이그레이션 파일 정보 조회]] | `/snsInfoMigrationFile` |
| [[#대교 리스트 조회]] | `/bridgeList` |
| [[#고속도로 휴게소 주유소 정보 조회]] | `/searchOilStation` |
| [[#마일리지 이력 등록]] | `/mileageHisInsert` |
| [[#방면 음성 정보 조회]] | `/directionVoice` |
| [[#신규 DP 확대도 정보 조회]] | `/extendedNewMap` |
| [[#외부 계정 연동 로그아웃]] | `/snsLogout` |
| [[#외부 계정 연동 가입여부 확인]] | `/snsCheck` |
| [[#외부 계정 연동 로그인]] | `/snsLogin` |
| [[#외부 계정 연동 정보입력]] | `/snsMemberInfoInsert` |
| [[#외부 계정 연동 통합회원 전환 로그인]] | `/snsTransLogin` |
| [[#외부 계정 연동 회원탈퇴]] | `/signout` |
| [[#유고, VVMS, 수해 정보 상세 조회]] | `/roadEventDetail` |
| [[#제보하기 간소화]] | `/simpleReport` |
| [[#재난, 긴급출동차량 위치 상세조회]] | `/emergencyDetail` |
| [[#주행 이력 그룹 리스트 조회 FivePin - AIR]] | `/drivingHisGroupListUM` |
| [[#주행 이력 그룹 리스트 조회]] | `/drivingHisGroupList` |
| [[#주행 이력 삭제]] | `/drivingHisDelete` |
| [[#주행 이력 일 상세 리스트 조회]] | `/drivingHisDayListDetail` |
| [[#주행 이력 일 상세 리스트 조회 FivePin - AIR]] | `/drivingHisDayListDetailUM` |
| [[#주행 이력 일별 리스트 조회]] | `/drivingHisDayList` |
| [[#최근 목적지 리스트 등록]] | `/latelyPoiListInsert` |
| [[#주행 이력별 상제 좌표 조회 FivePin - AIR]] | `/drivingHisCoordUM` |
| [[#최근 목적지 리스트 조회]] | `/latelyPoiListSelect` |
| [[#혼잡 차선 조회]] | `/confusionLane` |
| [[#확대도 정보 조회]] | `/extendedMap` |
| [[#환경 설정 저장]] | `/saveConfig` |
| [[#회원탈퇴]] | `/integratedSignout` |

## 기타
> Confluence page id: 2262306807 · 최종 수정: 10월 06, 2026

카테고리 상위 페이지. 본문은 하위 페이지 링크 목록이다(원본 순서).

- 🧭외부 계정 연동 로그인
- 🧭외부 계정 연동 가입여부 확인
- 🧭외부 계정 연동 통합회원 전환 로그인
- 🧭외부 계정 연동 로그아웃
- 🧭외부 계정 연동 정보입력
- 🧭외부 계정 연동 회원탈퇴
- 🧭확대도 정보 조회
- 🧭신규 DP 확대도 정보 조회
- 🧭방면 음성 정보 조회
- 🧭고속도로 휴게소 주유소 정보 조회
- 🧭환경 설정 저장
- 🧭대교 리스트 조회
- 🧭최근 목적지 리스트 조회
- 🧭최근 목적지 리스트 등록
- 🧭유고, VVMS, 수해 정보 상세 조회
- 🧭CCTV 상세 조회
- 🧭재난, 긴급출동차량 위치 상세조회
- 🧭주행 이력 그룹 리스트 조회
- 🧭주행 이력 일별 리스트 조회
- 🧭주행 이력 일 상세 리스트 조회
- 🧭주행 이력 그룹 리스트 조회 FivePin - AIR
- 🧭주행 이력 일 상세 리스트 조회 FivePin - AIR
- 🧭주행 이력별 상제 좌표 조회 FivePin - AIR
- 🧭주행 이력 삭제
- 🧭마일리지 이력 등록
- 🧭혼잡 차선 조회
- 🧭KT 종료 마이그레이션 파일 정보 조회
- 🧭KT 종료 마이그레이션 정보 조회
- 🧭제보하기 간소화
- 🧭AIR SOS
- 🧭회원탈퇴

## AIR SOS
> Confluence page id: 2262306885 · 최종 수정: 10월 01, 2026

### Function

> SOS 정보를 도로관리기관에 전달

### URL

> `/roadAcdntNotiSos`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| sosInfo | Array |  | SOS 정보 |
| ┣ evntType | String | O | 이벤트 type<br>01 : SOS<br>02 : 급감속 |
| ┣ evntLoctX | String | O | 정규화좌표 X값(8자리) |
| ┣ evntLoctY | String | O | 정규화좌표 Y값(8자리) |
| ┣ vhclAngl | String | O | 차량 정북기준 각도(0\~359) |
| ┣ roadNm | String | O | 도로 이름 |
| ┣ mrVer | String | O | 요청 MR Version |
| ┣ mrlink | Object | O | 요청 MRLink 정보 리스트 |
| ┣ mapid | Integer | O | 도로 MapID |
| ┣ linkid | Integer | O | 도로 LinkID |
| ┗ direction | Integer | O | 도로 Direction |
| ┗ naviCd | String | O | 내비사 코드<br>02 : 아이나비(Defalut) |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |

## KT 종료 마이그레이션 정보 조회
> Confluence page id: 2262306905 · 최종 수정: 10월 01, 2026

### Function

> KT 종료 마이그레이션 파일 정보 조회

### URL

> `/snsInfoMigrationData`

[[inavi-air-api-common#Request Header|Request Header]]

### Request Parameter

> 원본 표가 비어 있음

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |
| sns\_key | String | sns\_key |
| data | String | 마이그레이션 Data |

## CCTV 상세 조회
> Confluence page id: 2262306925 · 최종 수정: 10월 01, 2026

### Function

> CCTV 아이디를 이용하여 상세 정보를 조회

### URL

> `/cctvInfo`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| cctvList | Array\<String\> | O | CCTV ID 리스트 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |
| cctv\_cnt | Integer | CCTV 개수 |
| cctv\_list | Array | CCTV 정보 리스트 |
| ┣ cctv\_id | String | CCTV ID |
| ┣ cctv\_name | String | CCTV 명칭 |
| ┣ nosun | String | 도로명 |
| ┣ offer | String | CCTV 데이터 제공처 |
| ┣ thumbnail\_url | String | 썸네일 이미지 URL |
| ┣ stream\_url | String | CCTV Stream URL |
| ┗ time | String | 업데이트 시간 (YYYYMMDDHHMISS) |

## KT 종료 마이그레이션 파일 정보 조회
> Confluence page id: 2262306945 · 최종 수정: 10월 01, 2026

### Function

> KT 종료 마이그레이션 파일 정보 조회

### URL

> `/snsInfoMigrationFile`

[[inavi-air-api-common#Request Header|Request Header]]

### Request Parameter

> 원본 표가 비어 있음

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |
| file\_name | String | 파일 이름 |
| file\_value | String | 파일 내용 |

## 대교 리스트 조회
> Confluence page id: 2262306965 · 최종 수정: 10월 01, 2026

### Function

> 대교 리스트 조회

### URL

> `/bridgeList`

[[inavi-air-api-common#Request Header|Request Header]]

### Request Parameter

> 원본 표가 비어 있음

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |
| bridge\_list | Array | 대교 리스트 |
| ┣ name | String | 대교 이름 |
| ┣ up\_x | String | 상행 X좌표(정규화) |
| ┣ up\_y | String | 상행 Y좌표(정규화) |
| ┣ down\_x | String | 하행 X좌표(정규화) |
| ┗ down\_y | String | 하행 Y좌표(정규화) |

## 고속도로 휴게소 주유소 정보 조회
> Confluence page id: 2262306985 · 최종 수정: 10월 01, 2026

### Function

> 고속도로 휴게소 주유소 정보 조회

### URL

> `/searchOilStation`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| serviceid | String | O | 서비스 ID<br>1063 : 휴게소 주유소 검색 |
| count | String | O | salist 개수 |
| salist | Array | O | 휴게소 명칭 리스트 |
| ┗ saname | String | O | 휴게소 명칭 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| total\_num | Integer | 전체 검색 결과 개수 |
| search\_num | Integer | 검색 결과 개수 |
| oslist | Array | 휴게소 쥬우소 목록 |
| ┣ id | Integer | OPWID |
| ┣ pole | Integer | POLE |
| ┣ x | Integer | 정규화 X좌표 |
| ┣ y | Integer | 정규화 Y좌표 |
| ┣ update\_date | Integer | 변경날짜 YYYYMMDD |
| ┣ update\_time | Integer | 변경시간 HHMMSS |
| ┣ hg\_price | Integer | 고급 휘발유 |
| ┣ g\_price | Integer | 휘발유 |
| ┣ k\_price | Integer | 경유 |
| ┣ d\_price | Integer | 등유 |
| ┣ l\_price | Integer | LPG |
| ┣ saname | String | 휴게소 명칭 |
| ┗ name | String | OPW 이름 |
| evlist | Array | 휴게소 전기차 충전소 목록 |
| ┗ saname | String | 휴게소 명칭 |

## 마일리지 이력 등록
> Confluence page id: 2262307007 · 최종 수정: 10월 01, 2026

### Function

> 마일리지 이력 등록(LogApi 전용)

### URL

> `/mileageHisInsert`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| start\_addr | String |  | 출발 주소 |
| end\_addr | String |  | 도착 주소 |
| start\_x | String |  | 출발 좌표x (정규화) |
| start\_y | String |  | 출발 좌표x (정규화) |
| end\_x | String |  | 도착 좌표x (정규화) |
| end\_y | String |  | 도착 좌표x (정규화) |
| start\_dt | String |  | 출발 시간(초단위Timestamp) |
| end\_dt | String |  | 도착 시간(초단위Timestamp) |
| distance | Long |  | 주행 거리(단위 m) |
| point | Long | O | 마일리지 |
| type | String | O | D : 주행 이력 마일리지<br>E : 기타 마일리지 |
| title | String | O | 제목(예 : 가입 기념 마일리지) |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |

## 방면 음성 정보 조회
> Confluence page id: 2262307027 · 최종 수정: 10월 01, 2026

### Function

> 방면 음성 정보 조회<br>방면음성 정보 ID(vid)는 한글을 포함하므로 Encoding(utf-8)하여 전송한다.<br>결과의 data\_url 사용 시에도 마지막 vid 부분은 Encoding(utf-8)하여 전송한다.

### URL

> `/directionVoice`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| vid | String | O | 방면 음성 ID |
| type | String |  | 음성 타입<br>1 : 부드러운 음성<br>2 : 발랄한 음성<br>3 : 신규 부드러운 음성<br>4: 신규 발랄한 음성 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |
| vid | String | 조회한 방면 음성 ID |
| data\_url | String | 음성 파일 Data URL |
| playtime | String | 음성 실행 시간 |

## 신규 DP 확대도 정보 조회
> Confluence page id: 2262307047 · 최종 수정: 10월 01, 2026

### Function

> 신규 DP 확대도 정보 조회<br>확대도 ID(extid)는 한글을 포함하므로 Encoding(utf-8)을 하여 전송한다.<br>결과의 data\_url 사용 시에도 마지막 extid 부분은 Encoding(utf-8)하여 전송한다.

### URL

> `/extendedNewMap`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| extid | String | O | 확대도 ID |
| type | String |  | 확대도 tyep<br>ieg : 기존 이미지<br>mp4 : 영상 이미지 |

#### Response Paramete

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |
| data\_url\_new | String | 신규 DP엔진 확대도 Data URL |
| extid | String | 조회한 3D확대도 ID |
| type | String | 요청한 확대도 tyep<br>ieg : 기존 이미지<br>mp4 : 영상 이미지 |

\`

## 외부 계정 연동 로그아웃
> Confluence page id: 2262307067 · 최종 수정: 10월 01, 2026

### Function

> SNS 로그아웃

### URL

> `/snsLogout`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| buttonFlag | boolean | O | 팝업버튼 플래그값<br>YES : true<br>NO : false |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |

## 외부 계정 연동 가입여부 확인
> Confluence page id: 2262307087 · 최종 수정: 10월 01, 2026

### Function

> 외부 계정 연동 가입여부 확인

### URL

> `/snsCheck`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| snsId | String | O | 통합로그인시 memberCd(현재는 통합회원만 지원) |
| snsType | String | O | SNS 타입<br>f : 페이스북<br>g : 구글<br>k : 카카오<br>n : 네이버<br>a L 애플<br>u : 통합로그인 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |

## 외부 계정 연동 로그인
> Confluence page id: 2262307107 · 최종 수정: 10월 01, 2026

### Function

> SNS 로그인

### URL

> `/snsLogin`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| token | String | O | SNS 토큰<br>통합로그인시 memberCd |
| snsType | String | O | SNS 타입<br>f : 페이스북<br>g : 구글<br>k : 카카오<br>k2 : 카카오(APIv2)<br>n : 네이버<br>a : 애플<br>u : 통합로그인 |
| appleAuthCode | String |  | 애플인 경우 로그인 시 생성 되는 authorization\_code |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| snsType | String | snsType |
| snsKey | String | snsKey값 |
| snsRegPopUpFlag | boolean | 즐겨찾기 동기화 팝업 노출여부<br>true : 팝업노출<br>false : 팝업미노출<br>위값들은 snsPrivateKey값의 ts가지고 판단하였음 |
| birthday | String | 생년월일 (입력해두지 않았을경우 null반환) |
| gender | String | 성별 (입력해두지 않았을경우 null반환) |
| hipass | String | 하이패스 옵션<br>0: OFF<br>1: ON |
| discount | String | 국가유공자 및 장애인 할인<br>0: OFF<br>1: ON |
| car\_type | String | 차종<br>0: 경차(1종 통행료 할인 적용)<br>1: 1종(소형차)<br>2: 2종(중형차)<br>3: 3종(대형차)<br>4: 4종(대형화물차)<br>5: 5종(특수화물차)<br>6: 이륜차 |
| car\_mark | String | 자차마크<br>0: 기본<br>1: 흰색세단<br>2: 빨간스포츠카<br>3: 하늘색SUV<br>4: 노란스포츠카<br>5: 경찰차<br>6: 소방차<br>7: 파란색트럭<br>8 : 봉고차<br>9: 초록 해치백<br>10 : 파란버스<br>11 : 파란오토바이<br>12 : 빨간오토바이 |
| oil\_type | String | 유종<br>0: 휘발유<br>1: 고급휘발유<br>2: 경유<br>3: LPG<br>4: 전기차 충전소 |
| oil\_station | String | 선호주유소 (중복 설정시 "\_"구분자로 전송 \*전체선택시 -\> 0, 이경우 이외 다른값 전달 금지)<br>0: 전체<br>1: SK<br>2: S-OIL<br>3: 현대 OilBank<br>4: GS<br>5: E-1<br>선호 충전기(중복 설정시 "\_"구분자로 전송)<br>0: DC차데모<br>1:AC급속3상<br>2:DC콤보<br>3:AC완속 |
| total\_distance | Long | 총 주행 거리 |
| total\_point | Long | 총 적립 포인트 |
| gender | String | 성별<br>M: 남자<br>F : 여자 |
| birthday | String | 생년월일<br>EX([생년월일 예시 제거]) -\> YYYY.MM.DD |
| carNum | String | 차량번호<br>EX([차량번호 예시 제거]) |
| birthTime | String | 태어난시간(ex : 1930)<br>모름 : DNK |
| sL | String | 음력 양력<br>양력 : S<br>음력 : L<br>음력윤달 : LI |
| tutoComplete | boolean | 튜토리얼 완료여부 |
| driveLineColor | String | 주행선 색상 (환경설정 -\> 지도설정 -\> 주행선 색상)<br>0 : traffic<br>1 : red<br>2 : orange<br>3 : yellow<br>4 : green<br>5 : blue (Default)<br>6 : indigo |
| onAirBenefits | String | 맞춤형 온에어 혜택 (Default ON)<br>0 : OFF<br>1 : ON |
| defaultRouteOption | String | 추천  경로 옵션 설정 (0 \~ 5)<br>0 : 에어추천 (Default)<br>1 : 가장 빠름 <br>2: 무료도로 <br>3: 큰길 위주<br>4: 고속도로 위주<br>5 : 최단 거리 |
| issueReport | String | 제보하기 개선 (Default OFF)<br>0 : OFF<br>1 : ON |
| onlyCamera | String | Only 카메라 모드 (Default OFF)<br>0 : OFF<br>1 : ON |
| realTimeTraffic | String | 실시간 교통 신호 안내 (Default ON)<br>0 : OFF<br>1 : ON |
| mainRecentPlaces | String | 메인화면 최근장소 더보기 (Default OFF)<br>0 : OFF<br>1 : ON |
| mbSpdEnfrc | String | 이동식 과속 단속 (Default : ON)<br>0 : OFF<br>1: ON |
| bxtSpEnfrc | String | 박스형 과속 단속 (Default : ON)<br>0 : OFF<br>1: ON |
| crckdIntrv | String | 끼어들기 단속 (Default : OFF)<br>0 : OFF<br>1: ON |
| ovrldCntrl | String | 과적 단속 (Default : OFF)<br>0 : OFF<br>1: ON |
| trfclCmr | String | 교통정보 수집 카메라(Default : ON)<br>0 : OFF<br>1: ON |
| sharpCurve | String | 급커브 구간 (Default : ON)<br>0 : OFF<br>1: ON |
| acdntBndln | String | 사고다발 구간 (Default : ON)<br>0 : OFF<br>1: ON |
| speedBump | String | 과속 방지턱 (Default : ON)<br>0 : OFF<br>1: ON |
| chlEldRsr | String | 어린이/노인 보호구역 (Default : ON)<br>0 : OFF<br>1: ON |
| wldlfSnctr | String | 야생동물 보호구역 (Default : ON)<br>0 : OFF<br>1: ON |
| rlrdCrsng | String | 철도 건널목 (Default : ON)<br>0 : OFF<br>1: ON |
| fallStSect | String | 낙석 구간 (Default : OFF)<br>0 : OFF<br>1: ON |
| entrnGrtrr | String | 녹색교통지역 진입 (Default : ON)<br>0 : OFF<br>1: ON |

## 외부 계정 연동 정보입력
> Confluence page id: 2262307127 · 최종 수정: 10월 01, 2026

### Function

> SNS 정보입력

### URL

> `/snsMemberInfoInsert`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| gender | String |  | 성별<br>M: 남자<br>F : 여자 |
| birthday | String |  | 생년월일<br>EX([생년월일 예시 제거]) -\> YYYY.MM.DD |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |

## 외부 계정 연동 통합회원 전환 로그인
> Confluence page id: 2262307147 · 최종 수정: 10월 01, 2026

### Function

> SNS 연동 통합회원 전환 로그인

### URL

> `/snsTransLogin`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| memberCd | String | O | 아이나비 memberCd |

#### Response Paramete

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| snsType | String | snsType |
| snsKey | String | snsKey값 |

## 외부 계정 연동 회원탈퇴
> Confluence page id: 2262307167 · 최종 수정: 10월 01, 2026

### Function

> SNS 회원탈퇴

### URL

> `/signout`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| buttonFlag | boolean | O | 팝업버튼 플래그값<br>YES : true<br>NO : false |
| snsType | String | O | SNS 타입<br>f : 페이스북<br>g : 구글<br>k : 카카오<br>n : 네이버<br>u: 통합회원 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |

## 유고, VVMS, 수해 정보 상세 조회
> Confluence page id: 2262307187 · 최종 수정: 10월 01, 2026

### Function

> 유고, VVMS 아이디를 이용하여 상세 정보를 조회

### URL

> `/roadEventDetail`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| id | String | O | 유고 or VVMS or 수해 ID |
| eventType | Integer | O | 0: VVMS, 1: 유고, 2: 수해 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |
| id | String | 유고 or VVMS or 수해 ID |
| comment | String | 상세 유고 or VVMS or 수해 정보 |

## 제보하기 간소화
> Confluence page id: 2262307207 · 최종 수정: 10월 01, 2026

### Function

> 에어3 주행 중 원터치로 제보하기

### URL

> `/simpleReport`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| category | String | O | 제보하기 카테고리<br>CAM : 카메라 정보 틀림<br>ROU : 경로 오류<br>DES : 목적지 위치 오류 |
| ┣ nowLoc | Object | O | 현재 위치 정보 |
| ┣ x | String | O | 현재 좌표 X (6자리 정규화 좌표) |
| ┣ y | String | O | 현재 좌표 Y (6자리 정규화 좌표) |
| ┣ startLoc | Object |  | 출발지 정보(category가 ROU 일때 필수) |
| ┣ x | String |  | 출발지 좌표 X (6자리 정규화 좌표) |
| ┣ y | String |  | 출발지 좌표 Y (6자리 정규화 좌표) |
| ┗ name | String |  | 출발지명 |
| ┣ desLoc | Object |  | 목적지 정보(category가 ROU, DES 일때 필수) |
| ┣ x | String |  | 목적지 좌표 X (6자리 정규화 좌표) |
| ┣ y | String |  | 목적지 좌표 Y (6자리 정규화 좌표) |
| ┗ name | String |  | 목적지명 |
| searchOption | String |  | Agent 탐색 종류(category가 ROU 일때 사용)<br>agt\_recommend : 추천경로 (LGU+ 향으로는 “빠른길”)<br>agt\_short\_time : 최소시간<br>real\_traffic\_freeroad : 무료도로<br>short\_distance\_priority : 최단거리<br>highway\_priority : 고속도로우선<br>motorcycle : 이륜차 이용도로<br>beginner : 초보자(편한길) (LGU+ 향으로는 “편한길”)<br>recommendation : 엔진기반 추천경로(agt\_recommend 대체)<br>time\_priority : 엔진기반 최소시간(agt\_short\_time 대체) |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |

## 재난, 긴급출동차량 위치 상세조회
> Confluence page id: 2262307227 · 최종 수정: 10월 01, 2026

### Function

> 재난, 긴급출동차량 위치 상세 정보를 조회

### URL

> `/emergencyDetail`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| id | String | O | 재난 혹인 긴급출동차량 위치 정보 아이디 |
| type | Integer | O | 2 : 재난정보, 3 : 긴급출동차량 위치 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |
| emergency\_text | String | 상세정보 (현재는 고정문구로 서비스) |

## 주행 이력 그룹 리스트 조회 FivePin - AIR
> Confluence page id: 2262307247 · 최종 수정: 10월 01, 2026

### Function

> 주행 이력 그룹 리스트 조회 -FIVE PIN

### URL

> `/drivingHisGroupListUM`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| memCode | String | O | 통합회원 멤버코드 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |
| total\_distance | Long | 총 주행 거리 |
| days | List | 현재 달 주행 이력 일별 리스트 |
| ┣ date | String | 년.월.일(초단위Timestamp) |
| ┗ distance | Long | 주행 거리(단위 m) |
| months | List | 현재 달을 제외한 주행 이력 월별 리스트 |
| ┣ date | String | 년.월(초단위Timestamp) |
| ┗ distance | Long | 주행 거리(단위 m) |

## 주행 이력 그룹 리스트 조회
> Confluence page id: 2262307267 · 최종 수정: 10월 01, 2026

### Function

> 주행 이력 그룹 리스트 조회

### URL

> `/drivingHisGroupList`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| type | String |  | 1: 총 마일리지, 총 주행거리만 표출<br>0: 리스트 포함 전체 표출<br>기본값: 0 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |
| total\_distance | Long | 총 주행 거리 |
| total\_point | Long | 총 적립 포인트 |
| days | List | 현재 달 주행 이력 일별 리스트 |
| ┣ date | String | 년.월.일(초단위Timestamp) |
| ┣ distance | Long | 주행 거리(단위 m) |
| ┗ point | Long | 마일리지 |
| months | List | 현재 달을 제외한 주행 이력 월별 리스트 |
| ┣ date | String | 년.월(초단위Timestamp) |
| ┣ distance | Long | 주행 거리(단위 m) |
| ┗ point | Long | 마일리지 |

## 주행 이력 삭제
> Confluence page id: 2262307287 · 최종 수정: 10월 01, 2026

### Function

> 주행 이력 삭제

### URL

> `/drivingHisDelete`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| date\_months | List\<String\> |  | 삭제 년.월(초단위Timestamp) |
| date\_days | List\<String\> |  | 삭제 년.월.일(초단위Timestamp) |
| reg\_ids | List\<String\> |  | 삭제 주행 이력 ID |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |

## 주행 이력 일 상세 리스트 조회
> Confluence page id: 2262307307 · 최종 수정: 10월 01, 2026

### Function

> 주행 이력 일 상세 리스트 조회

### URL

> `/drivingHisDayListDetail`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| date | String | O | 조회 년.월.일(초단위Timestamp) |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |
| details | List | 조회 날짜 주행 이력 날짜 상세 리스트 |
| ┣ reg\_id | String | 주행 이력 고유 ID |
| ┣ start\_addr | String | 출발 주소 |
| ┣ end\_addr | String | 도착 주소 |
| ┣ start\_dt | String | 출발 시간(초단위Timestamp) |
| ┣ end\_dt | String | 도착 시간(초단위Timestamp) |
| ┣ distance | Long | 주행 거리(단위 m) |
| ┗ point | Long | 마일리지 |

## 주행 이력 일 상세 리스트 조회 FivePin - AIR
> Confluence page id: 2262307327 · 최종 수정: 10월 01, 2026

### Function

> 주행 이력 일 상세 리스트 조회

### URL

> `/drivingHisDayListDetailUM`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| memCode | String | O | 아이나비 통합회원 멤버코드 |
| date | String | O | 조회 년.월.일(초단위Timestamp) |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |
| details | List | 조회 날짜 주행 이력 날짜 상세 리스트 |
| ┣ reg\_id | String | 주행 이력 고유 ID |
| ┣ start\_addr | String | 출발 주소 |
| ┣ end\_addr | String | 도착 주소 |
| ┣ start\_dt | String | 출발 시간(초단위Timestamp) |
| ┣ end\_dt | String | 도착 시간(초단위Timestamp) |
| ┗ distance | Long | 주행 거리(단위 m) |

## 주행 이력 일별 리스트 조회
> Confluence page id: 2262307347 · 최종 수정: 10월 01, 2026

### Function

> 주행 이력 일별 리스트 조회

### URL

> `/drivingHisDayList`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| date | String | O | 조회 년.월(초단위Timestamp) |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |
| total\_distance | Long | 조회 월 총 주행 거리 |
| total\_point | Long | 조회 월 총 적립 포인트 |
| days | List | 조회 월 주행 이력 일별 리스트 |
| ┣ date | String | 년.월.일(초단위Timestamp) |
| ┣ distance | Long | 주행 거리(단위 m) |
| ┗ point | Long | 마일리지 |

## 최근 목적지 리스트 등록
> Confluence page id: 2262307367 · 최종 수정: 10월 01, 2026

### Function

> 최근 목적지 리스트 등록

### URL

> `/latelyPoiListInsert`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| lately\_poi\_list | List | O | 최근 목적지 리스트 |
| ┣ name | String | O | 목적지 이름 |
| ┣ rpx | String | O | 탐색 X좌표 |
| ┣ rpy | String | O | 탐색 Y좌표 |
| ┣ dpx | String |  | Display X좌표 |
| ┣ dpy | String |  | Display Y좌표 |
| ┣ poi | String |  | POI ID |
| ┣ address | String |  | 지번 주소 |
| ┣ road\_address | String |  | 도로명 주소 |
| ┣ ts | String | O | Timestamp |
| ┣ catecode | String |  | 목적지 CATECODE |
| ┗ cnt | int | O | 목적지 탐색 횟수 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |

## 주행 이력별 상제 좌표 조회 FivePin - AIR
> Confluence page id: 2262307387 · 최종 수정: 10월 01, 2026

### Function

> 주행 이력별 좌표 조회 -Five Pin

### URL

> `/drivingHisCoordUM`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| regId | String | O | 주행 regId |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |
| userLocInfo | Object | 유저 주행정보 |
| ┣ id | String | 주행 regId |
| ┗ locTraces | List | 주행좌표 리스트 |
| ┣ lat | String | 출발지 위도, 정규화좌표 Y값(TW INDEX) |
| ┣ lng | String | 출발지 경도, 정규화좌표 X값(TW INDEX) |
| ┣ speed | Integer | 속도 |
| ┗ insert\_time | String | 입력시간 |

## 최근 목적지 리스트 조회
> Confluence page id: 2262307407 · 최종 수정: 10월 01, 2026

### Function

> 최근 목적지 리스트 조회

### URL

> `/latelyPoiListSelect`

[[inavi-air-api-common#Request Header|Request Header]]

### Request Parameter

> 원본 표가 비어 있음

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |
| lately\_poi\_list | List | 최근 목적지 리스트 |
| ┣ name | String | 목적지 이름 |
| ┣ rpx | String | 탐색 X좌표 |
| ┣ rpy | String | 탐색 Y좌표 |
| ┣ dpx | String | Display X좌표 |
| ┣ dpy | String | Display Y좌표 |
| ┣ poi | String | POI ID |
| ┣ address | String | 지번 주소 |
| ┣ road\_address | String | 도로명 주소 |
| ┣ ts | String | Timestamp |
| ┣ catecode | String | 목적지 CATECODE |
| ┗ cnt | int | 목적지 탐색 횟수 |

## 혼잡 차선 조회
> Confluence page id: 2262307427 · 최종 수정: 10월 01, 2026

### Function

> 혼잡 차선 KS Link ID 조회

### URL

> `/confusionLane`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| mrVer | String | O | 요청 MR Version |
| mrlinks | Array | O | 요청 MRLink 정보 리스트 |
| ┣ mapid | Integer | O | 도로 MapID |
| ┣ linkid | Integer | O | 도로 LinkID |
| ┗ direction | Integer | O | 도로 Direction |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |
| kslinks | Array | 응답 KSLink 정보 리스트 |
| ┣ mapid | Integer | 도로 MapID |
| ┣ linkid | Integer | 도로 LinkID |
| ┣ direction | Integer | 도로 Direction |
| ┣ speed | Integer | 속도 |
| ┗ kslinkid | Integer | 도로 KS LinkID |

## 확대도 정보 조회
> Confluence page id: 2262307447 · 최종 수정: 10월 01, 2026

### Function

> 확대도 정보 조회<br>확대도 ID(extid)는 한글을 포함하므로 Encoding(utf-8)을 하여 전송한다.<br>결과의 data\_url 사용 시에도 마지막 extid 부분은 Encoding(utf-8)하여 전송한다.

### URL

> `/extendedMap`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| extid | String | O | 확대도 ID |
| type | String |  | 확대도 tyep<br>ieg : 기존 이미지<br>mp4 : 영상 이미지 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |
| data\_url | String | 확대도 Data URL |
| extid | String | 조회한 3D확대도 ID |
| type | String | 요청한 확대도 tyep<br>ieg : 기존 이미지<br>mp4 : 영상 이미지 |

## 환경 설정 저장
> Confluence page id: 2262307467 · 최종 수정: 10월 06, 2026

### Function

> 환경설정 저장

### URL

> `/saveConfig`

[[inavi-air-api-common#Request Header|Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| hipass | String | O | 하이패스 옵션<br>0: OFF<br>1: ON |
| discount | String | O | 국가유공자 및 장애인 할인<br>0: OFF<br>1: ON |
| car\_type | String | O | 차종<br>0: 경차(1종 통행료 할인 적용)<br>1: 1종(소형차)<br>2: 2종(중형차)<br>3: 3종(대형차)<br>4: 4종(대형화물차)<br>5: 5종(특수화물차)<br>6: 이륜차 |
| oil\_type | String | O | 유종<br>0: 휘발유<br>1: 고급휘발유<br>2: 경유<br>3: LPG<br>4: 전기차 충전소<br>5: 수소 |
| oil\_station | String | O | 선호주유소 (중복 설정시 "\_"구분자로 전송 \*전체선택시 -\> 0, 이경우 이외 다른값 전달 금지)<br>0: 전체<br>1: SK<br>2: S-OIL<br>3: 현대 OilBank<br>4: GS<br>5: E-1<br>선호 충전기(중복 설정시 "\_"구분자로 전송)<br>0: DC차데모<br>1:AC급속3상<br>2:DC콤보<br>3:AC완속 |
| car\_mark | String | O | 자차마크<br>0: 기본<br>1: 흰색세단<br>2: 빨간스포츠카<br>3: 하늘색SUV<br>4: 노란스포츠카<br>5: 경찰차<br>6: 소방차<br>7: 파란색트럭<br>8 : 봉고차<br>9: 초록 해치백<br>10 : 파란버스<br>11 : 파란오토바이<br>12 : 빨간오토바이 |
| push\_status | String | O | PUSH 수신 동의 여부<br>0: OFF<br>1: ON |
| bbox | String | O | 블랙박스 설정상태<br>0: OFF<br>1: ON<br>(LOG)**N** |
| mapSetting | String | O | 지도다운로드설정<br>DW : 다운로드<br>STREAM: 스트리밍<br>(LOG)**N** |
| bboxAOF | String | O | 블랙박스 상시녹화 ON/OFF<br>(LOG)**N** |
| aIStatus | String | O | AI기능 활성화 ON/OFF<br>0: OFF<br>1: ON<br>(LOG)**N** |
| aIVCFlag | String | O | AI보이스호출 사용 ON/OFF<br>0: OFF<br>1: ON<br>2: 선택안함<br>(LOG)**N** |
| aIVCString | String | O | 0: 지니야<br>1: 기가지니<br>2: 선택안함 |
| gender | String |  | 성별<br>M: 남자<br>F : 여자 |
| birthday | String |  | 생년월일<br>EX([생년월일 예시 제거]) -\> YYYY.MM.DD |
| carNum | String |  | 차량번호<br>EX([차량번호 예시 제거]) |
| tutoComplete | boolean | O | 튜토리얼 완료여부 |
| birthTime | String |  | 태어난시간(ex : 1930)<br>모름 : DNK |
| sL | String |  | 음력 양력<br>양력 : S<br>음력 : L<br>음력윤달 : LI |
| cash\_push\_status | String |  | 에어 캐시 PUSH 수신 동의 여부<br>0 : 미동의<br>1 : 동의 |
| driveLineColor | String |  | 주행선 색상 (환경설정 -\> 지도설정 -\> 주행선 색상)<br>0 : traffic<br>1 : red<br>2 : orange<br>3 : yellow<br>4 : green<br>5 : blue (Default)<br>6 : indigo |
| onAirBenefits | String |  | 맞춤형 온에어 혜택 (Default ON)<br>0 : OFF<br>1 : ON |
| defaultRouteOption | String |  | 추천  경로 옵션 설정 (0 \~ 5)<br>0 : 에어추천 (Default)<br>1 : 가장 빠름 <br>2: 무료도로 <br>3: 큰길 위주<br>4: 고속도로 위주<br>5 : 최단 거리<br>6: 친환경 추천 |
| issueReport | String |  | 제보하기 개선 (Default OFF)<br>0 : OFF<br>1 : ON |
| onlyCamera | String |  | Only 카메라 모드 (Default OFF)<br>0 : OFF<br>1 : ON |
| realTimeTraffic | String |  | 실시간 교통 신호 안내 (Default ON)<br>0 : OFF<br>1 : ON |
| mainRecentPlaces | String |  | 메인화면 최근장소 더보기 (Default OFF)<br>0 : OFF<br>1 : ON |
| mbSpdEnfrc | String |  | 이동식 과속 단속 (Default : ON)<br>0 : OFF<br>1: ON |
| bxtSpEnfrc | String |  | 박스형 과속 단속 (Default : ON)<br>0 : OFF<br>1: ON |
| crckdIntrv | String |  | 끼어들기 단속 (Default : OFF)<br>0 : OFF<br>1: ON |
| ovrldCntrl | String |  | 과적 단속 (Default : OFF)<br>0 : OFF<br>1: ON |
| trfclCmr | String |  | 교통정보 수집 카메라(Default : ON)<br>0 : OFF<br>1: ON |
| sharpCurve | String |  | 급커브 구간 (Default : ON)<br>0 : OFF<br>1: ON |
| acdntBndln | String |  | 사고다발 구간 (Default : ON)<br>0 : OFF<br>1: ON |
| speedBump | String |  | 과속 방지턱 (Default : ON)<br>0 : OFF<br>1: ON |
| chlEldRsr | String |  | 어린이/노인 보호구역 (Default : ON)<br>0 : OFF<br>1: ON |
| wldlfSnctr | String |  | 야생동물 보호구역 (Default : ON)<br>0 : OFF<br>1: ON |
| rlrdCrsng | String |  | 철도 건널목 (Default : ON)<br>0 : OFF<br>1: ON |
| fallStSect | String |  | 낙석 구간 (Default : OFF)<br>0 : OFF<br>1: ON |
| entrnGrtrr | String |  | 녹색교통지역 진입 (Default : ON)<br>0 : OFF<br>1: ON |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |

## 회원탈퇴
> Confluence page id: 2262307487 · 최종 수정: 10월 01, 2026

### Function

> 통합 회원탈퇴

### URL

> `/integratedSignout`

[[inavi-air-api-common#Request Header|Request Header]]

### Request Parameter

> 원본 표가 비어 있음

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |

## Sources
- Confluence "INAVI AIR API" > 기타 (2026-10-27 조회): 기타 (2) (2262306807), AIR SOS (2262306885), KT 종료 마이그레이션 정보 조회 (2262306905), CCTV 상세 조회 (2) (2262306925), KT 종료 마이그레이션 파일 정보 조회 (2262306945), 대교 리스트 조회 (2262306965), 고속도로 휴게소 주유소 정보 조회 (2) (2262306985), 마일리지 이력 등록 (2262307007), 방면 음성 정보 조회 (2) (2262307027), 신규 DP 확대도 정보 조회 (2262307047), 외부 계정 연동 로그아웃 (2262307067), 외부 계정 연동 가입여부 확인 (2262307087), 외부 계정 연동 로그인 (2262307107), 외부 계정 연동 정보입력 (2262307127), 외부 계정 연동 통합회원 전환 로그인 (2262307147), 외부 계정 연동 회원탈퇴 (2262307167), 유고, VVMS, 수해 정보 상세 조회 (2) (2262307187), 제보하기 간소화 (2262307207), 재난, 긴급출동차량 위치 상세조회 (2262307227), 주행 이력 그룹 리스트 조회 FivePin - AIR (2262307247), 주행 이력 그룹 리스트 조회 (2262307267), 주행 이력 삭제 (2262307287), 주행 이력 일 상세 리스트 조회 (2262307307), 주행 이력 일 상세 리스트 조회 FivePin - AIR (2262307327), 주행 이력 일별 리스트 조회 (2262307347), 최근 목적지 리스트 등록 (2) (2262307367), 주행 이력별 상제 좌표 조회 FivePin - AIR (2262307387), 최근 목적지 리스트 조회 (2) (2262307407), 혼잡 차선 조회 (2) (2262307427), 확대도 정보 조회 (2) (2262307447), 환경 설정 저장 (2262307467), 회원탈퇴 (2262307487)
