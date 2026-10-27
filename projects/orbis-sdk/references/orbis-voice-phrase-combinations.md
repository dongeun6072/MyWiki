---
title: >-
    다국어 음성 발성 조합 (한·영·번체·간체 문구와 조각 키 전체)
category: references
project: orbis-sdk
tags: [voice, i18n, tts, audio-keys, orbis, visibility/internal]
aliases: [다국어 음성 발성 조합]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/826212376
summary: >-
    한국어·영어·번체·간체 음성 안내 문구와 audio_* 조각 키 조합 전체, 회전·카메라·터널 템플릿의 언어별 어순과 치환 키 목록
provenance:
  extracted: 0.90
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T13:00:00+09:00
updated: 2026-10-26T14:30:00+09:00
snapshots:
  - "[[_raw/_archived/다국어+음성+발성+조합.doc|다국어+음성+발성+조합.doc]]"
---

# 다국어 음성 발성 조합

안내 음성 한 문장을 `audio_*` 조각 키의 조합으로 만드는 방식과, 언어별 문구·조각 키 매핑을 정리한 문서(2025-09-22 수정)다. 템플릿 사양은 [[orbis-guidance-engine-dev-spec]], 요약은 [[orbis-guidance-and-voice-spec]], 번역 리소스 관리는 [[orbis-i18n-units-notation-and-translation-resources]], 목차는 [[orbis-design-and-review-hub]].

표기: `/` 뒤가 발성 조각 키 조합이다. 들여쓴 줄(원문의 하위 항목)은 같은 의미의 대안 문구로, 표에서는 "대안" 열에 따로 표시했다. `%d`는 거리 숫자, `%s`는 방면 등 문자열이다.

## 조각 키 의미 (키 이름에서 읽히는 범위) ^[inferred]
`audio_m_a`(N미터 앞), `audio_and`(이어서), `audio_soon`(잠시후), `audio_for_m`(N미터까지), `audio_toward`(방면), `audio_end_road`(도로 끝에서), `audio_right/left`(우/좌회전), `audio_right_way/left_way`(오른쪽/왼쪽 도로), `audio_straight_2`(직진), `audio_u_turn_1`(유턴), `audio_round`(회전교차로), `audio_exit_2`(출구 진출), `audio_gate`(톨게이트), `audio_ramp`(램프/고가), `audio_highway`(고속도로), `audio_paralled`(평행 도로), `audio_arrive_near`(목적지 부근), `audio_waypoint`(경유지).

## 한국어

| 문구 | 조각 키 |
|---|---|
| 약 %d 미터 앞 우회전입니다. | audio_m_a + audio_right |
| 약 %d 미터 앞 좌회전입니다. | audio_m_a + audio_left |
| 약 %d 미터 앞 오른쪽 도로입니다. | audio_m_a + audio_right_way |
| 약 %d 미터 앞 왼쪽 도로입니다. | audio_m_a + audio_left_way |
| 약 %d 미터 앞 직진입니다. | audio_m_a + audio_straight_2 |
| 약 %d 미터 앞 유턴하세요. | audio_m_a + audio_u_turn_1 |
| 약 %d 미터 앞 회전교차로에 진입하세요. | audio_m_a + audio_round |
| 약 %d 미터 앞 출구로 진출하세요. | audio_m_a + audio_exit_2 |
| 약 %d 미터 앞 톨게이트입니다. | audio_m_a + audio_gate |
| 약 %d 미터 앞 고가 도로에 진입하세요. | audio_m_a + audio_ramp |
| 약 %d 미터 앞 고속도로에 진입하세요. | audio_m_a + audio_highway |
| 약 %d 미터 앞 평행 도로에 진입하세요. | audio_m_a + audio_paralled |
| 이어서 약 %d 미터 앞 우회전입니다. | audio_and + audio_m_a + audio_right |
| 이어서 약 %d 미터 앞 직진입니다. | audio_and + audio_m_a + audio_straight_2 |
| 이어서 약 %d 미터 앞 톨게이트입니다. | audio_and + audio_m_a + audio_gate |
| 이어서 약 %d미터까지 직진입니다. | audio_and + audio_for_m + audio_straight_2 |
| 이어서 %s방면으로 우회전입니다. | audio_and + audio_toward + audio_right |
| 이어서 첫번째 출구로 진출하세요. | audio_and + audio_exit_first |
| 이어서 첫번째 우회전입니다. | audio_and + audio_right_first |
| 이어서 목적지 부근입니다. | audio_and + audio_arrive_near |
| 이어서 경유지 부근입니다. | audio_and + audio_waypoint |
| 잠시후 우회전입니다. | audio_soon + audio_right |
| 잠시후 오른쪽 도로입니다. | audio_soon + audio_right_way |
| 잠시후 유턴하세요. | audio_soon + audio_u_turn_1 |
| 잠시후 회전교차로에 진입하세요. | audio_soon + audio_round |
| 잠시후 한시 방향 우회전입니다. | audio_soon + audio_right_one |
| 잠시후 고가 도로에 진입하세요. | audio_soon + audio_ramp |
| 잠시후 목적지 부근입니다. | audio_soon + audio_arrive_near |
| 잠시후 경유지 부근입니다. | audio_soon + audio_waypoint |
| 잠시후 도로 끝에서 우회전입니다. | audio_soon + audio_end_road + audio_right |

