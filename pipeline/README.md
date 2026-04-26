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

## PDF Image Extraction

For original Steinmetz diagrams, use the PyMuPDF-based extraction tool:

```powershell
python -m pip install -r pipeline/requirements.txt

python pipeline/scripts/extract_pdf_images.py `
  --source-id radiation-light-and-illumination `
  --pdf sources/radiation-light-and-illumination/raw/radiation-light-and-illumination-1909-ia-scan.pdf `
  --mode pages `
  --pages 1-20 `
  --dpi 220
```

Generated full-page renders and embedded image dumps are review candidates, not canonical diagrams. Curated figure crops should be promoted into:

```text
diagrams/original/<source-id>/figures/
```

with exact source-page metadata and a matching diagram analysis page.

To crop a verified region from a rendered page:

```powershell
python pipeline/scripts/crop_image_region.py `
  --source-id radiation-light-and-illumination `
  --figure-id rli-fig-14-spectrum-of-radiation `
  --source-image processed/radiation-light-and-illumination/image_extraction/page_renders/pdf-page-0038-220dpi.png `
  --source-location "Radiation, Light and Illumination, printed page 18, Fig. 14" `
  --box 120,620,1010,930 `
  --out diagrams/original/radiation-light-and-illumination/figures/fig-14-spectrum-of-radiation.png
```

## Review Standard

Machine output is useful but not authoritative. Quotations, formulas, and figure descriptions must be checked against the scan before being treated as canonical.
