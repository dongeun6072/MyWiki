---
title: >-
    셀 AI 도구·라이선스 현황
category: references
tags: [company, ai, claude, license, tooling, visibility/internal]
aliases: [Claude 팀플랜, AI TF, 유료 라이선스 조사]
relationships:
  - target: "[[entities/모빌리티개발셀]]"
    type: derived_from
  - target: "[[concepts/ai-doc-first-development]]"
    type: related_to
summary: >-
    모빌리티개발셀의 유료 라이선스 목록, Claude 팀플랜 도입·결제 이력, AI TF 가설 검증, MCP·슬랙봇 거버넌스 문제, Confluence·Notion 변경(2025-07~2026-10).
provenance:
  extracted: 0.8
  inferred: 0.2
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

# 셀 AI 도구·라이선스 현황

[[entities/모빌리티개발셀]] 기준. 계정 ID, 비밀번호, 초대 링크는 채널에 있었지만 옮기지 않았다.

## 유료 라이선스 조사 (2025-11-10, AI TF 사용분 제외)

Windows/MS, Figma(공용 개발 계정), IntelliJ IDEA(1명), Confluence·Jira·Slack(전원), Bitbucket(전원), GitHub(조직 계정), Notion(부문장만 유료), ChatGPT(공용 계정), NHN Cloud 배포용 서비스.

## 연표

| 날짜 | 내용 |
|---|---|
| 2023-12-11 | JetBrains AI Assistant 내장 안내. 데이터 공유 옵션 해제 권장, 소스 조각은 학습에 쓰이지 않는다는 정책 |
| 2025-07-23 | 사내 Slack(PRO)에 Slack AI 일부 적용(대화·스레드 요약, 허들 노트) |
| 2025-11-05 | 개발용 AI 도구 사용 설문(ChatGPT/Codex, Gemini, Claude Code, Copilot, Cursor, Junie) |
| 2025-11-19 | AI TF 가설 3개 검증 시작(아래) |
| 2026-03-30 | AI-FLOW 품의 결재 완료, 03-31 Claude 팀플랜 결제·순차 초대(그룹 팀과 셀 팀 두 개, 셀 4시트) |
| 2026-04-07~09 | 셀 전용 팀으로 재구성할지 비용 재검토, 초대 완료, 관리자 설정 캔버스 생성 |
| 2026-06-29~07-01 | 결제일을 바꾸려고 팀플랜을 해지 후 재구독, 스탠다드 시트 1개 추가(CI/CD 연동·연구용) |
| 2026-08-03 | 오래 걸린 Claude 결제 문제가 카드 변경으로 해결 |
| 2026-09-03 | 라이선스 갱신 성공 |
| 2026-10-06~26 | Confluence 라이선스 수를 그룹·셀 단위로 줄이고(개발 부문은 Confluence만 대상) Notion 유료 구독이 10-28까지만 유지됨. 일부 인원은 공용 계정으로 정리될 수 있다 |

결제는 카드 한도·갱신일 문제로 여러 번 끊겼다. 구독을 해지하고 다시 가입할 때는 세션이 일시적으로 끊길 수 있다.

## AI TF 가설 (APP 파트, 2025-12까지)

1. Figma 원문 텍스트 추출 → 다국어 XML 자동 변환·번역: 90% 이상 시간 단축(검증 완료).
2. Figma 기반 Compose UI 코드 자동 생성: 50% 이상 단축(진행 중).
3. GitHub Copilot Code Review를 PR에 적용: 리뷰 시간 50% 이상 단축.

2025-12-04에는 Claude Code(Opus 4.5, Sonnet 4.5)와 Figma MCP로 사내 GUI 가이드의 토큰·컴포넌트·화면을 CMP로 구현한 데모를 공유했다. 이후 2026-04에는 기획·디자인·APP·SVR을 모두 AI로 진행하는 신사업 킥오프가 언급됐다.

## 활용 경험과 거버넌스

- 커피챗 주제로 Claude Code 사용 후기(2026-04-09), AI 도입 경험(2026-04-22)을 다뤘다. 스킬 문서와 CLAUDE.md, 스웨거 연동, AI 생성 코드의 PR 통제·책임이 논점이었고 "정답은 없고 함께 만든다"로 정리됐다.
- 2026-05-28 이사가 슬랙봇·MCP·서드파티 앱 요청이 무분별하다며 기본 룰셋과 거버넌스가 필요하다고 지적했다. 도구 연동 권한은 셀장에게 공유한다.
- 2026-07-06 전사 AI 활용 현황 조사에서 셀은 Superpowers 기반 ADR·플랜과 위키를 합친 Agentic Development를 소개했다 → [[concepts/ai-doc-first-development]].
- 2026-07-16 셀 슬랙 웹훅(Claude 연동)은 만든 사람이 참여한 채널만 받을 수 있다. 웹훅 URL은 보안 정보다.
- 2026-07-27 부문 프로젝트에서 Jira Time Tracker(JTT, Mac/Windows 앱)를 개발해 팀 베트남과 동행맵 구성원에게 먼저 배포 검증하기로 했다.
- 2026-10-08 부문 강령: AI 기반 산출물의 1차 책임은 작성자이며 부적절한 용어, 메모 문구, 프롬프트 이력, 미검수 내용이 제출 문서에 남지 않게 자체 점검한다.

## 더 보기

- 사용 팁, 스킬, ADR·Dev Wiki, 크레딧 한도 운영은 [[concepts/claude-code-team-practices]], 모델 출시 연표는 [[references/mobility-tech-talk-channel]].

## Sources

- 슬랙 `#모빌리티개발셀`(2023-12~2026-10).