## 영문 (English)

| 문구 | 조각 키 |
|---|---|
| After %d meters, Turn right | audio_m_a + audio_right |
| After %d meters, Turn left | audio_m_a + audio_left |
| After %d meters, Keep right | audio_m_a + audio_right_way |
| After %d meters, Keep left | audio_m_a + audio_left_way |
| After %d meters, Continue straight for now | audio_m_a + audio_straight_2 |
| After %d meters, Make a U-turn | audio_m_a + audio_u_turn_1 |
| After %d meters, Enter the roundabout. | audio_m_a + audio_round |
| After %d meters, Take the exit. | audio_m_a + audio_exit_2 |
| After %d meters, Pass through the tollgate. | audio_m_a + audio_gate |
| After %d meters, Take the entrance ramp. | audio_m_a + audio_ramp |
| After %d meters, Take the highway. | audio_m_a + audio_highway |
| After %d meters, Switch to the parallel road. | audio_m_a + audio_paralled |
| Then After %d meters, Turn right. | audio_and + audio_m_a + audio_right |
| Then After %d meters, Continue straight for now. | audio_and + audio_m_a + audio_straight_2 |
| Then After %d meters, Pass through the tollgate. | audio_and + audio_m_a + audio_gate |
| Then For %d meters, Continue straight for now. | audio_and + audio_for_m + audio_straight_2 |
| Then Toward %s, Turn right | audio_and + audio_toward + audio_right |
| Then Take the first exit. | audio_and + audio_exit_first |
| Then Take the first right. | audio_and + audio_right_first |
| Then You have reached your destination. | audio_and + audio_arrive_near |
| Then You have reached your waypoint. | audio_and + audio_waypoint |
| Soon Turn right | audio_soon + audio_right |
| Soon Keep right | audio_soon + audio_right_way |
| Soon Make a U-turn. | audio_soon + audio_u_turn_1 |
| Soon Enter the roundabout. | audio_soon + audio_round |
| Soon Slight right | audio_soon + audio_right_one |
| Soon Take the entrance ramp. | audio_soon + audio_ramp |
| Soon You have reached your destination. | audio_soon + audio_arrive_near |
| Soon You have reached your waypoint. | audio_soon + audio_waypoint |
| Soon At the end of the road, Turn right | audio_soon + audio_end_road + audio_right |

## 번체 (Traditional Chinese)

