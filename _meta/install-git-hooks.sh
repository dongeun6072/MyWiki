#!/bin/sh
# 새 환경에서 한 번 실행: sh _meta/install-git-hooks.sh
# 커밋 전·push 전에 _meta/security-scan.py를 실행해서 통과하지 못하면 막는다(Obsidian Git 포함).
ROOT=$(git rev-parse --show-toplevel) || exit 1
for H in pre-commit pre-push; do
  cat > "$ROOT/.git/hooks/$H" <<'HOOK'
#!/bin/sh
ROOT=$(git rev-parse --show-toplevel) || exit 1
cd "$ROOT" || exit 1
# GUI 앱(Obsidian Git, IDE)은 PATH에 Homebrew가 없어 pdftotext를 못 찾고 PDF가 전부 "검사 불가"가 된다
PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"; export PATH
OUT=$(/usr/bin/env python3 _meta/security-scan.py 2>&1)
CODE=$?
if [ $CODE -ne 0 ]; then
  echo "❌ 보안 검사 실패: 차단했습니다 (종료코드 $CODE)" >&2
  echo "$OUT" | tail -25 >&2
  echo "→ 값을 가리거나 파일을 삭제한 뒤 다시 시도하세요. 규칙은 CLAUDE.md" >&2
  exit 1
fi
exit 0
HOOK
  chmod +x "$ROOT/.git/hooks/$H"
done
echo "설치 완료: pre-commit, pre-push"
