---
title: >-
    TSD A-01 (유럽향 TomTom 내비 탑재 프로젝트)
category: project
tags: [tsd-a01, tomtom, head-unit, europe, visibility/internal]
aliases: [TSD-A01, A01, HK PBV, TCI-P, 유럽향 TomTom 내비]
relationships:
  - target: "[[inavi-2024-mail-overview]]"
    type: derived_from
  - target: "[[tsd-a01-issue-log-2024]]"
    type: related_to
  - target: "[[orbis-navisdk-poc-prep-2025]]"
    type: related_to
sources: [~/Develop/Wiki/_raw/articles/Outlook_2024.md, ~/Develop/Wiki/_raw/articles/Outlook_2025.md]
summary: >-
    2024년 상반기 아이나비시스템즈가 맡은 유럽향 차량 헤드유닛용 TomTom 내비 앱 발행·검수·연동 프로젝트. 참여사 역할, 앱 발행 절차, 월별 진행을 메일에서 정리했다.
provenance:
  extracted: 0.70
  inferred: 0.28
  ambiguous: 0.02
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T10:30:00+09:00
updated: 2026-10-26T14:30:00+09:00
snapshots:
  - "[[_raw/_archived/Outlook_2024|Outlook_2024]]"
  - "[[_raw/_archived/Outlook_2025|Outlook_2025]]"
  - "[[_raw/_archived/04 MH300L_TSD_Web_Manual_KOR_Navi.pptx|04 MH300L_TSD_Web_Manual_KOR_Navi.pptx]]"
  - "[[_raw/_archived/05 MH300L_TSD_Web_Manual_KOR_Map_240102.pdf|05 MH300L_TSD_Web_Manual_KOR_Map_240102.pdf]]"
  - "[[_raw/_archived/3rd party apps_GUI_design_guide_0818.pdf|3rd party apps_GUI_design_guide_0818.pdf]]"
  - "[[_raw/_archived/a01_network.pptx|a01_network.pptx]]"
  - "[[_raw/_archived/ISA 평가루트.xlsx|ISA 평가루트.xlsx]]"
  - "[[_raw/_archived/TomTom Definition of Issue Severity.pdf|TomTom Definition of Issue Severity.pdf]]"
  - "[[_raw/_archived/TomTom Jira Ticket Report Template.pdf|TomTom Jira Ticket Report Template.pdf]]"
  - "[[_raw/_archived/ConnectedServicesPlatformGuide (2).pdf|ConnectedServicesPlatformGuide (2).pdf]]"
  - "[[_raw/_archived/TomTom-HazardsService-TechnicalSpecification-B2B-1.3.pdf|TomTom-HazardsService-TechnicalSpecification-B2B-1.3.pdf]]"
  - "[[_raw/_archived/hazards-udf-schema-v1.0.1 (2).zip|hazards-udf-schema-v1.0.1 (2).zip]]"
  - "[[_raw/_archived/TSD_A01_유럽향_VR_Navi_연동규격서_v0.6.xlsx|TSD_A01_유럽향_VR_Navi_연동규격서_v0.6.xlsx]]"
  - "[[_raw/_archived/TSD_A01_유럽향_VR_Navi_연동규격서_v0.93.xlsx|TSD_A01_유럽향_VR_Navi_연동규격서_v0.93.xlsx]]"
---

# TSD A-01 (유럽향 TomTom 내비 탑재 프로젝트)

2024년 1~7월 메일에 가장 자주 나오는 외부 프로젝트다. 유럽 판매 차량(코드명 A01)의 헤드유닛(H/U)에 **TomTom 내비 앱**을 올리고, 아이나비시스템즈는 그 앱을 받아 **검수·발행**하고 차량 시스템과 이어주는 **연동 서비스**(NaviService, ISA Reconstructor, PBVService)를 만들고 시험했다. 메일 제목에는 `TSD-A01`, `TSD A-01 EU`, `HK PBV`, `TCI-P`가 섞여 나오는데 같은 프로그램의 다른 이름으로 보인다. ^[inferred] 시험 단계별 이슈는 [[tsd-a01-issue-log-2024]]에 있다. 담당자 [[이동은]]은 모빌리티Tech그룹 소속으로 참조 수신, 시스템 업데이트 후 시험, 결과 공유에 참여했다.