| 문구 | 조각 키 | 비고 |
|---|---|---|
| %d公尺後 右轉 | audio_m_a + audio_right | |
| %d公尺後 左轉 | audio_m_a + audio_left | |
| %d公尺後 請靠右行駛 | audio_m_a + audio_right_way | |
| %d公尺後 靠左行駛 | audio_m_a + audio_left_way | |
| %d公尺後 請暫時直行 | audio_m_a + audio_straight_2 | |
| %d公尺後 繼續直行 | audio_m_a + audio_straight_3 | 대안 |
| %d公尺後 請迴轉 | audio_m_a + audio_u_turn_1 | |
| %d公尺後 進入圓環 | audio_m_a + audio_round | |
| %d公尺後 請從出口離開 | audio_m_a + audio_exit_2 | |
| %d公尺後 從出口駛出 | audio_m_a + audio_exit_3 | 대안 |
| %d公尺後 通過收費站 | audio_m_a + audio_gate | |
| %d公尺後 進入匝道 | audio_m_a + audio_ramp | |
| %d公尺後 行駛高速公路 | audio_m_a + audio_highway | |
| %d公尺後 切到平行道路 | audio_m_a + audio_paralled | |
| 然後 %d公尺後 右轉 | audio_and + audio_m_a + audio_right | |
| 然後 %d公尺後 請暫時直行 | audio_and + audio_m_a + audio_straight_2 | |
| 然後 %d公尺後 繼續直行 | audio_and + audio_m_a + audio_straight_3 | 대안 |
| 然後 %d公尺後 通過收費站 | audio_and + audio_m_a + audio_gate | |
| 然後 再 %d 公尺 請暫時直行 | audio_and + audio_for_m + audio_straight_2 | |
| 然後 朝 %s 方向 右轉 | audio_and + audio_toward + audio_right | |
| 然後 走第一個出口 | audio_and + audio_exit_first | |
| 然後 第一個路口右轉 | audio_and + audio_right_first | |
| 然後 您已到達目的地 | audio_and + audio_arrive_near | |
| 然後 您已抵達途經點 | audio_and + audio_waypoint | |
| 快到了 右轉 | audio_soon + audio_right | |
| 前方 右轉 | audio_soon_2 + audio_right | 대안 |
| 快到了 請靠右行駛 | audio_soon + audio_right_way | |
| 快到了 請迴轉 | audio_soon + audio_u_turn_1 | |
| 快到了 進入圓環 | audio_soon + audio_round | |
| 快到了 微向右轉 | audio_soon + audio_right_one | |
| 前方 稍向右轉 | audio_soon_2 + audio_right_one_2 | 대안 |
| 快到了 進入匝道 | audio_soon + audio_ramp | |
| 快到了 您已到達目的地 | audio_soon + audio_arrive_near | |
| 快到了 您已抵達途經點 | audio_soon + audio_waypoint | |
| 快到了 在道路的盡頭 右轉 | audio_soon + audio_end_road + audio_right | |
| 前方 道路盡頭 右轉 | audio_soon_2 + audio_end_road_2 + audio_right | 대안 |

## 간체 (Simplified Chinese)

| 문구 | 조각 키 | 비고 |
|---|---|---|
| %d 公尺后 右转 | audio_m_a + audio_right | |
| 前方 %d 公尺 右转 | audio_m_a_2 + audio_right | 대안 |
| %d 公尺后 左转 | audio_m_a + audio_left | |
| %d 公尺后 靠右行驶 | audio_m_a + audio_right_way | |
| %d 公尺后 靠左行驶 | audio_m_a + audio_left_way | |
| %d 公尺后 暂时继续直行 | audio_m_a + audio_straight_2 | |
| %d 公尺后 继续直行 | audio_m_a + audio_straight_3 | 대안 |
| %d 公尺后 掉头 | audio_m_a + audio_u_turn_1 | |
| %d 公尺后 进入环岛 | audio_m_a + audio_round | |
| %d 公尺后 从出口驶出 | audio_m_a + audio_exit_2 | |
| %d 公尺后 通过收费站 | audio_m_a + audio_gate | |
| %d 公尺后 驶入入口匝道 | audio_m_a + audio_ramp | |
| %d 公尺后 驶入匝道 | audio_m_a + audio_ramp_2 | 대안 |
| %d 公尺后 驶入高速公路 | audio_m_a + audio_highway | |
| %d 公尺后 切换到平行道路 | audio_m_a + audio_paralled | |
| 前方 %d 公尺 切换到平行道路 | audio_m_a_2 + audio_paralled | 대안 |
| 然后 %d 公尺后 右转 | audio_and + audio_m_a + audio_right | |
| 然后 %d 公尺后 暂时继续直行 | audio_and + audio_m_a + audio_straight_2 | |
| 然后 %d 公尺后 继续直行 | audio_and + audio_m_a + audio_straight_3 | 대안 |
| 然后 %d 公尺后 通过收费站 | audio_and + audio_m_a + audio_gate | |
| 然后 在 %d 公尺内 暂时继续直行 | audio_and + audio_for_m + audio_straight_2 | |
| 然后 在 %d 公尺内 继续直行 | audio_and + audio_for_m + audio_straight_3 | 대안 |
| 然后 朝向 %s 右转 | audio_and + audio_toward + audio_right | |
| 然后 从第一出口驶出 | audio_and + audio_exit_first | |
| 然后 在第一个路口右转 | audio_and + audio_right_first | |
| 然后 您已到达目的地 | audio_and + audio_arrive_near | |
| 然后 您已抵达途经点 | audio_and + audio_waypoint | |
| 即将 右转 | audio_soon + audio_right | |
| 即将 靠右行驶 | audio_soon + audio_right_way | |
| 即将 掉头 | audio_soon + audio_u_turn_1 | |
| 即将 进入环岛 | audio_soon + audio_round | |
| 即将 稍向右转 | audio_soon + audio_right_one | |
| 即将 稍微右转 | audio_soon + audio_right_one_2 | 대안 |
| 即将 驶入入口匝道 | audio_soon + audio_ramp | |
| 即将 您已到达目的地 | audio_soon + audio_arrive_near | |
| 即将 到达目的地 | audio_soon + audio_arrive_near_2 | 대안 |
| 即将 您已抵达途经点 | audio_soon + audio_waypoint | |
| 即将 到达途经点 | audio_soon + audio_waypoint_2 | 대안 |
| 即将 在道路的尽头 右转 | audio_soon + audio_end_road + audio_right | |
| 即将 到达路的尽头 右转 | audio_soon + audio_end_road_2 + audio_right | 대안 |

