# Turbo Bullfinch

![turbo-bullfinch logo](logo.png)

Turbo Bullfinch gives your AI coding agent a few good habits for the last mile of development. Use it to turn a stiff draft into something you’d actually send, pick the changes that belong in a commit, or open a pull request that tells reviewers what changed and why.

## Skills and plugins

- [humanized](plugins/humanized/README.md) helps write, edit, and check natural-sounding text. Available for Claude Code, Codex, and other agents supporting Agent Skills.
- [commit](plugins/commit/skills/commit/SKILL.md) reviews and commits task changes with a task ID.
- [push](plugins/push/skills/push/SKILL.md) commits task changes and pushes the current branch.
- [mr](plugins/mr/skills/mr/SKILL.md) reviews and publishes task changes as a GitLab merge request or GitHub pull request.

The Git skills ask for a task ID when creating a commit. `mr` also requires an authenticated CLI for the Git host.

## Claude Code marketplace

```bash
claude plugin marketplace add roovwhite/turbo-bullfinch
claude plugin install humanized@turbo-bullfinch
claude plugin install commit@turbo-bullfinch
claude plugin install push@turbo-bullfinch
claude plugin install mr@turbo-bullfinch
```

## Codex and other agents

From a clone of this repository, copy each desired skill directory into the agent's skills directory. For example, to install `commit`, `push`, and `mr` for the current Codex user:

```bash
mkdir -p ~/.agents/skills
cp -R plugins/commit/skills/commit ~/.agents/skills/
cp -R plugins/push/skills/push ~/.agents/skills/
cp -R plugins/mr/skills/mr ~/.agents/skills/
```

If a destination already exists, update or remove it first to avoid nesting directories. Start a new session and invoke the skills with `$commit`, `$push`, or `$mr`. For `humanized` and project-local installation, see its [installation instructions](plugins/humanized/README.md). Other agents supporting Agent Skills can use the same skill directories in their own configured locations.
