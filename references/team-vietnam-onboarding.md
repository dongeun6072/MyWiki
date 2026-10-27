---
title: >-
    팀 베트남 채용·온보딩
category: references
tags: [company, hiring, onboarding, vietnam, visibility/internal]
aliases: [팀 베트남]
relationships:
  - target: "[[entities/모빌리티개발셀]]"
    type: derived_from
summary: >-
    2025-11~2026-07 모빌리티개발셀이 팀 베트남 개발자를 채용하고 온보딩한 과정. 첫 프로젝트 선정, 코딩 과제 대신 인터뷰 플랫폼 검토, 4/13 합류 후 리뷰 일정.
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0.0
base_confidence: 0.47
lifecycle: draft
lifecycle_changed: 2026-10-27
tier: supporting
created: 2026-10-27
updated: 2026-10-27
sources:
  - "slack:#모빌리티개발셀"
---

# 팀 베트남 채용·온보딩

[[entities/모빌리티개발셀]]이 현지 개발자와 협업하게 된 과정이다.

## 채용 (2025-11)

- 첫 프로젝트는 **커넥티드 해외향 Android**로 확정됐다. 현지 1차 면접 통과 후보가 있어 사내에서 기술 과제를 내야 했다.
- 공유한 기술 스택: Compose 주력(XML 일부), Room, Firebase, SharedPreferences/DataStore, Retrofit, Coroutine.
- 커넥티드 기반 과제는 시간이 오래 걸려 현지 채용 절차와 맞지 않아, 코딩 인터뷰 플랫폼(HackerRank, CodeSignal 등)을 검토했다. 검토 내용은 Confluence에 공유됐다.

## 합류와 온보딩 (2026)

- 03-04 Android 개발자 4/13 출근 확정, iOS 개발자 1명 추가 채용(QA 2명 계획은 1명으로 조정). 04-02 iOS 채용 확정, 04-13 Android·iOS 2명 합류.
- 온보딩은 Confluence 문서 기준이며 온보딩 저장소는 Access Token 방식 권한으로 만들었다. 3년차 개발자 기준 온보딩 과제 기간은 1~4주 설문으로 정했다.
- 리뷰 일정: 온보딩 과제(04-23), 기획·APP 사용 분석 및 Figma 검토(05-08), 커넥티드 해외향 소스 분석(05-15), 매주 금요일 리뷰와 Daily Report(Slack List) 일일 보고.
- 의존성 정리: 서브모듈과 SPM에서 권한이 필요한 항목을 제거하도록 요청했고, 05-21 해외향 배포 문서를 전달했다. 상용 배포와 메일 전송은 팀 베트남이 맡고 Jenkins·NAS 관련 내용은 문서에서 뺐다.
- 05-28 팀 베트남 대표 방한 시 회사 방향성 발표 자료를 공유했다. 07-28 Jira Time Tracker를 팀 베트남에 먼저 배포해 검증하기로 했다 → [[references/cell-ai-tools-and-licenses]].

## Sources

- 슬랙 `#모빌리티개발셀`(2025-11~2026-07).
