---
title: >-
    에어봇 생성형 AI 검토 (ChatGPT, Perplexity, Llama, 2024)
category: references
project: inavi-air
tags: [inavi-air, genai, llm, chatgpt, visibility/internal]
aliases: [에어봇, ChatGPT 활용 방안, perplexity 개발 검토, Llama 관련 자료, LLM AI 활용 서비스]
relationships:
  - target: "[[inavi-air]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/overview
summary: >-
    2024년 에어 앱에 생성형 AI(에어봇 ver 0.5)를 넣기 위해 GPT-4o mini, GPT-4o, Perplexity Sonar, Llama를 비교한 내용: 사용 사례, 비용, 프롬프트와 대화 유지 방식, 출시 결과.
provenance:
  extracted: 0.85
  inferred: 0.12
  ambiguous: 0.03
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T12:40:00+09:00
updated: 2026-10-26T12:40:00+09:00
---

# 에어봇 생성형 AI 검토 (ChatGPT, Perplexity, Llama, 2024)

[[inavi-air]]에 대화형 AI를 붙이는 사업을 2024-06~10에 검토했다. 6월 "신규 Feature Ideation" 스크럼에서 "LLM AI 활용 UseCase"가 나왔고, 9월 스크럼에서 AI 타당성 검토와 품의를 마쳤다. 결과물은 **에어봇 ver 0.5**(AOS v03.05.42 / iOS v03.05.20)로, 에어 연구소에서 "추천받고 싶은 장소를 에어봇에게 물어보는" 서비스다.

## 사용 사례 (ChatGPT 활용 방안)

개인화된 운전 경험, 음성 비서(날씨, 메시지, 전화, 음악), 일정 관리(캘린더 연동), 여행 정보와 역사 가이드, 운전자 피드백 수집, 일상 대화, 목적지 주변 장소 추천, 드라이브 코스 추천(예: "가족과 함께 가면 좋은 서울 근교 드라이브 코스"), 다국어 지원과 교통 법규 설명, 고객 지원(FAQ). 이 중 장소·코스 추천이 먼저 구현됐다.

## 모델과 비용 비교

| 후보 | 비용 | 평가 |
|---|---|---|
| GPT-4o mini | 입력 $0.15 / 출력 $0.60 (100만 토큰당) | 채택. 기획 예제 기준으로 프롬프트 엔지니어링으로 진행 |
| GPT-4o | 입력 $2.50 / 출력 $10.00 | 자연어가 더 부드럽고 주소가 정확하며 요약 길안내가 낫지만 mini보다 10배 이상 비싸다. POI 정확도는 둘 다 없는 경우가 있어 추가 확인 필요 |
| Perplexity Sonar(small online/chat) | 요청 1,000건당 $5 + 토큰 소액(small $0.2/100만) | online 모델 중심으로 검토. chat 모델은 POI 응답이 GPT와 비슷하거나 낮았다. 스트리밍 응답을 누적 문자열로 받으면 출력 토큰이 과도하게 늘었다(49요청에 출력 약 3.2만 토큰, 총 $0.25) |
| Llama 3 | 무료 등급(Hugging Face), 클라우드 쿼터(리전별 QPM 제한), 직접 서버 구축은 서버 자원 외 무료 | 메타 공식 리전에 한국이 없지만 직접 구축은 문제 없다 |

- 파인튜닝은 정확도가 오르지만 학습·모델 비용이 크게 늘어서 하지 않고 프롬프트 엔지니어링으로 갔다.
- 질문 하나(입력 38토큰)에 답변이 약 930토큰 나오는 예가 있어, 출력 길이를 제한하는 "간결하게 알려줘" 같은 지시를 시스템 프롬프트에 넣었다.

## 개발 사양 (ChatGPT 개발 사양)

- Chat 기반 API, 스트리밍으로 실시간 처리. 시스템 프롬프트에 서비스 이름("아이나비 에어봇"), 버전, 자동차 내비 역할, 현위치와 도착지를 넣는다.
- 답변 중 장소명은 앞뒤를 `##`로 감싸 통합 검색과 연결하고, 하이라이트 링크로 보여 준다.
- 대화 연속성을 위해 최근 user + assistant 대화 3쌍을 유지하고 system 데이터는 기본값을 유지한다.
- 에어 연구소의 기능 on/off 설정에 AI 최대 길이(Max Length)가 있다(2024-08 스크럼).

## 관련 사항

- 8월에 생성형 AI 디자인과 연구소 연동을 진행했고, 9월 "생성형 AI 서비스 추가"를 안건으로 다뤘다. 같은 시기 음성 DB를 교체했다 → [[air-confluence-scrum-and-voice-2023-2024]].
- LLM 비용은 사용량에 비례하므로 출시 이후 호출량 모니터링이 필요할 것으로 보인다. ^[inferred]

## Sources

- [Confluence 스페이스 아이나비 에어 & NSDK](https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/overview) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음. ChatGPT 관련 내용 정리, ChatGPT 활용 방안, ChatGPT 개발 사양, GPT-4o vs GPT-4o mini, perplexity 개발 검토, Llama 관련 자료, 에어봇(ver 0.5)
