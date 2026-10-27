---
title: >-
    Orbis NaviSDK 사업·법무 검토 (2025): TomTom 파트너십, 특허, 현지 업체, 싱가포르 서버
category: references
project: orbis-sdk
tags: [orbis-sdk, tomtom-orbis, taiwan, legal, partnership, visibility/internal]
aliases: [대만향 NaviSDK 사업, TomTom Solution Provider, FTO 특허 검토, Hetone, 싱가포르 리전]
relationships:
  - target: "[[orbis-navisdk-development-2025]]"
    type: related_to
  - target: "[[orbis-navisdk-poc-prep-2025]]"
    type: related_to
  - target: "[[inavi-2025-mail-overview]]"
    type: derived_from
sources: [~/Develop/Wiki/_raw/articles/Outlook_2025.md]
summary: >-
    2025년 대만향 NaviSDK의 비개발 이슈: TomTom 파트너십 계약 범위, 특허 침해(FTO) 검토 결과, 현지 POI·고객 협의, 라이선스·오픈소스 고지, 싱가포르 서버의 개인정보 규제 검토.
provenance:
  extracted: 0.75
  inferred: 0.22
  ambiguous: 0.03
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T11:12:00+09:00
updated: 2026-10-26T14:30:00+09:00
snapshots:
  - "[[_raw/_archived/Outlook_2025|Outlook_2025]]"
---

# Orbis NaviSDK 사업·법무 검토 (2025)

개발 흐름은 [[orbis-navisdk-development-2025]]에 있다. 이 페이지는 같은 해 전략팀·해외사업팀·법무지재팀이 개발팀에 확인을 요청한 항목이다. 메일 일부는 **대외비**로 표시돼 있어 수치와 상대 이름은 적지 않았다. **인증·키 전달 방식은 뺐다.**

## TomTom Solution Provider 파트너십 (03-27)

계약 직전에 개발팀이 필요한 항목이 빠졌는지 확인한 메일이다.

- 라이선스 제품: **Orbis 지도 데이터**(전 세계 81개 지역, 전체 지도 PBF 포맷), 표준·강화 디스플레이, 지오코딩, 4륜·트럭 경로 탐색, 내비게이션, 표지판·안전 경고, 도로 위험 지수 등. 지도 갱신 주기는 표에 weekly, 설명란에 quarterly로 달라 TomTom 법무가 **weekly로 정정**했다.
- 실시간 서비스: 날씨, 교통 흐름, 교통 사고 피드(OpenLR/OSM ID 기반).
- 개발팀이 계약서에서 **빠진 API**로 짚은 것은 과속 카메라, Hazard Warning 등이다. 개발 측은 Maps SDK의 MapDisplay, Location, Search, Routing 네 모듈의 이용 가능 여부 확인을 요청했다.
- Hazard Warning End User 서비스(07-03)는 테스트 환경과 운영 환경이 달라 운영 환경에서 시험하라는 안내를 받았다.

## 특허 침해(FTO) 검토 (08-07)

- 수행: 외부 특허법인, 2025-04-22 ~ 7월 말. 범위는 대만향 NaviSDK 서비스. 초안 → 내부 엔지니어 사실관계 확인 → 법인 미팅 → 최종 보고 순서.
- 결과: **침해 우려 특허 2건**(대만 특허). 대응 방안은 별첨으로 정리됐다.
  - 한 건은 시간 정보 수신·이벤트 검색 모듈을 구성에 두지 않아 **비침해**로 대응하고, 선행 사례로 무효 자료 제출도 가능하다.
  - 다른 한 건은 차량 탑재 장치 전제인데 자사는 **차량 외부 단말 기반 플랫폼**이고, 탐색은 Dijkstra 전파에 A*의 목적지 가중치를 결합한 복합 알고리즘이라 비침해로 대응한다. 권리자가 학교이고 분쟁 이력이 없어 가능성은 낮게 본다.

세부 구성(핵심 34건, 검토 17건, 대응 논리 표)은 [[taiwan-navisdk-fto-patent-review-2025]]에 있다.

## 현지 파트너와 고객

- **POI**(06-27): ITS 총회에서 TomTom 소개로 만난 대만 TMS가 로컬 POI 카탈로그를 보냈다(비밀유지협약 하에 수령). 범위·품질·갱신 주기는 추가 수령 예정이고 주간 회의에서 도입 여부를 검토한다.
- **Hetone Green Energy**(10-30, 11-07, 12-08): EV 충전 인프라·운영 플랫폼 업체. 전시회에서 만나 NaviSDK 시범 시험을 요청했다. NDA와 EA 계약을 먼저 안내했으나 상대가 빨리 시험하길 원했다. 법무 의견은 EA 계약서의 비밀유지조항(3.3)이 있어 **별도 NDA 없이 EA만으로 가능**이다. 시험 앱은 **사용 기한을 건 샘플/디버그 앱**으로 제공했고, 11-07 디버그 앱은 사용 기한 11-30, MMC 0.6.0-debug, 앱 시작 시 NMEA 로그 저장을 넣었다. 12-08에는 EA 체결 보도자료 초안 검토 요청이 왔다. 유사 논의 업체로 USPACE가 같이 나온다.
- **12-10 진행 상황 보고**(대외비): 대만 업체 관계 정리, 추가 접촉 중인 업체(주차 관련), TomTom의 **Solera 건**, **호주·뉴질랜드 건**, TomTom과 협의 중인 **오프라인 지도와 지역 확대**로 구성됐다. ^[inferred] 대만 외 시장으로 넓히려는 구상으로 읽힌다.

## 라이선스와 오픈소스 고지 (11-18)

- Orbis Navigation SDK 라이선스는 Maps SDK와 같은 **Apache 2.0**으로 적고 MapLibre 등 오픈소스 내용을 추가했다.
- 상용화 이슈는 크게 없고 저작권·면책 고지만 지키면 된다는 정리다. 에어, iMPS Map SDK, 스탬프 앱 등이 이미 '오픈소스 라이선스' 메뉴로 고지하고 있어 같은 수준으로 준비한다. 해외 지도 플랫폼 상품은 MapLibre GL Native → flutter-maplibre-gl 순서로 검토한다. → [[orbis-sdk]]

## 싱가포르 리전 서버 (11-26)

탐색·CDN·DB 서버를 AWS 등으로 **싱가포르 리전**에 두고 한국에서 운영하며 대만 사용자에게 서비스하는 구조의 법무 검토다.

| 지역 | 요지 |
|---|---|
| 한국 | 해외 이용자 정보도 국내에서 처리·접근하면 개인정보보호법·정보통신망법 대상이 될 수 있다. 위치정보가 민감하므로 최소 수집 |
| 싱가포르 | 합리적 보호조치 요구. 클라우드 사업자와의 처리 계약, 국제 전송 요건 점검 |
| 대만 | PDPA 준수. 국외 이전 명시 동의까지는 불필요하다고 봤다 |

권고 조치: ① 데이터 **마스킹·익명화** ② 접근통제와 권한 관리 강화 ③ 접근 로그를 위변조 방지 저장소에 **1년 이상** 보관.

## Open Questions

- 계약 체결일과 EA 이후 상용 계약 조건은 메일에 없다.
- 특허 대응 방안 별첨의 상세는 첨부 문서라 위키에 없다.

## Sources

- [[_raw/_archived/Outlook_2025.md]] — 2025 업무 메일
