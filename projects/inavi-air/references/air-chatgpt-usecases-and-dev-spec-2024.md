---
title: >-
    ChatGPT 활용 방안(UseCase)과 개발 사양, 에어봇 ver 0.5 (2024)
category: references
project: inavi-air
tags: [inavi-air, genai, airbot, chatgpt, visibility/internal]
aliases: [ChatGPT 활용 방안, ChatGPT 개발 사양, 에어봇(ver 0.5)_TBD, UseCase & Benefits]
relationships:
  - target: "[[inavi-air]]"
    type: related_to
  - target: "[[air-genai-airbot-review-2024]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/522389148
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/503382137
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/540049522
summary: >-
    ChatGPT(GPT-4o mini) 활용 UseCase 10종과 테스트 케이스별 비용, 개발 사양(시스템 프롬프트, 대화 3개 유지, 요청 JSON 구조, 이후 검토 항목), 에어봇 ver 0.5 스토어 문구.
provenance:
  extracted: 0.92
  inferred: 0.06
  ambiguous: 0.02
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T13:00:00+09:00
updated: 2026-10-26T13:00:00+09:00
---

# ChatGPT 활용 방안(UseCase)과 개발 사양, 에어봇 ver 0.5

2024년 8~10월 에어 앱 에어봇 개발을 위해 정리한 문서 세 건이다. "ChatGPT 활용 방안"(8/28), "ChatGPT 개발 사양"(9/19), "에어봇(ver 0.5)_TBD"(10/10, 스토어 출시 문구). 가격·토큰 조사는 [[air-genai-model-research-and-cost-2024]], 대안 모델은 [[air-perplexity-and-llama-evaluation-2024]], 허브는 [[air-genai-and-ideation-hub]].

## 1. 활용 방안 개요

- 사용 모델: GPT-4o mini (input US$0.150 / 1M, output US$0.600 / 1M)
- 테스트 방식: ChatGPT Playground와 Python으로 기능 확인, System 프롬프트 설정, Assistants 개인화 지정.

## 2. UseCase & Benefits (전체)

| # | UseCase | Benefits |
|---|---|---|
| 1 | 개인화된 운전 경험 | 내비게이션에 통합해 운전 습관, 선호도, 과거 기록을 학습하고 개인화된 운전 경험 제공 |
| 2 | 음성 비서 역할 통합 | 운전 중 날씨 확인, 메시지 보내기, 전화 걸기, 음악 재생 등 다양한 요청 처리 |
| 3 | 스케줄 관리 기능 | 캘린더 연동으로 기록, 추가, 편집 등 요청을 처리·관리 |
| 4 | 여행 정보 및 역사적 배경 가이드 | 지역의 역사적 배경과 문화 정보 제공 |
| 5 | 운전자 피드백 수집 및 개선 | 경로 안내가 불명확했던 부분의 피드백을 실시간 수집해 이후 안내를 더 명확하고 정확하게 학습 |
| 6 | 일상적인 대화 | 주행 중 대화로 에어와 소통한다는 느낌을 줌 |
| 7 | 목적지 주변 장소 추천 | 따로 검색하지 않아도 추천 장소로 이동 가능 |
| 8 | 드라이브 코스 추천 | 따로 찾지 않아도 추천 코스 활용, 장거리 여행 계획에 도움 |
| 9 | 다국어 지원 및 문화적 차이 해결 | TTS 기존 안내 음성을 다국어로 대체 가능, 대한민국 교통 법규 설명 |
| 10 | 고객 지원 서비스 | 자주 묻는 질문에 응답 |

## 3. 테스트 케이스와 비용 (모델 GPT-4o mini, 3만 명 Firebase 일 사용자 기준)

### 3.1 개인화된 운전 경험

시스템 프롬프트(중괄호는 사용자 속성 치환 자리):

```
You are a driving assistant.
The driver has a {스피드광} driving style, prefers {k-pop} music,
and usually commutes for {1시간}.
Provide personalized driving advice for their next trip.
```

응답 내용은 이미지 항목(내용 없음). 비용: input 78 token(12,820회 요청 시 $0.15), output 418 token(2,392회 요청 시 $0.6), 3만 명 기준 일 $7.85 / 월 $235.5. 연속 대화(78+418+추가 대화…)는 기존 대화가 누적되어 토큰이 배수로 증가한다(상세 생략).

### 3.2 스케줄 관리 기능

Assistants function 설정:

```
{
  "name": "get_date",
  "description": "일정을 등록 합니다.",
  "strict": false,
  "parameters": {
    "type": "object",
    "properties": {
      "date": {
        "type": "string",
        "description": "Must be a date in the format of day month, for example 1 June, 23 July."
      }
    },
    "required": []
  }
}
```

비용: input 665 token(1,503회 요청 시 $0.15), output 46 token(21,739회 요청 시 $0.6), 일 $3.8 / 월 $114.

### 3.3 드라이브 코스 추천

Assistants 설정:

```
아이나비 에어봇
나이는 28살.
자동차 내비게이션.
도착지 구의로 65.
간결하게 알려줘.
```

비용: input 320 token(3,125회 요청 시 $0.15), output 297 token(3,367회 요청 시 $0.6), 일 $6.78 / 월 $203.4.

### 3.4 케이스별 월 비용 요약

| 케이스 | input | output | 일 | 월 |
|---|---|---|---|---|
| 개인화 운전 | 78 | 418 | $7.85 | $235.5 |
| 스케줄 관리 | 665 | 46 | $3.8 | $114 |
| 드라이브 코스 | 320 | 297 | $6.78 | $203.4 |
| 연속 대화(input 1,602 / output 1,464) | 1,602 | 1,464 | $33.6 (input $7.2 + output $26.4) | $1,008 |