## 참여사와 역할

| 참여사 | 역할 |
|---|---|
| TomTom | 내비 앱(APK) 개발, 앱 외형을 바꾸는 Chameleon 툴과 RRO 제공, 이슈 등급·Jira 보고 양식 정의 |
| 모트렉스 | 헤드유닛 시스템 SW, 컨테이너·PBVService 개발, Redmine으로 이슈 관리(등급 S/A/B/C), 현지 시험 |
| 셀바스AI | 음성인식(VR) 앱, 내비 연동 규격서 관리 |
| 42dot, 현대 | 완성차 쪽 시스템 담당(수신자로 등장) |
| 아이나비시스템즈 | 앱 발행·검수, NaviService·ISA Reconstructor 개발, 한국 내수차 시험, 가이드·매뉴얼 지원 |

## 앱 발행 절차(2024-02-07 메일 기준)

TomTom이 엔지니어링 릴리즈를 알리면 아래 순서로 진행한다.

1. TomTom APK 내려받기
2. H/U에 설치해 기본 시험(검색, 길찾기, 지도 교통정보 표출) — 약 10분
3. Chameleon 툴로 커스터마이즈한 결과 적용(이 회차는 생략)
4. NAS에 TomTom APK와 Chameleon 산출물 업로드(이 회차는 APK만)
5. 정식 발행 메일 전송

## 진행 흐름

| 시기 | 내용 |
|---|---|
| 2024-01 | Chameleon 툴 전달, 디자인 변경 항목 정리, 네트워크 상태 콜백 협의, ISA 평가 루트 공유, VR 바이너리(TTS) 수정 |
| 2024-02 | 2차 필드 시험(pre-test) 시작, 독일 지도만 담은 V0 맵 전달, ISLA 제한속도 이상, ISA 시험 경로(JIT) |
| 2024-04 | 신규 내비 앱 3.1-v140 반영, PBVService 안정화, 네트워크·교통정보 이슈, TBT 글자 크기 |
| 2024-05 | VR 경유지 추가 규격 확정, G4 사전점검에서 UUID 입력 확인, 20개 언어 매뉴얼 제작 문의, 가이드용 스크린샷 |
| 2024-06~07 | 사용자 전환·USB 업데이트 뒤 지도 미표출 원인 확인 |

이후 이 프로젝트의 메일은 2024-07 이후 나오지 않는다. 같은 TomTom을 쓰는 해외향 SDK 작업은 [[navi-sdk-2024-activity]]와 [[orbis-navisdk-poc-prep-2025]]로 이어진다. ^[inferred]

## 2025년 후속 메일

- **What3Words(W3W) 양산 적용**(02-28 ~ 05-15): 현대향 A01에 W3W를 넣는 방안 검토 요청이다. 모트렉스가 최신 SW·지도 DB·VR DB를 공유했고 부팅 로고를 현대로 바꾼 variant 진행이 필요했다. 05-15 셀바스AI가 **번역본과 UX 사양서를 반영한 VR 바이너리**를 보냈고 리소스가 추가돼 전체 설치가 필요하다.
- **PBV 소프트웨어 릴리즈**(03-26): TomTom이 UK 관련 PBV 소프트웨어 **7.0-v442**를 릴리즈했다. 직전 SOP 소프트웨어에 W3W만 추가해 별도 릴리즈 노트는 없다.
- **ISA 재평가**(10-23): 유럽 연구소 담당이 같은 시나리오를 다시 시험했고 기존 ISLA 이슈는 재현되지 않았다. 한편 전방 카메라가 일부 표지판을 암묵 표지로 오인식한 로그 분석 건이 있었다. → [[tsd-a01-issue-log-2024]]
- **TomTom 유럽 지도 납품**(11-20): 11월 공식 유럽 지도(NDS 4.0.0, 약 20.6GB)가 납품됐다.
- **TomTom ANA 6.0 시험**(12-04): 앱 설치·실행은 성공했으나 타깃 단말에서 지도가 안 떴다. 로그상 **호스트 해석 실패**여서 DNS 설정 문제로 판단했고(IP 직접 ping은 성공), 단말 시스템 SW가 이전 AMS 시험 시기 버전이라 모트렉스 확인이 필요하다. 태블릿에서는 정상이었고 설정의 온라인 지도 항목이 타깃에서는 '구독하지 않음'으로 나왔다.

