#!/usr/bin/env python3
"""Seed structured records for Steinmetz's Commonwealth Edison report.

The report is not a textbook chapter sequence. It contains a cover letter,
recommendations, a discussion, an event record, and a mathematical appendix.
This source-specific parser preserves that engineering structure and labels all
outputs as PDF-text-derived candidates pending scan verification.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


SOURCE_ID = "commonwealth-edison-generating-system-trouble"
SOURCE_TITLE = "Investigation of Some Trouble in the Generating System of the Commonwealth Edison Co."


@dataclass
class Section:
    slug: str
    title: str
    kind: str
    line_start: int
    line_end: int
    summary: str
    concept_tags: list[str]


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def normalize_spaces(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def count_term(text: str, term: str) -> int:
    pattern = r"\b" + r"\s+".join(re.escape(part) for part in term.split()) + r"\b"
    return len(re.findall(pattern, text, flags=re.I))


def find_line(lines: list[str], pattern: str, start: int = 1) -> int:
    regex = re.compile(pattern, re.I)
    for index in range(start - 1, len(lines)):
        if regex.match(normalize_spaces(lines[index])):
            return index + 1
    raise SystemExit(f"Could not find line matching {pattern!r}")


def build_page_lookup(lines: list[str]) -> dict[int, int]:
    lookup: dict[int, int] = {}
    current_page = 0
    page_re = re.compile(r"^\[\[PDF_PAGE:(\d+)\]\]$")
    for index, line in enumerate(lines, start=1):
        match = page_re.match(line.strip())
        if match:
            current_page = int(match.group(1))
        lookup[index] = current_page
    return lookup


def page_for(line_number: int, page_lookup: dict[int, int]) -> int | None:
    return page_lookup.get(line_number) or None


def source_ref(line_start: int, line_end: int, page_lookup: dict[int, int]) -> dict[str, Any]:
    return {
        "source_id": SOURCE_ID,
        "line_start": line_start,
        "line_end": line_end,
        "pdf_page_start": page_for(line_start, page_lookup),
        "pdf_page_end": page_for(line_end, page_lookup),
        "verification": "pdf-text-extracted-needs-scan-verification",
    }


def first_match_ref(lines: list[str], terms: list[str], page_lookup: dict[int, int]) -> dict[str, Any]:
    patterns = [
        re.compile(r"\b" + r"\s+".join(re.escape(part) for part in term.split()) + r"\b", re.I)
        for term in terms
    ]
    for index in range(len(lines)):
        window = normalize_spaces(" ".join(lines[index:index + 4]))
        if any(pattern.search(window) for pattern in patterns):
            return source_ref(index + 1, min(index + 4, len(lines)), page_lookup)
    return {}


def section_text(lines: list[str], line_start: int, line_end: int) -> str:
    return "\n".join(lines[line_start - 1:line_end]).strip() + "\n"


def find_sections(lines: list[str]) -> list[Section]:
    recommendations = find_line(lines, r"^RECOMMENDATIONS$")
    discussion = find_line(lines, r"^Discussion$")
    record = find_line(lines, r"^RECORD$")
    appendix = find_line(lines, r"^APPENDIX$", record + 1)
    end = len(lines)

    return [
        Section(
            slug="front-letter-01",
            title="Cover Letter to Samuel Insull",
            kind="front-matter",
            line_start=1,
            line_end=recommendations - 1,
            summary=(
                "Steinmetz introduces the investigation, notes limits in his familiarity with the "
                "expanded system, recommends study of power-limiting reactors and substation "
                "interference, and proposes a scaled operating model for experimental disturbance study."
            ),
            concept_tags=["engineering-method", "power-limiting-reactor", "system-model", "substation-interference"],
        ),
        Section(
            slug="section-01-recommendations",
            title="Recommendations",
            kind="report-section",
            line_start=recommendations,
            line_end=discussion - 1,
            summary=(
                "A practical protection program: inspect relays, current transformers, breaker mechanisms, "
                "substation feeder arrangements, differential relay schemes, feeder reactances, and station "
                "power-limiting reactors."
            ),
            concept_tags=[
                "protective-reactance",
                "power-limiting-reactor",
                "differential-relay",
                "circuit-breaker",
                "feeder-reactance",
            ],
        ),
        Section(
            slug="section-02-discussion-of-recommendations",
            title="Discussion of Recommendations",
            kind="report-section",
            line_start=discussion,
            line_end=record - 2,
            summary=(
                "Steinmetz identifies the severe symptom: after the short circuit cleared, major station "
                "sections did not promptly return to normal voltage because machines apparently drifted out "
                "of synchronism. He argues for local power limitation while preserving enough synchronizing power."
            ),
            concept_tags=[
                "short-circuit",
                "synchronism",
                "synchronizing-power",
                "power-limiting-reactor",
                "transient-stability",
            ],
        ),
        Section(
            slug="section-03-record",
            title="Record of Four Troubles",
            kind="report-record",
            line_start=record - 1,
            line_end=appendix - 1,
            summary=(
                "A dated engineering record of four 1919 system troubles, including short circuits, synchronous "
                "machine drop-outs, out-of-step operation, tie-cable behavior, reactor heating, and recovery sequence."
            ),
            concept_tags=[
                "event-record",
                "short-circuit",
                "synchronous-machines",
                "out-of-synchronism",
                "tie-cable",
                "hunting-pulsation",
            ],
        ),
        Section(
            slug="appendix-01-synchronous-operation",
            title="Appendix: Synchronous Operation",
            kind="mathematical-appendix",
            line_start=appendix,
            line_end=end,
            summary=(
                "Mathematical appendix on two alternators or station sections connected while displaced in "
                "phase or frequency. The extracted text includes candidate formulas for resultant voltage, "
                "interchange current, synchronizing power, energy transfer, and critical slip."
            ),
            concept_tags=[
                "synchronous-operation",
                "synchronizing-power",
                "phase-angle",
                "frequency-slip",
                "reactance",
                "impedance",
            ],
        ),
    ]


CONCEPTS = [
    {
        "id": "protective-reactance",
        "label": "Protective reactance",
        "terms": ["protective reactance", "protective reactances"],
        "steinmetz_usage": "A previously installed reactance layer that had improved operating safety before later system growth changed conditions.",
        "modern_equivalent": "Fault-current limiting and system-segmentation reactance used as part of protection coordination.",
        "related": ["power-limiting-reactor", "short-circuit", "protective-relaying"],
    },
    {
        "id": "power-limiting-reactor",
        "label": "Power limiting reactor",
        "terms": ["power limiting reactor", "power limiting reactors", "power limiting reactance"],
        "steinmetz_usage": "A reactor inserted between station sections or bus sections to limit local concentration of power during trouble.",
        "modern_equivalent": "Series reactor or fault-current-limiting reactor used to bound short-circuit contribution and separate system sections.",
        "related": ["reactance", "fault-current-limiting", "synchronizing-power"],
    },
    {
        "id": "synchronism",
        "label": "Synchronism",
        "terms": ["synchronism", "out of synchronism", "pull into synchronism", "in step"],
        "steinmetz_usage": "The condition of station sections or alternators remaining in step after a disturbance.",
        "modern_equivalent": "Synchronous stability and out-of-step operation of interconnected generators.",
        "related": ["synchronizing-power", "transient-stability", "frequency-slip"],
    },
    {
        "id": "synchronizing-power",
        "label": "Synchronizing power",
        "terms": ["synchronizing power"],
        "steinmetz_usage": "The power exchanged through the interconnection that tends to pull alternators or station sections back into step.",
        "modern_equivalent": "Synchronizing torque or power-angle restoring effect in synchronous-machine stability analysis.",
        "related": ["synchronism", "reactance", "phase-angle"],
    },
    {
        "id": "short-circuit",
        "label": "Short circuit",
        "terms": ["short circuit", "short-circuit"],
        "steinmetz_usage": "The initiating local fault that drops voltage, trips synchronous loads, and can push station sections out of step.",
        "modern_equivalent": "Fault event causing high current, voltage depression, protection operation, and transient stability stress.",
        "related": ["circuit-breaker", "protective-relaying", "transient-stability"],
    },
    {
        "id": "differential-relay",
        "label": "Differential relay",
        "terms": ["differential relay", "differential relays"],
        "steinmetz_usage": "A recommended method for detecting cable or feeder faults before a short circuit fully develops.",
        "modern_equivalent": "Current-differential protection comparing currents at protected-zone boundaries.",
        "related": ["protective-relaying", "current-transformer", "split-conductor-cable"],
    },
    {
        "id": "circuit-breaker",
        "label": "Circuit breaker",
        "terms": ["circuit breaker", "circuit breakers", "breaker"],
        "steinmetz_usage": "Switching apparatus that must clear a trouble rapidly enough for the system to return to normal operation.",
        "modern_equivalent": "Fault interruption apparatus coordinated with relays and current transformers.",
        "related": ["protective-relaying", "short-circuit"],
    },
    {
        "id": "current-transformer",
        "label": "Current transformer",
        "terms": ["current transformer", "current transformers"],
        "steinmetz_usage": "A protective-system device to be inspected for condition and reliability.",
        "modern_equivalent": "Instrument transformer feeding relay and metering circuits.",
        "related": ["protective-relaying", "differential-relay"],
    },
    {
        "id": "synchronous-machines",
        "label": "Synchronous machines",
        "terms": ["synchronous machine", "synchronous machines", "alternator", "alternators"],
        "steinmetz_usage": "Machines that may drop out, speed up, lose excitation, or fail to pull back into step during a system event.",
        "modern_equivalent": "Synchronous generators, motors, or converters participating in transient stability behavior.",
        "related": ["synchronism", "synchronizing-power", "governor-action"],
    },
    {
        "id": "tie-cable",
        "label": "Tie cable",
        "terms": ["tie cable", "tie cables"],
        "steinmetz_usage": "Interstation cables that also served feeder duty and therefore complicated placement of power-limiting reactors.",
        "modern_equivalent": "Interconnection or feeder cables whose protection and operating role must be coordinated.",
        "related": ["substation-interference", "feeder-cable", "power-limiting-reactor"],
    },
    {
        "id": "system-model",
        "label": "Scaled system model",
        "terms": ["model of your system", "operated by direct current", "experimentally investigated"],
        "steinmetz_usage": "A proposed small-scale model of the generating stations, cables, and substations for disturbance experiments.",
        "modern_equivalent": "Physical network analyzer or simulation model for studying operating contingencies.",
        "related": ["engineering-method", "disturbance-study"],
    },
    {
        "id": "hunting-pulsation",
        "label": "Hunting pulsation",
        "terms": ["hunting", "hunting pulsation"],
        "steinmetz_usage": "A possible oscillatory condition of machines or station sections after disturbance.",
        "modern_equivalent": "Electromechanical oscillation or power-system hunting.",
        "related": ["oscillation-damping", "synchronism", "transient-stability"],
    },
]


GLOSSARY = [
    ("power limiting reactor", "series reactor used to limit power/fault-current concentration between station sections"),
    ("power limiting reactance", "the reactance value supplied by a power-limiting reactor"),
    ("protective reactance", "reactance installed for protection and fault-current limitation"),
    ("feeder reactance", "series reactance in feeder circuits used to reduce local trouble propagation"),
    ("busbar reactance", "reactance dividing busbar or station sections"),
    ("differential relay", "relay scheme comparing currents to detect internal faults"),
    ("split conductor cable", "cable arrangement discussed for differential protection"),
    ("tie cable", "interstation cable also used as feeder path in the report"),
    ("synchronous apparatus", "synchronous machines connected to the alternating-current system"),
    ("hunting pulsation", "oscillatory power or speed fluctuation of synchronous machines"),
    ("synchronizing power", "restoring power tending to hold or pull synchronous machines into step"),
    ("critical slip", "frequency difference or slip at which pulling into synchronism becomes critical"),
]


QUOTE_CANDIDATES = [
    (
        "scaled-system-model",
        121,
        132,
        "Steinmetz proposes a reduced operating model of stations, cables, and substations for experimental disturbance study.",
        "This is a hidden gem because it shows Steinmetz thinking like a systems simulator before digital simulation existed.",
    ),
    (
        "out-of-synchronism-voltage-collapse",
        756,
        771,
        "The extracted text says the stations apparently broke out of synchronism and kept voltage practically at zero.",
        "This makes the report an early practical stability case study, not just a protection memorandum.",
    ),
    (
        "limit-local-power-concentration",
        772,
        786,
        "Steinmetz argues that very large power systems need power-limiting reactors to limit local power concentration.",
        "The statement connects fault-current limitation with system architecture and disturbance containment.",
    ),
    (
        "synchronizing-power-voltage-square",
        855,
        861,
        "The report states that lowered voltage also lowers synchronizing power, which varies with voltage squared.",
        "This is a concise bridge between short-circuit voltage depression and loss of synchronizing stability.",
    ),
    (
        "maximum-synchronizing-power-reactance",
        3562,
        3599,
        "The appendix states that synchronizing power can be maximized by a specific relation between external and machine reactance.",
        "This is the mathematical core of the report's reactor recommendation and needs scan-verified promotion.",
    ),
]


CURATED_EQUATIONS = [
    {
        "id": f"{SOURCE_ID}-eq-sync-emfs-0001",
        "original_form": "e1 = E cos(...); e2 = E cos(...), OCR candidate",
        "modern_form": "Two equal-voltage alternator EMFs displaced by a phase angle.",
        "variables": ["E: effective machine EMF", "phase angle: OCR damaged", "f: frequency"],
        "physical_meaning": "Represents two alternators or station sections that remain at the same frequency but differ in phase.",
        "line_start": 2211,
        "line_end": 2217,
    },
    {
        "id": f"{SOURCE_ID}-eq-resultant-voltage-0002",
        "original_form": "e = e1 - e2 = 2E sin(...) sin(...), OCR candidate",
        "modern_form": "Difference voltage between two equal alternating EMFs displaced in phase.",
        "variables": ["e: resultant interconnection voltage", "E: machine EMF", "phase displacement: OCR damaged"],
        "physical_meaning": "The out-of-phase connection creates the interchange voltage driving current through the interconnection impedance.",
        "line_start": 2218,
        "line_end": 2230,
    },
    {
        "id": f"{SOURCE_ID}-eq-interchange-current-0003",
        "original_form": "i = (2E / z) sin(...) sin(...), OCR candidate",
        "modern_form": "Interchange current equals resultant voltage over circuit impedance with phase shift.",
        "variables": ["i: interchange current", "z: impedance", "a: impedance phase angle"],
        "physical_meaning": "The current between alternators is set by phase displacement and by the impedance/reactance between station sections.",
        "line_start": 2231,
        "line_end": 2239,
    },
    {
        "id": f"{SOURCE_ID}-eq-impedance-angle-0004",
        "original_form": "z = sqrt(r^2 + x^2); tan a = x / r, OCR candidate",
        "modern_form": "Z = sqrt(R^2 + X^2), alpha = atan(X/R)",
        "variables": ["r or R: resistance", "x or X: reactance", "z or Z: impedance magnitude", "a or alpha: impedance angle"],
        "physical_meaning": "Defines the interconnection impedance controlling magnitude and phase of synchronizing current.",
        "line_start": 2240,
        "line_end": 2255,
    },
    {
        "id": f"{SOURCE_ID}-eq-frequency-slip-0005",
        "original_form": "one alternator frequency (1 - s)f, the other (1 + s)f, OCR candidate",
        "modern_form": "f1 = (1 - s) f; f2 = (1 + s) f",
        "variables": ["s: fractional frequency difference", "f: nominal frequency"],
        "physical_meaning": "Represents station sections slipping past each other in frequency rather than merely being out of phase.",
        "line_start": 2571,
        "line_end": 2591,
    },
    {
        "id": f"{SOURCE_ID}-eq-max-sync-power-condition-0006",
        "original_form": "x2 = 2x1 + x, OCR candidate",
        "modern_form": "Candidate maximum synchronizing-power condition involving machine and external reactance.",
        "variables": ["x: external circuit reactance", "x1/x2: OCR labels needing scan verification"],
        "physical_meaning": "Steinmetz uses a reactance relation to reason about maximum synchronizing power and pull-in behavior.",
        "line_start": 3557,
        "line_end": 3561,
    },
]


def build_concepts(text: str, lines: list[str], page_lookup: dict[int, int]) -> list[dict[str, Any]]:
    records = []
    for concept in CONCEPTS:
        terms = concept["terms"]
        occurrences = sum(count_term(text, term) for term in terms)
        records.append(
            {
                "id": concept["id"],
                "label": concept["label"],
                "source_id": SOURCE_ID,
                "occurrence_count_in_ocr": occurrences,
                "steinmetz_usage": concept["steinmetz_usage"],
                "modern_equivalent": concept["modern_equivalent"],
                "interpretive_reading": "",
                "related": concept["related"],
                "source_refs": [first_match_ref(lines, terms, page_lookup)] if first_match_ref(lines, terms, page_lookup) else [],
                "status": "pdf-text-extracted-candidate",
            }
        )
    return records


def build_glossary(text: str, lines: list[str], page_lookup: dict[int, int]) -> list[dict[str, Any]]:
    records = []
    for term, modern in GLOSSARY:
        ref = first_match_ref(lines, [term], page_lookup)
        records.append(
            {
                "term": term,
                "source_id": SOURCE_ID,
                "modern_equivalent": modern,
                "occurrence_count_in_ocr": count_term(text, term),
                "steinmetz_usage": "",
                "mathematical_meaning": "",
                "conceptual_meaning": modern,
                "source_refs": [ref] if ref else [],
                "status": "pdf-text-extracted-candidate",
            }
        )
    return records


def build_quotes(page_lookup: dict[int, int]) -> list[dict[str, Any]]:
    return [
        {
            "id": f"{SOURCE_ID}-quote-{slug}",
            "source_id": SOURCE_ID,
            "quote_candidate": candidate,
            "why_it_matters": why,
            "source_ref": source_ref(start, end, page_lookup),
            "status": "pdf-text-extracted-candidate",
        }
        for slug, start, end, candidate, why in QUOTE_CANDIDATES
    ]


def build_equations(lines: list[str], page_lookup: dict[int, int]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for item in CURATED_EQUATIONS:
        records.append(
            {
                "id": item["id"],
                "source_id": SOURCE_ID,
                "original_form": item["original_form"],
                "modern_form": item["modern_form"],
                "variables": item["variables"],
                "physical_meaning": item["physical_meaning"],
                "source_ref": source_ref(item["line_start"], item["line_end"], page_lookup),
                "status": "curated-pdf-text-candidate",
            }
        )

    equation_re = re.compile(r"(=|sin|cos|tan|sqrt|frequency|reactance|impedance|slip|\bohms?\b)", re.I)
    skip_re = re.compile(r"^\[\[|^Report of Charles P\. Steinmetz$|^\d+$", re.I)
    appendix_start = find_line(lines, r"^APPENDIX$", 2000)
    for index in range(appendix_start, len(lines) + 1):
        clean = normalize_spaces(lines[index - 1])
        if len(clean) < 8 or len(clean) > 180 or skip_re.search(clean):
            continue
        if not equation_re.search(clean):
            continue
        if sum(char.isdigit() for char in clean) == 0 and "=" not in clean:
            continue
        records.append(
            {
                "id": f"{SOURCE_ID}-eq-candidate-{len(records) + 1:04d}",
                "source_id": SOURCE_ID,
                "original_form": clean,
                "modern_form": "",
                "variables": [],
                "physical_meaning": "",
                "source_ref": source_ref(index, index, page_lookup),
                "status": "pdf-text-extracted-candidate",
            }
        )
    return records[:220]


def build_figures(page_lookup: dict[int, int]) -> list[dict[str, Any]]:
    return [
        {
            "id": f"{SOURCE_ID}-fig-001",
            "source_id": SOURCE_ID,
            "figure_number": 1,
            "caption": "Appendix Figure 1, candidate reference for synchronous-operation current and voltage curves.",
            "source_ref": source_ref(2560, 2570, page_lookup),
            "linked_concepts": ["synchronism", "synchronizing-power", "frequency-slip", "phase-angle"],
            "status": "pdf-text-extracted-candidate",
        }
    ]


def build_annotations(sections: list[Section], page_lookup: dict[int, int]) -> list[dict[str, Any]]:
    return [
        {
            "id": f"{SOURCE_ID}-annotation-{section.slug}",
            "source_id": SOURCE_ID,
            "target_type": "section",
            "target_id": f"{SOURCE_ID}-{section.slug}",
            "annotation_type": "processing-note",
            "note": section.summary,
            "source_ref": source_ref(section.line_start, section.line_end, page_lookup),
            "status": "pdf-text-extracted-candidate",
        }
        for section in sections
    ]


def build_crosslinks() -> list[dict[str, Any]]:
    links = []
    for concept in CONCEPTS:
        links.append(
            {
                "source_id": SOURCE_ID,
                "from_type": "source",
                "from_id": SOURCE_ID,
                "to_type": "concept",
                "to_id": concept["id"],
                "reason": f"{concept['label']} appears in the Commonwealth Edison report intake.",
                "status": "candidate",
            }
        )
    return links


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--text",
        type=Path,
        default=Path("processed") / SOURCE_ID / "cleaned_text" / "pdf-extracted-text.txt",
    )
    parser.add_argument("--out", type=Path, default=Path("processed") / SOURCE_ID)
    args = parser.parse_args()

    text = args.text.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")
    lines = text.splitlines()
    page_lookup = build_page_lookup(lines)
    sections = find_sections(lines)
    cleaned_dir = args.out / "cleaned_text"
    cleaned_dir.mkdir(parents=True, exist_ok=True)

    chapter_records = []
    for sequence, section in enumerate(sections, start=1):
        text_path = cleaned_dir / f"{section.slug}.md"
        text_path.write_text(section_text(lines, section.line_start, section.line_end), encoding="utf-8")
        chapter_records.append(
            {
                "id": f"{SOURCE_ID}-{section.slug}",
                "source_id": SOURCE_ID,
                "kind": section.kind,
                "sequence": sequence,
                "number": sequence,
                "roman": None,
                "title": section.title,
                "line_start": section.line_start,
                "line_end": section.line_end,
                "pdf_page_start": page_for(section.line_start, page_lookup),
                "pdf_page_end": page_for(section.line_end, page_lookup),
                "text_path": str(text_path).replace("\\", "/"),
                "summary": section.summary,
                "concept_tags": section.concept_tags,
                "status": "pdf-text-extracted-candidate",
            }
        )

    write_json(args.out / "chapters.json", chapter_records)
    write_json(args.out / "concepts.json", build_concepts(text, lines, page_lookup))
    write_json(args.out / "glossary.json", build_glossary(text, lines, page_lookup))
    write_json(args.out / "quotes.json", build_quotes(page_lookup))
    write_json(args.out / "equations.json", build_equations(lines, page_lookup))
    write_json(args.out / "figures.json", build_figures(page_lookup))
    write_json(args.out / "annotations.json", build_annotations(sections, page_lookup))
    write_json(args.out / "crosslinks.json", build_crosslinks())

    report = [
        "# Processing Report",
        "",
        f"Source ID: `{SOURCE_ID}`",
        f"Source title: `{SOURCE_TITLE}`",
        f"Input text: `{args.text}`",
        "",
        "## Status",
        "",
        "This pass uses embedded PDF text extracted by `extract_pdf_text.py`. It is not corrected OCR and it is not a reviewed transcription. All source claims, equations, and figure records remain candidates until checked against page images.",
        "",
        "## Structural Records",
        "",
        f"- Sections generated: {len(chapter_records)}",
        f"- Concept candidates: {len(CONCEPTS)}",
        f"- Glossary candidates: {len(GLOSSARY)}",
        f"- Curated equation clusters plus appendix equation candidates: {len(build_equations(lines, page_lookup))}",
        "- Figure candidates: 1",
        "",
        "## Generated Files",
        "",
        "- `chapters.json`",
        "- `concepts.json`",
        "- `glossary.json`",
        "- `quotes.json`",
        "- `equations.json`",
        "- `figures.json`",
        "- `annotations.json`",
        "- `crosslinks.json`",
        "- `cleaned_text/front-letter-01.md`",
        "- `cleaned_text/section-01-recommendations.md`",
        "- `cleaned_text/section-02-discussion-of-recommendations.md`",
        "- `cleaned_text/section-03-record.md`",
        "- `cleaned_text/appendix-01-synchronous-operation.md`",
        "",
    ]
    (args.out / "processing_report.md").write_text("\n".join(report), encoding="utf-8")
    print(f"Seeded {len(chapter_records)} Commonwealth Edison report sections")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
