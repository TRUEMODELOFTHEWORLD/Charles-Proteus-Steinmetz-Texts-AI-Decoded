# Master Project Tracker

This tracker converts the original project charter into a working control file. It is the source of truth for what the archive is trying to become, what has already been built, what is only seeded, and what still needs careful research.

The guiding rule is speed with labels: publish useful candidate layers quickly, but never hide uncertainty. A statement must trace to a Steinmetz source, a modern reference, a mathematical derivation, or an explicitly marked interpretive reading.

## Status Legend

| Status | Meaning |
| --- | --- |
| Done | Implemented and usable in the repo or public site. |
| Started | Structure exists and first examples are public, but the work is not complete. |
| Repeating | Must be applied to every source, concept, equation, diagram, and interpretive note. |
| Pending | Not yet meaningfully implemented. |
| Needs Verification | Candidate material exists but requires scan, citation, OCR, or mathematical review. |
| Future Scope | Important, but intentionally held until the Steinmetz foundation is stronger. |

## Current Snapshot

| Area | Current State |
| --- | --- |
| Public site | Astro/Starlight documentation site with GitHub Pages deployment workflow. |
| Live URL | https://truemodeloftheworld.github.io/Charles-Proteus-Steinmetz-Texts-AI-Decoded/ |
| Seeded Steinmetz records | Eleven source records in `sources/source_catalog.json`. |
| Expanded bibliography intake | `sources/steinmetz_bibliography_manifest.json` maps the current Wikipedia works list into seeded, planned, and verification-needed records. |
| Patent intake | `sources/steinmetz_patents/patent_register.json` seeds the Wikipedia-listed patent examples and marks the full 200-plus patent catalog as an authority-pass milestone. |
| First canonical source | `Radiation, Light and Illumination` by Charles Proteus Steinmetz. |
| Public pages | Source library, source dashboard, concepts, equations, diagrams, comparisons, glossary, hidden gems, research questions, roadmap, and tools. |
| Original scan crops | Fifteen promoted crops: five from `Radiation, Light and Illumination`, four from `Alternating Current Phenomena`, and six from `Transient Electric Phenomena and Oscillations`, with manifests and checksums. |
| Modern redraw sheets | Source-keyed redraw sheets now exist for AC symbolic-method geometry and transient condenser-response behavior. |
| Reader UX layer | Global reader controls now provide source-only filtering, page-local ask/search, translation shortcuts, diagram lightbox viewing, readable source/code blocks, and a Start Reading route for non-specialist entry. |
| Original-source access | Source pages now expose Archive.org scan links, OCR links, and inline scan readers where stable archive IDs exist. |
| Source text browser | Generated public reader pages now expose 304 processed chapters, lectures, sections, and report divisions under `site/src/content/docs/source-texts/`. |
| Book coverage atlas | Generated book-level coverage pages now expose all 11 seeded sources under `site/src/content/docs/book-coverage/`, with every processed section linked to source text and chapter workbench pages. |
| Chapter workbench | Generated research maps now expose 304 processed sections under `site/src/content/docs/chapter-workbench/`, joining source links, theme snippets, concept/glossary hits, equation candidates, figure candidates, quote candidates, modern prompts, interpretive boundaries, and promotion checklists. |
| Concept concordance | Generated concept-trace pages now expose 77 curated terms and concepts under `site/src/content/docs/concept-concordance/`, linking every hit back to source text and chapter workbench pages. |
| Completion audit | `processed/completion_audit.json` and a public completion-audit page now measure source-by-source readiness for canonical review. |
| World-class criteria | Public expert finishing criteria now define what the archive must do before it can honestly call itself definitive. |
| Scholarly exports | `CITATION.cff`, `processed/citation_index.json`, CSL JSON, BibTeX, public `/data/` exports, and a data manifest now publish reusable research data with review-state labels intact. |
| Review governance | Editorial policy, canonical review workflow, contribution rules, and GitHub issue templates now guide source, equation, and diagram promotion. |
| World-class ledgers | `processed/notation_ledger.json`, `processed/diagram_provenance_ledger.json`, `processed/schema_reference.json`, and `processed/expert_review_packets.json` now route notation, diagram, data, patent, concept, and interpretive-boundary review. |
| Publication readiness | `processed/release_readiness.json`, `processed/accessibility_audit.json`, `processed/edition_comparison_index.json`, and `processed/patent_theory_bridge.json` now track release levels, accessibility, edition collation, and patent-to-theory work. |
| Canonical verification workbench | `processed/canonical_verification_workbench.json`, equation/figure/patent verification queues, and four public roadmap pages now turn priority candidates into scan-check work cards. |
| Claim attribution ledger | `processed/claim_attribution_ledger.json` now classifies facts, OCR candidates, equations, modern translations, figures, patents, and future interpretive layers by source and claim type. |
| Evidence ledger | `processed/evidence_ledger.json` now indexes 3,345 traceability records across sources, concepts, glossary terms, equations, figures, quotes, and promoted scan crops. |
| Chapter atlas | `processed/chapter_atlas.json` now maps 304 chapter, lecture, section, and report-section records to OCR/PDF-text theme counts for research routing. |
| New deep-decoding pages | Public pages now include General Lectures on high-frequency surges, Elementary Lectures on the electric field, Theoretical Elements on fields of force and hysteresis/effective resistance, Electric Apparatus on the hysteresis motor, Relativity and Space on the gravitational field, America and the New Epoch on industrial government as historical context, and Commonwealth Edison on reactors and synchronism. |
| Research indexes | Generated JSON indexes for sources, concepts, equations, figures, glossary terms, and quotes under `processed/`. |
| Verification control | `VERIFICATION_QUEUE.md` tracks the next scan-check and promotion work. |

