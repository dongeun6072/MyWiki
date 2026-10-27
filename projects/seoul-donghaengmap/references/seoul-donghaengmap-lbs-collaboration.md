---
title: >-
    LBS테크 협업 자료 (AR-Navi 서버, 내비 패키지)
category: references
tags: [seoul-donghaengmap, lbs-tech, navigation, pedestrian, visibility/internal]
aliases: [LBS테크, AR-Navi, 보행 경로 서버, pathfinder]
relationships:
  - target: "[[seoul-donghaengmap-functional-spec]]"
    type: related_to
sources:
  - ~/Develop/Wiki/_raw/articles/project-seoul/LBS Tech/협업자료_(주)엘비에스테크/내비게이션_서버 DB_규격서.pdf
  - ~/Develop/Wiki/_raw/articles/project-seoul/LBS Tech/협업자료_(주)엘비에스테크/내비게이션_참고문서.pdf
  - ~/Develop/Wiki/_raw/articles/project-seoul/LBS Tech/협업자료_(주)엘비에스테크/네비게이션 api 문서/openapi.json
  - ~/Develop/Wiki/_raw/articles/project-seoul/LBS Tech/협업자료_(주)엘비에스테크/2026 서울동행맵 WBS_(주)엘비에스테크.xlsx
summary: >-
    보행 약자 경로·POI 서버를 제공하는 LBS테크의 AR-Navi 백엔드(Node/PostGIS/Cloud Run), pathfinder API, Flutter 내비게이션 이벤트 패키지, 자체 WBS를 정리했다.
provenance:
  extracted: 0.88
  inferred: 0.12
  ambiguous: 0.00
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T09:31:30+09:00
updated: 2026-10-26T09:31:30+09:00
snapshots:
  - "[[_raw/_archived/내비게이션_서버 DB_규격서.pdf|내비게이션_서버 DB_규격서.pdf]]"
  - "[[_raw/_archived/내비게이션_참고문서.pdf|내비게이션_참고문서.pdf]]"
  - "[[_raw/_archived/openapi.json|openapi.json]]"
  - "[[_raw/_archived/2026 서울동행맵 WBS_(주)엘비에스테크.xlsx|2026 서울동행맵 WBS_(주)엘비에스테크.xlsx]]"
---

# LBS테크 협업 자료 (AR-Navi 서버, 내비 패키지)

보행 약자 경로 안내를 제공하는 **LBS테크**가 컨소시엄에 전달한 자료다. 앱서버가 이 서버를 호출해 도보 경로와 POI를 받는다. ([[seoul-donghaengmap-backend-env]]) 프로젝트는 [[seoul-donghaengmap]]이다. 접속 URL과 운영 자격증명은 이 페이지에 적지 않았다.

## AR-Navi 백엔드 (서버·DB 규격서 v1.0, 대외용)

| 항목 | 내용 |
|---|---|
| 형태 | GCP 위의 단일 REST API 서버(Node.js + Express, TypeScript) |
| DB | PostgreSQL(Cloud SQL) + **PostGIS** + **pgRouting**. 스키마 `navi`(회원, POI, 리뷰, 즐겨찾기, 공지, 문의), `pedestrian`(서비스별 보행 경로 그래프 edge·vertex) |
| 저장소·알림 | Cloud Storage(이미지), Firebase Cloud Messaging(공지·문의 답변) |
| 실행 | Cloud Run(리전 asia-northeast3), 소스 push → Cloud Build → 자동 배포 |
| API 도메인 12개 | `/pathfinder`(전동·수동·시각 접근성 가중 보행 경로), `/pois`, `/users`, `/reviews`, `/favorites`, `/notice`, `/qna`, `/status`(점검 여부, 최소 버전), `/reports`(POI 접근성 정보 신고), `/travel`, `/city`, `/stech`(검수 완료 POI) |

## 외부 API (AR-Navi OpenAPI 1.0.0, 모든 요청에 `x-api-key`)

