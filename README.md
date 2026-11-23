# Turbo Bullfinch

![turbo-bullfinch logo](logo.png)

Turbo Bullfinch collects skills for writing and editing. Use it to develop a fictional character or revise a draft for its reader.

## Skills and plugins

- <img src="plugins/humanized/logo.png" alt="" width="40" height="40"> [humanized](plugins/humanized/README.md) helps you write for your audience, cut filler, and preserve the author’s voice and facts. Review mode explains what sounds formulaic while keeping the draft intact. Available for Claude Code, Codex, and other agents supporting Agent Skills.
- <img src="plugins/character/logo-portraits.png" alt="" width="40" height="40"> [character](plugins/character/skills/character/SKILL.md) develops fictional characters from a premise, deepens existing ones, and reviews dialogue and decisions in scenes.

## Claude Code marketplace

```bash
claude plugin marketplace add roovwhite/turbo-bullfinch
claude plugin install humanized@turbo-bullfinch
claude plugin install character@turbo-bullfinch
```

## Codex and other agents

For `humanized`, see its [installation instructions](plugins/humanized/README.md).

For `character` in Codex, copy `plugins/character/skills/character` into `~/.agents/skills/`, or into `.agents/skills/` in your book project. In a new session, try `$character A former detective goes home after her father's death. She is generous with her time but makes people uneasy. The book is a restrained mystery.`

In Claude Code, invoke the skill with `/character:character`. To try the plugin from this checkout, start Claude Code with `claude --plugin-dir ./plugins/character`.
