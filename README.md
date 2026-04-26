# Steinmetz Decoded

An open-source research archive and public knowledge base for the writings of Charles Proteus Steinmetz.

This project is designed to become a rigorous, source-grounded, mathematically faithful, historically careful, and conceptually deep archive of Steinmetz's books, lectures, papers, diagrams, terminology, equations, and electrical worldview.

The project is not a summary site. It is a research system.

## Mission

For every processed source, the archive aims to preserve and explain:

- Steinmetz's original wording, notation, definitions, diagrams, and page references.
- Modern electrical engineering equivalents and mathematical translations.
- Historical context from early twentieth-century electrical science.
- Tesla-era parallels and differences, when the evidence supports them.
- Clearly labeled ether-field or Ken Wheeler-style interpretive readings, separated from historical claims.
- Hidden gems: statements that are technically rich, forgotten, philosophically important, or unusually clear.

Every claim should be traceable to a source text, a derivation, a modern reference, or an explicitly labeled interpretation.

## Repository Map

```text
sources/       Raw PDFs, scans, source manifests, custody notes, and source metadata.
processed/     Cleaned OCR, chapter splits, extracted candidate JSON, page maps, and processing reports.
analysis/      Book, chapter, concept, equation, and diagram commentary.
concepts/      Cross-source concept encyclopedia pages.
math/          Equation catalogs, derivations, notation translations, and worked examples.
diagrams/      Original, cleaned, recreated, and annotated diagrams.
comparisons/   Steinmetz vs modern EE, Tesla-era science, and labeled ether-field readings.
glossary/      Historical, obsolete, and modernized electrical terminology.
hidden-gems/   Important overlooked passages and research notes.
research-questions/
               Living research agenda and unresolved questions.
pipeline/      Repeatable ingestion, extraction, schema, and quality-control tooling.
site/          Astro/Starlight public documentation website.
```

## First Canonical Source

The first source is:

**Charles Proteus Steinmetz, _Radiation, Light and Illumination: A Series of Engineering Lectures Delivered at Union College_**, McGraw-Hill, 1909, compiled and edited by Joseph LeRoy Hayden.

The local raw source files are stored in:

```text
sources/radiation-light-and-illumination/raw/
```

The first processed OCR seed is stored in:

```text
processed/radiation-light-and-illumination/cleaned_text/internet-archive-ocr.txt
```

## Seeded Source Corpus

The first expansion pass has also copied local PDFs and, where available, downloaded public OCR seeds for:

- _Elementary Lectures on Electric Discharges, Waves and Impulses, and Other Transients_
- _Engineering Mathematics_
- _Theory and Calculation of Alternating Current Phenomena_
- _Theory and Calculation of Transient Electric Phenomena and Oscillations_
- _Theoretical Elements of Electrical Engineering_
- _Investigation of Some Trouble in the Generating System of the Commonwealth Edison Co._

See `sources/source_catalog.json` for the current corpus inventory and processing state.

## Quality Labels

Use these labels throughout the project:

- **Steinmetz explicitly states**: directly supported by source text.
- **Modern equivalent**: translation into current electrical engineering language.
- **Mathematical reconstruction**: a derivation or notation translation reconstructed from source and math.
- **Historical note**: contextual material requiring a source.
- **Interpretive reading**: ether-field, Ken Wheeler-style, Dollard-style, or other nonstandard reading.
- **Speculative connection**: possible but unproven connection.
- **Needs verification**: claim, page map, OCR, citation, diagram, or derivation still awaiting review.

## Website

The public site skeleton lives in `site/` and uses Astro + Starlight. It supports MDX long-form pages, sidebar navigation, search, KaTeX math, citations, callouts, and interactive explainer components.

Current site features include:

- Expanded source-library pages for the first seeded Steinmetz corpus.
- Recreated research-guide diagrams for radiation, transients, symbolic AC geometry, hysteresis, field propagation, and illumination.
- Interactive frequency/wavelength and impedance/reactance tools.
- Quality labels that separate source claims, modern interpretation, mathematical reconstruction, and speculative readings.

To run it after dependencies are installed:

```powershell
cd site
npm run dev
```

To verify a production build:

```powershell
cd site
npm run build
```

## Processing Pipeline

The first standard-library pipeline script is:

```powershell
python pipeline/scripts/seed_source_from_ocr.py `
  --source-id radiation-light-and-illumination `
  --ocr processed/radiation-light-and-illumination/cleaned_text/internet-archive-ocr.txt
```

It creates chapter splits and candidate catalogs while preserving the raw OCR. Human review is still required before promoting candidates to canonical analysis.
