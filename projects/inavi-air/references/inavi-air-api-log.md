---
title: "INAVI AIR API — 로그"
category: references
tags: [inavi-air, api, logging, visibility/internal]
aliases: [로그]
relationships:
  - target: "[[inavi-air-api-detail-spec]]"
    type: derived_from
sources: ["url:https://inavisystems.atlassian.net/wiki/spaces/AS/pages/2262307507"]
summary: >-
    INAVI AIR 로그 API(AI 로그, User Event 로그 전송, 에어연구소 로그, 주행로그 업로드)의 요청·응답 필드와 User Event 항목 전체를 Confluence 원문 그대로 옮긴 명세.
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

# INAVI AIR API — 로그

Confluence "INAVI AIR API" > "로그" 영역을 원문 그대로 옮긴 페이지다. 엔드포인트 색인은 [[inavi-air-api-detail-spec]], 공통 헤더와 결과 코드는 [[inavi-air-api-common]], 소속 프로젝트는 [[inavi-air]]이다.

| API | URL |
|---|---|
| AI 로그 업로드 | `/uploadAiLog` |
| 로그 전송(User Event) | `/userEvent` |
| 에어연구소 로그 업로드 | `/uploadAirlabLog` |
| 주행로그 업로드 | `/uploadDrivingLog` |

## 개요
> Confluence page id: 2262307507 · 최종 수정: 10월 06, 2026

- 📙공통 정보
- 🧭로그 전송(User Event)
- 🧭주행로그 업로드
- 🧭AI 로그 업로드
- 🧭에어연구소 로그 업로드

## AI 로그 업로드
> Confluence page id: 2262307549 · 최종 수정: 10월 01, 2026

### Function

> AI 업로드

### URL

`/uploadAiLog`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| aclData | String | O | \<ActTypeID\>│\<CallType\>│\<uword\>│\<ActTypeID\>│\<CallType\>│\<uword\>│...갯수만큼 반복한다<br>ActTypeID = AI 엔진에서 리턴된 액션 ID 값<br>CallType = C or V (C = Click. 버튼으로 호출. V = Voice. 보이스로 호출)<br>uword = AI 엔진에서 인식한 추가 String. 없다면 공백. |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |

## 로그 전송(User Event)
> Confluence page id: 2262307569 · 최종 수정: 10월 06, 2026

### Function

> 로그 전송(User Event)

### URL

