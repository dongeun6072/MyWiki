---
title: >-
    Orbis NaviSDK 개발 흐름 (2025): 경로 서버 릴리즈, 맵매칭 라이브러리, 디스플레이, 테스트 앱
category: references
project: orbis-sdk
tags: [orbis-sdk, navi-sdk, tomtom-orbis, taiwan, map-matching, visibility/internal]
aliases: [Orbis NaviSDK 2025, 대만 NaviSDK MVP, OrbisMap 맵매칭 라이브러리, U-Map, Turn Type 산정]
relationships:
  - target: "[[navi-sdk-2024-activity]]"
    type: extends
  - target: "[[orbis-navisdk-poc-prep-2025]]"
    type: related_to
  - target: "[[taiwan-routeserver-api]]"
    type: related_to
  - target: "[[orbis-route-data-lib]]"
    type: related_to
  - target: "[[inavi-2025-mail-overview]]"
    type: derived_from
sources: [~/Develop/Wiki/_raw/articles/Outlook_2025.md]
summary: >-
    2025년 메일로 본 Orbis NaviSDK 개발: 경로 서버·데이터 라이브러리 릴리즈 이력, 맵매칭 라이브러리 0.1~0.6 이슈, 지도 디스플레이(PBF, MapLibre), 현지화, 한국·대만 샘플 앱, Turn Type 기준.
provenance:
  extracted: 0.78
  inferred: 0.20
  ambiguous: 0.02
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T11:10:00+09:00
updated: 2026-10-26T11:10:00+09:00
snapshots:
  - "[[_raw/_archived/Outlook_2025|Outlook_2025]]"
---

# Orbis NaviSDK 개발 흐름 (2025)

TomTom Orbis 지도 데이터로 대만 NaviSDK MVP를 만든 한 해를 메일로 다시 그린 것이다. 앞 해는 [[navi-sdk-2024-activity]], 사전 검토는 [[orbis-navisdk-poc-prep-2025]]이다. 규격 자체는 [[taiwan-routeserver-api]], [[orbis-route-data-lib]], [[orbismap-api-docs]]에 있다. **인증·키·토큰·로그인 관련 내용과 서버 주소는 의도적으로 뺐다.**

## 팀별 역할 (메일 서명 기준)

| 팀 | 맡은 일 |
|---|---|
| 경로기술개발팀 | Orbis 도로 네트워크 기반 **경로 서버**(대만·한국)와 **Route Data Library** 릴리즈 |
| 선행기술Lab Dev.2팀 | **맵매칭(MMC) 라이브러리** |
| Digital&Display팀 | 지도 데이터 컨버전, 스타일, 디스플레이 |
| 모빌리티Tech그룹(개발PM) | SDK 앱 통합, 샘플 앱, 시험·이슈 취합 |
| 전략팀·해외사업팀 | TomTom·현지 업체 협의 → [[orbis-taiwan-business-2025]] |

## 경로 서버·데이터 라이브러리 릴리즈 이력

**INAVI Route Server for Taiwan** (v0.4 → v1.8, 3월~11월, 약 15회). 눈에 띄는 변화만 적는다.

| 버전 | 시기 | 변화 |
|---|---|---|
| v0.4 | 03-06 | 응답에 방향 전환 유형 `maneuver` 추가, 중거리 탐색 시간 초과 수정 |
| v0.5 | 04-16 | POST에서 `application/json` 요청 지원, 응답 헤더에 JSON 명시 |
| v0.6 | 04-25 | TomTom 실시간 **도로 통제 회피** 우회 탐색(실시간 통제 서버 상용화는 7월 이후) |
| v0.7 | 05-23 | 소요 시간을 Google 지도 결과와 더 비슷하게 보정 |
| v0.9 | 06-19 | 링크 진행 방향 `links > direction` 추가 |
| v1.2 | 08-08 | 오토바이 전용 도로 회피, 고립 링크·페리 항로로 인한 탐색 실패 개선, Orbis Taiwan v25240 적용 |
| v1.3 | 09-05 | **다중 경로** API `searchroutemulti`(최적 경로 포함 최대 3개) |
| v1.4 | 09-22 | 같은 링크의 경유지 실패, 일방통행 역주행, 주변 도로 없음 시 엔진 종료 수정 |
| v1.6 | 10-20 | 출발·도착 좌표의 도로 방향성 옵션 `sideroadstart`, `sideroadend` |
| v1.8 | 11-27 | 회전교차로 상세 코드(8 직진, 9 진출, 10 진입) 추가 |

