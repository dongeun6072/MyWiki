---
title: >-
    OrbisMap NaviSDK 검토 및 사전 준비 (2025 PoC)
category: references
project: orbis-sdk
tags: [orbis-sdk, tomtom, poc, taiwan, visibility/internal]
aliases: [OrbisMap NaviSDK 검토, NSDK PoC 사전 준비, TomTom 연동 검토]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[orbis-routing-stack]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/670433348/OrbisMap+NaviSDK
source_url: https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/670433348/OrbisMap+NaviSDK
summary: >-
    2025년 해외향 Navi SDK PoC 전에 정리한 Confluence 페이지. TomTom 교통·과속카메라·Hazard 연동, 지도 컨버팅 흐름, 대만 지도의 안내 데이터 유무 검토, PoC 범위 합의를 담았다.
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T11:00:00+09:00
updated: 2026-10-26T11:00:00+09:00
stub: false
---

# OrbisMap NaviSDK 검토 및 사전 준비 (2025 PoC)

아이나비 에어 & NSDK 스페이스의 Confluence 페이지(원제 "OrbisMap NaviSDK 검토 및 사전 준비", 최종 수정 2025-05-14)다. 개발 담당자 4명이 편집 권한을 갖고, 2025-03~04 항목이 날짜순으로 쌓여 있다. 이 시기는 [[orbis-sdk]]의 해외향 Navi SDK 개발 초반(2025-01~10)에 해당한다. **이 페이지에는 테스트 서비스, JFrog, TomTom 개발자 계정의 ID/PW와 API 키 앞자리가 평문으로 적혀 있다. 위키에는 옮기지 않았다.**

## PoC 범위 합의

- 지도는 처음에 **전체 지도를 한 번에 내려받는 방식**으로 간다. PoC 이후 스트리밍 방식을 검토한다.
- 기능 흐름은 검색 → 탐색 → 경로 선택 → 주행 화면(모의주행 포함). 주행 컴포넌트는 TBT, 과속단속 심볼, ETA다.
- **Android만 지원**한다. TomTom API 비통신형은 제외한다.
- Agent 서버는 PoC 동안 두지 않는 것으로 잠정 합의했고, 이후 바뀔 수 있다.
- TTS는 PoC 동안 기기 내장 TTS를 쓴다(삼성 Android 중심). 중국산 Android 폰까지 지원해야 하면 Google Cloud TTS를 검토한다. 언어는 영어, 중국어(간체/번체), 한국어다.
- 안내 요소: TBT(차기·차차기·차로 정보, 회전 코드·거리·방면·휴게소), 목적지 남은 시간·거리, 과속카메라. 신호단속 카메라와 방지턱은 취소선 처리되어 PoC에서 빠진 것으로 보인다. ^[inferred]

## TomTom 연동

| 항목 | 내용 |
|---|---|
| 교통정보 | CES 시연에서는 임시 URL을 받아 처리했다. 정식으로는 TomTom **Intermediate Traffic API**를 쓴다: Traffic Flow는 Protobuf, Traffic Incidents는 DATEX II |
| 과속카메라 | **Safety Camera Alerts** API로 데이터를 받는다. 전용 API 키를 개발자 계정에 추가해 두었다 |
| Hazard Warning | **Hazard Warnings Intermediate B2B**용 키가 발급됐다. 전달 방식은 Kafka(서버 간)와 MQTT(서버→단말) 중 정해야 한다 |
| Live Speed Restrictions | 피드 링크는 SSL 인증서가 있는 주소에서만 접근되고, 계약 기간에만 쓸 수 있다. **홍콩과 대만은 지원하지 않고 일본만 제공**돼서, 사양 검증은 일본 데이터로 한다 |
| Maps SDK, Search API | 개발자 계정의 기본 API 키로 호출한다(검색, 경로, 지도 표시). 교통정보는 CES 때 쓴 키를 그대로 쓴다 |

TomTom 개발자 사이트의 일부 문서는 로그인한 상태와 쿠키 허용이 필요하다. Chrome에서 안 열려 Safari로 접속했고, Chrome 쿠키를 초기화한 뒤 정상 접속을 확인했다고 적혀 있다.

SDK가 호출하는 TomTom 프록시는 [[orbismap-api-docs]]에 있다.

## 지도 컨버팅과 데이터 흐름

- 지도기술개발팀이 TomTom 원도(pbf)를 shape으로 바꾸고, 경로기술개발팀이 shape을 탐색용 binary DB로 바꾼다. binary Reader(라이브러리와 가이드)가 제공되고, MMC가 쓴다.
- 탐색용 binary는 서버에 둔다. MMC, 안내, 메인은 **로컬 지도**가 필요하다. 과속카메라, 신호단속 카메라, 방지턱은 컨버팅과 DB 포맷을 따로 협의해야 한다.
- 전체 구조는 [[orbis-routing-stack]], 도로 데이터 라이브러리는 [[orbis-route-data-lib]]에 있다.

## 대만 지도의 안내 데이터 유무 검토 (지도 데이터 담당과 함께)

원도에 데이터는 일부 있지만 `supported=no` 플래그가 붙어 있고, 모든 데이터의 라이선스가 ODbL이다. TomTom이 검증하지 않은 데이터라 미지원으로 둔 것으로 보이며, 실제로 쓸 수 있는지는 TomTom에 문의해야 한다. ^[inferred]

| 종류 | 있는 것 | 판단 |
|---|---|---|
| 과속카메라 | Point 872개(대부분 위치만 있고 각도·제한 속도 없음), 관계 정보 107개(최고속도 95, 평균속도 12) | 관계 정보는 From/To 지점과 제한 속도가 있어 쓸 만하고, Point는 쓰기 곤란 |
| 신호단속 카메라 | 관계 정보 9개 | |
| 방범카메라 | Point 190개, 각도 대부분 없음 | |
| 방지턱 | Point 213개(각도 없음), 링크 속성 819개 | |
| 트럭 속성 | 높이 제한 2,325, 중량 제한 286, 차폭 제한 15(링크 속성) | → [[vehicle-restriction-routing]] |
| 도로 표지판 | 없음 | |

## 그 밖의 항목

- 대만향 **경로탐색 비교 서비스**(아이나비 vs 구글)의 프런트 페이지를 만들어 두었다. 접속 정보는 옮기지 않았다.
- 이슈 체크리스트는 별도 스프레드시트에 있다(시트 권한 필요).
- 지도 데이터 전달·컨버팅 데이터 흐름도는 외부 공유 문서로 연결되어 있다. 링크는 옮기지 않았다.
- NSDK 의존성 저장소(JFrog)의 관리자 계정이 적혀 있다. 값은 옮기지 않았다.

## Open Questions

- 교통정보 임시 URL에서 정식 Intermediate Traffic API 키로 언제 넘어갔는지는 이 페이지에 없다.
- Hazard Warning 전달 방식(Kafka vs MQTT)의 결정 결과는 이 페이지에 없다.
- 평문으로 적힌 계정 정보는 Confluence 원본에서 정리가 필요해 보인다. 접근 권한이 있는 팀 안에서만 보이는 페이지인지 확인이 필요하다. ^[inferred]

## Related

- [[orbis-sdk]] — 프로젝트 개요
- [[orbis-routing-stack]], [[orbismap-api-docs]], [[taiwan-routeserver-api]]

## Sources

- [OrbisMap NaviSDK 검토 및 사전 준비 (Confluence)](https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/670433348/OrbisMap+NaviSDK) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
