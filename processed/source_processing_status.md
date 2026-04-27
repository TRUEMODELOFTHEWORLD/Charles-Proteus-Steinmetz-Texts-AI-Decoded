# Source Processing Status

This dashboard is generated from the processed JSON catalogs. Counts describe custody and review state; they are not claims that every OCR-derived candidate is correct.

## Corpus Table

| Source | Status | Chapters | Equations | Figures | Original Crops | Glossary | Quotes | Next Action |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Radiation, Light and Illumination | lecture splits, candidate equations, figures, concepts, glossary, quotes | 13 | 300 | 98 | 5 | 12 | 3 | Triage candidate equations into canonical, false positive, and needs-review groups. |
| Elementary Lectures on Electric Discharges, Waves and Impulses, and Other Transients | lecture splits and candidate catalogs from OCR | 10 | 300 | 16 | 0 | 12 | 0 | Promote scan-verified figure crops and anchor high-value figures to pages. |
| Engineering Mathematics: A Series of Lectures Delivered at Union College | chapter splits and candidate catalogs from OCR | 6 | 300 | 9 | 0 | 12 | 0 | Promote scan-verified figure crops and anchor high-value figures to pages. |
| Theory and Calculation of Alternating Current Phenomena | chapter splits and candidate catalogs from OCR; edition alignment needs review | 37 | 300 | 145 | 4 | 12 | 0 | Triage candidate equations into canonical, false positive, and needs-review groups. |
| Theoretical Elements of Electrical Engineering | OCR and candidate catalogs; structural split needs custom part/section parser | 0 | 300 | 10 | 0 | 12 | 0 | Review structural parser; no chapter or lecture records were found. |
| Theory and Calculation of Transient Electric Phenomena and Oscillations | chapter splits and candidate catalogs from OCR; multi-section numbering requires review | 58 | 300 | 1 | 6 | 12 | 0 | Triage candidate equations into canonical, false positive, and needs-review groups. |
| Investigation of Some Trouble in the Generating System of the Commonwealth Edison Co. | local PDF copied; OCR and bibliographic verification pending | 0 | 0 | 0 | 0 | 0 | 0 | Run OCR, create bibliographic metadata, then seed candidate catalogs. |

## Quality Rules

- Candidate records are generated from OCR and must not be treated as canonical without scan review.
- Promoted original crops are scan-derived assets with a crop manifest and checksum.
- Concept and glossary counts are discovery aids, not interpretive conclusions.
- Ether-field and Tesla-era links belong in labeled interpretive or comparative pages, not in raw source indexes.
