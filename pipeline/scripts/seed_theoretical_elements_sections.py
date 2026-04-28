#!/usr/bin/env python3
"""Create section records for Theoretical Elements of Electrical Engineering.

The book is not laid out as ordinary "Chapter I" headings. Part I uses
numbered theory sections, while Part II uses apparatus families and Roman
subsections. This source-specific splitter preserves that structure as review
candidates without claiming corrected OCR or verified pagination.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path


SOURCE_ID = "theoretical-elements-electrical-engineering"

APPARATUS_HEADINGS = {
    "SYNCHRONOUS MACHINES",
    "DIRECT-CURRENT COMMUTATING MACHINES",
    "SYNCHRONOUS CONVERTERS",
    "ALTERNATING-CURRENT TRANSFORMER",
    "INDUCTION MACHINES",
}

ROMAN_VALUES = {
    "I": 1,
    "II": 2,
    "III": 3,
    "IV": 4,
    "V": 5,
    "VI": 6,
    "VII": 7,
    "VIII": 8,
    "IX": 9,
    "X": 10,
    "XI": 11,
    "XII": 12,
    "XIII": 13,
    "XIV": 14,
    "XV": 15,
    "XVI": 16,
    "XVII": 17,
}


@dataclass
class SectionHeading:
    line_index: int
    title: str
    kind: str
    number: int | None = None
    roman: str | None = None
    part: str = ""
    apparatus: str = ""


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def normalize_spaces(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def title_case(value: str) -> str:
    small = {"and", "of", "the", "in", "on", "or", "to", "with", "as"}
    words = normalize_spaces(value).lower().split()
    titled: list[str] = []
    for index, word in enumerate(words):
        if index and word in small:
            titled.append(word)
        else:
            titled.append(word[:1].upper() + word[1:])
    return " ".join(titled)


def is_upper_heading_text(value: str) -> bool:
    letters = re.sub(r"[^A-Za-z]", "", value)
    if not letters:
        return False
    return letters.upper() == letters and len(letters) >= 4


def heading_continuation(lines: list[str], index: int) -> str:
    parts: list[str] = []
    for lookahead in range(index + 1, min(index + 4, len(lines))):
        candidate = normalize_spaces(lines[lookahead])
        if not candidate:
            continue
        if re.match(r"^[^A-Za-z]*\d+\.\s+", candidate):
            break
        if re.match(r"^(\d+|[IVXLCDM]+|[A-Z])\.\s+", candidate):
            break
        if re.match(r"^\d+\s+ELEMENTS\b|^[A-Z. ]+\s+\d+$", candidate):
            continue
        if is_upper_heading_text(candidate) and len(candidate) <= 80:
            parts.append(candidate)
            continue
        if re.match(r"^[A-Z][A-Za-z-]+(?:\s+[A-Z][A-Za-z-]+){0,2}$", candidate):
            parts.append(candidate)
            continue
        break
    return " ".join(parts)


def find_line(lines: list[str], pattern: str, start: int = 0) -> int:
    regex = re.compile(pattern, re.I)
    for index in range(start, len(lines)):
        if regex.match(normalize_spaces(lines[index])):
            return index
    return -1


def find_body_end(lines: list[str], start: int) -> int:
    for index in range(start, len(lines)):
        if re.match(r"^INDEX\.?$", normalize_spaces(lines[index]), re.I):
            return index
    return len(lines)


def concept_tags_for(title: str) -> list[str]:
    lower = title.lower()
    candidates = {
        "alternating-current": ["alternating", "synchronous", "phase"],
        "complex-quantities": ["rectangular", "vector", "symbolic"],
        "dielectricity": ["capacity", "condenser", "dielectric"],
        "fields": ["field", "force"],
        "hysteresis": ["hysteresis"],
        "impedance-reactance": ["impedance", "admittance", "reactance"],
        "magnetism": ["magnet", "flux", "inductance", "transformer", "armature"],
        "machines": ["machine", "motor", "generator", "converter", "apparatus"],
        "power": ["power", "efficiency", "loss"],
        "transmission-lines": ["transmission line"],
    }
    tags = []
    for tag, needles in candidates.items():
        if any(needle in lower for needle in needles):
            tags.append(tag)
    return tags


def find_headings(lines: list[str]) -> tuple[int, int, list[SectionHeading]]:
    part_i_start = find_line(lines, r"^1\.\s+MAGNETISM\s+AND\s+ELECTRIC\s+CURRENT$")
    if part_i_start < 0:
        raise SystemExit("Could not find Part I body start.")

    part_ii_start = find_line(lines, r"^PART\s+II$", part_i_start + 1)
    if part_ii_start < 0:
        raise SystemExit("Could not find Part II body start.")

    body_end = find_body_end(lines, part_ii_start)
    headings: list[SectionHeading] = []

    for index in range(part_i_start, part_ii_start):
        line = normalize_spaces(lines[index])
        match = re.match(r"^(?:[A-Za-z]\s+)?(\d{1,2})\.\s+(.+)$", line)
        if not match:
            continue
        number = int(match.group(1))
        if not 1 <= number <= 20:
            continue
        title = normalize_spaces(match.group(2) + " " + heading_continuation(lines, index))
        if not is_upper_heading_text(title):
            continue
        headings.append(
            SectionHeading(
                line_index=index,
                title=title_case(title),
                kind="theory-section",
                number=number,
                part="Part I - General Theory",
            )
        )

    current_apparatus = ""
    intro_index = find_line(lines, r"^INTRODUCTION\.?$", part_ii_start)
    if 0 <= intro_index < body_end:
        headings.append(
            SectionHeading(
                line_index=intro_index,
                title="Introduction",
                kind="apparatus-introduction",
                part="Part II - Special Apparatus",
            )
        )

    for index in range(part_ii_start, body_end):
        line = normalize_spaces(lines[index])
        letter_match = re.match(r"^([A-E])\.\s+(.+)$", line)
        if letter_match and is_upper_heading_text(letter_match.group(2)):
            candidate = normalize_spaces(letter_match.group(2) + " " + heading_continuation(lines, index))
            candidate_plain = normalize_spaces(candidate).upper().rstrip(".")
            if candidate_plain in APPARATUS_HEADINGS:
                current_apparatus = title_case(candidate)
                continue
            if current_apparatus:
                headings.append(
                    SectionHeading(
                        line_index=index,
                        title=f"{current_apparatus}: {title_case(candidate)}",
                        kind="apparatus-subsection",
                        part="Part II - Special Apparatus",
                        apparatus=current_apparatus,
                    )
                )
                continue

        roman_match = re.match(r"^([IVXLCDMNHivxlcdmnh]+)\.\s+(.+)$", line)
        if not roman_match or not current_apparatus:
            continue
        roman = roman_match.group(1).upper().replace("H", "II").replace("N", "II")
        if roman not in ROMAN_VALUES:
            continue
        title = normalize_spaces(roman_match.group(2) + " " + heading_continuation(lines, index))
        if not title:
            continue
        headings.append(
            SectionHeading(
                line_index=index,
                title=f"{current_apparatus}: {title_case(title)}",
                kind="apparatus-section",
                number=ROMAN_VALUES[roman],
                roman=roman,
                part="Part II - Special Apparatus",
                apparatus=current_apparatus,
            )
        )

    headings.sort(key=lambda heading: heading.line_index)
    deduped: list[SectionHeading] = []
    seen: set[int] = set()
    for heading in headings:
        if heading.line_index in seen:
            continue
        seen.add(heading.line_index)
        deduped.append(heading)
    return part_i_start, body_end, deduped


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
    body_start, body_end, headings = find_headings(lines)

    cleaned_dir = args.out / "cleaned_text"
    chapter_records: list[dict[str, object]] = []
    for sequence, heading in enumerate(headings, start=1):
        next_line = headings[sequence].line_index if sequence < len(headings) else body_end
        section_lines = lines[heading.line_index:next_line]
        text_path = cleaned_dir / f"section-{sequence:02d}.md"
        text_path.write_text("\n".join(section_lines).strip() + "\n", encoding="utf-8")
        chapter_records.append(
            {
                "id": f"{SOURCE_ID}-section-{sequence:02d}",
                "source_id": SOURCE_ID,
                "kind": heading.kind,
                "sequence": sequence,
                "number": heading.number,
                "roman": heading.roman,
                "title": heading.title,
                "part": heading.part,
                "apparatus": heading.apparatus,
                "line_start": heading.line_index + 1,
                "line_end": next_line,
                "text_path": str(text_path).replace("\\", "/"),
                "summary": "Candidate section split generated from OCR body headings; scan verification required.",
                "concept_tags": concept_tags_for(heading.title),
                "status": "candidate",
            }
        )

    write_json(args.out / "chapters.json", chapter_records)
    report = [
        "# Processing Report",
        "",
        f"Source ID: `{SOURCE_ID}`",
        f"OCR input: `{args.ocr}`",
        f"Body start line: {body_start + 1}",
        f"Body end line: {body_end}",
        f"Structural headings found: {len(chapter_records)}",
        "",
        "## Status",
        "",
        "Theoretical Elements uses a source-specific section parser. Records are OCR-derived candidates and require scan verification before canonical citation.",
        "",
        "## Generated Files",
        "",
        "- `chapters.json`",
        "- `cleaned_text/section-XX.md`",
        "",
    ]
    (args.out / "processing_report.md").write_text("\n".join(report), encoding="utf-8")
    print(f"Seeded {len(chapter_records)} sections for {SOURCE_ID}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