`/userEvent`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description | 상태 |
| --- | --- | --- | --- | --- |
| **start\_route\_u** | Object | 제목 없음 | 안내시작(Log) | 운영 |
| ┣ cur\_x | String | 제목 없음 | 현위치x(좌표는 TW Index 좌표) | 운영 |
| ┣ cur\_y | String | 제목 없음 | 현위치y(좌표는 TW Index 좌표) | 운영 |
| ┣ rid | String | 제목 없음 | 경로 ID | 운영 |
| ┣ length | String | 제목 없음 | 경로길이 (단위 : M) | 운영 |
| ┣ etime | String | 제목 없음 | 목적지까지 걸리는 시간 (단위 : sec) | 운영 |
| ┣ inmethod | String | 제목 없음 | 경로탐색을 호출한 기능(통합검색, 최근검색어, 즐겨찾기, 이전목적지, 타임머신)<br>UNITED 통합검색<br>RECENT 최근검색어<br>FAV 즐겨찾기<br>PDEST 이전목적지<br>TM 타임머신<br>AI AI를통한 호출<br>MAP 지도(위치지정)<br>MAINCARD 메인카드<br>INTR 외부연동<br>NEARBY 주변검색<br>ADDR 주소검색<br>UNDEF 미정의 | 운영 |
| ┣ routeopt | String | 제목 없음 | 안내시작으로 선택한 경로의 경로옵션(추천/최소시간/편한길/이륜차/고속우선/무료경로/최단거리 등) <br>SGST 추천경로 (LGU+ 향으로는 “빠른길”)<br>FAST 최소시간<br>BEGI 초보자(편한길) (LGU+ 향으로는 “편한길”)<br>2W 이륜차<br>HIGH 고속우선<br>FREE 무료경로<br>SHORT 최단거리<br>SGECO 친환경추천탐색<br>T1R (트럭) 실시간 만차<br>T1RF (트럭) 실시간 만차 무료<br>T2R (트럭) 실시간 공차<br>T2RF (트럭) 실시간 공차 무료<br>T1N (트럭) 국도 만차<br>T2N (트럭) 국도 공차<br>TES (트럭) 공차시 추천경로<br>TEF (트럭) 공차시 무료경로<br>TEN (트럭) 공차시 국도위주경로<br>TFS (트럭) 만차시 추천경로<br>TFF (트럭) 만차시 무료경로<br>TFN (트럭) 만차시 국도위주경로 | 운영 |
| ┣ routeopt2 | String | 제목 없음 | 경로옵션2(대교탐색/해안도로/구간비교/주행중탐색)<br>BRDG 대교탐색<br>SHORE 해안도로 | 운영 |
| ┣ opt2string | String | 제목 없음 | 대교탐색 시 해당 대교의 이름 | 운영 |
| ┣ startpos | String | 제목 없음 | 출발지 정보: X / Y / PID / 이름 (지역명칭 or POI 명칭) (좌표는 TW Index 좌표) | 운영 |
| ┣ destpos | String | 제목 없음 | 도착지 정보: X / Y / PID / 이름 (지역명칭 or POI 명칭) (좌표는 TW Index 좌표) | 운영 |
| ┗ pasgpos | String | 제목 없음 | 경유지 정보: X / Y / PID / 이름 (지역명칭 or POI 명칭) (좌표는 TW Index 좌표)<br>경유지가 없다면 공란으로 입력, 경유지가 두개이면 연속해서 입력 | 운영 |
| **cancel\_route\_u** | Object | 제목 없음 | 경로취소(Log) | 운영 |
| ┣ cur\_x | String | 제목 없음 | 현위치x(좌표는 TW Index 좌표) | 운영 |
| ┣ cur\_y | String | 제목 없음 | 현위치y(좌표는 TW Index 좌표) | 운영 |
| ┣ rid | String | 제목 없음 | 경로 ID | 운영 |
| ┣ destpos | String | 제목 없음 | 도착지 정보<br>X / Y / PID / 이름 (지역명칭 or POI 명칭) (좌표는 TW Index 좌표) | 운영 |
| ┣ rlength | String | 제목 없음 | 남은 거리 (단위 : M) | 운영 |
| ┣ opt | String | 제목 없음 | AI: AI를 통한 호출<br>그외의 상황에서는 공백으로 보내주면됨 | 운영 |
| ┗ rtime | String | 제목 없음 | 남은 시간 (단위 : sec) | 운영 |
| **arrive\_nearby\_u** | Object | 제목 없음 | 목적지 접근 안내(Log)(경유지/히든경유지 접근안내 포함) | 운영 |
| ┣ rid | String | 제목 없음 | 경로 ID(Log) | 운영 |
| ┣ rdist | String | 제목 없음 | 남은 거리 (단위 : M) | 운영 |
| ┣ rtime | String | 제목 없음 | 남은 시간 (단위 : sec) | 운영 |
| ┣ posinfo | String | 제목 없음 | 경유지/목적지<br>PASG 경유지<br>DEST 목적지 | 운영 |
| ┣ objpos | String | 제목 없음 | 도착지 정보 X / Y / PID / 이름 (지역명칭 or POI 명칭) (좌표는 TW Index 좌표) | 운영 |
| **goal\_notify\_u** | Object | 제목 없음 | 도착안내 팝업(Log) | 운영 |
| ┣ rid | String | 제목 없음 | 경로 ID | 운영 |
| ┣ length | String | 제목 없음 | 경로 총 길이 (단위 : M) | 운영 |
| ┣ time | String | 제목 없음 | 주행 총 시간 (단위 : sec) | 운영 |
| ┣ destpos | String | 제목 없음 | 도착지 정보: X / Y / PID / 이름 (지역명칭 or POI 명칭) (좌표는 TW Index 좌표) | 운영 |
| ┗ point | String | 제목 없음 | 화면상에 보여준 마일리지 적립 포인트 값 | 운영 |
| **poi\_share\_u** | Object | 제목 없음 | 위치공유(Log) | 운영 |
| ┣ name | String | 제목 없음 | POI 이름 | 운영 |
| ┣ pid | String | 제목 없음 | POI ID | 운영 |
| ┗ shopt | String | 제목 없음 | 공유 방식 구분 - SMS / COPY / KAKAO / LINE / BAND | 운영 |
| **opt\_blackbox\_u** | Object | 제목 없음 | 블랙박스(Log) | 운영 |
| ┗ opt | String | 제목 없음 | 블랙박스 버튼 사용시 - ON: 녹화시작, OFF: 녹화종료 | 운영 |
| **app\_entry\_u** | Object | 제목 없음 | 앱 종료(Log) | 운영 |
| ┗ opt | String | 제목 없음 | OFF로 String 값 고정 | 운영 |
| **stat\_map\_dw\_u** | Object | 제목 없음 | 지도 다운로드(Log) | 운영 |
| ┣ result | String | 제목 없음 | 다운로드 결과 (OK/FAIL) | 운영 |
| ┣ version | String | 제목 없음 | 지도버전 | 운영 |
| ┣ mode | String | 제목 없음 | 다운로드/스트리밍 (DW/STREAM) | 운영 |
| ┗ etc | String | 제목 없음 | 안전운행 데이터 버전 | 운영 |
| **carplay\_u** | Object | 제목 없음 | 카플레이 설정(Log) | 운영 |
| ┣ uiType | String | 제목 없음 | 화면타입 (CarPlay\_Map) | 운영 |
| ┗ maptheme | String | 제목 없음 | 지도테마 설정값(NORMAL / EXTREME3D) **+ 설정값 추가 (NORMAL / EXTREME3D / CARTOON / NATURE)** | 변경 |
| **maptheme\_a** | Object | 제목 없음 | 맵테마설정 | 운영 |
| ┗ maptheme | String | 제목 없음 | 지도테마 설정값 - NORMAL / EXTREME3D / CARTOON / NATURE | 운영 |
| **android\_auto\_u** | Object | 제목 없음 | 안드로이드 설정(Log) | 신규 |
| ┣ platform | String | 제목 없음 | 플랫폼 (Android) 고정 | 신규 |
| ┣ guidevolume | String | 제목 없음 | 안내 볼륨 설정 값 - MUTE / LOW / MEDIUM / HIGH / MAX | 신규 |
| ┣ autovolumeflag | String | 제목 없음 | 볼륨 자동 조절 - Y / N | 신규 |
| ┣ lanecolor | String | 제목 없음 | 주행선 색상 - RTTI / RED / ORANGE / YELLOW / GREEN / BLUE | 신규 |
| ┣ daynightmode | String | 제목 없음 | 주/야간 모드 - SYNC / AUTO / DAY / NIGHT | 신규 |
| ┣ viewmode | String | 제목 없음 | 뷰 모드 - 3D / 2DROTATE / 2DFIX | 신규 |
| ┣ maptheme | String | 제목 없음 | 지도테마 설정값 - NORMAL / EXTREME3D / CARTOON / NATURE | 신규 |
| ┣ mapfontsize | String | 제목 없음 | 지도 글자 크기 - SMALL / DEFAULT / LARGE | 신규 |
| ┗ mapzoom | String | 제목 없음 | 속도별 지도 확대/축소 - AUTO / NEAR / DEFAULT / FAR / FARTHER | 신규 |
| **airlab\_setting\_u** | Object | 제목 없음 | 에어연구소 설정 로그 (에어연구소 설정 변경시) | 신규 |
| ┣ airbot | String | 제목 없음 | 에어봇 로그 - ON/OFF | 신규 |
| ┣ hudsetting | String | 제목 없음 | 카플레이 연결시 HUD 길안내 - ON/OFF | 신규 |
| ┣ routeopt | String | 제목 없음 | 경로 안내 기본 옵션 설정 - SGST / FAST / FREE / MAINROAD / HIGHWAY / SHORT | 신규 |
| ┣ voicecancel | String | 제목 없음 | 기본 안내 음성 제거 - ON/OFF | 신규 |
| ┣ smartsig | String | 제목 없음 | 똑똑한 신호등 - ON/OFF | 신규 |
| ┗ homesetting | String | 제목 없음 | 메인화면 설정 - ON/OFF | 신규 |
| **airbot\_ask\_u** | Object | 제목 없음 | 에어봇 질의응답 로그 (에어봇 질문 입력 -\> 답변 완료시) | 신규 |
| ┣ result | String | 제목 없음 | 결과코드 | 신규 |
| ┣ inputtype | String | 제목 없음 | 질문 종류 - SGST: 추천 질문 / CUSTOM: 직접 입력 | 신규 |
| ┣ questionstring | String | 제목 없음 | 입력 질문 | 신규 |
| ┗ suggestlist | String | 제목 없음 | 에어봇 추천 장소 리스트 (장소로 이어지는 키워드만 적재)<br>검색어1/검색어2/검색어3/…/검색어n<br>에어봇 추천 장소가 없으면 공란 입력, 두개이상이면 연속해서 입력 | 신규 |
| **nearby\_fav\_poi\_u** | Object | 제목 없음 | 주변 인기장소 정보 로그 (메인화면 → '주변인기장소' 클릭시) | 신규 |
| ┣ poiid | String | 제목 없음 | POI ID | 신규 |
| ┗ poiname | String | 제목 없음 | POI 명칭 | 신규 |

