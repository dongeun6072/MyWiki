---
title: >-
    OrbisMap NaviSDK 개발 사양과 검토 및 사전 준비 (PoC)
category: references
project: orbis-sdk
tags: [orbismap, navisdk, poc, tomtom, map-mode, visibility/internal]
aliases: [OrbisMap NaviSDK 개발 사양, OrbisMap NaviSDK 검토 및 사전 준비, OrbisMap NaviSDK]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1105690655
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/670433348
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/735674369
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/618102815
summary: >-
    지도 모드(2D 고정/회전/3D) 줌·틸트 수치와 자동 줌 레벨 규칙, PoC 사전 준비(교통정보·안전카메라·TTS·지도 컨버팅·TomTom 지도 데이터 카메라/제한 현황) 전체
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

# OrbisMap NaviSDK 개발 사양과 검토 및 사전 준비

OrbisMap NaviSDK의 지도 모드 사양(2025-09-15)과, PoC 시작 전 TomTom 데이터·서버·지도 컨버팅을 점검한 "검토 및 사전 준비" 페이지(2025-05-14)를 합쳤다. 요약은 [[orbis-navisdk-poc-prep-2025]], 구글 지도 레벨 분석은 [[google-navigation-guidance-and-map-level-analysis]], 목차는 [[orbis-design-and-review-hub]].

## OrbisMap NaviSDK 개발 사양 (2025-09-15)

### 지도 모드

| 모드 | zoom level | tilt |
|---|---|---|
| 2D 고정 | 15.3 | 0 |
| 2D 회전 | 15.8 | 0 |
| 3D 외전(원문 표기, 3D 회전으로 읽힘 ^[ambiguous]) | 16.5 | 30 |

### 자동 줌 레벨
- 조건: 일정 속도를 3초간 유지하면 레벨을 조정한다.
- 수치

| 속도 | 줌 레벨 |
|---|---|
| 40 미만 | 16.5 |
| 60 미만 | 16.2 |
| 80 미만 | 15.7 |
| 그 외 | 15.5 |

속도 단위는 원문에 없다(km/h로 추정). ^[inferred]

## OrbisMap NaviSDK 검토 및 사전 준비 (2025-05-14)

원문에는 문서 편집 권한자 목록, 대만향 경로탐색 비교 서비스(아이나비 vs 구글) 프론트 페이지의 접속 주소와 테스트 계정, JFrog Admin 계정, TomTom Developer 계정(ID/비밀번호), API 키 앞자리, 개발자 계정 메일이 적혀 있다. 모두 미수록이다.

### 준비 항목 개요
- 대만향 경로탐색 비교 서비스 프론트 페이지 구성(링크·계정 미수록)
- 이슈 체크리스트(시트, 권한 필요, 링크 생략)
- 지도 데이터 전달 및 컨버팅: 데이터 흐름도 링크가 있다(링크 생략).

### HazardWarning TomTom Guide
- TomTom으로부터 메일을 받았다. 내용: Connected Services 플랫폼과 **Hazard Warnings Intermediate B2B**에 대한 접근이 개발자 계정에 연결된 API 키로 열렸다. 애플리케이션 이름은 **Hazard Warnings Intermediate B2B**. 허용된 consumer group은 회사 전용 접두어로 시작하는 consumer group(접두어 미수록). 허용 topic 확인 방법은 첨부 `ConnectedServicesPlatformGuide.pdf` 2.3절에 있다. (계정, 키 앞자리, 그룹 접두 이하 값은 미수록)

### Agent 서버
- PoC 기간에는 Agent 없이 진행하는 것으로 잠정 협의했다. 이후 상황에 따라 변경될 수 있다.

### 교통정보 사용 URL
- Orbis Map SDK를 위해 TomTom으로부터 전달받은 URL 문서가 있다(링크 생략).

### API 사용 확인
- Maps SDK / Search API는 "My First API Key"를 사용한다. Maps SDK 내에서 API(검색, 경로, 지도 표시 등)를 실행할 때 API 키가 필요하며 MyFirst API Key를 쓴다.
- 교통정보는 CES에서 사용한 Key를 그대로 쓴다. (키 값 미수록)

### 교통정보 검토
- CES 때 시연을 위해 임시 URL을 받아 처리했다.
  - trafficflow, incidents 각각 임시 URL(링크 생략)
- TomTom 개발자 사이트 확인 결과 Traffic APIs > Intermediate Traffic API를 사용하면 되는 것으로 확인했다.
  - Traffic Flow — Protobuf
  - Traffic Incidents — DATEX II

### Safety Camera Alerts (Speed Camera)
- 관련 문서 링크가 있다(링크 생략). TomTom Developer 사이트에 로그인한 상태로 접속해야 하며 쿠키를 허용해야 한다. 일부 환경에서 Chrome 접속이 안 되어 Safari로 접속했고, Chrome 쿠키를 초기화한 뒤 정상 접속을 확인했다.

