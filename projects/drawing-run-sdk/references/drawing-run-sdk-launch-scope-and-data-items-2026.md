---
title: >-
    드로잉런 SDK 1차 론칭 범위와 데이터 제공 항목 (2026-04, Confluence)
category: references
project: drawing-run-sdk
tags: [drawing-run-sdk, sdk, scope, running-data, permissions, visibility/internal]
aliases: [드로잉런 SDK/API 개발, 1차 론칭 개발 및 데이터 제공 항목, 데이터 제공 관련 검토, 러닝 데이터 항목, SDK 필요 권한]
relationships:
  - target: "[[drawing-run-sdk]]"
    type: related_to
  - target: "[[drawing-run-poc-course-generation-review-2026]]"
    type: derived_from
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/2Ozy8QblnTwf/pages/1837432838
  - url:https://inavisystems.atlassian.net/wiki/spaces/2Ozy8QblnTwf/pages/1854832673
  - url:https://inavisystems.atlassian.net/wiki/spaces/2Ozy8QblnTwf/pages/1855225883
  - url:https://inavisystems.atlassian.net/wiki/spaces/2Ozy8QblnTwf/pages/1855291773
  - url:https://inavisystems.atlassian.net/wiki/spaces/2Ozy8QblnTwf/pages/1865810384
summary: >-
    코스 생성 PoC가 "혼자 달리기" 기록 SDK로 바뀐 개발 계획 변경, 삼성생명과 아이나비의 역할 분담, 러닝 데이터 제공 항목 표와 SDK 가능 여부, iOS/Android 필요 권한과 구현 방법.
provenance:
  extracted: 0.90
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T14:55:00+09:00
updated: 2026-10-26T14:55:00+09:00
---

# 드로잉런 SDK 1차 론칭 범위와 데이터 제공 항목 (2026-04)

[[drawing-run-poc-course-generation-review-2026]]의 PoC가 2026-04-01에 **서비스 론칭용 SDK**로 바뀌었다. 프로젝트 홈(드로잉 런)의 설명은 "사용자가 지도 위에 러닝 코스를 그리고, 따라 달리며 기록을 남기고 공유하는 참여형 러닝 서비스"이고, 이슈 추적은 Jira 프로젝트 `SLDR`에서 한다(링크는 옮기지 않음). 홈 아래의 "Overview" 페이지는 목적과 개발 진행 방향 제목만 있는 빈 틀이다.

## 개발 계획 변경 (2026-04-01 → 04-09 갱신)

| 항목 | 내용 |
|---|---|
| 방향 | 코스 생성 PoC → **서비스 론칭 SDK** |
| 1차 범위 | **혼자 달리기** |
| 1차 스펙 아웃 | **함께 달리기**. 처음에는 "PoC 이후 코스 생성 기능을 활용해 코스 생성·등록"이었으나 04-09 개정에서 **2차 스펙에 포함(7월 말 예상)** 으로 바뀜 |
| 론칭 일정 | 6월 중 (이후 6월 말, 다시 연기. [[drawing-run-sdk-scrum-2026-04-to-05]], [[drawing-run-phase2-voice-guidance-and-meetings-2026]]) |

### 역할 분담

| 삼성생명 | 아이나비시스템즈 |
|---|---|
| 앱 개발, 어드민 개발, 기획·디자인·개발 수행 | 위치기반 솔루션 제공, 사용자 주행 내역 취득과 저장, 주행 경로 이미지 변환 |

04-01 초안은 아이나비 쪽에 코스 트래킹, 주행 중 안내, 완주 여부 판별도 있었으나 취소선으로 빠졌다(2차로 이동).

### 기능 개발 및 제공 항목

| 기능 | 담당 |
|---|---|
| 등록된 코스 호출 | 삼성생명 |
| GPX 데이터 업로드 | 삼성생명 |
| 주행 및 데이터 수집 | SDK |
| 주행 경로 이미지 변환 | SDK |
| ~~주행 중 안내~~, ~~완주 여부 판별~~ | ~~SDK~~ (1차 제외) |

## 데이터 제공 항목과 SDK 판단

| 카테고리 | 항목 (단위) | SDK 판단 | 비고 |
|---|---|---|---|
| 날짜 | 날짜, 시작/종료 시간 | 가능 | |
| 거리 | 총 거리(km), 러닝 거리, 걸은 거리, 상세 경로 | 총 거리·상세 경로 가능, 러닝/걸은 거리는 계산 | |
| 시간 | 총 시간, 러닝 시간, 걷기 시간, 대기 시간 | 총 시간 가능, 나머지 계산 | |
| 칼로리 | 소모 칼로리(kcal) | **조건부** | 임의 계산 또는 헬스 연동 |
| 속도 | 이동 속도(km/h) | 가능 | |
| 페이스 | 평균 페이스(신호 대기 등을 포함한 총 시간 기준), 평균 이동 페이스(실제 달린 시간만), 최고 페이스, 구간별 평균 페이스, 첫 구간 대비 평균 페이스 차이 (시간/km) | 계산 | |
| 랩 | 랩 수(400m 1바퀴 자동), 랩 거리(수동 설정), 랩 타임, 랩 페이스 | 계산 | |
| 걸음 수 | 걸음 수 | 가능(모션 연동) | 04-09 검토 페이지에서 추가 |
| 케이던스 | 최소/최대/평균(SPM) | 모션 연동 또는 헬스 연동 | 분당 180~200회 권장, 초보 160~170대, 숙련 180 이상 |
| 고도 | 고도 상승, 고도 하강, 구간별 고도 변화 (m) | 계산 | 센서가 없는 단말은 N/A 처리 ([[drawing-run-sdk-scrum-2026-04-to-05]]) |

