---
title: >-
    에어 리소스 배포 메모 2023 (5월~8월)
category: references
project: inavi-air
tags: [inavi-air, resource-deploy, aircash, airlab, visibility/internal]
aliases: [2023.05.16, 2023.06.14, 2023.07.13B, 2023.08.29, 리소스 배포 메모 2023 상반기]
relationships:
  - target: "[[inavi-air]]"
    type: related_to
  - target: "[[inavi-air-feature-history]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/161480758
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/158040065
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/150372382
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/167313503
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/167739393
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/169050113
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/169836545
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/171016201
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/174325912
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/175996931
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/175800525
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/179109954
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/189661227
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/193495041
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/193658881
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/195592193
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/202932233
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/202932292
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/212959287
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/214663225
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/221085697
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/221839364
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/225607681
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/225706010
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/226525272
summary: >-
    2023-05-16 ~ 2023-08-30 사이 날짜 제목 페이지 25건에 기록된 에어 앱 이미지·Lottie 리소스 추가/수정/삭제 항목(에어캐시 스탬프·룰렛, 에어연구소, 제보하기 등)을 날짜별로 정리.
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

# 에어 리소스 배포 메모 2023 (5월~8월)

디자인 쪽에서 앱 개발자에게 전달한 이미지/Lottie 리소스 묶음을 날짜 제목 페이지로 남긴 기록 중 2023년 5월~8월분이다. 각 페이지는 "리소스 추가/수정/삭제" 분류 아래 파일명(식별자)을 나열한 형태이며, 파일 배포 링크는 `<링크 생략>`(원본에 있음, 미수록)이다. 접두어 `airre_`는 에어 앱 전용, `inv_`/`tkl_`/`hbl_`은 내비 엔진 공용, `car_`는 Android Auto, `_n`/`_p`/`_s`/`_e`는 normal/pressed/selected/enabled 상태 이미지로 보인다 ^[inferred]. 페이지 제목의 날짜와 원본 수정일이 다른 경우(예: 2023.07.07은 7월 19일 수정)는 제목 날짜를 따른다. 이후 기록은 [[air-resource-deploy-log-2023-h2]], 전체 목차는 [[air-release-and-resource-log-hub]].

## 2023-05-16 — 에어캐시 적립 개선(스탬프) 리소스 추가
- 버튼/배경: airre_btn_go_stamp_n, airre_bg_stamp
- 코인: airre_coin_3d, airre_coin_line, airre_coin_medium_front
- 툴팁: airre_no_save_cash_tooltip, airre_no_save_randomcash_tooltip, airre_stamp_tooltip_blank, airre_stamp_tooltip_coin
- 스탬프 상태: airre_stamp_completed, airre_stamp_completed_blank, airre_stamp_completed_img, airre_stamp_saving, airre_stamp_unsaved
- 시스템 버튼: airre_sys_close_wh_n/p, airre_sys_mycashlist_n/p

## 2023-05-16_carplay — 출발·도착·경유지 핀 수정
- 폴더명: mappin_carplay
- airre_car_map_start, airre_car_map_goal, airre_car_map_pathway_01/02/03

## 2023-05-23 — 스탬프 색상·디자인 수정
- airre_stamp_unsaved, airre_stamp_saving, airre_stamp_completed, airre_stamp_tooltip_blank, airre_stamp_tooltip_coin

## 2023-06-14 — 리소스 수정 및 신규 추가
- json 파일: airre_reward_completed_particle, airre_aircash_drive_progress_ios, airre_aircash_drive_progress_aos
- 9.patch: airre_cashpage_btn_n, airre_cashpage_1/2/3
- 신규 추가
  - 에어캐시: airre_aircash_btn_drive_record, airre_aircash_logo, airre_aircash_reward_img_1~7, airre_bt_aircash_n/p, airre_drive_medium, airre_onair_medium
  - 메인 카드: airre_maincard_img_1_a, 1_b, 2_a, 3_a/3_b/3_c, 4_a/4_b/4_c, 5_a/5_b, 6_a/6_b, 7_a, 8_a, 9_a/9_b/9_c/9_d
  - 리워드: airre_reward_again_img, airre_reward_blank, airre_reward_completed, airre_reward_completed_img, airre_reward_rullet_nextmonth, airre_reward_rullet_off, airre_reward_rullet_on, airre_reward_saving, airre_reward_unsaved, airre_stamp_rullet_complete
  - 기타: airre_main_notice_pagenumber(메인 하단 팝업)
