# Processing Pipeline

The pipeline turns raw Steinmetz source material into reviewable data.

It is intentionally transparent: every machine-produced output should be inspectable, reproducible, and marked with a review status.

## Stages

1. **Custody**
   - Copy or link raw PDFs, scans, OCR, and metadata into `sources/<source-id>/`.
   - Record checksums and external source URLs.

2. **OCR and Text Cleaning**
   - Preserve raw OCR.
   - Create normalized text without deleting uncertain readings.
   - Mark OCR defects instead of silently fixing technical terms.

3. **Structural Split**
   - Split by book, lecture, chapter, section, and page when possible.
   - Preserve page mapping separately from cleaned prose.

4. **Candidate Extraction**
   - Equations
   - Figures
   - Concepts
   - Glossary terms
   - Quotes and hidden gems
   - Crosslinks

5. **Review and Promotion**
   - Candidates remain in `processed/`.
   - Reviewed explanatory work moves to canonical Markdown pages.

## First Script

```powershell
python pipeline/scripts/seed_source_from_ocr.py `
  --source-id radiation-light-and-illumination `
  --ocr processed/radiation-light-and-illumination/cleaned_text/internet-archive-ocr.txt
```

The script uses only the Python standard library. It creates lecture splits and candidate JSON catalogs from the Internet Archive OCR seed.

## Review Standard

Machine output is useful but not authoritative. Quotations, formulas, and figure descriptions must be checked against the scan before being treated as canonical.
