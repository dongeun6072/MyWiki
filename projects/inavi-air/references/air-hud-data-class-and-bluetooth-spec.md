---
title: >-
    에어 HUD 데이터 클래스와 Bluetooth 전문 매핑 (NaviHUDData)
category: references
tags: [inavi-air, hud, bluetooth, spec, visibility/internal]
aliases: [NaviHUDData, HUD 규격, HUD Bluetooth 매핑, 아이허드 라이브러리 개발계획]
relationships:
  - target: "[[air-hud-integration-2023]]"
    type: related_to
  - target: "[[air-image-hud-review-2025]]"
    type: related_to
sources:
  - ~/Develop/Wiki/_raw/articles/project-air/INavi_HUD.pdf
  - ~/Develop/Wiki/_raw/articles/project-air/아이나비 규격.pdf
  - ~/Develop/Wiki/_raw/articles/project-air/아이나비 규격_전달용 bb11884f4f3541e1bff7938092dd4ecb.pdf
  - ~/Develop/Wiki/_raw/articles/project-air/아이나비 규격 데이터 예시.pdf
  - ~/Develop/Wiki/_raw/articles/project-air/Bluetooth Data_Mapping.xlsx
  - ~/Develop/Wiki/_raw/articles/project-air/아이허드_라이브러리_개발계획_20250331.pptx
summary: >-
    아이나비 에어가 HUD 단말로 넘기는 NaviHUDData 클래스(기본·TBT·안전운전·구간단속 필드), 외주사 전달용 축약본, 회전·안전운전 코드표, HUD 쪽 Bluetooth 프레임 구성과 2025년 TBT 이미지 전송 라이브러리 계획을 정리했다.
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0.00
base_confidence: 0.5
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T15:00:00+09:00
updated: 2026-10-26T15:00:00+09:00
snapshots:
  - "[[_raw/_archived/INavi_HUD.pdf|INavi_HUD.pdf]]"
  - "[[_raw/_archived/아이나비 규격_전달용 bb11884f4f3541e1bff7938092dd4ecb.pdf|아이나비 규격_전달용 bb11884f4f3541e1bff7938092dd4ecb.pdf]]"
  - "[[_raw/_archived/아이나비 규격 데이터 예시.pdf|아이나비 규격 데이터 예시.pdf]]"
  - "[[_raw/_archived/아이나비 규격.pdf|아이나비 규격.pdf]]"
  - "[[_raw/_archived/Bluetooth Data_Mapping.xlsx|Bluetooth Data_Mapping.xlsx]]"
  - "[[_raw/_archived/아이허드_라이브러리_개발계획_20250331.pptx|아이허드_라이브러리_개발계획_20250331.pptx]]"
---

# 에어 HUD 데이터 클래스와 Bluetooth 전문 매핑

[[air-hud-integration-2023]]의 라이브러리 요구 사양에서 말한 "아이나비 Class 문서와 데이터 매핑 문서"의 실제 내용이다. 앱이 약 1초마다 만드는 `NaviHUDData`를 HUD용 라이브러리가 받아 Bluetooth 전문으로 바꿔 보낸다. ^[inferred]

## NaviHUDData 구조 (내부 원본판)

| 클래스 | 역할 | 주요 필드 |
|---|---|---|
| `NaviHUDData` | 최상위 | basicData, currentTbt, nextTbt, safeData |
| `NaviHUDBasicData` | 내비 기본 정보 | 주행 화면 상태(모의 1/실제 2), 주행 상태(정상 1 고정), 도로 구분(도로 0/터널 1/지하차도 2), 주야간, GPS 수신 여부, 현위치 좌표, 현재 속도, 목적지까지 남은 거리(m)와 시간(초) |
| `NaviHUDTbtData` | 회전(TBT) 정보. 현재·다음 두 개 | 회전 지점 좌표, 거리, 회전 코드, 톨게이트 요금, 방면 명칭 |
| `NaviHUDSafeData` | 안전운전 정보 | 표출 여부, 안전운전 코드, 좌표, 남은 거리, 안전 ID, 제한속도, **구간단속**(여부, 남은 거리, 권장·평균 속도, 시간, 타입, 종료 좌표) |

