---
title: >-
    드로잉런 SDK 연동 질의응답 2026
category: references
tags: [drawing-run-sdk, sdk, integration, qna, android, ios, visibility/internal]
aliases: [드로잉런 연동 이슈, pause resume 사양, 프로가드 kermit]
relationships:
  - target: "[[projects/drawing-run-sdk/drawing-run-sdk]]"
    type: derived_from
  - target: "[[projects/drawing-run-sdk/references/drawing-run-sdk-release-history-2026]]"
    type: related_to
summary: >-
    고객사(삼성생명)가 SDK 연동 중 낸 문의와 대응: 일시정지/재시작 사양, 경과시간 리스너, 난독화 규칙, 포그라운드 서비스, iOS 위치 수신, 버전 요건, 데이터 항목 문의.
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
  - "slack:#011_삼성생명_드로잉런_dev"
---

# 드로잉런 SDK 연동 질의응답 2026

[[projects/drawing-run-sdk/drawing-run-sdk]]의 1.0.0 이후 고객사 연동 단계에서 나온 문의를 주제별로 모았다. 배포 버전은 [[projects/drawing-run-sdk/references/drawing-run-sdk-release-history-2026]], 채널 연표는 [[projects/drawing-run-sdk/references/drawing-run-slack-dev-channel-2026]]. 문의 대부분은 고객사 앱이 **웹뷰 기반 네이티브 웹앱**이라는 점에서 나왔다.

## 일시정지·재시작 (1.0.1, 06-25)

- 06-05 요청: 시작 → 일시정지 → 재시작 → 종료, 일시정지 횟수 제한 없음, 종료 시 일시정지 구간을 제외한 데이터와 코스를 만들고 "총 주행 시간(시작~종료)"과 "일시정지 시간"을 따로 준다.
- 06-16 모의 위치로 테스트한 고객사가 이슈를 냈다. 기존 가이드는 일시정지에 `stopTracking`을 쓰게 했는데, 1분 뒤 `restartTracking`을 하면 거리가 일시정지 시점(0.26km)이 아니라 계속 움직인 만큼(0.45km) 누적됐다.
- 06-23 확정 사양: `pause` 추가, `restart`를 `resume`으로 변경, `stop`은 기존과 같되 stop 후 resume은 동작하지 않음, 총 거리와 UI 거리는 **움직인 구간만 누적**. 동작 순서가 `start → pause → resume → stop`으로 명확해졌고 기존 안내(`start → stop(pause) → restart → stop`)를 정정해야 했다.
- 07-22 문의: `pause` 후 `resume` 없이 바로 `stop`을 호출해도 SDK 내부에 문제가 없는지. 고객사 테스트에서는 결과 수신에 문제가 없었다.
- 일정 방침(06-18): 요구가 정리되면 개별 배포 대신 별도 일정을 세워 한 번에 배포한다.

## 경과시간·실시간 값

- 06-17 요청: 현재까지 경과시간(`durationMillis`)만 0.5~1초 단위로 주는 리스너. 웹뷰에서 직접 계산하면 앱 종료/재시작 때 동기화가 어긋나므로 SDK가 값을 주길 원했다. 1.0.1에서 1초 단위 리스너가 추가됐다.
- 06-18 확인: 러닝/워킹 거리는 `uiData`의 `movement.runningDistanceMeters`, `movement.walkingDistanceMeters`를 쓰면 되는지.
- 05-13 테스트 문의: 데이터의 "기타 시간"이 항상 0이고 걸음 수가 "-"로 나온다. 걸음 수는 권한(모션) 요건과 연결된다 → [[projects/drawing-run-sdk/references/drawing-run-sdk-launch-scope-and-data-items-2026]].

## Android 포그라운드 서비스

