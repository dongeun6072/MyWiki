---
title: >-
    구글 안내 사양·지도 레벨 사양 분석
category: references
project: orbis-sdk
tags: [google-maps, guidance, map-level, orbis, visibility/internal]
aliases: [구글 안내 사양 분석, 구글 지도 레벨 사양 분석]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1028849674
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1119715398
summary: >-
    구글 내비게이션의 음성·TBT·도로명·카메라 안내 방식 13개 항목과 구글 뷰모드(2D Fix/3D) 지도 레벨 분석
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

# 구글 안내 사양·지도 레벨 사양 분석

Orbis 안내 사양을 정하기 위해 구글 내비게이션의 안내 방식(2025-08-25)과 지도 레벨/뷰모드(2025-09-11)를 분석한 두 페이지를 합쳤다. Orbis 쪽 안내 엔진 사양은 [[orbis-guidance-engine-dev-spec]], 지도 모드 수치는 [[orbismap-navisdk-dev-spec-and-poc-prep]], 목차는 [[orbis-design-and-review-hub]].

## 구글 안내 사양 분석 (2025-08-25)

| # | 안내 | 내용 |
|---|---|---|
| 1 | 진출 안내 | 표현 예시 「1km 앞에서 우측 출구로 진출하세요」. 상황: 고속도로 출구 진출. |
| 2 | 램프·분기점 진입 안내 | 예시 「램프에 진입하세요」「분기점에서 우측으로 진입하세요」「600m 앞에서 램프로 우회전 하세요」. 상황: 고속도로 내 분기점 및 연결램프 진입. |
| 3 | 시작 턴 안내 | 거리별 차등 표현 — 「300m 앞에서 살짝 좌회전 입니다」「600m 앞에서 좌회전 입니다」「200m 앞에서 직진 입니다」 |
| 4 | 400m 턴 안내 | 예시 「400m 앞에서 우회전 입니다」. 일반 도로 주행에서 사용. |
| 5 | 1km 턴 안내 | 예시 「1km 앞에서 직진 입니다」. 고속도로 주행에서 사용. |
| 6 | 잠시후 안내 | 100m 이내 안내. 고속도로 1km 안내 이후 일정 구간에서는 "잠시 후" 안내만 제공. |
| 7 | 이어서 안내 | 연속되는 교차로/분기에서 추가 안내 — 「램프에 진입하세요. 그 다음에 오른쪽 분기점입니다」「우회전 입니다. 그 다음에 우회전 입니다」 |
| 8 | 회전교차로 안내 | 예시 「400m 앞에서 회전교차로, 5번째 출구입니다」 |
| 9 | TBT (Turn By Turn) | 기본 화면은 차기만 표시하고, 다음 안내가 필요할 때 차차기에 "다음"으로 표시한다. TBT 아이콘을 터치하면 해당 거리 정보 표시, 추천 차로 정보 표시, 거리 사양 기준 음성 발성을 한다. |
| 10 | 도로/방면 정보 안내 | 도로명 + 직진 거리 안내 「*도로명*으로 계속 직진, 목적지까지 11km」. 차선 이용 안내 「좌측 2개 차선을 이용하여 좌회전」. 경우에 따라 방면 정보를 포함해 표현한다. |
| 11 | 추천 차로 표시 | 차선 정보를 제공할 때 화면에 차선을 강조 표시한다. |
| 12 | 도로명칭 표출 | 정보가 있는 도로는 차량 아이콘 하단에 도로명을 표시한다. 정보가 없는 도로는 "알 수 없는 도로(unknown road)"를 표시한다. |
| 13 | 카메라 안내 | 카메라 관련 안내 없음 |

## 구글 지도 레벨 사양 분석 (2025-09-11)
주행 레벨 조정을 위해 현재 Orbis와 Google의 지도 레벨을 분석한 문서다.

### 구글 뷰모드 사양
- 구글에는 지도 모드를 바꾸는 별도 설정이 없다.
- 구글 내비게이션 설정의 지도표시 항목에서 "항상 북쪽을 위쪽으로" 활성화 여부에 따라 기울기와 줌 레벨이 바뀐다.
  - 활성화 시 `2D Fix`
  - 비활성화 시 `3D`
- 지금까지 검토한 바로는 2D에 대한 설정은 없어 보인다.

### 주행 화면
원문에는 소제목 `2D Fix`, `3D`, `2D`(구글)만 있고 본문(스크린샷/수치)은 비어 있다. 아래 Orbis 수치는 [[orbismap-navisdk-dev-spec-and-poc-prep]]의 "OrbisMap NaviSDK 개발 사양"을 참고한다.

## Related
- [[orbis-guidance-engine-dev-spec]] — Orbis 안내 엔진 사양
- [[orbis-guidance-and-voice-spec]] — 안내·음성 사양 요약
- [[orbismap-navisdk-dev-spec-and-poc-prep]] — 지도 모드(2D 고정/회전, 3D) 수치
- [[orbis-sdk]]

## Sources
- Confluence "구글 안내 사양 분석" (pageId 1028849674) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "구글 지도 레벨 사양 분석" (pageId 1119715398) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
