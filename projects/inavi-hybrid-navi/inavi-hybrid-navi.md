---
title: >-
    아이나비 하이브리드 내비 (Where / 3D Streaming 외부포팅 / MXI)
category: project
tags: [hybrid-navi, where, mxi, external-porting, visibility/internal]
aliases: [Hybrid 내비, inavi WHERE, 아이나비 3D Streaming, AOS 외부포팅, 포팅내비, MXI]
relationships:
  - target: "[[이동은]]"
    type: related_to
sources: [~/Develop/Wiki/_raw/articles/Outlook_2022.md]
summary: >-
    2022년 모빌리티Tech그룹이 외부 단말(MXI, 아트뷰 M2C, 유브릿지 IAN-10)에 공급한 하이브리드 내비 제품군의 구성, 엔진 구조, 고객·단말, 배포 방식을 2022년 업무 메일로 정리했다.
provenance:
  extracted: 0.75
  inferred: 0.25
  ambiguous: 0.00
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T09:40:56+09:00
updated: 2026-10-26T09:40:56+09:00
snapshots:
  - "[[_raw/_archived/Outlook_2022|Outlook_2022]]"
  - "[[_raw/_archived/Outlook_2023|Outlook_2023]]"
---

# 아이나비 하이브리드 내비 (Where / 3D Streaming 외부포팅 / MXI)

2022년 모빌리티Tech그룹이 **외부 업체의 단말에 아이나비 내비 앱을 공급**하던 제품군이다. 같은 앱이 이름만 다르게 불렸다: 하이브리드 내비, `inavi WHERE`(MXI), `아이나비 3D Streaming`(아트뷰, 유브릿지 포팅), 포팅내비. 통신이 되면 서버 경로를 쓰고 안 되면 단말 안의 경로·검색·지도 데이터로 동작하는 **하이브리드(통신형 + 비통신형)** 구조다. ^[inferred] 2022년 업무 메일([[inavi-2022-mail-overview]]) 중 이 제품군 이야기가 가장 많다. [[이동은]]은 2022년 AOS 외부포팅(MXI, 아트뷰) 유지보수를 맡았다. ([[job-description-2023-2026]])

## 고객과 단말

| 구분 | 내용 |
|---|---|
| **MXI** | 팅크웨어가 만든 단말. **서울시설공단(서울 장애인 콜택시)** 에 납품되어 콜앱과 내비(Where)가 함께 돌아간다. 순천, 경주, 하남 등 지방 납품 건도 있다. 서비스는 아이나비모빌리티와 팅크웨어 필드이슈관리팀이 현장 대응을 한다. |
| **아트뷰** | 외부 포팅 단말 `M2C-D110i`, `M2C-200i`(2종, OTA 2022-05-25), `M2C-T9100`(GPS 칩셋 수급 이슈) |
| **유브릿지 IAN-10** | 아이나비 3D Streaming 신규 포팅 (V1.2.5~1.2.7, TBT 미지원) |
| 그 밖에 | `J100`, 쌍용 `Y450`(전화번호 검색 VOC) 등 비통신 검색 엔진을 쓰는 단말 |

서울 장애인 콜택시는 [[seoul-donghaengmap]]의 콜택시 연계(대표번호 안내)와 같은 이용자층을 대상으로 한다. 같은 사업이 아니라 이용 맥락이 겹치는 것이다. ^[inferred]

## 구성 요소

| 구성 | 설명 |
|---|---|
| 안내 엔진 | `GuideAdapter` 인터페이스. 과속 알림음 거리별 설정(일반/고속도로) 등 |
| DP 엔진 | 지도 표출. `hybridnavi_android` v0.0.9c, v0.0.9d |
| 검색 엔진 | 비통신 검색 엔진(J100 등). MXI와 3D Streaming도 같은 엔진 사용 |
| 맵매칭 라이브러리 | `libmapmatch`. 아트뷰 GPS 변경 대응 테스트판 |
| 앱 패키지 | `TW_Where.apk`, `TW_happywayard.apk`, `TW_tbt.apk`(3종을 함께 배포) |
| 외부 연동 | 콜앱이 `wherenavi://routepassui` 로 Where에 길안내를 요청(탐색 결과 없이 안내 시작) |

엔진별 배포 내용은 [[hybrid-navi-engine-releases-2022]], 배포·OTA 방식은 [[mxi-where-release-ota-2022]], 현장 장애는 [[mxi-field-incidents-2022]]에 있다.

## 운영 방식 요약

- 앱 배포는 **버전 발행 메일**(대상 단말, versionName, versionCode, 릴리즈 노트, 링크)로 한다.
- MXI는 **OTA**로 업데이트한다. 가오픈(테스트 단말 등록) → 상용 오픈 순서.
- 현장 이슈는 고객사(아이나비모빌리티/팅크웨어) → 그룹 → 개발자 순으로 내려오고, 재현 경로와 로그를 주고받는다.
- 기간 한정 테스트 빌드는 **타임락(만료일) 버전**으로 만든다.

## 2023년

택시 기사용 사양(승하차 입구점, 최소 요금 탐색, 아파트 동호수)과 V2.4.2/2.4.3 발행, 검색엔진 규격 변경으로 인한 NPE는 [[mxi-taxi-version-2023]]에 있다.

## 2022년 이후

2023년 직무기술서에는 외부포팅 업무가 "2022 ~ 2023"으로 끝난다. ([[job-description-2023-2026]]) 이후 아이나비 에어 쪽으로 업무가 옮겨 갔다. ([[inavi-air-feature-history]])

## Sources

- [[_raw/_archived/Outlook_2022.md]] — 2022 업무 메일 정리
