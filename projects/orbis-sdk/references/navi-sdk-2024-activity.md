---
title: >-
    NaviSDK 2024년 활동: 맵매칭 엔진, 티머니 크래시, SDK Renewal, 대만향 검토
category: references
project: orbis-sdk
tags: [orbis-sdk, navi-sdk, map-matching, tmoney, taiwan, visibility/internal]
aliases: [NaviSDK 2024, SDK Renewal, LG AR 맵매칭, 티머니 MMC 크래시, 대만향 NaviSDK 검토]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[orbis-navisdk-poc-prep-2025]]"
    type: related_to
  - target: "[[inavi-2024-mail-overview]]"
    type: derived_from
sources: [~/Develop/Wiki/_raw/articles/Outlook_2024.md]
summary: >-
    2024년 메일 속 NaviSDK 관련 일: LG AR용 맵매칭 엔진 배포, 티머니 기사앱 맵매칭 크래시, 이륜차·도보 샘플앱, 후면카메라 안내, 11~12월 SDK Renewal과 TomTom 기반 대만향 검토 요청.
provenance:
  extracted: 0.65
  inferred: 0.30
  ambiguous: 0.05
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T10:34:00+09:00
updated: 2026-10-26T10:34:00+09:00
snapshots:
  - "[[_raw/_archived/Outlook_2024|Outlook_2024]]"
---

# NaviSDK 2024년 활동

2025년에 시작한 해외향 [[orbis-sdk]]의 직전 해다. 2024년 메일에서 NaviSDK에 닿는 일을 모았다. 2025년 PoC 사전 검토는 [[orbis-navisdk-poc-prep-2025]]에 있다.

## 맵매칭 엔진(MMC)

- **LG AR 프로젝트용 맵매칭 엔진 1차 배포**(05-23~24): 선행기술Lab이 라이브러리와 `MMCModule.java` 변경(diff 첨부), JSON 경로 샘플을 줬다. 질의와 답변은 다음과 같다.
  - Android는 맵매칭 엔진 시작 → 맵매칭 모드 설정 → JSON 경로 설정 → 모의주행 시작 **순서**로 부르면 되고, 시작 시점에 경로 값을 미리 넣지 않아도 되도록 비정상 종료 문제를 고쳤다.
  - iOS는 debug/release가 arm64만 와서 **x86_64+arm64 universal**로 다시 받았다.
  - 신규 결과 객체(`MMCBWResult`)의 WGS84 좌표가 소수 단위(0.00x)로 들어오던 문제와 모의주행 호출 뒤 값이 안 변하던 문제를 수정했다.
- **티머니 기사앱 맵매칭 크래시**(11-14): 티머니가 강하게 클레임 중이다. 앱에서 맵매칭 시작/종료 타이밍을 몇 차례 보완했지만 해결되지 않았다. 엔진 담당은 이전에 **iM택시 앱(NaviSDK)**에서 `VirtualMMC()` 비정상 종료가 있었고, SDK를 빠르게 종료·재시작할 때 엔진이 **스레드를 정리하지 못한 채 다시 시작**해서 났다고 설명했다. 크래시 로그만으로는 재현 경로를 알 수 없어 ① 문제 버전의 앱 또는 SDK 소스, ② 티머니 앱의 맵매칭 시작·종료 시나리오를 요청했다. 앱 측은 엔진에서 크래시가 안 나게 방어해 달라고 요청했다.
- 05-16 지도 업데이트 뒤 에어 맵매칭 이상은 [[air-operations-2024]]에 있다.

## 기능 현행화

- **후면 단속 카메라 안내**(10-16): 성남 택시조합 요청을 확인하니 NaviSDK 쪽이 현행화되지 않았다. 개발·발행 2일 예상, 최신 SDK 버전에 작업한다.
- **이륜차·도보 안내**(08-07): iOS 자전거/도보 시험용 샘플앱 소스(`naviSDKSample`)를 전달했다. 이륜차·도보 안내 기능이 SDK에 들어가던 시기다. ^[inferred]
- 09-20 **루트원(차주용 모바일 앱) 구성안**: 11-06 전시회에서 FMS와 Navi SDK 솔루션을 알리려고 목업과 **Navi SDK 데모 앱**으로 제안한 상태였고 확정이 필요했다. 루트원은 [[inavi-2024-mail-overview]]의 회사 맥락 참고.

## SDK Renewal과 대만향 검토 (11~12월)

- 11-27 **SDK Renewal 스크럼**, 11-29 **NaviSDK Renewal 리뷰 및 플래닝** 회의 초대가 이어졌다. 같은 날 AIR 미션 아이데이션·기획 리뷰, 12-13 미션 기획 1차 리뷰도 열렸다. 본문은 초대장뿐이다.
- 12-04 **[개발검토요청] TomTom Overture Pjt - 대만향 NaviSDK 개발검토** 메일이 왔다. 본문은 비어 있지만 제목으로 보아 2025년 대만 PoC([[orbis-navisdk-poc-prep-2025]], [[taiwan-routeserver-api]])의 출발점으로 보인다. ^[inferred]
- 12-13 에어 교통정보 관련 탐색/CTT 이슈 확인 요청도 있었다(본문 없음).

## Open Questions

- SDK Renewal의 범위와 이것이 2025년 Orbis SDK 개발로 이어진 정확한 경로는 메일 본문이 없어 확인되지 않았다.
- 티머니 맵매칭 크래시의 최종 원인과 해결 버전은 2024 메일에 없다.

## Sources

- [[_raw/_archived/Outlook_2024.md]] — 2024 업무 메일
