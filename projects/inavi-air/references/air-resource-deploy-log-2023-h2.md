---
title: >-
    에어 리소스 배포 메모 2023 (9월~12월)
category: references
project: inavi-air
tags: [inavi-air, resource-deploy, myplace, hud, visibility/internal]
aliases: [2023.09.05, 2023.09.25 리소스 용량 개선, 2023.10.17, 2023.11.21, HUD & SKP 연동, 서비스 안정화(리소스)]
relationships:
  - target: "[[inavi-air]]"
    type: related_to
  - target: "[[inavi-air-feature-history]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/230359041
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/232783873
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/232849409
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/232849748
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/243531847
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/260046849
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/263028737
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/256311297
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/257064961
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/258834433
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/259293185
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/265388033
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/268369921
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/269025322
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/270270465
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/271384577
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/282918913
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/283443262
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/283771280
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/296845313
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/282919040
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/296615938
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/282853405
summary: >-
    2023-09-05 ~ 2023-12-12 날짜 제목 페이지 20여 건과 HUD&SKP 연동·서비스 안정화 표의 리소스 항목(안전운전 심볼 숫자, 내 장소, 에어퀴즈, HUD 연동, 용량 30% 개선 등).
provenance:
  extracted: 0.90
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T13:00:00+09:00
updated: 2026-10-26T13:00:00+09:00
---

# 에어 리소스 배포 메모 2023 (9월~12월)

2023년 9월~12월의 리소스 배포 메모다. 9월에는 숫자(속도·안전운전 심볼) 수정과 리소스 용량 30% 개선, 10~11월에는 "내 장소"와 에어퀴즈, 11월 말에는 HUD & SKP 광고 연동 리소스가 중심이다. 앞 기간은 [[air-resource-deploy-log-2023-h1]], 이후는 [[air-resource-deploy-log-2024-2026]]이다. HUD 연동 배경은 [[air-hud-integration-2023]], 스크럼은 [[air-hud-and-stabilization-scrums-2023-12]].

## 2023-09-05 — 리소스 수정 및 파일 구분
원문은 "기존 리소스 수정" 아래에 플랫폼별 수정 대상을 한 번에 나열했다(파일 링크는 원본에 있음, 미수록).
- 에어 공통: airre_tooltip_onair(.json), airre_airlab_trafficlights_img
- 바텀시트/리스트 배지: airre_bottomsheet_badge_goal, _newroute, _no01~no03, _start / airre_list_badge_no01~no05 / airre_list_ico_goal, _ic, _jc, _pathway, _start, _tg
- 그룹 순위: airre_group_list_rank01~rank10, airre_mappin_group_rank01~10 각 _n/_s
- 지도 핀: airre_map_goal, airre_map_pathway_01~03, airre_map_start, airre_map_warning_pedestrian
- iOS only: airre_btn_go_coupon_n/p, airre_btn_go_shop_n/p
- 안전운전: inv_map_safe_pin_17, inv_map_safe_pin_23, inv_map_safe_sign_bg00/01/04/05/06/09/10/11/13/17/18/21/26/29/30_tm
- 목록 선택 버튼: inv_listsel_btn_home_n/p, inv_listsel_btn_office_n/p (aos@xhdpi), inv_listsel_btn_bookmark_n/p (ios only), inv_listsel_btn_location_n/p, inv_listsel_btn_plus_n/p (aos only)
- 번호 핀(aos@xhdpi): inv_map_num_pin_n_01~20, inv_map_num_pin_s_01~20
- 전기차 충전 아이콘(aos@xhdpi): tkl_listsel_ic_evc_ac_slow, ac_three_phase, dc_chademo, dc_combo 각 _disabled/_normal
- Auto: airre_auto_close_bg, airre_auto_close_n, airre_auto_close_p
- Carplay: airre_car_map_pathway_01~03

## 2023-09-07 / 07B / 07C — 숫자(속도, 안전운행 심볼) 수정
- 09-07 [공통]: inv_inputlist_mt_n/p, inv_map_1tap_bt_po_n/p
- 09-07 [aos_xxhdpi only]: inv_map_safe_sign_n00~n10_tm, inv_map_safe_sign_o00~o10_tm
- 09-07 [ios]: inv_map_ms_no00~no09, inv_map_num_l_0~9 의 _g 및 _gn (각 10쌍)
- 09-07B: 숫자 "1" 수정 — inv_map_ms_no01, inv_map_num_b_1_tm, inv_map_num_l_1_g, inv_map_num_l_1_gn, inv_map_num_l_1_n_tm, inv_map_num_l_1_tm. 에어연구소 수정 — airre_airlab_basicoption_img_01~07
- 09-07C: inv_map_safe_sign_n08_tm, n09_tm, n10_tm, o08_tm, o09_tm, o10_tm

