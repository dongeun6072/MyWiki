---
title: >-
    2026 목표와 주요업무 체크인
category: references
tags: [career, goals, okr, visibility/internal]
aliases: [2026 상반기 목표, 2026 주요업무 정리]
relationships:
  - target: "[[이동은]]"
    type: related_to
sources:
  - ~/Develop/Wiki/_raw/articles/inavi/2026_상반기_목표_주요업무_정리.md
  - conversation:2026-10-28
summary: >-
    2026년 연간 목표 3개와 주요업무 2개의 진척도, 2~6월 체크인 요약과 10월 체크인(git 커밋 기준). 모빌리티개발셀 상위 목표와의 연결도 포함한다.
provenance:
  extracted: 0.90
  inferred: 0.10
  ambiguous: 0.00
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T09:20:33+09:00
updated: 2026-10-28T08:48:35+09:00
snapshots:
  - "[[_raw/_archived/2026_상반기_목표_주요업무_정리|2026_상반기_목표_주요업무_정리]]"
---

# 2026 목표와 주요업무 체크인

인사평가시스템에 [[이동은]]이 직접 쓴 체크인을 정리한 문서다(기간 2026-01-01 ~ 12-31, 2026-06-24 기준). 체크인 주기는 대략 월 1회다.

## 목표 3개

| 목표 | 상위 목표(모빌리티개발셀) | 진척도 | 궤적 |
|---|---|---|---|
| 1. KMP/CMP 기반 멀티플랫폼 프로젝트 전환 | 프로덕트 상품성 강화 및 R&D | 50% | 15 → 20 → 30 → 40 → 50 |
| 2. AI 도입을 통한 업무 생산성 개선 | 개발/운영 비용 절감 | 50% | 15 → 20 → 30 → 40 → 50 |
| 3. 고객사 프로젝트 요구사항 및 일정 준수 | Partnership SI 사업 수행 | 50% | 15 → 20 → 30 → 40 → 50 |

- 목표 1 상세: 레거시 프로젝트에 KMP 모듈 적용, 비즈니스 로직 일부 통합, Compose 화면 통합 → [[kmp-cmp-adoption]]
- 목표 2 상세: 비개발 JIRA 티켓 유지보수 자동화 검토, AI 번역 프로세스 개선 → [[ai-doc-first-development]]
- 목표 3 상세: 해외향 Navi SDK(Phase-1 1월 iOS SDK 출시, Phase-2 고도화), 국내향 Navi SDK(Phase-1 Flutter 플러그인), 해외향 Maps SDK(Phase-1 출시) → [[orbis-sdk]]

## 주요업무 2개

| 업무 | 진척도 | 내용 |
|---|---|---|
| 1. CMP 역량 강화 | 30% | KMP 역량(프로젝트 유지보수, Global Map SDK KMP 검토), Compose 역량(드로잉런 샘플/데모 앱을 Compose UI로) |
| 2. 아이나비 에어 정기 업데이트 대응 | 45% | 신규 OS, 유지보수·업체 협업, Android Auto 최신 라이브러리 대응. 월별 내용은 [[inavi-air-feature-history]] |

## 월별 핵심 (요약)

| 시점 | 주요 사건 |
|---|---|
| 2월 | Global Maps SDK 기능 개발(좌표 변환과 이벤트 콜백 제외 완료), 국내향 Java → Kotlin 전환 |
| 3월 | 해외향 Maps SDK 출시(IMPS 가이드, Demo 앱), Navi SDK 트럭향 API와 v1.0.2, 삼성생명 POC 시작 |
| 4월 | 드로잉런 SDK 기능 개발 완료, Navi SDK 리팩토링, Jira 티켓 자동화 |
| 5월 | 드로잉런 SDK Android/iOS 배포, Flutter Plugin Step 1 배포, Navi SDK v1.0.3 |
| 6월 | Navi SDK 다국어·`setLanguage`·Web 인증 Style, Maps SDK 웹 인증 Style, KMP 공통 트래킹 이슈 대응, AI 스펙 문서를 셀 Wiki로 이관 |

프로젝트별 상세는 [[drawing-run-sdk]], [[orbis-sdk]]에 있다.

## 10월 체크인 (2026-09-25 ~ 10-24)

레몬베이스 체크인은 전월 25일부터 당월 24일까지를 한 달로 센다. 이 절은 다섯 저장소의 본인 git 커밋을 항목별로 다시 묶은 것이다. 에어 항목만 팀 전체 커밋을 본다. 진척도(%)는 커밋에서 알 수 없어 적지 않았다. 해외향 Navi SDK와 해외향 Maps SDK는 이 기간에 본인 커밋이 없다. 서울동행맵 커밋은 9/28부터 있다.

### 목표 1. KMP/CMP 기반 멀티플랫폼 프로젝트 전환

