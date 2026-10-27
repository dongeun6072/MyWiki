---
title: >-
    생성형 AI 조사: ChatGPT 모델·가격·토큰·테스트 결과, GPT-4o 비교 (2024)
category: references
project: inavi-air
tags: [inavi-air, genai, chatgpt, llm-cost, visibility/internal]
aliases: [ChatGPT 관련 내용 정리, GPT-4o vs GPT-4o mini, LLM AI 활용 서비스, 생성형 AI(에어봇)]
relationships:
  - target: "[[inavi-air]]"
    type: related_to
  - target: "[[air-genai-airbot-review-2024]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/493486082
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/582549611
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/387449254
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/502890628
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/516063252
summary: >-
    에어봇용 ChatGPT(GPT-4o mini) 조사 상세: 모델 가격, 질의별 토큰 수, 월 비용 추정(3만 DAU 가정), 시스템 프롬프트 시험 결과, GPT-4o와 mini 비교.
provenance:
  extracted: 0.90
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T13:00:00+09:00
updated: 2026-10-26T13:00:00+09:00
---

# 생성형 AI 조사: ChatGPT 모델·가격·토큰·테스트 결과

2024년 에어 앱에 대화형 AI(에어봇)를 넣기 위해 OpenAI ChatGPT API를 조사한 기록이다. 모델 가격, 질문/답변 토큰 수, 3만 명 일 사용자 가정의 월 비용, 시스템 프롬프트 시험, GPT-4o와 GPT-4o mini 비교를 담았다. 요약본은 [[air-genai-airbot-review-2024]], 전체 목차는 [[air-genai-and-ideation-hub]], 앱 전체 맥락은 [[inavi-air]]를 본다.

## 1. 조사 방향 (ChatGPT 관련 내용 정리, 2024-08-06 수정)

- 하위 링크 페이지: "Llama 관련 자료"(→ [[air-perplexity-and-llama-evaluation-2024]]), "ChatGPT 개발사양"(→ [[air-chatgpt-usecases-and-dev-spec-2024]]).
- Fine-tuning models를 쓰면 응답 정확도는 높아지나 트레이닝 비용과 모델 비용이 크게 늘어난다. 그래서 **prompt engineering 단계에서 기획 예제 기준으로 작업을 추출하고 예상하는 방식**으로 진행하기로 했다.
- 참고 자료: ChatGPT Document, ChatGPT 가격 페이지, ChatGPT 토큰 계산기(`<링크 생략>`).

## 2. 모델 가격표

| 모델 | Input (1M tokens) | Output (1M tokens) |
|---|---|---|
| GPT-4o mini | US$0.150 | US$0.600 |
| GPT-4o | US$2.50 | US$10.00 |

(GPT-4o 가격은 "GPT-4o vs GPT-4o mini" 페이지, 2024-10-23 수정 기준.)

## 3. 토큰 측정 (GPT-4o mini)

테스트 질의 1: "가족과 함께 가면 좋은 서울 근교 드라이브 코스 알려줘" → `input token 38`, 답변 `output token 932`.

답변 구성(요지): 서울 근교 가족용 드라이브 코스 5곳을 `###` 소제목과 `특징/주요 명소/추천 이유` 형식으로 나열하고 마무리 문장을 덧붙였다.

| 번호 | 코스 | 주요 명소 |
|---|---|---|
| 1 | 남양주 다산유적지 | 다산 유적지, 물의 정원, 다산 생태공원 |
| 2 | 양평 두물머리 | 두물머리, 세미원 |
| 3 | 파주 헤이리 예술마을 | 헤이리, 프로방스 마을, 파주 출판단지 |
| 4 | 가평 아침고요수목원 | 아침고요수목원, 남이섬 |
| 5 | 인천 소래포구 | 소래포구 어시장, 소래습지생태공원 |

## 4. 비용 추정 (3만 명 = Firebase 일 사용자 기준, 모두 동일 질문을 하루 1회 한다고 가정)

| 시나리오 | 토큰 | 단가 환산 | 일 비용 | 월 비용 |
|---|---|---|---|---|
| 단발 질문, 답변 제한 없음 (input 비용 제외) | output 932 | 1,073회 사용 시 $0.6 | $16.8 | $504 |
| 단발 질문, 답변 max 256 token (input 비용 제외) | output 256 | 3,906회 사용 시 $0.6 | $4.6 | $139 |
| 연속 대화, 답변 제한 없음 (input+output 전체) | input 1,602 / output 1,464 | input 624회 사용 시 $0.15, output 683회 사용 시 $0.6 | input $7.2 + output $26.4 = $33.6 | $1,008 |

## 5. 연속 대화 시험 (에어봇 응답 기록)

연속성 있는 대화는 이전 대화가 매 호출에 다시 input으로 들어가 토큰이 배수로 늘어난다. 시험 흐름은 3턴이다.

