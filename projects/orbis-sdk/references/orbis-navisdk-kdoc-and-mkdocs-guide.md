---
title: >-
    Orbis NaviSDK API 문서(KDoc)와 MkDocs 작성 가이드
category: references
project: orbis-sdk
tags: [navisdk, kdoc, mkdocs, api-docs, kmp, visibility/internal]
aliases: [Orbis NaviSDK API Document 작성 문서, KDoc, MkDocs]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/984055941
summary: >-
    Orbis NaviSDK의 API 문서를 javadoc에서 KDoc으로 전환한 방식, 문서 생성/발행 절차, 태그 사용법, 가이드 문서용 MkDocs 설치와 사용, 마크다운 문법 정리.
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

# Orbis NaviSDK API 문서(KDoc)와 MkDocs 작성 가이드

2026-01-12 수정된 "Orbis NaviSDK API Document 작성 문서"를 옮겼다. Kotlin Multiplatform에 맞게 javadoc을 KDoc으로 바꾸고, 개발자 가이드는 MkDocs로 배포하기로 한 결정과 절차를 담는다. SDK 구조는 [[orbis-navisdk-architecture-and-flutter-plan]], 프로젝트는 [[orbis-sdk]], 목차는 [[air-internal-docs-and-integration-hub]]를 본다.

## API 문서 정리

- 기존 javadoc을 대체해 **KotlinMultiplatform에 적합한 KDoc** 형태로 문서화한다.
- 현재는 Android/Common Main 부분만 문서화하고 있으며 추후 iOS까지 함께 생성할 수 있다.
- 원본에 생성된 KDoc 예시 이미지가 있다(이미지 항목, 내용 없음).

### 생성 위치와 발행
- `navisdk > api-references` 폴더 안에 navisdk(기본 페이지)와 각 모듈별 페이지가 생성된다.
- 발행된 API 문서 페이지 링크가 있다(링크 생략).
- 개발자 가이드 문서(gitbook) 경로는 취소선 처리되어 폐기되었다. 개발자 가이드는 **MkDocs로 Markdown 파일을 배포**하기로 결정했다.
- 가이드 문서(.md)는 프로젝트 소스의 `/guide-documents/docs`에 있다.

### Git 관련
- 기존 `navisdk_core` git 안에 **submodule**로 등록되어 있다. 문서 배포용 저장소에 write 권한이 있어야 submodule을 수정할 수 있다.
- `navisdk-core`에서 pull한 뒤 `navisdk/api-references` 폴더만 생성된 상태라면 다음으로 동기화한다.

```
git submodule update --init --recursive
```

### 문서화 실행 명령어
여러 번 발행할 때는 사전에 클린 빌드가 필요하다.

```
sh aosPublish.sh --publish-documents
```

### KDoc 문법과 공용 설정
- `navisdk/api-references/includes.md`를 참조한다. 이 파일에서 특정 모듈, 패키지별 설명을 추가할 수 있다. 모듈/패키지 설명이 적용된 화면 예시 이미지가 원본에 있다.

주요 태그:

| 태그 | 설명 |
|---|---|
| `@param <이름>` | 매개변수 이름, 이름 뒤에 설명 작성 |
| `@suppress` | 해당 요소를 문서에서 제외 |
| `@return` | 반환값 |
| `@see <대상>` | 관련 클래스/함수 링크 생성(see also) |
| `@constructor` | 주 생성자 |
| `@throws <예외 클래스>` | 예외 클래스, 클래스명 뒤에 설명 작성 |
| `@since` | 해당 기능이 추가된 API 버전 명시 |

도구: **kdoc-generator**(Android Studio 플러그인)를 설치하면 `/**` 입력 후 엔터 시 형식에 맞게 자동 생성한다.

## MkDocs로 Markdown/HTML 문서 생성

### 1. Python과 pip 설치
1. `brew install python`.
2. 터미널을 완전히 종료했다 다시 열고 `python3 --version`, `pip3 --version`으로 확인. macOS 기본 내장 구버전을 피하려고 반드시 `python3`, `pip3`를 쓴다.

### 2. MkDocs 설치
1. `pip3 install mkdocs`
2. `mkdocs --version`으로 확인. 2025년 9월 기준 **1.6.1** 사용.

### 프로젝트 생성과 실행
1. 프로젝트 폴더를 만들고 이동한다(예: `mkdir my-docs`, `cd my-docs`).
2. `mkdocs new .` 로 시작한다.
3. 생성 구조:

```
my-docs/
├── docs/
│   └── index.md  # 기본 홈페이지 마크다운 파일
└── mkdocs.yml    # MkDocs 전체 설정 파일
```

- `docs/`: 모든 마크다운 문서 위치
- `mkdocs.yml`: 사이트 이름, 내비게이션 메뉴, 테마 등 전체 설정

### 로컬 서버(`mkdocs serve`)
- 프로젝트 폴더에서 `mkdocs serve`를 실행하면 로컬 개발 서버가 뜨고 문서 수정 시 자동 새로고침되는 실시간 미리보기가 된다.
- 브라우저에서 로컬 주소로 접속한다. .md를 수정·저장하면 바로 반영된다.

### 최종 HTML 빌드(`mkdocs build`)
- 작성이 끝나면 `mkdocs build`로 HTML을 만든다. 프로젝트 폴더에 `site` 폴더가 생성된다.

```
my-docs/
├── docs/
├── site/  <-- 생성된 HTML 결과물 폴더
│   ├── index.html
│   └── ... (CSS, JS, 폰트 파일 등)
└── mkdocs.yml
```

- `site/index.html`을 직접 열면 pretty url 기능 때문에 페이지 간 이동이 정상 표출되지 않을 수 있으므로 결과 확인은 `mkdocs serve`로 한다.

## 주요 Markdown 문법(원본 정리)

| 요소 | 문법 |
|---|---|
| 제목 | `# 제목 1`, `## 제목 2`, `### 제목 3` |
| 강조 | `*기울임*` 또는 `_기울임_`, `**굵게**` 또는 `__굵게__`, `~~취소선~~` |
| 순서 없는 목록 | `*`, `+`, `-` (들여쓰기로 중첩) |
| 순서 있는 목록 | `1.`, `2.`, `3.` |
| 링크 | `[링크 텍스트](URL)` |
| 이미지 | `![대체 텍스트](이미지 경로 또는 URL)` |
| 인라인 코드 | 백틱 하나로 감쌈 |
| 코드 블록 | 백틱 세 개, 언어 이름을 쓰면 문법 강조 |
| 인용문 | 줄 시작에 `>` |
| 표 | `\|`와 `-`로 작성, 하이픈 줄로 머리글 구분. 정렬은 `:------`(왼쪽), `:----:`(가운데), `------:`(오른쪽) |

## Related
- [[orbis-navisdk-architecture-and-flutter-plan]] — SDK 아키텍처와 KMP 계획
- [[orbis-sdk]] — 프로젝트 개요
- [[navisdk-api-coverage-and-domestic-sdk-guide]] — API 범위
- [[air-internal-docs-and-integration-hub]] — 이 묶음 목차

## Sources
- Confluence "Orbis NaviSDK API Document 작성 문서" (pageId 984055941) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