- 줌, 도로 최고속도, 현위치·다음 도로명, TBT의 도로·교차로 명칭과 시간 필드는 원본에 "사용하지 않음"으로 표시돼 있다.
- **외주사 전달용 축약본**은 위 구조에서 좌표, 다음 TBT, 도로명류를 빼고 `tbtDistance`, `tbtCode` 등 HUD가 실제로 쓰는 필드만 남겼다. 현재 TBT만 있고 다음 TBT는 없다. 함께 만든 "데이터 예시" 문서는 같은 클래스에서 설명 열을 비운 형태다.
- 전달용 문서는 "Navi Hud Data 조회" 기능 하나와 데이터 매핑 엑셀을 짝으로 안내한다.

## 코드표 (전달용 문서)

- **회전 코드**: 0은 보낼 데이터 없음. 고가도로·터널·지하차도 진입, 고속도로 좌/우 진입·진출, 직진, 유턴, 좌·우회전(시계 방향 시각으로 표현), 로터리(1·3·5·7·9·11·12시 방향)로 구성된다.
- **안전운전 코드**: 주정차·버스전용차로·신호과속·과속 단속 카메라, 어린이 보호구역, 구간단속 시작(1112)/종료(1113). 구간단속 타입 필드도 이 시작/종료 값을 쓴다.

## Bluetooth 전문 매핑 (HUD 쪽)

- 프레임은 `Header(1B) + ID + Command + Data Length + Payload + Tail` 순서의 고정 헤더/꼬리 구조다. 헤더와 꼬리 바이트는 고정값이다.
- 엑셀에는 회전 코드를 HUD 아이콘 번호(직진, 좌·우회전 방향, 유턴, 고속도로 진입·진출, 로터리, 터널·지하차도·고가도로)로 바꾸는 표, "페어링 준비 완료" 응답, **TBT 메시지**(회전 코드가 0일 때 과속·신호과속·구간단속·스쿨존·주정차·버스전용 카메라 점등/소등)가 있다.
- 점등/소등 규칙은 `NaviHUDSafeData`의 표출 여부와 안전운전 코드를 매칭한 것이다. 이는 [[air-hud-integration-2023]]에서 외주사가 "점등/소등 사양"을 요청한 항목에 대응한다. ^[inferred]

## 2025 아이허드 라이브러리 개발 계획 (외주 제안)

- 2025-03-31자 외주사 문서. 핵심 기능은 앱(에어)이 라이브러리를 거쳐 HUD로 **TBT 이미지를 전송**하는 것이고, 기존 기능 유지와 안정성을 전제로 한다. [[air-image-hud-review-2025]]와 같은 흐름이다. ^[inferred]
- 프로세스: ① HUD 연결 상태 요청과 응답 → ② HUD 연결 요청, 연결, 페어링 준비 완료 → ③ TBT 이미지 전달과 응답.
- 일정: 설계, 구현, 단위 테스트, 통합 테스트를 약 2.7개월(M ~ M+2)로 잡고 Android와 iOS를 모두 범위로 한다. 단위 테스트는 테스트 앱, 통합 테스트는 에어 앱(라이브러리 포함)으로 한다.
- 클래스 설계: `HudConnection` 클래스의 `SendTBTImage(이미지 byte[], 표기 위치 type)`로 이미지를 보내며, 성공·실패는 이벤트 리스너로 돌려준다. 하드웨어 전송 방식에 따라 바뀔 수 있다고 명시했다.
- 회사 소개 슬라이드(외주사 개요와 신용 정보)는 위키에 옮기지 않았다.

## Sources

- [[_raw/_archived/INavi_HUD.pdf]] — 내부 데이터 클래스
- [[_raw/_archived/아이나비 규격.pdf]], [[_raw/_archived/아이나비 규격_전달용 bb11884f4f3541e1bff7938092dd4ecb.pdf]] — 외주사 전달용 규격(두 파일은 내용이 같음)
- [[_raw/_archived/아이나비 규격 데이터 예시.pdf]] — 필드 예시
- [[_raw/_archived/Bluetooth Data_Mapping.xlsx]] — 전문 매핑
- [[_raw/_archived/아이허드_라이브러리_개발계획_20250331.pptx]] — 2025 라이브러리 계획
