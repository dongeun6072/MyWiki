---
title: >-
    TomTom Connected Services 플랫폼과 Hazard Warnings 규격
category: references
project: tsd-a01
tags: [tsd-a01, tomtom, kafka, protobuf, hazards, visibility/internal]
aliases: [ConnectedServicesPlatformGuide, Hazard Warnings B2B, hazards-udf-schema]
relationships:
  - target: "[[tsd-a01]]"
    type: related_to
  - target: "[[tomtom-traffic-flow-openlr-inquiries-2024]]"
    type: related_to
sources:
  - "[[_raw/_archived/ConnectedServicesPlatformGuide (2).pdf]]"
  - "[[_raw/_archived/TomTom-HazardsService-TechnicalSpecification-B2B-1.3.pdf]]"
  - "[[_raw/_archived/hazards-udf-schema-v1.0.1 (2).zip]]"
summary: >-
    TomTom B2B 전달 플랫폼(Kafka + Protobuf UDF)의 접속 개념과 위험 경고(Hazard Warnings) 서비스 v1.3의 유형, 토픽 규칙, 데이터 구조.
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0.0
base_confidence: 0.55
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T14:00:00+09:00
updated: 2026-10-26T14:00:00+09:00
snapshots:
  - "[[_raw/_archived/TomTom-HazardsService-TechnicalSpecification-B2B-1.3.pdf|TomTom-HazardsService-TechnicalSpecification-B2B-1.3.pdf]]"
  - "[[_raw/_archived/ConnectedServicesPlatformGuide (2).pdf|ConnectedServicesPlatformGuide (2).pdf]]"
  - "[[_raw/_archived/hazards-udf-schema-v1.0.1 (2).zip|hazards-udf-schema-v1.0.1 (2).zip]]"
---

# TomTom Connected Services 플랫폼과 Hazard Warnings 규격

## Connected Services 플랫폼 가이드

- **Apache Kafka 기반** 이벤트 스트리밍이다. 데이터는 Kafka 프로토콜로 제공되고, 메시지(event)는 TomTom 자체 **Unified Data Format(UDF, Protobuf)** 이다.
- 개념: topic(발행/구독 단위), producer, consumer, **consumer group**(같은 그룹 인스턴스는 이벤트를 한 번만 받음, 허용 group id는 TomTom이 지정).
- 온보딩: TomTom 개발자 포털 계정 + "Connected Services API" 제품의 API 키(팀 단위 메일 권장) → 담당 어카운트 매니저에 알려 키 설정 → 포털의 키 관리에서 확인.
- 인증: **OAuth2**. API 키로 토큰 엔드포인트에서 토큰을 받아 Kafka 클러스터에 연결한다(clientId/secret은 형식상 필수이며 아무 문자열). 보안 프로토콜은 SASL_SSL, 메커니즘은 OAUTHBEARER. 키는 비밀로 보관해야 한다. 접속 정보와 키 값은 이 위키에 두지 않는다.
- 연결 시험은 `kafka-console-consumer`, 토픽 목록은 `kafka-topics`로 확인한다.

## Hazard Warnings 서비스 (B2B 규격 v1.3, 2024-06-19)

저지연 안전 경고 서비스다. 프로브 데이터에 정부 피드, 커뮤니티 입력, 차량 센서 데이터를 더해 화면 표출이나 자율주행의 속도 조정에 쓴다.

| 범주 | 유형 |
|---|---|
| Traffic | Accident, Broken-down vehicle, Emergency Vehicle Approaching(v1.1), Jam tail, Wrong Way Driver(v1.2) |
| Weather | Slippery road, Reduced visibility, Strong winds |
| Road | Bad road conditions, Objects on road, Roadworks |
| Generic | 위에 분류되지 않는 기타 |

- 버전 이력: 1.0(2023-04) 최초, 1.1 EVA 추가, 1.2 Wrong Way Driver 추가, 1.3 **OSM Way ID 참조 추가**와 새 토픽 명명 규칙 적용.
- 토픽 형식: `<data_channel>.tomtom.hazards.<content_api_version>.<product_configuration>.<region>.<hazard_type>`.
- 데이터 구조: `HazardsReport` > `MetaData`, `HazardMessage`(Identifier, Location, Times, Hazard) > HazardCategory / HazardType / HazardSeverity / DetailInformation(유형별: 노면 불량, 정체 꼬리, 긴급차량, 도로 위 물체, 시야 저하, 공사, 강풍).
- 위치에 OSM Way ID가 붙으므로 [[tomtom-traffic-flow-openlr-inquiries-2024]]의 OSM ID 매핑 방식과 연결해 쓸 수 있다. ^[inferred]

## UDF 스키마 묶음 (v1.0.1)

zip에는 `.proto` 8개가 들어 있다: `hazardsFeed`, `hazards`, `hazards-types`, `location`, `shared`, `shared-traffic`, `countrycodes`, `uuid`. Hazard 메시지를 디코딩하는 Protobuf 정의다(2024-05 작성). 원본 압축은 풀어서 확인한 뒤 임시 폴더를 삭제했다.

## Sources

- [[_raw/_archived/ConnectedServicesPlatformGuide (2).pdf]]
- [[_raw/_archived/TomTom-HazardsService-TechnicalSpecification-B2B-1.3.pdf]]
- [[_raw/_archived/hazards-udf-schema-v1.0.1 (2).zip]]