- 기존 리소스 수정: airre_point_tooltip(android only), airre_sys_back_n, airre_sys_cash_info_n, airre_sys_mycashlist_n, airre_coin_medium, airre_btn_go_coupon_n, airre_btn_go_shop_n

## 2023-06-14B
- 기존 파일 원복: airre_sys_back_n
- 신규 추가: airre_aircash_back_n/p
- Auto 차로 정보 수정 반영
  - car_inv_ico_lane_option1, car_inv_ico_lane_option1_1normal/_1selected ~ _5normal/_5selected(1~5번 각 normal/selected 쌍), car_inv_ico_lane_option3
  - car_inv_ico_lc00 ~ car_inv_ico_lc95 (연번 96종)
  - car_inv_img_pocket_l, car_inv_img_pocket_r

## 2023-06-15 — IOS 누락 건 재전달 및 수정
- 재전달: airre_resource_230615 iOS용 zip (iOS 누락분)
- 기존 리소스 수정: airre_aircash_drive_progress(json), airre_sys_cash_info_n, airre_aircash_back_p
- 신규 추가: airre_aircash_blank_drive, airre_aircash_blank_onair, airre_bt_aircash_off_n/p, airre_bt_aircash_on_n/p, airre_reward_month, airre_reward_rullet_btn_off, airre_reward_rullet_btn_on, airre_reward_rullet_popup_btn, airre_stamp_rullet_btn_completed

## 2023-06-15B — 파일명 정정 및 9patch 분리
- 파일명 정정: airre_sys_cash_info_n ↔︎ p (n/p 뒤바뀜 정정)
- 9patch(이미지 분리 반영): airre_cashpage_1.9(수정), airre_cashpage_1.9b(추가)

## 2023-06-16 — pressed 리소스 추가 및 파일명 수정
- iOS only
  - 파일명 수정: airre_reward_rullet_btn_on → airre_reward_rullet_btn_on_n, airre_reward_rullet_popup_btn → airre_reward_rullet_popup_btn_n
  - 추가: airre_reward_rullet_btn_on_p, airre_reward_rullet_popup_btn_p
- 공통
  - 파일명 수정: airre_aircash_btn_drive_record → airre_aircash_btn_drive_record_n
  - 추가: airre_aircash_btn_drive_record_p, airre_btn_go_coupon_p, airre_btn_go_shop_p, airre_roulette_tiket_bg
  - 수정: airre_reward_completed_img, airre_roulette_bg, airre_roulette_pin, airre_roulette_rotation, airre_roulette_startbtn, airre_bg_particle, airre_bg_title

## 2023-06-21 — 이미지 수정 및 기존 룰렛 리소스 삭제
- android 수정: airre_reward_saving, airre_reward_completed
- ios(90x90) 수정: airre_reward_blank, airre_reward_unsaved, airre_reward_saving, airre_reward_completed
- 삭제(기존 룰렛 리소스): airre_bg_coin, airre_toggle_premium, airre_toggle_special
  - premium/special/standard 룰렛 각 4종(`_roulette_bg`, `_pin`, `_rotation`, `_startbtn`): airre_premium_roulette_*, airre_special_roulette_*, airre_standard_roulette_*

## 2023-06-22 — GUI 개선안에 따른 사이즈 조정
- 이미지 수정: airre_aircash_logo, airre_maincard_img_1_a, 1_b, 2_a, 3_a, 3_c, 4_a, 4_b, 5_a, 5_b, 6_a, 6_b, 7_a, 8_a, 9_a/9_b/9_c/9_d, airre_reward_completed, airre_reward_saving
- aos only 캐시버튼: airre_point_coinbank, airre_point_tooltip
- 이미지 추가: airre_maincard_img_3_b, airre_maincard_img_4_c

## 2023-06-23 — 스탬프 파일명 오류 정정
- airre_reward_saving, airre_reward_completed

## 2023-06-27 — 색상·형태 수정
- 적립내역 버튼: airre_sys_mycashlist_n
- 주행이력 버튼: airre_aircash_btn_drive_record_n, airre_aircash_btn_drive_record_P (원문 표기 대문자 P)