연속 대화 예시는 "가족과 함께 가면 좋은 서울 근교 드라이브 코스" 3턴(코스 10개 추천 후 10번 상세)이며 응답 전문은 [[air-genai-model-research-and-cost-2024]] 5절에 정리했다.

## 4. 개발 사양 (2024-09-19)

- Chat 기반 API 사용. Chat을 Stream 기반으로 실시간 처리하는 방안은 **사양 검토 필요**.
- System 프롬프트로 우선 설정:

```
아이나비 에어봇
version 0.5.
자동차 내비게이션.
현위치 성남시 삼평동.
도착지 구의로 65. //도착지는 상황에 따라 변경
```

- 응답에서 앞뒤 `##` 로 구분한 명칭을 통합검색 대상으로 삼는다. 해당 명칭을 하이라이트 링크로 표시해 검색하도록 유지한다.
- 연속 대화: 최근 `user + assistant` 한 쌍을 하나의 단락으로 보고 **대화 3개를 유지**하면서 API 통신한다. system 데이터는 default로 유지한다.
- max token은 500으로 진행. 추천 목록 중 답변이 중간에 잘리는 경우가 나오면 조정이 필요하다(아래 샘플 JSON은 시험 당시 256).

### 4.1 요청 JSON 구조

| 키 | 값/의미 |
|---|---|
| `model` | `gpt-4o-mini` |
| `messages[]` | `role`(`system`/`user`/`assistant`)과 `content[]`(`type: "text"`, `text`)의 배열. 첫 항목은 system, 이후 user/assistant 쌍이 반복 |
| `temperature` | 1 |
| `max_tokens` | 256(샘플) / 운영 방침 500 |
| `top_p` | 1 |
| `frequency_penalty` | 0 |
| `presence_penalty` | 0 |

```
{
  "model": "gpt-4o-mini",
  "messages": [
    { "role": "system", "content": [ { "type": "text",
        "text": "아이나비 에어봇\n나이는 28살.\n자동차 내비게이션.\n도착지 구의로 65.\n간결하게 알려줘." } ] },
    { "role": "user", "content": [ { "type": "text",
        "text": "가족과 함께 가면 좋은 서울 근교 드라이브 코스 알려줘" } ] },
    { "role": "assistant", "content": [ { "type": "text", "text": "(추천 코스 4곳 답변)" } ] },
    { "role": "user", "content": [ { "type": "text", "text": "2번 코스 자세히 알려줘" } ] },
    { "role": "assistant", "content": [ { "type": "text", "text": "(두물머리 상세 답변, 길이 제한으로 문장 중간에 잘림)" } ] },
    { "role": "user", "content": [ { "type": "text", "text": "추가 내용 알려줘" } ] },
    { "role": "assistant", "content": [ { "type": "text", "text": "(추가 정보 답변, 역시 중간에 잘림)" } ] }
  ],
  "temperature": 1,
  "max_tokens": 256,
  "top_p": 1,
  "frequency_penalty": 0,
  "presence_penalty": 0
}
```

샘플 응답 요지: 1턴은 남산서울타워, 양평 두물머리, 남한산성, 파주 임진각 4곳을 추천. 2턴은 두물머리 가는 길(올림픽대로 → 팔당대교 → 6번 국도 → 양수대교 → 두물머리, 주차장), 볼거리(두물머리 나루터, 세미원). 3턴은 두물경 낚시터, 자전거 대여, 카페·음식점, 산책로, 주변 관광지(양수리, 소나무숲길, 용문사). 두 응답 모두 max_tokens 제한으로 끊겼다.

### 4.2 이후 검토 항목

- **Function Calling** 방식: 특정 함수 목록을 지정해 정해진 object를 추출할 수 있다. 예시:

```
{
  "name": "get_place",
  "description": "장소를 찾아봅니다.",
  "parameters": {
    "type": "object",
    "properties": {
      "place": { "type": "string", "description": "The name of place e.g. 부산" }
    },
    "required": [ "place" ]
  }
}
```

- **Fine-Tuning**을 통한 개별 학습: 비용이 대략 2배로 늘어난다. 라마(Llama)를 활용하는 방안을 차기에 검토([[air-perplexity-and-llama-evaluation-2024]]).

## 5. 에어봇 ver 0.5 스토어 문구 (2024-10-10, TBD 상태)

| 구분 | 버전 | 문구 항목 |
|---|---|---|
| AOS | v03.05.42 | "에어봇 ver 0.5 출시!" (ChatGPT를 활용한 서비스 오픈, 추천받고 싶은 장소를 에어봇에게 질문, 자세한 내용은 에어연구소 참고) / "발랄한 음성 변경!" (환경설정 > 안내 설정 > 길안내 음성에서 확인) / "버그 수정 및 안정성 개선" / "최신 버전으로 지금 업데이트 해보세요! 더 좋은 서비스를 위해 에어팀은 항상 귀 기울이고 있습니다." |
| iOS | v03.05.20 | AOS와 동일한 3개 항목과 마무리 문구(이모지만 빠짐) |

## Related
- [[air-genai-model-research-and-cost-2024]] — 가격과 시험 결과 전체
- [[air-genai-scrum-2024]] — 개발 시기의 스크럼(품의, 출시 일정)
- [[air-genai-airbot-review-2024]] — 기존 요약본
- [[inavi-air]] — 프로젝트 홈
- [[air-confluence-scrum-and-voice-2023-2024]] — 발랄한 음성 작업 맥락

## Sources
- Confluence "ChatGPT 활용 방안" (pageId 522389148) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "ChatGPT 개발 사양" (pageId 503382137) — 같음
- Confluence "에어봇(ver 0.5)_TBD" (pageId 540049522) — 같음
