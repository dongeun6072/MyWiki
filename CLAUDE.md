# Wiki Vault 규칙 (obsidian-wiki)

이 저장소(`~/Develop/MyWiki`)는 Obsidian vault이자 GitHub(`dongeun6072/MyWiki`)에 올라가는 Git 저장소다.
전역 `~/.claude/CLAUDE.md`의 규칙(커밋 금지, 한국어 답변)이 그대로 적용되고, 아래 규칙이 추가된다.

## 🔒 보안 최우선 규칙

**카드번호·유효기간, 서비스 키·API 키, 서버 주소·서버 접속 정보, 계정, 개인정보처럼 보안 이슈가 될 내용은 이 저장소에 두지 않는다.** (사용자 지시, 2026-10-26)

처리 원칙은 다음 순서다. **사용자에게 묻지 않고 규칙대로 처리한 뒤 결과를 보고한다.**

1. **값만 가릴 수 있으면 가린다(마스킹).** md, txt, json, html, csv 같은 텍스트 파일과, 내부 XML을 안전하게 고칠 수 있는 docx/pptx/xlsx/xlsm이 해당한다.
2. **파일 안의 값을 가릴 수 없으면 파일을 삭제한다.** PDF, HWP, 이미지, 구형 doc/ppt/xls가 해당한다. `.gitignore`로 push만 막는 것은 해결이 아니다(이미 한 번 올라간 적이 있다).
3. 파일을 삭제하면 위키의 참조(`sources:`, `snapshots:`, `## Sources`, `.manifest.json`)를 함께 정리하고, 본문 `## Sources`에는 "원본 삭제: 보안 사유"라고 적는다.
4. **"확인했다"고 말하려면 `python3 _meta/security-scan.py`의 결과가 근거여야 한다.** 차단(BLOCK) 0건, 검사 불가 0건일 때만 통과다. 직접 grep한 결과는 근거가 되지 않는다(아래 "검사가 놓친 사례" 참고).

### 금지 대상

| 구분 | 예 |
|---|---|
| 키·토큰 | FCM 서버 키(`AAAA…:APA91…`), 기기 토큰(`APA91…`), **서비스 키**, API 키, AppKey, `x-api-key` 값, JWT, `Bearer` 토큰, 개인키(`-----BEGIN … PRIVATE KEY-----`), AWS `AKIA…` |
| 계정 | ID/PASSWORD 쌍, 공유 폴더·릴리즈 서버·단말·개발자 계정, `.env`, 인증서·키스토어(`.jks`, `.p12`, `.pem`) |
| **카드·금융** | **카드번호(전체, 부분 마스킹 `****-1234-…` 형태 포함), 카드 유효기간·만료일**, 계좌번호, 법인 결제 수단 |
| **서버 주소** | **IP 주소(사설 포함), `호스트:포트`, 개발/상용 API 서버·CDN·관리 서버의 도메인**, 내부 URL, 공유 폴더 경로, 개발자 모드·서버 전환 같은 숨은 기능 진입 방법 |
| 개인정보 | 휴대폰·유선 번호, 개인 메일 주소, 주민등록번호, 생년월일·입사일 |
| 공유 링크 | SharePoint, Google Drive/Docs/Sheets, Dooray, Notion, Figma, gofile, naver.me, bit.ly, forms.gle, Jira/Confluence 링크(출처용 Confluence 페이지 주소 제외) |

**서버 API에 대한 해석**: API 엔드포인트 **경로**(`/path`)와 요청·응답 필드 명세는 위키에 둘 수 있다. 호스트, IP, 포트가 붙은 **서버 주소**와 키, 계정은 둘 수 없다.

### 허용하는 것 (확인된 예외)

- 공개 문서의 예시와 공식 연락처(법령, 정부 가이드, 공개 표준, 입찰 공고의 담당 부서 연락처, TomTom 같은 공개 개발 가이드의 `your_api_key` 예시). 목록은 `_meta/security-scan.py`의 `ALLOW`에 **근거와 함께** 있다. 근거 없이 추가하지 않는다.
- **인사·평가 문서**(승진 추천서, 성과점검, 직무기술서, 평가 루트)는 사용자가 "그대로 두라"고 결정했다(2026-10-26). 위키의 `visibility/pii` 페이지도 그대로 둔다.
- 사람 이름은 업무 맥락이라 원본(`_raw/`)에는 남긴다. 위키 페이지에는 쓰지 않고 역할로 쓴다(저장소 소유자 `이동은` 제외).

### 원본(`_raw/`)은 저장소 안에 둔다 — 다만 비밀 값은 가리거나 파일을 삭제한다

이 vault는 **여러 환경에서 git으로 받아 쓰므로 원본(`_raw/`)도 저장소에 포함한다.** `_raw/`를 통째로 `.gitignore`에 넣거나 vault 밖으로 옮기지 않는다. 가린 뒤에도 파일은 그대로 두고 위키의 `[[_raw/_archived/…]]` 링크와 `snapshots:`를 유지한다.

