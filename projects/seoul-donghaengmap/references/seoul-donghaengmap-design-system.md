---
title: >-
    서울동행맵 디자인 컨셉과 디자인 가이드
category: references
tags: [seoul-donghaengmap, design-system, accessibility, visibility/internal]
aliases: [동행맵 디자인 가이드, 접근성 우선 디자인 시스템, 디자인 컨셉 A/B]
relationships:
  - target: "[[seoul-donghaengmap-screen-design]]"
    type: related_to
  - target: "[[seoul-donghaengmap-design-concept-evolution]]"
    type: related_to
  - target: "[[digital-government-uiux-guideline]]"
    type: related_to
  - target: "[[korean-mobile-app-accessibility-guidelines]]"
    type: related_to
sources:
  - ~/Develop/Wiki/_raw/articles/project-seoul/디자인컨셉_아이나비시스템즈/Seoul_Donghaeng_DesignGuide_261013.pptx
  - ~/Develop/Wiki/_raw/articles/project-seoul/디자인컨셉_아이나비시스템즈/서울동행맵_디자인_시각장애인용_v0.9_260918.pptx
  - ~/Develop/Wiki/_raw/articles/project-seoul/디자인컨셉_아이나비시스템즈/서울동행맵_디자인컨셉_v1.0_260820.pptx
summary: >-
    접근성 우선 디자인 시스템(2026-10): 네 가지 원칙, 블루 계열 컬러 토큰과 대비율, 상태 표현, 타이포그래피 6단계, 간격·레이아웃 규칙. 컨셉 A(블루)/B(그린) 비교와 전맹용 화면 방향도 포함한다.
provenance:
  extracted: 0.88
  inferred: 0.12
  ambiguous: 0.00
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T09:31:30+09:00
updated: 2026-10-26T15:30:00+09:00
snapshots:
  - "[[_raw/_archived/Seoul_Donghaeng_DesignGuide_261013.pptx|Seoul_Donghaeng_DesignGuide_261013.pptx]]"
  - "[[_raw/_archived/서울동행맵_디자인_시각장애인용_v0.9_260918.pptx|서울동행맵_디자인_시각장애인용_v0.9_260918.pptx]]"
  - "[[_raw/_archived/서울동행맵_디자인컨셉_v1.0_260820.pptx|서울동행맵_디자인컨셉_v1.0_260820.pptx]]"
  - "[[_raw/_archived/Seoul_Donghaeng_Concept_260820.pptx|Seoul_Donghaeng_Concept_260820.pptx]]"
  - "[[_raw/_archived/Seoul_Donghaeng_Concept_260820_수정.pptx|Seoul_Donghaeng_Concept_260820_수정.pptx]]"
  - "[[_raw/_archived/서울동행맵_디자인컨셉_초안_260716.pptx|서울동행맵_디자인컨셉_초안_260716.pptx]]"
---

# 서울동행맵 디자인 컨셉과 디자인 가이드

아이나비시스템즈(프로덕트전략셀)의 디자인 산출물 세 편을 합쳤다. 컨셉 시안(2026-08-20) → 시각장애인용 화면 구성(09-18) → **디자인 가이드(2026-10-13)** 순으로 진행됐다. 화면 규칙은 [[seoul-donghaengmap-screen-design]], 요구의 근거는 [[korean-public-mobile-app-compliance]], 프로젝트는 [[seoul-donghaengmap]]이다.

## 컨셉 시안: 블루(A) 대 그린(B)

초안(07-16, 그린 단일) → 08-20 A/B → 수정본(A의 Primary를 `#2364D2` 5.49:1에서 `#1A4E9B` 8:1로 상향)의 변천은 [[seoul-donghaengmap-design-concept-evolution]]에 있다.

| | 시안 A (블루) | 시안 B (그린) |
|---|---|---|
| 방향 | 적·녹 색맹 인지 개선, 저시력에서 조건 간 편차가 적고 대중교통·공공 서비스에서 신뢰를 주는 색 | 현행 서울동행맵의 컬러 범위로 브랜드 통일감 유지 |
| 스타일 | 라운드 버튼 + Line 형태 | 사각 버튼 + Filled 형태 |
| 주요 색 | Primary `#1A4E9B`(8:1), Secondary `#00892E` | Primary `#00892E`(4.55:1), Secondary `#266EE7` |

공통: 본문·보조 텍스트 10.3:1 이상(AAA), 색만으로 구분하지 않고 **아이콘·라벨·형태를 병기**, WCAG 2.1/KWCAG 2.1 AA(4.5:1) 반영. 저시력자와 적·녹 색맹 시뮬레이션으로 확인했다. **최종 가이드는 시안 A(블루 `#1A4E9B`)를 채택**한 것으로 보인다(가이드의 Primary가 시안 A와 같다). ^[inferred]

## 디자인 가이드의 네 가지 원칙

"한 화면의 미달이 앱 전체의 인증 실패로 이어지므로 모든 화면에 같은 원칙을 적용한다."

| 원칙 | 기준 |
|---|---|
| 명도 대비 | 모든 텍스트와 정보 전달 경계 4.5:1 이상 |
| 터치 타겟 | 최소 44×44pt, 인접 타겟 간격 8 이상 |
| 텍스트 하한 | 16pt 미만 금지, 전 역할 행간 150% |
| 상태 표현 | 색 단독 금지, 텍스트와 아이콘 병기 |

**같은 메뉴, 두 개의 화면**: 토큰·정보 구조·용어·음성 안내 문구는 공유하고 진입 동선만 나눈다. ① 교통약자 통합 화면(지체·청각·고령·저시력) ② 전맹 화면(스크린리더 사용자, 세로 배열과 논리적 포커스 순서)

