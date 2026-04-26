#!/usr/bin/env python3
"""Crop a verified region from a rendered source page.

Use this after rendering source pages with extract_pdf_images.py. The output is
a candidate original figure crop that can be reviewed and promoted into the
diagram archive.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_box(value: str) -> tuple[int, int, int, int]:
    parts = [int(part.strip()) for part in value.split(",")]
    if len(parts) != 4:
        raise argparse.ArgumentTypeError("Box must be x0,y0,x1,y1")
    x0, y0, x1, y1 = parts
    if x1 <= x0 or y1 <= y0:
        raise argparse.ArgumentTypeError("Box must have x1 > x0 and y1 > y0")
    return x0, y0, x1, y1


def rel(path: Path) -> str:
    return str(path).replace("\\", "/")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-image", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--box", type=parse_box, required=True, help="Pixel crop box: x0,y0,x1,y1")
    parser.add_argument("--source-id", required=True)
    parser.add_argument("--figure-id", required=True)
    parser.add_argument("--source-location", required=True)
    parser.add_argument("--status", default="candidate scan crop")
    parser.add_argument("--manifest", type=Path)
    args = parser.parse_args()

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(args.source_image) as image:
        cropped = image.crop(args.box)
        cropped.save(args.out)

    manifest = {
        "id": args.figure_id,
        "source_id": args.source_id,
        "asset_type": "original-scan-crop",
        "status": args.status,
        "source_image": rel(args.source_image),
        "source_location": args.source_location,
        "crop_box_pixels": list(args.box),
        "output_path": rel(args.out),
        "width": cropped.width,
        "height": cropped.height,
        "sha256": sha256_file(args.out),
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "quality_note": "Crop coordinates should be reviewed against the source page before canonical use.",
    }

    manifest_path = args.manifest or args.out.with_suffix(args.out.suffix + ".json")
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote crop {args.out}")
    print(f"Wrote manifest {manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
