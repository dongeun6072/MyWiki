---
title: >-
    NaviSDK 스크럼 스냅샷 (초기 환경·Architecture 2024-10, KMP Base 2024-12, 상품화 #7·#9 2025-12, DEMO #5 2025-10)
category: references
project: orbis-sdk
tags: [navisdk, scrum, kmp, architecture, visibility/internal]
aliases: ["[10/28] 초기 환경 구성 - 리뷰", "[10/31] Architecture 정의 - 스크럼", "[12/26] KMP Base 로직 강화 - 스크럼", "[12/11] NaviSDK 상품화 #7 - 스크럼", "[12/24] NaviSDK 상품화 #9 - 스크럼", "[10/15] DEMO/전시회 앱 기능 고도화 #5 - 스크럼"]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[air-growth-research-hub]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/567967770
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/594345988
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/667190337
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1221328897
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1496711169
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/1556447233
summary: >-
    NaviSDK 개발 스크럼 6건(초기 환경 구성 리뷰, Architecture 정의, KMP Base 로직 강화, DEMO/전시회 #5, 상품화 #7·#9)의 목표·티켓 번호·영역별 진행·로드맵을 날짜별로 정리.
provenance:
  extracted: 0.88
  inferred: 0.08
  ambiguous: 0.04
base_confidence: 0.58
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T13:00:00+09:00
updated: 2026-10-26T13:00:00+09:00
---

# NaviSDK 스크럼 스냅샷

에어 성장 프로젝트 묶음에 섞여 있던 NaviSDK 스크럼 6건을 시간순으로 정리했다. SDK 스프린트 전체 흐름은 [[sdk-sprints-2024-2025-hub]], 같은 시기 상세는 [[sdk-sprint-initial-setup-architecture-modules-2024-q4]]와 [[sdk-sprint-kmp-base-logic-2025-01]], 상품화 스크럼은 [[navisdk-commercialization-scrums-2025-2026]], DEMO 앱은 [[demo-exhibition-app-scrums-2025]]를 본다. 담당자는 앱 개발자 A·B·C와 [[이동은]]으로 표기한다(원문 이름 대신 역할).

## 1. [10/28] 초기 환경 구성 - 리뷰 (2024-10, 11/19 수정)
- 대상: 앱 개발자 3명(A, B, [[이동은]]). 목표: 프로젝트 초기 환경 구성 세팅
- 완료 항목: NSDK-239, NSDK-241, NSDK-244, NSDK-248
- 다음 스프린트 이관: NSDK-240, NSDK-242, NSDK-243
- 차기 스프린트 목표: SDK Architecture 구성 방안 정의
- 기타 의견: 초기 인터페이스는 초기 인증을 먼저 진행. Private Key 관리는 OS별로 따로, 통신 모듈은 공통으로. SDK가 지도를 n개 제공하는 Feature 고려

## 2. [10/31] Architecture 정의 - 스크럼 (2024-10~11, 11/19 수정)
- 목표: SDK Architecture 구성 방안 정의
- 담당과 티켓(완료 → 진행): 앱 개발자 A: NSDK-240 완료, NSDK-250·NSDK-255 진행(SDK 발표 자료 산출). 앱 개발자 B: NSDK-242 완료, NSDK-251. [[이동은]]: NSDK-243 완료, NSDK-251(SDK 발표 자료)
- 후속 논의(원문 날짜 표기 "10/5(화)", "10/7(목)"은 월 표기 오류로 보임 ^[ambiguous])
  - Architecture 도구 통일, Architecture 개발 담당 논의 후 구조 통일
  - 모듈별 역할, 개발 단계별, 단계별 산출물별 구조 논의
- 구조 용어 통일
  - **Navigation Core**: 내비 인터페이스, 지도 컨트롤 인터페이스, 통신, 각 뷰 컴포넌트 표출 로직(UIController)
  - **Navigation UI**: 각 플랫폼 컴포넌트 GUI
- "New NaviSDK Plan" 문서의 "SDK 구조도/세부구조도"로 구조 통일 ([[new-navisdk-plan-detail]])
- 후속 논의: 일부 명칭 통일 필요(예: Core와 Common 구분), 오해 없는 용어 사용, 전체 구조 → 모듈별 상세 구조 방식의 여러 구조도, 모듈 역할별 구조도 필요
- **Architecture 설계 1차 완료**, 개발하면서 고도화 예정
- 내비게이션 초기 단계는 Step별로 개발하며 2 Track 진행: (1) 초기 엔진(Static Library) 인터페이스 작업(AOS, iOS) (2) 통신 모듈 개발(공통)

## 3. [12/26] KMP Base 로직 강화 - 스크럼 (2024-12, 2025-01-23 수정)
- 목표: 내부 KMP Base 로직 강화. 기존 NaviMainThread 역할을 세분화해 구조화, 구조도와 프로젝트 구조 정리
- 이 페이지에는 주차별 표 3개가 이어져 있다(앞에서부터 1주차 → 3주차 순 ^[inferred]).

### 티켓 (완료 / 진행)
| 주차 | 앱 개발자 A | 앱 개발자 B | 앱 개발자 C | [[이동은]] |
|---|---|---|---|---|
| 1 | 진행: NSDK-275, 286, 279 | 완료: NSDK-280, 285, 293 / 진행: NSDK-291 | 진행: NSDK-276, 277, 278, 284 | 완료: NSDK-272 / 진행: NSDK-283, 259 |
| 2 | 완료: NSDK-311 / 진행: NSDK-318, 320 | 완료: NSDK-310 / 진행: NSDK-315 | 진행: NSDK-313 | 진행: NSDK-321, 314, 323 |
| 3 | 진행: NSDK-320 | 완료: NSDK-326 / 진행: NSDK-327, 328 | 진행: NSDK-324 | 완료: NSDK-323 / 진행: NSDK-314 |
| 4 | 진행: NSDK-332, 334, 333, 342 | 완료: NSDK-327, 335 / 진행: NSDK-340, 341 | 완료: NSDK-330 / 진행: NSDK-331 | 완료: NSDK-329, 336, 337, 338 / 진행: NSDK-339 |

(표가 4개 나오며, 두 번째 요약 서술과 세 번째 서술 사이에 배치되어 있어 주차 대응은 추정이다 ^[ambiguous].)

### 영역별 진행
- 앱 개발자 A (1~2차 서술): MMC 구조체(C 언어)를 Objective-C로 변환하는 과정의 오류 수정, SMR 컨트롤러 개발 시작. 이후: SMR 컨트롤러 구현 완료(AOS: 파일 Write 확인 중, iOS: fetch 로직 중 Crash → Dispatcher 변경으로 수정 완료, String Formatter 오류 수정 완료, 잘못된 URL 처리는 네트워크 모듈과 함께 지속 확인, DP 지도 Download 시 Crash 수정 완료)
- 앱 개발자 B: NaviMainThread 분해: 데이터 관리(엔진 데이터 수집·가공), 타이머(Util), 상태 관리. 이후: Location Provider 병합 완료, 위치 관리 `PositionManager` 개발(현위치와 LastGPS 관리, `NaviLocation` / `CurLocation` / `MMCInfo`). 네이밍 규칙: 외부 공개는 접두어 생성, 내부는 접두어 없이 사용. `Adapter` = 엔진 연동, `Manager` = 내부 관리 모듈
- 앱 개발자 C: 현재 구조의 `runRoute` 규격 맞춤, 탐색 Agent Request Param은 논의 후 티켓 생성 필요. 이후 탐색 파라미터 구현 중(출발지 PTItem → RPoint, Preference 설정값 필요, routeData·guidanceData·trafficData 3개 다운로드, 부가정보 다운로드)
- [[이동은]]: MMC, GPS 비즈니스 로직 통합(논의 후 티켓 정리 필요). 이후 GPS/MMC 모듈 통합 완료, 간헐적 비정상 종료 발생(foreground → background 전환 시만 발생하는 것은 아님, 원인 분석·지속 테스트)

## 4. [10/15] DEMO/전시회 앱 기능 고도화 #5 - 스크럼 (2025-10-15)
- 목표: DEMO/전시회 버전, UMap 기능 고도화, 화면별 GUI 구성
- 앱 개발자 A: (완료) 교통정보 재탐색 주기 개발(기본 5분, 교통정보 갱신 주기 확인 필요), 유턴 사양 적용(안내, DP), 대만 출장
- 앱 개발자 B: MMC 적용, (완료) 가이드 문서 작성(GitBook; 작성 계정 전환과 번역 문구 정리 ~9/30, kdocs → ChatGPT 번역)
- [[이동은]]: (완료) 멀티 경로 기능 추가(MMC 멀티경로 탐색 규격 적용, 멀티경로 포맷만 유지), 멀티경로 시나리오 적용
- 추가: 1개 앱 다국가 지원(국가별 앱 출시, 빌드 구성 대만향·싱가폴향), 구글 픽셀 4a 단말 대여 요청(MMC, 10/1/2025 전달)
- 전시회 버전: 지도 야간 테마(디자인 책임자 담당), 소스 난독화(aar), TBT 이슈(직진인데 좌/우측 안내, 탐색 엔진 확인 중: 유턴 7,7,7,7 연속 시 첫 번째 7만 사용(원문 취소선) → 7,0,0,0으로 변경), 터널 진행 중 자차 UI, 차로 정보

## 5. [12/11] NaviSDK 상품화 #7 - 스크럼 (2025-12, 2026-01-21 수정)
- 목표: iOS NaviSDK 서비스, MapsSDK 서비스
- 앱 개발자 A: 경로선택화면, CES 시연용 세팅
- [[이동은]]: 효과음 기능 추가, Genesis Search API 대체 검토(12/16까지 마무리 필요)
- 상시: iOS 출시에 맞춰 AOS도 버전·가이드 업데이트(버전 1.0.0, Release Note 항목 추가)
- 이슈: 경로가 존재할 때 주야간 변경 타이밍에 비정상 종료
- 국내 실차: 차주(16일 오전~18일) 차량 확인

## 6. [12/24] NaviSDK 상품화 #9 - 스크럼 (2025-12, 2026-01-21 수정)
- 목표: iOS Navi SDK 서비스, AOS/iOS Map SDK 서비스
- 앱 개발자 A: (완료) 경로선택화면, (완료) CES 시연용 세팅, Framework Upload 프로세스 확인
- [[이동은]]: (완료) 효과음 기능 추가, (완료) Genesis Search API 대체 검토(Key 값을 서버에서 수신해 처리하는 구조, RGC·GC API를 Genesis key로 변경). 경로 존재 시 주야간 변경 비정상 종료 대응: 1차 style.json 교체(1-1 style 교체 중 소스/레이어 삭제로 잘못된 참조 Crash, style 교체 시 메모리 부족), 1-2차 flag로 layer 변경(style.json 1개)
- ~1월 중: iOS 출시에 맞춰 AOS 버전(1.0.0)·가이드·Release Note·라이선스 공지 확인, AOS AppTester 배포
- 언젠가: 인증 실패 시 모든 API 사용 불가 예외 처리
- 이슈: iOS background 상태에서 위치 갱신 안 됨(MMC 또는 메인)

### 로드맵 (#7, #9 공통)
- 25년 4분기: iOS NaviSDK 서비스
- 26년 1분기: MapsSDK 서비스
- 상시 대응: 상용 서버 전환, 업체 요청 대응, 미진한 항목(차로 안내) 검토·개발, 실차 개선 항목(연결로 진입/진출 안내, 특히 고가도로·램프 구간 안내 강화, 회전 구간 안내 강화)

## Related
- [[sdk-sprints-2024-2025-hub]] — SDK 스프린트 허브
- [[navisdk-commercialization-scrums-2025-2026]] — 상품화 스크럼
- [[orbis-sdk]] — 프로젝트 개요
- [[air-growth-research-hub]] — 이 묶음 목차

## Sources
- Confluence "[10/28] 초기 환경 구성 - 리뷰" (pageId 567967770), "[10/31] Architecture 정의 - 스크럼" (594345988), "[12/26] KMP Base 로직 강화 - 스크럼" (667190337), "[10/15] DEMO/전시회 앱 기능 고도화 #5 - 스크럼" (1221328897), "[12/11] NaviSDK 상품화 #7 - 스크럼" (1496711169), "[12/24] NaviSDK 상품화 #9 - 스크럼" (1556447233) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
