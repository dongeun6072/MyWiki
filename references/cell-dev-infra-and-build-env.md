---
title: >-
    셀 빌드·배포 인프라
category: references
tags: [company, build, ci, infrastructure, distribution, visibility/internal]
aliases: [빌드맨, 원격 빌드 캐시, 배포 그룹, 공용 개발 계정]
relationships:
  - target: "[[entities/모빌리티개발셀]]"
    type: derived_from
summary: >-
    모빌리티개발셀이 쓰는 빌드 서버(빌드맨), Gradle 원격 캐시, SDK 저장소, 앱 배포 그룹, 공용 개발 계정 운영 이력과 주의점. 서버 주소·계정은 수록하지 않는다.
provenance:
  extracted: 0.8
  inferred: 0.2
  ambiguous: 0.0
base_confidence: 0.47
lifecycle: draft
lifecycle_changed: 2026-10-27
tier: supporting
created: 2026-10-27
updated: 2026-10-27
sources:
  - "slack:#모빌리티개발셀"
---

# 셀 빌드·배포 인프라

[[entities/모빌리티개발셀]]의 개발 환경 공지를 정리했다. 서버 주소, 포트, 계정은 채널에 있었지만 **미수록**이다.

## 빌드 서버(빌드맨)

- 본사 Jenkins 맥미니가 2024-04에 오프라인이 된 적이 있다. 접속이 안 되면 담당 자리의 맥미니 상태를 먼저 점검한다.
- 2026-05~06 인텔 빌드맨의 프로젝트를 M1 맥 빌드맨으로 옮기고 인텔 쪽은 포맷했다. 외부 접속용 무료 터널이 한도를 넘어 내부 접속으로 바꿨고, 보안 프로그램(CWP) 때문에 변동 IP만 접근 가능했다가 6/2 고정 IP 할당과 6/11 NAC 인증으로 복구됐다. 외부 터널은 Bitbucket 웹훅과 원격 근무 때만 쓴다.

## Gradle 원격 빌드 캐시 (2026-10-07 오픈)

- 한 사람이 빌드한 컴파일·ktlint 결과를 팀이 공유한다. 사내망에서만 접속되고 인증이 없다.
- 설정은 `settings.gradle.kts`에 `buildCache { remote<HttpBuildCache> { ... isPush = true } }`를 넣고 `gradle.properties`에 `org.gradle.caching=true`를 둔다. http 주소라 `isAllowInsecureProtocol = true`가 필요하다.
- 외부망에서는 원격 캐시 연결이 실패하지만 빌드는 로컬로 계속된다. 연결 확인은 없는 키를 요청해 404가 오는지 본다.

## SDK 저장소·배포

- 자사 모바일 SDK를 서비스하는 아티팩트 저장소는 2026-05 서버 이전 예정이 공지됐고, 2026-10-07 보안 취약점 패치로 다운로드가 일시 끊겼다. 2026-09-09에는 메모리 부족이 간헐적으로 생겨 배포 사이트 접속을 자제해 달라는 공지가 있었다.
- 2026-07-22 아이나비 지도 CMP 버전 라이브러리를 Maven 저장소에 배포해 프로젝트별 SDK 직접 연동이 필요 없어졌다 → [[concepts/kmp-cmp-adoption]].
- 2026-10-06 중공업 협력사 SDK가 POM 없이 AAR 단독으로 배포 검토된 이력이 있는지 셀장이 다른 담당자들에게 문의했다.

## 앱 배포·테스트 그룹

- 2026-03-04 운영 중인 App Store Connect 계정 두 곳(아이나비시스템즈, 팅크웨어)에 셀 배포 그룹을 만들었다. 자동 배포는 꺼 두어 배포할 때 해당 그룹을 추가한다.
- 안드로이드는 Firebase App Distribution, iOS는 TestFlight로 내부 테스트를 한다. 2025-09 사내 베타 서비스(미션 3개)도 같은 방식이다.
- 2026-09-10 App Store Connect 라이선스 계약이 갱신되어 이사 승인이 필요했다(10/2까지).

## 공용 개발 계정

- 2023-09부터 애플·구글 공용 개발 계정에 2단계 인증이 걸려, 인증코드를 받는 기기 소지자의 승인 없이는 로그인할 수 없었다. 2026-09 이중 인증이 필수가 되어 백업 코드를 나눠 쓰고, 소진되면 재발급하는 방식으로 운영했다.
- 2026-05-22 공용 구글 계정에 연결된 서비스를 조사했고(Figma dev seat, Google Remote, App Distribution 테스터, Apple, Kakao, Flutter Pub, ChatGPT 무료), 6·7월에 비밀번호를 바꾸고 세션을 만료시켰다. 7-14에 셀은 미사용 계정으로 정리했다. 자격 정보는 캔버스로 공유했을 뿐 위키에 두지 않는다.

## 클라우드

- 2026-01 클라우드 크레딧을 그룹 예산(월 약 15만 원)으로 편성, 후보는 AWS, Supabase, Firebase. 비용은 [[concepts/cell-budget-and-expense-policy]].

## Sources

- 슬랙 `#모빌리티개발셀`(2023-09~2026-10).