## Original Goal Matrix

| Original Goal | Status | Notes |
| --- | --- | --- |
| Build a GitHub repo and public knowledge base | Done | Repo structure, Pages workflow, and public site are in place. |
| Preserve raw sources, OCR, scans, metadata, and checksums | Started | First source and multi-source records exist. More checksum and custody work is needed source by source. |
| Process the first Steinmetz book as canonical example | Started | `Radiation, Light and Illumination` has OCR, chapter candidates, full generated lecture text pages, diagrams, first deep lecture page, figures, concepts, and equations. |
| Scale to multiple Steinmetz books | Started | AC, transient, engineering mathematics, theoretical elements, elementary lectures, General Lectures, Electric Apparatus, America and the New Epoch, Relativity and Space, and Commonwealth Edison are seeded; Theoretical Elements, America, and Commonwealth Edison now have source-specific structural parsers, and all processed sections have generated public text-reader pages. |
| Account for more notable Steinmetz works | Started | Wikipedia bibliography intake now tracks books, lecture collections, pamphlets, and papers beyond the seeded source catalog; four additional book-level OCR seeds were added. |
| Include patents in detail | Started | A seeded patent register covers the Wikipedia-listed examples with Google Patents links, technical digests, diagram targets, and completion rules; full 200-plus catalog remains pending authority verification. |
| Extract every major concept | Started | Public concept encyclopedia exists; generated concept concordance now traces 77 concepts across all processed sections; scan-grounded promotion continues. |
| Extract equations and derivations | Started | Equation candidates, public math pages, first twelve-equation canon, and a candidate Steinmetz hysteresis-law page now exist; scan verification and worked examples continue. |
| Extract diagrams and figures | Started | RLI, AC Chapter V, and transient crops exist; AC and transient redraw sheets now pair modern reading aids with original crops. |
| Build glossary of forgotten electrical language | Started | Glossary index plus source-located pages for condensive reactance, wattless component, imaginary unit `j`, electrostatic capacity, counter e.m.f., and effective resistance. |
| Compare Steinmetz with modern EE | Started | Radiation and AC symbolic method comparisons exist. Needs broader equation-by-equation comparison. |
| Compare Steinmetz with Tesla-era science | Started | Introductory Tesla-era comparison and transient page exist. Needs Tesla source anchoring before stronger claims. |
| Include Ken Wheeler-style ether-field readings | Started | Reading guide and concept sections exist. Must remain visibly interpretive. |
| Build hidden gems index | Started | Section exists. Needs many scan-verified entries. |
| Build research questions section | Started | Section exists and should evolve after each source pass. |
| Build interactive tools | Started | Frequency/wavelength, AC waveform/harmonics, impedance, phasor/symbolic-form, power-factor, hysteresis-loss, transient RLC condenser-discharge, and lightning/surge traveling-wave tools exist. |
| Build repeatable data pipeline | Started | OCR seeding, image extraction, crop tooling, and index generation exist. |
| Build evidence ledger, chapter atlas, and chapter workbench | Done | `processed/evidence_ledger.json`, `processed/chapter_atlas.json`, `processed/chapter_workbench.json`, and public explanatory/generated pages are live. |
| Build concept concordance | Done as generated research layer | `processed/concept_concordance.json` and public concept-trace pages are live as candidate source-location aids. |
| Build completion audit and final scholarly gates | Started | `processed/completion_audit.json`, public completion audit, and world-class completion criteria are live. |
| Avoid hallucination | Repeating | Labels and verification queue are active. This must be enforced forever. |