1. "가족과 함께 가면 좋은 서울 근교 드라이브 코스 알려줘" → 가평 남이섬, 양평 두물머리, 포천 허브아일랜드, 홍천 비발디 파크, 세종 가든파이브 등 1~5번 코스(각각 `코스: 서울 → … ` 경로와 추천 이유 포함).
2. "다른 추천코스도 알려줘" → 6 수원 화성행궁, 7 동두천 소요산, 8 강화도, 9 이천 도자기 마을, 10 안성 팜파크.
3. "10번 코스 자세히 알려줘" → 안성 팜파크의 위치, 운영 시간(대체로 10시~18시, 계절·행사에 따라 다름), 농장 체험(딸기·블루베리·고구마·옥수수 수확), 동물 체험(먹이 주기), 체험 프로그램(도자기·화분 만들기, 사전 예약 필요한 경우 있음), 먹거리, 야외 공간(소풍·바비큐), 주변 명소(안성맞춤랜드, 시내 카페, 용인 자연휴양림), 교통(자가용은 경부고속도로 안성IC, 대중교통은 버스/기차 후 택시).

관찰: 세종 가든파이브처럼 지리적으로 맞지 않는 코스가 섞여 나왔다 ^[inferred] (원문은 결과만 기록하고 평가는 적지 않음).

## 6. 시스템 프롬프트 설정 시험 (API Prompt 설정 및 테스트)

### 6.1 1차 시스템 프롬프트

```
너는 자동차 내비게이션 에어봇입니다. 내비게이션 톤으로 얘기해줘. 목적지는 팅크웨어 입니다.
POI 명칭들은 앞뒤로 ***** 붙여줘.
```

- 첫번째 응답: 결과는 만족. 다만 맛집 이름이 상호명이 아니었다("GPT의 한계?").
- 두번째 응답: POI 명칭 구분이 쉽지 않았다.

### 6.2 2차 시스템 프롬프트

```
너는 자동차 내비게이션 에어봇입니다.
내비게이션 톤으로 얘기해줘.
목적지는 팅크웨어 입니다.
추천하는 POI 명칭들은 앞뒤로 ***** 붙여줘.
출발지 관련 내용은 제거해줘.
대답할수 없을땐 "저는 잘 몰라요" 라고 대답해줘.
```

| 응답 순서 | 평가 (원문) |
|---|---|
| 첫번째 | 목적지에 대한 응답을 해줌. 뭔가 잘못됨. |
| 두번째 | 모르는 질문에 대답할 수 있는 수준 |
| 세번째 | NLP에 대한 가능성이 보임 |
| 네번째 | 안내를 진짜 해줌(실제 길안내처럼 답해 버려 부적절하다는 평가 ^[inferred]) |

## 7. GPT-4o vs GPT-4o mini (2024-10-23)

비교 결과:
- 4o는 mini보다 자연어 처리가 더 부드럽고 주소가 정확하게 표출된다.
- 가는 길도 내비에서 쓰기 좋은 요약 정보 형태로 알려줘 커스텀된 느낌을 준다.
- 비용은 4o가 mini보다 10배 이상 비싸 비용 측면이 크게 고려된다.
- POI는 좋은 케이스도 있었으나 동일하게 없는 케이스도 나와 정확도는 추가 확인이 필요하다.
- 비교 스크린샷 case1, case2(각각 GPT-4o와 mini 결과 이미지, 이미지 항목, 내용 없음).

## 8. 보조 페이지

- **LLM AI 활용 서비스** (2024-04-05 수정): 음성인식 관련 내용 제거 / OpenAI로 활용 가능한 영역으로 수정 / 탐색 경로 만드는 내용 수정. 기획 초기 메모 수준의 페이지.
- **생성형 AI(에어봇)**: 날짜·내용·비고 표 구조의 배포 이력. 행 두 개가 있다: "생성형 AI 관련 리소스 배포", "에어연구소(에어봇/Carplay HUD) 리소스 배포"(날짜 칸은 링크 항목, 날짜 값 없음).
- **생성형 AI(w/ ChatGPT)**: 하위 스크럼의 부모 페이지(본문 없음). 스크럼은 [[air-genai-scrum-2024]].

## Related
- [[air-chatgpt-usecases-and-dev-spec-2024]] — 활용 방안과 개발 사양
- [[air-perplexity-and-llama-evaluation-2024]] — 대안 모델 검토
- [[air-genai-airbot-review-2024]] — 기존 요약본
- [[air-confluence-scrum-and-voice-2023-2024]] — 같은 시기 스크럼과 음성 작업
- [[inavi-air]] — 프로젝트 홈

## Sources
- Confluence "ChatGPT 관련 내용 정리" (pageId 493486082) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "GPT-4o vs GPT-4o mini" (pageId 582549611) — 같음
- Confluence "LLM AI 활용 서비스" (pageId 387449254) — 같음
- Confluence "생성형 AI(에어봇)" (pageId 502890628) — 같음
- Confluence "생성형 AI(w/ ChatGPT)" (pageId 516063252, 본문 없음) — 같음
