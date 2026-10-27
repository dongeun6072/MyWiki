---
title: >-
    iNavi SDK Android 코드 표 (에러/상태 코드)
category: references
project: orbis-sdk
tags: [navisdk, android, error-codes, reference, visibility/internal]
aliases: [iNavi SDK Android 코드표, 에러 코드, errCode 목록]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[navisdk-api-coverage-and-domestic-sdk-guide]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/305430571
summary: >-
    iNavi SDK(Android) 가이드의 코드 표 전체. 성공(0)부터 길찾기/인증/지도 다운로드/엔진 초기화/검색 오류 코드(최대 6000)를 범주별로 정리.
provenance:
  extracted: 0.92
  inferred: 0.05
  ambiguous: 0.03
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T13:00:00+09:00
updated: 2026-10-26T13:00:00+09:00
---

# iNavi SDK Android 코드 표 (에러/상태 코드)

iNavi SDK Android 가이드 맨 끝 "코드 표"의 모든 행이다. Listener의 `onFail(errCode, errMsg)`로 전달되는 코드와 `runGuidance`/`startSimulation` 같은 Int 반환값(0 성공)의 해석에 쓴다. 원문은 번호순 단일 표이며, 여기서는 읽기 쉽도록 범주로 나누되 모든 행을 유지했다(범주 구분은 편집자 판단 ^[inferred]). 허브: [[inavi-sdk-android-guide-hub]], 함수는 [[inavi-sdk-android-controller-route-and-driving]], 타이완 RouteServer 쪽 코드는 [[taiwan-routeserver-api]]와 별개이다.

## 공통/성공
| 코드 | 설명 |
|---|---|
| 0 | 성공 |

## 길찾기 엔진 (1~121)
| 코드 | 설명 |
|---|---|
| 1 | 길찾기 실패 |
| 3 | 목적지가 물리적 섬 도로 |
| 4 | 유효하지 않은 출발지 |
| 5 | 유효하지 않은 목적지 |
| 9 | 요청 파라미터 오류 |
| 11 | 메모리 할당 실패 |
| 15 | 파일 오픈 실패 |
| 17 | 메모리 할당 실패 |
| 19 | 파일 읽기 실패 |
| 20 | 파일 쓰기 실패 |
| 21 | 유효하지 않은 지도 데이터 |
| 22 | 요청 파라미터 오류 |
| 23 | Projection 실패 |
| 25 | DB 오류 |
| 32 | 길찾기 가능 거리 초과 |
| 35 | 두 지점이 너무 가까운 경우 |
| 36 | 목적지 오류 |
| 39 | 논리적 길찾기 오류 |
| 43 | 차량이 진입할 수 없는 도로 |
| 48 | 소켓 연결 실패 |
| 49 | 결과 생성 실패 |
| 96 | 잘못된 경로 ID |
| 97 | Checksum 오류 |
| 120 | 최적경로(재탐색은 성공했으나 더 좋은 경로가 없는 경우) |
| 121 | 목적지 부근으로 재탐색이 필요 없는 경우 |

## 서버/인증 응답 (300~1005)
| 코드 | 설명 |
|---|---|
| 300 | 미 지원 서비스 |
| 800 | 서버 파일 저장 에러 |
| 900 | 인증 실패 |
| 901 | 인증 정보가 변경되어 앱 재시작 필요 |
| 902 | 입력 파라미터 오류 |
| 903 | 조회결과 없음 |
| 904 | 존재하지 않는 파일 요청 |
| 905 | DB 연동 에러 |
| 907 | 경로 ID 오류 |
| 931 | 유효하지 않은 좌표 |
| 933 | 유효하지 않은 검색어 |
| 1000 | 인증 데이터 오류 |
| 1001 | 인증 데이터 오류 |
| 1002 | 잘못된 요청 형식으로 인증 |
| 1003 | 인증 데이터가 존재하지 않음 |
| 1004 | 유효하지 않은 Unique Key(필수값인 Unique Key 값이 Null 이거나 Empty 인 경우) |
| 1005 | 유효하지 않은 Unique Key(필수값인 Unique Key 값이 20자 초과 인 경우) |

## SDK 내부 처리 오류 (2000~2013)
| 코드 | 설명 |
|---|---|
| 2000 | 처리되지 않은 예외 발생 |
| 2001 | 유효하지 않은 출발지 |
| 2003 | 유효하지 않은 목적지 |
| 2006 | 서버 응답 오류 |
| 2007 | 버퍼 NULL |
| 2008 | 데이터 파싱 실패 |
| 2010 | 패킷 생성 실패 |
| 2011 | 패킷 생성 실패 |
| 2012 | 다운로드 실패 |
| 2013 | 유효하지 않은 파라미터 |

## 인증/초기 데이터/엔진 초기화 (3000~3054)
| 코드 | 설명 |
|---|---|
| 3000 | 알 수 없는 인증 오류 |
| 3001 | 초기 지도 다운로드 실패 |
| 3002 | 초기 지도 다운로드 실패 |
| 3003 | 지도 URL 오류 |
| 3004 | 안전운행 URL 오류 |
| 3005 | 안전운행 URL 오류 |
| 3006 | 안전운행 다운로드 실패 |
| 3007 | 인증 실패 |
| 3008 | 인증 업데이트 실패 |
| 3050 | 지도 엔진 초기화 실패 |
| 3051 | SMR 엔진 초기화 실패 |
| 3052 | 맵매칭 엔진 초기화 실패(위치권한 미 획득시에도 발생할 수 있음) |
| 3053 | 안내 엔진 초기화 실패 |
| 3054 | 기타 엔진 초기화 실패 |

## 검색 (4000~4001, 6000)
| 코드 | 설명 |
|---|---|
| 4000 | 검색결과 없음 |
| 4001 | 유효하지 않은 검색어 |
| 6000 | 검색어 오류 |

## 길찾기 입력 검증 (5000~5005)
| 코드 | 설명 |
|---|---|
| 5000 | 출발지 오류 |
| 5001 | 목적지 오류 |
| 5002 | 출발지가 유효 범위를 벗어난 경우 (0.0.12에서 추가) |
| 5003 | 목적지가 유효 범위를 벗어난 경우 (0.0.12에서 추가) |
| 5004 | 출발지와 목적지가 가까워 길찾기가 불가능 (0.0.12에서 추가) |
| 5005 | 안내중인 경로가 유효하지 않은 경우 |

## 참고
- 중복 설명 코드: 11/17(메모리 할당 실패), 9/22(요청 파라미터 오류), 1000/1001(인증 데이터 오류), 2010/2011(패킷 생성 실패), 3001/3002(초기 지도 다운로드 실패), 3004/3005(안전운행 URL 오류)는 설명이 같은 서로 다른 코드이다. 세부 구분은 원문에 없다.
- 0.6.1부터 경유지가 포함된 경우 출발지-목적지 간 거리 체크를 하지 않는다([[inavi-sdk-android-revision-history]]).

## Related
- [[inavi-sdk-android-guide-hub]] — 이 가이드 묶음 목차
- [[inavi-sdk-android-controller-init-map-search]] — `initalizeNavi` 실패 코드 사용처
- [[navisdk-api-coverage-and-domestic-sdk-guide]] — 국내 SDK 가이드 개요
- [[orbis-sdk]] — SDK 프로젝트 허브

## Sources
- Confluence "iNavi SDK Android 개발 가이드" (pageId 305430571) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