- 트래킹 중 앱이 종료돼도 포그라운드 서비스(FGS)로 수집이 이어진다. 고객사는 앱 재시작 시 리스너로 들어오는 데이터를 UI에 반영한다.
- 06-18 문제: OS가 FGS를 간헐적으로 죽일 수 있어, **FGS가 떠 있는지**와 **트래킹 중인지**를 앱 시작 시 확인할 API(예: `isRunningForegroundService()`, `isTracking()` 형태)를 요청했다.
- 06-23 상태: "앱 종료 시 FGS와 트래킹도 종료"하는 요구는 미결정이었고, 기존 사양을 유지하면 요구 확인과 추가 개발이 필요하다고 정리했다.

## 난독화·배포 빌드

- 06-19: 난독화 적용 후 트래킹을 시작하면 `touchlab/kermit` 로거의 정적 메서드를 찾지 못한다는 오류가 났다. 해당 라이브러리에 대한 **프로가드 규칙**이 필요하다는 요청이었다.
- 06-24: 서명·난독화된 aab를 Play 콘솔 내부 테스트로 설치하면 10~20초 뒤 앱이 강제 종료된다. 서명·난독화한 APK를 직접 설치하면 재현되지 않고, 이전 릴리스 버전을 올린 경우에도 없었다.

## iOS 위치 수신

- 07-02: 샘플 앱에서는 위치·point 리스너가 정상인데 더헬스 앱에서는 리스너가 데이터를 받지 못하고 30초 걷고도 `totalDistanceKm`이 0이었다. 위치·모션 권한은 모두 허용된 상태에서 SDK 위치 수신에 필요한 조건을 물었다.
- 07-03 **iOS 1.0.2**: 백그라운드 스레드에서 SDK를 호출하면 위치 콜백이 오지 않는 문제를 고쳤다(개발 가이드 변경 없음). 앞선 문의의 원인으로 보이나 채널에서 직접 연결해 확인하진 않았다. ^[inferred]
- 10-15: 제공 SDK의 iOS 버전에서 `startTracking` 반환값이 오지 않는다는 문의. 고객사 개발자의 SDK 이해가 부족해 보여 간단한 가이드를 요청하는 내용이었다.

## 빌드 도구 버전 (10-13)

고객사가 SDK를 모니모 앱에 이식하려는데 최소 스펙이 Kotlin 2.0.0 / AGP 8.7.1이다. 전달한 SDK는 Kotlin 2.2.0 / AGP 8.11.2였다. 버전을 낮춰 재빌드할 수 있는지 검토가 요청됐다(회신은 채널에 없음). 같은 이유로 SDK의 최소 요건(Android minSdk 26, iOS 15)은 스크럼 회신에서 이미 정해졌다 → [[projects/drawing-run-sdk/references/drawing-run-sdk-scrum-2026-04-to-05]].

## 그 외 문의

| 날짜 | 문의 | 비고 |
|---|---|---|
| 04-20 | 고도: 기압 센서가 없는 단말(구형 iPhone, 일부 갤럭시 A시리즈)은 상대 고도를 못 구함. GPS 고도는 부정확 | 센서가 없을 때 표출 방식은 고객사 결정 사항 |
| 04-20 | 랩 페이스 단위: 속도(km/min)가 아니라 페이스(초/km)로 제공해야 앱에서 분'초"로 변환하기 쉬움(400m 랩 2분 8초 → 320초/km → 5'20") | 러닝 앱은 순간 속도보다 평균 페이스를 보여줌 |
| 05-20 | 라이선스 인증 횟수를 아이나비가 집계·통계로 볼 수 있는지 | 키 값은 미수록 |
| 06-09 | SDK가 수집한 위치가 고객사 서버와 통신 없이 기기 안에서만 처리되는지 | 개인정보 확인 |
| 07-20 | 도보/자전거 경로선형이 데이터에 포함되고 주행 좌표에 매칭 보정되는지, 도보 속도 상한(예: 30km/h 초과 구간 제외) 처리, 구간·시간별 주기 전달 | 채널에서 회신은 확인되지 않음 |

## Sources

- 슬랙 `#011_삼성생명_드로잉런_dev`(2026-04~10). 라이선스 키·서버 정보 미수록.