## Expert Additions Beyond The Original Charter

These are new workstreams added after the foundation was built. They define what must happen for the archive to become world-class rather than merely large.

| Added Workstream | Status | Why It Matters |
| --- | --- | --- |
| Critical-edition editorial policy | Started | OCR correction, uncertain readings, page breaks, spelling variants, and math transcription now have a public rule page. |
| Citation/export system | Started | Researchers can export BibTeX, CSL JSON, stable source IDs, recommended citations, and public JSON data. |
| Canonical review workflow | Started | Candidate -> source-located -> scan-verified -> mathematically reviewed -> context reviewed -> canonical is public and tied to issue templates. |
| Mathematical errata and notation ledger | Started | The first generated notation ledger maps source and modern symbols across the canonical equation seed set. |
| Diagram provenance ledger | Started | The generated provenance ledger maps 15 original crops and 9 modern redraws with source, asset, and review-state fields. |
| Edition comparison layer | Started | A generated edition-collation queue now identifies source edition review work. |
| Patent-to-theory bridge | Started | A generated patent bridge links seeded patents to concepts, diagram targets, and theory-review actions. |
| Accessibility and reading-quality audit | Started | Generated structural audit covers alt text, tables, iframes, and manual review gates. |
| Research API and data export | Started | Public data manifest, reusable JSON exports, citation index, CSL JSON, and BibTeX now generate. |
| Canonical verification workbench | Started | Equation OCR snippets, original crop cards, and patent authority-review cards now route scan-check work item by item. |
| Claim attribution and source isolation | Started | A generated ledger now keeps source custody, Steinmetz wording, math candidates, modern translations, diagrams, patents, and interpretation layers separate for future multi-author expansion. |
| Contributor governance | Started | Contribution rules and source/equation/diagram review templates are now present. |
| Independent expert review packets | Started | Six generated packets route source custody/OCR, equation notation, diagram provenance, concepts/glossary, patents, and interpretive-boundary review. |
| Definitive release levels | Started | Named release levels now distinguish foundation, source coverage, scan verification, equation canon, diagram canon, patent authority, and definitive release. |

## Extraction Requirements From The Original Charter

| Requirement | Status | Next Promotion Step |
| --- | --- | --- |
| 1. Every major concept Steinmetz explains | Started | Expand source-by-source concept index and promote pages only after source locations are recorded. |
| 2. Every important equation and derivation | Started | First twelve-equation canon is published as source-located candidate data and pages; next step is scan verification and more worked examples. |
| 3. Every diagram, figure, circuit, waveform, and geometric representation | Started | Complete second-pass review of AC and transient crops, then continue extracting line, surge, hysteresis, and apparatus figures. |
| 4. Every important definition of electrical terms | Started | Add exact Steinmetz wording to concept and glossary pages. |
| 5. Every unusual, obsolete, or nonmodern scientific term | Started | Promote `electrostatic capacity`, `counter-electromotive force`, and `effective resistance`. |
| 6. Statements on ether, fields, magnetism, dielectricity, hysteresis, reactance, impedance, transients, AC, complex quantities, symbolic methods, and waves | Started | Build one indexed evidence file per theme with page references. |
| 7. Where Steinmetz differs from modern textbook language | Started | Continue comparison pages, especially for symbolic method, reactance, admittance, and transients. |
| 8. Where Steinmetz anticipates, clarifies, or conflicts with modern EE | Started | Tie claims to exact quotes and modern formulas. |
| 9. Connections to Tesla-era electrical science | Started | Gather Tesla source passages before making stronger comparative pages. |
| 10. Connections to Ken Wheeler interpretations | Started | Keep as labeled interpretive readings with fact/interpretation/speculation separated. |
| 11. Hidden gems | Started | Convert priority quotes into scan-verified entries with research questions. |

## Layer Requirements

Each mature concept, equation, diagram, or comparison page should include these layers:

