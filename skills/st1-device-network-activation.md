---
title: >-
    ST1 단말 네트워크 활성화와 ANA 앱 실행
category: skills
tags: [tomtom, st1, embedded, howto, visibility/internal]
aliases: [네트워크 활성화, ANA 앱 실행, ST1 네트워크 설정]
relationships:
  - target: "[[이동은]]"
    type: related_to
sources: [~/Develop/Wiki/_raw/articles/project-sdk/st1/네트워크 활성화.md]
summary: >-
    ST1 개발 단말(Linux+Android)에서 네트워크 설정 파일을 교체하고 시간을 맞춘 뒤 TomTom ANA 테스트 앱을 실행하는 순서.
provenance:
  extracted: 0.90
  inferred: 0.10
  ambiguous: 0.00
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: peripheral
created: 2026-10-26T09:25:23+09:00
updated: 2026-10-26T09:25:23+09:00
snapshots:
  - "[[_raw/_archived/네트워크 활성화|네트워크 활성화]]"
---

# ST1 단말 네트워크 활성화와 ANA 앱 실행

개발자가 직접 쓴 짧은 작업 메모다(2025-12). 실행 순서가 중요하다: **네트워크 설정 → 시간 설정 → 앱 실행**(이때 UUID가 유효한지 확인). 단말은 Linux(LXC 컨테이너 설정이 있는 쪽)와 Android 환경이 함께 있는 차량용 개발 보드로 보이며, 앱 패키지 이름이 TomTom 차량 통합 테스트 앱이다. ^[inferred] 이 메모는 2024년 TomTom 프로젝트 경험([[이동은]])과 같은 계열 업무로 보이지만 어느 프로젝트의 문서인지는 직접 적혀 있지 않다. ^[ambiguous]

## 1. 네트워크 설정 (Linux 쪽)

1. `/etc/lxc/lcp` 폴더로 이동
2. `mount -o remount,rw /` 로 루트를 읽기/쓰기 모드로 다시 마운트
3. 기존 설정을 백업: `lcp_eur_net_config` → `lcp_eur_net_config_back`
4. 기본 설정을 유럽 설정 이름으로 교체: `lcp_default_net_config` → `lcp_eur_net_config`
5. `reboot -f` 로 재부팅

원본과 활성화 후의 `/etc/lxc/lcp/` 폴더 모습은 스크린샷 2장으로 남겨 두었는데, 이미지는 이전 vault에 있고 새 vault로 옮기지 않았다.

## 2. 시간 설정

`date MMDDhhmm[[CC]YY][.ss]` 형식. 예) `date 12100203.01`. 시간이 맞지 않으면 인증이 실패할 수 있다. ^[inferred]

## 3. ANA 앱 실행 (Android 쪽)

1. 최신 APK 다운로드(ANA, VilTest)
2. Android 환경에 APK 설치
3. 테스트 액티비티 실행: `am start -S -n com.tomtom.automotive.integration.vehicle.testApp/.VehicleIntegrationTestActivity`
4. 토큰 파일 복사: `/data/token.json`을 앱의 `files/token.json`(`/data/media/10/Android/data/<패키지>/files/`)으로 복사
5. 토큰 파일 권한 변경: `chmod 777 token.json`

## 주의

- 네트워크 파일 교체와 `chmod 777`, `reboot -f`는 **개발 단말에서만** 쓴다. 상용 단말에는 적용하지 않는다. ^[inferred]
- 토큰 파일(`token.json`)은 인증 정보라서 저장소에 올리지 않는다.

## Sources

- [[_raw/_archived/네트워크 활성화.md]] — 작업 메모 원본
