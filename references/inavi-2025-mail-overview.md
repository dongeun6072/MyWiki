---
title: >-
    2025년 업무 메일 개요 (받은편지함 정리)
category: references
tags: [mail, 2025, operations, orbis-sdk, inavi-air, visibility/internal]
aliases: [Outlook 2025, 2025 받은편지함, 2025 업무 메일]
relationships:
  - target: "[[inavi-2024-mail-overview]]"
    type: extends
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[inavi-air]]"
    type: related_to
sources: [~/Develop/Wiki/_raw/articles/Outlook_2025.md]
summary: >-
    2025-01~12월 받은편지함 업무 메일 약 180통의 주제별 지도. 대만향 Orbis NaviSDK 개발·사업, 에어 운영, 공통 내비 기능 변경, 유럽향 A01 후속, 월별 MR 갱신 표를 담았다.
provenance:
  extracted: 0.80
  inferred: 0.18
  ambiguous: 0.02
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T11:18:00+09:00
updated: 2026-10-26T11:18:00+09:00
snapshots:
  - "[[_raw/_archived/Outlook_2025|Outlook_2025]]"
---

# 2025년 업무 메일 개요 (받은편지함 정리)

[[이동은]]의 2025년 Outlook 받은편지함(2025-01-01 ~ 12-31)에서 인증·알림·Slack·Notion·Jira·Jenkins, 경영지원·HR 공지, 일정 초대를 뺀 업무 메일 약 180통이다. 2024년은 [[inavi-2024-mail-overview]]에 있다. 이어지는 2026년은 [[inavi-2026-mail-overview]]에 있다. **이름, 연락처, 서버 주소, 계정·키 정보는 위키에 옮기지 않았다. 암호·인증·로그인·인증서 관련 메일은 정리 대상에서 뺐다.**

## 2024년과 달라진 점

- **주제의 중심이 해외향 SDK로 옮겨 갔다.** 2024년 11월 SDK Renewal에서 시작한 일이 2025년에는 TomTom Orbis 지도 기반 **대만향 NaviSDK MVP**가 되어 경로 서버 릴리즈(15회 이상), 맵매칭 라이브러리(20회 안팎) 메일이 이어진다. → [[orbis-navisdk-development-2025]]
- 사업·법무 쪽 검토가 개발 메일에 섞여 들어온다(파트너십 계약, 특허 검토, 현지 업체, 개인정보 규제). → [[orbis-taiwan-business-2025]]
- 유럽향 A01은 양산 단계의 후속 메일만 남았다. → [[tsd-a01]]
- 서명 부서명이 모빌리티Tech그룹에서 **프로덕트개발부문**(10월 이후), **MX그룹**(10-22)으로 바뀐다. 경로기술개발팀은 자율주행기술그룹/부문 소속으로 나온다. ^[inferred]

## 주제별 지도

| 주제 | 정리한 곳 |
|---|---|
| 대만·한국 경로 서버, Route Data Library, 맵매칭 라이브러리, 디스플레이(PBF, MapLibre), 테스트 앱, 현지화 | [[orbis-navisdk-development-2025]] |
| TomTom 파트너십 범위, 특허 검토, POI·고객 협의, 오픈소스 고지, 싱가포르 서버 | [[orbis-taiwan-business-2025]] |
| 스토어 정책, 파트너 SDK, 오르다 연계, HUD 외부포팅, 도엽 오류, CDN 이관 | [[air-operations-2025]] |
| 시간제 통행제한, 스마트 재탐색, 소수점 교통정보, 스쿨존·결빙 안내, 재난 정보 연계 | [[nav-service-features-2025]] |
| 유럽향 TomTom 내비 후속(W3W, 소프트웨어 릴리즈, ISA 재평가, 지도 납품, ANA 6.0) | [[tsd-a01]]에 2025 절 추가 |
| 법인카드 정산·한도, 월 회계 결산 요청, 비용 지침 | **정리하지 않음**(금전 정보) |
| 패스트파이브 공유오피스, 신차 구매 사이트, 자율주행 전시 안내 등 | 정리하지 않음(시설·복지·행사 공지) |
| 앱스토어·개발자 계정, 인증서 만료·폐기, 통합회원·Thinkware 로그인 오류, 개발자 접근 승인 | **정리하지 않음**(인증 관련) |
| BMW ACE3.0 릴리즈, 아이나비레터 | 참조 수신, 별도 정리 안 함 |

## PND X1 MR(지도·탐색 엔진) 월별 갱신

흐름은 [[inavi-2024-mail-overview]]와 같다. `mrmanage.bin` 버전 표기는 `03 00 4D 52`를 유지한다.

| 월 | 지도 오픈 예정 | `mrmanage.bin` 생성일 | 적용 포트 |
|---|---|---|---|
| 2025-01 | 01-22 | 2024-12-13 | 30013 |
| 2025-03 | 03-19 | 2025-02-09 | 30014 |
| 2025-05 | 05-21 | 2025-04-01 | 30013 |
| 2025-07 | 07-23 | 2025-06-04 | 30014 |

09월(2509)과 11월분은 제목만 있고 본문이 남아 있지 않다. 에어 지도 발행은 2508a 메일이 있다.

## 회사 맥락 (공지와 뉴스레터)

- **아이나비 스탬프 - 오르다**: 2025-03-31 론칭한 스탬프 투어 아웃도어 서비스. 사내 안내(04-01)에서 앱 소개와 론칭 이벤트가 나온다. → [[air-operations-2025]]
- **자율주행·모빌리티 전시**(07-02), 2025 대만 전시(10월, TPCA)에서 U-Map 시연이 있었다.
- 09-30 **상장 철회 이후 재정비 현황과 지속 가능한 성장 계획** 공유 메일이 있었으나 본문이 남아 있지 않다. 2024년 뉴스레터는 연내 상장 계획을 알렸다. ^[inferred]
- 아이나비레터는 2주년(09-30, vol.26)을 맞았다.

## Open Questions

- 일부 메일은 본문이 "약"만 남아 있어 제목 외 내용을 알 수 없다.
- 상장 철회 이후 계획의 내용은 확인되지 않는다.

## Sources

- [[_raw/_archived/Outlook_2025.md]] — 2025 업무 메일
