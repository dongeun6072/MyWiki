---
title: >-
    Flutter SDK 개발 슬랙 채널 2026
category: references
project: orbis-sdk
tags: [orbis-sdk, flutter, pub-dev, slack, release, visibility/internal]
aliases: [10_prj-flutter-sdk-dev, Flutter Plugin 배포]
relationships:
  - target: "[[orbis-sdk]]"
    type: derived_from
  - target: "[[navisdk-flutter-plugin-plan-detail]]"
    type: extends
  - target: "[[sdk-flutter-scrums-2026]]"
    type: related_to
summary: >-
    Navi/Maps SDK의 Flutter Plugin 개발 채널(2026-05-06~07-23). 해외향 우선 배포 일정, pub.dev publisher 인증 절차, 패키지명, 샘플앱 플랫폼 차이 점검, 해외향 5/22와 국내향 7/23 pub.dev 배포 기록.
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0.0
base_confidence: 0.47
lifecycle: draft
lifecycle_changed: 2026-10-27
tier: core
created: 2026-10-27
updated: 2026-10-27
sources:
  - "slack:#10_prj-flutter-sdk-dev"
---

# Flutter SDK 개발 슬랙 채널 2026

[[orbis-sdk]]의 Navi SDK와 Maps SDK를 Flutter에서 쓰는 Plugin을 만드는 비공개 채널이다. 2026-05-06에 열렸고 마지막 글은 07-23이다. 계획 문서는 [[navisdk-flutter-plugin-plan-detail]], 주간 스크럼은 [[sdk-flutter-scrums-2026]]에 있다. 사람 이름은 역할로 적었고, 개발용 SDK 키와 공용 계정 비밀번호 요청은 값이 없어도 내용을 옮기지 않았다.

## 배포 방향 (2026-05-07)

리더에게 공유한 일정과 방향이다.

| 구분 | 일정·목표 |
|---|---|
| 해외향(선행) | 5/20 Navi·Maps Flutter Plugin 배포. 첫 고객은 Acer ITS(6월 중 앱 출시). 전략은 가격 경쟁력과 커스터마이징 지원 강조. 배포 후 이슈는 글로벌을 우선 대응 |
| 국내향(후행) | 6월 중 배포 목표. NaviSDK는 Step 2로 출시(Step 1은 시장 의미가 없고 혼선이 우려돼 건너뜀), MapSDK는 Step 1 출시 |
| 위험 | 해외향 요구사항에 따라 국내 우선순위와 일정이 밀릴 수 있음 |

이 방향은 스크럼의 Step 1/2 목표일 변화와 맞물린다 → [[sdk-flutter-scrums-2026]]. 채널 개설 당일(05-06)에는 별도 Flutter 공식 채널을 만들지 않고 기존 SDK별 채널에 공유하기로 했다. 같은 날 해외향을 "Orbis Maps/Orbis Navi SDK"라고 부를지 질문이 나왔고, 문서상으로는 "iNavi Global Navigation SDK"로 통일됐지만 구두로는 해외향·오비스 내비 등이 섞여 쓰인다는 답이 있었다.

## 진행 연표

| 날짜 | 내용 |
|---|---|
| 05-07 | 해외향 Navi SDK의 iOS CocoaPods 등록 완료(`Global-iNavi-Navigation-SDK`). SPM 의존성 추가가 안 돼 pods로 등록했고, 기존 배포 저장소는 변경 없음. podspec 관리는 navi_core 쪽에서 한다. 로컬 확인 시 같은 폴더 구조와 podspec 구성이 필요 |
| 05-11 | Flutter 샘플 앱의 `forceHideMapComponent`(UI 컴포넌트 강제 숨김/표시)가 코어 SDK 로직 문제로 동작하지 않는 것을 확인. SDK 수정은 앱 개발자가 맡기로 함 |
| 05-13 | 해외향 Maps Flutter Plugin 저장소 공유. Navi SDK 기반으로 초기 구성했고 Android·iOS 지도 연동까지 구현. Navi와 달리 컴포넌트별 구성이 필요해 고유 계획이 필요 |
| 05-14 | pub.dev 배포 준비 절차 공유(아래) |
| 05-19 | Plugin 배포는 구글 계정과 연동돼야 인증·배포가 가능하다. 공용 개발 publisher에 초대할 구글 계정을 요청 |
| 05-20 | 해외향 Maps Flutter 샘플 앱 동작 테스트 결과 공유(아래) |
| 05-22 | Global Navi 패키지명이 `navi_sdk_flutter`라 모호해 Maps와 같은 형식인 `inavi_global_navi_flutter`로 수정. **Global Navi/Maps Flutter Plugin v1.0.0을 pub.dev에 배포**(`inavi_global_navi_flutter`, `inavi_global_map_flutter`). 국내향 패키지명은 미정(`inavi_navi_flutter`, `inavi_map_flutter` 안) |
| 05-27 | 국내향 Maps SDK Flutter Plugin 개발에 쓸 개발용 SDK 키 전달 요청(값 미수록) |
| 06-05 | 국내향 Map SDK의 Custom Map Style 문의: Flutter Plugin에서 구현해야 하는지(과거 지도 스튜디오 방식은 deprecated 대상으로 들었으나 이력이 불확실), 그리고 네이티브 Android 샘플에서 custom style.json 요청 시 404가 난다 |
| 07-21 | 국내향 NaviSDK Flutter Plugin을 발행하면 pub.dev `homepage` URL을 국내향 지도 API 사이트로 우선 적용할지 문의(해외향은 글로벌 지도 플랫폼 사이트 적용) |
| 07-23 | **국내향 Navi/Maps Flutter Plugin을 pub.dev에 배포**(`inavi_navi_flutter`, `inavi_map_flutter`). Navi Plugin은 첫 배포 때 README에 플러그인 개발자 관점의 불필요한 내용이 올라가 재배포했고, 최신은 `1.0.1` |

