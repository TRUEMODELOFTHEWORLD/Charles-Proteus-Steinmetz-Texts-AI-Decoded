# Processed Outputs

This directory stores machine-generated and review-stage outputs derived from `sources/`.

Typical files:

- `cleaned_text/`
- `chapters.json`
- `equations.json`
- `figures.json`
- `concepts.json`
- `glossary.json`
- `quotes.json`
- `annotations.json`
- `crosslinks.json`
- `processing_report.md`

Corpus-wide generated indexes live at the root of this directory:

- `research_index.json`
- `equation_index.json`
- `figure_index.json`
- `concept_index.json`
- `glossary_index.json`
- `quote_index.json`
- `annotations_index.json`
- `crosslinks_index.json`
- `evidence_ledger.json`
- `chapter_atlas.json`
- `chapter_workbench.json`
- `concept_concordance.json`
- `completion_audit.json`
- `canonical_equations.json`
- `source_processing_status.md`

Files here may contain candidates and should include review status fields. Canonical explanations belong in `analysis/`, `concepts/`, `math/`, `diagrams/`, `comparisons/`, `glossary/`, and the website.
