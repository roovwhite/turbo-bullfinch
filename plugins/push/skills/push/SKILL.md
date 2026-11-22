---
name: push
description: Commit the current task's changes and push the current branch when asked to push or запушить.
---

# Commit and push task changes

1. Inspect the current branch, upstream, staged and unstaged diffs, and untracked files. Identify the task's changes and review them before staging. If HEAD is detached, resolve the intended branch with the user first.
2. When a new commit is needed, get the task ID from the branch, task documentation, or conversation. If it is missing, ask before staging. Follow repository conventions and use `<TASK-ID>: <short description>` in the task's language. Stage only task changes, inspect the staged diff, and commit. Preserve unrelated changes, including staged work. If the commit cannot be isolated safely, ask how to proceed.
3. Use the configured upstream as the destination. For a new branch, use the same branch name on the intended remote (usually `origin`). Review the outgoing commits against the destination or, for a new remote branch, against its base. If the push would include unrelated local commits, clarify the scope first. If the task is already committed, skip the commit step.
4. Push the current branch explicitly with `git push <remote> HEAD:refs/heads/<destination-branch>`, adding `-u` on the first push to establish tracking. Use a normal push. On rejection, report the reason and the local commit state. Do not force-push or open a review request.
5. Report the commit hash and subject and the remote branch that received it. If the branch is already up to date, say so.
