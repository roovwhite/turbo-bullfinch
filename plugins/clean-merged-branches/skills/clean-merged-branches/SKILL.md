---
name: clean-merged-branches
description: Clean up local Git branches already merged into main. Use for requests to delete, prune, or list merged local branches while keeping main.
---

# Clean merged branches

Run from the target Git repository using the script next to this skill:

- `sh <skill-dir>/scripts/clean-merged-branches.sh` lists merged branches available for deletion.
- `sh <skill-dir>/scripts/clean-merged-branches.sh --apply` deletes them using `git branch -d`. Use this when the user explicitly requests cleanup. For a list or a question about the workflow, use preview only.

The script uses the current local `main` and checks commit ancestry. It preserves `main`, branches checked out in any worktree, and remote refs. Squash and rebase merges may leave original commits outside the history of `main`. Leave those branches in place. If Git refuses a deletion, report the reason. Summarize which branches were deleted or skipped.
