---
title: >-
    서울동행맵 앱서버 개발 환경과 DB 테이블 명세
category: references
tags: [seoul-donghaengmap, backend, spring-boot, database, visibility/internal]
aliases: [앱서버 개발 환경, 동행맵 Table 명세서, 백엔드 컨벤션]
relationships:
  - target: "[[seoul-donghaengmap-functional-spec]]"
    type: related_to
sources:
  - ~/Develop/Wiki/_raw/articles/project-seoul/백엔드 환경구성/백엔드 개발 환경_아이나비시스템즈.pdf
  - ~/Develop/Wiki/_raw/articles/project-seoul/백엔드 환경구성/서울동행맵_Table 명세서_아이나비시스템즈_20260909.xlsx
summary: >-
    아이나비 앱서버의 기술 스택, 불투명 토큰 세션 인증, API·코드·DB 컨벤션과 기존 PostgreSQL 18개 테이블 대비 MySQL 신규 테이블 9개의 매핑.
provenance:
  extracted: 0.90
  inferred: 0.10
  ambiguous: 0.00
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T09:31:30+09:00
updated: 2026-10-26T09:31:30+09:00
snapshots:
  - "[[_raw/_archived/백엔드 개발 환경_아이나비시스템즈.pdf|백엔드 개발 환경_아이나비시스템즈.pdf]]"
  - "[[_raw/_archived/서울동행맵_Table 명세서_아이나비시스템즈_20260909.xlsx|서울동행맵_Table 명세서_아이나비시스템즈_20260909.xlsx]]"
---

# 서울동행맵 앱서버 개발 환경과 DB 테이블 명세

아이나비시스템즈가 맡는 **앱서버**(앱이 직접 호출하는 서버)의 개발 규약 문서(3쪽)와 DB 테이블 명세서(2026-09-09)다. 프로젝트는 [[seoul-donghaengmap]], 기능은 [[seoul-donghaengmap-functional-spec]]이다.

## 기술 스택

| 구분 | 내용 |
|---|---|
| 언어·런타임 | Kotlin 2.3, Azul Zulu JDK 25 |
| 프레임워크 | Spring Boot 4.1 (Web MVC, Security, Validation, AOP, Cache) |
| 빌드 | Gradle 9.6 (Kotlin DSL) |
| 영속 | MyBatis(어노테이션 SQL) + Spring Data JPA |
| DB | MySQL 8.0+ InnoDB, utf8mb4 |
| API 규격 | **OpenAPI 3.0.3 spec-first** — `openapi.yaml`이 단일 원천이며 서버 코드와 HTML 규격서를 생성 |
| 캐시 | JCache(Ehcache) |

## 인증

- 앱 ↔ 앱서버는 **JWT가 아니라 불투명(opaque) 토큰**을 서버 세션으로 검증한다. 전송은 `Authorization: Bearer`, 검증은 세션 테이블의 SHA-256 해시와 대조(상태 유지형). 유효기간과 재발급 없음, 후속 로그인이 세션 행을 덮어쓰고(계정/단말당 1행) 로그아웃 시 행을 삭제한다.
- 비회원도 세션 토큰을 가지며 회원 전용 API는 `MEMBER_ONLY`로 거절한다. 인증 예외는 6건(앱 초기화, 로그인, 가입, 닉네임 확인, 약관 조회·상세).
- 앱은 아로 서버를 직접 호출하지 않는다. 아로·LBS테크 연계 실패는 앱에 `EXTERNAL_API_ERROR` 하나로 내리고 원인은 서버 로그에만 남긴다.

## 컨벤션

