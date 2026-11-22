---
name: commit
description: Review and commit the current task’s changes with a task ID and concise message.
---

# Commit task changes

Use this skill when the user asks to commit changes in the current repository.

1. Inspect `git status`, the current branch, staged and unstaged diffs, and untracked files. Review the actual changes before staging anything.
2. Identify the task ID from the branch name, task documentation, or conversation, and follow repository-specific instructions. If the ID cannot be determined, stop before staging or committing and ask the user for it.
3. Stage only files that belong to the requested task. Do not use `git add -A` when that could include unrelated work. If task and unrelated changes are mixed in a file or cannot be safely separated, ask the user how to proceed.
4. Write a concise commit subject in the format `<TASK-ID>: <short description>`, for example: `TASK-008: затемнение границы при фокусе`. Use the task’s language and describe the change accurately.
5. Commit the staged task changes and report the commit hash and subject. If the commit fails, report the failure without claiming success.
