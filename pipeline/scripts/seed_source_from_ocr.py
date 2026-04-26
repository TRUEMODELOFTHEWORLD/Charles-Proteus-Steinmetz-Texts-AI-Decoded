#!/usr/bin/env python3
"""Seed processed catalogs from an OCR text file.

This script is deliberately conservative. It creates candidates for review; it
does not claim canonical correctness for OCR text, equations, page numbers, or
figure captions.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


LECTURE_ROMANS = {
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
}


def parse_roman(value: str) -> int | None:
    if value in LECTURE_ROMANS:
        return LECTURE_ROMANS[value]
    numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    previous = 0
    for char in reversed(value):
        current = numerals.get(char)
        if current is None:
            return None
        if current < previous:
            total -= current
        else:
            total += current
            previous = current
    return total if total > 0 else None


SEED_CONCEPTS = [
    ("radiation", "Radiation"),
    ("light", "Light"),
    ("illumination", "Illumination"),
    ("electric-waves", "Electric waves"),
    ("ether", "Ether"),
    ("wave-length", "Wave length"),
    ("frequency", "Frequency"),
    ("velocity-of-light", "Velocity of light"),
    ("refraction", "Refraction"),
    ("refractive-index", "Refractive index"),
    ("permeability", "Magnetic permeability"),
    ("dielectric-constant", "Dielectric constant"),
    ("spectrum", "Spectrum"),
    ("ultraviolet", "Ultra-violet radiation"),
    ("ultrared", "Ultra-red radiation"),
    ("luminescence", "Luminescence"),
    ("arc-lamp", "Arc lamp"),
    ("photometry", "Photometry"),
    ("brilliancy", "Brilliancy"),
    ("light-flux-density", "Light flux density"),
]


SEED_GLOSSARY = [
    ("ultra-red", "infrared"),
    ("ultra-violet", "ultraviolet"),
    ("wave length", "wavelength"),
    ("electric waves", "radio-frequency electromagnetic waves, broadly construed"),
    ("brilliancy", "luminance or perceived brightness, depending on context"),
    ("candle-power", "luminous intensity in candlepower, historically"),
    ("flux of light", "luminous flux"),
    ("light flux density", "illuminance"),
    ("radiant heat", "thermal radiation; Steinmetz criticizes the phrase as misleading"),
    ("ether", "historical luminiferous ether or field-bearing medium, context-dependent"),
    ("specific high frequency effect", "biological or chemical effect associated with shorter wavelengths"),
    ("mechanical equivalent of light", "energy-to-light conversion measure in historical photometry"),
]


@dataclass
class Heading:
    roman: str
    number: int
    title: str
    line_index: int
    kind: str = "lecture"


def normalize_ocr(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\ufeff", "")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip() + "\n"


def line_is_probable_body_start(line: str) -> bool:
    return bool(re.search(r"^RADIATION,\s+LIGHT,\s+AND", line, re.I))


def find_body_start(lines: list[str]) -> int:
    """Find the main text start, skipping front matter and contents."""
    candidates = [i for i, line in enumerate(lines) if line_is_probable_body_start(line.strip())]
    for index in reversed(candidates):
        window = "\n".join(lines[index:index + 10])
        if re.search(r"LECTURE\s+I\.", window, re.I):
            return index
    lecture_i = [
        i for i, line in enumerate(lines)
        if re.match(r"^\s*LECTURE\s+I\.?\b", line, re.I)
    ]
    if len(lecture_i) >= 2:
        return lecture_i[1]
    if lecture_i:
        return lecture_i[0]
    chapter_i = [
        i for i, line in enumerate(lines)
        if re.match(r"^\s*CHAPTER\s+I\.?\b", line, re.I)
    ]
    if len(chapter_i) >= 2:
        return chapter_i[1]
    if chapter_i:
        return chapter_i[0]
    return 0


def find_body_end(lines: list[str], body_start: int) -> int:
    """Find the end of the main text before the back-of-book index."""
    for index in range(body_start, len(lines)):
        if re.match(r"^\s*INDEX\.\s*$", lines[index], re.I):
            return index
    return len(lines)


def clean_heading_title(value: str) -> str:
    value = re.sub(r"\s+", " ", value)
    value = value.strip(" .:-")
    value = value.replace("Hi.", "III.")
    return value.title()


def extract_headings(lines: list[str], body_start: int) -> list[Heading]:
    headings: list[Heading] = []
    heading_re = re.compile(r"^(LECTURE|CHAPTER)\s+([IVXLCDMH]+)\.?\s*(.*)$")
    for index in range(body_start, len(lines)):
        line = lines[index].strip()
        match = heading_re.match(line)
        if not match:
            continue
        kind = match.group(1).lower()
        roman = match.group(2).upper().replace("H", "II")
        parsed = parse_roman(roman)
        if parsed is None:
            continue
        title_parts: list[str] = []
        inline_title = clean_heading_title(match.group(3))
        if inline_title and not re.match(r"^\d+$", inline_title):
            title_parts.append(inline_title)
        for lookahead in range(index + 1, min(index + 6, len(lines))):
            candidate = lines[lookahead].strip(" .")
            if not candidate:
                if title_parts:
                    break
                continue
            if re.match(r"^\d+\.", candidate):
                break
            if len(candidate) <= 90:
                title_parts.append(clean_heading_title(candidate))
        title = " ".join(title_parts) or f"{kind.title()} {roman}"
        title = re.sub(r"\s+", " ", title).strip()
        headings.append(
            Heading(
                roman=roman,
                number=parsed,
                title=title,
                line_index=index,
                kind=kind,
            )
        )
    deduped: list[Heading] = []
    seen: set[int] = set()
    for heading in headings:
        if heading.line_index in seen:
            continue
        seen.add(heading.line_index)
        deduped.append(heading)
    return deduped


def slug_source_chapter(source_id: str, kind: str, sequence: int) -> str:
    return f"{source_id}-{kind}-{sequence:02d}"


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def iter_windows(lines: list[str], center: int, radius: int = 2) -> Iterable[str]:
    for index in range(max(0, center - radius), min(len(lines), center + radius + 1)):
        yield lines[index].strip()


def extract_figures(
    lines: list[str],
    source_id: str,
    start_index: int = 0,
    end_index: int | None = None,
) -> list[dict]:
    figures: list[dict] = []
    seen: set[int] = set()
    end_index = len(lines) if end_index is None else end_index
    for index in range(start_index, end_index):
        line = lines[index]
        match = re.search(r"^\s*FIG\.\s*(\d+)\.?\s*$", line, re.I)
        if not match:
            continue
        number = match.group(1)
        if int(number) in seen:
            continue
        seen.add(int(number))
        nearby = " ".join(part for part in iter_windows(lines, index, 3) if part)
        figures.append(
            {
                "id": f"{source_id}-fig-{int(number):03d}",
                "source_id": source_id,
                "figure_number": int(number),
                "caption": nearby[:500],
                "source_ref": {
                    "source_id": source_id,
                    "line_start": index + 1,
                    "line_end": index + 1,
                    "verification": "needs-verification"
                },
                "linked_concepts": [],
                "status": "candidate"
            }
        )
    return figures


def extract_equation_candidates(
    lines: list[str],
    source_id: str,
    start_index: int = 0,
    end_index: int | None = None,
) -> list[dict]:
    equations: list[dict] = []
    equation_re = re.compile(
        r"(=|sin|cos|tan|log|sqrt|X\s*10|10\^|10~|\([0-9]+\)\s*$|sec\.|cm\.)",
        re.I,
    )
    skip_re = re.compile(r"^(FIG\.|LECTURE|CONTENTS|PAGE)\b", re.I)
    end_index = len(lines) if end_index is None else end_index
    for index in range(start_index, end_index):
        line = lines[index]
        clean = line.strip()
        if len(clean) < 8 or len(clean) > 220 or skip_re.search(clean):
            continue
        if not equation_re.search(clean):
            continue
        if sum(ch.isdigit() for ch in clean) < 1:
            continue
        equations.append(
            {
                "id": f"{source_id}-eq-candidate-{len(equations) + 1:04d}",
                "source_id": source_id,
                "original_form": clean,
                "modern_form": "",
                "variables": [],
                "physical_meaning": "",
                "source_ref": {
                    "source_id": source_id,
                    "line_start": index + 1,
                    "line_end": index + 1,
                    "verification": "needs-verification"
                },
                "status": "candidate"
            }
        )
    return equations[:300]


def count_term_occurrences(text: str, term: str) -> int:
    return len(re.findall(r"\b" + re.escape(term) + r"\b", text, flags=re.I))


def build_concepts(text: str, source_id: str) -> list[dict]:
    concepts: list[dict] = []
    for concept_id, label in SEED_CONCEPTS:
        occurrences = count_term_occurrences(text, label.replace("-", " "))
        if occurrences == 0:
            occurrences = count_term_occurrences(text, label)
        concepts.append(
            {
                "id": concept_id,
                "label": label,
                "source_id": source_id,
                "occurrence_count_in_ocr": occurrences,
                "steinmetz_usage": "",
                "modern_equivalent": "",
                "interpretive_reading": "",
                "related": [],
                "status": "seeded"
            }
        )
    return concepts


def build_glossary(text: str, source_id: str) -> list[dict]:
    return [
        {
            "term": term,
            "source_id": source_id,
            "modern_equivalent": modern,
            "occurrence_count_in_ocr": count_term_occurrences(text, term),
            "steinmetz_usage": "",
            "mathematical_meaning": "",
            "conceptual_meaning": "",
            "source_refs": [],
            "status": "seeded"
        }
        for term, modern in SEED_GLOSSARY
    ]


def extract_quote_candidates(
    lines: list[str],
    source_id: str,
    start_index: int = 0,
    end_index: int | None = None,
) -> list[dict]:
    patterns = [
        ("radiation-not-heat", r"radiant heat.*not heat|heat radiation.*wrong"),
        ("ether-seat-of-energy", r"ether.*seat of energy|seat of energy.*ether"),
        ("electric-waves-and-light", r"electric waves.*light waves|light waves.*electric waves"),
        ("light-not-vector", r"light not a vector quantity"),
        ("physiological-quantity", r"physiological quantity"),
    ]
    quotes: list[dict] = []
    end_index = len(lines) if end_index is None else end_index
    for index in range(start_index, end_index):
        line = lines[index]
        clean = line.strip()
        for slug, pattern in patterns:
            if re.search(pattern, clean, re.I):
                quotes.append(
                    {
                        "id": f"{source_id}-quote-{slug}-{index + 1}",
                        "source_id": source_id,
                        "quote_candidate": clean,
                        "why_it_matters": "",
                        "source_ref": {
                            "source_id": source_id,
                            "line_start": index + 1,
                            "line_end": index + 1,
                            "verification": "needs-verification"
                        },
                        "status": "candidate"
                    }
                )
    return quotes


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-id", required=True)
    parser.add_argument("--ocr", required=True, type=Path)
    parser.add_argument("--out", default="processed", type=Path)
    args = parser.parse_args()

    source_id = args.source_id
    out_dir = args.out / source_id
    text = normalize_ocr(args.ocr.read_text(encoding="utf-8", errors="replace"))
    lines = text.splitlines()
    body_start = find_body_start(lines)
    headings = extract_headings(lines, body_start)
    body_end = find_body_end(lines, headings[-1].line_index if headings else body_start)

    chapter_records: list[dict] = []
    cleaned_dir = out_dir / "cleaned_text"
    for i, heading in enumerate(headings):
        end = headings[i + 1].line_index if i + 1 < len(headings) else body_end
        chapter_lines = lines[heading.line_index:end]
        sequence = i + 1
        chapter_id = slug_source_chapter(source_id, heading.kind, sequence)
        chapter_path = cleaned_dir / f"{heading.kind}-{sequence:02d}.md"
        chapter_path.write_text("\n".join(chapter_lines).strip() + "\n", encoding="utf-8")
        chapter_records.append(
            {
                "id": chapter_id,
                "source_id": source_id,
                "kind": heading.kind,
                "sequence": sequence,
                "number": heading.number,
                "roman": heading.roman,
                "title": heading.title,
                "line_start": heading.line_index + 1,
                "line_end": end,
                "text_path": str(chapter_path).replace("\\", "/"),
                "summary": "",
                "concept_tags": [],
                "status": "candidate"
            }
        )

    write_json(out_dir / "chapters.json", chapter_records)
    write_json(out_dir / "figures.json", extract_figures(lines, source_id, body_start, body_end))
    write_json(out_dir / "equations.json", extract_equation_candidates(lines, source_id, body_start, body_end))
    write_json(out_dir / "concepts.json", build_concepts(text, source_id))
    write_json(out_dir / "glossary.json", build_glossary(text, source_id))
    write_json(out_dir / "quotes.json", extract_quote_candidates(lines, source_id, body_start, body_end))
    write_json(out_dir / "annotations.json", [])
    write_json(out_dir / "crosslinks.json", [])

    report = [
        "# Processing Report",
        "",
        f"Source ID: `{source_id}`",
        f"OCR input: `{args.ocr}`",
        f"Body start line: {body_start + 1}",
        f"Body end line: {body_end}",
        f"Structural headings found: {len(headings)}",
        "",
        "## Status",
        "",
        "All generated records are candidates or seeded terms. They require scan verification before canonical use.",
        "",
        "## Generated Files",
        "",
        "- `chapters.json`",
        "- `figures.json`",
        "- `equations.json`",
        "- `concepts.json`",
        "- `glossary.json`",
        "- `quotes.json`",
        "- `annotations.json`",
        "- `crosslinks.json`",
        "- `cleaned_text/<kind>-XX.md`",
        "",
    ]
    (out_dir / "processing_report.md").write_text("\n".join(report), encoding="utf-8")
    print(f"Seeded {len(chapter_records)} chapters for {source_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
