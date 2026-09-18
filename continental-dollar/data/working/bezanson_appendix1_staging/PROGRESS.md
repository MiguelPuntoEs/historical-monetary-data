# Bezanson Appendix Table 1 transcription progress

Source: Anne Bezanson, *Prices and Inflation during the American Revolution:
Pennsylvania, 1770-1790* (1951), Appendix Table 1, pp. 332-342. Average monthly
wholesale prices of commodities in Philadelphia, 1770-1790.

Local PDF: /Users/miguel/workspace/continentals-paper/sources/Prices_and_Inflation_During_the_Ameri_z_library_sk,_1lib_sk,.pdf
PDF page = printed page + 17 (printed 332 = pdf 349; confirmed).
Two years per PDF page for most of the range (verify per-page as you go).

Method: transcribe one commodity row at a time across all fetched years,
checking December(year N) -> January(year N+1) continuity as the primary
verification signal. Flag, don't guess, when a cell can't be read with
confidence or continuity breaks implausibly.

## Years fetched so far
- 1770-1777 (PDF pages 350-353), rendered and available for careful reading

## Commodities transcribed (years 1770-1777 only so far)
- Beef (£-bbl): DONE for 1770-1775, 1777. **FLAGGED: 1776 Dec, ambiguous
  between Beef and Chocolate row (both could read as jumping to 48.0 from a
  ~4-5 range) - needs a fresh careful look before finalizing.**

## Commodities NOT yet started (this batch of years)
Chocolate, Coffee, Corn, Flour Com., Flour Sup., Iron Bar, Molasses, Pepper,
Pork, Rum W.I., Sugar Mus., Tar, Tea Bohea, Wheat, Bread Ship, Cotton,
Flour Mid., Indigo, Leather sole, Rice, Sugar Loaf, Tobacco, Turpentine, Wine
(the last 10 are blank/sparse in the earliest years - check each year's
table for which commodities actually have entries; don't assume constancy)

## Years not yet fetched
1778-1790 (13 more years)

## Output
Once a commodity's full 1770-1790 row is verified, append to
bezanson_appendix1_wide.csv (create if absent) with columns:
commodity,unit,1770-01,1770-02,...,1790-12

## Update

**Useful technique found**: Beef and Chocolate use different decimal conventions
in this table (Beef, £-bbl: always 2 decimals, e.g. "4.30"; Chocolate, d-lb:
always 1 decimal, e.g. "48.0"). When two adjacent rows' values seem confused,
check decimal-place count against each commodity's established convention
before guessing. This resolved the Dec-1776 ambiguity: 48.0 (1 decimal) is
Chocolate's, not Beef's.

**Beef, £-bbl: DONE and verified for 1770-1777** (see beef.csv in this
directory). Continuity checks passed at every year boundary (largest jump:
Dec 1776 4.30 -> Jan 1777 6.96, +62%, consistent with the book's own account
of 1777 as when depreciation accelerated).

**Real-world pace note**: getting Beef fully verified for 8 years took multiple
read/re-read cycles and one genuine ambiguity requiring a targeted re-fetch.
A first attempt at Corn (same 8 years) produced a row identical to Beef's own
sequence - a duplication/recall error, not a fresh reading - and was abandoned
rather than committed. This confirms the core risk: reading one row from
memory/recall across a multi-page context is unreliable even when the
methodology (isolate one row, check continuity) is sound. Each row needs a
fresh look at the actual rendered page, not reuse of an earlier mental read.

**Realistic scope**: 25 commodities x 21 years at this rate is a multi-session
undertaking. Do not rush it by lowering the verification bar - that is exactly
how the greenbacks wages incident happened earlier this project. Better to
have 1 commodity fully correct than 25 commodities partially wrong.