한국어·영문 표에는 대안 문구가 없고, 번체·간체에만 `_2`/`_3` 접미사가 붙은 대안 키가 있다(`audio_straight_3`, `audio_exit_3`, `audio_soon_2`, `audio_right_one_2`, `audio_end_road_2`, `audio_m_a_2`, `audio_ramp_2`, `audio_arrive_near_2`, `audio_waypoint_2`).

## 템플릿별 언어 어순과 치환 키

문장은 `.`으로 끊긴 조각 순서로 재생된다. 템플릿의 `%1$d`는 거리, `%2$s`는 단위, `%3$s`(또는 `%s`)는 타입 조각이다.

### [회전]

**1. 약 + 거리(%1$d) + 단위(%2$s) + 타입(%3$s)** — 예: 약 50m 앞 우회전입니다.

| 언어 | 조합 |
|---|---|
| 한국어 | 약. %1$d %2$s. 앞. %3$s. |
| 영어 | %3$s. in %1$d %2$s. |
| 번체 | 大約%1$d%2$s.後%3$s. |
| 간체 | 大约%1$d%2$s.后%3$s. |

- `%2$s`: audio_unit_m, audio_unit_km, audio_unit_mile, audio_unit_feet, audio_unit_yard
- `%3$s`: audio_right, audio_left, audio_right_way, audio_left_way, audio_straight_2, audio_u_turn_1, audio_gate, audio_round, audio_paralled, audio_ramp, audio_highway, audio_exit_2

**2. 이어서 + 약 + 거리(%1$d) + 단위(%2$s) + 앞 + 타입(%3$s)** — 예: 이어서 약 50m 앞 우회전입니다.

| 언어 | 조합 |
|---|---|
| 한국어 | 이어서. %1$d %2$s. 앞. %3$s. |
| 영어 | Then. %3$s. in %1$d %2$s. |
| 번체 | 然後.在大約%1$d%2$s.後%3$s. |
| 간체 | 然后在.%1$d%2$s.后%3$s. |

- `%2$s`: audio_unit_m, audio_unit_km, audio_unit_mile, audio_unit_feet, audio_unit_yard
- `%3$s`: audio_right, audio_left, audio_gate

**3. 이어서 + 타입(%s)** — 예: 이어서 첫번째 출구로 진출하세요.

| 언어 | 조합 |
|---|---|
| 한국어 | 이어서. %s. |
| 영어 | Then. %s. |
| 번체 | 然後.%s. |
| 간체 | 然后.%s. |

- `%s`: audio_exit_right, audio_exit_left, audio_exit_first, audio_exit_second, audio_exit_third, audio_exit_fourth, audio_exit_fifth, audio_exit_sixth, audio_right_first, audio_right_second, audio_right_third, audio_left_first, audio_left_second, audio_left_third, audio_arrive_near, audio_waypoint

**4. 잠시후 + 타입(%s)** — 예: 잠시후 첫번째 출구로 진출하세요.