> requisite 열의 "제목 없음"은 원본 셀 값 그대로다.

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |

## 에어연구소 로그 업로드
> Confluence page id: 2262307589 · 최종 수정: 10월 01, 2026

### Function

> AI 업로드

### URL

`/uploadAirlabLog`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| properties | ArrayObject | O | LogAPI 규격 프로퍼티 개수만큼 설정 |
| ┣ name | String |  | 프로퍼티 이름 |
| ┗ value | String |  | 프로퍼티 값 |
| 제목 없음 |  |  |  |
| 프로퍼티 목록 |  |  | 로그 API 규격 추가시 규격과 동일한 순서대로 전달 (유연한 설정 가능) |
| ┣ airbot | String |  | 에어봇 로그 - ON/OFF |
| ┣ hudSetting | String |  | 카플레이 연결시 HUD 길안내 - ON/OFF |
| ┣ routeOpt | String |  | 경로 안내 기본 옵션 설정 - SGST / FAST / FREE / MAINROAD / HIGHWAY / SHORT |
| ┣ voiceCancel | String |  | 기본 안내 음성 제거 - ON/OFF |
| ┣ smartSig | String |  | 똑똑한 신호등 - ON/OFF |
| ┗ homeSetting | String |  | 메인화면 설정 - ON/OFF |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| [[#result_code\|result\_code]] | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| [[#result_msg\|result\_msg]] | String | 결과코드에 따른 메세지 |

> 원본에 Response Parameter 표가 두 번 있다. 두 번째 표의 parameter 셀은 아래 하위 페이지(result_code, result_msg)로 링크된다.

#### result_code
> Confluence page id: 2262307613 · 최종 수정: 10월 01, 2026

> 원본 표가 비어 있음 (원본 페이지 본문이 비어 있다)

#### result_msg
> Confluence page id: 2262307629 · 최종 수정: 10월 01, 2026

> 원본 표가 비어 있음 (원본 페이지 본문이 비어 있다)

## 주행로그 업로드
> Confluence page id: 2262307645 · 최종 수정: 10월 01, 2026

### Function

> 주행로그 업로드

### URL

`/uploadDrivingLog`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| data | File | O | Upload 할 File (Multipart로 파일을 전송한다.) |
| rtopt | String | O | 경로 여부<br>0 : 경로 없음<br>1 : 경로 있음 |
| sec | String | O | 주행 시간(초단위 입력) |
| dist | String | O | 주행 거리 |
| mrVersion | String | O | MR Version (19.01a) |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |

## Sources

- Confluence "INAVI AIR API" > 로그 (2026-10-27 조회): 로그 (2262307507), AI 로그 업로드 (2262307549), 로그 전송(User Event) (2262307569), 에어연구소 로그 업로드 (2262307589), result_code (2262307613), result_msg (2262307629), 주행로그 업로드 (2262307645)