| API | 설명 |
|---|---|
| `GET /pathfinder` | 두 지점 사이 최적 보행 경로(GeoJSON). 파라미터 `startX/Y`, `endX/Y`, `option`, `service`(blind / auto / manual), `srid` |
| `POST /pois/origins`, `GET /pois/origin/{origin_id}` | 원천 ID로 POI 기본정보(일괄/단건) |
| `GET /pois/search` | 키워드 검색(BBox 또는 중심+반경, 접근성 필터, 페이징) |
| `GET /pois/bounds` | BBox 안 POI(카테고리, 반경, 접근성 필터) |
| `GET /pois/{poi_id}/poidetails` | 접근성 상세, VPS, 파일 |
| `GET /pois/nearest` | 좌표 기준 500m 최근접 POI 1건 |

## 내비게이션 이벤트 패키지 (Flutter, 참고문서)

경로 안내 이벤트를 알리는 Dart 패키지(`navigation`, 1.0.0)다. `Directions`로 경로를 정의하고 `NavigationEventHandlerDelegate`를 구현해 초기화하면 이벤트가 전달된다.

- 이벤트 8종: 위치 갱신(`onLocationUpdated`: 입력과 보정 좌표), 출발, 도착, **경로 이탈**(`onDeviation`: 새 `Directions`를 반환하면 재탐색), 노드 접근, 노드 도착, 중간 안내(구간 내 남은 거리), 경로 초기화
- 제어: `controller.start(locationStream)`, `pause(resumeFuture)`, `stop()`
- 거리 계산은 사용자 쪽이 제공한다(`distanceBetween`): 패키지가 좌표계를 모르기 때문이다.

이 패키지가 현행 보행 안내의 엔진이고, 신규 SDK는 이를 KMP로 포팅한다(WBS 2.2.2 "navigation → commonMain, 기하 13함수"). ([[seoul-donghaengmap-wbs]], [[kmp-cmp-adoption]])

## LBS테크 자체 WBS (2026-07~12)

| 대분류 | 내용 |
|---|---|
| 1. 사업 운영 | 착수·중간·최종 보고, 산출물 점검, **SDK 자체 실증 테스트** |
| 2.1 시스템 개발 | 공간 DB 정합성 개선, 내비 알고리즘 개선(엔진 패치 로그) |
| 2.2 내비 SDK (KMP) | PoC(KMP 셋업 + JTS/Vincenty 골든 검증) → 엔진 포팅 → Pathfinder Ktor 클라이언트 + GeoJSON 매퍼 → 플랫폼 expect/actual(위치·음성·햅틱·지도) → 네이버 지도 통합 → 음성·햅틱 오케스트레이터 → Android UI(Compose) → iOS UI(SwiftUI + KMP 상태 구독/SKIE) → 시뮬레이션 모드 → 실측 튜닝·통합 테스트·빌드(AAR/XCFramework) |
| 2.3 DB·서버 | 공간 DB(ERD), 접점 연계 데이터 모델(ICD), 경로 탐색 엔진/로직, 통합 API 명세서, 보행망 갱신 파이프라인, 서버 배포 이중화 |

## 파트너 역할 분담 (기능정의서 전제)

경로 통합과 순위 결정은 **LBS테크**, 대중교통 경로 계산은 **아로정보기술**(지금은 ODsay 사용), 실내는 **파파**, 서버 인프라는 **아이나비시스템즈**. 연계 위험은 [[seoul-donghaengmap-design-audit]]에 정리되어 있다.

## Open Questions

- `navi-swagger.html`은 OpenAPI와 같은 내용으로 보여 이번에 읽지 않았다.
- `추가자료/2026 서울동행맵 WBS.xlsx`와 협업자료 WBS의 차이는 확인하지 않았다.

## Sources

- [[_raw/_archived/내비게이션_서버 DB_규격서.pdf]] — 서버·DB 규격서
- [[_raw/_archived/내비게이션_참고문서.pdf]] — Flutter 내비게이션 패키지
- [[_raw/_archived/openapi.json]] — AR-Navi OpenAPI
- [[_raw/_archived/2026 서울동행맵 WBS_(주)엘비에스테크.xlsx]] — LBS테크 WBS
