---
title: >-
    셀 보안 사고 교훈
category: concepts
tags: [company, security, incident, secrets, visibility/internal]
aliases: [키 유출 교훈, 서비스 키 교체]
relationships:
  - target: "[[entities/모빌리티개발셀]]"
    type: derived_from
  - target: "[[concepts/public-security-vulnerability-check-guides]]"
    type: related_to
summary: >-
    모빌리티개발셀에서 공유된 보안 사고와 조치(타사 AWS 키 탈취 사고 전달, SDK 앱 키 포함 배포 제거, 오르다 서버 침입, 방화벽·접근 정리)에서 뽑은 실무 원칙.
provenance:
  extracted: 0.6
  inferred: 0.4
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

# 셀 보안 사고 교훈

[[entities/모빌리티개발셀]]에서 공지된 사건을 시간순으로 적고 원칙을 뽑았다. 값(키, 주소)은 적지 않는다.

## 사건

| 날짜 | 내용 | 조치 |
|---|---|---|
| 2026-03-05 | 전산팀이 사용하지 않는 서버 방화벽을 닫는 중. 외부 근무용 접근 이력이 있는 포트의 사용 여부 확인 요청 | 사용자별 확인 |
| 2026-07-02 | 오르다 서비스 서버에 외부 침입 이슈. 고객정보 유출은 없다고 확인 | 로그인·FCM 키 등 교체 가능성 공유 |
| 2026-08-11 | 지도 SDK(compose)의 0.1.11 미만 버전에 앱 키가 포함되어 배포됨 | 해당 버전을 저장소에서 제거, 0.1.11로 올리도록 안내 |
| 2026-09-16 | 타사 개인정보 유출 사고가 AWS 키 탈취로 추정된다는 기사 | 형상관리 소스에 인증키 등 민감 정보를 넣지 않도록 부문 전달 |
| 2026-09-11 | 공용 계정에 이중 인증 적용 | 백업 코드 방식으로 운영 |

## 원칙

1. 소스 저장소와 배포 산출물(AAR, POM, 패키지)에 키·토큰이 들어가지 않게 한다. 한 번 배포되면 지워도 이미 받은 사람에게는 남으므로 키 교체가 필요하다. ^[inferred]
2. 서비스 키를 교체하는 절차를 미리 정해 둔다(로그인, FCM 등). 침입 이슈 때마다 즉흥 교체가 되지 않게 한다. ^[inferred]
3. 오래된 방화벽 규칙과 포트는 정리하고, 사용 이력이 있으면 사용자에게 확인한다.
4. 공용 계정은 비밀번호를 채널에 올리지 않고, 이중 인증과 세션 만료를 쓴다. 비밀번호가 대화창에 올라온 이력이 있었다는 점이 이 위키에서 가장 크게 경계할 부분이다.
5. 슬랙 웹훅 URL, 서드파티 앱·MCP 연동은 보안 정보로 보고 권한을 셀장이 관리한다([[references/cell-ai-tools-and-licenses]]).

## 이 위키에서의 대응

이 vault에도 2026-10-26에 비슷한 사고가 있었다(카드번호·서비스 키가 원격에 올라감). 규칙은 `CLAUDE.md`의 보안 절차를 따른다.

## Sources

- 슬랙 `#모빌리티개발셀`(2026-03~09).
