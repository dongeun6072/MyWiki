---
title: >-
    대만향 Orbis NaviSDK 개발 메일 (2026): 경로 서버 v1.7~v2.31, 맵매칭, Horizon 서버
category: references
project: orbis-sdk
tags: [orbis-sdk, taiwan, route-server, map-matching, visibility/internal]
aliases: [대만 경로 서버 2026, Route Server v2, Mobility Horizon Server, 맵매칭 라이브러리 0.6.5]
relationships:
  - target: "[[orbis-navisdk-development-2025]]"
    type: extends
  - target: "[[taiwan-routeserver-api]]"
    type: related_to
  - target: "[[vehicle-restriction-routing]]"
    type: related_to
  - target: "[[inavi-2026-mail-overview]]"
    type: derived_from
sources: [~/Develop/Wiki/_raw/articles/Outlook_2026.md]
summary: >-
    2026년 대만향 경로 서버 릴리즈(v1.7~v2.31: 포트 분기, 트럭 제원·위험물, 경유지 모드), Mobility Horizon Server v0.1, Route Data Library와 맵매칭 라이브러리 버전, Admin 통계 요청을 정리했다.
provenance:
  extracted: 0.85
  inferred: 0.13
  ambiguous: 0.02
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T15:12:00+09:00
updated: 2026-10-26T15:12:00+09:00
snapshots:
  - "[[_raw/_archived/Outlook_2026|Outlook_2026]]"
---

# 대만향 Orbis NaviSDK 개발 메일 (2026)

2025년 흐름은 [[orbis-navisdk-development-2025]]에 있다. 경로탐색 엔진은 자율주행기술부문 경로기술개발팀이 릴리즈하고, 맵매칭 라이브러리는 선행기술Lab이 배포한다. 서버 주소(IP·포트 연결 정보)는 원본에 있으나 옮기지 않았다. API 경로와 파라미터는 [[taiwan-routeserver-api]]가 다룬다.

## 경로 서버 릴리즈 (INAVI Route Server for Taiwan)

| 버전 | 날짜 | 주요 변경 |
|---|---|---|
| v1.7 | 01-07 전달(원 릴리즈 2025-10-24) | 출발지·목적지 근처에 도로가 없어 탐색이 실패하던 문제 개선 |
| v1.9 | 01-22 | 오토바이·이륜차 전용 도로 회피. 서비스 데이터 대만 v25270, 한국 v25292. 한국 실차 테스트용 Korea 엔진 v0.8에도 적용 |
| v2.0 | 03-05 | **포트 분기 서비스**: 엔진·데이터·라이브러리 버전별로 포트를 나눠 서비스(17931은 v1.9·데이터 25270·라이브러리 1.0.1.3, 17932는 v2.0·데이터 25271·라이브러리 1.0.1.4). **트럭 제원 옵션** `weight`, `height`, `length` 추가. 한국 실차 테스트용 Korea 엔진은 종료. 서버 증설 없이 포트를 나눠 초당 처리 성능이 낮아질 수 있다는 주의가 붙었다 |
| v2.1 | 05-19 | 탐색 API에 전폭 `width`, 위험물 운송 제한 도로 회피 `hazmat` 추가(다중 경로 탐색 `searchroutemulti`에도 동일 적용). 트럭 전용 경로 탐색 기능 |
| v2.2 | 06-19 | 본문 없음 |
| 데이터 v26220 | 06-24 | 본문 없음 |
| v2.3 | 07-21 | **경유지 모드 `waypointroutingmode`**(기본 1). 0 = 법규 우선(일방통행 역주행 제한, 위반 시 탐색 실패, 결과 코드 23), 1 = 경로 유형 유지(필요 시 역주행·우회 허용, 상세 코드 20). 실패 시 고유 코드 반환 개선. 17931은 엔진 2.3·데이터 26220·라이브러리 1.0.1.6 |
| v2.31 | 08-14 | 교통정보 연동 서버 수정 |

- 포트 분기의 운영 의미: 신규 지도·엔진은 새 포트에서 검증한 뒤 SDK 사용 업체에 새 SDK 버전(v1.0.2 등)으로 올리도록 공지하고, 이후 기존 포트에 신규 지도를 적용하는 순서로 진행한다(04-17 메일). Agent 로그상 17931 포트에도 구버전 호출이 들어와 순서를 정했다. ^[inferred]
- 트럭 제원·위험물 옵션은 [[vehicle-restriction-routing]]의 제한 도로 회피와 이어진다.

## Mobility Horizon Server for Taiwan v0.1 (01-15)

