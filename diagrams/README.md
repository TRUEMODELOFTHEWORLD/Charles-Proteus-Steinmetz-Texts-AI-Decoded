# Diagram Archive

This directory stores original, cleaned, recreated, and annotated diagrams.

Recommended structure:

```text
diagrams/original/<source-id>/
diagrams/original/<source-id>/figures/
diagrams/cleaned/<source-id>/
diagrams/recreated/<source-id>/
```

Each diagram should have:

- Original scan crop.
- Cleaned raster version.
- Recreated vector version when possible.
- Diagram page in `analysis/<source-id>/diagrams/`.
- Links to concepts and equations.
- Separate modern and interpretive annotations.

Full-page renders and embedded-image dumps created by the pipeline remain in `processed/<source-id>/image_extraction/` or `processed/<source-id>/page_renders/` until a researcher promotes a verified crop.

Current recreated source-keyed sheets:

- `diagrams/recreated/ac-symbolic-method-redraw-sheet.svg`
- `diagrams/recreated/transient-condenser-response-redraw-sheet.svg`

These are reading aids, not documentary evidence. They must remain paired with original scan crops, crop manifests, and verification notes.
