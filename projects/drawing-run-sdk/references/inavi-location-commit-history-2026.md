---
title: >-
    inavi-location 작업 이력 2026
category: references
project: drawing-run-sdk
tags: [drawing-run-sdk, kmp, tracking, sdk, bitbucket, commit-history, visibility/internal]
relationships:
  - target: "[[drawing-run-sdk]]"
    type: related_to
  - target: "[[drawing-run-sdk-release-history-2026]]"
    type: related_to
  - target: "[[drawing-run-sdk-launch-scope-and-data-items-2026]]"
    type: related_to
sources:
  - repo:bitbucket/mobility-tech/inavi-location
summary: >-
    inavi-location(삼성생명 위치·드로잉런 SDK) 본인 커밋 219건(2026-04~10)의 주제별 이력. 커밋 메시지 기준이며 diff는 검증하지 않았다.
provenance:
  extracted: 0.85
  inferred: 0.12
  ambiguous: 0.03
base_confidence: 0.42
lifecycle: draft
lifecycle_changed: 2026-10-28
tier: supporting
created: 2026-10-28T10:00:00+09:00
updated: 2026-10-28T10:00:00+09:00
snapshots:
  - "[[_raw/_archived/Bitbucket_inavi-location_커밋목록_dongeun|Bitbucket_inavi-location_커밋목록_dongeun]]"
---

# inavi-location 작업 이력 2026

본인이 작성한 `inavi-location` 저장소(드로잉런 위치·트래킹 SDK, Kotlin Multiplatform) 커밋 219건(2026-04-09 ~ 2026-10-15)을 주제별로 묶은 이력이다. 프로젝트 개요는 [[drawing-run-sdk]], 릴리즈는 [[drawing-run-sdk-release-history-2026]], 범위와 데이터 항목은 [[drawing-run-sdk-launch-scope-and-data-items-2026]], 연동 문의는 [[drawing-run-sdk-integration-qna-2026]]를 본다. 월별 건수는 2026-04 144건, 05 44건, 06 22건, 07 1건, 08 2건, 10 7건이다.

> [!warning] 커밋 메시지 기준, diff 미검증
> 이 페이지는 커밋 메시지만 근거로 한 요약이다. 메시지와 실제 변경이 다를 수 있다. 주제 분류는 메시지 키워드와 이슈 키로 한 1차 분류라 경계 사례가 있고 ^[inferred], 대상을 알 수 없는 커밋은 따로 모았다 ^[ambiguous]. 각 항목의 해시로 `git show <해시>`를 실행해 확인한다. 동기와 효과는 메시지에 있는 것만 적었다. 서버 포트와 숨은 기능 진입 방법 등 보안 대상 값은 원본에서도 가렸다.

근거는 커밋 메시지뿐이며 diff와 코드는 확인하지 않았다.

## 기간 개요

커밋 목록은 2026-04-09부터 2026-10-15까지 219건이다. 월별로는 2026-04 144건, 2026-05 44건, 2026-06 22건, 2026-07 1건, 2026-08 2건, 2026-10 6건이어서 4월에 전체의 3분의 2가 몰려 있다. 커밋 메시지상 4월에는 프로젝트 초기 구성, 모듈 구조 정리, 권한 요청, 페이스·활동 인식 지표, Foreground 서비스 관련 작업이 이어진다. 5월에는 `[SLDR-30]` 키가 붙은 공개 API 정리, Artifactory 배포 설정, 연동 가이드 문서 작업이 중심이다. 6월 이후에는 stop/pause 분리와 reset API 같은 세션 제어 작업과 로컬 AAR 전달, 세션 삭제 API 추가, 빌드 버전 조정 작업이 소수 있다.

## 1. 프로젝트 초기 구성 및 AI 에이전트 설정 (20건)

기간: 2026-04~2026-04

커밋 메시지상 KMP 프로젝트 빌드 환경 설정, shared/Android/iOS 앱 모듈 추가, composeApp 삭제, shared에서 core 멀티모듈 구조로의 전환, core:location·core:gpx 모듈 추가 관련 작업이 15건 있다. 이어서 Kermit/Koin 기반 Component 베이스 클래스 추가와 core:common 템플릿 코드 삭제가 있다. Claude Code 프로젝트 스킬·MCP 설정, AI Agent 표준 가이드 문서, kotlin-refactor 스킬, AGENTS.md 모듈 구조 갱신 관련 작업이 5건 있다.

