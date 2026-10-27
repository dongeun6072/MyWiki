---
title: >-
    모빌리티개발셀 tech_talk 채널 기록
category: references
tags: [company, slack, tech-talk, ai, conference, visibility/internal]
aliases: [tech_talk 채널, 모빌리티개발셀_tech_talk]
relationships:
  - target: "[[entities/모빌리티개발셀]]"
    type: derived_from
  - target: "[[concepts/claude-code-team-practices]]"
    type: related_to
summary: >-
    2026-01-13에 열린 셀 기술 공유 채널의 성격, 시기별 흐름, AI 모델·도구 출시 연표, 컨퍼런스 일정. 사람 이름과 링크는 수록하지 않았다.
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
  - "slack:#모빌리티개발셀_tech_talk"
---

# 모빌리티개발셀 tech_talk 채널 기록

[[entities/모빌리티개발셀]]의 기술 공유 전용 채널이다. 2026-01-13에 셀장이 열었고, 기존에 따로 있던 Android 기술 채널 두 개를 여기로 통합해 운영하자고 안내했다. 셀원 약 9명이 참여하고, 글은 대부분 "소식 공유 + 한두 줄 의견"이다. 주제는 AI 개발 도구(약 절반), KMP/CMP·Android·iOS, 컨퍼런스, 장비·가격 소식이다.

세부 내용은 다음 페이지에 있다.
- AI 도구 사용 팁과 팀 운영: [[concepts/claude-code-team-practices]]
- KMP/Android/iOS 소식과 사내 산출물: [[references/mobility-tech-talk-kmp-android-ios]]

## 시기별 흐름

| 기간 | 주된 내용 |
|---|---|
| 2026-01~03 | KMP 생태계 소식(KMP 소식 모음 사이트, 라이브러리 검색기), Kotlin 2.3.0 iOS 이슈, AGP 9.0과 KMP 빌드 구성 변화 영상, Kotlin 공식 AI 에이전트 스킬 |
| 2026-04 | 셀 공식 "AI Oriented Development" 시작(04-01). Claude Code 팁이 집중적으로 올라옴, Android CLI·공식 Android 스킬 저장소 공유 |
| 2026-05~06 | 리뷰 자동화 파이프라인 공유, LLM Wiki 기반 ADR과 M.Tech Dev Wiki 운영 시작(06-22), View 기반 UI 라이브러리가 유지 관리 모드로 전환 |
| 2026-07~09 | CMP/KMP 표준 아키텍처 데모 공개, 지도 Compose SDK 0.4.0 배포, iPhone Duo 대응 정보, Firebase iOS 크래시 이슈 |
| 2026-10 | 아티팩트 공유 설정 변경, Xcode 멀티 설치 팁, 모델 출시 소식 |

## AI 모델·도구 출시 소식 (채널에서 공유된 날짜 기준)

| 날짜 | 소식 |
|---|---|
| 04-08 | Claude Mythos Preview 발표(일반 공개 계획은 없음) |
| 04-17 | Claude Opus 4.7 공개. 같은 날 Android CLI 소개 |
| 05-29 | Opus 4.8 출시 |
| 06-10 | Fable 5 출시. 앱 기준 Opus보다 사용량을 2배 빠르게 소모한다고 표시됨 |
| 07-01 | Sonnet 5 출시. 8/31까지 출시 할인가($2/$10 per 백만 토큰), 이후 $3/$15 |
| 07-27 | Opus 5 출시 |
| 09-23 | Opus 5.5 출시와 함께 사용 한도 초기화권 지급 |
| 10-08 | Haiku 5.5 출시 |

외부 소식도 이어졌다. OpenAI GPT-6 Astra(토큰 가격이 Claude Fable과 같다는 언급, 09-08), Gemini 4 Argon(10-14), 오픈클로 모바일 앱(07-01), Cursor iOS 앱(06-29 출시, 유료 플랜 한정), 국내에서 DeepSeek이 차단됐다는 소식(08-19). Android Bench 갱신에서는 Claude가 아직 앞서지만 다른 모델이 많이 따라왔다는 평가였다(08-14).

## 컨퍼런스·행사

- 2026-04-11 Build with AI 2026(GDG Korea Android), 07-25 Google I/O Extended Android, 08-16 KotlinConf Extended South Korea, 09-14 당근 밋업 Android(추첨제, 셀장은 탈락), 10-28 우아콘 2026, 11-02 드로이드나이츠(티켓 오픈 공유).
- KotlinConf'26 키노트(05-26), if(kakao)26 라이브(10-13)도 공유됐다.
- 사내에서는 2026-07-01 챗봇 LLM 활용 내부 세미나 자료를 공유했다.

## 기타

- 도구·장비: 맥 정리 도구(mole), 터미널 `eza`, 모니터 밝기 조절 앱, Apple 제품 DB 사이트, Xcode 여러 버전 병행 사용(Command Line Tools 설정으로 기본 Xcode 결정, 10-22).
- 2026-06-26 애플 제품 가격이 크게 오른 소식(맥북 에어 13형 179만 → 219만 원 등)이 공유됐다. 노트북 교체 수요 조사와 연결해 볼 만하다 → [[concepts/cell-budget-and-expense-policy]].

## Sources

- 슬랙 `#모빌리티개발셀_tech_talk` 전체(2026-01-13~10-22). 원본은 저장소에 없고, 링크·사람 이름·초대 주소는 옮기지 않았다.