## 관련 문서(st1 폴더 수집분)

- [[tsd-a01-vr-navi-interface-spec]] — VR 앱과 내비 사이 Android Intent 연동규격(v0.6, v0.93)
- [[tomtom-connected-services-and-hazard-warnings-spec]] — TomTom B2B 전달 플랫폼(Kafka/Protobuf)과 Hazard Warnings, UDF 스키마
- **TomTom 이슈 관리 문서**: 이슈 등급은 S(안전, 차량 설계 영역 밖 동작 등) / A(Showstopper, 지도·검색·경로 전면 불능, 충돌, 클라우드 연결 불가) / B(Major, 부분 기능 손실·성능 저하) / C(Minor, 번역 오류·경미한 UI)로 정의된다. Jira 보고 양식은 버그(재현 절차·SW/지도 버전·발생률·**logcat 필수**, ANR 로그, DLT는 디버그 로그가 걸러져 부적합)와 개선 요청(사용 사례·배경·운전자 불만 여부)으로 나뉘고, 클라이언트 SDK 이슈는 호출 API·파라미터·응답·기대 응답·버전을 적는다. 모트렉스의 S/A/B/C 등급 관리와 같은 체계다. ^[inferred]
- **서드파티 앱 GUI 디자인 가이드(TCI-P)**: 모트렉스 배포. 라인 타입 그래픽, 지정 폰트(New HD2.1 Regular/Medium)와 지정 포인트 컬러만 허용, 텍스트 색은 Normal/Press/Focus/Focus Press 상태별 정의, 버튼은 흰색 17%/7% 투명도 효과, 아이콘은 라인 타입에 모서리 R값 적용.
- **네트워크 구성도(a01_network)**: 호스트(Linux) 위에 VR, TomTom, Android 컨테이너가 있고 eth0/eth1과 DCU, APN0~3, 브리지로 연결되는 안드로이드 컨테이너 네트워크 도식이다(세부 주소 미수록).
- **ISA 평가 루트**: 독일 내 출발·도착과 경로 옵션(고속도로 회피 포함), 거리·시간, 고속/국도/시내 구간 비율을 적은 **주행 시험 경로표**다. 인사 평가 문서가 아니다. 주소는 옮기지 않는다.
- **MH300L TSD 웹 매뉴얼(내비·지도 편)**: 국내 TMAP AUTO 기반 내비 사용자 매뉴얼. 검색/경로 화면, 통합·주소·카테고리 검색(전기차 충전소는 배터리 잔량 기준 도달 가능 범위 검색, 도착 시 예상 잔량 표시), 최근 목적지 편집(즐겨찾기·상단 고정·삭제), 지도 설정을 다룬다. Navi 편 pptx는 서식 틀만 있고 본문이 비어 있다.

## Open Questions

- 본문이 "약"만 남은 메일이 일부 있고, 인용이 겹쳐 있어 일정의 정확한 선후는 확인하지 못했다.
- 최종 출시 여부와 시기는 메일에 없다.

## Sources

- [[_raw/_archived/04 MH300L_TSD_Web_Manual_KOR_Navi.pptx]]
- [[_raw/_archived/05 MH300L_TSD_Web_Manual_KOR_Map_240102.pdf]]
- [[_raw/_archived/3rd party apps_GUI_design_guide_0818.pdf]]
- [[_raw/_archived/a01_network.pptx]]
- [[_raw/_archived/ISA 평가루트.xlsx]] — 시험 경로표
- [[_raw/_archived/TomTom Definition of Issue Severity.pdf]]
- [[_raw/_archived/TomTom Jira Ticket Report Template.pdf]]
- [[_raw/_archived/ConnectedServicesPlatformGuide (2).pdf]]
- [[_raw/_archived/TomTom-HazardsService-TechnicalSpecification-B2B-1.3.pdf]]
- [[_raw/_archived/hazards-udf-schema-v1.0.1 (2).zip]]
- [[_raw/_archived/TSD_A01_유럽향_VR_Navi_연동규격서_v0.6.xlsx]]
- [[_raw/_archived/TSD_A01_유럽향_VR_Navi_연동규격서_v0.93.xlsx]]
- [[_raw/_archived/Outlook_2024.md]] — 2024 업무 메일