## pub.dev 배포 절차 (05-14)

1. 필요한 것: 공용 개발 구글 계정으로 첫 업로드 권한 인증, 회사 도메인 소유권 인증용 DNS 레코드(서버플랫폼셀 지원 요청, Google Search Console 방식).
2. 최초 배포는 공용 개발 계정으로 올린다.
3. pub.dev에서 도메인 소유권을 확인해 **Verified Publisher**를 얻는다.
4. 최초 배포 패키지를 공식 Publisher 아래로 이전한다.
5. 공용 계정을 최상위 Admin으로 유지하고, 개발자들의 구글 계정을 Publisher 멤버로 초대한다.
6. 이후에는 개별 계정으로 배포할 수 있다.

도메인 인증은 배포 전에 미리 할 수 있어 먼저 진행하자고 했다. 스크럼에는 publisher 등록 완료가 기록돼 있다 → [[sdk-flutter-scrums-2026]].

## 샘플 앱 플랫폼 차이 점검 (05-20, 해외향 Maps)

Android와 iOS 사이에서 확인된 차이다. 같은 코드를 쓰는 Flutter에서 SDK 쪽 사양 차이가 그대로 드러난 사례다.

| 항목 | 내용 |
|---|---|
| 기본 지도 스타일 | Android/iOS SDK의 기본 스타일이 다르다. iOS에는 축척바가 표시되지 않는다 |
| CameraMove | 이징이 Android는 Ease-in-Out, iOS는 Ease-in으로 보인다 |
| Camera Events | iOS에는 CameraCancelCallback이 없어 취소가 되지 않는다 |
| Shape/Polygon/Polyline/Circle width | Flutter가 넘기는 값은 논리 픽셀(dp/pt)인데 Android SDK는 물리 픽셀(px)을 입력으로 가정하고 내부에서 비율로 나눠 단위가 어긋난다 |
| Marker | Asset 마커 크기가 다르다(iOS 커보임). Android에서 icon scale이 동작하지 않는다(icon/pixelRatio 문제인지 확인 필요) |
| InfoWindow | Android 기본 TextView는 가운데 정렬이 아니다 |
| 이상 없음 | FitBounds, Map Click, Marker Overlap, Map Padding, Projection |
| 코드 이슈 | Android develop 기준 `MethodChannelHandler`에서 FlutterInjector 참조 문제가 있어 FlutterAssets로 바꿔 테스트 중 |

국내향 iOS Plugin에는 시뮬레이터 슬라이스 부재로 Rosetta 실행이 필요한 문제도 있다 → [[navisdk-flutter-plugin-plan-detail]].

## 읽을 점

- 계획 문서에서 M3(pub.dev 공개 배포)는 "대기"였으나 이 채널로 **해외향 2026-05-22, 국내향 2026-07-23 배포**가 확인된다. 계획 문서의 M3 상태는 낡았다.
- 국내향 Map SDK의 Custom Map Style이 Flutter에서 필요한지, 서버 404의 원인이 호출 오류인지는 채널에서 결론이 나지 않았다.
- 별도 채널 `#10_prj-flutter-sdk-dev-noti`(같은 날 개설)는 읽지 않았다. 알림 채널로 보인다. ^[inferred]

## Sources

- 슬랙 `#10_prj-flutter-sdk-dev` 전체(2026-05-06~07-23). 원본 비보관. 개발용 키, 계정, 저장소·스타일 서버 주소, 공유 링크는 미수록.