이슈 키: [SLDR-2], [SLDR-8]

- `cd349c8` (2026-04-09) Initial commit
- `68d734f` (2026-04-10) KMP 프로젝트 빌드 환경 설정
- `0c3839c` (2026-04-10) [SLDR-2] shared를 core 멀티모듈 구조로 전환
- `ab14353` (2026-04-10) [SLDR-2] core:location 모듈 추가
- `cab0391` (2026-04-10) [SLDR-2] Koin/Kermit 기반 Component 베이스 클래스 추가
- `fe52cdf` (2026-04-13) AI Agent 표준 가이드 문서 추가

## 2. 위치·모션·알림 권한 요청 (11건)

기간: 2026-04~2026-05

커밋 메시지상 moko-permissions 의존성 추가와 위치 권한 요청 구현, 앱 연동 작업이 있다. 활동 인식(모션) 권한 요청 추가, startLocationUpdate 호출 전 위치 권한 확인·요청(Android, iOS 각각), iOS CMMotion 권한 요청 방식 교체와 거부 시 조기 리턴 관련 작업이 있다. 권한 요청 책임을 `:core`/`:samsunglife`에서 빼고 체크 전용 API로 정비하며 샘플 앱에서 직접 처리하도록 바꾼 작업이 2건 있다.

이슈 키: [SLDR-8], [SLDR-29]

- `b71ab51` (2026-04-13) [SLDR-8] moko-permissions 의존성 및 위치 권한 설정 추가
- `ad76e26` (2026-04-13) [SLDR-8] 위치 권한 요청 기능 구현
- `b77aff0` (2026-04-17) [SLDR-29] 활동 인식(모션) 권한 요청 추가
- `c977929` (2026-04-30) 권한 요청 책임 분리, 체크 전용 API로 정비
- `3d4db05` (2026-04-30) iOS CMMotion 권한 요청을 startActivityUpdates 표준 패턴으로 교체
- `23ca1c1` (2026-05-06) iOS CMMotion 권한 거부 시 조기 리턴 추가

## 3. 모듈·패키지 구조 및 DI 리팩터링 (24건)

기간: 2026-04~2026-04

커밋 메시지상 `[SLDR-8]` 아래 서브모듈 패키지 구조 정규화, core:common·core:database 패키지 이동, core:location을 core:tracking으로 이동, samsunglife 파사드 모듈 추가 관련 작업이 있다. LocationService를 TrackingRepository로 교체하고 Flow 노출·리스너 파사드로 전환한 작업, Koin 초기화 이전과 Component CoroutineScope 추가, 자체 Time 유틸의 kotlinx-datetime 교체, LocationSample의 LocationPoint 리네이밍, 미사용 코드·의존성 제거, LocationTracker 상태 관리 정리 관련 작업이 있다. iOS 빌드 스크립트와 Xcode 설정 변경도 포함된다.

이슈 키: [SLDR-8]

- `eda9209` (2026-04-14) [SLDR-8] 서브모듈 패키지 구조 정규화
- `07a8d93` (2026-04-14) [SLDR-8] core:location을 core:tracking 모듈로 이동하고 패키지 재편성
- `52d8225` (2026-04-14) [SLDR-8] samsunglife 파사드 모듈 추가, 앱을 해당 모듈 기반으로 전환
- `604ff52` (2026-04-14) [SLDR-8] LocationService를 TrackingRepository로 교체
- `6bc73ea` (2026-04-15) [SLDR-8] Koin 초기화를 samsunglife 모듈로 이전
- `38f95fe` (2026-04-15) [SLDR-8] LocationSample을 LocationPoint로 리네이밍

## 4. 세션 저장 모델·TrackingResult·DB 스키마 (6건)

기간: 2026-04~2026-04

커밋 메시지상 TrackingResult GPS 추적 결과 데이터 모델 추가, 경로 이미지 배경 투명 변경, DB 스키마 버전 업그레이드와 스키마 변경 시 자동 재생성 설정 관련 작업이 있다. 세션 총 시간(duration) 저장 기능 추가와 LocationPoint/TrackingSession Repository 신규 추가도 있다.