| Layer | Status | Rule |
| --- | --- | --- |
| Steinmetz original wording and meaning | Started | Quote sparingly and cite exact source location. |
| Modern electrical engineering interpretation | Started | Use modern terms only after preserving Steinmetz's framing. |
| Mathematical breakdown | Started | Preserve original notation before translating it. |
| Plain-English explanation | Started | Clarify without flattening the technical content. |
| Historical context | Started | Mark as historical note and source later. |
| Ether-field interpretive reading | Started | Label as interpretation, not historical proof. |
| Tesla-era comparison | Started | Label overlap, divergence, and open questions. |
| Current status of the concept | Started | Say whether it is still used, renamed, absorbed, or obsolete. |

## Repository Architecture Tracker

| Directory | Status | Role |
| --- | --- | --- |
| `sources/` | Done, expanding | Raw source texts, public-domain records, scans, OCR custody, manifests. |
| `sources/steinmetz_patents/` | Started | Patent register, authority workflow, and future raw patent custody folders. |
| `processed/` | Done, expanding | Cleaned OCR, chapter candidates, JSON indexes, figure/equation/glossary candidates, generated annotations, and crosslink indexes. |
| `analysis/` | Started | Deep commentary by book, chapter, concept, equation, and diagram. |
| `concepts/` | Started | Repo-native encyclopedia source material. |
| `math/` | Started | Equation catalogs, canonical equation set, derivations, notation translations, worked examples. |
| `diagrams/` | Started | Original crops, manifests, public copies, modern redraws. |
| `comparisons/` | Started | Mainstream, Steinmetz, Tesla-era, and ether-field comparison notes. |
| `glossary/` | Started | Historical terminology and modern equivalents. |
| `hidden-gems/` | Started | Overlooked statements and follow-up questions. |
| `research-questions/` | Started | Living research agenda. |
| `pipeline/` | Started | Repeatable processing scripts and extraction workflow. |
| `templates/` | Started | Page templates for future promotions. |
| `site/` | Done, expanding | Public website and interactive tools. |

## Website Section Tracker

| Section From Charter | Status | Current Location |
| --- | --- | --- |
| 1. Home | Done | `site/src/content/docs/index.mdx`, with `site/src/content/docs/start-reading.mdx` as a guided reader entry |
| 2. Who Was Steinmetz? | Done | `site/src/content/docs/who-was-steinmetz.mdx` |
| 3. Why Steinmetz Matters | Done | `site/src/content/docs/why-steinmetz-matters.mdx` |
| 4. Source Library | Done, expanding | `site/src/content/docs/source-library/index.mdx`, source pages with source-access readers, generated book coverage pages, generated source-text browser pages, generated chapter workbench pages, and generated concept concordance pages |
| 4a. Expanded Bibliography Intake | Started | `site/src/content/docs/source-library/bibliography-intake.mdx` |
| 4b. Steinmetz Patent Register | Started | `site/src/content/docs/sources/steinmetz-patents/index.mdx` |
| 4c. Source Text Browser | Started | `site/src/content/docs/source-texts/` generated from processed chapter records |
| 4d. Book Coverage Atlas | Started | `site/src/content/docs/book-coverage/` generated from processed workbench records, with one index and one source-level coverage page per seeded source |
| 4e. Chapter Research Workbench | Started | `site/src/content/docs/chapter-workbench/` generated from processed chapter, concept, glossary, equation, figure, and quote records |
| 4f. Concept Concordance | Started | `site/src/content/docs/concept-concordance/` generated from processed text sections and curated concept vocabulary |
| 4g. Completion Audit | Started | `site/src/content/docs/roadmap/completion-audit.mdx` generated from source readiness gates |
| 4h. Citation And Data Export | Started | `site/src/content/docs/roadmap/citation-and-data-export.mdx`, `CITATION.cff`, public `/data/` exports, BibTeX, and CSL JSON generated |
| 4i. Editorial Policy And Review Workflow | Started | `site/src/content/docs/roadmap/editorial-policy.mdx`, `site/src/content/docs/roadmap/canonical-review-workflow.mdx`, contribution rules, and GitHub issue templates |
| 4j. Notation, Provenance, Schema, And Review Packets | Started | `site/src/content/docs/roadmap/notation-ledger.mdx`, `diagram-provenance-ledger.mdx`, `schema-reference.mdx`, and `expert-review-packets.mdx` generated |
| 4k. Canonical Verification Workbench | Started | `site/src/content/docs/roadmap/canonical-verification-workbench.mdx`, `equation-verification-queue.mdx`, `figure-verification-queue.mdx`, and `patent-verification-queue.mdx` generated |
| 4l. Claim Attribution Ledger | Started | `site/src/content/docs/roadmap/claim-attribution-ledger.mdx` and `processed/claim_attribution_ledger.json` generated |
| 5. Book-by-Book Deep Decoding | Started | RLI, AC, transient, engineering math, Theoretical Elements, Electric Apparatus, General Lectures, Relativity and Space, Commonwealth Edison, historical-context pages, and generated book coverage pages |
| 6. Concept Encyclopedia | Started | `site/src/content/docs/concepts/` |
| 7. Mathematics of Steinmetz | Started | `site/src/content/docs/mathematics/` |
| 8. Diagram Archive | Started | `site/src/content/docs/diagrams/` with global lightbox viewing |
| 9. Steinmetz vs Modern EE | Started | `site/src/content/docs/comparisons/` |
| 10. Steinmetz and Tesla-Era Electrical Science | Started | `site/src/content/docs/comparisons/tesla-era-electrical-science.mdx` |
| 11. Steinmetz and Ken Wheeler-Style Field Interpretation | Started | `site/src/content/docs/comparisons/ether-field-reading-guide.mdx` |
| 12. Hidden Gems Index | Started | `site/src/content/docs/hidden-gems.mdx` |
| 13. Glossary of Forgotten Electrical Language | Started | `site/src/content/docs/glossary/` |
| 14. Research Questions | Started | `site/src/content/docs/research-questions.mdx` |
| 15. Interactive Tools | Started | `site/src/content/docs/tools/index.mdx`, including wave relation, AC waveform/harmonics, impedance, phasor/symbolic form, power factor, hysteresis loss, transient RLC response, and lightning/surge traveling waves. |
| Reader filtering and multilingual access | Started | Site-wide source-only filter, page-local ask/search, Google Translate shortcuts, lightbox diagram viewer, and readable source/code transcript blocks. |
| 16. Data Pipeline | Started | `pipeline/` and `processed/source_processing_status.md` |

