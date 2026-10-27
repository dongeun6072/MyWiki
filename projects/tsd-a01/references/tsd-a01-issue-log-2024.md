---
title: >-
    TSD A-01 이슈 로그 (2024): ISA, VR 연동, PBVService, 지도 미표출
category: references
project: tsd-a01
tags: [tsd-a01, tomtom, isa, voice-recognition, android, visibility/internal]
aliases: [A01 이슈, ISA Reconstructor, ISLA 이슈, PBVService, Chameleon 툴]
relationships:
  - target: "[[tsd-a01]]"
    type: related_to
  - target: "[[inavi-2024-mail-overview]]"
    type: derived_from
sources: [~/Develop/Wiki/_raw/articles/Outlook_2024.md]
summary: >-
    TSD A-01 시험 중 나온 기술 이슈와 원인·조치: Chameleon 커스터마이즈, ISA/ISLA 제한속도, VR 연동 규격, 멀티유저 DB, 심볼릭 링크 지도 미표출, 네트워크·시간 문제.
provenance:
  extracted: 0.80
  inferred: 0.18
  ambiguous: 0.02
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T10:31:00+09:00
updated: 2026-10-26T10:31:00+09:00
snapshots:
  - "[[_raw/_archived/Outlook_2024|Outlook_2024]]"
---

# TSD A-01 이슈 로그 (2024)

[[tsd-a01]] 메일에서 원인이나 조치가 적힌 이슈만 골랐다. 사람 이름과 연락처, 공유 링크는 옮기지 않았다.

## Chameleon 툴(TomTom 앱 외형 변경)

- 2024-01-09 TomTom이 GUI 변경 툴을 전달했다. 설치 파일(msi)로 깔고, 설정 파일(chc)은 **APK와 쌍**이어서 새 APK가 나올 때마다 같이 릴리즈된다.
- 툴로 바꾼 내용은 별도 **runtime object** 파일로 나오고, 이 파일을 H/U에 설치해야 앱 실행 때 적용된다. 새 버전이 나오면 이전 산출물을 툴에서 불러와 새 APK/chc에 다시 적용할 수 있다.
- 신규 APK 3.1-v140은 기존 RRO(automotive-customization 2.1-v123)와 호환됐다. RRO 활성화는 `cmd overlay enable --user current <패키지>` 형태이고, 초기 안내에 하이픈 하나가 빠진 오타가 있었다(04-09).
- 디자인 요구: 완성차 폰트와 테마 색 적용, 아이콘 교체(경로 설정 화면 설정 아이콘을 톱니바퀴로, 즐겨찾기 아이콘을 테마와 무관하게 파란색으로). 툴로 안 되면 넘어가기로 했다.
- 04-23 TBT 화면의 "Finding best route" 글자가 "Applying"보다 작다는 지적이 나와 툴에서 **28pt를 32pt로** 바꾸도록 안내했다.

## ISA / ISLA (제한속도 안내)

- ISA Reconstructor는 TomTom 내비가 CAN 형태로 보내는 값을 받아 **재구성한 뒤 H/U로 전달**하는 서비스다. ^[inferred]
- 02-16 유럽 연구소 근처 시험에서 ISLA 제한속도가 **50으로 고정**되고 LinkClass가 `Arterial_Country`로 나왔다. 로그 확인 결과 Reconstructor는 TomTom이 보낸 **FRC(Functional Road Class) 2 또는 3**을 Arterial Country로 판단하므로, 그 위치에서 이 값이 오는 것이 맞는지 TomTom에 확인을 요청했다.
- 51 버전부터 태블릿에서는 ISA 데이터가 오지 않고 목표 단말에서만 받았다.
- 02-26 `adasis-android 1.1.35+15.160` 라이브러리를 반영한 시험용 APK를 전달했다. 내부 시험은 정상이었지만 데이터는 크게 달라지지 않았다.
- ISA 시험 경로(03-01 JIT): 고속 86.3km, 비도시 24.4km, 도시 55km. 유럽차가 G3를 시험하는 동안 내수차로 같은 코스를 돌았다.
- 01-30 모트렉스가 NaviService와 ISA Reconstructor에 **난독화가 안 걸렸다**고 알려 와서 옵션을 바꿔 다시 전달했다. 적용 여부는 jadx-gui로 확인한다.

## VR(음성인식) 연동

