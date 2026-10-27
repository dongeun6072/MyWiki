---
title: >-
    하이브리드 내비 엔진·외부포팅 릴리즈 이력 (2022)
category: references
tags: [hybrid-navi, engine, external-porting, release, visibility/internal]
aliases: [안내엔진 발행, DP엔진 배포, 외부포팅 APK 발행, 검색엔진 발행]
relationships:
  - target: "[[inavi-hybrid-navi]]"
    type: related_to
sources: [~/Develop/Wiki/_raw/articles/Outlook_2022.md]
summary: >-
    2022년 안내 엔진(과속 알림음 거리 설정), DP 엔진(흑화 개선), 검색 엔진(전화번호 검색), 맵매칭 테스트 라이브러리와 아트뷰·유브릿지 외부포팅 APK 발행 이력.
provenance:
  extracted: 0.88
  inferred: 0.12
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

# 하이브리드 내비 엔진·외부포팅 릴리즈 이력 (2022)

[[inavi-hybrid-navi]]의 엔진 계층별 발행 기록이다. 단말에는 [[mxi-where-release-ota-2022]]의 앱 발행으로 전달된다. 공유 폴더 계정 같은 접속 정보는 메일에 있으나 적지 않았다.

## 안내 엔진 (MXI)

| 날짜 | 내용 |
|---|---|
| 05-18 | **과속 알림음 거리별 설정**(신규): 카메라 남은 거리별로 알림음을 고른다. 일반도로 `없음 / 잠시후 / 300m / 500m`, 고속도로 `없음 / 잠시후 / 300m / 500m / 1km`. 인터페이스 `SetCamWaringSoundDistOpt(일반옵션, 고속옵션)` (`GuideAdapter.java`) |
| 05-25 | **고속도로 300m 옵션 제거**, 통신형 경로가 없을 때 과속 알림 효과음 미연동 |

고속도로 300m를 뺀 이유: "잠시후" 거리가 일반 150m, 고속도로 250m인데 고속 주행에서 250m와 300m는 체감 차이가 거의 없었다. UX 기획팀과 개발자가 협의해 설계서(지도주행 v2.8, 환경설정 v2.5)에 반영했다. 이 기능 설계는 [[이동은]]의 2022년 "AOS 외부포팅: 과속 경고 알림 설정 메뉴(UI)와 안내엔진, 데이터 절약 설정" 업무에 해당한다. ([[inavi-air-feature-history]]) 일정: 과속 경고 알림 설정 5/27 완료, 데이터 절약 설정 6/15 예정(선거일과 현충일 고려).

## DP 엔진 (지도 표출)

| 버전 | 날짜 | 내용 |
|---|---|---|
| `hybridnavi_android_v0.0.9c` | 06-03 | 지도 흑화 개선(`setPreserveEGLContextOnPause`) → [[map-black-screen-lifecycle]] |
| `v0.0.9d` | 06-13 | SMDC 데이터 offset 자료형 타입 수정. 6월 17일 발행 MXI에 반영 |
| (재적용) | 10-31 | 아트뷰 단말에서 흑화가 접수되어 개선된 DP 엔진을 반영한 포팅내비 발행(AOS 외부포팅 마지막 정식 발행은 5월 3D V1.2.9 B56) |

5월 31일 action item: 통신 ↔ 비통신 전환 시 흑화 등 지도 갱신 로직 개선을 6월 3일 이전에 DP 엔진으로 배포.

## 검색 엔진

- 08-02 `J100` 비통신 검색 엔진 발행: **일부 지역 전화번호 검색이 되지 않는 이슈**(쌍용 Y450 VOC) 수정. MXI와 아이나비 3D Streaming(포팅내비)도 같은 엔진이므로 각 브랜치에 라이브러리를 적용한다. 내비 발행 일정은 아직 없다.

## 맵매칭 라이브러리 (아트뷰)

- 아트뷰의 GPS 칩셋 수급 이슈로 **맵매칭 판단 조건을 하향 검토**했다(M2C-T9100).
- 09-28 선행개발 팀이 **GPS 속도 5km/h 이하는 사용하지 않는** 테스트판 `libmapmatch`를 전달하고, 이를 적용한 **타임락(10월 말)** 버전을 만들어 사업부에 테스트용으로 전달했다.
- 10-26 맵매칭 적용 타임락 버전 발행

## 외부포팅 APK 발행

| 대상 | 버전 | 날짜 | 비고 |
|---|---|---|---|
| 유브릿지 IAN-10 | 아이나비 3D V1.2.5 (B46) | 05-18 | TBT 미지원 적용. 타임락 버전 있음 |
| 아트뷰, 유브릿지 | 3D Streaming V1.2.9 (B56) | 05-24 | OTA: 아트뷰 M2C-D110i, M2C-200i 2종(05-25 14:00) |
| 유브릿지 IAN-10 | 3D Streaming V1.2.7 (B50) | 07-04 | 가오픈 요청: MAP 통신 22.02a, 비통신 22.01a, 검증 발행 |

공통 구성: `hybridnavi.apk`, `hybridnavi_happywayard.apk`(v3.2, code 102), `hybridnavi_tbt.apk`(1.0, code 857). 발행 메일은 대상, 버전, 링크, 릴리즈 노트로 구성한다. 05-18의 발행 메일이 이후 **발행 메일 샘플**이 됐다.

## 기타 지식

- **경로 탐색 옵션 문자열**: 추천경로 `TRAFFIC`, 최소시간 `TRAFFIC_2`. 외부 앱이 최소시간으로 요청해도 탐색옵션 화면에는 "추천경로"로 표시되는 문제가 08월에 접수됐다. ([[mxi-field-incidents-2022]])
- **"길 건너 목적지" 설정**(서울 장애인 콜택시 문의): 켜면 도로 레벨을 고려한 목적지 방향성 탐색을 하지 않는다. 기본값은 Off. 즐겨찾기는 앱 내 DB라 파일로 공유할 수 없고, 통신이 되면 **통합회원 로그인으로 백업·복원**한다(에어의 즐겨찾기 API와 같은 계열: `/regPointInsert`, `/moveRegPoint`. [[inavi-air-api-detail-spec]]) ^[inferred]

## Sources

- [[_raw/_archived/Outlook_2022.md]] — 2022 업무 메일