## Data Pipeline Tracker

| Pipeline Function | Status | Current Implementation |
| --- | --- | --- |
| Ingest PDFs or text files | Started | Local source folders and `sources/source_catalog.json`. |
| Run OCR if needed | Pending | External OCR workflow still needs standardization. |
| Split by book/chapter/page | Started | `seed_source_from_ocr.py`, `extract_pdf_text.py`, and source-specific parsers for `Theoretical Elements`, `America and the New Epoch`, and `Commonwealth Edison`. |
| Extract equations | Started | Candidate extraction in generated indexes. |
| Extract figures | Started | PyMuPDF image extraction and crop tooling. |
| Create metadata | Started | Source catalog plus crop manifests. |
| Generate concept tags | Started | Research index builder. |
| Generate summaries | Started | Public source and chapter pages, mostly curated. |
| Generate public source text readers | Started | `generate_source_text_pages.py` builds 316 public source-text pages from processed chapter records. |
| Generate book coverage atlas pages | Started | `generate_book_coverage_atlas.py` builds 12 public book-coverage pages plus `processed/book_coverage_atlas.json`. |
| Generate chapter workbench pages | Started | `generate_chapter_workbench.py` builds 316 public workbench pages plus `processed/chapter_workbench.json`. |
| Generate concept concordance pages | Started | `generate_concept_concordance.py` builds 78 public concept-concordance pages plus `processed/concept_concordance.json`. |
| Generate completion audit | Started | `generate_completion_audit.py` builds `processed/completion_audit.json` and the public completion audit page. |
| Generate scholarly exports | Started | `generate_scholarly_exports.py` builds `CITATION.cff`, citation JSON, CSL JSON, BibTeX, public `/data/` exports, a data manifest, and the public citation/export page. |
| Generate world-class scholarly ledgers | Started | `generate_world_class_artifacts.py` builds notation, diagram provenance, schema reference, and expert review packet JSON plus public roadmap pages. |
| Generate publication readiness controls | Started | `generate_publication_readiness.py` builds release readiness, accessibility audit, edition comparison, and patent bridge JSON plus public roadmap pages. |
| Generate canonical verification queues | Started | `generate_verification_workbench.py` builds equation OCR-snippet queues, original-figure crop review cards, patent authority-review cards, and public roadmap pages. |
| Generate claim attribution ledger | Started | `generate_claim_attribution_ledger.py` classifies evidence, canonical equations, modern translations, diagrams, and patents by claim type and interpretation layer. |
| Generate glossary candidates | Started | `processed/glossary_index.json`. |
| Generate equation candidates | Started | `processed/equation_index.json`. |
| Generate diagram candidates | Started | `processed/figure_index.json`. |
| Store outputs as JSON and Markdown | Started | `processed/` plus site MDX pages. |
| Preserve source page references | Started | Active rule; many candidates still need page verification. |

