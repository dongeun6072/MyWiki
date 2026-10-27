---
title: >-
    Orbis Tile 지도 style 분석 1차·2차
category: references
project: orbis-sdk
tags: [orbis, tile-map, map-style, tomtom, visibility/internal]
aliases: [Tile 지도 style 분석, Tile 지도 style 분석 2차]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/973504759
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1057980417
summary: >-
    아이나비 Orbis 타일 지도와 TomTom Orbis 지도 스타일을 비교한 1차(2025-08-28)와 2차(2025-09-02) 분석 항목
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

# Orbis Tile 지도 style 분석 1차·2차

좌측은 아이나비 Orbis, 우측은 TomTom Orbis 지도를 기준으로 스타일 차이를 정리한 두 페이지다(1차 2025-08-28, 2차 2025-09-02). 비교 스크린샷은 이미지 항목이라 옮기지 않았다. 관련 비교는 [[apple-map-display-comparison]], 목차는 [[orbis-design-and-review-hub]].

## 1차 분석 (2025-08-28)
1. 도로 번호 / 고속도로 이미지 현지화 필요
2. 도로명 표출 필요, 방향성 표출이 가능한지 확인 필요
3. 건물 데이터 추가가 가능한지 확인 필요
4. 도로 라인 라운드 부분 및 연결 지점 확인 필요
5. 도로 높이별 레이아웃 확인 필요
6. 도로 선형 차이 확인 필요(동일 레벨 기준)

## 2차 분석 (2025-09-02)
1. 겹치는 도로의 경우 고도 기준 위아래 구분이 되지 않음.
2. 3D 건물 표현 데이터가 적용되었는지 확인 필요.
3. 언어별 스타일 필요. 현재 공유된 스타일은 `NAME_EN`으로 설정되어 있음 — 설정 변경을 통해 해결.
   - 추가 발행 시 언어별 처리하는 부분은 관리 주체를 정해야 할 것으로 판단한다.

## 변화 요약
- 1차의 "도로 높이별 레이아웃 확인"이 2차에서 "겹치는 도로의 고도 구분 불가"로, 1차의 "건물 데이터 추가 가능 여부"가 2차에서 "3D 건물 데이터 적용 여부"로 구체화되었다. ^[inferred]
- 언어 문제(`NAME_EN` 고정)는 스타일 설정 변경으로 해결되었다고 원문에 적혀 있다.

## Related
- [[apple-map-display-comparison]] — 아이나비 vs 애플지도 Display 비교
- [[orbismap-api-docs]] — OrbisMap API 문서
- [[orbis-routing-stack]] — Orbis 라우팅/지도 구성
- [[orbis-sdk]]

## Sources
- Confluence "Tile 지도 style 분석" (pageId 973504759) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "Tile 지도 style 분석 2차" (pageId 1057980417) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