### 안내 데이터 (PoC에는 SpeedCamera만 지원하는 것으로 협의 중)
- **SpeedCamera**: TomTom API로 데이터를 수신한다. 개발자 계정에 Speed Camera용 API 키 추가를 완료했다.
- **Hazard Warning**: Kafka 프로토콜(Server to Server)과 MQTT(Server to Device) 중 결정이 필요하다. Hazard 문서가 있다.
- **Live Speed Restrictions**
  - 첨부 Excel 파일에서 해당 피드 접근 링크를 확인할 수 있다.
  - 제공된 링크는 SSL 인증서가 있는 주소에서만 접근할 수 있으며 TomTom과의 계약 기간 동안만 이용할 수 있다.
  - 피드의 인터페이스 설명과 기술 배경 정보는 별도 문서에 있다(링크 생략).
  - 단, 홍콩과 대만은 지원하지 않고 일본에 한해 제공된다(사양 검증은 일본 데이터로 진행할 수 있다고 함).

### TTS
- PoC 기간에는 기본 내장 TTS를 사용한다(삼성 안드로이드 지원에 집중).
- 이후 중국산 Android 폰까지 지원이 필요하면 구글 Cloud TTS를 검토·적용한다.
- 언어: 영어, 중국어(간체/번체), 한국어

### 지도 컨버팅
- 지도기술개발팀: pbf(TomTom 원도) → shape
- 경로기술개발팀: shape → binary(경로탐색에 사용하는 DB)
  - binary Reader(Lib 및 가이드)를 제공하며 MMC에서 사용한다.

### 지도
- 탐색에서 사용하는 binary는 서버에 구성한다.
- MMC, 안내, 메인이 사용하려면 로컬 지도가 필요하다.
  - 컨버팅 대상: 과속카메라, 신호단속카메라, 방지턱 — 컨버팅 및 DB 포맷 협의 필요
  - 다운로드 방식: PoC에는 초기 전체 다운로드 방식, 실제 서비스 적용 시에는 스트리밍 방식을 적용해야 한다.

### 안내 요소
- TBT(차기, 차차기, 차로정보) → 회전코드, 거리, 방면정보, 휴게소 정보(휴게소인 경우)
- 목적지 정보 → 남은 시간, 남은 거리
- 과속카메라(~~신호단속 카메라?, 방지턱?~~ — 원문에서 취소선 처리)

### 과속카메라 정보 존재 유무 검토
지도 담당자와 함께 검토한 내용이다.
- 데이터는 일부 존재하나 지원하지 않음(supported=no) flag가 설정되어 있어 실제로 사용할 수 있는지 TomTom에 문의가 필요하다.
- 모든 데이터의 License가 "ODbL"로 지정된 것으로 보아, TomTom 측에서 검증되지 않은 데이터라서 지원하지 않음으로 설정한 것으로 보인다.

| # | 항목 | 현황 |
|---|---|---|
| 1 | 과속 카메라 | Point 형상 872개, 관계 정보 107개(최고속도 95, 평균속도 12). Point 형상은 대다수가 위치 정보만 있고 각도/속도 제한 값이 없어 사용이 곤란할 것으로 예상. 관계 정보는 대부분 From, To Point와 속도 제한 값을 가진다. |
| 2 | 신호단속 카메라 | 관계 정보로 9개 |
| 3 | 방범카메라 | Point 형상 190개, 각도 값이 대부분 없음 |
| 4 | 방지턱 | Point 형상 213개(각도 값 없음), 링크 속성 819개 |
| 5 | 트럭 관련 속성(중량, 높이, 차폭) | 링크 속성. 높이제한 2,325, 중량제한 286, 차폭제한 15 |
| 6 | 도로 표지판 | 정보 없음 |

### PoC 초기 협의 항목
- 초기에는 Full 지도 방식(메인 쪽에서 초기에 전체 데이터를 다운로드)으로 검토한다. PoC 이후 스트리밍을 검토한다.
- 검색 > 탐색 > 경로선택 > 주행화면(+모의주행) 구현
  - 주행 컴포넌트: TBT + 과속단속 심볼 + ETA
- Android만 지원
- TomTom API 비통신형 제외

## 하위/관련 빈 페이지
- "OrbisMap NaviSDK" (pageId 735674369, 2025-05-23 수정) — 제목만 있는 상위 페이지
- "NaviSDK/Maps API Key" (pageId 618102815, 2024-11-22 수정) — 본문 없음(키 관련 페이지로 값은 어차피 미수록)

## Related
- [[orbis-navisdk-poc-prep-2025]] — 요약
- [[google-navigation-guidance-and-map-level-analysis]] — 구글 지도 레벨 분석
- [[tomtom-maps-sdk-api-review-detail]] — TomTom Maps SDK API 검토
- [[orbis-routing-stack]] — 경로 스택
- [[orbis-sdk]]

## Sources
- Confluence "OrbisMap NaviSDK 개발 사양" (pageId 1105690655) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "OrbisMap NaviSDK 검토 및 사전 준비" (pageId 670433348) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "OrbisMap NaviSDK" (pageId 735674369) — 본문 없음
- Confluence "NaviSDK/Maps API Key" (pageId 618102815) — 본문 없음
