---
title: >-
    Orbis SDK (해외향 Navi/Maps SDK, Flutter Plugin)
category: project
tags: [orbis-sdk, sdk, kmp, navigation, visibility/internal]
aliases: [OrbisNaviSDK, 해외향 Navi SDK, 해외향 Maps SDK, Global Maps SDK, Orbis Navi/Map SDK]
relationships:
  - target: "[[kmp-cmp-adoption]]"
    type: uses
sources:
  - ~/Develop/Wiki/_raw/articles/inavi/2026_상반기_목표_주요업무_정리.md
  - ~/Develop/Wiki/_raw/articles/inavi/2026_상반기_성과점검_이동은.md
  - ~/Develop/Wiki/_raw/articles/inavi/2026_직무 기술서_이동은.docx
  - ~/Develop/Wiki/_raw/articles/Outlook_2024.md
  - ~/Develop/Wiki/_raw/articles/Outlook_2025.md
summary: >-
    해외향 Navi SDK, MapLibre 기반 Maps SDK, 두 SDK의 Flutter Plugin을 묶은 프로젝트. 2025~2026년 버전 이력, 기능, 배포 과정의 어려움을 정리했다.
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0.00
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T09:20:33+09:00
updated: 2026-10-26T14:30:00+09:00
snapshots:
  - "[[_raw/_archived/2026_상반기_목표_주요업무_정리|2026_상반기_목표_주요업무_정리]]"
  - "[[_raw/_archived/2026_상반기_성과점검_이동은|2026_상반기_성과점검_이동은]]"
  - "[[_raw/_archived/2026_직무 기술서_이동은.docx|2026_직무 기술서_이동은.docx]]"
  - "[[_raw/_archived/Outlook_2024|Outlook_2024]]"
  - "[[_raw/_archived/Outlook_2025|Outlook_2025]]"
---

# Orbis SDK (해외향 Navi/Maps SDK, Flutter Plugin)

모빌리티개발셀이 파트너 SI 사업으로 진행하는 SDK 묶음이다. 모두 [[이동은]]이 개발과 배포를 맡았다. 표기가 문서마다 다르다(해외향 Navi SDK, OrbisNaviSDK, Global Maps SDK, Orbis Navi/Map SDK). 같은 제품군을 가리키는 것으로 보인다. ^[inferred]

## 구성

| 제품 | 내용 | 기간/상태 |
|---|---|---|
| 해외향 Navi SDK | 검색, 경로탐색, TTS, DP 등 핵심 기능. 대만 현지 실주행 테스트와 전시회 대응, KMP 전환 | 2025-01 ~ 2025-10 개발, 이후 유지보수 |
| 해외향 Maps SDK | MapLibre 기반 지도 SDK. 기능: 인증, 지도 컨트롤, 카메라, 마커, 도형, 사용자 위치, 클러스터링, 좌표 변환, 이벤트 콜백 | 2025-12 ~ 2026-03 출시 |
| Flutter Plugin | Orbis Navi/Map SDK용. Step 1 배포 완료, Dart 위젯 대응은 다음 Step | 2026-04 ~ 2026-05-26 |
| 국내향 Navi SDK | Phase-1이 Flutter 플러그인 대응. Java 로직을 Kotlin으로 전환 | 2026 진행 |

## 버전 이력 (2026 체크인 기준)

- **Navi SDK v1.0.2** (2026-03): 트럭향 API 추가
- **v1.0.3** (2026-05): 탐색 엔진과 맵매칭 업데이트, Flutter Plugin 대응
- **v1.0.4** (예정, 2026-06 기준): 경로 변경 시 교통정보 색상 미반영 이슈 수정, Style 기반 지도 다국어와 `setLanguage` API, Web 인증 Style 연동
- **Maps SDK v1.0.1** (예정): 웹 인증 기반 Style 연동, 다국어 동적 적용
- Maps SDK 출시 때 API 레퍼런스, Demo 앱, IMPS 페이지 연동 가이드를 함께 만들었다.
- **Flutter Plugin pub.dev 배포**: 해외향 Navi/Maps v1.0.0은 2026-05-22, 국내향 Navi/Maps는 2026-07-23(Navi는 README 정정 재배포로 1.0.1). 상세는 [[flutter-sdk-dev-slack-2026]].