## 2023-09-25 — 리소스 용량 개선
- 1차 목표: 기존 대비 30% 용량 줄이기 — 9/25 완료
- 2차 목표: 배포 전 해상도별 이미지 Anti-aliasing 확인 — 테스트 중

## 2023-10-17 — 내 장소 리소스 추가 + 기존 수정
- 기존 리소스 수정: inv_listsel_ic_share_n/p, inv_map_ic_go_n/p, inv_list_ic_pin_n/p, inv_ico_lc77 ~ inv_ico_lc95
- 내 장소 추가: airre_bg_delete_numbers, airre_btn_mymap_n/p, airre_btn_myplace_more_n/p, airre_btn_myplace_plus_n/p, airre_icon_maincard_airlab, airre_icon_maincard_cctv, airre_icon_myplace, airre_icon_myplace_more, airre_icon_myplace_home, airre_icon_myplace_location, airre_list_icon_search, airre_mapbtn_plus_n/p, airre_mymap_marker_large, airre_mymap_marker_small_n/p, inv_listsel_ic_share_n/p, inv_list_ic_pin_n/p, inv_map_ic_go_n/p
- 10-17B: 기존 수정 — inv_map_ic_loc, inv_map_ic_regist_n/p, tkl_ic_arrival_distance, tkl_map_ic_time. 내 장소 추가 — airre_bt_myplace_n/p, airre_list_icon_recentplace, airre_mapbtn_close_day

## 2023-10-19 / 10-19B,C
- 10-19: 색상 수정 — tkl_ic_arrival_distance, hbl_destination_km_ic(ios), tkl_map_ic_time. 내 장소 추가 — airre_list_drag-drop_handle, airre_unablebar_round_l (9.patch)
- 10-19B/C: 삭제 — airre_list_pin. 내 장소 추가 — airre_list_pin_on/off, airre_recentplace_empty_img, airre_unablebar_round_r (9.patch)

## 2023-10-20 — 내 장소 리소스 추가
- airre_card_check_blank_n/s, airre_maincard_s_bg (9.patch)

## 2023-10-26 — 색상·디자인 수정 및 에어퀴즈
- 기존 수정: inv_main_card_ic_poi, inv_map_num_pin_n_01~20, inv_map_num_pin_s_01~20
- 에어퀴즈 리소스 추가: airre_maincard_survey_bg (9.patch), airre_maincard_survey_btn, airre_maincard_survey_img, airre_maincard_survey_label (에어퀴즈 설문 배경은 [[air-confluence-scrum-and-voice-2023-2024]]도 참고)

## 2023-11-01 — 내 장소 이름 변경 팝업, 미사용 리소스 삭제
- 추가(이름 변경 팝업): airre_sys_delete_02_n/p
- 기존 미사용 삭제: airre_aircash_btn_drive_record, airre_airlab_coin, airre_airlab_forbid, airre_airlab_trafficlights, airre_airlab_more, airre_bt_cctv_n/s, airre_icon_cash, airre_icon_point, inv_main_card_ic_poi(aos_drawable-hdpi/xxhdpi/xxxhdpi), inv_pin_me(aos_drawable-hdpi/xxhdpi/xxxhdpi)
- iOS 사용 중(삭제 보류): airre_mapbtn_all_n/p, airre_mapbtn_back_n/p, airre_mapbtn_gasstaion_n/p(원문 철자), airre_mapbtn_group_make_n/p, airre_mapbtn_group_out_n/p, airre_mapbtn_more_n/p, airre_mapbtn_routeset_n/p, airre_mapbtn_schoolzone_n/p/s

