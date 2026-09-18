# Bezanson Appendix Table 1 transcription - status after second pass

Source: Anne Bezanson, "Prices and Inflation during the American Revolution:
Pennsylvania, 1770-1790" (1951), Appendix Table 1, pp. 332-342. Average monthly
wholesale prices, ~25 commodities, 21 years (1770-1790).

**Published: `../../published/bezanson_1951_appendix1_monthly_prices.csv`
(448 commodity-year rows of ~525 possible, ~5,300 cells).**

## History

First pass built the file from the PDF's embedded OCR text layer (pdftotext
-layout), repaired programmatically, giving 392 rows. See git history for
that commit's full reasoning (OCR chosen over direct vision transcription
because direct transcription proved unreliable on this specific table -
reproducible row-mixing errors even on good print quality).

Second pass (same session, prompted by "why not do the other rows?") worked
through most of the ~130 rows flagged as unresolved, fetching each year's
page fresh and reading it directly rather than relying on OCR, since OCR had
already done its job getting the bulk of the table and what remained was
exactly the cases OCR parsing couldn't resolve automatically. Added 56 rows,
bringing the total to 448.

## Method for the second pass

- Fetched each year's page image fresh (not reusing earlier renders)
- Resolved full 12-month rows for the core commodities directly
- For 1781 specifically: recognized the mid-table currency switch (Jan-Apr
  in one unit, May-Dec in another, reflecting the March 1781 currency
  reform) and concatenated both halves as printed, consistent with the
  file's existing units note
- For partial-year secondary commodities (Bread Ship, Cotton, Flour
  Middling, Indigo, Leather sole, Rice, Sugar Loaf, Tobacco, Turpentine,
  Wine in their early years): inferred which months a partial row covers
  from its visual position in the row (values clustered toward the right
  of the table generally mean the commodity's price record starts partway
  through the year and runs to December). This is a reasonable inference,
  not a pixel-confirmed reading - a case where the row is short and the
  months are genuinely uncertain, treat the position as approximate.
- One real self-caught error: two batches of resolved rows were prepared in
  reasoning but not actually written to the working file before the merge -
  caught by cross-referencing the published file against what had been
  discussed, and added afterward (Corn 1778, Pepper 1778, Tea Bohea 1778,
  Tar 1781). Worth remembering: reasoning through a fix is not the same as
  recording it - always verify the file actually contains what was decided.
- Final validation: structural check (all rows exactly 14 fields, all
  values parse as floats), isolated-spike detection (a value that jumps
  >3x then reverts >2.5x within one month either side), duplicate
  commodity-year key check. One spike flag (Tar 1781 July, transcribed as
  120.4) was left documented as an unresolved anomaly rather than silently
  corrected - the user then checked the actual page directly and confirmed
  the real value is 20.4 (a leading "1" was a misread, not a real digit).
  Fixed; zero spike flags remain.

## What remains (~80 rows, NOT in the published file)

Concentrated in:
- 1776, 1777, 1779, 1781: very sparse partial-year secondary commodities
  where even the *number* of real months present is uncertain from the OCR
  fragments alone (e.g. 1781 Bread Ship, Indigo, Rice, Wine; 1779 Pepper)
- A few single-cell gaps in otherwise-complete rows where one month could
  not be read with confidence from the page (documented per-cell in earlier
  git history where found)

To continue: for each remaining row, fetch the relevant page fresh, and
either resolve the value/position with a clearer look, or confirm it
genuinely cannot be determined from this scan and needs a different source.

## Files in this directory

- `ocr_raw.txt` - the raw OCR extraction (pdftotext -layout, pp. 332-342)
- `parse_ocr.py` - OCR parser (decimal-merge + unit-token stripping)
- `canonicalize.py` - maps OCR-garbled commodity labels to canonical names
- `canonical_rows.json` - all 517 OCR-parsed rows before the clean/messy split
- `bezanson_clean_long.csv` - the 392 rows from the first pass (superseded -
  the published file now has 448 rows including the second pass's additions
  and corrections; treat the published file as authoritative)
- `messy_to_fix.txt` - the rows still needing resolution as of the first
  pass (partially out of date now that the second pass resolved most of
  them; the "What remains" section above is the current accurate list)