이슈 키: [SLDR-8], [SLDR-12]

- `82adc52` (2026-04-16) [SLDR-8] DB 스키마 버전 업그레이드
- `a2b9e07` (2026-04-16) [SLDR-8] TrackingResult GPS 추적 결과 데이터 모델 추가
- `2ea583c` (2026-04-16) [SLDR-8] 경로 이미지 배경을 투명으로 변경
- `bbde347` (2026-04-16) [SLDR-12] 스키마 변경 시 DB 자동 재생성 설정
- `a30e0ec` (2026-04-16) [SLDR-12] 세션 총 시간(duration) 저장 기능 추가
- `7e8f243` (2026-04-17) LocationPoint/TrackingSession Repository 신규 추가

## 5. Tracking 엔진·서비스 분리 및 클래스 네이밍 정리 (25건)

기간: 2026-04~2026-04

커밋 메시지상 Tracking 오케스트레이션의 Service/Engine 분리, TrackingService 인터페이스 분리, startTracking의 디스패처 변경 관련 작업이 있다. 여러 Calculator/Accumulator/Tracker 클래스에 `Tracking` 접두사를 붙이는 rename 작업이 약 10건이다. 실시간 지표 6개 Flow를 UIData 단일 Flow로 통합한 작업, 미사용 클래스 제거, nowMillis·toRadians 유틸 추가가 있다. runSession 중복 실행 가드, DB/IO를 Default Dispatcher로 이동, TrackingEngine stop에서 job 취소 수정 같은 버그 수정도 포함된다.

이슈 키: [SLDR-29]

- `3015b2d` (2026-04-17) Tracking 오케스트레이션을 Service/Engine으로 분리
- `a795f5a` (2026-04-17) TrackingEngine stop에서 job을 실제로 취소하도록 수정
- `bcc1588` (2026-04-17) [SLDR-29] SamsungLifeService.startTracking을 Main 디스패처로 실행
- `83667f6` (2026-04-23) LapCalculator를 TrackingLapCalculator로 rename
- `ddf8f78` (2026-04-24) 실시간 지표 6개 Flow를 UIData 단일 Flow로 통합
- `a743701` (2026-04-27) runSession 중복 실행 가드 추가

## 6. 페이스 계산·표시 및 고도 설정 (20건)

기간: 2026-04~2026-04

커밋 메시지상 평균/최고 페이스 계산기(TrackingPace) 추가, TrackingSession 페이스 컬럼 추가, SamsungLifeService 페이스 Flow 구독 API 추가, Android/iOS 앱 표시 관련 작업이 `[SLDR-15]`로 11건 있다. 이후 최고 페이스 표시 제거와 코드 리뷰 반영이 이어진다. `[SLDR-16]`에서는 이동(러닝+걷기) 평균 페이스 계산·노출과 데이터 탭 표시, `[SLDR-18]`에서는 구간별 첫 구간 대비 페이스 차이 계산이 있다. 고도 deadband 기본값 조정, iOS 데이터 탭 상승/하강 고도 표시 제거, 페이스 디버그용 원시값 Flow 노출 관련 작업이 4건 있다.

이슈 키: [SLDR-15], [SLDR-16], [SLDR-18]

- `77a0bbf` (2026-04-20) [SLDR-15] 평균/최고 페이스 계산기 TrackingPace 추가
- `8b1eba0` (2026-04-20) [SLDR-15] SamsungLifeService에 페이스 Flow 구독 API 추가
- `0e700ef` (2026-04-20) [SLDR-15] 현재 포인트에서 최고 페이스 표시 제거
- `4b366dd` (2026-04-22) [SLDR-16] 이동(러닝+걷기) 평균 페이스 계산·노출
- `a6d1836` (2026-04-21) altitudeDeadbandMeters 기본값을 0.3m로 하향
- `7c55c55` (2026-04-27) [SLDR-18] 구간별 첫 구간 대비 페이스 차이 계산

## 7. 활동 인식(모션) 및 러닝/걷기/대기 통계 (22건)

기간: 2026-04~2026-06