## Required Data Files

| Data File | Status |
| --- | --- |
| `source_manifest.json` | Started through source catalog and per-source manifests. |
| `book_metadata.json` | Started in source records, needs per-book promotion. |
| `chapters.json` | Started in processed source outputs. |
| `equations.json` | Started through `processed/equation_index.json`. |
| `canonical_equations.json` | Started with the first twelve source-located equation records. |
| `figures.json` | Started through `processed/figure_index.json` and crop manifests. |
| `concepts.json` | Started through `processed/concept_index.json`. |
| `glossary.json` | Started through `processed/glossary_index.json`. |
| `quotes.json` | Started through `processed/quote_index.json`. |
| `annotations.json` | Started through per-source files and generated `processed/annotations_index.json`. |
| `crosslinks.json` | Started through per-source files and generated `processed/crosslinks_index.json`. |
| `evidence_ledger.json` | Done as the archive-wide traceability layer for source claims, candidates, and promoted assets. |
| `chapter_atlas.json` | Done as the archive-wide OCR/PDF-text theme routing map for chapters, lectures, sections, and report divisions. |
| `book_coverage_atlas.json` | Started as the generated source-by-source coverage map with section links, theme totals, concept density, glossary density, and candidate counts. |
| `chapter_workbench.json` | Done as the archive-wide generated workbench index joining section text, theme routing, term hits, equations, figures, quotes, links, and promotion status. |
| `concept_concordance.json` | Done as the archive-wide generated concept-trace index across processed source text. |
| `completion_audit.json` | Started as the source-by-source readiness audit for canonical review. |
| `citation_index.json` | Started as the archive-wide citation record set for project and source records. |
| `citation_index.csl.json` | Started as the CSL JSON export for citation managers. |
| `citation_index.bib` | Started as the BibTeX export for citation managers. |
| `notation_ledger.json` | Started as the source/modern symbol review ledger for the first canonical equation set. |
| `diagram_provenance_ledger.json` | Started as the provenance ledger for original crops and modern redraws. |
| `schema_reference.json` | Started as the descriptive schema reference for processed and public exports. |
| `expert_review_packets.json` | Started as the routed expert-review bundle index. |
| `release_readiness.json` | Started as the named publication release-level map. |
| `accessibility_audit.json` | Started as the structural accessibility scan and manual gate list. |
| `edition_comparison_index.json` | Started as the edition-collation queue for seeded sources. |
| `patent_theory_bridge.json` | Started as the patent-to-concept and patent-to-theory bridge. |
| `canonical_verification_workbench.json` | Started as the queue index for equation, figure, and patent verification work. |
| `equation_verification_queue.json` | Started as the scan-check queue for canonical equation candidates, including OCR snippets and source/workbench links. |
| `figure_verification_queue.json` | Started as the scan-crop review queue for original Steinmetz figures. |
| `patent_verification_queue.json` | Started as the authority PDF, claim, drawing, and theory-bridge queue for seeded patents. |
| `claim_attribution_ledger.json` | Started as the source-isolation ledger for facts, candidates, translations, diagrams, patents, and interpretive boundaries. |
| `site/public/data/manifest.json` | Started as the public data export manifest. |
| generated `source-texts/` pages | Started with 304 text-section pages plus source indexes, marked candidate and pagefind-disabled. |
| generated `book-coverage/` pages | Started with one corpus index and 11 source-level coverage maps. |
| generated `chapter-workbench/` pages | Started with 304 section workbench pages plus source indexes and a corpus index. |
| generated `concept-concordance/` pages | Started with 77 concept pages plus a corpus index. |
| generated completion audit page | Started with source-by-source readiness gates and next actions. |
| `steinmetz_bibliography_manifest.json` | Started with Wikipedia-derived works intake and source-processing status. |
| `patent_register.json` | Started with Wikipedia-listed patent examples and Google Patents authority links. |

## Near-Term Milestone Sequence