## 서버 구조와 규격 문서

- 전체 구조(도로 데이터 → 변환기 → 데이터 라이브러리 → 탐색 서버 → ORBISMAP → SDK): [[orbis-routing-stack]]
- 탐색 서버 API 규격(v2.0, v2.3): [[taiwan-routeserver-api]]
- 도로 네트워크 데이터 라이브러리: [[orbis-route-data-lib]]
- SDK가 호출하는 ORBISMAP API(JWT, 서비스 게이트, 탐색, TomTom 프록시): [[orbismap-api-docs]]
- 트럭향 탐색의 차량 제원 옵션과 실패 코드: [[vehicle-restriction-routing]]
- 2025년 PoC 사전 검토(TomTom 연동, 지도 컨버팅, 대만 안내 데이터 유무, PoC 범위): [[orbis-navisdk-poc-prep-2025]]

## 개발 기록 (Confluence 스페이스 아이나비 에어 & NSDK)

- 스프린트별 결정 타임라인(2024-10 ~ 2026-07): [[navisdk-confluence-sprint-timeline-2024-2026]]
- New NaviSDK 구조(KMP, UI 확장성, 상태 관리), AOS/iOS 엔진 차이, Flutter 플러그인 마일스톤: [[orbis-navisdk-architecture-and-flutter-plan]]
- 안내 엔진 사양, 구글 안내 비교, 다국어 음성 조합, 번역 프로세스: [[orbis-guidance-and-voice-spec]]
- OrbisMap Route와 TomTom Maps SDK 검토: [[orbismap-route-and-tomtom-sdk-review-2025]]
- 국내향 SDK 가이드, 해외향 API 호환 현황, 에어 외부 연동 규격: [[navisdk-api-coverage-and-domestic-sdk-guide]]
- 대만 현지 실차 평가(2025-10): [[taiwan-field-evaluation-2025]]
- 2024년 NaviSDK 활동(맵매칭 엔진, 티머니 크래시, SDK Renewal, 대만향 검토 요청): [[navi-sdk-2024-activity]]
- 2025년 개발 흐름(경로 서버·맵매칭 라이브러리 릴리즈, 디스플레이, 샘플 앱): [[orbis-navisdk-development-2025]]
- 2025년 사업·법무 검토(TomTom 파트너십, 특허, 현지 업체, 싱가포르 서버): [[orbis-taiwan-business-2025]]
- 2026년 개발 흐름(경로 서버 v1.7~v2.31, Horizon 서버, 맵매칭, Admin 통계): [[orbis-taiwan-development-2026]]
- 본인 작업 이력(Bitbucket 커밋 기준, diff 미검증): 내비게이션 SDK는 [[navisdk-core-commit-history]](972건, 2024-10~2026-09), 글로벌 지도 SDK Android는 [[global-map-sdk-android-commit-history-2026]](163건, 2026-01~07)
- 프로젝트 채널(#10_prj-orbis-navisdk, 2025-02~2026-10) 대화: [[navisdk-prj-slack-2025-h1]] → [[navisdk-prj-slack-2025-q3]] → [[navisdk-prj-slack-2025-q4]] → [[navisdk-prj-slack-2026-h1a]] → [[navisdk-prj-slack-2026-h1b]]

## 개발 방식

- Android/iOS 공통 로직을 KMP 모듈로 올리는 리팩토링을 계속했다: 초기 국내향 Navi SDK 소스 제거, 플랫폼별 로직을 공통 로직으로 이동, 공통 SDK 에러 처리 구조 일원화 → [[kmp-cmp-adoption]]
- Flutter Plugin부터는 기능 스펙과 ADR을 먼저 `docs` 폴더에 쓰고 AI와 협업했다. → [[ai-doc-first-development]]

## 배포 프로세스의 어려움

배포는 Android 서브모듈 빌드 → Dokka 빌드 → iOS XCFramework 빌드 → SPM 순서로 여러 단계를 차례로 수행해야 해서 복잡했다. 2026 상반기에 공통 배포 프로세스를 정비해 일부 줄였고, 안정성과 효율은 계속 개선 대상이다. 팀 리더도 "배포 프로세스 전문가로 성장하는 것 같다"는 평을 남겼다([[2026-performance-review-selfeval]]).

## 상세 문서 (Confluence 전체 반영)

요약 페이지의 상세판이다. 원본 Confluence 페이지를 압축하지 않고 옮겼다(2026-10-26 가져옴).

- [[inavi-sdk-android-guide-hub]] — 국내향 iNavi SDK Android 가이드(개정이력, 세팅, 시나리오, API 레퍼런스, 에러 코드)
- [[inavi-sdk-ios-guide-hub]] — 국내향 iNavi SDK iOS 가이드
- [[orbis-design-and-review-hub]] — Orbis 설계·검토 문서(신 NaviSDK, 상태 흐름, 엔진 차이, Flutter 계획, 음성·번역, 대만 평가)
- [[sdk-sprints-2024-2025-hub]] — SDK 스프린트 2024-10 ~ 2025-06 상세
- [[sdk-sprints-2025-2026-hub]] — SDK 스프린트 2025-06 ~ 2026-07 상세
- [[navisdk-inavicontroller-unimplemented-status]] — 해외향 SDK API 미구현 현황 전체 표
- [[orbis-navisdk-kdoc-and-mkdocs-guide]] — KDoc과 MkDocs 문서 발행 가이드
- [[navisdk-scrum-snapshots-2024-10-to-2025-12]] — NSDK 스크럼 보충(초기 환경, Architecture, DEMO #5, 상품화 #7·#9)
- [[flutter-sdk-dev-slack-2026]] — Flutter SDK 개발 슬랙 채널(2026-05~07): 해외향 선행 배포 방향, pub.dev publisher 인증 절차, 패키지명, 샘플앱 Android/iOS 차이, 배포 기록

- 대만 FTO 검토: [[taiwan-navisdk-fto-patent-review-2025]]
- TomTom 교통 흐름(OpenLR) 질의응답: [[tomtom-traffic-flow-openlr-inquiries-2024]]

## Open Questions

- Navi SDK v1.0.4, Maps SDK v1.0.1이 실제 배포됐는지는 2026-06 체크인 이후 기록이 없어 확인되지 않았다.
- 2025-06 이후 OrbisMap Maps SDK가 제공되지 않아 MapLibre로 자체 구축했다는 기록이 있다([[navisdk-confluence-sprint-timeline-2024-2026]]). Orbis 스타일과 어떻게 맞췄는지는 확인되지 않았다.
- 해외 규격 문서는 [[taiwan-routeserver-api]] 등으로 정리했지만, SDK 앱 코드와 문서 버전이 대응하는 지점은 확인되지 않았다.

## Sources

- [[_raw/_archived/2026_상반기_목표_주요업무_정리.md]] — 월별 체크인
- [[_raw/_archived/2026_상반기_성과점검_이동은.md]] — 상반기 성과
- [[_raw/_archived/2026_직무 기술서_이동은.docx]] — 프로젝트 수행 기간
- [[_raw/_archived/Outlook_2024.md]] — 2024 업무 메일(SDK Renewal, 대만향 검토 요청)
- [[_raw/_archived/Outlook_2025.md]] — 2025 업무 메일(대만향 NaviSDK 개발·사업)
- [[_raw/_archived/Outlook_2026.md]] — 2026 업무 메일(경로 서버 릴리즈, 맵매칭, 운영)
