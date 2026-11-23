# Turbo Bullfinch

![turbo-bullfinch logo](logo.png)

Turbo Bullfinch gives your AI assistant specific guidance for writing and editing. It starts with your material, whether that’s a draft, a story premise, or a scene, and uses your audience, voice, and existing decisions to guide its suggestions.

## Skills and plugins

- <img src="plugins/humanized/logo.png" alt="" width="40" height="40"> [humanized](plugins/humanized/README.md) is for writers, editors, and anyone drafting posts, articles, or work emails. Use it to cut filler, clarify what the reader needs to know, and keep the author’s voice and facts. In review mode, it points out what sounds formulaic and explains why.
- <img src="plugins/character/logo-portraits.png" alt="" width="40" height="40"> [character](plugins/character/skills/character/SKILL.md) is for fiction writers developing a cast or revising a manuscript. Use it to work out what a character wants, test what they’d do under pressure, or pinpoint why a line of dialogue or a decision feels out of character.

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
