#!/usr/bin/env python3
"""볼트 보안 검사. 사용: python3 _meta/security-scan.py [--verbose]

- 모든 파일의 '본문'을 형식별로 열어서 검사한다(md/txt/json/html, docx/pptx/xlsx, pdf, hwp, doc/ppt/xls).
- 검사하지 못한 파일(이미지형 PDF, 읽기 실패 등)은 "검사 불가"로 따로 보고한다. 0이 아니면 사람이 직접 열어 본다.
- 걸린 항목은 ALLOW(확인된 예외, 근거 포함)에 없으면 차단(BLOCK)이다. BLOCK이 있으면 종료 코드 1.
- 값은 출력하지 않는다. 파일 경로와 항목, 건수만 출력한다.
- HWP 본문 추출용 olefile은 _meta/lib에 포함되어 있다(별도 설치 불필요).
"""
import os, re, sys, zipfile, subprocess, unicodedata, zlib, struct, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
VERBOSE = '--verbose' in sys.argv

sys.path.insert(0, os.path.join(ROOT, '_meta', 'lib'))   # 포함된 olefile(HWP 본문 추출용)
try:
    import olefile
except ImportError:
    olefile = None

# ── 검사 항목 ────────────────────────────────────────────────────────────
PATTERNS = {
    'FCM키': r'APA91[A-Za-z0-9_-]{20,}',
    '개인키': r'BEGIN [A-Z ]*PRIVATE KEY',
    'AWS키': r'AKIA[0-9A-Z]{16}',
    'Google API키': r'AIza[0-9A-Za-z_-]{30,}',
    'JWT': r'eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.',
    'Bearer토큰': r'[Bb]earer\s+[A-Za-z0-9._-]{20,}',
    '키·토큰값': r'(?i)(service ?key|api[_ -]?key|app[_ -]?key|secret|token|authorization|인증키|서비스키)["\']?\s*[:=：]?\s*["\']?(?![A-Za-z_]*(?:here|your|example|xxx))[A-Za-z0-9+/_=%-]{24,}',
    '긴16진수(40자+)': r'(?<![A-Za-z0-9/_-])[A-Fa-f0-9]{40,}(?![A-Za-z0-9])',
    'ID/PW값': r'(?i)(passw(or)?d|pwd|비밀번호)\s*[:=：]\s*(?!\[|<|\*|["\']\s*["\'])[^\s\[\]<,)"]{4,}',
    '카드번호형': r'(?<!\d)\d{4}[- ]\d{4}[- ]\d{4}[- ]\d{4}(?!\d)|\*{2,4}[- ]\d{4}[- ]\d{4}[- ]\d{4}',
    '카드 유효기간': r'카드\s*\*{4}\s*(?:\n\s*)*20\d{2}\s*[./-]\s*\d{1,2}|(?:카드|유효)\s*(?:유효\s*기간|만료일?)\s*[:：]?\s*20\d{2}\s*[./-]\s*\d{1,2}',
    '계좌번호': r'계좌[^\n]{0,20}(?<!\d)\d{3,6}-\d{2,6}-\d{4,8}(?!\d)',
    '주민번호형': r'(?<!\d)\d{6}-[1-4]\d{6}(?!\d)',
    '휴대폰': r'(?<!\d)01[016789][-. ]?\d{3,4}[-. ]?\d{4}(?!\d)',
    '유선전화': r'(?<!\d)0(?:2|[3-6]\d)[-. ]\d{3,4}[-. ]\d{4}(?!\d)',
    '메일': r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
    'IP주소': r'(?<![\d.])(?:[1-9]\d{1,2})\.\d{1,3}\.\d{1,3}\.\d{1,3}(?![\d.])',
    '호스트:포트': r'\b[a-z0-9-]+(?:\.[a-z0-9-]+)+:\d{2,5}\b',
    '회사호스트': r'\b(?!www\.)[a-z0-9-]+(?:\.[a-z0-9-]+)*\.(?:inavi|inavisys|thinkware|thinkwaresys|tmoney|lbstech)\.(?:com|co\.kr|net)\b',
    '국제/인터넷전화': r'\+82[ -]?\(?0?\d{1,2}\)?[ -]\d{3,4}[ -]\d{4}|(?<!\d)0[5-7]0[-. ]\d{3,4}[-. ]\d{4}(?!\d)',
    '공유링크': r'(dooray\.com/|sharepoint\.com|docs\.google\.com|drive\.google\.com|gofile\.io|naver\.me|bit\.ly|forms\.gle|figma\.com|notion\.so|notion\.site|notion\.com/|slack\.com/archives|teams\.microsoft\.com/meet)',
}
RX = {k: re.compile(v) for k, v in PATTERNS.items()}

