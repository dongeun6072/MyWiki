---
title: >-
    Orbis 안내 엔진 사양과 다국어 음성·표기 처리
category: concepts
project: orbis-sdk
tags: [orbis-sdk, guidance, tts, i18n, visibility/internal]
aliases: [안내 엔진 개발 사양, 다국어 음성 발성 조합, Onesky 다국어 프로세스, 구글 안내 사양 분석]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[orbis-routing-stack]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/overview
summary: >-
    해외향 Navi SDK의 음성 안내 거리·템플릿 규칙, 카메라 판단, 구글 안내와의 비교, 음성 조각을 조합하는 다국어 방식, 단위·시간 표기, Onesky 번역 프로세스.
provenance:
  extracted: 0.88
  inferred: 0.10
  ambiguous: 0.02
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T12:10:00+09:00
updated: 2026-10-26T12:10:00+09:00
---

# Orbis 안내 엔진 사양과 다국어 음성·표기 처리

[[orbis-sdk]]의 안내(TBT, 음성, 카메라)와 다국어(한국어, 영어, 중국어 번체/간체) 처리 규칙을 한곳에 모았다. 대만 현지 평가에서 지적된 개선점은 [[taiwan-field-evaluation-2025]]에 있다.

## 안내 엔진 개발 사양 (2025-08)

### 음성 안내 거리

| 종류 | 조건 | 템플릿 | 도로 |
|---|---|---|---|
| 턴 "잠시후" | 차기 거리 100m 이내 | `잠시후 + 타입` | 전체 |
| 턴 "이어서" | 잠시후 안내 구간 + 100m 이내의 차차기 | `이어서 + 약 + 거리 + 단위 + 앞 + 타입` | 전체 |
| 턴 500m | 500m(+50m) 이내 | `약 + 거리 + 단위 + 타입` | 전체 |
| 턴 1km | 1000m(+50m) 이내 | 위와 같음 | 고속도로 |
| 카메라 "잠시후" | 100m 이내 | `잠시후 + 카메라 종류가 있습니다` | 전체 |
| 카메라 500m, 1km | 500m(+70m), 1000m(+70m) | `약 + 거리 + 단위 + 앞에 + 종류가 있습니다` | 500m 전체, 1km 고속도로 |

- **턴 코드**: 도로 속성이 바뀌는 직진 코드만 직진으로 취급한다. 경유지는 U턴이 아니면서 링크 ID와 OSM ID가 같은 링크일 때 설정한다.
- **카메라 판단**: TomTom 고정식 카메라와 이동식 카메라 API를 쓴다. 좌표에 가장 가까운 링크에 매칭하고, 경로 링크에 매칭되는 카메라만 검출해 링크 프로젝션으로 위치를 구한다. **이동식은 신뢰도 0.5 이상(최대 1.0)일 때만** 표시한다.

### 구글 안내와의 비교 (2025-08~09)

구글 내비를 분석해 거리별 문구를 비교했다. 구글에는 카메라 안내가 없었다. 구글의 특징은 다음과 같다.

- 진출("1km 앞에서 우측 출구로 진출"), 램프·분기점 진입 안내가 있다. 시작 턴은 300m/600m 같은 거리별로 표현이 다르고, "이어서"는 "그 다음에"로 연결한다. 회전교차로는 몇 번째 출구인지까지 말한다.
- TBT는 기본 화면에서 차기만 보이다가 다음 안내가 필요할 때 차차기를 "다음"으로 표시한다. 아이콘을 누르면 거리와 추천 차로를 보여 주고 음성도 다시 말한다.
- 도로명 + 직진 거리("*도로명*으로 계속 직진, 목적지까지 11km")와 차선 이용 안내가 있다. 정보 없는 도로는 "알 수 없는 도로"로 표시한다.
- 지도 뷰 모드: 별도 설정 대신 "항상 북쪽을 위쪽으로"를 켜면 2D 고정, 끄면 3D가 되며 순수 2D 모드는 없다.

### 아이나비·애플지도 지도 표현 비교

디스플레이 담당 팀과 도로 색상, 지하차도 구분, 테두리 굵기, 회전교차로, 교통정보 선 굵기, 배경(강·산 채도), 고도(힐셰이드), 위성지도, 건물, 랜드마크를 비교했다. 대부분 지도 스타일 변경으로 되고, 힐셰이드와 위성 14레벨은 DP 엔진과 데이터 구조 변경이 필요한 중장기 과제다. 랜드마크 3D 모델은 구축 규모를 보고 투자 여부를 판단한다.

