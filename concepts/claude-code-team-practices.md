---
title: >-
    셀 Claude Code 활용 관행
category: concepts
tags: [company, ai, claude-code, workflow, adr, visibility/internal]
aliases: [AI Oriented Development, Claude Code 팁, M.Tech Dev Wiki]
relationships:
  - target: "[[entities/모빌리티개발셀]]"
    type: derived_from
  - target: "[[concepts/ai-doc-first-development]]"
    type: extends
  - target: "[[references/cell-ai-tools-and-licenses]]"
    type: related_to
summary: >-
    모빌리티개발셀이 2026-04부터 공식 도입한 AI Oriented Development의 규칙, Claude Code 사용 팁, ADR+superpowers 워크플로, M.Tech Dev Wiki, 사용량·크레딧 운영 방식.
provenance:
  extracted: 0.7
  inferred: 0.3
  ambiguous: 0.0
base_confidence: 0.47
lifecycle: draft
lifecycle_changed: 2026-10-27
tier: core
created: 2026-10-27
updated: 2026-10-27
sources:
  - "slack:#모빌리티개발셀_tech_talk"
  - "slack:#모빌리티개발셀"
---

# 셀 Claude Code 활용 관행

[[entities/모빌리티개발셀]]이 tech_talk 채널에서 공유한 AI 개발 도구 사용 방식이다. 개인 사례는 [[concepts/ai-doc-first-development]], 라이선스와 결제는 [[references/cell-ai-tools-and-licenses]]에 있다.

## 공식 시작 (2026-04-01)

셀장이 "공식적으로 AI ORIENTED DEVELOPMENT를 시작한다"고 공지했다. 확인 사항은 네 가지였다.
1. Claude 초대를 받지 못한 사람은 알린다(가입 이름은 본명으로).
2. Claude Code를 Mac에 설정한다.
3. 보안 파일과 정보는 경로나 환경변수로 따로 관리하고 git에서 무시한다. 표준이 될 수 있게 공유하고 논의한다.
4. AI에 지나치게 의존하거나 맹신해서 책임질 수 없는 환경은 경계한다.

시작은 `CLAUDE.md` 만들기(`/init`)부터라고 안내했다. 부문 차원에서도 2026-10-08에 "AI 기반 산출물의 1차 책임은 작성자"라는 지침이 내려왔다 → [[references/mobility-dev-cell-timeline-2023-2026]].

## 공유된 사용 팁

| 주제 | 내용 |
|---|---|
| 모델 선택 | `/model`로 작업 난이도에 맞춰 선택(일상 코딩은 Sonnet, 복잡한 추론·대규모 리팩토링은 Opus, 간단한 질의는 Haiku). 토큰 절약에 효과 |
| 컨텍스트 | 더러워지면 나쁜 답만 나오므로 `/clear`를 자주 쓴다 |
| 입력 | `!` 접두사로 bash 인라인 실행, Ctrl+S로 프롬프트 임시 저장(stash), `/btw`로 작업을 멈추지 않고 추가 질문 |
| 설정 | statusline 꾸미기(브랜치, 모델, 실시간 사용량), `/config` output-style을 Explanatory로, 작업 완료 알림 훅, 폴더별 `.claude/rules` 가이드라인 |
| 정확도 | 모델이 옛 정보를 참조할 때 크롬 확장으로 최신 문서 기준 질의, 애플 문서용 MCP로 JS 렌더링 문서 가져오기 |
| 확장 | `/goal`(목표 달성까지 반복) 명령, Claude Code 아티팩트(06-19), git diff 뷰어(09-04), 조직 스킬이 Claude Code에서도 보이는 것으로 확인(10-14; 07-24에는 불가였음) |
| 터미널 | 앱과 터미널 중 터미널 선호가 다수 |

## 스킬·플러그인

- **superpowers**(에이전트 스킬 프레임워크)를 06-18 커피챗에서 소개했고, 사용하며 각자의 루틴을 나누자고 했다. 서브에이전트 주도 개발이 느려지는 이슈(Sonnet을 오케스트레이터로 쓰는 방안)가 보고됐다(08-13). spec과 plan 두 중간 산출물 중 spec이 과한 느낌이라는 의견과 관리 방법 질문이 있었다(07-08).
- **caveman**(토큰 절약 스킬)과 **grill-me**, `everything-claude-code`, Matt Pocock 스킬 모음, Kotlin 공식 에이전트 스킬, Android 공식 스킬 저장소, Koin 마이그레이션 스킬(Hilt/Dagger→Koin 최신), 한국어 윤문 스킬, Android 리버스엔지니어링 스킬이 소개됐다. 스킬 마켓플레이스에는 97만 개가 넘게 올라와 있다는 언급이 있었다.
- 직접 만든 것: PR 작성 스킬(03-26), 리뷰 자동화 파이프라인·스크립트·스킬(05-07), 스케줄러 자동화(Cowork), AI 용어집 아티팩트(09-02).
- 2026-07-27 셀장이 플러그인·스킬 없는 바닐라 Claude Code로 개발해 보니, 어느 정도 구축된 프로젝트에서는 품질 차이가 크지 않다고 느꼈다고 적었다. ^[ambiguous]

## ADR + LLM Wiki 전략

- 2026-06-10 커피챗 주제가 "LLM Wiki 기반 ADR"이었고, 관련 아티클과 Karpathy의 LLM Wiki 문서, Obsidian 설치를 안내했다.
- 06-22: ADR + superpowers + caveman 조합으로 AI 주도 개발을 하며, 두 플러그인을 설치하면 훅이 자동 등록돼 세션 시작 때 활성화된다. 모델만 잘 관리하면 적절한 토큰으로 제한된 개발이 잘 돌아간다고 평가했다.
- **M.Tech Dev Wiki**: 각 프로젝트의 Wiki(ADR)를 해당 저장소의 서브모듈 개별 브랜치로 만들고 develop으로 통합하는 방식이다. 이 위키(MyWiki)의 구조와 같은 방향이다. ^[inferred]

## 사용량·크레딧 운영

- Claude는 두 팀으로 운영된다: 셀 팀(월 결제, 프리미엄 시트 가능, 4시트)과 그룹 팀(연 결제, 스탠다드 5시트). 필요 시 프리미엄과 스탠다드를 전환한다(04-01).
- 크레딧 이벤트가 있을 때 개인별 지출 한도를 먼저 걸고 활성화했다: 4월 추가 $200 크레딧에 1인 $20 한도, 7월 $700 크레딧에 1인 $50 한도(07-27).
- 개인 요금제는 Pro에서 Claude Code를 지원하지 않게 바뀐 것으로 보인다는 공유(04-22, 팀 요금제는 문제 없음). 5월 요금제 개편에서 Agent SDK와 `claude -p`가 유료화됐다는 공유(05-14)도 있었다.
- 10-13 Claude 아티팩트를 모든 사용자가 공유할 수 있게 설정을 바꿨고, 10-21 한도 리필권을 쓴 뒤 다시 받은 사람이 있는지 확인이 있었다.
- 2026-04-01 Claude Code 소스맵 유출 사건이 있었고, 한국어로 번역된 내부 구조 문서 아카이브가 공유됐다. 비공식 자료이므로 참고용이다. ^[inferred]

## Sources

- 슬랙 `#모빌리티개발셀_tech_talk`(2026-03~10)와 `#모빌리티개발셀`.
