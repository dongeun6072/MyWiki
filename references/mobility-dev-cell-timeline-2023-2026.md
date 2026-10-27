---
title: >-
    모빌리티개발셀 연혁 2023~2026
category: references
tags: [company, organization, timeline, slack, visibility/internal]
aliases: [모빌리티개발셀 타임라인]
relationships:
  - target: "[[entities/모빌리티개발셀]]"
    type: derived_from
summary: >-
    슬랙 #모빌리티개발셀에서 추린 조직 개편, 인원 변동, 사무실 이동, 정책 공지 연표(2023-02~2026-10). 사람 이름은 역할로 대체했다.
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0.0
base_confidence: 0.47
lifecycle: draft
lifecycle_changed: 2026-10-27
tier: supporting
created: 2026-10-27
updated: 2026-10-27
sources:
  - "slack:#모빌리티개발셀"
---

# 모빌리티개발셀 연혁 2023~2026

허브: [[entities/모빌리티개발셀]]. 잡담(점심, 커피, 회식, 자판기)은 제외했다.

## 2023

- 02-01 조직 개편에 맞춰 채널 개설, 약 15명 참여. 04~09 소수 인원 입·퇴장.
- 04-26~27 상반기 워크숍(PmG 셀과 함께). 일정 조사 → 허들 회의 → 차량 배정 순으로 준비했다.
- 08-08 자리배치안을 당일 제출해야 해서 허들 회의로 협의.
- 09~10 공용 개발 계정(애플)에 2단계 인증이 걸려 기기 소지자의 승인이 필요해짐 → [[references/cell-dev-infra-and-build-env]].
- 12-05 Bitbucket 클라우드 DB 유지보수(12/10 새벽) 공지. 12-11 JetBrains AI Assistant 내장 안내.

## 2024

- 신규 입장자가 간헐적으로 들어옴(03, 06, 08, 09, 10, 12월).
- 07-16 iOS 온보딩 프로젝트 최종 리뷰, 10-02 Android 온보딩 프로젝트 최종 리뷰(연구원·주임 단위).
- 10-08 본사 이전 작업. 04월 본사 Jenkins 맥미니가 오프라인이었다가 복구됨.
- 12-23 Firebase Dynamic Links가 2025-08 종료 예정이라 대체 링크 서비스 조사 요청.
- 라이선스·조직 정책 공지는 이 채널에 거의 없었다.

## 2025

- 08-14 타 조직에서 1명 합류. 09월 셀원 다수 이탈.
- **10-01 조직 개편**: 모빌리티Tech그룹 → MX그룹, 신임 그룹장 부임. 셀 구성원 1명이 "리더" 역할을 맡음(팀장 직책과 구분, 역할은 프로세스 개선과 지원).
- 10-15 평가는 올해도 부문장이 진행, 레몬베이스 피드백도 부문장 중심. 10-28 평가 작성 가이드 → [[concepts/cell-performance-and-workreport-process]].
- 11-19 전도금 관리를 Notion에서 Confluence DB로 이전 → [[concepts/cell-budget-and-expense-policy]].
- 11-10 유료 라이선스 조사. 11-12 팀 베트남 첫 프로젝트 확정 → [[references/team-vietnam-onboarding]].
- 12-23 송년회, 12-29 종무식(전사 행사 없이 부문 주관), 12-30~31 권장 휴무.

## 2026

- 01-14 국내향 커넥티드 개발을 외주에서 셀 내부로 전환 결정. 해외향과 같은 포메이션으로 진행.
- 01-26 사무실 이사(좌석 재배치). 04~05월 사업기획팀 이동에 맞춘 셀 자리 재배치.
- 03-31 Claude 팀플랜 결제·초대 → [[references/cell-ai-tools-and-licenses]].
- 04-13 팀 베트남 Android·iOS 개발자 2명 출근.
- 07-02 오르다 서비스 서버 외부 침입 이슈 → [[concepts/cell-security-lessons]].
- 06-30 셀장 유연근무제 A 타입 전환. 07-01 셀원 1명 이탈, 07-20 인원 감소로 커피챗을 소회의실에서 진행.
- 07-22 아이나비 지도 Compose Multiplatform 라이브러리를 Maven 저장소에 배포 → [[concepts/kmp-cmp-adoption]].

### 2026-08 ~ 10 (최근 공지)

- 08-03 Claude 결제 문제가 카드 변경으로 해결(근본 결제 이슈가 남으면 팀을 옮길 수도 있다는 언급). 09-03 라이선스 갱신 성공 → [[references/cell-ai-tools-and-licenses]].
- 08-11 compose 지도 SDK 0.1.11 미만 버전에 앱 키가 포함돼 배포된 문제로 저장소에서 제거 → [[concepts/cell-security-lessons]].
- 08-28 M.Tech 데모 앱 Auth 리팩토링(develop)을 동행맵에 참고하도록 공유.
- 09-14 사내 베타 서비스 시작(Android APK, iOS TestFlight 배포), 미션 3개 오픈. 09-17 서현 오피스 복귀(10/12~19)가 알려져 10-02 부문 전체 자리 이동 공지, 10-08 개인·공용 물품 포장 완료.
- 09-16 타사 개인정보 유출이 AWS 키 탈취로 추정된다는 기사를 근거로 형상관리 소스에 인증키를 넣지 말라는 부문 전달.
- 09-21 직무기술서 현행화 작성 요청(프로덕트개발부문 대상, 주요 업무 Top 3와 협업 방식 중심).
- 10-06 Confluence 라이선스 수 제한 통보(부문 단위 배정을 그룹·셀 단위로 조정), 대표 지시로 직속 조직 자리 조정 중이라는 공유. 10-26 개발 부문은 Confluence만 조정 대상이며 완료 후 공용 계정 생성 예정, Notion 유료 구독은 10-28까지만 유지되어 이후 페이지 생성·파일 업로드·게스트 초대가 제한됨(Confluence 이전 권장).
- 10-07 Gradle 원격 빌드 캐시 서버 오픈 안내, 모바일 SDK 다운로드 서버(Artifactory) 보안 패치로 다운로드 일시 중단 → [[references/cell-dev-infra-and-build-env]].
- 10-08 부문 강령 전달: AI 생성 산출물의 1차 책임은 작성자 본인, 기한이 정해진 요청은 지연하지 말 것.
- 10-19 INAVI MAPS 탐색 장애 의심 공유. 10-26 Claude 표준 시트가 1개 남아 공용 계정에 할당.

## Sources

- 슬랙 `#모빌리티개발셀` 채널(2023-02~2026-10). 원본 비보관, 링크·계정·서버 주소 미수록.
