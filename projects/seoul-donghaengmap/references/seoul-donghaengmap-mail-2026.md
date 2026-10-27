---
title: >-
    서울 동행맵 고도화 메일 (2026): 수주, 컨소시엄 R&R, 앱 이관, 실내 내비
category: references
project: seoul-donghaengmap
tags: [seoul-donghaengmap, consortium, indoor-navigation, visibility/internal]
aliases: [동행맵 2026 메일, 동행맵 컨소시엄 R&R, 동행맵 앱 이관]
relationships:
  - target: "[[seoul-donghaengmap]]"
    type: extends
  - target: "[[seoul-donghaengmap-lbs-collaboration]]"
    type: related_to
  - target: "[[inavi-2026-mail-overview]]"
    type: derived_from
sources: [~/Develop/Wiki/_raw/articles/Outlook_2026.md]
summary: >-
    2026-06~10월 메일 속 서울 동행맵 진행: 3개사 컨소시엄 수주, 08-12 협의 R&R, 기존 앱 이관 질의, 디자인 보안 솔루션, 지도 SDK 키 발급, 실내 내비 지하철역 확정.
provenance:
  extracted: 0.80
  inferred: 0.17
  ambiguous: 0.03
base_confidence: 0.35
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T15:16:00+09:00
updated: 2026-10-26T15:16:00+09:00
snapshots:
  - "[[_raw/_archived/Outlook_2026|Outlook_2026]]"
---

# 서울 동행맵 고도화 메일 (2026)

프로젝트 개요는 [[seoul-donghaengmap]], LBS 협업은 [[seoul-donghaengmap-lbs-collaboration]]에 있다.

## 타임라인

| 날짜 | 내용 |
|---|---|
| 06-25 | 3개사 컨소시엄과 협력사 1곳이 참여한 제안을 마치고 **우선협상자로 선정**, 기술 협상 후 당일 계약 예정. 서울시 착수보고회가 같은 날 있었다. 역할은 동행맵 앱(Android/iOS) 신규 기획·디자인·개발과 서울시 지하철 10개 역 실내 내비 연계다. 제안 인력 프로필 작성 요청도 이 메일 계열이다 |
| 08-12 | 컨소시엄 개발 협의(08-13 회신 메일이 R&R과 To-do 정리). 협업 Repo에 ingest됨 |
| 08-18 | 기획·디자인 리뷰 |
| 09-03 | 서울시 담당자가 유지보수업체 답변을 전달한 **앱 이관 질의** 메일 체인 |
| 09-17 | 디자인 시안 의견, 지도 SDK AppKey 발급 요청 |
| 10-14 | 실내 내비 대상 지하철역 확정(시청역 포함 11개), 신도림·동묘앞 도면 송부 |

## 컨소시엄 R&R (08-13)

| 회사 | 담당 |
|---|---|
| 총괄 업체(아로정보기술) | 전체 총괄, H/W 인프라, 음성인식·LLM AI SD, 백엔드 서버, 웹 어드민 |
| 아이나비시스템즈 | UX·UI 기획과 디자인, 앱(AOS·iOS) 개발, 도보(실외) 내비 SDK 통합과 실내 내비 측위 SDK 통합·구현, 앱 서비스 Agent 서버(로그인, 회원정보·즐겨찾기, 외부앱 연동 정보), INAVI Maps SDK·API 제공 |
| LBS 업체 | 도보 내비 길안내 UX·UI 사양(메인 앱과의 전환·복귀 시나리오까지만 구성) |

- 디자인 시스템은 색상·폰트·공통 컴포넌트 수준을 지켜 룩앤필을 통일한다. 기능 리스트 기준으로 당사 역할은 별도 제안한다.

## 앱 이관 질의 (09-03)

기존 앱의 소스 이관을 위해 서울시가 유지보수업체에 확인한 내용이 왔다: 앱 서명 키 관련 파일, 소셜 로그인(Apple은 `sign_in_with_apple` 네이티브 방식으로 받은 `userIdentifier`를 자체 로그인 API에 전달 등), 네이버 로그인 설정 파일 등. 첨부 파일과 값은 옮기지 않았다. → [[seoul-donghaengmap-existing-app-v2]]

## 기타

- **보안 솔루션(09-17)**: 디자인 관련 전달 메일에 보안 솔루션 항목이 있어 우리 쪽도 적용이 필요할 수 있다고 봤다. → [[seoul-donghaengmap-app-vulnerability-reports]]
- **지도 SDK AppKey(09-17)**: 서비스용과 LBS Tech 개발용 두 개의 AppKey가 발급됐다(키 값은 옮기지 않음).

## Open Questions

- 이관 질의의 최종 답변과 인수 범위는 메일 체인에서 확정되지 않았다.

## Sources

- [[_raw/_archived/Outlook_2026.md]] — 2026 업무 메일
