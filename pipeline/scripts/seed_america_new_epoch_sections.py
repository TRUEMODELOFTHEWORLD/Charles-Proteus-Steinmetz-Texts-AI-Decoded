#!/usr/bin/env python3
"""Create chapter records and source-specific seed terms for America and the New Epoch."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path


SOURCE_ID = "america-and-new-epoch"

CHAPTER_PATTERNS = [
    ("I", "Eras in the World's History", r"ERAS\s+IN\s+THE\s+WORLD"),
    ("II", "The Epoch of the French Revolution", r"EPOCH\s+OF\s+THE\s+FRENCH\s+REVOLUTION"),
    ("III", "The Individualistic Era: From Competition to Co-operation", r"FROM\s+COMPETITION\s+TO\s+CO-OPERATION"),
    ("IV", "The Individualistic Era: The Other Side", r"THE\s+INDIVIDUALISTIC\s+ERA.?\s+THE\s+OTHER\s+SIDE"),
    ("V", "England in the Individualistic Era", r"ENGLAND\s+IN\s+THE\s+INDIVIDUALISTIC\s+ERA"),
    ("VI", "Germany in the Individualistic Era", r"GERMANY\s+IN\s+THE\s+INDIVIDUALISTIC\s+ERA"),
    ("VII", "The Other European Nations in the Individualistic Era", r"OTHER\s+EUROPEAN\s+NATIONS"),
    ("VIII", "America in the Past", r"AMERICA\s+IN\s+THE\s+PAST"),
    ("IX", "America in the Individualistic Era", r"AMERICA\s+IN\s+THE\s+INDIVIDUALISTIC\s+ERA"),
    ("X", "Public and Private Corporations", r"PUBLIC\s+AND\s+PRIVATE\s+CORPORATIONS"),
    ("XI", "Democracy and Monarchy", r"DEMOCRACY\s+AND\s+MONARCHY"),
    ("XII", "Evolution: Political Government", r"EVOLUTION.?\s+POLITICAL\s+GOVERNMENT"),
    ("XIII", "Evolution: Industrial Government", r"EVOLUTION.?\s+INDUSTRIAL\s+GOVERNMENT"),
    ("XIV", "Evolution: Inhibitory Power", r"EVOLUTION.?\s+INHIBITORY\s+POWER"),
    ("XV", "The American Nation", r"THE\s+AMERICAN\s+NATION"),
    ("XVI", "The Future Corporation", r"THE\s+FUTURE\s+CORPORATION"),
    ("XVII", "Conclusion", r"CONCLUSION"),
]

CONCEPT_SEEDS = [
    ("individualistic-era", "Individualistic era"),
    ("industrial-capitalism", "Industrial capitalism"),
    ("co-operation", "Co-operation"),
    ("competition", "Competition"),
    ("corporation", "Corporation"),
    ("public-corporation", "Public corporation"),
    ("private-corporation", "Private corporation"),
    ("democracy", "Democracy"),
    ("monarchy", "Monarchy"),
    ("industrial-government", "Industrial government"),
    ("political-government", "Political government"),
    ("inhibitory-power", "Inhibitory power"),
    ("social-democracy", "Social Democracy"),
    ("world-war", "World war"),
]

GLOSSARY_SEEDS = [
    ("individualistic era", "Steinmetz's historical term for the competitive industrial age."),
    ("industrial capitalism", "Industrial production organized through private capital and competition."),
    ("co-operation", "Coordinated industrial organization; spelling follows the source when present."),
    ("public corporation", "A municipality, state, nation, or public body treated as a corporate actor."),
    ("private corporation", "A privately owned industrial corporation."),
    ("industrial government", "Steinmetz's proposed administrative structure for industrial coordination."),
    ("political government", "The civic/governmental structure contrasted with industrial administration."),
    ("inhibitory power", "A supervisory or checking power rather than a direct executive power."),
    ("Social Democracy", "The socialist political movement discussed in Steinmetz's historical account."),
]


@dataclass
class Heading:
    roman: str | None
    number: int | None
    title: str
    line_index: int
    kind: str


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def count_occurrences(text: str, term: str) -> int:
    words = term.split()
    if len(words) > 1:
        pattern = r"\b" + r"\W+".join(re.escape(word) for word in words) + r"\b"
        return len(re.findall(pattern, text, flags=re.I))
    return len(re.findall(r"\b" + re.escape(term) + r"\b", text, flags=re.I))


def find_heading_line(lines: list[str], pattern: str, start: int) -> int:
    regex = re.compile(pattern, re.I)
    for index in range(start, len(lines)):
        line = normalize(lines[index])
        if not line:
            continue
        if regex.search(line):
            return index
    return -1


def include_previous_roman(lines: list[str], index: int, roman: str) -> int:
    for lookback in range(index - 1, max(-1, index - 6), -1):
        line = normalize(lines[lookback]).upper().replace("ILL", "III")
        if not line:
            continue
        if line == roman:
            return lookback
        if len(line) > 20:
            break
    return index


def find_headings(lines: list[str]) -> list[Heading]:
    introduction = find_heading_line(lines, r"^INTRODUCTION$", 0)
    if introduction < 0:
        raise SystemExit("Could not locate Introduction.")

    headings = [Heading(None, None, "Introduction", introduction, "introduction")]
    search_start = introduction + 1
    for number, (roman, title, pattern) in enumerate(CHAPTER_PATTERNS, start=1):
        title_line = find_heading_line(lines, pattern, search_start)
        if title_line < 0:
            raise SystemExit(f"Could not locate chapter {roman}: {title}")
        start_line = include_previous_roman(lines, title_line, roman)
        headings.append(Heading(roman, number, title, start_line, "chapter"))
        search_start = title_line + 1
    return headings


def concept_tags_for(title: str) -> list[str]:
    lower = title.lower()
    tags = []
    for tag, needles in {
        "historical-context": ["era", "epoch", "history", "past", "war"],
        "industrial-organization": ["corporation", "industrial", "competition", "co-operation"],
        "political-theory": ["democracy", "monarchy", "government", "nation", "inhibitory"],
        "steinmetz-biographical-context": ["america", "germany", "england", "european"],
    }.items():
        if any(needle in lower for needle in needles):
            tags.append(tag)
    return tags


def build_concepts(text: str) -> list[dict[str, object]]:
    return [
        {
            "id": concept_id,
            "label": label,
            "source_id": SOURCE_ID,
            "occurrence_count_in_ocr": count_occurrences(text, label),
            "steinmetz_usage": "",
            "modern_equivalent": "",
            "interpretive_reading": "",
            "related": [],
            "status": "seeded-source-specific",
        }
        for concept_id, label in CONCEPT_SEEDS
    ]


def build_glossary(text: str) -> list[dict[str, object]]:
    return [
        {
            "term": term,
            "source_id": SOURCE_ID,
            "modern_equivalent": note,
            "occurrence_count_in_ocr": count_occurrences(text, term),
            "steinmetz_usage": "",
            "mathematical_meaning": "",
            "conceptual_meaning": "",
            "source_refs": [],
            "status": "seeded-source-specific",
        }
        for term, note in GLOSSARY_SEEDS
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--ocr",
        type=Path,
        default=Path("processed") / SOURCE_ID / "cleaned_text" / "internet-archive-ocr.txt",
    )
    parser.add_argument("--out", type=Path, default=Path("processed") / SOURCE_ID)
    args = parser.parse_args()

    text = args.ocr.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")
    lines = text.splitlines()
    headings = find_headings(lines)
    body_end = len(lines)

    cleaned_dir = args.out / "cleaned_text"
    chapter_records = []
    for sequence, heading in enumerate(headings, start=1):
        end = headings[sequence].line_index if sequence < len(headings) else body_end
        path = cleaned_dir / f"{heading.kind}-{sequence:02d}.md"
        path.write_text("\n".join(lines[heading.line_index:end]).strip() + "\n", encoding="utf-8")
        chapter_records.append(
            {
                "id": f"{SOURCE_ID}-{heading.kind}-{sequence:02d}",
                "source_id": SOURCE_ID,
                "kind": heading.kind,
                "sequence": sequence,
                "number": heading.number,
                "roman": heading.roman,
                "title": heading.title,
                "line_start": heading.line_index + 1,
                "line_end": end,
                "text_path": str(path).replace("\\", "/"),
                "summary": "Candidate OCR chapter split; scan verification required before canonical citation.",
                "concept_tags": concept_tags_for(heading.title),
                "status": "candidate",
            }
        )

    write_json(args.out / "chapters.json", chapter_records)
    write_json(args.out / "concepts.json", build_concepts(text))
    write_json(args.out / "glossary.json", build_glossary(text))

    report = [
        "# Processing Report",
        "",
        f"Source ID: `{SOURCE_ID}`",
        f"OCR input: `{args.ocr}`",
        f"Structural headings found: {len(chapter_records)}",
        "",
        "## Status",
        "",
        "America and the New Epoch uses a source-specific historical chapter parser. Records are OCR-derived candidates and require scan verification before canonical citation.",
        "",
        "## Generated Files",
        "",
        "- `chapters.json`",
        "- `concepts.json`",
        "- `glossary.json`",
        "- `cleaned_text/introduction-01.md`",
        "- `cleaned_text/chapter-XX.md`",
        "",
    ]
    (args.out / "processing_report.md").write_text("\n".join(report), encoding="utf-8")
    print(f"Seeded {len(chapter_records)} chapters for {SOURCE_ID}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