# ── 확인된 예외 (경로 일부, 항목, 근거). 근거 없이 추가하지 않는다 ───────────────
ALLOW = [
    ('.manifest.json', '긴16진수(40자+)', 'SHA-256 콘텐츠 해시'),
    ('_raw/', '카드번호형', 'MR 포맷 문서의 비트 패턴 예시(0000 0000 …)이고 카드가 아님'),   # MR(X1…) docx 3개로 한정 확인됨
    ('CLAUDE.md', '공유링크', '금지 대상 도메인을 규칙으로 나열한 문장'),
    ('CLAUDE.md', '카드번호형', '마스킹 규칙 설명(****-####)'),
    ('CLAUDE.md', 'IP주소', '규칙 설명의 예시 표기'),
    ('_meta/security-scan.py', None, '이 스크립트 자체의 정규식'),
    ('_meta/lib/', None, '서드파티 라이브러리 olefile 코드(저작권 표기 메일 등)'),
    ('.obsidian/', None, '서드파티 플러그인 코드와 설정(제작자 메일, 코드 상수)'),
    ('UIUX가이드라인', '휴대폰', '공개 행정 문서의 입력 예시와 공식 문의처'),
    ('UIUX가이드라인', '메일', '공개 행정 문서의 공식 문의 메일'),
    ('UIUX 가이드라인', '휴대폰', '공개 행정 문서의 입력 예시'),
    ('UIUX 가이드라인', '유선전화', '공개 행정 문서의 입력 예시'),
    ('UIUX 가이드라인', '메일', '공개 행정 문서의 공식 문의 메일'),
    ('디지털 정부', None, '공개 행정 가이드 문서의 예시 문자열'),
    ('취약점', None, '공개 보안 가이드의 코드·접속 예시(password=, 127.0.0.1, 192.168.x.x 등)'),
    ('웹 접근성', '메일', '공개 접근성 지침의 문의 메일'),
    ('디지털포용법', None, '법령 원문(법령 번호, 담당 부서 전화)'),
    ('모바일 전자정부 서비스 관리 지침', None, '행정안전부 예규 원문'),
    ('제안요청서', None, '공개 입찰 문서의 계약 담당 부서 공식 연락처'),
    ('openapi.json', '유선전화', 'API 응답 예시 값(02-123-4567 형태)'),
    ('navi-swagger.html', '유선전화', 'API 응답 예시 값(02-123-4567 형태)'),
    ('ConnectedServicesPlatformGuide', None, 'TomTom 공개 가이드 예시(your_api_key, 공식 도메인)'),
    ('KS X 3253', None, '공개 표준 문서 예시'),
    ('KSX3253', None, '공개 표준 문서 예시'),
    ('KWCAG', None, '공개 접근성 지침 예시'),
    ('작업분할표', '긴16진수(40자+)', 'WBS 도구의 시트 위치 상태값(SCHEDULE_SHEET_POSITION:…)이고 비밀이 아님'),
    ('직무기술_이동은.doc', '카드번호형', 'GUID 문자열'),
]
PUBLIC_IP_OK = re.compile(r'^(127\.|0\.|192\.168\.|169\.254\.)')   # 루프백/예시 대역은 항목 판정에서 제외


# ── 글자를 추출할 수 없어 사람이 직접 열어 본 파일 (경로 일부, 확인일, 근거) ─────────────
MANUAL_OK = [
    ('아이나비스탬프-오르다', '2026-10-26', '6쪽 홍보성 발표 자료. 서비스 소개와 스토어용 QR뿐이고 내부 정보 없음'),
    ('기술적_취약점_분석_평가_방법_상세가이드.pdf', '2026-10-26', '과기정통부·KISA 공개 가이드(756쪽 이미지형). 표지와 본문 표본 확인'),
]


def manual_ok(path):
    n = unicodedata.normalize('NFC', path)
    return any(sub in n for sub, _, _ in MANUAL_OK)


def allowed(path, cat):
    for sub, c, _ in ALLOW:
        if sub in unicodedata.normalize('NFC', path) and (c is None or c == cat):
            return True
    return False


