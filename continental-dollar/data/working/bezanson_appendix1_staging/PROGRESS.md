# Bezanson Appendix Table 1 transcription - final status, this session

Source: Anne Bezanson, "Prices and Inflation during the American Revolution:
Pennsylvania, 1770-1790" (1951), Appendix Table 1, pp. 332-342. Average monthly
wholesale prices, ~25 commodities, 21 years (1770-1790).

**Published: `../../published/bezanson_1951_appendix1_monthly_prices.csv`
(392 commodity-year rows, ~4,700 cells).**

## What happened

Direct vision-based cell-by-cell transcription (the method used successfully
elsewhere in this project) proved unreliable on this specific table even
though the source print quality is good - repeated, reproducible row-mixing
errors (see git history: an entire "Beef" row was initially transcribed
correctly for Corn, and vice versa). Rather than continue an error-prone
method, this table was built from the PDF's embedded OCR text layer instead
(pdftotext -layout), which is high quality for this clean 1951 typeset book,
then repaired programmatically (reassembling OCR-split decimal points) and
spot-checked against fresh page images throughout.

This inverts the project's usual rule ("transcribe from images, not OCR") -
justified here specifically because this source's OCR is demonstrably more
reliable than direct vision reading was proving to be, which is the opposite
of the situation with the 1866/1828 scans used elsewhere in this collection.
That reasoning, and the spot-check evidence for it, should travel with the
data - it is not a general license to prefer OCR elsewhere in this project.

## Verification performed

- Automated: OCR-split decimal reassembly (~400 individual token merges)
- Automated: isolated-spike detection (value jumps >3x then reverts >2.5x
  within 2 months) - zero flags in the final published file
- Manual: full read-through of every "clean" (12-value) row looking for
  values that passed the 12-count check by coincidence but were still wrong
  (e.g. "300" instead of "3.00", stray leading/trailing digits) - found and
  fixed 6 such cases
- Targeted image re-verification: Beef 1770 (raw OCR matched), Coffee 1786
  (exact match), Wheat 1780 (exact match), Corn 1780 (one genuinely ambiguous
  cell resolved by economic-plausibility argument - see file header), Flour
  Superfine 1773 and Tea Bohea 1774 (both resolved by direct page read),
  Beef 1776 and 1777 (fully replaced with earlier direct-vision-verified
  values from this same session, which included resolving a real Beef/
  Chocolate row ambiguity via each commodity's distinct decimal-place
  convention)

## What remains (NOT in the published file)

~130 commodity-year rows where OCR parsing produced genuinely ambiguous
results not resolved by pattern-matching - see `messy_to_fix.txt` for the
exact list with the raw (unresolved) tokens for each. Concentrated in:

- 1778-1782: the years with the most complex print layout, including a
  mid-1781 currency-unit switch (shillings to pounds) printed within the same
  table, which badly confuses simple column-position parsing
- Secondary/minor commodities with partial-year coverage (Bread Ship, Cotton,
  Indigo, Leather sole, Rice, Sugar Loaf, Tobacco, Turpentine, Wine in their
  early appearing years) - these need image verification to distinguish
  "OCR dropped a real value" from "the source genuinely has fewer than 12
  months this year," which cannot be resolved from the OCR text alone

To continue: read `messy_to_fix.txt`, for each row either resolve via
economic-plausibility reasoning + a targeted image check (as done for the
six cases above), or confirm against the image how many real months of data
that commodity has that year before assigning values to month positions.

## Files in this directory

- `ocr_raw.txt` - the raw OCR extraction (pdftotext -layout, pp. 332-342)
- `parse_ocr.py` - final parser (decimal-merge + unit-token stripping)
- `canonicalize.py` - maps OCR-garbled commodity labels to canonical names
- `canonical_rows.json` - all 517 parsed rows before the clean/messy split
- `bezanson_clean_long.csv` - the 392 rows that became the published file
  (pre-manual-QA-fixes; the published file has since had further corrections
  applied directly, so treat the published file as authoritative, not this one)
- `messy_to_fix.txt` - the ~130 rows still needing resolution
