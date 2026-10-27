---
title: "INAVI AIR API — 이벤트"
category: references
tags: [inavi-air, api, event, lucky-box, visibility/internal]
aliases: [이벤트, 이벤트 API, 행운상자 API]
relationships:
  - target: "[[inavi-air-api-detail-spec]]"
    type: derived_from
sources: ["url:https://inavisystems.atlassian.net/wiki/spaces/AS/pages/2262308561"]
summary: >-
    Confluence "INAVI AIR API > 이벤트" 하위 7개 API(이벤트 조회, 행운상자 정보·뽑기·보관함·상품리스트, 이벤트 페이지 에어 캐시 적립, 모바일 교환권 캐시 적립)의 명세를 원문 그대로 옮긴 페이지.
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

# INAVI AIR API — 이벤트

Confluence "이벤트" 영역을 원문 그대로 옮긴 것이다. 전체 목록은 [[inavi-air-api-detail-spec]], 공통 Request Header·결과 코드는 [[inavi-air-api-common]], 서비스 개요는 [[inavi-air]]를 본다.

| API | URL |
| --- | --- |
| [[#이벤트 조회]] | `/event` |
| [[#행운상자 상품리스트 조회(Admin)]] | `/getLuckyProductList` |
| [[#행운상자 정보]] | `/getLuckyBoxStatus` |
| [[#행운상자 뽑기]] | `/luckyBoxOpen` |
| [[#행운상자 뽑기 이력 및 쿠폰리스트 조회(보관함)]] | `/luckyBoxList` |
| [[#에어 캐시 적립]] | `/event/cash/earn` |
| [[#모바일 교환권 캐시 적립]] | `/event/cash/voucherExchange` |

## 개요
> Confluence page id: 2262308561 · 최종 수정: 10월 06, 2026

- 🧭이벤트 조회 → [[#이벤트 조회]]
- 🧭행운상자 상품리스트 조회(Admin) → [[#행운상자 상품리스트 조회(Admin)]]
- 🧭행운상자 정보 → [[#행운상자 정보]]
- 🧭행운상자 뽑기 → [[#행운상자 뽑기]]
- 🧭행운상자 뽑기 이력 및 쿠폰리스트 조회(보관함) → [[#행운상자 뽑기 이력 및 쿠폰리스트 조회(보관함)]]
- 🧭에어 캐시 적립 → [[#에어 캐시 적립]]
- 🧭모바일 교환권 캐시 적립 → [[#모바일 교환권 캐시 적립]]

## 에어 캐시 적립
> Confluence page id: 2262308591 · 최종 수정: 10월 01, 2026

### Function

> 이벤트 페이지 에어 캐시 적립

### URL

> `/event/cash/earn`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| eventID | String | O | 이벤트 페이지 버튼에서 전달받은 ID |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]]<br>0 : 성공<br>970 : 에어 캐시 정합성 체크 실패<br>980 : 기지급<br>999 : 정의 되지 않은 오류 |
| result\_msg | String | 결과값에 따른 메세지 |

## 모바일 교환권 캐시 적립
> Confluence page id: 2262308611 · 최종 수정: 10월 01, 2026

### Function

> 이벤트 페이지 에어 캐시 적립

### URL

> `/event/cash/voucherExchange`

[[inavi-air-api-common#Request Header|📙Request Header]]

#### Request Parameter

| parameter | type | requisite | description |
| --- | --- | --- | --- |
| loginKey | String | O | 암호화된 로그인 키(AES-128) |
| mobileVoucherCode | String | O | 모바일 교환권 코드(16자리 난수) |

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]]<br>0 : 성공<br>970 : 에어 캐시 정합성 체크 실패<br>980 : 기지급<br>999 : 정의 되지 않은 오류 |
| result\_msg | String | 결과값에 따른 메세지 |

## 행운상자 뽑기
> Confluence page id: 2262308631 · 최종 수정: 10월 01, 2026

### Function

> 행운상자 뽑기

### URL

> `/luckyBoxOpen`

[[inavi-air-api-common#Request Header|📙Request Header]]

### Request Parameter

> 원본 표가 비어 있음 (제목만 있고 표 없음)

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| isWin | boolean | 당첨여부 |
| giftImageUrl | String | 상품 이미지 URL |
| luckyTimes | Integer | 이번이벤트 1일 응모 가능 횟수 |
| numberOfTimes | Integer | 금일 응모한 횟수 |
| isPossible | Boolean | 응모가능여부 (횟수조건, 마일리지조건 or로 하여 최종판단하여 내려줌) |
| usePoint | Integer | 1회응모에 드는 마일리지 |
| remainMileage | Integer | 응모에 사용가능 마일리지 |

## 이벤트 조회
> Confluence page id: 2262308651 · 최종 수정: 10월 01, 2026

### Function

> 이벤트 조회

### URL

> `/event`

[[inavi-air-api-common#Request Header|📙Request Header]]

### Request Parameter

> 원본 표가 비어 있음 (제목만 있고 표 없음)

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| attEvent | Object | 이벤트 |
| ┣ idx | String | 이벤트 idx |
| ┣ status | String | 사용자 상태<br>1: 응모전<br>2: 응모후<br>3: 응모중 |
| ┗ value | String | 이벤트 값 |

## 행운상자 뽑기 이력 및 쿠폰리스트 조회(보관함)
> Confluence page id: 2262308671 · 최종 수정: 10월 01, 2026

### Function

> 행운상자 기프트 리스트 조회(보관함)

### URL

> `/luckyBoxList`

[[inavi-air-api-common#Request Header|📙Request Header]]

### Request Parameter

> 원본 표가 비어 있음 (제목만 있고 표 없음)

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| giftList | Array | 상품리스트 |
| ┣ barcodeImageUrl | String | 바코드 이미지 URL |
| ┣ giftImageUrl | String | 상품 이미지 URL |
| ┣ company | String | 회사명 |
| ┣ productName | String | 상품명 |
| ┣ expireDate | String | 만료일 |
| ┣ isExpired | Boolean | 만료여부 |
| ┣ drawingDate | String | 뽑은날짜 |
| ┗ extraInfo | String | 상품명/설명/주의 등등 줄 수 있는 정보 |

## 행운상자 상품리스트 조회(Admin)
> Confluence page id: 2262308691 · 최종 수정: 10월 01, 2026

### Function

> 행운상자 상품리스트 조회(Admin)

### URL

> `/getLuckyProductList`

[[inavi-air-api-common#Request Header|📙Request Header]]

### Request Parameter

> 원본 표가 비어 있음 (제목만 있고 표 없음)

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| productList | Array | 등록가능한 상품리스트 |
| ┣ imageUrl | String | 상품이미지 URL |
| ┣ company | String | 회사이름 |
| ┣ sellPrice | String | 판매가격 |
| ┣ productName | String | 상품명 |
| ┗ usePrice | String | 소비자가격 |

## 행운상자 정보
> Confluence page id: 2262308711 · 최종 수정: 10월 01, 2026

### Function

> 행운상자 정보

### URL

> `/getLuckyBoxStatus`

[[inavi-air-api-common#Request Header|📙Request Header]]

### Request Parameter

> 원본 표가 비어 있음 (제목만 있고 표 없음)

#### Response Parameter

| parameter | type | description |
| --- | --- | --- |
| result\_code | String | [[inavi-air-api-common#결과 코드\|📙결과 코드]] |
| result\_msg | String | 결과코드에 따른 메세지 |
| luckyTimes | Integer | 이번이벤트 1일 응모 가능 횟수 |
| numberOfTimes | Integer | 금일 응모한 횟수 |
| isPossible | Boolean | 응모가능여부 (횟수조건, 마일리지조건 or로 하여 최종판단하여 내려줌) |
| usePoint | Integer | 1회응모에 드는 마일리지 |
| remainMileage | Integer | 응모에 사용가능 마일리지 |
| impossibleReason | String | 응모 불가 이유 |

## Sources

- Confluence "INAVI AIR API" > 이벤트 (2026-10-27 조회): 이벤트 (2262308561), 에어 캐시 적립 (2262308591), 모바일 교환권 캐시 적립 (2262308611), 행운상자 뽑기 (2262308631), 이벤트 조회 (2262308651), 행운상자 뽑기 이력 및 쿠폰리스트 조회(보관함) (2262308671), 행운상자 상품리스트 조회(Admin) (2262308691), 행운상자 정보 (2262308711)