## 2023-07-07 — 메인 하단 메뉴/툴팁 리소스
- json: airre_bt_aircash_on_bg
- 9.patch: airrie_main_tooltip_bg_1 (원문 철자 airrie)
- 신규 추가: airre_bt_aircash_off_n/p, airre_bt_aircash_on_n/p, airre_bt_cctv_n/s, airre_bt_location_n/s, airre_bt_safedrive_n/s, airre_bt_set_n/s, airre_bt_set_new_n/s, airre_main_tooltip_bg_2, airre_main_tooltip_img_1~7, airre_map_warning_pedestrian
- 기존 리소스 삭제: airre_bt_set_new, airre_bt_aircash_n, airre_bt_aircash_p

## 2023-07-13 — 안전운전 심볼/핀 신규
- 안전운전 심볼: inv_map_safe_sign_bg28_tm(후면단속카메라), inv_map_safe_sign_bg29_tm(마을주민보호구역), inv_map_safe_sign_bg30_tm(장애인보호구역)
- 안전운전 핀: inv_map_safe_pin_33(후면단속카메라), inv_map_safe_pin_34(마을주민보호구역), inv_map_safe_pin_35(장애인보호구역)

## 2023-07-13B — 리소스 삭제 예정 대상
삭제 예정 목록(미사용 정리).
- AOS: airre_bg_stamp, airre_btn_go_mycashlist_n, airre_btn_go_stamp_n, airre_coin_3d, airre_icon_cash, airre_icon_point, airre_icon_rewards, airre_icon_route_merge_n/p, airre_main_banner, airre_main_coin_logout, airre_main_coin_plus, airre_my_aircash_bg.9, airre_my_routehistory_n/p, airre_mycash_full, airre_mycash_plus, airre_no_save_cash_tooltip, airre_no_save_randomcash_tooltip, airre_setting_labimg, airre_stamp_completed, airre_stamp_completed_blank, airre_stamp_completed_img, airre_stamp_saving, airre_stamp_tooltip_blank, airre_stamp_tooltip_coin, airre_stamp_unsaved, airre_sys_go_rewards_n/p, airre_sys_mycashlist_p
- iOS: airre_btn_go_mycashlist_n, airre_btn_go_stamp_n, airre_coin_3d, airre_coin_large, airre_coin_small, airre_icon_cash, airre_icon_point, airre_icon_rewards, airre_icon_route_merge_n/p, airre_main_banner, airre_main_coin, airre_main_coin_logout, airre_main_coin_plus, airre_main_coin_zero, airre_my_aircash_bg, airre_my_routehistory_n/p, airre_mycash_full, airre_mycash_plus, airre_no_save_cash_tooltip, airre_no_save_randomcash_tooltip, airre_setting_labimg, airre_stamp_completed, airre_stamp_completed_blank, airre_stamp_completed_img, airre_stamp_saving, airre_stamp_tooltip_blank, airre_stamp_tooltip_coin, airre_stamp_unsaved, airre_sys_go_rewards_n/p, airre_toggle_off, airre_toggle_on, airre_widget_icon_cash
- (이 페이지에는 수정일 7월 19일, 파일 링크 없음)

## 2023-07-17 — 후면 카메라(신호등) 심볼 추가
- inv_map_safe_sign_bg31_tm

## 2023-07-25 / 2023-07-26 — 메인 하단 메뉴 텍스트 크기 수정
- 07-25: airre_bt_cctv_n, airre_bt_location_n, airre_bt_safedrive_n, airre_bt_set_n, airre_bt_set_new_n
- 07-26: 위 5종의 n/s 쌍 전체(airre_bt_cctv_n/s, airre_bt_location_n/s, airre_bt_safedrive_n/s, airre_bt_set_n/s, airre_bt_set_new_n/s)

## 2023-08-09 — 주변 검색 / 모의 주행 배속 수정
- 모의주행 컨트롤러: airre_controller_{1x,2x,4x,8x}_n, airre_controller_{1x,2x,4x,8x}_night_n, airre_controller_{1x,2x,4x,8x}_p
- 주변 검색 아이콘: airre_icon_around_01 ~ 12 의 _n/_p (24종)

## 2023-08-11 (Carplay) — 주변 검색 수정
- inv_poi_ic_01, 02, 03, 04, 05, 07, 10, 12 각각 _n/ _p

## 2023-08-22 — 에어연구소 리소스 추가(39종)
- airre_airlab_back_n/p
- airre_airlab_basicoption_btn_01~06 각 _n/_p/_e
- airre_airlab_basicoption_n/p
- airre_airlab_basicoption_tab_01~06
- airre_airlab_btn_detail_n/p, airre_airlab_forbid_n/p, airre_airlab_intro_01, airre_airlab_intro_02, airre_airlab_logo_img, airre_airlab_more_n/p, airre_airlab_trafficlights_n/p

