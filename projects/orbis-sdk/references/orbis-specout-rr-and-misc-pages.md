---
title: >-
    Specout 리스트·R&R·기타 소형 페이지 (Orbis/SDK 및 에어 보조 문서)
category: references
project: orbis-sdk
tags: [orbis, specout, rr, misc, confluence, visibility/internal]
aliases: [Specout List, R&R - 251127, 내부 테스트 및 TC, UI 디자인 리소스 All, ADAS MAP, 서버 구성도 - 251125, Archived ( POC, MVP ), UX/UI 스토리 보드]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1023705106
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1439137813
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/151191688
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/149028865
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/357236796
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1439301633
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1381105665
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/149061633
summary: >-
    Orbis 이관 시 제외 기능(Specout) 목록, 2025-11 R&R 역할 구조, 내부 테스트 TC 목록 제목, 에어 UI 리소스, 제목만 있는 빈 페이지 목록
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

# Specout 리스트·R&R·기타 소형 페이지

Orbis 관련 소형 페이지와 본문이 거의 없는 페이지를 한곳에 모았다. 큰 주제는 [[orbis-design-and-review-hub]]에서 개별 페이지로 연결된다.

## Specout 리스트 (2025-08-28)
Orbis(대만 PoC)에서 제공하지 않는(Specout) 기능 목록으로 보인다. 원문에는 "Specout"의 정의가 없고 일부 항목에 "데이터 존재/없음" 메모만 붙어 있다. ^[ambiguous]

| 분류 | 항목 | 메모 |
|---|---|---|
| 검색 | 추천어 제공 | |
| 검색 | 내장소 등록 | |
| 검색 | 최근목적지 | |
| 검색 | 지도로 목적지 설정 | |
| 안내 | 구간 카메라 안내 | 데이터 존재 |
| 안내 | 위험지역, 차로정보, 확대도 | 데이터 없음 |
| 탐색 | 회피 탐색 | |
| 교통정보 | 교통정보 진행바 | |
| 교통정보 | CTT | |
| UI | 가로모드 | |
| UI | 야간모드 | |
| 기타 | 오토바이, 화물차 전용 기능 | |

## R&R - 251127 (2025-11-27)
Orbis 프로젝트의 역할 분담표다. 사람 이름은 옮기지 않고 직급/소속으로 적었다. 빈 칸은 원문에서 담당이 비어 있다.

### PM
| 영역 | 담당 |
|---|---|
| NaviSDK, MapsSDK PM | 수석 1인 |
| Web, Admin PM | 팀장 1인 |

### 개발
| 영역 | 소속 / 담당 |
|---|---|
| 메인 | MX그룹/모빌리티개발셀 — 책임 1인, 선임 1인, 주임 1인([[이동은]]) |
| Agent | MX그룹/서버플랫폼셀 (담당자 미기재) |
| 탐색 엔진 | 자율주행기술부분/경로기술개발팀 — 수석 1인 |
| 교통정보 | 통합Map개발부문/선행기술Lab/Dev.2팀 — 주임 1인 |
| MMC | 통합Map개발부문/선행기술Lab/Dev.2팀 — 책임 1인 |
| Maps API | (비어 있음) |
| Web(고객사이트, Admin 사이트) | (비어 있음) |
| CDN | (비어 있음) |
| DB 서버 | (비어 있음) |

### 지도 발행
| 단계 | 하위 | 담당 |
|---|---|---|
| 톰톰 원도 수령 | | (비어 있음) |
| 내비게이션 지도 | 원도 컨버팅 / 원도 컨버터 개발 | (비어 있음) |
| 내비게이션 지도 | 서비스 지도 컨버팅 / 서비스 지도 컨버터 개발 | (비어 있음) |
| 내비게이션 지도 | 서비스 지도 CDN 업로드 | (비어 있음) |
| Tile 지도 | Tile 지도 생성 | (비어 있음) |
| Tile 지도 | Style.json 생성 | (비어 있음) |

### QA
| 영역 | 담당 |
|---|---|
| 앱 검증 | (비어 있음) |
| 지도 검증 | (비어 있음) |

## 내부 테스트 및 TC (2024-02-23, 에어 앱)
에어 앱 기능별 내부 테스트/TC 문서 링크 모음이다. 링크는 모두 `<링크 생략>`. 항목 제목만 옮긴다. 관련 기능 맥락은 [[inavi-air]], [[air-service-stability-release-notes-2023-2026]].
- 제보하기/연구소 리뉴얼
- AI 횡단보도
- 기능고도화
- 에어 캐시 적립 개선
- w3w/카카오 비즈보드/캐시버튼
- HUD/SKP 연동
- 서비스 안정화(23년 12월)
- SKP 광고
- 외부 베타테스터용 이슈 리스트

## UI 디자인 리소스 All (2025-05-27, 에어 앱)
디자인 파일 링크 2건이 있다(Figma 링크 생략): INAVI_AIR_1(2022~2023 #1), INAVI_AIR_2(2023 #2 이후). 이어서 "AIR Resource all" 표제와 "Update" 표제만 있고 본문은 없다.

## 제목만 있는 빈 페이지

| 제목 | pageId | 수정일 |
|---|---|---|
| ADAS MAP | 357236796 | 2024-03-29 |
| 서버 구성도 - 251125 | 1439301633 | 2025-11-27 |
| Archived ( POC, MVP ) | 1381105665 | 2025-11-13 |
| UX/UI 스토리 보드 | 149061633 | 2023-06-15 |

서버 구성도는 이미지 항목으로 추정된다(내용 없음). ^[inferred]

## Related
- [[orbis-sdk]] — Orbis SDK 프로젝트 홈
- [[inavi-air]] — 에어 앱 프로젝트 홈
- [[orbis-navisdk-poc-prep-2025]] — PoC 준비 요약
- [[orbis-design-and-review-hub]] — 이 묶음의 목차

## Sources
- Confluence "Specout List" (pageId 1023705106) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "R&R - 251127" (pageId 1439137813) — 가져온 날짜 2026-10-26
- Confluence "내부 테스트 및 TC" (pageId 151191688) — 가져온 날짜 2026-10-26
- Confluence "UI 디자인 리소스 All" (pageId 149028865) — 가져온 날짜 2026-10-26
- Confluence "ADAS MAP" (pageId 357236796) — 본문 없음
- Confluence "서버 구성도 - 251125" (pageId 1439301633) — 본문 없음
- Confluence "Archived ( POC, MVP )" (pageId 1381105665) — 본문 없음
- Confluence "UX/UI 스토리 보드" (pageId 149061633) — 본문 없음
