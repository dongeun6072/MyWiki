---
title: >-
    지도 흑화(검은 화면)와 앱 전환 생명주기
category: concepts
tags: [android, opengl, lifecycle, map, visibility/internal]
aliases: [Where 흑화, 지도 흑화, EGL 컨텍스트 손실, 블랙스크린]
relationships:
  - target: "[[mxi-field-incidents-2022]]"
    type: derived_from
sources: [~/Develop/Wiki/_raw/articles/Outlook_2022.md]
summary: >-
    Android 내비 앱의 지도가 검게 나오는 흑화 현상의 재현 시나리오와 대응 방법(EGL 컨텍스트 유지, FG 전환 알림, onResume 점검, 뷰모드 재적용). 2022 MXI 사례에서 정리했다.
provenance:
  extracted: 0.55
  inferred: 0.45
  ambiguous: 0.00
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T09:40:56+09:00
updated: 2026-10-26T09:40:56+09:00
snapshots:
  - "[[_raw/_archived/Outlook_2022|Outlook_2022]]"
---

# 지도 흑화(검은 화면)와 앱 전환 생명주기

2022년 MXI와 아트뷰 단말에서 반복된 **"지도가 검게 나오는" 현상**과 대응이다. 단말·장애 이력은 [[mxi-field-incidents-2022]], 엔진 배포는 [[hybrid-navi-engine-releases-2022]], 제품 전체는 [[inavi-hybrid-navi]]다.

## 재현 시나리오 (고객사 콜앱 개발자 정리)

1. 콜앱에서 **Where를 호출**한다. Where는 이미 실행된 상태이고 BG에서 FG로 올라오려는 중이다.
2. 그 시점에 콜앱이 **새 콜이나 메시지를 받아 다시 FG로** 올라오고, Where는 BG로 내려간다.
3. 다시 콜앱에서 Where로 들어오면 **검은 화면**이다.

다른 제품(Where를 쓰는 2년 이상 납품 제품)에서는 접수되지 않았다. 콜앱처럼 호출 직후 FG가 뒤집히는 서비스 시나리오가 없었기 때문이다. 고객사 분석: Where가 처음 구동될 때보다 `onStart`/`onResume`에서 처리하는 코드가 도는 중에 `onPause`/`onStop`이 오면 발생하는 것 같다는 추정이다. 콜 수신 횟수가 늘어난 앱 버전 이후 더 자주 발생했다.

## 대응 방법 (2022)

| 방법 | 내용 |
|---|---|
| **EGL 컨텍스트 보존** | DP 엔진 v0.0.9c에서 `setPreserveEGLContextOnPause` 옵션을 적용 (06-03). OpenGL ES 컨텍스트가 BG 전환 때 사라지는 것을 막는 설정이다. ^[inferred] |
| **FG 전환 알림** | 내비가 FG로 올 때 **Broadcast**(`naviresume`)를 보내 콜앱이 타이밍을 알도록 했다. 콜앱 버튼이 느리게 표시되는 문제와도 연결된다. |
| **`onResume` 점검 로그** | 임시 앱에 `onResume`이 정상 동작하는지 확인하는 테스트 로그를 넣고, 재현 시 로그를 달라고 요청 |
| **통신 ↔ 비통신 전환 시 지도 갱신 로직** | 흑화 등 지도 갱신 로직을 개선(05-31 action item, DP 엔진으로 배포) |
| **뷰모드 재적용** | 3D 회전뷰 설정이 2D로 바뀌는 현상은 "타이밍상 뷰모드 변경이 안 된 경우"로 보고, 안내 시작 같은 시점에 뷰모드를 다시 적용하도록 보완 |

10월에 흑화가 접수된 아트뷰 단말에는 위 DP 엔진을 포팅내비에 다시 반영해 발행했다.

## 일반화

- **다른 앱이 계속 FG를 뺏는 환경**(콜앱, 런처 위에서 도는 내비 앱 등)에서는 앱 상태가 "FG 진입 직후 BG 복귀"로 흔들린다. 지도 SDK와 GL 표면은 그 순간 복원 로직이 완료되지 않을 수 있다. ^[inferred]
- 대응은 ① 컨텍스트 손실을 막는 설정 ② 생명주기 콜백 안에서 하는 일을 줄이고 멱등하게 만들기 ③ 외부 앱과 FG 전환 신호 주고받기 ④ 재현 로그 수집 순서로 정리할 수 있다. ^[inferred]
- 같은 팀의 이후 SDK 작업(해외향 Navi/Maps SDK)에서도 앱 전환과 재진입은 확인 항목이다. ([[orbis-sdk]]) ^[inferred]

## Open Questions

- 흑화가 최종적으로 해소됐는지는 메일에 없다(11월에도 ANR 건이 이어짐). ANR은 흑화와는 별개 원인(UI 스레드 차단)으로 분석됐다.

## Sources

- [[_raw/_archived/Outlook_2022.md]] — 2022 MXI 관련 메일
