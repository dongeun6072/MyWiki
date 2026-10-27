---
title: "INAVI AIR API — 에어 캐시"
category: references
tags: [inavi-air, api, air-cash, coupon, visibility/internal]
aliases: [에어 캐시, 에어 캐시 API]
relationships:
  - target: "[[inavi-air-api-detail-spec]]"
    type: derived_from
sources: ["url:https://inavisystems.atlassian.net/wiki/spaces/AS/pages/2262308151"]
summary: >-
    Confluence "INAVI AIR API > 에어 캐시" 하위 16개 API(캐시 정보·적립, 스탬프, 룰렛, 상품 카탈로그, 쿠폰 구매·쿠폰함·재발송, 적립내역)의 요청·응답 명세를 원문 그대로 옮긴 페이지.
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

# INAVI AIR API — 에어 캐시

Confluence "에어 캐시" 영역을 원문 그대로 옮긴 것이다. 전체 목록은 [[inavi-air-api-detail-spec]], 공통 Request Header·결과 코드는 [[inavi-air-api-common]], 서비스 개요는 [[inavi-air]]를 본다.

| API | URL |
| --- | --- |
| [[#에어 캐시 정보 조회]] | `/cashInfo` |
| [[#에어 캐시 적립하기]] | `/cashSave` |
| [[#구매 상품 카탈로그 조회]] | `/productList` |
| [[#구매 상품 카탈로그 상세 정보 조회]] | `/productDetail` |
| [[#쿠폰 구매하기]] | `/couponPurchase` |
| [[#쿠폰함 조회]] | `/couponBox` |
| [[#쿠폰함 상세 정보 조회]] | `/couponBoxDetail` |
| [[#쿠폰 재발송]] | `/couponResend` |
| [[#적립내역]] | `/airCashHistory` |
| [[#룰렛 게임]] | `/roulette` |
| [[#적립 스탬프 조회]] | `/stampHistory` |
| [[#스탬프 완성(랜덤 캐시 지급)]] | `/stampComplete` |
| [[#캐시 스탬프 적립 (구 미적립 캐시 스탬프 적립)]] | `/cashStampSave` |
| [[#에어 캐시 및 스탬프 정보 조회]] | `/cashStampInfo` |
| [[#에어 캐시 스탬프 룰렛 게임]] | `/cashStampRouletteGame` |
| [[#에어 캐시 스탬프 룰렛 이용권 조회]] | `/cashStampRouletteTicket` |

## 개요
> Confluence page id: 2262308151 · 최종 수정: 10월 06, 2026

- 🧭에어 캐시 정보 조회 → [[#에어 캐시 정보 조회]]
- 🧭에어 캐시 적립하기 → [[#에어 캐시 적립하기]]
- 🧭구매 상품 카탈로그 조회 → [[#구매 상품 카탈로그 조회]]
- 🧭구매 상품 카탈로그 상세 정보 조회 → [[#구매 상품 카탈로그 상세 정보 조회]]
- 🧭쿠폰 구매하기 → [[#쿠폰 구매하기]]
- 🧭쿠폰함 조회 → [[#쿠폰함 조회]]
- 🧭쿠폰함 상세 정보 조회 → [[#쿠폰함 상세 정보 조회]]
- 🧭쿠폰 재발송 → [[#쿠폰 재발송]]
- 🧭적립내역 → [[#적립내역]]
- 🧭룰렛 게임 → [[#룰렛 게임]]
- 🧭적립 스탬프 조회 → [[#적립 스탬프 조회]]
- 🧭스탬프 완성(랜덤 캐시 지급) → [[#스탬프 완성(랜덤 캐시 지급)]]
- 🧭캐시 스탬프 적립 (구 미적립 캐시 스탬프 적립) → [[#캐시 스탬프 적립 (구 미적립 캐시 스탬프 적립)]]
- 🧭에어 캐시 및 스탬프 정보 조회 → [[#에어 캐시 및 스탬프 정보 조회]]
- 🧭에어 캐시 스탬프 룰렛 게임 → [[#에어 캐시 스탬프 룰렛 게임]]
- 🧭에어 캐시 스탬프 룰렛 이용권 조회 → [[#에어 캐시 스탬프 룰렛 이용권 조회]]

## 구매 상품 카탈로그 상세 정보 조회
> Confluence page id: 2262308199 · 최종 수정: 10월 01, 2026

### Function

> 구매 상품 카탈로그 상세 정보 조회

### URL

> `/productDetail`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| productCode | String | O | 상품 코드 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| productDetail | Object | 상품 상세 정보 |
| ┣ productName | String | 상품명 |
| ┣ imageUrl | String | 상품이미지 URL |
| ┣ company | String | 회사이름 |
| ┣ sellPrice | Integer | 판매가격 |
| ┣ discountPrice | Integer | 할인 판매 가격 (`discountFlag`가 true일 경우에만 유효한 데이터) |
| ┣ discountFlag | boolean | 할인 판매 가격 적용 여부 플래그<br>true : 할인 판매 가격 적용<br>false : 할인 판매 가격 미적용 |
| ┗  useNote | String | 유의 사항 |
| totalAirCash | Integer | 나의 총 에어 캐시 |
| mdn | String | 쿠폰 수신 암호화 MDN |

## 구매 상품 카탈로그 조회
> Confluence page id: 2262308219 · 최종 수정: 10월 01, 2026

### Function

> 구매 상품 카탈로그 조회

### URL

> `/productList`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| productList | Array | 구매 가능한 상품리스트 |
| ┣ productName | String | 상품명 |
| ┣ productCode | String | 상품 코드 |
| ┣ imageUrl | String | 상품이미지 URL |
| ┣ company | String | 회사이름 |
| ┣ sellPrice | Integer | 판매가격 |
| ┣ discountPrice | Integer | 할인 판매 가격 (`discountFlag`가 true일 경우에만 유효한 데이터) |
| ┗ discountFlag | boolean | 할인 판매 가격 적용 여부 플래그<br>true : 할인 판매 가격 적용<br>false : 할인 판매 가격 미적용 |
| totalAirCash | Integer | 나의 총 에어 캐시 |

## 룰렛 게임
> Confluence page id: 2262308239 · 최종 수정: 10월 01, 2026

### Function

> 룰렛 게임

### URL

> `/roulette`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| type | String | O | 룰렛 타입<br>P : 프리미엄<br>S : 스페셜<br>B : 보너스 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]]<br>502 : 에어 마일 관련 에러 (에어 마일이 부족하거나 1000 마일 이상 보유자가 보너스 룰렛을 시도했을 때)<br>970 : 에어 캐시 정합성 체크 실패 (캐시 어뷰징 의심) |
| result\_msg | String | 결과값에 따른 메세지 |
| winningCash | Integer | 당첨 캐시 |
| totalAirMile | Integer | 에어 마일리지 |
| convertedCash | Integer | 전환된 에어 캐시 |

## 스탬프 완성(랜덤 캐시 지급)
> Confluence page id: 2262308259 · 최종 수정: 10월 01, 2026

### Function

> 스탬프 완성(랜덤 캐시 지급)

### URL

> `/stampComplete`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]]<br>0 : 성공<br>970 : 에어 캐시 정합성 체크 실패 (캐시 어뷰징 의심)<br>999 : 정의 되지 않은 오류 |
| result\_msg | String | 결과코드에 따른 메세지 |
| randomCash | Integer | 추가 지급 된 랜덤 캐시 |

## 에어 캐시 및 스탬프 정보 조회
> Confluence page id: 2262308279 · 최종 수정: 10월 01, 2026

### Function

> 에어 캐시 및 스탬프 정보 조회

### URL

> `/cashStampInfo`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]]<br>0 : 성공<br>999 : 정의 되지 않은 오류 |
| result\_msg | String | 결과코드에 따른 메세지 |
| noneSavedCashValidDt | String | 미적립 캐시 유효 기간 표출 문구<br>EX ) 24시간 |
| myAirCashInfo | Object | 나의 에어캐시 정보 |
| ┣ totalAirCash | Integer | 나의 총 에어 캐시 |
| ┣ todaySavedCash | Integer | 오늘 주행을 통해 적립된 캐시 |
| ┣ todayOnAirSavedCash | Integer | 오늘 온에어를 통해 적립된 캐시 |
| ┣ todayDrivingDistance | Integer | 오늘 주행 거리(m) |
| ┣ maxDrivingDistance | Integer | 최대 주행 거리(m) |
| ┣ maxCash | Integer | 최대 적립 캐시 |
| ┗ offerWall | Boolean | 오퍼월 활성 여부<br>true: 활성화<br>false: 비활성화 |
| currentMonth | Integer | 현재 월(1 \~ 12)<br>ex) 6 |
| stampCount | Integer | 랜덤 캐시 지급을 위해 한달에 모아야 하는 스탬프 갯수<br>Default : 9 |
| stampNotiMsg | String | 스탬프 하단 안내 문구<br>EX)<br>• 스탬프는 최대 1일 1개 제공되며, 매월 1일 초기화 됩니다.<br>• 추가 캐시 지급이 완료되면 스탬프는 처음부터 다시시작됩니다.<br>• 미적립 캐시는 3일간 유효하며 이후엔 자동 소멸됩니다.<br>• 캐시 유효기간 및 적립스탬프는 아이나비 에어의 정책에 따라 변경될 수 있습니다. |
| stampList | Array | 스탬프 리스트 |
| ┣ date | String | 날짜 (`MM-dd)`<br>ex) 04-19 |
| ┗ status | String | 적립 상태 여부<br>S : 적립 상태<br>N : 미적립 상태<br>A : 적립/미적립 모두 보유 상태 |
| stampStartNumber | Integer | 스탬프 해당 회차 기준 시작 숫자<br>ex)<br>1회차 : 1<br>2회차 : 10<br>3회차 : 19<br>4회차 : 28 |
| storyMsg | String | 표출 스토리 문구<br>ex) 주행 적립하면 9회차에 캐시 룰렛 도착! |
| rouletteButtonActive | String | 룰렛 버튼 활성화/비활성화 여부<br>Y : 활성화<br>N : 비활성화 |
| rouletteButtonMsg | String | 룰렛 버튼 표출 문구<br>ex) 캐시 룰렛 도착! |
| skpEventInfo | Object | SKP 이벤트 관련 정보(2023년 12월 31일 이후 제거 예정) |
| ┣ url | String | SKP URL<br>ex) `[URL]` |
| ┗date | String | 날짜 (yyyyMMdd)<br>ex)20231231 |

## 에어 캐시 스탬프 룰렛 게임
> Confluence page id: 2262308299 · 최종 수정: 10월 01, 2026

### Function

> 에어 캐시 스탬프 룰렛 게임

### URL

> `/cashStampRouletteGame`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]]<br>0 : 성공<br>970 : 에어 캐시 정합성 체크 실패 (캐시 어뷰징 의심)<br>972 : 에어캐시 스탬프 룰렛 이용권 미존재<br>999 : 정의 되지 않은 오류 |
| result\_msg | String | 결과코드에 따른 메세지 |
| cash | Integer | 당첨 캐시 |

## 에어 캐시 적립하기
> Confluence page id: 2262308319 · 최종 수정: 10월 01, 2026

### Function

> 에어 캐시 적립하기

### URL

> `/cashSave`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]]<br>970 : 에어 캐시 정합성 체크 실패 (캐시 어뷰징 의심) |
| result\_msg | String | 결과값에 따른 메세지 |
| randomCashYn | String | 랜덤 캐시 지급 가능 여부<br>Y : 지급 가능<br>N : 지급 불가 |
| noneSavedCashYn | String | 미적립 캐시 존재 여부<br>Y : 존재<br>N : 미존재 |
| myAirCashInfo | Object | 나의 에어캐시 정보 |
| ┣ totalAirCash | Integer | 나의 총 에어 캐시 |
| ┣ todaySavedCash | Integer | 오늘 주행을 통해 적립된 캐시 |
| ┣ todayOnAirSavedCash | Integer | 오늘 온에어를 통해 적립된 캐시 |
| ┣ todayDrivingDistance | Integer | 오늘 주행 거리(m) |
| ┣ maxDrivingDistance | Integer | 최대 주행 거리(m) |
| ┣ maxCash | Integer | 최대 적립 캐시 |
| ┣  saveableAirCash | Integer | 적립 가능한 캐시 |
| ┗ offerWall |  | 오퍼월 활성 여부<br>true: 활성화<br>false: 비활성화 |

## 에어 캐시 스탬프 룰렛 이용권 조회
> Confluence page id: 2262308339 · 최종 수정: 10월 01, 2026

### Function

> 에어 캐시 스탬프 룰렛 이용권 조회

### URL

> `/cashStampRouletteTicket`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]]<br>0 : 성공<br>999 : 정의 되지 않은 오류 |
| result\_msg | String | 결과코드에 따른 메세지 |
| count | Integer | 이용권 횟수 |

## 에어 캐시 정보 조회
> Confluence page id: 2262308359 · 최종 수정: 10월 01, 2026

### Function

> 에어 캐시 정보 조회

### URL

> `/cashInfo`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| 제목 없음 |  |  |  |

> 원본 표가 비어 있음 (행 하나에 "제목 없음"만 있음)

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과값에 따른 메세지 |
| randomCashYn | String | 랜덤 캐시 지급 가능 여부<br>Y : 지급 가능<br>N : 지급 불가 |
| noneSavedCashYn | String | 미적립 캐시 존재 여부<br>Y : 존재<br>N : 미존재 |
| noneSavedCashValidDt | String | 미적립 캐시 유효 기간 표출 문구<br>EX ) 24시간 |
| myAirCashInfo | Object | 나의 에어캐시 정보 |
| ┣ totalAirCash | Integer | 나의 총 에어 캐시 |
| ┣ todaySavedCash | Integer | 오늘 주행을 통해 적립된 캐시 |
| ┣ todayOnAirSavedCash | Integer | 오늘 온에어를 통해 적립된 캐시 |
| ┣ todayDrivingDistance | Integer | 오늘 주행 거리(m) |
| ┣ maxDrivingDistance | Integer | 최대 주행 거리(m) |
| ┣ maxCash | Integer | 최대 적립 캐시 |
| ┣ saveableAirCash | Integer | 적립 가능한 캐시 |
| ┗ offerWall | Boolean | 오퍼월 활성 여부<br>true: 활성화<br>false: 비활성화 |
| rouletteInfo | Object | 룰렛 관련 정보 |
| ┣ totalAirMile | Integer | 나의 총 에어 마일리지 |
| ┣ convertedCash | Integer | 전환된 에어 캐시 |
| ┗ roulettePeriod | String | 룰렛 기간 |

## 적립내역
> Confluence page id: 2262308379 · 최종 수정: 10월 01, 2026

### Function

> 적립 내역

### URL

> `/airCashHistory`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| currentMonth | Integer | 현재 월(1 \~ 12)<br>ex) 6 |
| useableAirCash | Integer | 사용 가능한 에어 캐시 |
| exipiredAirCash | Integer | 소멸 예정 에어 캐시 |
| expiredAirCashPopMsg | Object | 소멸 예정 캐시 팝업 |
| ┣ title | String | 제목<br>ex) 소멸 예정 캐시 |
| ┗ contents | String | 내용<br>ex) 약관에 따라 \~ 소멸 예정 캐시 부터 사용 됩니다. |
| airCashHistoryList | Array | 적립 내역 리스트 |
| ┣ date | String | 날짜 (MM.dd)<br>ex) 05.08 |
| ┣ type | String | 항목 (적립 OR 사용)<br>ex) 적립 |
| ┣ detail | String | 항목 상세 내역<br>ex) 주행 거리 적립 |
| ┗ cash | Integer | 적립 OR 사용 항목 캐시<br>ex)<br>적립 case : 20<br>사용 case : -100 |

## 적립 스탬프 조회
> Confluence page id: 2262308399 · 최종 수정: 10월 01, 2026

### Function

> 적립 스탬프 조회

### URL

> `/stampHistory`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]]<br>0 : 성공<br>920 : 이벤트 종료 사유 등으로 서버 메세지 표출<br>999 : 정의 되지 않은 오류 |
| result\_msg | String | 결과코드에 따른 메세지 |
| currentMonth | Integer | 현재 월(1 \~ 12)<br>ex) 6 |
| stampCount | Integer | 랜덤 캐시 지급을 위해 한달에 모아야 하는 스탬프 갯수<br>Default : 9 |
| baseDay | String | 적립 스탬프 기준 일<br>Ex) “한 달” |
| randomCashYn | String | 랜덤 캐시 지급 가능 여부<br>Y : 지급 가능<br>N : 지급 불가 |
| stampNotiMsg | String | 스탬프 안내 문구<br>EX)<br>• 스탬프는 최대 1일 1개 제공되며, 매월 1일 초기화 됩니다.<br>• 추가 캐시 지급이 완료되면 스탬프는 처음부터 다시시작됩니다.<br>• 미적립 캐시는 3일간 유효하며 이후엔 자동 소멸됩니다.<br>• 캐시 유효기간 및 적립스탬프는 아이나비 에어의 정책에 따라 변경될 수 있습니다. |
| stampList | Array | 스탬프 리스트 |
| ┣ date | String | 날짜 (`MM-dd)`<br>ex) 04-19 |
| ┣ status | String | 적립 상태 여부<br>S : 적립 상태<br>N : 미적립 상태 |
| ┣ cash | Integer | 적립된 캐시 OR 적립 가능한 캐시 |
| ┗ randomCash | Integer | 적립 된 랜덤 캐시<br>- 랜덤 캐시 전환 후 초기화 이전 표출 될 랜덤 캐시<br>- stampLIst 마지막 값만 유효하며 나머지 값들은 0<br>- 랜덤캐시 전환 이력이 없는 경우 모두 0 |
| stampStartNumber | Integer | 스탬프 배경 숫자 변경을 위한 시작 값 (해당 회차 기준 시작 숫자)<br>ex)<br>1회차 : 1<br>2회차 : 10<br>3회차 : 19<br>4회차 : 28 |

## 캐시 스탬프 적립 (구 미적립 캐시 스탬프 적립)
> Confluence page id: 2262308419 · 최종 수정: 10월 01, 2026

### Function

> 캐시 스탬프 적립 (구 미적립 캐시 스탬프 적립)

### URL

> `/cashStampSave`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| date | String | O | 적립할 캐시 스탬프의 미적립 날짜 (`MM-dd)`<br>[[#적립 스탬프 조회\|🧭적립 스탬프 조회]] 의 date<br>[[#스탬프 완성(랜덤 캐시 지급)\|🧭스탬프 완성(랜덤 캐시 지급)]] 의 date<br>EX) 04-01 |
| cashRenewal | String |  | 에어 캐시 고도화 버전 여부<br>Y : 에어 캐시 고도화 버전 |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]]<br>0 : 성공<br>970 : 에어 캐시 정합성 체크 실패 (캐시 어뷰징 의심)<br>971 : 유효하지 않은 캐시 스탬프 date (이미 소멸 된 캐시 의심)<br>⇒ 해당 에러를 받을 경우,<br>[[#적립 스탬프 조회\|🧭적립 스탬프 조회]] 호출하여 데이터 구성 필요<br>999 : 정의 되지 않은 오류 |
| result\_msg | String | 결과코드에 따른 메세지 |
| cash | Integer | `캐시 고도화 이전` : 해당 날짜에 적립 된 스탬프의 캐시<br>`캐시 고도화 이후` : 현재 적립 되는 캐시 |

## 쿠폰 구매하기
> Confluence page id: 2262308443 · 최종 수정: 10월 01, 2026

### Function

> 쿠폰 구매하기

### URL

> `/couponPurchase`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| productCode | String | O | 상품 코드 |
| mdn | String | O | 암호화 된 MDN |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]]<br>501 : 에어 캐시 부족<br>970 : 에어 캐시 정합성 체크 실패 (캐시 어뷰징 의심) |
| result\_msg | String | 결과코드에 따른 메세지 |
| totalAirCash | Integer | 나의 총 에어 캐시 |

## 쿠폰 재발송
> Confluence page id: 2262308463 · 최종 수정: 10월 01, 2026

### Function

> 쿠폰 재발송

### URL

> `/couponResend`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| trId | String | O | 트랜잭션 ID |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]]<br>`920`인 경우, `result_msg`를 통해 메시지 표출 |
| result\_msg | String | 결과코드에 따른 메세지 |

## 쿠폰함 상세 정보 조회
> Confluence page id: 2262308483 · 최종 수정: 10월 01, 2026

### Function

> 쿠폰 상세 정보 조회

### URL

> `/couponBoxDetail`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| trId | String | O | 트랜잭션 ID |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| gift | Object | 상품리스트 |
| ┣ giftImageUrl | String | 상품 이미지 URL |
| ┣ company | String | 회사명 |
| ┣ productName | String | 상품명 |
| ┣ trId | String | 트랜잭션 ID (재발송 시 필요) |
| ┣ drawingDate | String | 발급일 |
| ┣ expireDate | String | 만료일 |
| ┣ isExpired | Boolean | 만료여부 |
| ┣ isResend | Boolean | 재전송 가능여부 |
| ┣ useNote | String | 유의 사항 |
| ┗ mdn | String | 쿠폰 수신한 암호화 MDN |

## 쿠폰함 조회
> Confluence page id: 2262308503 · 최종 수정: 10월 01, 2026

### Function

> 쿠폰함 조회

### URL

> `/couponBox`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| giftList | Array | 상품리스트 |
| ┣ giftImageUrl | String | 상품 이미지 URL |
| ┣ company | String | 회사명 |
| ┣ productName | String | 상품명 |
| ┣ trId | String | 트랜잭션 ID (재발송 시 필요) |
| ┣ expireDate | String | 만료일 |
| ┗  isExpired | Boolean | 만료여부 |

## Sources

- Confluence "INAVI AIR API" > 에어 캐시 (2026-10-27 조회): 에어 캐시 (2262308151), 구매 상품 카탈로그 상세 정보 조회 (2262308199), 구매 상품 카탈로그 조회 (2262308219), 룰렛 게임 (2262308239), 스탬프 완성(랜덤 캐시 지급) (2262308259), 에어 캐시 및 스탬프 정보 조회 (2262308279), 에어 캐시 스탬프 룰렛 게임 (2262308299), 에어 캐시 적립하기 (2262308319), 에어 캐시 스탬프 룰렛 이용권 조회 (2262308339), 에어 캐시 정보 조회 (2262308359), 적립내역 (2262308379), 적립 스탬프 조회 (2262308399), 캐시 스탬프 적립 (구 미적립 캐시 스탬프 적립) (2262308419), 쿠폰 구매하기 (2262308443), 쿠폰 재발송 (2262308463), 쿠폰함 상세 정보 조회 (2262308483), 쿠폰함 조회 (2262308503)