| 대상 | 가리는 방법 |
|---|---|
| FCM 서버 키, 기기 토큰, API 키 | `[FCM_SERVER_KEY_REMOVED]` 등으로 치환 |
| ID/PASSWORD, "기본 비밀번호는 …", 표의 Password 값 | `[PASSWORD_REMOVED]` |
| 사용자 식별자(`device_id`, `mdn`, `snsId`), MAC·시리얼 | `[REMOVED]`, `[MAC/SN]` |
| 문서 공유 링크 | `[LINK_REMOVED]` |
| 전화번호, 메일 주소, IP 주소 | `[PHONE]`, `[EMAIL]`, `[IP]` |
| **카드번호 전체·부분(4-4-4-4, 연속 16자리, 앞 4자리만 가린 형태)** | `카드 ****` |
| **카드 유효기간·만료일** | `[유효기간 제거]` |
| **서버 호스트명과 포트**(회사 도메인의 하위 도메인, `호스트:포트`. 공식 홈페이지 `www.…`는 제외) | `[HOST]` |

가린 뒤에는 `obsidian-wiki cache-update`로 해시를 갱신한다(파일명이 한글이면 NFC/NFD 차이로 키가 어긋날 수 있으니 manifest 키를 확인한다). 마스킹 전 원본은 저장소 밖에 두지 않는다. 필요하면 임시로 두고 작업이 끝나면 즉시 삭제한다.

### 처리 이력 (2026-10-26)

**마스킹**

| 파일 | 가린 내용 |
|---|---|
| `Push Curl.md` | FCM 서버 키·기기 토큰·postman 토큰, 호스트 |
| `Outlook_2022.md`, `Outlook_2023.md` | 계정·비밀번호, 사용자 식별자, 전화번호, 메일, IP, 공유 링크, **카드번호 전체·부분, 카드 유효기간(18건)**, 호스트 |
| `Outlook_2024.md`, `API 명세.md`, `ORBISMAP API DOCS (Agent, Swagger).md` | 서버 IP, `호스트:포트` |
| `서울동행맵_고도화_작업분할표(통합)_v0.5/v0.8.xlsm` | WBS 도구 메타데이터의 작성자 메일(`AUTHOR_EMAIL`) |
| `2023_2310Air VOC반영리스트.xlsx` | 외부 담당자 유선 번호 |
| 위키 `inavi-air-api-overview`, `orbismap-api-docs` | 서버 호스트명 |

**삭제(가릴 수 없는 파일)**

| 파일 | 이유 |
|---|---|
| `AI2023-DD-02[인터페이스정의서]_(아이나비).hwp` 와 `.hwp.pdf` | 서비스 키(64자)와 수집 서버 IP |
| 대만 RouteServer API 설명서 `v0_1`, `v0_4`, `v2_0`, `v2_3` PDF 4개 | 서버 IP |

위 PDF들에서 만든 위키 페이지(`taiwan-routeserver-api`, `orbis-routing-stack`, `vehicle-restriction-routing`)는 규격 내용(경로, 파라미터, 코드)만 남아 있고 서버 주소는 없다. 이 페이지들의 `## Sources`에 원본이 삭제됐다고 적었다.

### 이미 push된 히스토리 사고 (2026-10-26)

Obsidian Git 플러그인의 "vault backup" 커밋(`94e3181`, 10:17)이 검사 없이 전체 파일을 올렸고, 마스킹 전 카드번호, 서버 IP, 서비스 키가 원격에 올라갔다. **원격 `main`을 `08f1825`(`.gitignore`와 README만 있는 커밋)로 되돌려 강제 push했고(사용자 지시), 로컬 reflog와 객체도 정리했다.** 다만 다음은 남는다.

- GitHub 서버가 가리키는 곳이 없는 옛 커밋을 SHA 주소로 한동안 접근 가능하게 둘 수 있다. 완전한 제거는 GitHub Support 요청이나 저장소 재생성이 필요하다.
- **올라갔던 서비스 키는 교체 대상이다.** 히스토리 삭제만으로는 충분하지 않다. 담당 팀에 교체를 문의한다.
- 법인카드 번호와 유효기간이 올라갔으니 경영지원 확인이 필요하다.
- **Obsidian Git의 "Create backup"과 자동 백업은 쓰지 않는다.** 쓰려면 먼저 `_meta/security-scan.py`를 통과해야 한다.

### 검사가 놓친 사례 (이 때문에 스크립트가 지금 형태다)

| 놓친 것 | 원인 | 대응 |
|---|---|---|
| 한글 파일명의 파일 | macOS 파일명이 NFD인데 패턴은 NFC라 `find -iname`, `.gitignore`, manifest 키가 어긋남 | 파일명을 NFC로 정규화해 비교한다. `.gitignore`는 와일드카드(`API*설명서`)를 쓴다 |
| 압축된 HWP 안의 키·IP | `strings`로는 압축 본문이 보이지 않음 | `olefile`로 본문을 직접 풀어서 검사한다(`pip install olefile`) |
| 이미지형 PDF | 글자 추출이 안 됨 | "검사 불가"로 보고하고 사람이 직접 열어 보고 `MANUAL_OK`에 근거와 함께 기록한다 |
| xlsm 안의 작성자 메일 | `.xlsm`을 검사 대상 형식에서 빠뜨림 | docx/pptx/xlsx/xlsm 내부 XML을 모두 연다 |
| 카드번호의 부분 마스킹과 유효기간 | `****-1234-5678-9012`, `YYYY.MM` 형태를 패턴에 안 넣음 | 카드번호형, 카드 유효기간 패턴을 추가했다 |
| IP가 아닌 서버 주소 | 도메인과 포트(`호스트:포트`)를 검사하지 않음 | `호스트:포트`, 회사 도메인 패턴을 추가했다 |
| 사용자 계정의 자동 백업 커밋 | 커밋 전 검사 절차가 없었음 | 아래 "커밋/푸시 전 필수 절차" |

