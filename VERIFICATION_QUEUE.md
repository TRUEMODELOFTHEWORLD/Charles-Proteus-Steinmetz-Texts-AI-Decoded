# Verification Queue

This file turns the project charter into a practical review queue. It is meant to keep speed and rigor aligned: publish candidate layers quickly, then promote the most important material by scan verification.

## Priority 1: Public Trust Anchors

1. Verify `Radiation, Light and Illumination`, printed pages 17-18:
   - Spectrum of radiation table.
   - Fig. 14 spectrum graphic.
   - Frequency, wavelength, and octave values.
2. Verify `Radiation, Light and Illumination`, printed page 22:
   - Fig. 15 refraction geometry.
   - Sine-law derivation and notation.
3. Verify `Radiation, Light and Illumination`, printed pages 28-29:
   - Fig. 18 regular reflection.
   - Fig. 19 irregular reflection.
   - Reflection, absorption, and transmission language.

## Priority 2: AC Symbolic Method Canon

4. Verify `Theory and Calculation of Alternating Current Phenomena`, Chapter V:
   - Introduction of rectangular components.
   - Introduction of `j`.
   - `j^2 = -1`.
   - Multiplication by `j` as quarter-period rotation.
5. Verify AC Chapter V impedance passages:
   - `Z = r + jx`.
   - `E = ZI`.
   - Inductive and condensive reactance notation.
6. Extract and crop original figures from AC Chapter V:
   - Figs. 21-24 if present in the selected edition.
   - 2026-04-27 progress: Figs. 21-24 were found in the local scan, rendered, cropped, and promoted as scan-crop assets with manifests. They still need second-pass bibliographic and crop-coordinate review before being marked canonical.

## Priority 3: Admittance And Parallel Circuit Language

7. Verify AC Chapter VIII:
   - Admittance definition.
   - `Y = g - jb` or exact edition notation.
   - Conductance and susceptance definitions.
8. Extract Fig. 49 and any related conductance/susceptance curves.
9. Build a scan-checked worked example converting impedance to admittance.

## Priority 3A: First Canonical Equation Set

9a. Scan-verify the first twelve-equation canon in `processed/canonical_equations.json`:
   - `S = f lambda`
   - `I = i + ji'`
   - `j^2 = -1`
   - `x = 2 pi f L`
   - `x_1 = 1 / (2 pi f C)`
   - `Z = r + jx`
   - `E = ZI`
   - `Y = 1/Z = g - jb`
   - conductance/susceptance reciprocal components
   - `P = EI cos theta`
   - `P = I^2 r_eff`
   - `b = 2 pi f C`
   - 2026-04-27 progress: the equation canon was created as source-located candidate data and public pages. Several OCR symbols, especially pi, frequency, and square-root forms, still need scan correction.

## Priority 4: Transient Theory Core

10. Verify transient source Chapter 24:
    - Permanent term and transient term.
    - Energy storage in inductance and capacity.
    - Conditions for gradual versus oscillatory approach.
11. Verify transient source Chapter 27:
    - Oscillation frequency.
    - Critical resistance.
    - Decrement of oscillation.
12. Extract original figures:
    - Fig. 4 starting of AC circuit.
    - Fig. 14 condenser charging/discharge.
    - Fig. 15 decrement of oscillation.
    - 2026-04-27 progress: Figs. 4, 11, 12, 13, 14, and 15 were found in the local scan, rendered, cropped, and promoted as scan-crop assets with manifests. They still need second-pass bibliographic and crop-coordinate review before being marked canonical.

## Priority 5: Tesla-Era Comparison Anchors

13. Verify passages connecting periodic transient terms to high-frequency currents and wireless telegraphy.
14. Verify condenser discharge and spark-gap passages.
15. Compare only after exact passages are located in Tesla source material.

## Priority 6: Glossary Promotion

16. Promote `condensive reactance` after exact source wording is checked.
17. Promote `wattless component` after exact source wording is checked.
18. Promote `electrostatic capacity`, `counter-electromotive force`, and `effective resistance`.
    - 2026-04-27 progress: source-located candidate pages were added for all three terms. Next step is scan verification of the cited OCR line ranges before marking them reviewed.

## Priority 7: Expanded Bibliography Intake

19. Acquire and verify the highest-priority Wikipedia bibliography intake works:
    - `On the Law of Hysteresis`.
    - `Complex Quantities and Their Use in Electrical Engineering`.
    - `The General Equations of the Electric Circuit`.
    - `Mechanical Forces in Magnetic Fields`.
    - `Theory and Calculation of Electric Apparatus`.
20. For each acquired work:
    - Store raw scan/PDF and checksum.
    - Preserve external bibliographic record.
    - Generate OCR, page map, chapter or section split, figures, equations, glossary candidates, quotes, annotations, and crosslinks.
    - Mark all generated items as candidate until scan checked.

## Priority 8: Steinmetz Patent Authority Pass

21. Verify the 11 Wikipedia-listed patent examples in `sources/steinmetz_patents/patent_register.json`.
22. Download patent PDFs and drawings for each seeded patent.
23. Search USPTO, PatentCenter, Google Patents, Espacenet, and assignment data for the full Steinmetz patent catalog.
24. Reconcile the "over 200 patents" claim before calling the patent register complete.
25. Create public patent pages only after title page facts, claims, drawings, and source URLs are verified.

## Promotion Rule

A page can move from candidate to reviewed when:

- The source scan has been checked.
- The page or chapter location is recorded.
- OCR defects in the passage have been corrected or noted.
- Interpretation is visibly separated from source fact.
