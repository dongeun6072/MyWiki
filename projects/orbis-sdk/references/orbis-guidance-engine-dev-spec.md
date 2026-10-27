---
title: >-
    안내 엔진 개발 사양 (음성 안내 템플릿·턴 코드·카메라 판단)
category: references
project: orbis-sdk
tags: [guidance-engine, voice-template, camera, orbis, visibility/internal]
aliases: [안내 엔진 개발 사양]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/987463744
summary: >-
    턴/카메라 음성 안내(잠시후·이어서·500m·1km)의 템플릿·거리 조건·도로 타입, 턴 코드 속성, TomTom 카메라 판단 규칙
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

# 안내 엔진 개발 사양

Orbis 안내 엔진의 음성 안내 템플릿과 판단 규칙을 정리한 문서(2025-08-06 수정)다. 언어별 발성 조각 조합은 [[orbis-voice-phrase-combinations]], 구글 비교는 [[google-navigation-guidance-and-map-level-analysis]], 요약은 [[orbis-guidance-and-voice-spec]], 목차는 [[orbis-design-and-review-hub]].

## 음성 안내 — 턴

| 안내 | 음성 템플릿 | 거리 조건 | 도로 타입 | 예 |
|---|---|---|---|---|
| 잠시후 안내 | 잠시후 + 타입(%s) | 차기 거리 100m 이내 | 전체 | 잠시후 우회전 입니다. |
| 이어서 안내 | 이어서 + 약 + 거리(%1$d) + 단위(%2$s) + 앞 + 타입(%3$s) | 차차기 거리: 잠시후 안내 + 100m 이내 | 전체 | 이어서 약 20m 앞 우회전 입니다. |
| 500m 안내 | 약 + 거리(%1$d) + 단위(%2$s) + 타입(%3$s) | 차차기 거리 500m(+50m) 이내 | 전체 | 약 500m 우회전 입니다. |
| 1km 안내 | 약 + 거리(%1$d) + 단위(%2$s) + 타입(%3$s) | 차차기 거리 1000m(+50m) 이내 | 고속도로 | 약 1km 우회전 입니다. |

## 음성 안내 — 카메라

| 안내 | 음성 템플릿 | 거리 조건 | 도로 타입 | 예 |
|---|---|---|---|---|
| 잠시후 안내 | 잠시후 + 카메라 종류(%s) 가 있습니다. | 차기 거리 100m 이내 | 전체 | 잠시후 고정식 과속 단속 카메라 가 있습니다. |
| 500m 안내 | 약 + 거리(%1$d) + 단위(%2$s) + 앞에 + 타입(%3$s) 가 있습니다. | 차차기 거리 500m(+70m) 이내 | 전체 | 약 500m 앞에 고정식 과속 단속 카메라 가 있습니다. |
| 1km 안내 | 약 + 거리(%1$d) + 단위(%2$s) + 앞에 + 타입(%3$s) 가 있습니다. | 차차기 거리 1000m(+70m) 이내 | 고속도로 | 약 1km 앞에 고정식 과속 단속 카메라 가 있습니다. |

(원문 표기상 "차차기 거리"라고 쓰인 항목이 500m/1km 안내의 판정 거리이며, 턴 500m·1km의 허용 오차는 +50m, 카메라는 +70m다.)

## 턴 코드 속성
- **직진**: 도로 속성이 변경되는 직진 코드만 직진 코드로 설정한다.
- **경유지**: U턴이 아니면서, 링크 id와 osm_id가 동일한 링크일 때 경유지로 설정한다.

## 카메라 판단
- TomTom fix, mobile camera API를 사용한다.
- 좌표 기준으로 가장 가까운 link에 매칭한다.
- 경로열 link에 매칭되는 카메라를 검출한다.
  - 검출된 카메라 링크 프로젝션을 통해 위치를 산정한다.
- 이동식 카메라인 경우 신뢰도 0.5(max 1.0) 이상인 경우만 카메라를 표출한다.

## Related
- [[orbis-voice-phrase-combinations]] — 템플릿에 들어가는 발성 조각과 언어별 문구
- [[orbis-guidance-and-voice-spec]] — 요약
- [[google-navigation-guidance-and-map-level-analysis]] — 구글 안내 방식 비교
- [[orbis-routing-stack]] — Orbis 경로 스택
- [[orbis-sdk]]

## Sources
- Confluence "안내 엔진 개발 사양" (pageId 987463744) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
