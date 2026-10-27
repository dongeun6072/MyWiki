---
title: >-
    Perplexity Sonar와 Llama 검토 (2024)
category: references
project: inavi-air
tags: [inavi-air, genai, perplexity, llama, visibility/internal]
aliases: [perplexity 개발 검토, Llama 관련 자료]
relationships:
  - target: "[[inavi-air]]"
    type: related_to
  - target: "[[air-genai-airbot-review-2024]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/600244462
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/496894028
summary: >-
    에어봇 대안으로 검토한 Perplexity Sonar(online/chat) 가격표, 스트리밍 비용 테스트, 프롬프트별 응답, 장단점 결론과 Llama 제공 방식·제한.
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

# Perplexity Sonar와 Llama 검토

ChatGPT 외 대안으로 검토한 Perplexity API(2024-11-08 수정)와 Llama(2024-07-31 수정) 기록이다. ChatGPT 쪽은 [[air-genai-model-research-and-cost-2024]], [[air-chatgpt-usecases-and-dev-spec-2024]]. 허브는 [[air-genai-and-ideation-hub]].

## 1. Perplexity 검토 기반

`llama-3.1-sonar-small-128k-online`과 `llama-3.1-sonar-small-128k-chat`을 비교할 예정이었다. 초기 분석에서 chat 모델은 GPT와 비슷하거나 낮은 수준의 POI 응답을 보여, **online 모델을 중점 검토**하기로 했다.

## 2. 비용 구조

GPT와 달리 input/output token 단가를 따로 두지 않는다. online 모델은 요청 횟수 고정 요금에 token 기반 소액 변동 요금을 합산한다("a fixed price per request and a small variable price based on number of input and output tokens").

| 모델 (Sonar online) | 1,000 요청당 | 1M token당 |
|---|---|---|
| llama-3.1-sonar-small-128k-online | $5 | $0.2 |
| llama-3.1-sonar-large-128k-online | $5 | $1 |
| llama-3.1-sonar-huge-128k-online | $5 | $5 |

| 모델 (Chat) | 1M token당 |
|---|---|
| llama-3.1-sonar-small-128k-chat | $0.2 |
| llama-3.1-sonar-large-128k-chat | $1 |

## 3. 비용 테스트

max 토큰을 제한하지 않은 전체 테스트에서 streaming 방식의 output token이 과도했다. 문자열이 분리되어 오지 않고 응답을 받을 때마다 기존 문자열에 이어 붙는 형태(가 → 가나 → 가나다)로 증가해 더 많은 token이 소모되는 것으로 보인다.

| 항목 | 값 |
|---|---|
| Total Cost | $0.25 |
| 방식 | Streaming |
| Requests | 49 |
| Input | 1,362 |
| Output | 31,775 |

## 4. 프롬프트와 응답 (online, small)

시스템 프롬프트(`$$` 로 POI 구분):

```
"아이나비 에어봇"
"version 0.5."
"자동차 내비게이션."
"명칭,POI,상호명은 앞뒤로 $$만 붙여줘"
"목적지 구의로65"
```

| 질문 | 응답 요약 |
|---|---|
| 너는 누구야? | 문장을 영어("Who are you?")로 번역하고 단어 구조를 설명. 시스템 프롬프트(에어봇 역할)를 인지하지 못함 |
| 판교역 주변 맛집 알려줘 | 8곳을 위치·특징·리뷰 요약 형태로 제시: 라디오베이(펍, 파스타·칵테일), 해미옥(칼국수·해물 뚝배기), 흑화돗(고깃집), 우몽블랙(한우 룸식당, 콜키지 무료), 고수양꼬치(양꼬치·꿔바로우, 성남사랑상품권 사용 가능), 신도세기 판교역점(항정살·갈매기살), 후라토식당 아브뉴프랑 판교점(오므라이스·규카츠), 브루클린더버거조인트 판교점(버거). 실제 상호명과 위치가 나옴 |
| 목적지 주변 맛집 알려줘 | 목적지 맥락을 쓰지 못하고 현대차그룹의 '맛집 로드' 서비스(음성인식 버튼, 1억 8천 건 이상 평가 데이터, 5천 곳 선정 등)를 소개하는 엉뚱한 답 |

## 5. 프롬프트와 응답 (chat, small)

시스템 프롬프트는 4절과 동일(목적지 문구만 "목적지 구의로65").

| 질문 | 응답 요약 |
|---|---|
| 너는 누구야? | "아이나비 에어봇 version 0.5"로 소개하고 목적지 구의로65 길 안내를 하겠다고 답함. 이후 내비 앱 사용법 같은 일반 안내를 늘어놓음 |
| 목적지 주변 맛집 알려줘 | "구의로 65 식당/카페/레스토랑/분식집/피자집"처럼 주소를 이름에 붙인 가짜 항목 5개를 나열하고 "실제로 확인된 데이터가 아니다"라고 덧붙임. 지도/리뷰 사이트 검색을 권유 |

## 6. 결론

| 구분 | 내용 |
|---|---|
| 장점 | online 모델 기준 POI 검색 결과가 ChatGPT보다 정확도 우수 |
| 단점 1 | online 모델은 system prompt 설정을 인지하지 못함(한국어 문제인지 추가 확인 필요) |
| 단점 2 | chat 모델은 POI 검색 결과가 ChatGPT보다 떨어짐 |
| 단점 3 | Streaming 사용 시 현재 API 응답 구조상 token과 리소스가 많이 소모되어 비용 증가와 응답 속도 감소 |

ChatGPT와 동일하게 적용하면 POI 외 나머지 응답 인식률이 떨어진다. API 방식으로 쓰기에는 아직 개발 안정화가 필요하고, 상용 반영은 더 고려가 필요하다는 판단이다. 참고: Perplexity API는 Pro Search(다단계 추론으로 답변 품질을 높이는 기능)를 아직 지원하지 않는다.

## 7. Llama 관련 자료 (2024-07-31)

- 모델 입수: Meta에서 직접 다운로드하거나 다운로드 파트너 Hugging Face, Kaggle 이용.
- Hugging Face가 Llama 3 활용을 위한 무료 등급을 제공해 테스트 가능. 가격 정책은 추후 자세히 확인 예정.
- Google Cloud 등 클라우드 제공 방안도 검토 필요. Google 할당량(Llama 3.1 405B):

| Region | Quota system | Supported context length |
|---|---|---|
| us-central1 | 15 QPM | 32,000 tokens |

- 직접 서버를 구축해 환경을 제공하는 방안: 가용 서버 리소스 외에는 무료.
- 제한: Meta 공식 리전에 아직 한국이 포함되지 않았다. 직접 구축은 문제없다.

## Related
- [[air-genai-model-research-and-cost-2024]] — ChatGPT 가격·토큰 조사
- [[air-chatgpt-usecases-and-dev-spec-2024]] — 개발 사양, Fine-tuning 대신 라마 검토 언급
- [[air-genai-airbot-review-2024]] — 기존 요약본
- [[inavi-air]] — 프로젝트 홈

## Sources
- Confluence "perplexity 개발 검토" (pageId 600244462) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "Llama 관련 자료" (pageId 496894028) — 같음
