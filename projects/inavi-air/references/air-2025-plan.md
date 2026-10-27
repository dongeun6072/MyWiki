---
title: >-
    2025 AIR Plan (분기별 사업·QA·개발 계획)
category: references
project: inavi-air
tags: [inavi-air, roadmap, 2025, plan, visibility/internal]
aliases: [2025 AIR Plan, 2025 에어 연간 계획]
relationships:
  - target: "[[inavi-air]]"
    type: related_to
  - target: "[[inavi-air-feature-history]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/669549145
summary: >-
    2025년 에어 앱의 분기·월별 사업/QA/개발 계획 표 전체. 아바티, 황금티켓, 전기차 할인율, 시간제 통행규제, AIR/NSDK 서버분리, Firebase Dynamic Links 대응, 블랙아이스 연동 등.
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

# 2025 AIR Plan (분기별 사업·QA·개발 계획)

2025년 1월 24일 마지막 수정된 에어 앱 연간 계획 표다. 분기(1Q~4Q)별로 월 칸이 있고 각 칸에 `[사업]`, `[QA]`, `[개발]` 담당 구분과 항목이 적혀 있다. 이 계획이 실제 출시 문구로 이어진 결과는 [[air-app-version-notes-2025]]에서 확인할 수 있고, 2024년의 운영 흐름은 [[air-operations-2024]]를 본다.

원문 표는 분기 행의 라벨(1Q 등)과 본문 행이 서로 어긋나 있어, 본문 3개 칸(+ 빈 칸 1개)을 해당 분기의 1·2·3번째 달로 읽었다 ^[inferred]. 항목 앞의 `[QA]`/`[개발]` 사이에 줄바꿈 없이 붙은 하이픈 항목은 가장 가까운 앞 구분(마지막으로 나온 태그)에 속하는 것으로 해석했다 ^[ambiguous].

## 1분기
| 월 | 사업 | QA | 개발 |
|---|---|---|---|
| 1월 | 아바티, 황금티켓 | 전기차 할인율 변경 | PP 고속도로 팝업 추가, AOS 앱 평가 다이얼로그, iOS HUD 안정성 개선 1차 |
| 2월 | 설/추석 무료 개방 주차장 | (항목 없음) | 신규 로그 추가(w/ 선행), iOS HUD 안정성 개선 2차 |
| 3월 | 침수 피해 안내(GUI 변경) | 시간제 통행 규제 | (항목 없음) |

## 2분기
| 월 | 사업 | QA | 개발 |
|---|---|---|---|
| 4월 | 광고상품 추가 (SKP) | (항목 없음) | (항목 없음) |
| 5월 | (항목 없음) | (항목 없음) | AIR/NSDK 서버분리 ^[inferred] |
| 6월 | (항목 없음) | (항목 없음) | Firebase Dynamic Links 중단 대응 ^[inferred] |

## 3분기
| 월 | 사업 | QA | 개발 |
|---|---|---|---|
| 7월 | 신호등 안내 확대 | (항목 없음) | (항목 없음) |
| 8월 | (항목 없음) | (항목 없음) | (항목 없음) |
| 9월 | 설/추석 무료 개방 주차장 | (항목 없음) | (항목 없음) |

## 4분기
| 월 | 사업 | QA | 개발 |
|---|---|---|---|
| 10월 | 블랙아이스 연동 | (항목 없음) | (항목 없음) |
| 11월 | (항목 없음) | (항목 없음) | (항목 없음) |
| 12월 | (항목 없음) | (항목 없음) | (항목 없음) |

## 계획과 실제 문서의 대응(참고)
- 전기차 할인율 변경(1월 QA) ↔ 스토어 문구 "전기차 할인율 및 서비스안정화_25.01"
- 시간제 통행 규제(3월 QA) ↔ "시간제 차량 통행제한 안내_25.04" ([[vehicle-restriction-routing]] 참고)
- 침수 피해 안내(3월 사업) ↔ 2025-06-25 수해 VMS 리소스(`inv_map_vms_ic_noti4~9`)와 "재난 경보 안내_25.06" ^[inferred]
- 광고상품 추가(SKP, 4월) ↔ 2025-12-09 광고 미션 리소스(`airre_cashpage_ad_mission`) ^[inferred]
- 황금티켓(1월 사업) ↔ 2025-01-16 `airre_point_coinbank` 리소스 ([[air-resource-deploy-log-2024-2026]])

## Related
- [[inavi-air]] — 에어 앱 프로젝트 허브
- [[inavi-air-feature-history]] — 기능 이력
- [[air-growth-strategy-and-metrics-2024]] — 2024 성장 전략과 지표
- [[air-release-and-resource-log-hub]] — 이 묶음 목차

## Sources
- Confluence "2025 AIR Plan" (pageId 669549145) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