커밋 메시지상 MotionProvider 활동 인식 구현(Android, iOS), 러닝/걷기/대기 집계 모델과 세션 컬럼 추가(DB v9, v10), movementStatsFlow 연동, UI 실시간 통계 표시 관련 작업이 `[SLDR-13]`로 12건 있다. 활동 판정에 신뢰도 필터·히스테리시스·보행속도 교차검증을 추가했다는 커밋과 기타(excluded) 누적 시간 전파 작업이 포함된다. `[SLDR-44]`와 그 전후로 iOS CMMotionActivity 동시 발화 매핑 보정, 모션 원천 라벨 디버그 노출, dwell/candidate 메커니즘 제거, 판정 방식 변경 설계 문서가 있다. 추적 공백을 excluded로 분리 누적하는 작업, ON_FOOT 활동의 RUNNING/WALKING 분기, 6월 raw 활동 라벨/신뢰도 UI 표출 테스트와 그 제거도 포함된다.

이슈 키: [SLDR-13], [SLDR-44], [SLDR-30]

- `b53e0a8` (2026-04-21) [SLDR-13] 러닝/걷기/대기 집계 TrackingMovement와 MovementStats 모델 추가
- `d2f9d58` (2026-04-21) [SLDR-13] MotionProvider에 활동 인식 구현 (Android + iOS)
- `f28c92a` (2026-04-21) [SLDR-13] 활동 판정에 신뢰도 필터·히스테리시스·보행속도 교차검증 추가
- `9333342` (2026-04-27) 추적 공백 시간을 excluded로 분리 누적
- `683892e` (2026-04-28) [SLDR-44] 모션 활동 원천 라벨 디버그 노출
- `17dce01` (2026-05-11) [SLDR-30] ON_FOOT 활동을 RUNNING/WALKING 서브 액티비티로 분기

## 8. 세션 stop/pause 분리 및 재개 (16건)

기간: 2026-04~2026-06

커밋 메시지상 4월 말에는 세션 재시작(restartTracking) API 추가, Android/iOS 미종료 세션 클릭 시 재개 다이얼로그 표시, 세션 재시작 시 대기시간 오산 수정이 있다. 6월 24~25일에는 세션 종료 플래그(stopped) 설계 문서, tracking_sessions의 stopped 컬럼 추가(DB v3), stop/pause 분리와 종료 세션 재개 차단, stop/pause 동시 호출 시 플래그 오기록 방지 관련 작업이 있다. 끝자락 구간 집계 제외를 추가했다가 철회하고 종료 시점 마커 스냅샷으로 활동시간을 보존한 흐름, iOS 트래킹 API 변경 대응, Pause 세션의 라이브 표시 전환도 같은 기간에 있다.

이슈 키: [SLDR-30]

- `d107e9a` (2026-04-27) 세션 재시작(restartTracking) API 추가
- `08e341d` (2026-05-07) [SLDR-30] 세션 재시작 시 이전 위치 타임스탬프로 인한 대기시간 오산 수정
- `36d3585` (2026-06-24) tracking_sessions에 stopped 컬럼 추가 (DB v3)
- `237f81e` (2026-06-24) stop/pause 분리 및 종료 세션 재개 차단
- `d99379e` (2026-06-25) 끝자락 집계 제외 철회, 종료 시점 마커 스냅샷으로 활동시간 보존
- `9333918` (2026-06-25) Pause 세션을 라이브 표시로 전환 (Android·iOS)

## 9. Foreground 서비스 및 종료 시 정리·reset (11건)

기간: 2026-04~2026-06

커밋 메시지상 `[SLDR-34]` 아래 Foreground 서비스 Provider/Config expect-actual 추가, TrackingService 제어 메서드 추가, SamsungLifeService 공개 API 노출, 앱 연동과 알림 권한 요청 관련 작업이 있다. POST_NOTIFICATIONS 권한의 앱 모듈 이동, 권한 승인 후에만 서비스를 시작하는 수정, develop 브랜치 머지 커밋 1건이 포함된다. 6월에는 스와이프 종료 시 프로세스 정리, onTaskRemoved 설계/구현 계획 문서, 트래킹·리스너 전체 초기화 reset() API, reset() 시 duration 상태 정리 수정 관련 작업이 있다.

