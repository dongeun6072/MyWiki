---
title: >-
    2023년 업무 메일 개요 (받은편지함 정리)
category: references
tags: [mail, 2023, operations, inavi-air, visibility/internal]
aliases: [Outlook 2023, 2023 받은편지함, 2023 업무 메일]
relationships:
  - target: "[[inavi-2022-mail-overview]]"
    type: extends
  - target: "[[inavi-air]]"
    type: related_to
sources: [~/Develop/Wiki/_raw/articles/Outlook_2023.md]
summary: >-
    2023-01~12월 받은편지함 업무 메일 약 150통의 주제별 지도. HUD 연동, 대구 신호등·AI 횡단보도, MXI 택시 버전, 지도 데이터, 제휴·광고, 플랫폼 마감이 어떤 문서에 정리됐는지와 월별 MR 갱신 표를 담았다.
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0.00
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T10:02:28+09:00
updated: 2026-10-26T10:02:28+09:00
snapshots:
  - "[[_raw/_archived/Outlook_2023|Outlook_2023]]"
---

# 2023년 업무 메일 개요 (받은편지함 정리)

[[이동은]]의 2023년 Outlook 받은편지함(2023-01-01 ~ 12-31)에서 인증·알림·Slack·Notion·Jira·Jenkins, 경영지원 공지, 일정 초대를 뺀 업무 메일 약 150통이다. 2022년 메일은 [[inavi-2022-mail-overview]], 2024년 메일은 [[inavi-2024-mail-overview]]에 있다. **이름, 연락처, 서버 주소, 계정 정보, 사용자 식별자는 위키에 옮기지 않았다.**

## 2022년과 달라진 점

- **외주·외부 연계의 비중이 커졌다.** 2022년은 MXI 등 단말 장애 대응이 절반이었는데, 2023년은 에어(HUD, 대구 신호등/횡단보도, 제휴·광고, 쿠폰)가 더 크다. 직무기술서에서 외부포팅 업무가 2023년에 끝나는 것과 맞다. ([[job-description-2023-2026]]) ^[inferred]
- **조직 표기**: 2023-02부터 같은 팀 서명이 모빌리티Tech그룹에서 **Automotive개발그룹**으로 바뀌는 메일이 있다(MXI, 외부포팅 담당). 운영팀은 품질운영센터/품질운영그룹으로 표기되고 에어 쪽은 모빌리티개발셀/PmG셀로 나온다.
- 에어 스크럼 초대는 2023년에는 필터에서 빠졌다.

## 주제별 지도

| 주제 | 정리한 곳 |
|---|---|
| HUD 연동, Bluetooth 라이브러리, 시리얼 정책, 1차 시험 | [[air-hud-integration-2023]] |
| 대구 보행자 신호등, AI 횡단보도, 실차 테스트 | [[air-daegu-crosswalk-signal-2023]], [[daegu-traffic-light-protocol]] |
| 후면 번호판 단속, 요금 할인, MR 포맷 v5.1, 행정구역 명칭 | [[air-map-data-and-safety-guidance-2023]] |
| w3w, 캐시버튼, 광고 PoC, 쿠폰, 제보하기, 공항 주차 | [[air-partner-integrations-2023]] |
| MXI 택시용 버전, 아트뷰 OTA, 검색엔진 NPE | [[mxi-taxi-version-2023]] |
| Google Play, 카카오 종료, CDN 장애 대책, IDC | [[inavi-platform-deadlines-2023]] |
| 법인카드·전도금 정산·한도 안내(약 30통), 카드 사용 지침, 회계모듈, 전표 | **정리하지 않음**(금전 정보) |
| 방화벽/백본 PM, 그룹웨어 점검, 워크샵, 뉴스레터, 사내 NAS, PC 실사용 조사 | 정리하지 않음(조직·시설 공지) |
| BMW ACE3.0 펌웨어 릴리즈(41~44차, PRO 39~42차) | 참조 수신. 2022와 같은 패턴이라 별도 정리 안 함 |

## PND X1 MR(지도·탐색 엔진) 월별 갱신

매 홀수 달 지도가 갱신될 때 지도 팀이 X1 `mrdata` 버전을 알리면 경로기술개발팀이 **탐색 엔진 상용 장비에 적용**하고 포트를 알린다. `mrmanage.bin` 버전 표기는 계속 `03 00 4D 52`이다. 탐색 포트는 두 개를 번갈아 쓴다.

| 월 | 지도 오픈 예정 | `mrmanage.bin` 생성일 | 적용 포트 |
|---|---|---|---|
| 2023-01 | (23.01a) | 2022-12-07 | 30013 |
| 2023-03 | 03-22 | 2023-02-06 | 30014 |
| 2023-05 | 05-24 | 2023-04-12 | 30013 |
| 2023-07 | 07-19 | 2023-06-22 | 30014 |
| 2023-09 | 09-20 | 2023-07-31 | 30013 |
| 2023-11 | 11-22 | 2023-10-10 | 30014 |

2022년 이후 구조: 지도 팀 → "라이브 탐색 및 도로망 업그레이드 테스트를 위한 서버 동기화" 요청 → 경로기술개발팀 적용 → 운영팀이 라이브 탐색 포트 서버 적용 완료 회신. 여기서 MR은 [[inavi-mr-format-spec]]이다.

## 기타 메모

- **단말 연동 서버 이슈**(10월, Thinkware connected 주행 기록 미표출): 최초 T700이 규격을 구현할 때 서버가 **IMSI로 단말 PK(ICCID)를 찾도록** 만들었는데, Wi-Fi 모델이 추가되면서 규격이 바뀌었다. IMSI 자리에 **MAC 주소**를 보내려면 `model type`을 1(Function Flag 2 또는 3)로 보내야 한다. 테스트 단말은 Flag 0, model type 0이라 맞지 않았고 Flag 0x2, model type 1로 바꾸자 주행 기록이 생성됐다. 좌표가 `0.0, 0.0`으로 들어오는 구간도 확인됐다. 서버 쪽에서 TCP 바이트 패킷을 16진수로 찍는 로그 속성이 있어 켜고 끌 수 있다.
- **LG U+ 내비게이션 품질 미팅**(7/21) 회의록 공유와 후속 회의 요청이 10월에 있었다(본문은 거의 비어 있음).
- **TTLID 생성 문의**(11-02): 지도 엔진의 CTT 그리는 부분에 영향이 없는지 확인 필요.
- Google 계정, 쿠폰 코드 목록, 오퍼월 사용자 로그, 단말 MAC·시리얼은 원본에 있으나 옮기지 않았다.

## Open Questions

- 원본은 답장 인용이 겹치고 일부 메일은 본문이 "약"만 남아 있다(스텝형 주소 검색, 에어 제보하기 개선 등).

## Sources

- [[_raw/_archived/Outlook_2023.md]] — 2023 업무 메일