- **INAVI Route Server for Korea v0.1**(08-08): 같은 Orbis 데이터의 한국 도로망(v25290)으로 **국내 실차 시험**을 하려고 만든 서버다. TomTom 실시간 교통정보는 아직 적용되지 않았고, 규격은 대만 서버 v1.1과 같다. 이후 대만 서버의 다중 경로(v1.3)와 안정성 수정(v1.4)도 같이 적용했다.
- **INAVI Purpose Based Route Server for Taiwan v0.1**(12-23): 물류용 **목적 기반 탐색**. 경로 거리 행렬 API(`/searchrdm`)와 경유지 순서 최적화 TSP API(`/searchtsp`)가 처음 나왔다.
- **Orbis Route Data Library**(v1.0.0.1 02-19 → v1.0.1.2 11-18, 10회): 초기에 `GetExtentLink`, `GetExtentNode`가 붙었고 v1.0.0.7(06-13)에 도로명 조회와 링크 길이 미터 단위가 들어갔다. v1.0.1.1(09-29)은 메모리 사용과 **다중 프로세스 동시 사용** 문제를 고쳤고, v1.0.1.2(11-18)에서 iOS를 지원했다. 대만·한국 서비스 데이터가 같은 라이브러리로 동작한다.

### Turn Type 산정(10-14 공유)

현재 링크와 다음 링크의 각도로 계산한다. 오른쪽으로 꺾이면 음수, 왼쪽이면 양수이다. 기준은 NDS를 따르되 경험치로 TURN과 SHARP 구간을 조정했다.

| 코드 | 유형 | 각도 |
|---|---|---|
| 0 | STRAIGHT | -17 ~ 17 |
| 1 / 2 | SLIGHT RIGHT / LEFT | -62 ~ -18 / 18 ~ 62 |
| 3 / 4 | TURN RIGHT / LEFT | -124 ~ -63 / 63 ~ 124 (NDS는 ±118까지) |
| 5 / 6 | SHARP RIGHT / LEFT | -162 ~ -125 / 125 ~ 162 (NDS는 ±119부터) |
| 7 | U-TURN | ±163 ~ ±180 |

## 맵매칭(MMC) 라이브러리

- 2024년 LG AR용 엔진([[navi-sdk-2024-activity]])과 별도로 **OrbisMap용 새 라이브러리**가 7월부터 나왔다(Android 0.1.0 07-17 → 0.6.2 11-19, iOS 0.6.3 12-09, 약 20회). 0.5.x는 번호가 순서대로 나오지 않는다(0.5.6이 10-22, 0.5.3이 11-04에 배포). 병행 가지로 보인다. ^[inferred]
- **0.1.0**: `matchStatus`(0 매칭, 1 오프로드)는 건물 진입 같은 실제 오프로드에서만 1이 되고 다른 도로로 붙으면 0이라 이탈 판단에 못 쓴다. 경로 내 링크 인덱스(`indexOnRoute`)는 항상 -1이었고, 오프로드 진입 후 속도가 130~150, 300 넘게 올라가는 값도 있었다. 로그 주행 시 차가 뒤로 가는 현상은 개선됐다.
- 06-13 요청으로 **링크 프로젝션**(`linkProjection`) 추가: 현위치가 아닌 임의 지점의 링크와 비율로 거리를 계산하려는 목적이다.
- **0.4.0**(08-29) 모의주행 추가: 앱은 대만 앱에 모의주행이 중요해 이 기능을 먼저 달라고 했다. 요청 사항은 `setOrbisRoute` 반환값이 문서와 반대(0 실패, 1 성공)인 점, 모의주행 경로 **인덱스**를 얻는 인터페이스다(0.4.1에서 추가). 모의주행 중 `GetDataLink`를 불필요하게 중복 호출해서 Crash가 났고 약 30ms 갱신 주기에서도 안 나게 고쳤다.
- **0.5.1**(09-08) 이슈: 경유지를 넣은 모의주행에서 경유지 링크를 한 번 더 반복, 도착지·경유지가 링크 중간이어도 끝까지 진행. 09-25 시험에서는 MMC와 메인이 동시에 `GetDataLink`를 호출할 때 **전체 경로 보기에서 거의 100% 종료**됐다(경로 3개, 약 400개 링크). 같은 달 Route Data Library 테스트판(v1.0.1.01)이 이 문제의 대응이었다.
- 11-06 디버그 로그를 파일로 저장하는 기능을 넣은 시험용 라이브러리, 11-19 `Location.hasVerticalAccuracy()`가 없는 Android 21 단말에서 `NoSuchMethodError`로 초기 종료.
- 11-14 이후 에어에서도 MMC 이슈가 나왔고 → [[air-operations-2025]]

