---
title: >-
    Onesky 다국어 관리 프로세스
category: references
project: orbis-sdk
tags: [onesky, i18n, translation, process, visibility/internal]
aliases: [Onesky 다국어 관리 프로세스]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/739115034
summary: >-
    구글 스프레드시트 스크립트 작성부터 Onesky 업로드·번역 요청·검수·Android/iOS 리소스 추출까지의 신규/유지보수 번역 절차와 Key 작성 규칙
provenance:
  extracted: 0.90
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T13:00:00+09:00
updated: 2026-10-26T13:00:00+09:00
---

# Onesky 다국어 관리 프로세스

다국어 문구를 구글 스프레드시트로 관리하고 Onesky로 번역해 Android/iOS 리소스를 만들어 개발팀에 넘기는 절차(2025-07-22 수정)다. 표기 규칙은 [[orbis-i18n-units-notation-and-translation-resources]], 음성 문구는 [[orbis-voice-phrase-combinations]], 목차는 [[orbis-design-and-review-hub]]. 스프레드시트·참고 링크는 모두 `<링크 생략>`이며(권한 필요), 결제 수단 정보는 원본에 있으나 미수록이다.

## 1. 신규 번역 프로세스

### 1) 구글 스프레드시트에 포맷에 맞는 스크립트 작성 (권한 필요 링크)
- **Description**: 문맥에 맞는 설명, 주석
- **String Identifier(Keys)**: 유지보수를 위한 값 생성
- Character Limit: 문자 제한(선택)
- **기본 언어**: 영문(한국어는 참고용으로 작성) + α(영문 기준으로 추가 언어를 번역)
- 번역이 필요한 열을 정한다.

작성 규칙
1. 중복된 문구를 제거한다.
2. 데이터 연결이 필요한 부분은 출력지정자로 표출한다.
   - `%d`: 숫자(정수). `%1$d`, `%2$d`, `%3$d` …: 같은 종류의 변수가 여러 개인 경우
   - `%f`: 숫자(소수점, 실수)
   - `%s`: string, 텍스트, 목적지명 등
3. 활용 가능한 문장이면 최소 단어로 분리한다.
   - **원인**과 **제안** 문구를 분리해 중복을 없애고 활용도를 높인다.
   - 예: 2가지 문구로 분리 — "선택한 지도를 삭제할 수 없습니다." / "나중에 다시 시도하세요."
4. String Identifier(Keys) 작성 규칙
   - `[모듈/화면]_[역할/위치]_[의미]` 순서
   - 소문자로 작성
   - 최대한 짧고 간결하게 작성

Key 구성 요소(원문 표. 두 열은 서로 대응하지 않는 목록이다)

| 모듈/화면 | 역할/위치 |
|---|---|
| main | label |
| search | btn |
| map / route / drive | msg |
| place / category | error |
| setting | toggle |
| audio | unit |
| popup | time |
| common | |

5. English(Script) 작성 유의사항: 대소문자 확인, 중복 문자 확인

### 2) Excel 파일 업로드 준비
1. 작성된 구글 스프레드시트를 Excel 파일로 다운로드한다.
2. 영문 기준으로 한글 번역도 1차로 진행한다(교차 확인용). 한글 번역을 위해 기존에 작성한 열(한국어)은 삭제한다.

### 3) Onesky 프로젝트 업로드
1. Excel(xlsx) 파일 업로드
2. 업로드된 파일 구조 정의(각 열의 의미 매칭)
3. 업로드 완료

### 4) 번역 요청 및 비용 결제
1. 사내에서 공유받은 법인 결제 수단으로 결제한다(결제 수단 정보는 미수록). 비밀번호 없이 웹페이지 안에서 결제 정보 입력만으로 결제가 진행된다. 결제가 안 된 경우의 원인은 1회 결제 한도가 낮았던 것이다.
2. 파일 및 옵션 설정: 전문가 번역 선택, 리뷰어는 미선택. 추가 옵션으로 번역 톤과 쓰임을 간단히 설명한다.
3. 결제

### 5) 번역 완료 후 번역본 다운로드
1. 번역 완료 후 내보내기(Export) — Excel(xlsx) 파일 다운로드
2. Translation Overview > Download Translation(우측 상단) > Export

### 6) 번역본 검수
1. 구글 스프레드시트에 번역 언어를 업데이트한다.
2. 검수를 진행한다.
   - 작성한 한국어와 영어 기반으로 번역된 한국어를 교차 확인한다.
   - ChatGPT를 활용해 전체를 검수한다.
   - 한국어 교차 확인 시 어색한 부분은 추가 검수한다.

### 7) 리소스 추출 및 개발팀 공유
1. 스프레드시트 상단 우측 메뉴의 "CX Translator" > "Android 리소스 생성"을 선택한다(참고 링크 생략). iOS의 InfoPlist는 생성하지 않도록 설계되어 있다.
2. 구글 드라이브의 Android 폴더 안에 언어별 파일이 생성된다.
3. 내려받은 뒤 압축 파일을 개발팀에 공유한다. 내려받은 후에는 구글 드라이브 폴더를 바로 삭제한다(리소스 추출 시 파일 혼동 방지).

### 8) 프로젝트 확장 시
- 구글 스프레드시트 하단에 시트를 추가해 프로젝트를 만든다.

## 2. 기존 번역본 유지보수
1. 기존 구글 스프레드시트에서 문구를 추가·수정한다.
2. Onesky에 업로드한다.
3. 새 문구와 업데이트 문구는 자동 감지되며 번역 여부도 선택할 수 있다(참고 링크 생략).
4. 번역을 요청한다.
5. 번역 후 관리는 동일하다.

## 3. xml, strings 추출 방법
1. 구글 스프레드시트 상단 **CX Translator**를 선택한다.
2. **Android, iOS 리소스 생성**을 선택한다.
3. 구글 드라이브에 파일이 생성되었는지 확인하고 개발팀에 공유한다.
   - 오류 시 파일 전체를 삭제하고 다시 추출한다.
   - 언어 파일 개수를 최종 확인한다.
4. 개발팀에 공유한 뒤 구글 드라이브의 파일은 삭제한다(버전 관리 목적).

(1절 7항에서는 iOS InfoPlist를 생성하지 않는다고 하고 3절에서는 Android, iOS 리소스 생성을 선택한다고 적혀 있어, iOS는 strings만 생성하는 것으로 읽힌다.) ^[inferred]

## Related
- [[orbis-i18n-units-notation-and-translation-resources]] — 표기 사양과 번역 리소스 이력
- [[orbis-voice-phrase-combinations]] — 발성 조각 키 규칙
- [[new-navisdk-plan-detail]] — 다국어 지원 1안/2안(플랫폼 리소스 vs moko-resources)
- [[orbis-sdk]]

## Sources
- Confluence "Onesky 다국어 관리 프로세스" (pageId 739115034) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