각 항목은 Jira `SLDR-4`~`SLDR-23` 범위의 하위 이슈로 연결돼 있다(예: 날짜 SLDR-12, 총 시간 SLDR-13, 속도 SLDR-14, 페이스 SLDR-15/17/18, 랩 SLDR-19, 케이던스 SLDR-4/5/20/21, 고도 SLDR-22, 칼로리 SLDR-23).

## 필요 권한

| 구분 | iOS | Android |
|---|---|---|
| 위치 | `NSLocationWhenInUseUsageDescription`, 백그라운드 추적 시 `NSLocationAlwaysAndWhenInUseUsageDescription` + `UIBackgroundModes` location updates + `allowsBackgroundLocationUpdates = true` | `ACCESS_FINE_LOCATION`(권장) / `ACCESS_COARSE_LOCATION`, 백그라운드 동작은 포그라운드 서비스 `FOREGROUND_SERVICE`, `FOREGROUND_SERVICE_LOCATION` |
| 모션 | `NSMotionUsageDescription` (걸음 수·케이던스는 필수, 러닝/걷기 구분은 권장) | API 29+ `ACTIVITY_RECOGNITION`, API 28 이하는 Play Services의 같은 이름 권한 |
| 헬스 | HealthKit capability + `NSHealthShareUsageDescription`(읽기), `NSHealthUpdateUsageDescription`(쓰기). **필수 아님** | Health Connect 타입별 권한(`TotalCaloriesBurnedRecord`, `ExerciseSessionRecord`, `StepsRecord` 등). **필수 아님**. 운동 경로 읽기는 별도 취급 |

- Android 백그라운드 위치는 포그라운드 서비스를 누가 관리하는지 정해야 하고, Play 스토어 정책에 따라 사용 사유 제출이 필요할 수 있다.
- 항목별 필요 권한: 날짜·거리·경로·속도·페이스·랩은 위치만, 러닝/걷기/대기 구분은 위치+모션, 걸음 수·케이던스는 모션 필수, 고도는 위치로 가능(iOS는 `verticalAccuracy > 0`일 때만 유효, 기압계를 쓰면 모션 권한), 칼로리는 헬스 연동.

## 구현 참고 (iOS / Android)

| 항목 | iOS | Android |
|---|---|---|
| 시간·날짜 | 세션 시작/종료를 앱에서 기록, 필요 시 HKWorkout | 세션 시작/종료를 앱에서 기록, 필요 시 ExerciseSessionRecord |
| 총 거리 | CLLocation 누적 | Fused Location 연속 업데이트 누적(보조로 DistanceRecord) |
| 러닝/걷기 분리 | CMMotionActivity의 walking/running과 GPS 구간 결합 | Activity Recognition WALKING/RUNNING과 GPS 구간 결합 |
| 칼로리 | HealthKit workout 통계의 activeEnergyBurned (`HKWorkout.totalEnergyBurned`는 iOS 16에서 deprecated) | Health Connect의 Active/Total CaloriesBurned |
| 속도 | `CLLocation.speed` | Location 속도 또는 SpeedRecord |
| 평균 이동 페이스 | 이동 시간 ÷ 이동 거리, 대기 구간 GPS 드리프트 거리 제외 | 동일 |
| 최고 페이스 | 짧은 window의 최고 속도 기준 | 동일 |
| 구간 페이스·랩 | 400m/1km 분할, 거리 임계값 자동 랩 | 동일 |
| 걸음 수·케이던스 | `CMPedometer`, `isCadenceAvailable()` 확인 후 `currentCadence` 집계 | `TYPE_STEP_COUNTER`/`TYPE_STEP_DETECTOR` 또는 StepsCadenceRecord |
| 고도 | `CLLocation.altitude` + `verticalAccuracy` 검증, 세밀한 변화는 `CMAltimeter.relativeAltitude` | `Location.altitude` + 검증, 필요 시 ElevationGainedRecord |

## 고객사 문의와 결정 (04-09)

- **지도는 삼성생명이 그리는 것으로 결정**됐다. 그래서 통합 SDK의 지도 UI 형태(액티비티 vs View/Fragment) 질문은 취소선 처리됐다.
- 권한을 **앱(모니모)에서 받을지, SDK가 받을지**와 **위치 정보를 앱이 취득해 SDK에 넘길지(SDK는 처리만) / SDK가 시스템 위치에 직접 접근할지**는 이후 회의에서 "앱에서 확인"으로 정리됐다 ([[drawing-run-sdk-scrum-2026-04-to-05]]).
- 04-01에 남은 확인 항목: 연동 구간 좌표 정보의 **통신 구간 암호화 규격(ARIA?)**, 삼성생명이 만든 GPX에 **안내 정보를 넣는 방법**(예: 주행 시 각도 계산).
- 2차 론칭 문의: 추가 기능 목록, 안내정보 포함 코스 생성 PoC 진행 여부, 예상 일정.

## Sources

- [Confluence: 드로잉런 - SDK/API 개발](https://inavisystems.atlassian.net/wiki/spaces/2Ozy8QblnTwf/pages/1837432838), [1차 론칭 개발 및 데이터 제공 항목](https://inavisystems.atlassian.net/wiki/spaces/2Ozy8QblnTwf/pages/1854832673), [[개발] 데이터 제공 관련 검토](https://inavisystems.atlassian.net/wiki/spaces/2Ozy8QblnTwf/pages/1855225883), [삼성생명 드로잉 런(스페이스 홈)](https://inavisystems.atlassian.net/wiki/spaces/2Ozy8QblnTwf/pages/1855291773), [Overview](https://inavisystems.atlassian.net/wiki/spaces/2Ozy8QblnTwf/pages/1865810384) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음. Jira와 개발자 문서 링크는 옮기지 않음