## 지도 디스플레이

- 06-12 데이터팀 검토: TomTom의 **PBF**는 OSM 원도 데이터를 바이너리로 묶은 패키지이고, 자사 **TiledMap(PBF)**은 레벨별로 타일링한 Mapbox Vector Tile이라 서로 다른 데이터다. TomTom 데이터를 쓰려면 벡터맵용 **컨버전**이 필요하고 레이어, 폰트, 심볼 구성이 작업 대상이다. Mapbox와 MapLibre는 같은 MVT를 렌더하므로 호환 문제는 기본적으로 없다(3D 건물, Terrain은 제외). → [[orbis-sdk]]의 MapLibre 기반 Maps SDK
- 07-17 컨버터 개발 완료 예정. 맵 스타일 스튜디오로 사전 확인해 터널 레이어 신규, 도로 아웃라인 `draw_order` 변경, 램프 `line_width` 분리, 보행로 레이어를 도로 아래로 옮기는 네 항목을 1차 테스트에 반영했다.
- 05-16 대만 시험 경로선과 TomTom 지도 SDK 배경이 어긋나는 증상이 보고됐고, 같은 경로가 OpenStreetMap, Mapbox 배경에서는 맞는다는 비교 자료가 공유됐다.

## 현지화

- 음성 문구 번역 피드백(06-12): 대만 중국어는 미터를 **公尺**(발음 공츠), 킬로미터를 **公里**로 바꿔야 한다.
- 중국 내비 거리 표기(05-19): 중국 AutoNavi는 거리를 한자로 표시하고, 팅크웨어 시절 중국향 제품은 km, m으로 표현했다.
- 05-27 TomTom 답변: Maps SDK는 Nav SDK의 하위 구성이다. 온라인 모드에서는 **지정학적 표기(Geopolitical View)가 단말 위치 기반으로 자동**이라 직접 못 바꾼다. Orbis 오프라인 지도(NDS)는 **한국용이 3분기 말 이후, 한국 외는 6월 말** 제공 예정이며 Orbis API는 Public Preview였다. 자체 지도나 API를 끼워 쓰는 기능은 지원하지 않는다.

## 테스트 앱과 전시

| 시기 | 앱 | 내용 |
|---|---|---|
| 08-21 ~ 09-05 | 한국향 샘플 앱 **U-Map** 0.0.1 | 한국 실주행에서 안정성 확인. 실제 타깃이 아니라 카메라, 도로명이 안 나올 수 있다. 의견은 시트로 수집 |
| 09-05 | 대만향 샘플 앱 | 사용 기한을 걸어 배포(10월 31일) |
| 09-11 | 국내 고객 이슈 | 고객이 `runSingleRoute`를 반복 호출하면 이전 결과가 초기화돼 마지막 경로만 보인다. `runRoute`와 병행하면 3개까지 받을 수 있으나 비공식. 4개 이상은 신규 기능 개발(약 2일) |
| 10-02 | 멀티탐색 샘플 프로젝트 | MMC에서 멀티 탐색 시험 |
| 10-22 | 전시용 U-Map | TPCA 전시 단말 비정상 종료 수정판. 전시장에서 위치가 안 잡히면 정문이나 가짜 GPS로 한 번 잡으면 마지막 위치로 설정됨 |

## 데이터 검토 (01-09)

대만 Orbis 데이터의 안전운행·위험지역 데이터는 일부만 있다. 과속 카메라 점 형상 872개(대부분 위치만 있고 각도·제한속도 없음)와 관계 정보 107개(최고속도 95, 평균속도 12), 신호단속 9, 방범 190, 방지턱 213(점)+819(링크 속성), 트럭 제한 높이 2,325·중량 286·차폭 15, 도로 표지판은 없다. 전부 `supported=no`이고 라이선스가 ODbL이어서 **TomTom이 검증하지 않은 데이터**로 보이며 사용 가능 여부는 확인이 필요했다.

## Open Questions

- 한국 SDK 사용 고객(아이나비 모빌리티)의 SDK 버전과 Orbis SDK의 관계는 메일로는 구분되지 않는다.
- 맵매칭 0.6.x 이후와 대만 MVP 최종 인도 범위는 2025 메일에 없다.

## Sources

- [[_raw/_archived/Outlook_2025.md]] — 2025 업무 메일
