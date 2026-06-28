# Source Acquisition Workflow

This checklist is for maintainers and contributors adding a new Steinmetz source to the research engine.

The archive may register a source before it is decoded, but it must not present a source as decoded until custody, OCR/text extraction, page mapping, and review state are visible.

## Intake Rule

Custody comes first. Interpretation comes last.

A valid source lead should identify:

- `source_id`: stable lowercase slug.
- `title`: full title as printed or cataloged.
- `creator`: author, editor, conference, patent inventor, or institutional custodian.
- `year`: year or approximate date.
- `edition`: edition, volume, issue, proceedings, or patent number when applicable.
- `source_type`: book, edition, article, lecture, patent, correspondence, archival collection, report, diagram, or finding aid.
- `authority_refs`: DOI, Internet Archive, HathiTrust, Google Books, Open Library, Google Patents, USPTO, library catalog, finding aid, or institutional URL.
- `custody_status`: public scan, local file, DOI only, catalog only, archive-only, restricted, needs acquisition, or duplicate check.
- `rights_note`: public domain, likely public domain, restricted, unknown, or contributor-supplied with provenance.
- `processing_status`: registered, acquired, OCR extracted, sectioned, indexed, reader generated, scan-reviewed, canonical.
- `concept_targets`: concepts likely affected.
- `equation_targets`: formulas or mathematical families likely affected.
- `figure_targets`: figures, plates, diagrams, or apparatus images likely affected.
- `glossary_targets`: historical terms likely affected.

## Repository Locations

Use these locations unless a source-specific pipeline says otherwise:

```text
sources/{source_id}/raw/          raw PDFs, scans, custody notes, checksum files
sources/{source_id}/metadata.json source-level custody and bibliographic record
processed/{source_id}/            OCR, page maps, section splits, candidate JSON
analysis/{source_id}/             human review notes and promoted commentary
site/src/content/docs/...         public source, concept, math, and visual pages
```

Do not overwrite an existing raw file with a different edition. Add edition or scan identifiers to the filename and metadata.

## Processing Gates

1. Register the source in the appropriate manifest.
2. Store the raw file or stable public source link.
3. Record custody, rights, edition, and authority metadata.
4. Generate or preserve OCR/text extraction.
5. Create page, chapter, article, lecture, or patent-section mapping.
6. Extract candidate concepts, glossary terms, quotes, formulas, and figures.
7. Generate source reader pages with verification warnings.
8. Update source overview, book coverage, concept concordance, theme evidence, equation maps, and visual maps.
9. Scan-check quotations, formulas, and diagrams before promoting them to canonical pages.
10. Update public contributor notes if a source still needs acquisition, review, or deferral.

## Review States

Use these states consistently:

- `registered`: source identified but not acquired.
- `acquired`: public scan, raw file, or official record is available.
- `ocr_extracted`: OCR/text exists and is preserved.
- `sectioned`: source has page/chapter/section mapping.
- `indexed`: candidate concepts, terms, quotes, formulas, and figures are extracted.
- `reader_generated`: public source reader exists.
- `scan_verified`: exact quotations, pages, formulas, or figures checked against scan.
- `canonical`: public synthesis is stable enough to cite as an archive explanation.

## Formula Caution

Never render raw OCR formula candidates as reviewed mathematics. Formula-like OCR belongs in verification queues until a scan check or human mathematical review confirms notation, variables, exponents, units, and surrounding prose.

Curated KaTeX belongs on canonical math pages. The source reader should remain trust-first: readable prose, isolated OCR fragments, raw transcript, and scan links.

## Contributor Path

Public contributors should use:

- `site/src/content/docs/source-library/source-acquisition-guide.mdx`
- `.github/ISSUE_TEMPLATE/new-source-intake.yml`
- `CONTRIBUTING.md`

Maintainers should use this file before promoting a new source into the generated corpus.
