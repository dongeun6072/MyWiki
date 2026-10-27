---
title: >-
    MXI Where 버전 이력과 OTA 배포 절차 (2022)
category: references
tags: [hybrid-navi, mxi, release, ota, visibility/internal]
aliases: [MXI 버전 발행, Where OTA, MXI 빌드 방법, 가오픈]
relationships:
  - target: "[[mxi-field-incidents-2022]]"
    type: related_to
sources: [~/Develop/Wiki/_raw/articles/Outlook_2022.md]
summary: >-
    MXI 단말용 inavi WHERE의 2022년 버전 이력(V2.3.3~2.4.1), 버전 번호 규칙과 빌드 방법, OTA 가오픈과 상용 오픈 절차, 최종 시험 결과, 10월 핫패치 항목.
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

# MXI Where 버전 이력과 OTA 배포 절차 (2022)

[[inavi-hybrid-navi]]의 MXI 단말용 앱 배포 기록이다. 장애 쪽 이력은 [[mxi-field-incidents-2022]]에 있다. [[이동은]]은 **앱 발행 정보 전달과 OTA 가오픈 테스트**를 맡았다.

## 버전 이력

| 버전 | 시기 | 내용 |
|---|---|---|
| V2.3.3 (B2210), V2.3.4 (B2213) | 06-09 ~ 06-17 | 서비스 중. 발행 메일에 릴리즈 노트, 솔루션 연동 인터페이스 문서(Where 연동 Android 인터페이스 V1.0.4) 첨부 |
| **V2.4.0 (B2260)** | 06-17 발행, **07-05 14:00 OTA** | 서울시설공단 patch 포함(현위치 Positioning 사양 변경). 이번 업데이트는 OTA로만 진행 |
| **V2.4.1 (B2282)** | 09-28 발행, **10-06 14:00 상용 오픈** | 10월 핫패치 |

함께 배포하는 하위 앱: `TW_happywayard.apk`(v3.8, code 108), `TW_tbt.apk`(1.0.B1399).

### 10월 핫패치 항목 (V2.4.1)

- 기본 탐색 옵션 변경(기본: **최소시간**)
- 내비가 Foreground로 올 때 Broadcast 전달
- 비정상 종료 수정(GPS null → NPE, null 체크)

OTA 날짜는 **10월 6일**로 정했다. 10월 5일에 지도 업데이트가 있어 같은 날 둘을 하면 이슈가 생길 수 있었기 때문이다. 하남은 SD 카드로 Where를 설치하는 작업은 하지 않고 OTA로 업데이트하기로 했다.

## 버전 번호와 빌드 방법 (06-17)

| 항목 | 규칙 |
|---|---|
| `versionName` `a.b.c` | a: 대규모 업데이트(거의 안 올림), b: 새 기능 추가 시(1자리), c: 버그 수정·검증 차수 추가(2자리). `app` 모듈 `build.gradle`에서 수정 |
| `versionCode` | 깃랩 소스트리에서 자동 추출. **정식 빌드 전 소스 커밋 필수** |
| 정식 배포 빌드 | `gradlew buildmooserelease` |

## OTA 절차

1. 앱 발행 정보를 OTA 담당에게 전달: OEM, APK, versionName, versionCode, 파일 크기
2. **OTA 가오픈 테스트**: APK 서버에 올린 뒤 어드민 페이지에서 가오픈. 테스트 단말은 OEM(예: `MSE`)과 시리얼로 등록 요청(웹마케팅팀)
3. 가오픈 후 회사 내부망으로 인터넷에 연결해 단말 테스트
4. 상용 오픈(어드민 페이지에서 시각 지정, 보통 화·목 14:00). 하루 전에 한 번 더 공지
5. 개발 서버 OTA 테스트 후 특이사항이 없으면 상용 오픈(아트뷰 2종도 같은 방식)

## 최종 시험 결과 (MXi 출시, 2022-08-12)

| 대상 | 전체 | PASS | FAIL | N/T | 합격률 |
|---|---|---|---|---|---|
| OS (펌웨어 `ULG18`) | 458 | 458 | 0 | 0 | 100% |
| Where (v2.4.0 B2260) | 102 | 102 | 0 | 0 | 100% |

- Web 서비스 예정일 2022-09-01, 양산 적용은 **9월 출하 물량 2.5K(2,500대) 생산분부터**(신규 SMT분)
- 펌웨어 개선: PMIC(nxe2000, axp228) 동시 지원, 부팅 중 `/data` fsck, recovery fsck 설정 메뉴, Side Command와 ServiceX 앱 적용
- Where 설치 파일 크기 약 89.5MB, 지도 데이터는 기존 양산 버전(22.07a) 적용 요청

## 펌웨어 릴리즈 (참조)

MXI 펌웨어 `MSE.ULF24`(2022-07-01), `N2G48H.MSE.ULG18`(07-21)이 SW개발본부에서 배포됐다. 사용자 버전과 개발 버전이 따로 있어 보유 단말에 맞게 골라 쓴다.

## Open Questions

- OTA 어드민 사이트와 APK 서버의 위치·계정은 메일에 있으나 위키에는 적지 않았다.

## Sources

- [[_raw/_archived/Outlook_2022.md]] — 2022 업무 메일