- 셀바스AI가 연동 규격서를 관리한다(01-31 v0.6, 05-20 v0.93). 01-12에 `ReqRoute`에 **목적지 여부 값**이 추가됐고, 01-31에 **내비 부팅 완료 여부** 규격이 들어갔다.
- 01-19 수정: 업데이트 뒤 VR이 동작하지 않는 문제, 내비 연동 시 Home 등록 실패, 검색어를 search-phrase로 전달. 01-23에는 TTS 연동 이슈를 모트렉스 가이드대로 고쳤다(1.0.5). 해결된 이슈는 터치 안 됨과 내비 음성 안 나옴이고, 내비 사운드가 작아 **Navi Sound 설정**이 아이나비 쪽 작업으로 남았다.
- 05-20 경유지 추가 시나리오 2안: VR이 내비에 경유지 추가를 요청하고 **30초 동안 성공/실패 이벤트가 없으면** `ReqAddWaypointCancel`을 보내고 VR을 종료하며 TomTom 경로 탐색을 취소한다. 또 serviceConnector에 VR 프로세스 감지 기능을 넣어 내비 쪽 커넥터만 교체해 시험하도록 했다.

## PBVService와 멀티유저

- 04-11 유럽 시험차에서 PBVService가 NaviService DB를 읽다 죽는 문제를 모트렉스가 **죽지 않게** 고쳤다. 그래도 NaviService가 `getCurrentAddress()`를 null 객체에 호출해 NPE가 났다.
- 원인 추정 셋: ① 1·2호차의 이전 버전은 현재 위치를 DB에 갱신하지 않았고 3호차는 갱신해서 증상이 달랐다. ② Android는 멀티유저라 DB 파일이 사용자별인데 **새 사용자는 DB 파일이 생성되지 않았다**. ③ v140 반영 때는 master update로 이전 DB가 사라진 것이 원인이어서 TomTom 문제가 아니었다. 조치는 DB 파일 강제 삭제 후 재생성 확인이었다.

## 지도가 안 뜨는 문제 (06-17 ~ 07-18)

- 지도 업데이트나 USB 업데이트 뒤 지도가 표출되지 않았다. 부팅 후 내비 **자동 실행** 문제도 의심해 자동 실행을 켜고 끄는 테스트 앱(PBVService)을 받았다.
- 07-18 원인: TomTom은 지도가 **한 곳에만** 있어야 정상 표출한다. 권한 문제로 Data 폴더를 사용자별 **심볼릭 링크**로 바꿔 쓰고, 물리적으로는 `mapdata` 아래 Data1, Data2에 지도가 둘 다 있었다. TomTom은 `ROOT.NDS` 파일 존재로 지도를 판단하므로 **현재 사용자의 폴더에만 `ROOT.NDS`가 있게** 하면(다른 쪽은 임의 이름으로 변경) 정상 동작했다. 사용자 전환 때마다 이름을 바꿔 주는 로직을 서비스 스크립트에 넣자는 제안이다.

## 네트워크와 시간

- 01-12 TomTom이 요청한 **네트워크 상태 체크 콜백**을 시스템이 Android 표준으로 제공하지 못한다고 결론 났다. 시스템이 Custom API를 제안했고(값은 CarProperty가 아니라 Settings Provider로 제공), 아이나비 쪽 작업은 없지만 TomTom 요청 시 대응이 필요하다.
- 02-13 0205 시스템 SW 설치 뒤 네트워크가 되지 않아 현지 시험이 불가능할 수 있어, 새 V0 맵에서 **독일 지역만** 내려받은 1.6GB 버전을 전달했다.
- 04-18 시스템 업데이트 뒤 교통정보가 안 나오고 지도 다운로드/삭제도 되지 않았다. 확인된 원인은 ① 도메인 적용 시 **화이트리스트가 정상 처리되지 않음**(IP로 등록하면 정상), ② **H/U 시간이 현재와 맞지 않으면 교통정보 연동이 안 됨**이었다. 그 뒤 추가 확인 없이 다른 업무를 진행하기로 했다.

## UUID와 문서

- 05-23 G4 사전점검에서 H/U에 UUID를 입력하는 방법(`fwinfo.ini`)을 시험해 설정됨을 확인했다. 가이드의 예시가 15자리였지만 **16자리**여야 적용됐고, EngineerMode > System > VersionInfo에서 확인한다.
- 01-31 TomTom이 **이슈 등급 정의**(모트렉스는 S/A/B/C)와 **Jira 티켓 보고 템플릿**을 보냈다. 신규 티켓은 영어로 쓰고 가능한 한 템플릿 항목을 채워 달라는 요청이다.
- 05-28 모트렉스가 TomTom에 **20개 언어 전체 번역 매뉴얼**과 **영어만** 두 안의 비용·일정을 물었다. 05-29 국문 가이드 초안용 스크린샷을 전달했다.

## Open Questions

- ISLA 50 고정 문제를 TomTom이 어떻게 답했는지는 메일에 없다.
- 심볼릭 링크 로직이 실제 서비스 스크립트에 반영됐는지는 확인되지 않았다.

## Sources

- [[_raw/_archived/Outlook_2024.md]] — 2024 업무 메일