| 영역 | 규약 |
|---|---|
| API | `/app/{도메인 복수형}/{하위}`, kebab-case, JSON camelCase, 불리언은 `~Yn` 접미 + JSON boolean, enum은 UPPER_SNAKE_CASE, 모든 응답에 `{code, message}`(`ResponseCode` 20종: 공통 6 + 도메인 14) |
| 공통 헤더 | `osType`(AOS/IOS), `osVer`, `appVer`, `appVerCode`, `device` (모두 선택) |
| 코드 | 컨트롤러 `~Cont`, 서비스 `~Svc/~SvcImpl`, 매퍼 `~Map`, 엔티티 `~Entity`, 외부 클라이언트 `~Client`. 인증은 `@AuthCheck` + AOP. XML 매퍼 미사용 |
| DB | `tbl_` 접두 snake_case 단수. `created_time`, `updated_time` 필수. PK는 앱 노출용 **UUIDv7 hex 32자 `CHAR(32)`**(ID 추측·규모 유출 방지), 내부 전용만 `AUTO_INCREMENT`. FK 제약은 만들지 않고 논리 참조로 comment에 명시, CHECK 적극 사용. 전 테이블·컬럼 한글 comment 필수. 변경 1건은 `commit.sql` + `rollback.sql` 쌍 |
| 용어 | `user_kind`(DEVICE 비회원 / MEMBER 회원), `user_type`(교통약자 유형 4종), `device_id_hash`(원문 미보관), `social_provider`(KAKAO·NAVER·GOOGLE·APPLE), `slot_kind`(HOME / GENERAL), `terms_type`(SERVICE·LOCATION·PRIVACY) |

즐겨찾기 슬롯은 HOME과 일반(1~3번)만 쓰고 WORK, WELFARE_CENTER는 ENUM에 남은 미사용 값이다. 화면기획의 "집·회사" 고정 슬롯이 v1.0에서 단순화된 흔적으로 보인다. ^[inferred]

## DB 테이블: AS-IS(PostgreSQL, 아로) → TO-BE(MySQL, 아이나비 v0.8 기준)

| 구분 | 내용 |
|---|---|
| AS-IS 18개 | 관리자, 공지사항, 지하철 정보, 에스컬레이터/엘리베이터, 즐겨찾기, 지하철역(서울), 보행자 불편지점, 광진구, 회원, 이동약자 시설물, 청계천 시설물, 커뮤니티맵, 길찾기 내역, 장애인용 화장실, 앱 버전, 전동휠체어 급속충전기, 로그인 이력, 사용자 관리 이력 |
| TO-BE 확정 9개 | `tbl_board`, `tbl_favorite`, `tbl_user`, `tbl_user_session`, `tbl_app_version`, `tbl_user_agreement`, `tbl_signup_token`, `tbl_terms`, `tbl_taxi_call` |
| 나머지 | "대응 테이블 없음 — 아로정보기술 검토 필요(관리자 웹)", "LBS Tech 편의시설 DB(WBS 4.14)", "아로정보기술 대중교통정보 DB(WBS 4.9)", "불편신고 DB(WBS 4.10, 아로·LBS테크)", "저상버스 예약 중계(WBS 4.16·BMS)" 등 파트너 담당 |

즉 앱서버는 계정·세션·즐겨찾기·약관·공지·택시 호출처럼 **앱이 직접 소유하는 데이터**만 갖고, 대중교통·편의시설·불편신고·예약은 아로나 LBS테크 쪽에서 받아 쓰는 분업 구조다. ([[seoul-donghaengmap-lbs-collaboration]]) ^[inferred]

## 감리와의 관계

감리 보고서는 컬럼정의서 312컬럼(24 테이블)의 표준 용어 준수를 점검했고, 일부 테이블의 1NF 위반과 공통코드 중복을 지적했다. ([[seoul-donghaengmap-design-audit]])

## Open Questions

- "기획 상세 발행 시 컬럼 추가 예정"이라는 메모가 있어 TO-BE 컬럼이 확정이 아닌 부분이 있다.
- 기존 앱 서버 이관(PostgreSQL → MySQL) 시점과 데이터 마이그레이션은 문서에 없다.

## Sources

- [[_raw/_archived/백엔드 개발 환경_아이나비시스템즈.pdf]] — 개발 환경과 컨벤션
- [[_raw/_archived/서울동행맵_Table 명세서_아이나비시스템즈_20260909.xlsx]] — AS-IS/TO-BE 테이블 명세
