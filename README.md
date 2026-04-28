# Steinmetz Decoded

LIVE DEMO : https://truemodeloftheworld.github.io/Charles-Proteus-Steinmetz-Texts-AI-Decoded/

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

See `sources/source_catalog.json` for the current processing corpus, `sources/steinmetz_bibliography_manifest.json` for the expanded Wikipedia-derived works intake, and `sources/steinmetz_patents/patent_register.json` for the seeded patent register.

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
- Recreated research-guide diagrams for radiation, transients, symbolic AC geometry, hysteresis, field propagation, and illumination, plus source-keyed redraw sheets for AC symbolic method and transient condenser response.
- A station-section/reactor reading aid for the Commonwealth Edison report.
- Interactive frequency/wavelength, AC waveform/harmonics, impedance/reactance, phasor/symbolic-form, power-factor, hysteresis-loss, transient RLC response, and lightning/surge traveling-wave tools.
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

## GitHub Pages

The repository includes `.github/workflows/deploy-pages.yml`, which builds the Astro/Starlight site from `site/` and deploys it with GitHub Actions.

On GitHub, enable Pages once:

1. Open repository **Settings**.
2. Go to **Pages**.
3. Under **Build and deployment**, set **Source** to **GitHub Actions**.
4. Push to `main` or run the workflow manually from the **Actions** tab.

The default Pages URL is:

```text
https://truemodeloftheworld.github.io/Charles-Proteus-Steinmetz-Texts-AI-Decoded/
```

## Processing Pipeline

The first standard-library pipeline script seeds source-level catalogs:

```powershell
python pipeline/scripts/seed_source_from_ocr.py `
  --source-id radiation-light-and-illumination `
  --ocr processed/radiation-light-and-illumination/cleaned_text/internet-archive-ocr.txt
```

It creates chapter splits and candidate catalogs while preserving the raw OCR. Human review is still required before promoting candidates to canonical analysis.

The corpus-wide research index builder is:

```powershell
python pipeline/scripts/build_research_indexes.py
```

It writes dashboard data for sources, concepts, equations, figures, glossary terms, quote candidates, annotations, and crosslinks into `processed/`, including `processed/source_processing_status.md`.

For PDFs with embedded text, the page-preserving extraction step is:

```powershell
python pipeline/scripts/extract_pdf_text.py `
  --source-id commonwealth-edison-generating-system-trouble `
  --pdf sources/commonwealth-edison-generating-system-trouble/raw/commonwealth-edison-generating-system-trouble-local.pdf
```

The source-specific Commonwealth Edison parser is:

```powershell
python pipeline/scripts/seed_commonwealth_edison_report.py
```

## Current Processing Milestone

The archive now includes:

- Eleven source records in `sources/source_catalog.json`.
- An expanded Steinmetz bibliography intake manifest for additional books, lecture collections, pamphlets, and papers.
- Four additional Internet Archive OCR seeds: _General Lectures on Electrical Engineering_, _America and the New Epoch_, _Theory and Calculation of Electric Apparatus_, and _Four Lectures on Relativity and Space_.
- A seeded Steinmetz patent register for the Wikipedia-listed examples, with the full 200-plus patent catalog marked as an authority-pass milestone.
- Cross-source JSON indexes under `processed/`.
- Generated annotation and crosslink indexes for review-state notes and navigation between sources, concepts, terms, equations, and figures.
- A first twelve-equation canon in `processed/canonical_equations.json`, with public pages for the new equation spine.
- A source-located candidate page for the Steinmetz hysteresis law and its 1.6-power loss relation.
- A generated source-processing dashboard.
- A PDF text extraction and page-map pass for the Commonwealth Edison report, with 5 report sections, 220 equation candidates, 12 concept candidates, 12 glossary candidates, and a deep page on reactors and synchronism.
- Fifteen original scan-derived crops: five from _Radiation, Light and Illumination_, four from _Alternating Current Phenomena_, and six from _Transient Electric Phenomena and Oscillations_, with crop manifests and checksums.
- Two source-keyed modern redraw sheets for AC symbolic-method geometry and transient condenser-response behavior.
- Public site pages for the dashboard, source library, diagram archive, concepts, equations, comparisons, and interactive tools.
- A second public layer for symbolic AC method, impedance, reactance, admittance, transient terms, standing/traveling waves, RLC oscillation, and source-located historical glossary terms.
- A practical verification queue in `VERIFICATION_QUEUE.md`.

The full requirement and milestone map is maintained in `MASTER_PROJECT_TRACKER.md`, with a public mirror at:

```text
https://truemodeloftheworld.github.io/Charles-Proteus-Steinmetz-Texts-AI-Decoded/project-tracker/
```

## Current Live-Ready Site Surface

The public site currently builds more than fifty pages, including:

- Source overviews for the seeded Steinmetz corpus.
- Deep source pages for _Radiation, Light and Illumination_, _Alternating Current Phenomena_, _Transient Electric Phenomena_, and _Engineering Mathematics_.
- Concept pages for radiation, electric waves, lightning and surges, ether, illumination, transients, symbolic method, harmonics and wave shape, hysteresis, impedance, reactance, admittance, power factor, distributed constants, oscillation and damping, inductance/capacity, power-limiting reactors, and synchronizing power.
- Equation pages for wavelength/frequency, symbolic operator `j`, reactance forms, impedance/reactance, admittance, power/effective resistance, capacity susceptance, transient terms, RLC oscillation, condenser decrement, and Commonwealth Edison synchronizing power.
- Glossary pages for condensive reactance, wattless component, imaginary unit `j`, electrostatic capacity, counter e.m.f., and effective resistance.
- Comparison pages for modern EE, AC symbolic method, Tesla-era science, Tesla-era transients, and ether-field interpretation.
- Interactive tools for frequency/wavelength, AC waveform/harmonics, impedance/reactance, phasor/symbolic form, power factor, hysteresis loss, transient RLC condenser-discharge response, and lightning/surge traveling waves.
- Original scan-crop pages for RLI visual anchors and AC Chapter V symbolic-method figures, with a modern symbolic-method redraw sheet.
- Original scan-crop page for transient starting current, condenser charge, oscillation, and decrement figures, with a modern condenser-response redraw sheet.