이슈 키: [SLDR-34]

- `8be19a7` (2026-04-22) Foreground 서비스 Provider/Config expect-actual 추가
- `d942879` (2026-04-22) SamsungLifeService에 Foreground 서비스 API 공개
- `24fe825` (2026-04-22) [SLDR-34] 권한 승인 후에만 포그라운드 서비스 시작
- `1267550` (2026-06-18) 스와이프 종료 시 프로세스 정리로 재시작 데이터 잔존 문제 해결
- `4f151ce` (2026-06-18) 트래킹·리스너 전체 초기화 reset() API 추가
- `31d6a7c` (2026-06-22) reset() 시 duration 상태 미정리 문제 해결

## 10. SDK 공개 API 정리 및 세션 삭제 API (18건)

기간: 2026-04~2026-10

커밋 메시지상 5월 초 applicationInit의 initialize 리네임, observeSessions의 getSessionIds 스냅샷 API 전환, observeCurrentMotion 제거와 setUiDataListener 리네임, 리스너 네이밍 개선, setCurrentPointListener 공개 타입의 CurrentPoint 분리 관련 작업이 있다. bindActivity 제거와 startLocationUpdate의 activity 파라미터 추가, startTracking 반환 타입(Long?) 변경 및 원복, iOS 반환값 nil 체크, 미사용 파라미터 제거, samsunglife BuildConfig/isDebugBuild 구현도 같은 계열이다. 2026-10-15에는 SamsungLifeService에 세션 삭제 API(deleteSession) 추가와 데모 앱 Delete 버튼 추가가 있으며, 같은 메시지의 커밋이 서로 다른 해시로 각각 2건씩 기록되어 있다(총 4건).

이슈 키: [SLDR-30]

- `6862d74` (2026-04-30) SamsungLifeService.startTracking Long? 반환 및 불필요한 Dispatcher 래핑 제거
- `6407d4f` (2026-05-06) [SLDR-30] applicationInit을 initialize로 리네임, 디버그 빌드 로그 비활성화
- `d813653` (2026-05-06) [SLDR-30] observeSessions를 getSessionIds 스냅샷 API로 전환
- `10a5fc4` (2026-05-12) [SLDR-30] setCurrentPointListener 공개 타입을 CurrentPoint로 분리
- `aed6833` (2026-10-15) SamsungLifeService에 세션 삭제 API(deleteSession) 추가
- `2869a2f` (2026-10-15) 데모 앱 세션 화면에 Delete 버튼 추가

## 11. SDK 배포·Artifactory·버전·빌드 설정 (20건)

기간: 2026-04~2026-10

커밋 메시지상 JFrog Artifactory AAR 배포 인프라 설정(4월 말)과, 5월 12일 전후 core:common·core:database·core:tracking·samsunglife 모듈별 배포 설정, ProGuard 규칙, Kotlin 메타데이터 보존, 내부 구현 은닉 관련 작업이 있다. useRemoteDeps 플래그, Room DB 버전 1 초기화, Artifactory 저장소 변경, minSdk 24에서 26으로 상향, release 버전 1.0.0·1.0.1·1.0.3 상향이 있다. Android Demo 서브모듈 추가와 포인터 업데이트, 난독화 시 내부 클래스 재패키징 규칙 추가, 로컬 전달용 AAR 빌드 스크립트와 연동 가이드 문서(8월), 10월 Kotlin 2.0.0 / AGP 8.7.1 다운그레이드가 포함된다.

이슈 키: [SLDR-30]

- `42875b4` (2026-04-30) JFrog Artifactory AAR 배포 인프라 설정
- `583e1ea` (2026-05-12) [SLDR-30] SDK 모듈 Artifactory 배포 환경 구성
- `afc442f` (2026-05-13) [SLDR-30] SDK 릴리스 버전 1.0.0으로 올림
- `3fc6333` (2026-06-25) release 버전 1.0.1로 상향
- `76c2fde` (2026-08-20) 로컬 전달용 AAR 빌드 스크립트 추가
- `853a095` (2026-10-15) Kotlin 2.0.0 / AGP 8.7.1 다운그레이드

