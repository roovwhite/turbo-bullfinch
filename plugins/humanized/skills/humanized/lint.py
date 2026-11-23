#!/usr/bin/env python3
"""Report likely chatbot wrappers, service tracking, and optional punctuation issues."""
import argparse
import re
import sys
from urllib.parse import parse_qsl, urlsplit

DASH = re.compile("[\u2014\u2013]| -- ")
QUOTES = re.compile("[\u00ab\u00bb\u201c\u201d\u201e\u2018\u2019\u2039\u203a]")
SERVICE_SOURCES = {"openai", "chatgpt.com"}

FENCE = re.compile(r"^(`{3,}|~{3,})")
INLINE_CODE = re.compile(r"(`+).+?\1")
URL_BODY = r"""(?:[^\s<>()[\]"«»“”]+|\([^()\s]*\))+"""
URL = re.compile(
    rf"\]\(<?(?P<destination>{URL_BODY})"
    rf"|(?P<absolute>https?://{URL_BODY})",
    re.I,
)
NON_PROSE = re.compile(r"^(?:#{1,6}(?:\s|$)|(?:-{3,}|\*{3,}|_{3,})\s*$)")
MARKUP = re.compile(r"^(?:\s*(?:[-*+] |\d+[.)] ))?\s*[*_]*")

CHATBOT_START = re.compile(
    r"^(?:(?:конечно|безусловно|разумеется|отличный вопрос)[!.,]\s+)?"
    r"(?:вот\s+(?:текст|обзор|переписанный текст|исправленный (?:текст|вариант)|"
    r"обновлённый вариант|готовый вариант)\b"
    r"|ниже\s+(?:представлен[ао]?|привед[её]н[ао]?)\s+(?:подробн\w+\s+)?"
    r"(?:обзор|анализ|текст|вариант|версия)\b)",
    re.I,
)
CHATBOT_END = re.compile(
    r"(?:^|(?<=[.!?])\s+)(?:"
    r"надеюсь,?\s+(?:это|мой ответ)\s+(?:помогло?|поможет)\b"
    r"|(?:сообщите|дайте знать|напишите)(?: мне)?,?\s+если"
    r"\s+(?:хотите|нужен)\s+(?:другой вариант|ещ[её] один вариант)\b)",
    re.I,
)


def blank(match):
    return " " * len(match.group())


def prose_lines(lines):
    """Yield numbered lines outside frontmatter, fences, and block quotes."""
    frontmatter_end = 0
    if lines and lines[0].strip() == "---":
        frontmatter_end = next(
            (number for number, line in enumerate(lines[1:], 2) if line.strip() == "---"),
            0,
        )

    fence = None
    for number, line in enumerate(lines, 1):
        if number <= frontmatter_end:
            continue
        stripped = line.strip()
        marker = FENCE.match(stripped)
        if fence:
            if (
                marker
                and marker[0].startswith(fence)
                and not stripped[marker.end():].strip()
            ):
                fence = None
            continue
        if marker:
            fence = marker[0]
            continue
        if not stripped.startswith(">"):
            yield number, line


def has_service_tracking(url):
    try:
        query = urlsplit(url).query
    except ValueError:
        return False
    return any(
        key.lower() == "utm_source" and value.lower() in SERVICE_SOURCES
        for key, value in parse_qsl(query)
    )


def fragment(line, start, end, width=25):
    left, right = max(0, start - width), min(len(line), end + width)
    return ("..." if left else "") + line[left:right].strip() + ("..." if right < len(line) else "")


def lint(text, *, ascii_punctuation=False):
    hits = []
    boundaries = []
    for number, line in prose_lines(text.splitlines()):
        no_code = INLINE_CODE.sub(blank, line)
        for match in URL.finditer(no_code):
            url = match["destination"]
            if url is None:
                url = match["absolute"].rstrip(".,;:!?")
            if has_service_tracking(url):
                hits.append((number, "utm", fragment(line, match.start(), match.end())))

        plain = URL.sub(blank, no_code)
        if ascii_punctuation:
            for rule, pattern in (("dash", DASH), ("quotes", QUOTES)):
                match = pattern.search(plain)
                if match:
                    hits.append((number, rule, fragment(line, match.start(), match.end())))

        if plain.strip() and not NON_PROSE.match(plain.lstrip()):
            offset = MARKUP.match(plain).end()
            boundaries.append((number, line, plain[offset:], offset))

    if boundaries:
        for boundary, pattern in ((boundaries[0], CHATBOT_START), (boundaries[-1], CHATBOT_END)):
            number, line, prose, offset = boundary
            match = pattern.search(prose)
            if match:
                hits.append((number, "chatbot", fragment(line, offset + match.start(), offset + match.end())))

    return sorted(hits)


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ascii-punctuation", action="store_true", help="also check dashes and quotes")
    parser.add_argument("file", nargs="?", help="path to a UTF-8 draft, or omit to read stdin")
    args = parser.parse_args(argv[1:])
    if args.file is None:
        text = sys.stdin.read()
    else:
        with open(args.file, encoding="utf-8") as file:
            text = file.read()

    hits = lint(text, ascii_punctuation=args.ascii_punctuation)
    for number, rule, snippet in hits:
        print(f"{number}: {rule}: {snippet}")
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
