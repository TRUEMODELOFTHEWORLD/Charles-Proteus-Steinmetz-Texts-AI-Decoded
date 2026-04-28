# Source Processing Status

This dashboard is generated from the processed JSON catalogs. Counts describe custody and review state; they are not claims that every OCR-derived candidate is correct.

## Corpus Table

| Source | Status | Chapters | Equations | Figures | Original Crops | Glossary | Quotes | Next Action |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Radiation, Light and Illumination | lecture splits, candidate equations, figures, concepts, glossary, quotes | 13 | 300 | 98 | 5 | 12 | 3 | Triage candidate equations into canonical, false positive, and needs-review groups. |
| Elementary Lectures on Electric Discharges, Waves and Impulses, and Other Transients | lecture splits and candidate catalogs from OCR | 10 | 300 | 16 | 0 | 12 | 0 | Promote scan-verified figure crops and anchor high-value figures to pages. |
| Engineering Mathematics: A Series of Lectures Delivered at Union College | chapter splits and candidate catalogs from OCR | 6 | 300 | 9 | 0 | 14 | 0 | Promote scan-verified figure crops and anchor high-value figures to pages. |
| Theory and Calculation of Alternating Current Phenomena | chapter splits and candidate catalogs from OCR; edition alignment needs review | 37 | 300 | 145 | 4 | 15 | 0 | Triage candidate equations into canonical, false positive, and needs-review groups. |
| Theoretical Elements of Electrical Engineering | source-specific part/section split and candidate catalogs from OCR | 114 | 300 | 10 | 0 | 12 | 0 | Promote scan-verified figure crops and anchor high-value figures to pages. |
| Theory and Calculation of Transient Electric Phenomena and Oscillations | chapter splits and candidate catalogs from OCR; multi-section numbering requires review | 58 | 300 | 1 | 6 | 12 | 0 | Triage candidate equations into canonical, false positive, and needs-review groups. |
| General Lectures on Electrical Engineering | Internet Archive OCR downloaded; ordinal lecture parser generated candidate catalogs | 17 | 134 | 14 | 0 | 12 | 0 | Promote scan-verified figure crops and anchor high-value figures to pages. |
| America and the New Epoch | source-specific historical chapter split and candidate catalogs from OCR | 18 | 21 | 0 | 0 | 9 | 0 | Scan-verify chapter starts and keep historical/social claims separate from electrical theory. |
| Theory and Calculation of Electric Apparatus | Internet Archive OCR downloaded; chapter splits and candidate catalogs generated | 22 | 300 | 13 | 0 | 12 | 0 | Promote scan-verified figure crops and anchor high-value figures to pages. |
| Four Lectures on Relativity and Space | Internet Archive OCR downloaded; lecture splits and candidate catalogs generated | 4 | 170 | 19 | 0 | 12 | 0 | Promote scan-verified figure crops and anchor high-value figures to pages. |
| Investigation of Some Trouble in the Generating System of the Commonwealth Edison Co. | embedded PDF text extracted; page map, report sections, candidate equations, figures, concepts, glossary, quotes, annotations, and crosslinks generated | 5 | 220 | 1 | 0 | 12 | 5 | Promote scan-verified figure crops and anchor high-value figures to pages. |

## Quality Rules

- Candidate records are generated from OCR and must not be treated as canonical without scan review.
- Promoted original crops are scan-derived assets with a crop manifest and checksum.
- Concept and glossary counts are discovery aids, not interpretive conclusions.
- Ether-field and Tesla-era links belong in labeled interpretive or comparative pages, not in raw source indexes.