## 12. SDK 연동 가이드·문서 (15건)

기간: 2026-05~2026-06

커밋 메시지상 삼성생명 SDK 연동 가이드 문서 추가, 세션 조회/삭제·센서 가용성 확인·트래킹 세션 공개 API 문서화, 오픈소스 라이센스 고지 문서 추가 관련 작업이 있다. 5월 14~15일에는 Android Maven 저장소·의존성 추가 가이드, iOS SPM 의존성 추가 가이드, 가이드 PDF 업데이트(한글 폰트 적용, 코드 블록 긴 줄 잘림 수정), SDK 명칭·권한·의존성 정정, 버전 정보 업데이트, ACCESS_COARSE_LOCATION 권한 추가 기재, PDF 현행화가 있다. 6월 25일에는 pause/resume/duration API와 포그라운드 종료 동작을 가이드에 반영한 커밋이 있다.

이슈 키: [SLDR-30]

- `d2f4104` (2026-05-06) [SLDR-30] 배포 가이드 문서용 공개 API 문서화
- `7bf1ec2` (2026-05-07) [SLDR-30] 오픈소스 라이센스 고지 문서 추가
- `be4d990` (2026-05-12) [SLDR-30] 삼성생명 SDK 연동 가이드 문서 추가
- `0ed7ecf` (2026-05-14) [SLDR-30] iOS SPM 의존성 추가 가이드 작성
- `2260cf3` (2026-05-15) [SLDR-30] PDF 가이드 현행화
- `504369a` (2026-06-25) SDK 가이드에 pause/resume/duration API 및 포그라운드 종료 동작 반영

## 13. 샘플 앱 세션 화면 UI 및 걸음수/케이던스 (9건)

기간: 2026-04~2026-05

커밋 메시지상 Compose 빌드 설정과 Compose 기반 세션 화면 구현(ViewBinding 레이아웃 제거), iOS ContentView를 Android SessionScreen 구조로 통일하는 작업이 있다. 세션 목록에 총 시간 표시, 세션 화면에 계산중 상태 표시, 앱 아이콘 및 이름 적용 관련 작업이 있다. 5월에는 Android/iOS 세션 화면 표출 사양 통일, 걸음수/케이던스 데이터 계층과 UI 표시 추가, iOS 재개 다이얼로그 수정이 있다.

이슈 키: [SLDR-8], [SLDR-12], [SLDR-30]

- `ce7d51f` (2026-04-15) [SLDR-8] Compose 빌드 설정 및 의존성 추가
- `e4f7ff5` (2026-04-15) [SLDR-8] Compose 기반 세션 화면 구현 및 ViewBinding 레이아웃 제거
- `edb92e0` (2026-04-16) [SLDR-8] iOS ContentView를 Android SessionScreen UI 구조로 통일
- `07c5367` (2026-04-23) 세션 화면에 계산중인 상태 표시 (Android/iOS)
- `44d7514` (2026-05-07) [SLDR-30] Android/iOS 세션 화면 표출 사양 통일 및 버그 수정
- `ef78d84` (2026-05-13) [SLDR-30] 걸음수/케이던스 데이터 계층 추가

## 14. 모호한 커밋 (2건)

대상 또는 범위를 메시지만으로 특정하기 어려운 커밋이다. 건수는 2건이다.

- `0adf1e1` (2026-07-03) Logger 표출하도록 수정 (어느 모듈·화면의 Logger인지 메시지에 없음)
- `a6bee76` (2026-06-10) Location accuarcy, fresh 필드 추가 (필드 추가 대상 모델이 메시지에 없음)

## 검산

주제별 건수: 20 + 11 + 24 + 6 + 25 + 20 + 22 + 16 + 11 + 18 + 20 + 15 + 9 + 2 = 219

검산: 주제별 건수 합 = 전체 건수 (219 = 219). 스크립트로 모든 해시가 정확히 한 번씩 배정되었음을 확인했다.

## Sources

- 원본 커밋 목록: [[_raw/_archived/Bitbucket_inavi-location_커밋목록_dongeun]] (해시|날짜|메시지)
- 저장소: Bitbucket `mobility-tech/inavi-location`, 필터 `--author` 본인, merge·stash 제외
