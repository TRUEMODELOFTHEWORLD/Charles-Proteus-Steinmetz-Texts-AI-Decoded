#!/usr/bin/env python3
"""Build cross-source research indexes from processed Steinmetz records.

This script is intentionally descriptive, not interpretive. It inventories the
processed JSON records and promoted diagram crops so the archive can expose what
has been ingested, what remains candidate material, and what has been promoted
after scan review.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


CATALOG_FILES = {
    "chapters": "chapters.json",
    "concepts": "concepts.json",
    "equations": "equations.json",
    "figures": "figures.json",
    "glossary": "glossary.json",
    "quotes": "quotes.json",
    "annotations": "annotations.json",
    "crosslinks": "crosslinks.json",
}

THEME_PATTERNS = {
    "alternating-current": ["alternating current", "alternating-current", "a.c.", " ac "],
    "complex-quantities": ["complex quantity", "complex quantities", "symbolic", "imaginary", " j "],
    "dielectricity": ["dielectric", "capacity", "electrostatic", "condenser", "displacement"],
    "ether": ["ether", "aether"],
    "fields": ["field", "magnetic field", "electric field", "electrostatic field"],
    "hysteresis": ["hysteresis", "magnetic lag", "molecular friction"],
    "impedance-reactance": ["impedance", "reactance", "admittance", "conductance", "susceptance"],
    "lightning-surges": ["lightning", "surge", "impulse", "arrester", "transient voltage"],
    "magnetism": ["magnetism", "magnetic", "flux", "reluctance", "permeability"],
    "radiation-light": ["radiation", "light", "illumination", "spectrum", "wave length", "frequency"],
    "transients": ["transient", "temporary", "permanent term", "oscillation", "damping", "decrement"],
    "waves-lines": ["wave", "waves", "transmission line", "standing wave", "traveling wave", "travelling wave"],
}


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def rel(path: Path, root: Path) -> str:
    return str(path.relative_to(root)).replace("\\", "/")


def status_counts(records: list[dict[str, Any]]) -> dict[str, int]:
    counts: Counter[str] = Counter()
    for record in records:
        counts[str(record.get("status") or "unspecified")] += 1
    return dict(sorted(counts.items()))


def verification_counts(records: list[dict[str, Any]]) -> dict[str, int]:
    counts: Counter[str] = Counter()
    for record in records:
        source_ref = record.get("source_ref") or {}
        if isinstance(source_ref, dict):
            counts[str(source_ref.get("verification") or "unspecified")] += 1
        elif record.get("source_refs"):
            counts["multiple-source-refs"] += 1
        else:
            counts["no-source-ref"] += 1
    return dict(sorted(counts.items()))


def compact_source_ref(record: dict[str, Any]) -> dict[str, Any]:
    source_ref = record.get("source_ref")
    if isinstance(source_ref, dict):
        return {
            "source_id": source_ref.get("source_id"),
            "line_start": source_ref.get("line_start"),
            "line_end": source_ref.get("line_end"),
            "verification": source_ref.get("verification", "unspecified"),
        }
    return {}


def discover_promoted_figures(root: Path) -> list[dict[str, Any]]:
    promoted: list[dict[str, Any]] = []
    for manifest_path in sorted((root / "diagrams" / "original").glob("*/figures/*.json")):
        manifest = load_json(manifest_path, {})
        if not isinstance(manifest, dict):
            continue
        output_path = Path(str(manifest.get("output_path", "")))
        public_path = ""
        if output_path.parts:
            try:
                source_id = manifest_path.parts[-3]
                public_candidate = (
                    root
                    / "site"
                    / "public"
                    / "diagrams"
                    / "original"
                    / source_id
                    / "figures"
                    / output_path.name
                )
                if public_candidate.exists():
                    public_path = "/" + rel(public_candidate, root / "site" / "public")
            except IndexError:
                public_path = ""
        promoted.append(
            {
                "id": manifest.get("id"),
                "source_id": manifest.get("source_id"),
                "status": manifest.get("status"),
                "source_location": manifest.get("source_location"),
                "output_path": manifest.get("output_path"),
                "manifest_path": rel(manifest_path, root),
                "public_path": public_path,
                "width": manifest.get("width"),
                "height": manifest.get("height"),
                "sha256": manifest.get("sha256"),
                "quality_note": manifest.get("quality_note"),
            }
        )
    return promoted


def source_next_action(source: dict[str, Any], counts: dict[str, int], promoted_count: int) -> str:
    source_status = str(source.get("source_status") or "")
    source_id = str(source.get("source_id") or "")
    if source_status == "raw":
        return "Run OCR, create bibliographic metadata, then seed candidate catalogs."
    if source_id == "america-and-new-epoch":
        return "Scan-verify chapter starts and keep historical/social claims separate from electrical theory."
    if counts.get("chapters", 0) == 0:
        return "Review structural parser; no chapter or lecture records were found."
    if counts.get("figures", 0) > 0 and promoted_count == 0:
        return "Promote scan-verified figure crops and anchor high-value figures to pages."
    if counts.get("figures", 0) == 0:
        return "Scan-verify structural starts, then identify whether the source has diagrams or figures worth extraction."
    if counts.get("equations", 0) > 0:
        return "Triage candidate equations into canonical, false positive, and needs-review groups."
    return "Continue scan verification and cross-link concepts, equations, and diagrams."


def build_source_summary(
    root: Path,
    source: dict[str, Any],
    promoted_by_source: dict[str, list[dict[str, Any]]],
) -> dict[str, Any]:
    source_id = source["source_id"]
    processed_dir = root / "processed" / source_id
    source_dir = root / "sources" / source_id
    records: dict[str, list[dict[str, Any]]] = {}
    record_counts: dict[str, int] = {}
    status_by_catalog: dict[str, dict[str, int]] = {}
    verification_by_catalog: dict[str, dict[str, int]] = {}

    for key, filename in CATALOG_FILES.items():
        loaded = load_json(processed_dir / filename, [])
        if not isinstance(loaded, list):
            loaded = []
        records[key] = loaded
        record_counts[key] = len(loaded)
        status_by_catalog[key] = status_counts(loaded)
        verification_by_catalog[key] = verification_counts(loaded)

    cleaned_dir = processed_dir / "cleaned_text"
    cleaned_files = sorted(
        path for path in cleaned_dir.glob("*.md") if path.name != "internet-archive-ocr.txt"
    )
    raw_files = sorted((source_dir / "raw").glob("*")) if (source_dir / "raw").exists() else []
    promoted = promoted_by_source.get(source_id, [])

    summary = {
        "source_id": source_id,
        "title": source.get("title"),
        "year": source.get("year"),
        "source_status": source.get("source_status"),
        "processed_status": source.get("processed_status"),
        "internet_archive_id": source.get("internet_archive_id"),
        "local_raw_file": source.get("local_raw_file"),
        "site_path": source.get("site_path"),
        "raw_file_count": len([path for path in raw_files if path.is_file()]),
        "has_processing_report": (processed_dir / "processing_report.md").exists(),
        "has_ocr_seed": (cleaned_dir / "internet-archive-ocr.txt").exists(),
        "cleaned_text_file_count": len(cleaned_files),
        "record_counts": record_counts,
        "status_by_catalog": status_by_catalog,
        "verification_by_catalog": verification_by_catalog,
        "promoted_original_figure_count": len(promoted),
        "next_action": source_next_action(source, record_counts, len(promoted)),
    }
    return summary


def build_equation_index(sources: list[dict[str, Any]], root: Path) -> dict[str, Any]:
    records: list[dict[str, Any]] = []
    source_titles = {source["source_id"]: source.get("title") for source in sources}
    for source in sources:
        source_id = source["source_id"]
        equations = load_json(root / "processed" / source_id / "equations.json", [])
        if not isinstance(equations, list):
            continue
        for equation in equations:
            records.append(
                {
                    "id": equation.get("id"),
                    "source_id": source_id,
                    "source_title": source_titles.get(source_id),
                    "original_form": equation.get("original_form"),
                    "modern_form": equation.get("modern_form"),
                    "variables": equation.get("variables", []),
                    "physical_meaning": equation.get("physical_meaning"),
                    "status": equation.get("status", "unspecified"),
                    "source_ref": compact_source_ref(equation),
                }
            )
    return {
        "quality_note": "Most records are OCR-derived equation candidates and require scan verification.",
        "total_records": len(records),
        "status_counts": status_counts(records),
        "verification_counts": verification_counts(records),
        "records": records,
    }


def build_figure_index(
    sources: list[dict[str, Any]],
    root: Path,
    promoted: list[dict[str, Any]],
) -> dict[str, Any]:
    records: list[dict[str, Any]] = []
    source_titles = {source["source_id"]: source.get("title") for source in sources}
    for source in sources:
        source_id = source["source_id"]
        figures = load_json(root / "processed" / source_id / "figures.json", [])
        if not isinstance(figures, list):
            continue
        for figure in figures:
            records.append(
                {
                    "id": figure.get("id"),
                    "source_id": source_id,
                    "source_title": source_titles.get(source_id),
                    "figure_number": figure.get("figure_number"),
                    "caption": figure.get("caption"),
                    "linked_concepts": figure.get("linked_concepts", []),
                    "status": figure.get("status", "unspecified"),
                    "source_ref": compact_source_ref(figure),
                }
            )
    return {
        "quality_note": "Candidate figure records come from OCR. Promoted crops are separate scan-derived assets.",
        "candidate_total_records": len(records),
        "promoted_original_figure_count": len(promoted),
        "status_counts": status_counts(records),
        "verification_counts": verification_counts(records),
        "candidate_records": records,
        "promoted_original_figures": promoted,
    }


def build_glossary_index(sources: list[dict[str, Any]], root: Path) -> dict[str, Any]:
    grouped: dict[str, dict[str, Any]] = {}
    for source in sources:
        source_id = source["source_id"]
        glossary = load_json(root / "processed" / source_id / "glossary.json", [])
        if not isinstance(glossary, list):
            continue
        for entry in glossary:
            term = str(entry.get("term", "")).strip()
            if not term:
                continue
            key = term.lower()
            bucket = grouped.setdefault(
                key,
                {
                    "term": term,
                    "modern_equivalents": [],
                    "total_occurrence_count_in_ocr": 0,
                    "sources": [],
                    "statuses": Counter(),
                },
            )
            modern = entry.get("modern_equivalent")
            if modern and modern not in bucket["modern_equivalents"]:
                bucket["modern_equivalents"].append(modern)
            bucket["total_occurrence_count_in_ocr"] += int(entry.get("occurrence_count_in_ocr") or 0)
            bucket["sources"].append(
                {
                    "source_id": source_id,
                    "source_title": source.get("title"),
                    "occurrence_count_in_ocr": entry.get("occurrence_count_in_ocr", 0),
                    "status": entry.get("status", "unspecified"),
                }
            )
            bucket["statuses"][str(entry.get("status") or "unspecified")] += 1

    records = []
    for bucket in grouped.values():
        records.append(
            {
                "term": bucket["term"],
                "modern_equivalents": bucket["modern_equivalents"],
                "total_occurrence_count_in_ocr": bucket["total_occurrence_count_in_ocr"],
                "sources": sorted(bucket["sources"], key=lambda item: item["source_id"]),
                "status_counts": dict(sorted(bucket["statuses"].items())),
            }
        )
    records.sort(key=lambda item: item["term"].lower())
    return {
        "quality_note": "Glossary entries are seeded from OCR term lists and must be refined against the source text.",
        "total_terms": len(records),
        "records": records,
    }


def build_concept_index(sources: list[dict[str, Any]], root: Path) -> dict[str, Any]:
    grouped: dict[str, dict[str, Any]] = {}
    for source in sources:
        source_id = source["source_id"]
        concepts = load_json(root / "processed" / source_id / "concepts.json", [])
        if not isinstance(concepts, list):
            continue
        for concept in concepts:
            concept_id = str(concept.get("id") or concept.get("label") or "").strip()
            if not concept_id:
                continue
            bucket = grouped.setdefault(
                concept_id,
                {
                    "id": concept_id,
                    "label": concept.get("label", concept_id),
                    "total_occurrence_count_in_ocr": 0,
                    "sources": [],
                    "statuses": Counter(),
                },
            )
            bucket["total_occurrence_count_in_ocr"] += int(concept.get("occurrence_count_in_ocr") or 0)
            bucket["sources"].append(
                {
                    "source_id": source_id,
                    "source_title": source.get("title"),
                    "occurrence_count_in_ocr": concept.get("occurrence_count_in_ocr", 0),
                    "status": concept.get("status", "unspecified"),
                }
            )
            bucket["statuses"][str(concept.get("status") or "unspecified")] += 1

    records = []
    for bucket in grouped.values():
        records.append(
            {
                "id": bucket["id"],
                "label": bucket["label"],
                "total_occurrence_count_in_ocr": bucket["total_occurrence_count_in_ocr"],
                "sources": sorted(bucket["sources"], key=lambda item: item["source_id"]),
                "status_counts": dict(sorted(bucket["statuses"].items())),
            }
        )
    records.sort(key=lambda item: (-item["total_occurrence_count_in_ocr"], item["label"]))
    return {
        "quality_note": "Concept counts are OCR occurrence aids, not conceptual conclusions.",
        "total_concepts": len(records),
        "records": records,
    }


def build_quote_index(sources: list[dict[str, Any]], root: Path) -> dict[str, Any]:
    records: list[dict[str, Any]] = []
    for source in sources:
        source_id = source["source_id"]
        quotes = load_json(root / "processed" / source_id / "quotes.json", [])
        if not isinstance(quotes, list):
            continue
        for quote in quotes:
            records.append(
                {
                    "id": quote.get("id"),
                    "source_id": source_id,
                    "source_title": source.get("title"),
                    "quote_candidate": quote.get("quote_candidate"),
                    "why_it_matters": quote.get("why_it_matters"),
                    "status": quote.get("status", "unspecified"),
                    "source_ref": compact_source_ref(quote),
                }
            )
    return {
        "quality_note": "Quote candidates preserve promising OCR lines; canonical quote pages require scan verification.",
        "total_records": len(records),
        "status_counts": status_counts(records),
        "verification_counts": verification_counts(records),
        "records": records,
    }


def infer_confidence(record_type: str, record: dict[str, Any]) -> str:
    status = str(record.get("status") or "").lower()
    source_ref = record.get("source_ref")
    source_refs = record.get("source_refs")
    if "promoted" in status or record_type == "promoted_original_figure":
        return "scan-crop-promoted"
    if isinstance(source_ref, dict) and source_ref.get("line_start"):
        return "source-located-ocr-candidate"
    if isinstance(source_refs, list) and source_refs:
        return "source-located-candidate"
    if record_type in {"concept", "glossary"}:
        return "ocr-occurrence-index"
    return "candidate-needs-review"


def evidence_record(
    source: dict[str, Any],
    record_type: str,
    record_id: str,
    label: str,
    status: str,
    evidence: dict[str, Any],
    confidence: str,
) -> dict[str, Any]:
    return {
        "id": f"{source['source_id']}::{record_type}::{record_id}",
        "person": "Charles Proteus Steinmetz",
        "collection": "steinmetz",
        "source_id": source["source_id"],
        "source_title": source.get("title"),
        "year": source.get("year"),
        "record_type": record_type,
        "record_id": record_id,
        "label": label,
        "status": status,
        "confidence": confidence,
        "site_path": source.get("site_path"),
        "evidence": evidence,
    }


def build_evidence_ledger(
    sources: list[dict[str, Any]],
    root: Path,
    promoted: list[dict[str, Any]],
) -> dict[str, Any]:
    records: list[dict[str, Any]] = []

    for source in sources:
        source_id = source["source_id"]
        records.append(
            evidence_record(
                source,
                "source",
                source_id,
                str(source.get("title") or source_id),
                str(source.get("source_status") or "unspecified"),
                {
                    "processed_status": source.get("processed_status"),
                    "internet_archive_id": source.get("internet_archive_id"),
                    "local_raw_file": source.get("local_raw_file"),
                },
                "source-custody-record",
            )
        )

        for concept in load_json(root / "processed" / source_id / "concepts.json", []):
            if not isinstance(concept, dict):
                continue
            record_id = str(concept.get("id") or concept.get("label") or "").strip()
            if not record_id:
                continue
            records.append(
                evidence_record(
                    source,
                    "concept",
                    record_id,
                    str(concept.get("label") or record_id),
                    str(concept.get("status") or "seeded"),
                    {
                        "occurrence_count_in_ocr": concept.get("occurrence_count_in_ocr", 0),
                        "related": concept.get("related", []),
                    },
                    infer_confidence("concept", concept),
                )
            )

        for term in load_json(root / "processed" / source_id / "glossary.json", []):
            if not isinstance(term, dict):
                continue
            label = str(term.get("term") or "").strip()
            if not label:
                continue
            records.append(
                evidence_record(
                    source,
                    "glossary",
                    label.lower().replace(" ", "-"),
                    label,
                    str(term.get("status") or "seeded"),
                    {
                        "modern_equivalent": term.get("modern_equivalent"),
                        "occurrence_count_in_ocr": term.get("occurrence_count_in_ocr", 0),
                        "source_refs": term.get("source_refs", []),
                    },
                    infer_confidence("glossary", term),
                )
            )

        for equation in load_json(root / "processed" / source_id / "equations.json", []):
            if not isinstance(equation, dict):
                continue
            record_id = str(equation.get("id") or "").strip()
            if not record_id:
                continue
            records.append(
                evidence_record(
                    source,
                    "equation",
                    record_id,
                    str(equation.get("original_form") or record_id),
                    str(equation.get("status") or "candidate"),
                    {
                        "original_form": equation.get("original_form"),
                        "modern_form": equation.get("modern_form"),
                        "source_ref": compact_source_ref(equation),
                    },
                    infer_confidence("equation", equation),
                )
            )

        for figure in load_json(root / "processed" / source_id / "figures.json", []):
            if not isinstance(figure, dict):
                continue
            record_id = str(figure.get("id") or "").strip()
            if not record_id:
                continue
            records.append(
                evidence_record(
                    source,
                    "figure",
                    record_id,
                    str(figure.get("caption") or figure.get("figure_number") or record_id),
                    str(figure.get("status") or "candidate"),
                    {
                        "figure_number": figure.get("figure_number"),
                        "caption": figure.get("caption"),
                        "linked_concepts": figure.get("linked_concepts", []),
                        "source_ref": compact_source_ref(figure),
                    },
                    infer_confidence("figure", figure),
                )
            )

        for quote in load_json(root / "processed" / source_id / "quotes.json", []):
            if not isinstance(quote, dict):
                continue
            record_id = str(quote.get("id") or "").strip()
            if not record_id:
                continue
            records.append(
                evidence_record(
                    source,
                    "quote",
                    record_id,
                    str(quote.get("quote_candidate") or record_id),
                    str(quote.get("status") or "candidate"),
                    {
                        "quote_candidate": quote.get("quote_candidate"),
                        "why_it_matters": quote.get("why_it_matters"),
                        "source_ref": compact_source_ref(quote),
                    },
                    infer_confidence("quote", quote),
                )
            )

    source_by_id = {source["source_id"]: source for source in sources}
    for figure in promoted:
        source = source_by_id.get(str(figure.get("source_id")))
        if not source:
            continue
        record_id = str(figure.get("id") or figure.get("output_path") or "").strip()
        records.append(
            evidence_record(
                source,
                "promoted_original_figure",
                record_id,
                str(figure.get("source_location") or record_id),
                str(figure.get("status") or "promoted"),
                {
                    "manifest_path": figure.get("manifest_path"),
                    "public_path": figure.get("public_path"),
                    "sha256": figure.get("sha256"),
                    "quality_note": figure.get("quality_note"),
                },
                "scan-crop-promoted",
            )
        )

    type_counts = Counter(record["record_type"] for record in records)
    confidence_counts = Counter(record["confidence"] for record in records)
    source_counts = Counter(record["source_id"] for record in records)

    return {
        "quality_note": (
            "Evidence ledger records are traceability objects. They are not all reviewed claims. "
            "Use confidence and status before quoting or interpreting a record."
        ),
        "total_records": len(records),
        "record_type_counts": dict(sorted(type_counts.items())),
        "confidence_counts": dict(sorted(confidence_counts.items())),
        "source_counts": dict(sorted(source_counts.items())),
        "records": records,
    }


def count_theme_hits(text: str) -> dict[str, int]:
    lower = f" {text.lower()} "
    counts: dict[str, int] = {}
    for theme, patterns in THEME_PATTERNS.items():
        total = 0
        for pattern in patterns:
            total += lower.count(pattern.lower())
        if total:
            counts[theme] = total
    return dict(sorted(counts.items(), key=lambda item: (-item[1], item[0])))


def read_chapter_text(root: Path, text_path: str) -> str:
    path = root / text_path
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def build_chapter_atlas(sources: list[dict[str, Any]], root: Path) -> dict[str, Any]:
    records: list[dict[str, Any]] = []
    for source in sources:
        source_id = source["source_id"]
        chapters = load_json(root / "processed" / source_id / "chapters.json", [])
        if not isinstance(chapters, list):
            continue
        for chapter in chapters:
            if not isinstance(chapter, dict):
                continue
            text_path = str(chapter.get("text_path") or "")
            text = read_chapter_text(root, text_path)
            theme_counts = count_theme_hits(text)
            records.append(
                {
                    "id": chapter.get("id"),
                    "source_id": source_id,
                    "source_title": source.get("title"),
                    "sequence": chapter.get("sequence"),
                    "kind": chapter.get("kind"),
                    "title": chapter.get("title"),
                    "line_start": chapter.get("line_start"),
                    "line_end": chapter.get("line_end"),
                    "text_path": text_path,
                    "status": chapter.get("status", "candidate"),
                    "word_count": len(text.split()) if text else 0,
                    "theme_counts": theme_counts,
                    "top_themes": list(theme_counts)[:5],
                }
            )
    source_counts = Counter(record["source_id"] for record in records)
    theme_totals: Counter[str] = Counter()
    for record in records:
        theme_totals.update(record["theme_counts"])
    return {
        "quality_note": (
            "Chapter atlas theme counts are OCR reading aids. They help route research work, "
            "but they do not replace corrected text or scan verification."
        ),
        "total_records": len(records),
        "source_counts": dict(sorted(source_counts.items())),
        "theme_totals": dict(sorted(theme_totals.items(), key=lambda item: (-item[1], item[0]))),
        "records": records,
    }


def build_annotation_index(
    sources: list[dict[str, Any]],
    root: Path,
    source_summaries: list[dict[str, Any]],
) -> dict[str, Any]:
    """Collect manual annotations and generate review annotations from custody state."""

    records: list[dict[str, Any]] = []
    summary_by_source = {summary["source_id"]: summary for summary in source_summaries}

    for source in sources:
        source_id = source["source_id"]
        annotations = load_json(root / "processed" / source_id / "annotations.json", [])
        if isinstance(annotations, list):
            for index, annotation in enumerate(annotations, start=1):
                if not isinstance(annotation, dict):
                    continue
                records.append(
                    {
                        "id": annotation.get("id") or f"{source_id}-manual-annotation-{index:03d}",
                        "source_id": source_id,
                        "source_title": source.get("title"),
                        "kind": annotation.get("kind", "manual"),
                        "annotation": annotation.get("annotation") or annotation.get("note"),
                        "target": annotation.get("target"),
                        "status": annotation.get("status", "manual-candidate"),
                        "generated": False,
                    }
                )

        summary = summary_by_source[source_id]
        counts = summary["record_counts"]
        records.append(
            {
                "id": f"{source_id}-next-action",
                "source_id": source_id,
                "source_title": source.get("title"),
                "kind": "next-action",
                "annotation": summary["next_action"],
                "target": source.get("site_path"),
                "status": "generated-review-aid",
                "generated": True,
            }
        )
        if summary["promoted_original_figure_count"]:
            records.append(
                {
                    "id": f"{source_id}-promoted-original-crops",
                    "source_id": source_id,
                    "source_title": source.get("title"),
                    "kind": "visual-custody",
                    "annotation": (
                        f"{summary['promoted_original_figure_count']} promoted original "
                        "scan-crop assets have manifests and checksums."
                    ),
                    "target": "diagrams/original",
                    "status": "generated-custody-note",
                    "generated": True,
                }
            )
        if counts.get("equations", 0):
            records.append(
                {
                    "id": f"{source_id}-equation-triage",
                    "source_id": source_id,
                    "source_title": source.get("title"),
                    "kind": "equation-triage",
                    "annotation": (
                        f"{counts.get('equations', 0)} OCR-derived equation candidates "
                        "need triage into canonical, false positive, and review groups."
                    ),
                    "target": f"processed/{source_id}/equations.json",
                    "status": "generated-review-aid",
                    "generated": True,
                }
            )
        if counts.get("glossary", 0):
            records.append(
                {
                    "id": f"{source_id}-glossary-review",
                    "source_id": source_id,
                    "source_title": source.get("title"),
                    "kind": "glossary-review",
                    "annotation": (
                        f"{counts.get('glossary', 0)} glossary records should be checked "
                        "against source wording before canonical promotion."
                    ),
                    "target": f"processed/{source_id}/glossary.json",
                    "status": "generated-review-aid",
                    "generated": True,
                }
            )

    return {
        "quality_note": (
            "Annotations include manual source notes when present plus generated review "
            "aids derived from processing state. Generated annotations are not source claims."
        ),
        "total_records": len(records),
        "manual_records": len([record for record in records if not record["generated"]]),
        "generated_records": len([record for record in records if record["generated"]]),
        "status_counts": status_counts(records),
        "records": records,
    }


def _crosslink_record(
    source: dict[str, Any],
    relation: str,
    target_type: str,
    target_id: str,
    target_label: str,
    status: str,
    evidence: dict[str, Any],
) -> dict[str, Any]:
    return {
        "source_id": source["source_id"],
        "source_title": source.get("title"),
        "relation": relation,
        "target_type": target_type,
        "target_id": target_id,
        "target_label": target_label,
        "status": status,
        "evidence": evidence,
    }


def build_crosslink_index(
    sources: list[dict[str, Any]],
    root: Path,
    promoted: list[dict[str, Any]],
) -> dict[str, Any]:
    """Build candidate navigation links between sources, terms, concepts, equations, and figures."""

    records: list[dict[str, Any]] = []
    manual_records = 0

    for source in sources:
        source_id = source["source_id"]

        crosslinks = load_json(root / "processed" / source_id / "crosslinks.json", [])
        if isinstance(crosslinks, list):
            for index, crosslink in enumerate(crosslinks, start=1):
                if not isinstance(crosslink, dict):
                    continue
                manual_records += 1
                records.append(
                    {
                        "source_id": source_id,
                        "source_title": source.get("title"),
                        "relation": crosslink.get("relation", "manual"),
                        "target_type": crosslink.get("target_type"),
                        "target_id": crosslink.get("target_id")
                        or f"{source_id}-manual-crosslink-{index:03d}",
                        "target_label": crosslink.get("target_label"),
                        "status": crosslink.get("status", "manual-candidate"),
                        "evidence": crosslink.get("evidence", {}),
                    }
                )

        concepts = load_json(root / "processed" / source_id / "concepts.json", [])
        if isinstance(concepts, list):
            for concept in concepts:
                if not isinstance(concept, dict):
                    continue
                occurrence_count = int(concept.get("occurrence_count_in_ocr") or 0)
                if occurrence_count <= 0:
                    continue
                concept_id = str(concept.get("id") or concept.get("label") or "").strip()
                if not concept_id:
                    continue
                records.append(
                    _crosslink_record(
                        source,
                        "source-mentions-concept",
                        "concept",
                        concept_id,
                        str(concept.get("label") or concept_id),
                        str(concept.get("status") or "candidate"),
                        {"occurrence_count_in_ocr": occurrence_count},
                    )
                )

        glossary = load_json(root / "processed" / source_id / "glossary.json", [])
        if isinstance(glossary, list):
            for term in glossary:
                if not isinstance(term, dict):
                    continue
                occurrence_count = int(term.get("occurrence_count_in_ocr") or 0)
                source_refs = term.get("source_refs", [])
                if occurrence_count <= 0 and not source_refs:
                    continue
                term_label = str(term.get("term") or "").strip()
                if not term_label:
                    continue
                records.append(
                    _crosslink_record(
                        source,
                        "source-uses-glossary-term",
                        "glossary-term",
                        term_label.lower().replace(" ", "-"),
                        term_label,
                        str(term.get("status") or "candidate"),
                        {
                            "occurrence_count_in_ocr": occurrence_count,
                            "source_ref_count": len(source_refs) if isinstance(source_refs, list) else 0,
                        },
                    )
                )

        equations = load_json(root / "processed" / source_id / "equations.json", [])
        if isinstance(equations, list):
            for equation in equations:
                if not isinstance(equation, dict):
                    continue
                equation_id = str(equation.get("id") or "").strip()
                if not equation_id:
                    continue
                records.append(
                    _crosslink_record(
                        source,
                        "source-has-equation-candidate",
                        "equation",
                        equation_id,
                        str(equation.get("original_form") or equation_id),
                        str(equation.get("status") or "candidate"),
                        compact_source_ref(equation),
                    )
                )

        figures = load_json(root / "processed" / source_id / "figures.json", [])
        if isinstance(figures, list):
            for figure in figures:
                if not isinstance(figure, dict):
                    continue
                figure_id = str(figure.get("id") or "").strip()
                if not figure_id:
                    continue
                records.append(
                    _crosslink_record(
                        source,
                        "source-has-figure-candidate",
                        "figure",
                        figure_id,
                        str(figure.get("caption") or figure_id),
                        str(figure.get("status") or "candidate"),
                        compact_source_ref(figure),
                    )
                )

    source_by_id = {source["source_id"]: source for source in sources}
    for figure in promoted:
        source = source_by_id.get(str(figure.get("source_id")))
        if not source:
            continue
        records.append(
            _crosslink_record(
                source,
                "source-has-promoted-original-figure",
                "original-scan-crop",
                str(figure.get("id") or ""),
                str(figure.get("source_location") or figure.get("id") or ""),
                str(figure.get("status") or "promoted"),
                {
                    "manifest_path": figure.get("manifest_path"),
                    "public_path": figure.get("public_path"),
                    "sha256": figure.get("sha256"),
                },
            )
        )

    relation_counter = Counter(str(record.get("relation") or "unspecified") for record in records)
    target_counter = Counter(str(record.get("target_type") or "unspecified") for record in records)

    return {
        "quality_note": (
            "Crosslinks are generated navigation and review aids. Candidate links do not "
            "make a source claim canonical."
        ),
        "total_records": len(records),
        "manual_records": manual_records,
        "generated_records": len(records) - manual_records,
        "relation_counts": dict(sorted(relation_counter.items())),
        "target_type_counts": dict(sorted(target_counter.items())),
        "records": records,
    }


def markdown_table_row(values: list[Any]) -> str:
    escaped = [str(value).replace("|", "\\|").replace("\n", " ") for value in values]
    return "| " + " | ".join(escaped) + " |"


def write_status_markdown(path: Path, source_summaries: list[dict[str, Any]]) -> None:
    lines = [
        "# Source Processing Status",
        "",
        "This dashboard is generated from the processed JSON catalogs. Counts describe custody and review state; they are not claims that every OCR-derived candidate is correct.",
        "",
        "## Corpus Table",
        "",
        markdown_table_row(
            [
                "Source",
                "Status",
                "Chapters",
                "Equations",
                "Figures",
                "Original Crops",
                "Glossary",
                "Quotes",
                "Next Action",
            ]
        ),
        markdown_table_row(["---", "---", "---:", "---:", "---:", "---:", "---:", "---:", "---"]),
    ]
    for summary in source_summaries:
        counts = summary["record_counts"]
        lines.append(
            markdown_table_row(
                [
                    summary["title"],
                    summary["processed_status"],
                    counts.get("chapters", 0),
                    counts.get("equations", 0),
                    counts.get("figures", 0),
                    summary["promoted_original_figure_count"],
                    counts.get("glossary", 0),
                    counts.get("quotes", 0),
                    summary["next_action"],
                ]
            )
        )

    lines.extend(
        [
            "",
            "## Quality Rules",
            "",
            "- Candidate records are generated from OCR and must not be treated as canonical without scan review.",
            "- Promoted original crops are scan-derived assets with a crop manifest and checksum.",
            "- Concept and glossary counts are discovery aids, not interpretive conclusions.",
            "- Ether-field and Tesla-era links belong in labeled interpretive or comparative pages, not in raw source indexes.",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--out-dir", type=Path, default=Path("processed"))
    args = parser.parse_args()

    root = args.root.resolve()
    out_dir = (root / args.out_dir).resolve()
    sources = load_json(root / "sources" / "source_catalog.json", [])
    if not isinstance(sources, list):
        raise SystemExit("sources/source_catalog.json must be a list")

    promoted = discover_promoted_figures(root)
    promoted_by_source: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for figure in promoted:
        promoted_by_source[str(figure.get("source_id"))].append(figure)

    source_summaries = [
        build_source_summary(root, source, promoted_by_source)
        for source in sources
    ]

    research_index = {
        "quality_note": "Repository-wide index of processed source custody and candidate review state.",
        "source_count": len(source_summaries),
        "sources": source_summaries,
    }

    write_json(out_dir / "research_index.json", research_index)
    write_json(out_dir / "equation_index.json", build_equation_index(sources, root))
    write_json(out_dir / "figure_index.json", build_figure_index(sources, root, promoted))
    write_json(out_dir / "glossary_index.json", build_glossary_index(sources, root))
    write_json(out_dir / "concept_index.json", build_concept_index(sources, root))
    write_json(out_dir / "quote_index.json", build_quote_index(sources, root))
    write_json(out_dir / "annotations_index.json", build_annotation_index(sources, root, source_summaries))
    write_json(out_dir / "crosslinks_index.json", build_crosslink_index(sources, root, promoted))
    write_json(out_dir / "evidence_ledger.json", build_evidence_ledger(sources, root, promoted))
    write_json(out_dir / "chapter_atlas.json", build_chapter_atlas(sources, root))
    write_status_markdown(out_dir / "source_processing_status.md", source_summaries)

    print(f"Wrote research indexes for {len(source_summaries)} sources to {rel(out_dir, root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
