#!/bin/sh
set -eu

case "${1:---dry-run}" in
    --dry-run|--apply) mode=${1:---dry-run} ;;
    *) printf 'Usage: %s [--dry-run|--apply]\n' "$0" >&2; exit 2 ;;
esac

if [ "$#" -gt 1 ]; then
    printf 'Usage: %s [--dry-run|--apply]\n' "$0" >&2
    exit 2
fi

base=refs/heads/main
if ! git rev-parse --verify --quiet "$base^{commit}" >/dev/null; then
    printf 'A local main branch is required.\n' >&2
    exit 1
fi

merged=$(git for-each-ref --merged="$base" \
    --format='%(if)%(worktreepath)%(then)checked-out%(else)available%(end) %(refname:lstrip=2)' \
    refs/heads/)

found=0
failed=0
while IFS=' ' read -r status branch; do
    case "$branch" in
        ''|main) continue ;;
    esac

    if [ "$status" = checked-out ]; then
        printf 'Skipped (checked out): %s\n' "$branch"
        continue
    fi

    found=1
    if [ "$mode" = --dry-run ]; then
        printf 'Merged: %s\n' "$branch"
    elif ! git merge-base --is-ancestor "refs/heads/$branch" "$base"; then
        printf 'Skipped (ancestry check failed): %s\n' "$branch" >&2
        failed=1
    elif ! git branch -d -- "$branch"; then
        failed=1
    fi
done <<EOF_BRANCHES
$merged
EOF_BRANCHES

if [ "$found" -eq 0 ]; then
    printf 'No merged local branches available for cleanup.\n'
fi

exit "$failed"