## 2023-08-23 — 에어연구소 리소스 추가(15종)
- airre_airlab_basicoption_img_01~07, airre_airlab_basicoption_tab_07
- airre_airlab_coin_img, airre_airlab_coin_n/p, airre_airlab_forbid_img, airre_airlab_intro_02, airre_airlab_more_img, airre_airlab_trafficlights_img

## 2023-08-29 (29B는 같은 내용의 파일링크판) — 리소스 수정 및 신규 추가
- 기존 리소스 수정: airre_icon_07, airre_icon_07_new, airre_icon_08 (29B는 airre_icon_08_new 추가)
- 에어연구소 수정: airre_airlab_basicoption_btn_01~06 의 _e/_n/_p(18종), airre_airlab_basicoption_img_07
- 에어연구소 신규: airre_airlab_report_n/p, airre_airlab_report_img_01/02 (29B는 airre_airlab_basicoption_img_01~07 신규로 명시)
- 제보하기 신규 추가
  - 아이콘/지도 버튼: airre_icon_08_new, airre_icon_07, airre_icon_07_new, airre_icon_08, airre_mapbtn_group_cancel_day/night, airre_mapbtn_group_report_day/night
  - 제보 화면: airre_report_add_n/p, airre_report_blank_img, airre_report_btn_camera_n/p, airre_report_btn_etc_n/p, airre_report_btn_location_n/p, airre_report_btn_road_n/p, airre_report_edit_btn_n/p, airre_report_label_bg
  - 목록: airre_report_list_add_n.9/p.9, airre_report_list_top_n.9/p.9, airre_report_myself_btn_n/p, airre_report_pin, airre_report_process_tab_01/02/03, airre_report_repory_search_btn_n/p, airre_report_retry_btn_n 및 airre_report_retry_btn__p(원문 언더스코어 두 개), airre_report_save_completed, airre_report_temporarily_cancel_n 및 airre_report_temporarily_cancel__p
  - 아이콘: arrie_report_btn_icon_n/p, arrie_report_list_icon_n/p (원문 철자 arrie)
- 29B 추가분: airre_report_list_camera_n/p, airre_report_list_road_n/p, airre_report_list_location_n/p, airre_report_list_etc_n/p
- 제보하기 기능 배경은 [[air-map-data-and-safety-guidance-2023]]도 참고

## 2023-08-30 — 제보하기 리소스 수정
- 기존 리소스 수정: airre_report_btn_camera_p, airre_report_btn_etc_p, airre_report_btn_location_p, airre_report_btn_road_p, airre_report_add_n/p, airre_report_list_camera_n/p, airre_report_list_etc_n/p, airre_report_list_location_n/p, airre_report_list_road_n/p, airre_airlab_trafficlights_img

## Related
- [[inavi-air]] — 에어 앱 프로젝트 허브
- [[inavi-air-feature-history]] — 기능 이력(에어캐시, 에어연구소, 제보하기)
- [[air-cash-reward-design-2023-2024]] — 스탬프/룰렛 에어캐시 설계 배경
- [[air-resource-deploy-log-2023-h2]] — 이어지는 기록
- [[air-release-and-resource-log-hub]] — 이 묶음 목차

## Sources
- Confluence "2023.05.16" (pageId 161480758) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.05.16_carplay" (pageId 158040065) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.05.23" (pageId 150372382) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.06.14" (pageId 167313503) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.06.14B" (pageId 167739393) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.06.15" (pageId 169050113) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.06.15B" (pageId 169836545) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.06.16" (pageId 171016201) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.06.21" (pageId 174325912) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.06.22" (pageId 175996931) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.06.23" (pageId 175800525) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.06.27" (pageId 179109954) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.07.07" (pageId 189661227) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.07.13" (pageId 193495041) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.07.13B" (pageId 193658881) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.07.17" (pageId 195592193) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.07.25" (pageId 202932233) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.07.26" (pageId 202932292) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.08.09" (pageId 212959287) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.08.11_Carplay" (pageId 214663225) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.08.22" (pageId 221085697) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.08.23" (pageId 221839364) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.08.29" (pageId 225607681) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.08.29B" (pageId 225706010) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
- Confluence "2023.08.30" (pageId 226525272) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