| 언어 | 조합 |
|---|---|
| 한국어 | 잠시후. %s. |
| 영어 | %s. |
| 번체 | 馬上.%s. |
| 간체 | 马上.%s. |

- `%s`: audio_right, audio_right_way, audio_right_one, audio_right_two, audio_right_four, audio_left_eight, audio_left_ten, audio_left_eleven, audio_round, audio_ramp, audio_arrive_near, audio_waypoint

### [카메라]

**1. 약 + 거리(%1$d) + 단위(%2$s) + 앞에 + 타입(%3$s) 가 있습니다.** — 예: 약 50m 앞에 고정식 과속 단속 카메라가 있습니다.

| 언어 | 조합 |
|---|---|
| 한국어 | 약. %1$d %2$s 앞에. %3$s가. 있습니다. |
| 영어 | %3$s. ahead. in %1$d %2$s. |
| 번체 | 前方%1$d%2$s.有%3$s. |
| 간체 | 前方%1$d%2$s.有%3$s. |

- `%2$s`: audio_unit_m, audio_unit_km, audio_unit_mile, audio_unit_feet, audio_unit_yard
- `%3$s`: setting_camera_fix, setting_camera_mobile, setting_camera_light, setting_camera_light_safety, setting_camera_section, setting_restricted

**2. 잠시후 + 카메라 종류(%s) 가 있습니다.** — 예: 잠시후 고정식 과속 단속 카메라가 있습니다.

| 언어 | 조합 |
|---|---|
| 한국어 | 잠시후. %s 가. 있습니다. |
| 영어 | %s. ahead. |
| 번체 | 稍后.有%s. |
| 간체 | 稍後.有%s. |

- `%s`: setting_camera_fix, setting_camera_mobile, setting_camera_light, setting_camera_light_safety, setting_camera_section, setting_restricted
- 번체에 간체 글자(稍后), 간체에 번체 글자(稍後)가 쓰인 것은 원문 표기 그대로다. ^[ambiguous]

### [터널 / 지하차도]

**1. 잠시후 + 타입(%s) 로 진입하세요.** — 예: 잠시후 지하차도로 진입하세요.

| 언어 | 조합 |
|---|---|
| 한국어 | 잠시후 %s 로 진입하세요. |
| 영어 | Enter. the %s. ahead. |
| 번체 | 稍后.請進入.%s |
| 간체 | 稍後.请进入.%s |

- `%s`: audio_tunnel, audio_underpass

**2. 잠시후 + 타입(%s)입니다. + 주의하세요.** — 예: 잠시후 터널입니다. 주의하세요.

| 언어 | 조합 |
|---|---|
| 한국어 | 잠시후. %s 입니다. 주의하세요. |
| 영어 | %s. ahead. Drive carefully. |
| 번체 | 稍后.有%s. 請注意安全 |
| 간체 | 稍後.有%s. 请注意安全 |

- `%s`: audio_tunnel, audio_underpass

**3. 약 + 거리(%1$d) + 단위(%2$s) + 앞 + 타입(%3$s) 입니다.** — 예: 약 50m 앞 터널입니다.

| 언어 | 조합 |
|---|---|
| 한국어 | 약. %1$d %2$s. 앞. %3$s. 입니다. |
| 영어 | %3$s. in %1$d %2$s. |
| 번체 | 大約%1$d%2$s.後%3$s. |
| 간체 | 大约%1$d%2$s.后%3$s. |

- `%2$s`: audio_unit_m, audio_unit_km, audio_unit_mile, audio_unit_feet, audio_unit_yard
- `%3$s`(원문에는 두 번째 `%2$s`로 오기): audio_tunnel, audio_underpass ^[ambiguous]

## Related
- [[orbis-guidance-engine-dev-spec]] — 안내 시점·거리·도로 타입 규칙
- [[orbis-guidance-and-voice-spec]] — 요약
- [[orbis-i18n-units-notation-and-translation-resources]] — 단위·표기, 번역 리소스 이력
- [[orbis-onesky-translation-process]] — 번역 리소스 생산 절차
- [[orbis-sdk]]

## Sources
- Confluence "다국어 음성 발성 조합" (pageId 826212376) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- [[_raw/_archived/다국어+음성+발성+조합.doc]] — 같은 Confluence 페이지의 내보내기본(2025-06, 본문 동일 계열)