- [[seoul-donghaengmap]]
  - 로컬 저장소 암호화(AES-GCM)를 공통 코드로 구현했다. 키 보관소만 Android와 iOS가 따로 구현한다.
  - 서버 통신 암호화(키 교환, 응답 필드 복호화)를 공통 모듈에 구현했다.
  - 길안내 TTS·진동을 양 플랫폼에서 지원한다. iOS 발화 오류를 고쳤고, 기기별 TTS 언어 지원 여부를 조회한다.
  - iOS 배포 대응: iPad 화면 방향 요건(App Store Connect 처리 실패 해소), 개발장비 접속용 ATS 예외.
  - 회원탈퇴 시 SNS 연결 해제(카카오·네이버·구글)를 플랫폼별로 구현했다.
- [[drawing-run-sdk]]: 고객사 빌드 환경에 맞춰 Kotlin 2.0.0 / AGP 8.7.1로 내려 빌드한다.

### 목표 2. AI 도입을 통한 업무 생산성 개선

- [[seoul-donghaengmap]]
  - GUI 시안 전량 대조를 AI로 반복한다. 시안이 개정될 때마다 내비, 마이페이지, 홈, 인증, 불편신고 화면에 반영했다.
  - 디자인 시스템 정본(Claude Design)과 앱 컴포넌트를 AI로 대조해 토큰·컴포넌트 변경을 개정마다 반영했다.
  - UX 화면사양 대조(로그인, 즐겨찾기, 서비스정보)와 감리 반영을 진행했다.
  - 리팩토링: 세션·인증 계층, 저장소, 내비게이션 정리, 화면 31개 Compose Preview 추가, 앱 모듈 전체 코드 품질 정리.
  - 팀 공유 Gradle 원격 빌드 캐시 서버에 연결했다.

### 목표 3. 고객사 프로젝트 요구사항 및 일정 준수

- [[drawing-run-sdk]]: SamsungLifeService에 세션 삭제 API를 추가하고 데모 앱에 반영했다. 1.0.3을 배포했다.
- [[seoul-donghaengmap]]
  - 불편신고 API(등록, 수정, 상세, 내역, 사진 업로드)를 연동했고 이중 제출을 막았다.
  - 즐겨찾기를 단말 로컬 저장으로 바꿨다. 계정별로 나눠 저장하고, 로그인하면 비회원 데이터를 옮기고, 탈퇴하면 지운다.
  - 서버 연동: 장소 검색, 언어 설정 서버 저장, 앱 실행 시 설치 출처 스토어 전달, 서버 규격 1.0.36~1.0.46 변경 대응.
  - 길안내 시작 전 전원 확인(배터리 사용 제한, 절전 모드)과 글자 크기 200% 대응을 넣었다.
  - 임시 개발장비로 서버 주소를 바꿨고 PR 리뷰 지적을 반영했다.
- [[orbis-sdk]] 해외향 Navi SDK·Maps SDK: 이 기간 커밋 없음.

### 주요업무 1. CMP 역량 강화

- [[seoul-donghaengmap]]
  - Compose Multiplatform 화면을 크게 개편했다(홈 재구성, 경로 입력 블록, 지도 검색 바, 장소 검색·즐겨찾기 화면 분리, 최근 검색, 개발자 옵션).
  - Compose 디자인 시스템 컴포넌트(다이얼로그, 시트, 토스트, 내비 배너, 타임라인)를 늘리고 표면·타이포 토큰 체계를 개편했다.
  - 텍스트 입력 커서와 한글 조합을 공통 처리로 바꿨고, 길안내 지도를 단일 인스턴스로 바꿨다.
  - 접근성: 이중 낭독을 없애고 낭독 순서를 정리했다.

### 주요업무 2. 아이나비 에어 정기 업데이트 대응

- [[inavi-air]] (팀 전체 커밋 기준, 10/6 한 차례)
  - 친환경 경로 옵션 추가(AIR-2073)
  - targetSdk 36(Android 16) 상향
  - 03.05.64 (301458) 버전 배포

### 10월 해석

10월 커밋은 대부분 서울동행맵이라 다섯 항목 중 네 항목이 같은 저장소에서 나왔다. 해외향 SDK 두 개는 활동이 없어, 목표 3의 SDK 축은 드로잉런 SDK 유지보수만 남았다. ^[inferred]

## 해석

세 목표가 [[orbis-sdk]]와 [[drawing-run-sdk]]에서 겹친다. 같은 작업이 "고객사 대응(목표 3)", "KMP 전환(목표 1)", "AI 활용(목표 2)"에 모두 체크인으로 등장한다. ^[inferred]

## Sources

- [[_raw/_archived/2026_상반기_목표_주요업무_정리.md]] — 목표와 체크인 원문
- conversation:2026-10-28 — 10월 체크인. inavi-location, inavi-air/Air, 해외향 Navi SDK, 해외향 Maps SDK, seoul-donghaeng(Appsource) 저장소의 git 커밋을 묶었다(커밋 메시지 기준, diff 미검증).