## 컬러 토큰 (Hue 215° 블루 한 축)

| 토큰 | 값 | 대비 |
|---|---|---|
| primary | `#1A4E9B` | 8.06:1 |
| primary-pressed | `#15407F` | 10.14:1 |
| accent-large | `#0F3468` | 12.27:1 (대표 수치) |
| primary-container | `#E3EDFB` | tonal 면 |
| on-surface | `#171C1C` | 17.23:1 |
| on-surface-secondary | `#374151` | 10.30:1 |
| border-strong | `#5A6472` | 6.07:1 (정보 경계) |
| border-subtle | `#D5DBE4` | 1.39:1 (장식 전용) |
| error / warning / success | `#990000` / `#B84500` / `#006E25` | 8.92 / 4.71 / 6.45 |
| 출발 / 경유 / 도착 | `#00707A` / `#374151` / `#3B7A0A` | 5.84 / 10.30 / 5.28 |

Neutral 9색은 N0~N100이며 **텍스트에는 N70 이상만** 쓴다(N40은 장식 전용). On-color 짝(표면 색마다 그 위의 텍스트 색)을 정의한다.

## 표면, 상태, 버튼

- 표면 4단계: surface-dim(바탕 `#F5F7FA`), surface-container(비활성 `#E9EDF3`), surface(카드·시트 `#FFFFFF`), field(입력 필드, **테두리 2px 필수**). 그림자는 보조 채널이다(elevation 1~3).
- 상태(Normal, Pressed, Focused, Selected, Disabled)마다 면·테두리·텍스트를 **함께** 바꾸고 모든 상태에서 4.5:1을 유지한다. Focused는 흰색 오프셋 2px + 3px 링.
- 버튼 4종: primary(주 행동, 화면당 1종), tonal(보조), outline(취소·닫기·종료, 2px 테두리), destructive(되돌릴 수 없는 행동, 다이얼로그 한정). 모두 둥근 라운드.

## 타이포그래피와 레이아웃

| 토큰 | 크기/행간 | 굵기 | 용도 |
|---|---|---|---|
| title-sm | 22/33 | Bold | 화면·섹션 제목 |
| title-xs | 20/30 | Bold | AppBar, 시트, 다이얼로그 제목 |
| body | 18/27 | Medium | 본문 기본 |
| body-sm, label | 16/24 | Medium | 보조 텍스트, 배지, 버튼 |
| numeric | 22/33 | Bold | 화면당 대표 수치 1개 |

- 굵기는 Medium(500)을 본문 하한으로, Bold(700)는 초점 요소에만 쓴다.
- **시스템 폰트 200% 확대 대응 4원칙**: 높이 가변(Hug), 가로 나열은 컨테이너 폭 기준으로 세로 스택 전환, 아이콘은 단계 확대(24→32px, 컨테이너 44→56px), **판단에 필요한 텍스트에 말줄임 금지**
- 간격은 4px 그리드 5단계(4, 8, 12, 16, 20). 좌우 여백 16, 바텀시트는 화면 높이 60% 이하(지도 40%).
- 아이콘은 단색 24px(확대 시 32px), 텍스트와 함께: 휠체어, 엘리베이터, 경사로, 계단, 화장실, 점자블록, 자동문, 센서문 등

## 시각장애인용 화면 구성 (v0.9)

네 가지 흐름: 회원가입에서 유형 선택(전맹) → 홈(위에서 아래 한 방향) → 음성으로 시작하는 길찾기(**화면을 길게 눌러 말하기**) → 대화형 길안내와 챗봇 접근성.

## 접근성 인증과의 연결

디자인 원칙(4.5:1, 44pt, 색 단독 금지)은 모바일 접근성 인증마크 획득 요구를 화면 단위로 충족하기 위한 것이다. ([[seoul-donghaengmap-negotiation-kickoff]]) ^[inferred] 앱 구현은 CMP 단일 코드베이스에서 이루어지며 이 토큰이 코드 토큰으로 이어진다. ([[kmp-cmp-adoption]])

지침 기준과 비교하면 이 디자인 원칙이 더 엄격하다. KS X 3253은 UI 컴포넌트·텍스트 명도 대비 3:1, 컨트롤 9mm 이상(권고)을 요구하고, 웹(KWCAG 2.2)은 텍스트 4.5:1이다. ([[korean-mobile-app-accessibility-guidelines]], [[kwcag-2-2]]) 공공 UI 컴포넌트와 패턴(입력폼, 로그인, 탭바 등)과 KRDS 토큰은 [[digital-government-uiux-guideline]]에서 대조할 수 있다. ^[inferred]

## Open Questions

- 컨셉 파일 3종과 07-16 초안은 텍스트만 읽었다(시안 이미지는 보지 않음). 내용은 [[seoul-donghaengmap-design-concept-evolution]].

## Sources

- [[_raw/_archived/Seoul_Donghaeng_DesignGuide_261013.pptx]] — 디자인 가이드
- [[_raw/_archived/서울동행맵_디자인_시각장애인용_v0.9_260918.pptx]] — 시각장애인용 화면
- [[_raw/_archived/서울동행맵_디자인컨셉_v1.0_260820.pptx]] — 컨셉 A/B
- [[_raw/_archived/서울동행맵_디자인컨셉_초안_260716.pptx]] — 07-16 Dual-Path 초안
- [[_raw/_archived/Seoul_Donghaeng_Concept_260820.pptx]] — A/B 비교안 원본
- [[_raw/_archived/Seoul_Donghaeng_Concept_260820_수정.pptx]] — A 블루 대비 상향 수정본
