---
title: >-
    에어 사용성 개선, 통계 분석, 릴리즈 노트와 리소스 배포 기록 (2024~2026)
category: references
project: inavi-air
tags: [air, release-notes, resources, hud, 2024, visibility/internal]
aliases: [에어 사용성 개선, 에어 사용성 개선 & 통계 분석, 스토리보드, HUD(로드피아) 미연결 이슈 수정_25.10, 안전운전 심볼 2026.09.08, 튜토리얼 유종 '수소' 심볼 2026.09.17, 수해지역 VMS 고도화]
relationships:
  - target: "[[inavi-air]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/375455745
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/401539073
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/260079811
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1190920193
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/2200502483
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/2232714767
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/890372097
summary: >-
    스크럼 이후 소규모 기록 페이지 모음. 에어 퀴즈 스토리보드, HUD 정식 서비스 시작 릴리즈 노트(AOS 03.05.37 / iOS 03.05.16), HUD 미연결 수정 노트, 안전운전·수소 심볼 리소스 배포, VMS 아이콘 배포.
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

# 에어 사용성 개선, 통계 분석, 릴리즈 노트와 리소스 배포 기록 (2024~2026)

에어팀 Confluence의 짧은 기록 페이지 7개를 한곳에 모았다. 스크럼 형식은 아니고 날짜/내용/비고 표나 스토어 공지 문구가 전부다. 스크럼 쪽은 [[air-skp-ad-scrums-2024]], 릴리즈 흐름 전체는 [[air-service-stability-release-notes-2023-2026]], 목차는 [[air-scrum-records-hub]]에 있다.

## 에어 사용성 개선 (수정 2024-03-22)

날짜/내용/비고 표 1행뿐이다.
| 날짜 | 내용 | 비고 |
|---|---|---|
| (링크 항목, 날짜 내용 없음) | 주변검색 리소스 수정 재배포 | (비어 있음) |

## 에어 사용성 개선 & 통계 분석 (수정 2024-04-23) — 스토어 업데이트 노트

HUD 연동 정식 서비스 시작 시점의 스토어 업데이트 문구다. 두 OS 모두 구조가 같다(HUD 정식 서비스 안내, 지도 개선, 버그 수정 및 안정성 개선, 마무리 인사).

**AOS v03.05.37**
- HUD 연동 정식 서비스 시작: 환경설정 > HUD 설정에서 기기를 등록하고, 에어의 길안내를 HUD에서 편리하게 사용
- 발전하는 에어 지도: 주행 중 보이는 경로선을 더 보기 좋게 변경, 안드로이드 오토 주행 중 더 넓게 볼 수 있게 개선
- 버그 수정 및 안정성 개선: 원활한 서비스 제공을 위해 준비
- 마무리: "최신 버전으로 지금 업데이트 해보세요! 더 좋은 서비스를 위해 에어팀은 항상 귀 기울이고 있습니다."(AOS에는 이모지 포함)

**iOS v03.05.16**
- AOS와 동일 구조. 차이는 "안드로이드 오토" 대신 "카플레이 주행 중 더 넓게 볼 수 있게 개선", 이모지 없음.

> 페이지 제목에 "통계 분석"이 있으나 본문에는 통계 내용이 없다. ^[ambiguous]

## 스토리보드 (수정 2024-03-06)

에어 퀴즈 기획의 단계 정의로 보인다. ^[inferred] 같은 시기 스크럼의 "사용자 분석 및 앱테크 기능 추가(에어 퀴즈)"와 연결된다.
- 1차: 에어퀴즈 형태의 간단한 응답을 통해 캐시 미적립 사용자 알아보기
- 2차: 에어 사용자는 앱테크에 관심 있는 사용자인가

## HUD(로드피아) 미연결 이슈 수정_25.10 (수정 2025-09-30)

iOS 스토어 공지 문구(버전 03.05.32, 빌드 488)
- HUD(로드피아) 연결 문제 수정 — 연결 오류를 해결하여 정상적으로 HUD를 사용할 수 있게 함
- 전반적인 서비스 안정성 개선
- 마무리 문구는 위와 동일

## 안전운전 심볼 2026.09.08 (수정 2026-09-08)

안전운전 심볼 추가 리소스 배포 내역.
| 리소스 | 변경 |
|---|---|
| inv_map_safe_label_rear_crackdown | 후면단속 라벨 추가 |
| inv_map_safe_label_two_way | 양방향 라벨 추가 |
| inv_map_safe_sign_bg28_tm | 기존 후면(기본)에서 "구간(신호)"로 변경/추가 |
| inv_map_safe_sign_bg31_tm | 기존 후면(신호), 삭제 |

## 튜토리얼 유종 '수소' 심볼 2026.09.17 (수정 2026-09-17)

- 유종 수소 심볼 추가 리소스 배포: `inv_tuta_btn_energy06` 추가

## 수해지역 VMS 고도화 (수정 2025-06-25)

날짜/내용/비고 표에 날짜 링크와 "VMS ICON 배포" 1행만 있다(비고 없음).

## Related
- [[air-scrum-records-hub]] — 목차
- [[air-service-stability-release-notes-2023-2026]] — 릴리즈 노트 전체 흐름
- [[air-hud-integration-2023]] — HUD 연동 배경
- [[air-hud-launch-stabilization-scrums-2024]] — HUD 정식 서비스 스크럼
- [[inavi-air]] — 프로젝트 허브

## Sources
- Confluence "에어 사용성 개선" (pageId 375455745) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "에어 사용성 개선 & 통계 분석" (pageId 401539073) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "스토리보드" (pageId 260079811) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "HUD(로드피아) 미연결 이슈 수정_25.10" (pageId 1190920193) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "안전운전 심볼 2026.09.08" (pageId 2200502483) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "튜토리얼 유종 '수소' 심볼 2026.09.17" (pageId 2232714767) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "수해지역 VMS 고도화" (pageId 890372097) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
