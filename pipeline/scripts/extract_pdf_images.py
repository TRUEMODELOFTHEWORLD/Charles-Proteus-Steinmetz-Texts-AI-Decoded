#!/usr/bin/env python3
"""Extract reviewable image assets from Steinmetz source PDFs.

This is an image custody tool, not an automatic figure verifier. It can render
source pages or dump embedded PDF images so a researcher can crop and promote
actual Steinmetz figures into diagrams/original/<source-id>/figures/.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


try:
    import fitz  # type: ignore
except ImportError:  # pragma: no cover - user-facing setup path
    print(
        "PyMuPDF is required. Install with: python -m pip install -r pipeline/requirements.txt",
        file=sys.stderr,
    )
    raise SystemExit(2)


@dataclass(frozen=True)
class PageSelection:
    indices: list[int]
    label: str


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_page_selection(spec: str | None, page_count: int, max_pages: int | None) -> PageSelection:
    if not spec:
        indices = list(range(page_count))
        label = "all"
    else:
        indices = []
        for part in spec.split(","):
            part = part.strip()
            if not part:
                continue
            if "-" in part:
                start_text, end_text = part.split("-", 1)
                start = int(start_text)
                end = int(end_text)
                if start > end:
                    raise ValueError(f"Invalid page range: {part}")
                indices.extend(range(start - 1, end))
            else:
                indices.append(int(part) - 1)
        label = spec

    unique = []
    seen = set()
    for index in indices:
        if index < 0 or index >= page_count:
            raise ValueError(f"Page {index + 1} is outside PDF page count {page_count}")
        if index not in seen:
            seen.add(index)
            unique.append(index)
    if max_pages is not None:
        unique = unique[:max_pages]
    return PageSelection(unique, label)


def rel(path: Path) -> str:
    return str(path).replace("\\", "/")


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def render_pages(
    doc: "fitz.Document",
    *,
    source_id: str,
    pdf_path: Path,
    out_root: Path,
    selection: PageSelection,
    dpi: int,
    overwrite: bool,
) -> list[dict]:
    page_dir = out_root / source_id / "image_extraction" / "page_renders"
    page_dir.mkdir(parents=True, exist_ok=True)
    zoom = dpi / 72
    matrix = fitz.Matrix(zoom, zoom)
    records: list[dict] = []

    for page_index in selection.indices:
        page = doc.load_page(page_index)
        out_path = page_dir / f"pdf-page-{page_index + 1:04d}-{dpi}dpi.png"
        if not out_path.exists() or overwrite:
            pixmap = page.get_pixmap(matrix=matrix, alpha=False)
            pixmap.save(out_path)
        records.append(
            {
                "id": f"{source_id}-page-render-{page_index + 1:04d}",
                "source_id": source_id,
                "asset_type": "page-render",
                "status": "generated-review-candidate",
                "source_pdf": rel(pdf_path),
                "pdf_page_index": page_index,
                "pdf_page_number": page_index + 1,
                "dpi": dpi,
                "path": rel(out_path),
                "sha256": sha256_file(out_path),
                "note": "Generated full-page render for manual figure verification and cropping.",
            }
        )
    return records


def extract_embedded_images(
    doc: "fitz.Document",
    *,
    source_id: str,
    pdf_path: Path,
    out_root: Path,
    selection: PageSelection,
    min_width: int,
    min_height: int,
    overwrite: bool,
) -> list[dict]:
    image_dir = out_root / source_id / "image_extraction" / "embedded_images"
    image_dir.mkdir(parents=True, exist_ok=True)
    records: list[dict] = []
    seen_xrefs: set[int] = set()

    for page_index in selection.indices:
        page = doc.load_page(page_index)
        for image_number, image in enumerate(page.get_images(full=True), start=1):
            xref = int(image[0])
            if xref in seen_xrefs:
                continue
            extracted = doc.extract_image(xref)
            width = int(extracted.get("width", 0))
            height = int(extracted.get("height", 0))
            if width < min_width or height < min_height:
                continue
            ext = str(extracted.get("ext", "bin")).lower()
            out_path = image_dir / f"pdf-page-{page_index + 1:04d}-xref-{xref}.{ext}"
            if not out_path.exists() or overwrite:
                out_path.write_bytes(extracted["image"])
            seen_xrefs.add(xref)
            records.append(
                {
                    "id": f"{source_id}-embedded-image-{len(records) + 1:04d}",
                    "source_id": source_id,
                    "asset_type": "embedded-image",
                    "status": "generated-review-candidate",
                    "source_pdf": rel(pdf_path),
                    "pdf_page_index": page_index,
                    "pdf_page_number": page_index + 1,
                    "pdf_page_image_number": image_number,
                    "xref": xref,
                    "width": width,
                    "height": height,
                    "path": rel(out_path),
                    "sha256": sha256_file(out_path),
                    "note": "Embedded PDF image extracted for manual figure verification and cropping.",
                }
            )
    return records


def build_manifest(
    *,
    source_id: str,
    pdf_path: Path,
    mode: str,
    page_selection: PageSelection,
    page_count: int,
    records: Iterable[dict],
) -> dict:
    return {
        "source_id": source_id,
        "source_pdf": rel(pdf_path),
        "source_pdf_sha256": sha256_file(pdf_path),
        "mode": mode,
        "page_selection": page_selection.label,
        "pdf_page_count": page_count,
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "quality_note": (
            "Generated assets are not canonical diagrams. Promote only after checking the scan, "
            "cropping the actual figure, and adding source-page metadata."
        ),
        "records": list(records),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-id", required=True)
    parser.add_argument("--pdf", type=Path, required=True)
    parser.add_argument("--mode", choices=["pages", "embedded", "both"], default="pages")
    parser.add_argument("--pages", help="1-based page spec, for example: 1-12,42,50-52")
    parser.add_argument("--max-pages", type=int)
    parser.add_argument("--dpi", type=int, default=200)
    parser.add_argument("--min-width", type=int, default=500)
    parser.add_argument("--min-height", type=int, default=500)
    parser.add_argument("--out-root", type=Path, default=Path("processed"))
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    pdf_path = args.pdf
    if not pdf_path.exists():
        raise SystemExit(f"PDF not found: {pdf_path}")

    with fitz.open(pdf_path) as doc:
        selection = parse_page_selection(args.pages, doc.page_count, args.max_pages)
        records: list[dict] = []
        if args.mode in {"pages", "both"}:
            records.extend(
                render_pages(
                    doc,
                    source_id=args.source_id,
                    pdf_path=pdf_path,
                    out_root=args.out_root,
                    selection=selection,
                    dpi=args.dpi,
                    overwrite=args.overwrite,
                )
            )
        if args.mode in {"embedded", "both"}:
            records.extend(
                extract_embedded_images(
                    doc,
                    source_id=args.source_id,
                    pdf_path=pdf_path,
                    out_root=args.out_root,
                    selection=selection,
                    min_width=args.min_width,
                    min_height=args.min_height,
                    overwrite=args.overwrite,
                )
            )

        manifest = build_manifest(
            source_id=args.source_id,
            pdf_path=pdf_path,
            mode=args.mode,
            page_selection=selection,
            page_count=doc.page_count,
            records=records,
        )

    manifest_path = args.manifest or (
        args.out_root / args.source_id / "image_extraction" / "manifest.json"
    )
    write_json(manifest_path, manifest)
    print(f"Wrote {len(records)} image records to {manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