이동체 기반 계획·예측 탐색 엔진의 최초 릴리즈. TomTom Orbis Maps 대만 도로망을 쓴다.

- **e-Horizon API** `/searchhorizon`: 차량 경로 예측 데이터 전달
- **Route Range API** `/searchrange`: 차량 주행 가능 범위 산출

## Orbis Route Data Library

외부 엔진이 경로 탐색 서비스 데이터를 쓰기 위한 라이브러리. 서비스 데이터는 경로 서버 릴리즈와 같은 파일로 함께 전달한다(대용량 첨부, 다운로드 기한 1주).

| 버전 | 날짜 | 내용 |
|---|---|---|
| v1.0.1.3 | 01-22 | 신규 지도 버전 발행에 따라 CDN 업데이트 요청 |
| v1.0.1.4 | 03-24 | 테스트 결과 이상 없음, 정식 배포 요청 |
| v1.0.1.5 | 03-25 | `GetDataLinkNearPt`, `GetDataNodeNearPt` 응답 속도 개선(좌표에서 가장 가까운 링크·노드 조회). 서비스 데이터 v25271 |
| v1.0.1.6 | 04-17 | 포트별 앱 버전 정리(위 포트 분기 참고) |

## 맵매칭 라이브러리 (OrbisMap)

| 버전 | 날짜 | 내용 |
|---|---|---|
| iOS 0.6.3.101 | 2025-12 | 위치 정보 callback용 Listener(`setMapMatchListener`, `OnMatchInfoUpdated`, `OnGPSInfoUpdated`) 추가. AOS와 같이 업데이트 주기를 Listener로 받게 해 달라는 요청에서 시작 |
| iOS 0.6.3.102 | 01-06 | `allowsBackgroundLocationUpdates` 미설정으로 백그라운드에서 위치 갱신이 안 되던 문제 수정 |
| Android 0.6.3 | 02-03 | 배포 |
| Android 0.6.5.101, iOS 0.6.5.103 | 03-03 | Route Data Lib v1.0.1.4 적용 |
| Android 0.6.6.101, iOS 0.6.6.103 | 05-15 | Route Data Lib v1.0.1.6 적용 |
| 에어용 단일 링크 모의주행 수정 | 01-30 | NDK 설정 오류로 16KB 페이지 대응 빌드가 빠져 재배포. 배포 전 16KB 대응 여부를 확인하기로 함 |

- 05-26 iOS xcframework 요청: 시뮬레이터 슬라이스에 `x86_64`를 추가(`-arch arm64 -arch x86_64`)해 xcframework 배포 형식에 맞춰 달라는 요청.

## SDK 운영·사업

- **Admin 통계 요청(03-04)**: 대만 사업 파트너와 계약이 완료되어 Admin 페이지에 월간·AppKey별 **API 호출수(아이나비 API와 TomTom API 구분)**, **SDK 사용자수(AOS·iOS 구분)** 통계가 필요하다. TomTom과의 비용 정산이 호출수와 사용자수 기준이라 3월 안에 마무리해야 했다.
- **웹지도(05-18, 05-21)**: 대만향 웹 지도를 검토해 배경·주기 색은 1차 결과를 유지하고, POI가 주·야간 단일 데이터라 야간 지도에서 균형이 맞지 않아 야간용 POI 데이터를 따로 두기로 했다. 글로벌 Maps 개발 사이트에 웹지도 개발 가이드가 추가되어 Map SDK에 수정이 필요한지 확인하는 요청이 있었다. 05-27에는 Orbis SDK 가이드 html 샘플이 전달됐다.
- **EC912 테스트 단말(07-21)**: 해외사업팀이 대만 EC912 단말용 Navi SDK Demo App 포팅 검토를 요청했다.
- **HUD 연동(05-19)**: 중국 업체의 신규 HUD 개발 검토를 위해 연동 규격(프로토콜) 문서를 전달했다. 5~6월 초 프로토콜 검토, 문제없으면 6월 중순~7월 초 계약 추진 예정이었다. → [[air-operations-2025]]의 HUD 외부포팅과 같은 계열 ^[inferred]
- **TomTom 도구 접근**: 맵 편집 샌드박스, Artifactory 접근 만료(10-12 종료) 메일이 있었다. 계정 정보는 옮기지 않았다.

## Open Questions

- v2.2와 데이터 v26220의 변경 내용은 본문이 없다.
- Admin 통계 개발의 완료 여부는 메일에 없다.

## Sources

- [[_raw/_archived/Outlook_2026.md]] — 2026 업무 메일 (경로 서버 주소·연결 정보는 원본에만 있고 가렸다)
