---
title: >-
    2023년 플랫폼 마감과 서버 장애 대책 (Google Play, Kakao, CDN, IDC)
category: references
tags: [platform, android, kakao, cdn, infra, visibility/internal]
aliases: [Target API 33, Kakao Legacy API 종료, CDN 장애 대책, IDC 이동설치]
relationships:
  - target: "[[inavi-2023-mail-overview]]"
    type: related_to
sources: [~/Develop/Wiki/_raw/articles/Outlook_2023.md]
summary: >-
    2023년에 일정이 정해져 있던 외부 플랫폼 변경(Google Play 대상 API 33, 카카오 Legacy API/SDK v1 종료)과 CDN 장애 이후의 통신 실패 대책, IDC 서버 이동 설치 검토를 정리했다.
provenance:
  extracted: 0.90
  inferred: 0.10
  ambiguous: 0.00
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T10:02:28+09:00
updated: 2026-10-26T10:02:28+09:00
snapshots:
  - "[[_raw/_archived/Outlook_2023|Outlook_2023]]"
---

# 2023년 플랫폼 마감과 서버 장애 대책

앱을 운영할 때 **외부에서 정해 주는 마감**과 장애 이후의 보완책이다. 에어와 Hybrid 제품군 모두에 해당한다. ([[inavi-air]], [[inavi-hybrid-navi]]) 메일 전체 지도는 [[inavi-2023-mail-overview]]다.

## 외부 플랫폼 마감

| 마감 | 내용 | 조치 |
|---|---|---|
| **Google Play 대상 API 수준** (2023-08-31) | 신규 앱과 업데이트는 **API 33** 타깃, 기존 앱은 **API 31 이상**이어야 모든 사용자에게 노출. 요청 시 **2023-11-01까지 연장** 가능. 03-22에 공지, 08-25에 "에어 앱 1개가 영향 받음" 경고 | 그룹장이 "전반적으로 확인해서 대응"하라고 지시. 에어 외 앱도 점검 대상 |
| **카카오 Legacy API 종료** (2023-11-30) | `api.kakao.com`, `p-api.kakao.com`의 `v1/users/me`, `v1/friends`를 쓰는 서비스는 **통합 SDK로 마이그레이션**. 에어(아이나비AIR)가 해당 | 티켓 생성 후 진행. **에어 외 다른 서비스도 검토** 필요 |
| **Kakao SDK v1 종료** (2023-03-31, 유예 ~11-30) | Android/iOS SDK v1은 유예 기간 후 **API 호출 실패**. v2로 마이그레이션 | 이미 조치됐을 수도 있다는 전제로 공유 |

에어의 2023년 업무 실적(5~6월)에 "Kakao API v2 마이그레이션"이 있는 것은 이 공지와 시기가 맞는다. ([[inavi-air-feature-history]]) ^[inferred] 이후 2025~2026 SDK 작업에서도 대상 API 수준과 SDK 종료 일정은 반복해서 확인해야 한다. ^[inferred] ([[orbis-sdk]])

## CDN 장애와 서버 장애 대책 (2023-08)

KG모빌리티 지도 업데이트 장애(CDN으로 파일을 받지 못한 이슈)를 계기로 앱과 Agent의 보완 개발 일정을 수립했다. (NHN Cloud 장애와는 별개 이슈)

| 항목 | 내용 |
|---|---|
| 초기 지도 다운로드 | 명령어 **POST → GET 변경**. 리눅스, Android 내비 개발 일정 수립. MR 일정과 U100 타깃 일정에 맞춰 배포 |
| CDN 연동 불가 시 | **비통신 모드 전환**(리커버리). 통신 인터페이스 체크만이 아니라 CDN을 거치는 파일 다운로드(탐색 파일, 지도 데이터)의 연동과 유효성 체크로 모드 전환 검토. 초기 다운로드뿐 아니라 **특정 API가 반복 실패해도** 전환 검토(대상 API 정리 필요) |
| 실패 전달 | CDN 서버를 쓰는 API가 실패하면 **앱이 Agent에 전달**하는 로직. CDN뿐 아니라 특정 API의 실패도 포함(항목 선정 필요) |
| 모니터링 | 제안된 방안 외에 **Health Check**로 볼 수 있어 운영팀의 CDN 모니터링으로 커버하거나, 차량 상태 추이를 볼 수 있는 HC 로그 전송 방안 검토 |
| 공지 | 통신형 지도 오픈 시 KG모빌리티에 공지, 통신형 지도 계획서 작성 |

## IDC 서버 이동 설치 (2023-09)

IDC 운영 중 **전력 분산** 때문에 일부 서버를 다른 랙으로 옮겨 설치해야 한다는 요청. 대상은 TconDB, AuthDB 4대 중 2대, 작업은 10월 평일 야간, 다운타임 10분. 개발 쪽 의견: **DB 서버는 영향도가 크므로 가급적 제외**하고, 꼭 필요하면 TconDB 1·2를 대상으로 한다. 같은 해 1월과 2월 판교 오피스 방화벽, 백본 스위치 PM 작업 공지, 5월 IDC 방화벽 정책 사용 확인 요청도 있었다.

## 관련 모니터링

운영팀이 사용 중인 모니터링 서비스(자빅스, 데이터독) 고도화를 위해 개발자 의견을 수렴했다(05-31). CI/CD와 성능 개선(사용 빈도에 따른 API 성능, 데드코드 탐지 같은 지표) 요구를 받는 설문이었다.

## Sources

- [[_raw/_archived/Outlook_2023.md]] — 2023 업무 메일
