---
title: >-
    다국어 내비게이션 단위/표기 사양과 번역 리소스 이력
category: references
project: orbis-sdk
tags: [i18n, units, notation, translation, orbis, visibility/internal]
aliases: [다국어 내비게이션 단위/표기 사양, 다국어 번역 리소스]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/809599362
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/813727747
summary: >-
    중국어 번체/간체 기준 거리·속도·시각·시간 표기 규칙과 국제표준 유지 항목, 번역 리소스 갱신 이력(검수 전 GPT 번역 포함)
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

# 다국어 내비게이션 단위/표기 사양과 번역 리소스 이력

Orbis 내비게이션의 표기 규칙(2025-05-22)과 번역 리소스 갱신 이력(2025-11-04)을 정리한 두 페이지를 합쳤다. 번역 절차는 [[orbis-onesky-translation-process]], 음성 문구는 [[orbis-voice-phrase-combinations]], 목차는 [[orbis-design-and-review-hub]].

## 1. 내비게이션 표기 사양 정의
- 국제표준을 사용할지에 따라 정의한다.
- 국제표준을 유지하는 경우 번역이 필요 없다.
  - 스크립트 내 `Description`은 "_표준", `Keys`는 "_standard"로 표기한다. 예: `Description` 공통_시간_오전_표준 / `Keys` common_time_AM_standard
  - 영문 표기와 동일하게 번역이 필요한 번체/간체 열에 국제표준을 적는다(예: AM/PM, km/h).
- 기능/화면별 표기 사양은 아래 표를 따른다(중국어 기준).

### 기능/화면별 표기 사양

| 기능 또는 화면 | 항목 | 중국어 번체 (zh-TW) | 중국어 간체 (zh-CN) | 비고 |
|---|---|---|---|---|
| 현재 위치, 경로 안내 UI, POI 검색결과 등 | 거리 | `500 公尺`, `2.3 公里` | `500 米`, `2.3 公里` | 한자 사용 |
| 현재 위치, 경로 안내 UI, POI 검색결과 등 | 속도(제한속도 등) | `60 km/h` | `60 km/h` | 국제 표준 유지 |
| 현재 위치, 경로 안내 UI, POI 검색결과 등 | 도착 예정 시각 | `10:30 AM`, `03:05 PM` | `10:30 AM`, `03:05 PM` | 12시간제를 선택한 경우 `AM/PM` 국제 표준 사용 |
| 현재 위치, 경로 안내 UI, POI 검색결과 등 | 예상 시간 | `1小時20分鐘` | `1小时20分钟` | 한자 사용 |
| 경로 요약/전체 보기 | 총 거리 | `13.2 公里` | `13.2 公里` | 한자 사용 |
| 경로 요약/전체 보기 | 예상 시간 | `1小時20分鐘` | `1小时20分钟` | 한자 사용 |
| 설정 > 단위 설정 | 거리 단위 | `公里 (km)` / `英哩 (mile)` | `公里 (km)` / `英里 (mile)` | 한자 + 국제표준 모두 사용 |
| 설정 > 단위 설정 | 속도 단위 | `km/h`, `mph` | `km/h`, `mph` | 국제 표준 유지 |
| 설정 > 시간 표기 형식 | 시간 표기 형식 | `24 小時制`, `12 小時制` | `24 小时制`, `12 小时制` | 한자 사용 |

## 2. 번역 리소스 갱신 이력 (2025-11-04 수정)
원문은 날짜 없이 "검수 전/후" 상태와 변경 내용만 순서대로 나열한다. 위가 오래된 항목으로 보이나 순서는 확정할 수 없다. ^[ambiguous] 제목에 해당하는 링크(스프레드시트 등)는 옮기지 않았다.

| 순번 | 상태 | 변경 내용 |
|---|---|---|
| 1 | 검수 전 | Onesky 번역 초안 |
| 2 | 번역 검수 완료 | 국제 표준 사양 추가 |
| 3 | 검수 전 | GPT 사용하여 번역. '일반 도로' 문구 추가 |
| 4 | 검수 전 | GPT 사용하여 번역. 영어 문구 중 일부 문구의 전치사 변경 |
| 5 | 검수 전 | GPT 사용하여 번역. 음성 카메라/회전 템플릿 추가 |
| 6 | 검수 전 | GPT 사용하여 번역. 음성 템플릿 수정 |
| 7 | 검수 전 | GPT 사용하여 번역. 터널/지하차도 음성 템플릿 추가 |
| 8 | 검수 전 | GPT 사용하여 번역. 모의 주행 시 기존 경로 취소 음성 문구 추가 |
| 9 | 검수 전 | GPT 사용하여 번역. 목적지 입력 문구 수정(어디로 갈까요? → 목적지를 입력해 주세요.) |
| 10 | 검수 전 | GPT 사용하여 번역. "지도다운로드 및 엔진 초기화" 문구 추가 |

## Related
- [[orbis-onesky-translation-process]] — Onesky 다국어 관리 프로세스
- [[orbis-voice-phrase-combinations]] — 음성 문구와 조각 키
- [[orbis-guidance-and-voice-spec]] — 안내·음성 요약
- [[taiwan-field-evaluation-2025]] — 번체/간체 대상 현지 평가
- [[orbis-sdk]]

## Sources
- Confluence "다국어 내비게이션 단위/표기 사양" (pageId 809599362) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "다국어 번역 리소스" (pageId 813727747) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
