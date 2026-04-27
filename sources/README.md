# Sources

This directory is the custody layer for source material.

Each source should have its own folder:

```text
sources/<source-id>/
  source_manifest.json
  book_metadata.json
  raw/
    original scans, PDFs, OCR files, downloaded metadata, or custody notes
```

The source layer should not contain interpretive claims. It records provenance, edition, public-domain status, file checksums, and processing status.

## Control Manifests

- `source_catalog.json` tracks sources already seeded into the processing pipeline.
- `steinmetz_bibliography_manifest.json` tracks the expanded Wikipedia-derived bibliography intake queue.
- `steinmetz_patents/patent_register.json` tracks the seeded patent examples and the future full patent authority pass.

The expanded manifests are allowed to contain planned records, but planned records are not source claims. They are acquisition and verification tasks.
