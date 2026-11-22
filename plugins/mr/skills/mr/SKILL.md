---
name: mr
description: Review current task changes, commit them, push the branch, and create a GitLab merge request or GitHub pull request.
---

# Create a merge request

Use this skill when the user asks to publish the current task branch as a merge request or pull request. The user’s authorization to run this workflow covers committing and pushing the current task’s changes and opening the review request; it does not cover unrelated changes or other external actions.

1. Inspect `git status`, the current branch, the diff, and recent commits. Identify the task ID from the branch, task documentation, or conversation. Follow repository instructions for task IDs and commit/title format. If the task ID cannot be established, stop before committing, pushing, or creating the request and ask the user for it.
2. Review every changed file and confirm the changes belong to this task. Stage and commit only the task’s changes. If unrelated or ambiguous changes are mixed in, leave them untouched and ask how to proceed. Format the commit subject as `<TASK-ID>: <short description>`, for example: `TASK-008: затемнение границы при фокусе`.
3. Identify the target branch from repository configuration (prefer the remote default branch; otherwise use the project’s documented base branch). Review the branch commits and aggregate change summary against that base, for example with `git log <base>..HEAD --oneline` and `git diff <base>...HEAD --stat`. Use the reviewed changes to draft:
   - A concise Russian title containing the task ID and a short task name.
   - A Russian description with 2–4 short bullets under **Что сделано** and a short **Затронутые модули / файлы** section naming the key components.
   - Explain the purpose when it is not already clear from the change summary. Keep the description factual and omit empty sections.
4. Check whether a request for this branch already exists. If one exists, report its URL and do not create a duplicate.
5. Push the current branch with `git push -u origin HEAD`.
6. Create the review request using the available authenticated CLI:
   - GitLab: if a `glab` skill is available, follow its instructions; otherwise check the installed CLI's help. Create with `glab mr create --title "..." --description-file <file> --yes` (or the installed version’s equivalent for a description file).
   - GitHub: create with `gh pr create --title "..." --body-file <file>`.
   Use a temporary description file or a structured tool argument to preserve Markdown and avoid shell-quoting errors. Do not include credentials or tokens in output.
7. Return the final title, description, and created request URL. If commit, push, or creation fails, report the exact completed steps and the failure; do not claim that the request was created.