## 다국어 음성 발성 조합 (2025-09)

음성은 통문장 녹음이 아니라 **조각을 이어 붙이는 방식**이다. 예: "약 %d 미터 앞 우회전입니다" = `audio_m_a + audio_right`.

- 조각 종류: 거리 접두(`audio_m_a`), "이어서"(`audio_and`), "잠시후"(`audio_soon`), 방면(`audio_toward`), 방향(`audio_right/left/straight_2/u_turn_1/round/exit_2/gate/ramp/highway/paralled` 등), 출구/회전 순번(`audio_exit_first`, `audio_right_first`...), 도착(`audio_arrive_near`, `audio_waypoint`), 단위(`audio_unit_m/km/mile/feet/yard`), 터널·지하차도(`audio_tunnel`, `audio_underpass`), 카메라 종류(`setting_camera_fix/mobile/light/light_safety/section`, `setting_restricted`).
- 4개 언어(한국어, 영어, 번체, 간체) 템플릿이 각각 있다. 같은 의미라도 언어마다 어순이 달라 순서를 언어별로 정의한다(예: 영어 "%3$s. in %1$d %2$s.").
- 중국어는 같은 뜻에 변형 문구가 둘 이상 있는 경우가 있다(예: `audio_straight_2`와 `audio_straight_3`, `audio_soon`과 `audio_soon_2`). 어느 쪽을 쓸지는 검수에서 정한 것으로 보인다. ^[inferred]
- 번역 리소스 이력: Onesky 초안 → 번역 검수 완료 → 이후 추가 문구(일반 도로, 음성 카메라/회전 템플릿, 터널/지하차도, 모의주행 시 기존 경로 취소, "어디로 갈까요?" → "목적지를 입력해 주세요", 지도 다운로드·엔진 초기화)는 GPT로 번역하고 **검수 전** 상태였다.

## 단위·시간 표기 사양

- 국제 표준을 유지하는 항목(속도 km/h·mph, AM/PM)은 번역하지 않는다. 스크립트에는 `Description`에 "_표준", `Keys`에 "_standard"를 붙인다.
- 중국어 거리 표기: 번체 `500 公尺`, `2.3 公里`, 간체 `500 米`, `2.3 公里`. 예상 시간 `1小時20分鐘`(번체), `1小时20分钟`(간체). 설정의 거리 단위는 한자와 국제 표준을 같이 쓴다(`公里 (km)`, `英哩 (mile)`).

## Onesky 번역 프로세스

1. 구글 스프레드시트로 포맷에 맞게 스크립트를 쓴다. 열은 Description, String Identifier(Keys), 글자 수 제한(선택), 영어(기본, 한국어는 참고용).
2. 문구 작성 규칙: 중복 제거, 값이 들어갈 자리는 `%d`/`%f`/`%s`(같은 종류가 여럿이면 `%1$d`, `%2$d`), 재사용되도록 최소 단위로 분리(원인과 제안 문구를 따로).
3. 키 규칙: `[모듈/화면]_[역할/위치]_[의미]` 순서, 소문자, 짧게. 모듈 예시는 main, search, map/route/drive, place/category, setting, audio, popup, common이고 역할 예시는 label, btn, msg, error, toggle, unit, time이다.
4. Excel로 내려받아 영어 기준으로 한국어도 1차 번역해 교차 검증용으로 두고, Onesky에 업로드한 뒤 열 의미를 매칭한다.
5. 전문가 번역을 선택하고(리뷰어는 선택하지 않음), 톤과 쓰임을 간단히 적어 결제한다. 결제는 법인 결제 수단을 쓰며 세부 정보는 적지 않았다.
6. 번역 완료 후 Excel로 내보내 스프레드시트에 반영하고 검수한다.

## Open Questions

- 구글 안내 분석에서 어떤 항목을 실제 Orbis 안내 사양에 반영했는지는 이 문서들에 명시되어 있지 않다.

## Related

- [[orbis-navisdk-architecture-and-flutter-plan]], [[navisdk-confluence-sprint-timeline-2024-2026]], [[orbis-navisdk-poc-prep-2025]]

## Sources

- [Confluence: 안내 엔진 개발 사양, 구글 안내 사양 분석, 구글 지도 레벨 사양 분석, 다국어 음성 발성 조합, 다국어 내비게이션 단위/표기 사양, 다국어 번역 리소스, Onesky 다국어 관리 프로세스, 아이나비·애플지도 Display 비교 분석](https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/overview) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