# ── 본문 추출 ────────────────────────────────────────────────────────────
def hwp_text(p):
    o = olefile.OleFileIO(p)
    hdr = o.openstream('FileHeader').read()
    if hdr[36] & 2:
        raise RuntimeError('암호화된 HWP')
    comp = bool(hdr[36] & 1)
    out = ''
    for s in o.listdir():
        if s[0] == 'BodyText':
            d = o.openstream(s).read()
            if comp:
                d = zlib.decompress(d, -15)
            i = 0
            while i < len(d):
                h = struct.unpack('<I', d[i:i + 4])[0]
                tag = h & 0x3ff
                sz = (h >> 20) & 0xfff
                i += 4
                if sz == 0xfff:
                    sz = struct.unpack('<I', d[i:i + 4])[0]
                    i += 4
                if tag == 67:
                    out += d[i:i + sz].decode('utf-16le', 'ignore') + '\n'
                i += sz
    return out


def extract(p):
    """텍스트 또는 None(검사 불가)"""
    ext = os.path.basename(p).lower().rsplit('.', 1)[-1] if '.' in os.path.basename(p) else ''
    try:
        if ext in ('md', 'txt', 'json', 'html', 'csv', 'xml', 'yml', 'yaml', 'js', 'css', 'sh', 'py', 'svg', 'tsv'):
            return open(p, encoding='utf-8', errors='ignore').read()
        if ext in ('docx', 'pptx', 'xlsx', 'docm', 'xlsm'):
            z = zipfile.ZipFile(p)
            return ' '.join(re.sub(r'<[^>]+>', ' ', z.read(n).decode('utf-8', 'ignore'))
                            for n in z.namelist() if n.endswith(('.xml', '.rels')))
        if ext == 'pdf':
            t = subprocess.run(['pdftotext', '-q', p, '-'], capture_output=True, text=True).stdout
            return t if len(t.strip()) >= 200 else None        # 이미지형 PDF
        if ext == 'hwp':
            return hwp_text(p) if olefile else None
        if ext in ('doc', 'ppt', 'xls'):
            a = subprocess.run(['strings', '-n', '5', p], capture_output=True, text=True).stdout
            b = subprocess.run(['strings', '-n', '5', '-e', 'l', p], capture_output=True, text=True).stdout
            return a + b
        if ext in ('png', 'jpg', 'jpeg', 'gif', 'webp', 'ico', 'zip', 'mp4', 'ds_store', 'ttf', 'woff', 'woff2'):
            return ''                                           # 비텍스트(이미지 안의 글자는 검사 못 함)
        if os.path.basename(p) in ('.DS_Store',):
            return ''
        return open(p, encoding='utf-8', errors='ignore').read()
    except Exception:
        return None


def git_ignored(path):
    return subprocess.run(['git', 'check-ignore', '-q', '--', path], capture_output=True).returncode == 0


def main():
    findings = collections.defaultdict(collections.Counter)
    unreadable, images = [], []
    nfiles = 0
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d != '.git']
        for f in files:
            p = os.path.join(root, f)[2:]
            nfiles += 1
            t = extract(p)
            if t is None:
                unreadable.append(p)
                continue
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                images.append(p)
            for cat, rx in RX.items():
                n = 0
                for m in rx.finditer(t):
                    if cat == 'IP주소' and PUBLIC_IP_OK.match(m.group(0)):
                        continue
                    if cat == 'IP주소' and any(int(x) > 255 for x in m.group(0).split('.')):
                        continue
                    n += 1
                if n:
                    findings[p][cat] += n
    block, ok = collections.Counter(), collections.Counter()
    block_files = collections.defaultdict(list)
    for p, c in sorted(findings.items()):
        for cat, n in c.items():
            if allowed(p, cat):
                ok[cat] += n
            else:
                block[cat] += n
                block_files[p].append(f'{cat}:{n}')
    print(f'검사 파일 {nfiles}개 (이미지 {len(images)}개는 글자 검사 불가)')
    print(f'확인된 예외(ALLOW): {sum(ok.values())}건')
    pending = [p for p in unreadable if not manual_ok(p)]
    print(f'수동 확인 완료(MANUAL_OK): {len(unreadable) - len(pending)}개')
    if pending:
        print(f'\n[검사 불가 {len(pending)}개] 직접 열어 확인해야 함:')
        for p in pending:
            print('  ', unicodedata.normalize('NFC', p))
    if block_files:
        print(f'\n[차단 BLOCK {sum(block.values())}건 / 파일 {len(block_files)}개]')
        for p, v in block_files.items():
            ign = ' (git 무시됨)' if git_ignored(p) else ''
            print('  ', unicodedata.normalize('NFC', p)[:90], ', '.join(v) + ign)
        print('\n=> 파일 안의 값을 가리거나(마스킹) 가릴 수 없으면 파일을 삭제한다. CLAUDE.md 참고.')
        sys.exit(1)
    if pending:
        sys.exit(2)
    print('\n차단 항목 없음')


if __name__ == '__main__':
    main()
