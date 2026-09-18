# Bezanson Appendix Table 1 transcription - status after fifth pass

Source: Anne Bezanson, "Prices and Inflation during the American Revolution:
Pennsylvania, 1770-1790" (1951), Appendix Table 1, pp. 332-342. Average monthly
wholesale prices, ~25 commodities, 21 years (1770-1790).

**Published: `../../published/bezanson_1951_appendix1_monthly_prices.csv`
(500 commodity-year rows of 525 possible, 95.2%, ~5,900 cells).**

## Fifth pass: 1778 and 1790 completed

Same checklist method (`VERIFY_1778_1790.md`). Both years resolved to 25/25
with no ambiguity - the user's shorthand ("value x count" for runs of
repeated values) made this pass fast. One more caught misread: Cotton 1790
August was first reported as "18.88" against neighbors all in the 1.5-2.1
range; asked to confirm, the real value is 1.88 - the same "spurious
leading 1" pattern as the Tar 1781 case. Two independent instances of the
identical error type is worth noting as a real, specific failure mode for
this reader/source combination, not a one-off.

Also resolved in passing: Pork 1790, a core commodity that had fallen
through every earlier pass without ever being flagged as missing (found by
explicitly diffing the published file's commodity list against the full
25 for every year, not by it showing up in any automated OCR output). The
user's reading confirmed an earlier, unconfirmed direct read of mine
exactly. Worth remembering: "not in the messy list" does not mean "not
missing" - always check presence against the full expected set, not just
against what OCR parsing flagged as ambiguous.

Nine years now complete for all 25 commodities: 1777, 1778, 1779, 1781,
1786, 1787, 1788, 1789, 1790.

## Sixth pass, in progress: the final 25 rows

`VERIFY_FINAL_25.md` covers the last 25 missing rows, scattered across
eleven years (1770-1776, 1780, 1782-1785), on PDF pages 350-352 and
355-357. A few of these (Coffee 1772, Pork 1772, Beef 1783) are core
commodities that fell through the cracks the same way Pork 1790 did -
worth flagging to whoever checks them that finding real data there is
expected, not surprising.

## Fourth pass: human verification continued (1776, 1777, 1779)

Same method as the third pass: a checklist (`VERIFY_1776_1777_1779.md`) named
exactly what was missing, the user read the relevant rows directly from the
page (PDF pages 353 and 354), and every row resolved cleanly - no further
anomalies found this round. 1777 and 1779 are now complete for all 25
commodities; 1776 is complete for 24 of 25 (Tobacco confirmed genuinely
blank that year - consistent with it never appearing in the OCR pass at
all, which in hindsight was itself informative rather than just a gap).

One correction worth recording: the user's first read of Bread Ship 1776
gave "1.5" for October; a plausibility check (a jump from blank straight to
1.5 then 17.8 looked odd against 12.5's smoother fit with neighbors) led to
asking again, and the real value was 12.5. Worth remembering as a pattern:
when a human-reported value breaks the local trend sharply, it's worth one
clarifying question before recording it - the same discipline used earlier
for OCR output applies to manual transcription too, human or automated.

Current state by year (commodities present / 25):
1770-24, 1771-24, 1772-22, 1773-23, 1774-24, 1775-24, 1776-24, 1777-25,
1778-16, 1779-25, 1780-22, 1781-25, 1782-21, 1783-21, 1784-22, 1785-24,
1786-25, 1787-25, 1788-25, 1789-25, 1790-15.

**1778 and 1790 are the weakest remaining years** and the natural next
target if continuing.

## Third pass: human verification

The user checked PDF page 355 (printed p.337, the 1781 table) directly
against the source, using a checklist (`VERIFY_1781.md`) generated from the
second pass's remaining gaps. Two things came of it:

1. The one isolated-spike flag from the second pass (Tar, 1781, July,
   transcribed as 120.4) was confirmed wrong - the real value is 20.4. A
   leading "1" in the automated/visual transcription was a misread, not a
   printed digit. This is a clean example of the isolated-spike heuristic
   doing its job: it can't fix an error, but it correctly identifies which
   cells are worth a second look.
2. All seven remaining sparse rows for 1781 (Bread Ship, Indigo, Leather
   sole, Rice, Sugar Loaf, Turpentine, Wine) were read directly and added.
   1781 is now complete for all 25 commodities. Six of the seven follow the
   same Jan-Apr (old currency) / May-Dec (new currency) split seen
   elsewhere in 1781; Turpentine has a single real value (December, 90),
   the rest of the year genuinely blank in the source.

Worth naming directly: human verification here wasn't used to spot-check a
claimed-solid dataset - it was used to resolve the *specific, named*
remaining gaps this document already knew about. That is a more efficient
division of labor than asking someone to re-check everything.

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
