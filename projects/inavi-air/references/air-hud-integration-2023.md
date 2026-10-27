---
title: >-
    아이나비 에어 HUD 연동 (2023): Bluetooth 라이브러리, 시리얼 정책, 1차 시험
category: references
tags: [inavi-air, hud, bluetooth, qa, visibility/internal]
aliases: [iHUD 연동, HUD BT 라이브러리, HUD S/N 정책, 에어 HUD]
relationships:
  - target: "[[inavi-air-feature-history]]"
    type: related_to
sources: [~/Develop/Wiki/_raw/articles/Outlook_2023.md]
summary: >-
    2023-08~12월 아이나비 에어와 HUD 단말을 BLE로 잇는 작업의 요구 사양(라이브러리 형태, 기능 목록), 외주 선정과 일정, HUD 시리얼 번호 체계, 1차 시험 결과(통과율 77.4%)를 정리했다.
provenance:
  extracted: 0.88
  inferred: 0.12
  ambiguous: 0.00
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T10:02:28+09:00
updated: 2026-10-26T15:30:00+09:00
snapshots:
  - "[[_raw/_archived/Outlook_2023|Outlook_2023]]"
  - "[[_raw/_archived/HUD 랜덤 값(221115).xlsx|HUD 랜덤 값(221115).xlsx]]"
---

# 아이나비 에어 HUD 연동 (2023)

아이나비 에어 앱이 **HUD 단말(iHUD)** 에 길안내 정보를 Bluetooth(BLE)로 보내는 기능이다. 2022년에는 HUD 규격 정리와 샘플 앱을 만들었고([[inavi-air-feature-history]]), 2023년 8월부터 **BLE 연동 라이브러리를 외주로 개발**하고 11월에 앱에 적용했다. 시리얼 인증 API는 [[inavi-air-api-detail-spec]]의 `/authSerialNumber`다. [[이동은]]은 같은 해 11월 "HUD 연동 적용"을 맡았다. 담당자와 외주사 직원 이름은 적지 않았다.

## 결정 경과

| 시기 | 내용 |
|---|---|
| 2023-08-17 | HUD 연결과 데이터 전송 라이브러리 개발 요구를 정리. 업체 후보 중 EMG는 리소스 문제로 제외, **로드피아 또는 아이앤소프트**로 진행. 두 업체 모두 개발 1.5개월 + 테스트·안정화 1개월 예상. 에어 업데이트로 **11월 중순** 목표 |
| 08-29 | 로드피아 재견적(HUD Bluetooth 라이브러리 개발계획)을 받고 **수요일부터 개발 시작** |
| 09-08 | 개발 Kick-off: 라이브러리 설계 내용 리뷰와 요구사항 조정 |
| 09-12 | 아이나비 Class 문서와 데이터 매핑 문서 전달. 규격상 **점등/소등 항목의 사양(시나리오)** 이 필요하다고 요청 |
| 10-10 | HUD 개발 단말 수급: 개발용 2대 필요. 단말 `TN202`가 전달됐고 `QR220` 2대를 추가 요청 |
| 12-07 | **1차 시험 결과**(QA) |
| 12-14 | 이슈 리뷰 회의. 2차 시험에서는 Android Auto, CarPlay와 BT **오토 페어링** 검증 |

## 라이브러리 요구 사양 (아이나비 → 외주사)

| 항목 | 내용 |
|---|---|
| 배포 형태 | Android `aar`, iOS `xcframework` |
| 대상 OS | Android targetSdk 33 / minSdk 23, iOS 13 |
| 기능 | BLE 권한 요청, BLE On/Off(iOS는 BT 설정 페이지 요청, Android는 On/Off), **BLE 스캔**(스캔 리스트 콜백, 선택), 스캔 중지, **연결**(자동 연결, 스캔 리스트에서 선택), 연결 끊기, 연결 상태 확인, **HUD 데이터 전송**(초 단위), BLE 응답 콜백 |
| 추가 산출물 | 연동 규격서(권한, API), 연동 샘플 코드 |

외주 iOS 개발자의 분석: 앱이 1초마다 `NaviHudData`를 받고, 각 메시지(① TBT ② 안전운전 ③ 거리/평균속도 ④ 속도 ⑤ Status)를 **200ms 단위**로 보내야 한다고 이해했다. ①②는 한 번에 전달하고 ③~⑤는 각각 우선순위가 있어 보여, 우선순위(TBT 코드 → 안전운전 코드 → 구간단속 평균속도와 남은 거리 → 제한속도와 현재 속도 → GPS 상태 점멸)를 아이나비에 확인했다.

## HUD 시리얼 번호 정책

- 형식 **10자: TYPE / 랜덤 / 순번**. TYPE은 `IHA`(상용), `IHT`(테스트용)
- HUD 앱의 시리얼 입력이 숫자만 가능했는데 영문이 포함되므로 **영문 입력 허용, 10자 제한**으로 수정 요청
- HUD 랜덤 값 7,000개(3001~10000)를 엑셀로 전달. 인증 API에는 아직 검사 로직이 없고 필요 시 추가할 수 있다. 앱 키 연동 인증은 별도 협의
- 에어에 시리얼 번호를 전달하는 방법도 요청사항으로 정리 필요

## 1차 시험 결과 (2023-12-07, SW 개발 완성도)

| 플랫폼 | 전체 | PASS | FAIL | N/T | N/A | 통과율 | 커버리지 |
|---|---|---|---|---|---|---|---|
| iOS | 96 | 77 | 17 | 2 | 46 | 80.2% | 97.9% |
| Android | 161 | 122 | 33 | 6 | 123 | 75.8% | 96.3% |
| 합계 | 257 | 199 | 50 | 8 | 169 | **77.4%** | 96.8% |

- 열린 이슈 21건. 사양 검토 요청과 미처리 이슈가 많아 12월 14일 오전에 이슈 리뷰 후 시험을 이어 가기로 했다.
- 2차 발행 일정과 AA/CarPlay 검증이 남았다.

## 연결

- 12월 5일 Android Auto 로그 저장용 APK(`InaviAir 03.05.33`)가 전달됐다. 주행 화면에서 **전체 경로를 선택하면 로그가 저장되고 종료**되는 방식이다. ([[inavi-2023-mail-overview]])
- HUD 데이터에는 TBT, 안전운전(과속 카메라), 구간단속 평균속도가 들어간다. 과속 카메라 종류 확장은 [[air-map-data-and-safety-guidance-2023]]와 연결된다. ^[inferred]

## Open Questions

- 점등/소등 시나리오 사양의 확정 내용과 2차 시험 결과는 메일에 없다.

## 규격 문서와 시리얼 랜덤 값 (보강)

- HUD로 보내는 데이터 클래스, 코드표, Bluetooth 전문 매핑, 2025 TBT 이미지 라이브러리 계획은 [[air-hud-data-class-and-bluetooth-spec]]에 정리했다.
- 시리얼 정책의 "랜덤 값 7,000개(3001~10000)" 엑셀(2022-11-15 작성)은 `TYPE / 랜덤 / 순번` 3열 구조로 7,000행이며, 랜덤 값은 영문 2자와 일련번호 조합이다. 실제 값은 옮기지 않는다.
- 2025-03 외주 제안(아이허드 라이브러리)은 BLE 데이터 전송에서 한 걸음 나아가 TBT 이미지 전송을 다룬다. ([[air-image-hud-review-2025]])

## Sources

- [[_raw/_archived/Outlook_2023.md]] — 2023 업무 메일
- [[_raw/_archived/HUD 랜덤 값(221115).xlsx]] — 시리얼 랜덤 값 표(값 미수록)
