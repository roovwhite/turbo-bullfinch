# Turbo Bullfinch

![turbo-bullfinch logo](logo.png)

A collection of excellent skills to speed up your work and make things more convenient. Let’s bring the joy back to development!

## Skills and plugins

- [people-text](plugins/people-text/README.md) helps write, edit, and check natural-sounding text. Available for Claude Code, Codex, and other agents supporting Agent Skills.
- [commit](plugins/commit/skills/commit/SKILL.md) reviews and commits task changes with a task ID.
- [mr](plugins/mr/skills/mr/SKILL.md) reviews and publishes task changes as a GitLab merge request or GitHub pull request.

Both `commit` and `mr` require a task ID; if one cannot be found, they ask for it. `mr` also requires an authenticated CLI for the Git host.

## Claude Code marketplace

```bash
claude plugin marketplace add roovwhite/turbo-bullfinch
claude plugin install people-text@turbo-bullfinch
claude plugin install commit@turbo-bullfinch
claude plugin install mr@turbo-bullfinch
```

## Codex and other agents

From a clone of this repository, copy each desired skill directory into the agent's skills directory. For example, to install `commit` and `mr` for the current Codex user:

```bash
mkdir -p ~/.agents/skills
cp -R plugins/commit/skills/commit ~/.agents/skills/
cp -R plugins/mr/skills/mr ~/.agents/skills/
```

If a destination already exists, update or remove it first to avoid nesting directories. Start a new session and invoke the skills with `$commit` or `$mr`. For `people-text` and project-local installation, see its [installation instructions](plugins/people-text/README.md). Other agents supporting Agent Skills can use the same skill directories in their own configured locations.
