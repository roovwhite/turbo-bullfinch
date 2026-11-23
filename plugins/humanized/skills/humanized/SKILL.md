---
name: humanized
description: "Draft, edit, or review prose for natural wording, an appropriate register, and the author's voice. Use when asked to make text sound more human, remove AI-like phrasing, or check a draft for formulaic language (это похоже на нейросеть?, только проверь)."
---

# humanized

Write for the reader and the situation. Preserve the author's meaning and voice. The examples below show editorial problems to look for in context.

## Draft or edit

1. Infer the audience, medium, and purpose from the request and draft. In a work thread, lead with the decision and give the reason and next step. In a client email, put dates, consequences, and required actions where the client can find them. In a personal post, use the author's actual observations and preserve their register. For a résumé, describe the work and its outcome at the level of detail the source supports. If the user supplies a writing sample, use it to guide register, vocabulary, and rhythm.
2. Read for meaning before changing words. Check what each paragraph contributes: a fact, a reason, a consequence, an action, or a detail that gives the text its voice. Cut generic praise, empty conclusions, and repeated assertions. If a vague sentence carries a real claim, restate it using facts already supplied. Move or merge material when the task allows it and the reader benefits. For a narrow edit, keep everything outside the requested scope verbatim.
3. Revise phrasing in context. Prefer a clear verb and name the actor when the source identifies one. Keep meaningful qualifications, distinctions, transitions, and genre conventions. Preserve characteristic wording and established terms such as API, pull request, or деплой. Keep typographic punctuation, lists, and emphasis where they fit the author's style or the medium. Apply a house style when requested.
4. Verify the result against the source. Preserve facts, dates, names, attributions, and the original degree of certainty. Keep code, quotations, and user-supplied links intact, subject to explicit scope and removable service tracking parameters on editable links. Never invent numbers, experience, motives, or evidence. If a requested detail is missing, finish what the source supports and ask a targeted question or mark the gap in a draft if appropriate.

Return the edited text. Explain substantive changes if asked. If the draft already fits the purpose, leave it as supplied and say so briefly.

### Patterns worth checking

- Inflated significance or generic praise: “играет ключевую роль”, “открывает новые горизонты”. State what changed when the source supports it, or cut the praise.
- Claimed analysis without a link to the evidence: “что подчёркивает важность…”, “по мнению экспертов”. Name the evidence or source if known. Keep uncertainty and attribution when they affect the claim.
- Bureaucratic phrasing: “осуществлять проверку документов” → “проверять документы”. Keep established legal, technical, or organisational terms where they carry a precise meaning.
- Formulaic rhythm: repeated “не только… но и…”, padded three-item lists, or paragraphs that all end with a conclusion. Revise when the pattern adds repetition, false emphasis, or filler. Keep useful contrasts and lists with real items.
- Chatbot wrapper: “Конечно! Вот переписанный текст” or “Надеюсь, это помогло!” outside the requested text. Keep real greetings, sign-offs, and conditional requests that do a job in the intended message.

## Review only

When the user asks to check the text without editing, give a short assessment of how it reads in context. Quote the strongest examples and explain the specific issue with each, such as empty emphasis, an unsupported inference, or a generic opening that delays the point. If no meaningful issues stand out, say so. Style alone cannot establish authorship. Leave the text as supplied and offer rewrites only if requested.

## Mechanical check

When Python 3 and the shell are available, run the adjacent script on the text itself, excluding any editorial notes. The default checks flag likely chatbot wrapper at the boundaries of the prose and known service tracking parameters on links. Reports include the line, rule, and fragment. Exit code 1 indicates a finding that needs context; the script makes no edits.

```bash
python3 /path/to/humanized/lint.py draft.md
```

Pass `--ascii-punctuation` only when the user or destination calls for ASCII dashes and quotes. If the script is unavailable, review the boundaries and links by hand. Verify accessible sources when needed and report verification limits accurately.