## 2023-11-03 — 내 장소 리소스 수정 및 추가
- 추가: airre_maincard_pin, airre_sys_close2_n/p
- 수정: airre_btn_mymap_n/p, airre_card_check02_s, airre_card_check_blank2_n, airre_list_notice, airre_list_notice_bg.9, airre_list_pin_off/on, airre_list_icon_recentplace, airre_mapbtn_back_day, airre_mapbtn_more_day, airre_recentplace_empty_img
- 기존 리소스 수정: inv_listsel_ic_info_n/p, inv_listsel_ic_share_n/p, inv_listsel_ic_star_n/p, inv_list_bt_go_n/p, inv_list_bt_regist_n/p, inv_map_ic_go_n/p, inv_map_pin_road_finish, inv_map_pin_road_start, inv_map_point_pin_d, inv_map_point_pin_n
- AOS-xhdpi only: 위 중 inv_listsel_ic_info, inv_listsel_ic_star, inv_list_bt_go, inv_list_bt_regist(각 n/p), inv_map_pin_road_finish/start, inv_map_point_pin_d/n

## 2023-11-06 ~ 11-08 — 내 장소 크기·색상 보정
- 11-06: airre_bt_myplace_n/p, airre_bt_safedrive_n/s, airre_unablebar_round_l.9, airre_unablebar_round_r.9, tkl_map_ic_time, tkl_ic_arrival_distance(aos), hbl_destination_km_ic(ios)
- 11-07: airre_bt_myplace_n/P; 기존 수정 inv_list_label_hot (aos_drawable-xhdpi only); 미사용 표시(취소선) inv_list_label_hit, inv_list_label_like
- 11-08: airre_bt_myplace_n/p

## 2023-11-21 ~ 11-23 — HUD & SKP 광고 연동
- 11-21 수정: inv_authority_addressbook, inv_authority_disk(ios 제외), inv_authority_location, inv_authority_phone(ios 제외), inv_list_bt_checkbox_d/n/p/s(aos_xhdpi only), airre_popup_firstdrive_cash_img
- 11-21 신규: airre_authority_bluetooth(ios 제외), airre_badge_beta, airre_badge_connect_n/p, airre_badge_disconnect_n/p, airre_cashpage_event, airre_icon_hud, airre_icon_hud_registration, airre_sys_eventmore_n/p
- 11-22 수정: airre_cashpage_event, airre_sys_eventmore_n. 신규: airre_rectangle_firstinput_phonenumber, airre_hud_img(json)
- 11-23 수정: airre_cashpage_event (교환권 > 쿠폰 문구 수정)

## 2023-12-12 — iOS 단축어 지원 위젯 리소스 수정
- airre_wg_icon_favorite, airre_wg_icon_home, airre_wg_icon_search

## 컨테이너 표 (날짜 링크 대신 내용만)
| 컨테이너 페이지 | 행 | 내용 | 비고 |
|---|---|---|---|
| HUD & SKP 연동 | 1 | 기존 리소스 수정 / HUD&SKP 연동 리소스 추가 | (11-21 추정) ^[inferred] |
| | 2 | HUD&SKP 연동 리소스 수정 및 추가 | airre_hud_img(json) |
| | 3 | HUD&SKP 연동 리소스 수정 | 이미지 문구 수정 |
| 서비스 안정화 | 1 | IOS 단축어 지원 관련 리소스 수정 | 위젯 리소스 수정 |
| HUD연동 | - | 링크 항목만 있음(링크 항목, 내용 없음) | |

## Related
- [[inavi-air]] — 에어 앱 프로젝트 허브
- [[inavi-air-feature-history]] — 기능 이력
- [[air-app-version-notes-2023]] — 같은 시기 스토어 문구(HUD Beta, 12월 안정화)
- [[air-release-and-resource-log-hub]] — 이 묶음 목차

## Sources
- Confluence "2023.09.05" (pageId 230359041) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.09.07" (pageId 232783873) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.09.07B" (pageId 232849409) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.09.07C" (pageId 232849748) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.09.25 리소스 용량 개선" (pageId 243531847) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.10. 20" (pageId 260046849) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.10. 26" (pageId 263028737) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.10.17" (pageId 256311297) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.10.17B" (pageId 257064961) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.10.19" (pageId 258834433) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.10.19B/C" (pageId 259293185) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.11. 01" (pageId 265388033) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.11. 03" (pageId 268369921) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.11. 06" (pageId 269025322) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.11. 07" (pageId 270270465) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.11. 08" (pageId 271384577) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.11. 21" (pageId 282918913) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.11. 22" (pageId 283443262) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.11. 23" (pageId 283771280) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.12.12" (pageId 296845313) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "HUD & SKP 연동" (pageId 282919040) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "서비스 안정화" (pageId 296615938) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "HUD연동" (pageId 282853405) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
