#!/usr/bin/env python3
"""Extract page-preserving text from a source PDF.

This is a custody step between raw PDF storage and OCR/structure parsing. It
uses embedded PDF text when available and marks the output as extracted text,
not corrected OCR or reviewed transcription.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


try:
    import fitz  # type: ignore
except ImportError:  # pragma: no cover - user-facing setup path
    print(
        "PyMuPDF is required. Install with: python -m pip install -r pipeline/requirements.txt",
        file=sys.stderr,
    )
    raise SystemExit(2)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def rel(path: Path) -> str:
    return str(path).replace("\\", "/")


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def normalize_page_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in text.splitlines()]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-id", required=True)
    parser.add_argument("--pdf", type=Path, required=True)
    parser.add_argument("--out", type=Path, default=Path("processed"))
    parser.add_argument("--text-name", default="pdf-extracted-text.txt")
    args = parser.parse_args()

    if not args.pdf.exists():
        raise SystemExit(f"PDF not found: {args.pdf}")

    out_dir = args.out / args.source_id
    cleaned_dir = out_dir / "cleaned_text"
    cleaned_dir.mkdir(parents=True, exist_ok=True)
    text_path = cleaned_dir / args.text_name
    page_map_path = out_dir / "page_map.json"

    page_records: list[dict[str, object]] = []
    chunks: list[str] = []

    with fitz.open(args.pdf) as doc:
        line_cursor = 1
        for page_index, page in enumerate(doc):
            page_number = page_index + 1
            page_text = normalize_page_text(page.get_text("text") or "")
            chunk_lines = [
                f"[[PDF_PAGE:{page_number}]]",
                page_text,
                f"[[END_PDF_PAGE:{page_number}]]",
            ]
            chunk = "\n".join(chunk_lines).strip() + "\n"
            chunks.append(chunk)

            line_count = len(chunk.splitlines())
            page_records.append(
                {
                    "source_id": args.source_id,
                    "pdf_page_index": page_index,
                    "pdf_page_number": page_number,
                    "line_start": line_cursor,
                    "line_end": line_cursor + line_count - 1,
                    "char_count": len(page_text),
                    "word_count": len(page_text.split()),
                    "text_status": "pdf-text-extracted",
                }
            )
            line_cursor += line_count

        manifest = {
            "source_id": args.source_id,
            "source_pdf": rel(args.pdf),
            "source_pdf_sha256": sha256_file(args.pdf),
            "pdf_page_count": doc.page_count,
            "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
            "text_path": rel(text_path),
            "page_map_path": rel(page_map_path),
            "quality_note": (
                "Text was extracted from the PDF text layer. It is not corrected OCR and "
                "must be checked against page images before canonical quotation."
            ),
            "pages_with_text": len([record for record in page_records if record["char_count"]]),
            "total_char_count": sum(int(record["char_count"]) for record in page_records),
            "records": page_records,
        }

    text_path.write_text("\n".join(chunks), encoding="utf-8")
    write_json(page_map_path, manifest)
    print(f"Wrote PDF text for {args.source_id} to {text_path}")
    print(f"Wrote page map to {page_map_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