### 자동 차단 (git 훅)

`pre-commit`과 `pre-push` 훅이 `_meta/security-scan.py`를 실행하고, 통과하지 못하면 **커밋과 push를 막는다.** Obsidian Git의 "Create backup"도 시스템 git을 쓰므로 똑같이 막힌다. 훅은 `.git` 안에 있어 저장소에 따라오지 않으니, 새 환경에서는 한 번 `sh _meta/install-git-hooks.sh`를 실행한다. `--no-verify`로 우회하지 않는다.

### 커밋/푸시 전 필수 절차

1. `python3 _meta/security-scan.py`를 실행한다(HWP를 검사하려면 `olefile` 필요). **종료 코드가 0이어야 한다.** BLOCK이 나오면 위 원칙대로 가리거나 파일을 삭제하고 다시 실행한다. 검사 불가 파일이 있으면 직접 열어 확인한 뒤 `MANUAL_OK`에 기록한다.
2. `git add -A`, `git add .`, `git commit -a`를 쓰지 않는다. **경로를 하나씩 지정**해서 스테이징한다.
3. 스테이징 직후 `git diff --cached --name-only`로 목록을 확인한다. 100MB를 넘는 파일이 없는지도 본다.
4. 푸시 전에 `git log origin/main..HEAD --stat`로 올라갈 파일을 한 번 더 확인한다.
5. 점검 결과는 **값을 출력하지 않고** 파일 경로, 항목, 건수만 보고한다. 비밀 값을 대화나 로그에 옮기지 않는다.
6. 이미 커밋·푸시된 뒤에 발견되면 즉시 사용자에게 알린다. 푸시된 경우 키 교체와 히스토리 정리가 필요하다. **히스토리 재작성과 force-push는 사용자의 명시 지시가 있을 때만** 한다.

### `.gitignore`

원본은 올리므로 `_raw/`는 제외하지 않는다. 비밀 파일 종류와 Office 임시 파일만 막는다. 보안 사유로 파일을 막는 용도로 쓰지 않는다(그런 파일은 삭제한다).

```
.env
*.pem
*.p12
*.jks
token.json
~$*
```

## 위키 작성 규칙 (ingest 시)

- 원본에 비밀·개인정보가 있으면 **값은 옮기지 않고** 구조만 정리한다. 예: "서비스 키와 수집 서버 IP가 원본에 있음(미수록)".
- 사람 이름, 연락처, 서버 IP, 호스트, 포트, 공유 링크는 쓰지 않는다. 역할(예: 고객사 콜앱 개발자)로 적는다.
- 회사 내부 문서에서 나온 페이지에는 `visibility/internal`, 인사·평가·개인정보는 `visibility/pii` 태그를 붙인다.
- 새 원본(특히 메일, 로그, 설계서, 연동 규격)을 `_raw/`에 넣으면 **수집 직후 `_meta/security-scan.py`를 실행**해서 BLOCK을 처리하고(마스킹 또는 삭제), 최종 보고에서 어떤 파일에 무엇이 있었는지와 처리 결과를 알린다.
- Confluence 같은 외부 시스템에서 가져올 때도 같은 규칙이다. 대화창과 로그에 값이 보이더라도 위키와 `_raw/`에는 옮기지 않는다. 작업용 임시 덤프는 작업이 끝나면 즉시 삭제한다.

## 구조 메모

- 위키 페이지: `concepts/`, `entities/`, `skills/`, `references/`, `synthesis/`, `journal/`, `projects/<이름>/`
- 원본: `_raw/articles/<폴더>`(미수집), 수집 후 `_raw/_archived/`(평평한 구조)
- 관리 파일: `index.md`, `log.md`, `hot.md`, `.manifest.json`, `_meta/`. `index.md`, `log.md`, `hot.md`는 직접 편집하지 않고 `obsidian-wiki memory sync`로만 갱신한다.
- 보안 검사: `_meta/security-scan.py` (허용 예외 `ALLOW`와 수동 확인 목록 `MANUAL_OK`가 이 파일 안에 있다)
- 설정: `~/.config/obsidian-wiki/config` (`OBSIDIAN_VAULT_PATH=/Users/dongeun/Develop/MyWiki`)
- Confluence 스페이스 "아이나비 에어 & NSDK" 419페이지는 압축 없이 반영했다(`projects/orbis-sdk/`, `projects/inavi-air/`의 허브 페이지 14개에서 시작).