| Milestone | Work Items | Definition Of Done |
| --- | --- | --- |
| M1. Public trust hardening | Master tracker, public tracker, verification queue, Pages, build checks. | A new contributor can see exactly what exists and what remains candidate. |
| M2. RLI scan-verified anchor | Verify spectrum table, Figs. 14, 15, 18, 19, and page references. | RLI first-source pages can be marked reviewed where applicable. |
| M3. AC symbolic canon | Verify `j`, rectangular components, `Z = r + jx`, reactance, admittance, conductance, susceptance, and power factor. | AC symbolic method section now has a first canonical equation set and Chapter V crops; scan verification remains. |
| M4. Transient canon | Verify permanent/transient terms, RLC oscillation, critical resistance, decrement, and surge figures. | Transient theory has canonical equation, diagram, and interactive response pages. |
| M5. Diagram expansion | Extract and publish original AC and transient figures with manifests. | Started with AC Chapter V and first transient condenser/decrement figures; source-keyed redraw sheets added; next step is surge, line, hysteresis, and apparatus figures. |
| M6. Glossary expansion | Promote key older terms with source usage and modern equivalents. | Started with source-located pages for electrostatic capacity, counter e.m.f., and effective resistance; concept pages now cover conductance, susceptance, and dielectric loss. |
| M7. Pipeline refinement | Improve parsers, page maps, OCR cleanup, annotation, crosslink, evidence, and chapter-atlas JSON. | Aggregate annotation, crosslink, evidence ledger, and chapter atlas now generate; Theoretical Elements, America, and Commonwealth Edison now have source-specific parsers; next step is scan verification and page-map refinement. |
| M7A. Public text coverage | Generate public reader pages for every processed chapter and section. | Generated 316 source-text pages, including 304 processed text-section pages and 12 index pages. |
| M7B. Book coverage atlas | Generate source-level coverage maps so every seeded book has a non-shell representation. | Generated 12 book-coverage pages, including one corpus index and 11 source maps, backed by `processed/book_coverage_atlas.json`. |
| M7C. Chapter research coverage | Generate a source-linked research map for every processed chapter and section. | Generated 316 chapter-workbench pages, including 304 section maps and 12 index pages, backed by `processed/chapter_workbench.json`. |
| M7D. Concept trace coverage | Generate cross-source concept concordance pages from the full processed text corpus. | Generated 78 concept-concordance pages, including 77 concept pages and a corpus index, backed by `processed/concept_concordance.json`. |
| M7E. Completion audit coverage | Generate source-by-source readiness gates and final scholarly criteria. | Generated `processed/completion_audit.json`, public completion audit, and world-class criteria page. |
| M7F. Scholarly export and review governance | Generate citation/data exports and public review rules. | Generated `CITATION.cff`, citation index, BibTeX, CSL JSON, public data manifest, editorial policy, canonical review workflow, and GitHub review templates. |
| M7G. Critical scholarly ledgers | Generate notation, diagram provenance, schema, and expert review packet controls. | Generated four processed ledgers and four public roadmap pages for review routing. |
| M7H. Publication readiness controls | Generate release, accessibility, edition, and patent bridge controls. | Generated four processed readiness indexes and four public roadmap pages. |
| M7I. Canonical verification workbench | Generate scan-check queues for equations, figures, and patents. | Generated four processed queue indexes and four public roadmap pages with source links and OCR snippets. |
| M7J. Claim attribution ledger | Generate source-isolation and interpretation-layer controls. | Generated a 3,380-record attribution ledger and public roadmap page. |
| M8. Expanded Steinmetz source intake | Add notable works and patents to control files, public pages, and verification queue. | Wikipedia bibliography and patent examples are now tracked; next step is acquisition and source-by-source processing. |
| M9. Future multi-author architecture | Prepare separate source domains for Tesla, Dollard, Walter Russell, and others. | Wider scope can be added without blending fact, comparison, and interpretation. |

## Multi-Author Future Scope

The current archive should remain Steinmetz-first. The site architecture should eventually support other research domains such as Nikola Tesla, Eric Dollard, Walter Russell, and related figures, but only after the source model is strong enough to keep each author's claims separate.

Future rule: never merge an author's position into Steinmetz's. Use comparison pages, explicit citations, and labeled interpretive sections.

The future architecture is now tracked publicly at `site/src/content/docs/roadmap/future-codex-architecture.mdx`. It is intentionally downstream of the Steinmetz-first milestone.

## Operating Rules

- Keep raw source custody visible before commentary.
- Keep original notation before modern translation.
- Keep diagrams tied to source page, crop manifest, and checksum where possible.
- Keep source fact, modern explanation, mathematical reconstruction, historical note, interpretive reading, speculative connection, and needs-verification labels visible.
- Do not promote OCR-derived claims to reviewed status without scan verification.
- Do not use Tesla, Wheeler, Dollard, or ether-field language as proof of Steinmetz's intent unless Steinmetz explicitly says it.
- Do not erase alternative interpretations; label them.
- Do not write shallow summary pages when a structured source page is needed.

## Update Log

| Commit | Contribution |
| --- | --- |
| `8747b5b` | Built the first Steinmetz Decoded research archive foundation. |
| `2aa209a` | Added PDF image extraction pipeline and first scan figure crop. |
| `58497a0` | Configured GitHub Pages deployment. |
| `d7d7866` | Added research index pipeline and original Steinmetz figure crops. |
| `90d0ed6` | Expanded AC and transient research codex pages. |
| `1e77f25` | Added master project tracker and power factor tool. |
| `26cff7e` | Added original AC symbolic method figure set. |
| `ee7c982` | Added original transient figure set. |
| `fa62a7d` | Promoted source-located glossary terms. |
| `d87468b` | Generated annotation and crosslink indexes. |
| `4f023b9` | Added first canonical equation set. |
| `a7bc0fe` | Added transient RLC explorer. |
| `d6078ef` | Added source-keyed diagram redraw sheets. |
| `5173d6e` | Added phasor symbolic form explorer. |
| `b7c70a7` | Added hysteresis loss explorer and Steinmetz-law candidate page. |
| `131b7b9` | Added AC waveform harmonics explorer and wave-shape concept page. |
| `b3f8d41` | Added lightning surge traveling-wave explorer and surge concept page. |
| `6330cc6` | Added expanded Steinmetz bibliography intake, seeded patent register, and future codex architecture page. |
| `2d678d1` | Seeded four additional Steinmetz OCR sources and added public source entry pages. |
| `646e3a2` | Added source reader UX, original-source access, reader filters, translation shortcuts, and diagram lightbox. |
| `5ad0fa6` | Added source-specific parsers for Theoretical Elements and America, expanded the chapter atlas, and published new deep-decoding pages. |
| `f920f7d` | Extracted Commonwealth Edison PDF text, generated page-map and report-section catalogs, added reactor/synchronism pages, and updated indexes. |
| `5532083` | Added the generated source-text browser for all processed chapters, lectures, sections, and report divisions. |
| `98d531d` | Added the generated chapter research workbench for all processed sections. |
| `d5c69f6` | Added the generated concept concordance across the processed Steinmetz corpus. |
| `feb0145` | Added the generated completion audit and world-class finishing criteria. |
| `62967cd` | Added scholarly citation/data exports, editorial policy, canonical review workflow, and issue templates. |
| `69ed6ec` | Added notation, diagram provenance, schema reference, and expert review packet ledgers. |
| pending commit | Added publication readiness, accessibility, edition comparison, and patent-to-theory bridge controls. |

## Next Work Queue

1. Verify RLI page anchors and promote the first reviewed source claims.
2. Complete second-pass review of original AC Chapter V figure crops and refine the symbolic-method redraw sheet.
3. Complete second-pass review of original transient figure crops and refine the condenser-response redraw sheet.
4. Scan-verify the first 12 canonical equations and expand each with exact page anchors and additional worked examples.
5. Scan-verify glossary term pages for `electrostatic capacity`, `counter-electromotive force`, and `effective resistance`, then promote dielectric and hysteresis terms.
6. Refine generated annotation and crosslink indexes with page maps, confidence levels, and curated canonical links.
7. Add advanced interactive tools: multi-section surge lattice diagram, vector phasor animation, and source-specific worked calculators.
8. Scan-verify the Commonwealth Edison report, crop Appendix Figure 1, and promote corrected synchronizing-power equations.
9. Use the generated book coverage atlas, source-text browser, chapter workbench, and concept concordance to promote the next batch of chapter-by-chapter deep readings without losing full-text coverage.
10. Acquire and process high-priority bibliography intake sources: `On the Law of Hysteresis`, `Complex Quantities and Their Use in Electrical Engineering`, `The General Equations of the Electric Circuit`, `Mechanical Forces in Magnetic Fields`, and first-edition variants where available.
11. Complete the Steinmetz patent authority pass, download patent PDFs/drawings, and create one verified patent page per patent.
12. Use the new citation/data exports, scholarly ledgers, and review templates to prepare external expert review packets.
13. Add the remaining world-class apparatus: formal JSON schemas, deeper accessibility testing, completed edition collation, verified patent dossiers, and named release publication notes.
