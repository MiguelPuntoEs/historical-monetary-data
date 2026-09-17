# The greenbacks transcriptions are not trustworthy

*17 September 2026.*

Three of this dataset's files have been checked against Mitchell's printed pages. One was
correct. Two were wrong — one of them badly, and it has since been re-transcribed. Nine
files remain unverified, so **this dataset should not be published or assigned a DOI yet.**

## How this surfaced

Not by reading the files. By trying to reproduce Table 1 of the pass-through paper and
getting coefficients that were close but wrong. Tracing the discrepancy back through the
inputs led to the first corrupt file, and checking that one against the page led to the
second.

## What was checked

Page images from the Internet Archive scan `historyofgreenba00mitcuoft` (leaf = printed
page + 21), cross-read against a second scan and against the local copy of the book.

### Appendix A, Table 1 — monthly gold prices — **correct**

`data/mitchell_appendix_a_table1_gold_prices_1862_1865.csv`, pages 423–424. All 48 rows
verified digit by digit across all five columns, including the date-of-high and date-of-low
strings. No errors. This is the file the website publishes and the only greenbacks file
currently known to be sound.

### Appendix A, Table 2 — daily gold prices — **corrupt**

Mitchell prints a highest and a lowest gold value for each trading day. The high cannot be
below the low. In the transcription it is, on **168 of 1,228 rows — 13.7 per cent**:

| date | highest | lowest |
|---|---|---|
| 1862-01-06 | 97.30 | 97.56 |
| 1862-02-10 | 94.52 | 96.27 |
| 1862-03-10 | 96.04 | 98.04 |

Set against EH.net's digitization of the same table, the file disagrees on **1,122 of the
1,187 dates the two share**, sometimes enormously:

| date | this repo (high/low) | EH.net (high/low) |
|---|---|---|
| 1863-11-13 | 68.67 / 97.91 | 68.03 / 67.85 |
| 1864-08-01 | 61.51 / 61.08 | 39.84 / 38.61 |

The 1864-08-01 row implies the greenback gained twenty-two gold cents overnight, a month
after its wartime trough. It carries 41 dates EH.net lacks and misses 31 it has, including
1 January 1863 and 4 July 1863, when the New York gold room did not trade.

### Appendix B, Table 3 — government prices — **was corrupt, now re-transcribed**

Page 450, the Navy Department's Bureau of Provisions and Clothing, fifteen rows. **Ten are
wrong.** The page against the file:

| item | Mitchell, p. 450 | this repo |
|---|---|---|
| Sugar | 100, 94, 74, 100, 281, 275 | 100, **91**, … |
| Blankets | —, 100, 99, 132, 232, 329 | **100, —**, 99, … (first two cells transposed) |
| Flannel | —, 100, 92, 124, 232, 276 | **100**, 100, 92, 124, **252**, 276 |
| Overshirts, flannel | 100, 96, 92, 103, 201, **267** | …, **207** |
| Satinet | —, 100, 94, 99, 180, 238 | **100, —, 109**, 94, 99, **190**, **228** (seven values in six columns) |
| Trousers, canvas duck | 100, 98, 97, 105, 194, **350** | …, **250** |
| Shoes, calf skin | 100, **86**, 74, 83, 124, 149 | 100, **83**, … |
| Socks, woolen | 100, **109**, 102, 113, **208**, 234 | 100, **186**, 102, 113, **436**, 234 |
| Mattresses | 100, 97, 94, 97, 244, **265** | …, **295** |
| Linseed oil, boiled | —, 100, **64**, 123, **190**, 227 | **100, 94, 94**, 123, **180**, 227 |

Six of these readings — 109, 208, 350, 180, 238 and 232 — were independently confirmed
against the book by the author before the file was replaced, as was the structural finding
below: on page 449 Pork reads blank under 1860 and 100 under 1861.

Re-transcribing the whole table from pages 449–451 showed the damage was far wider than
the one section. **54 of 77 rows differed; 170 of 456 cells.** Two further findings:

- The entire Commissary General section, all 25 rows, was **shifted one column left**.
  Mitchell prints "…" in the 1860 column for that section and bases the index at 1861 = 100.
  The old file put 100 under 1860 and moved every later year back one, so that each row's
  1865 value was silently dropped and each earlier year carried the wrong figure.
- Two item names were garbled: "Greatcoats" for "Great coats", and "R. and R. G. coffee"
  for "R. and R. and G. coffee".

The corrected file carries all four divisions of the table — Quartermaster General,
Commissary General of Subsistence, Bureau of Provisions and Clothing, and the Surgeon
General's drugs and chemicals — 79 rows in all, with blanks where Mitchell prints "…".

## What this means

The error pattern is diagnostic: 94→91, 86→83, 232→252, 267→207, 350→250, 109→186,
208→436, 265→295, 64→94, 238→228. Every one is a digit substitution of the kind optical
character recognition makes, and none is the kind a person reading a page makes. The
collection's README states that its files are transcribed from page images rather than from
OCR. **For the greenbacks files that claim does not hold**, and the README has been
corrected to say so until it does.

The damage is bounded in one useful way. The corrupt files feed nothing that has been
published. The website's greenback charts are built from Appendix A Table 1 and the money
stock series, and Table 1 is verified correct. The pass-through paper was estimated on
EH.net's daily quotations, not on the transcription here, which is why its results stand.

## What has been done

1. Both corrupt files moved to `data/suspect/`. Nothing in `analysis/` reads them.
2. `analysis/02_validate.py` checks the high/low invariant, date integrity and the presence
   of a provenance header across every file in `data/`, and runs before the analysis in the
   Makefile. It would have caught the daily file on the day it was written.
3. `data/ehnet_greenback_daily_1862_1878.csv` added for the daily quotations, clearly
   labelled as someone else's digitization rather than my transcription.

## What remains

- **Done:** Appendix B Table 3 re-transcribed from pages 449–451.
- Verify the nine unchecked files the same way. Their error rate is unknown, and both files
  checked before re-transcription were wrong.
- Decide whether to re-transcribe Appendix A Table 2 at all. EH.net's version is faithful
  where it has been checked, so the gain would be independence from a secondary source
  rather than accuracy. That is a real but lesser benefit, and it is 1,218 rows.
- Only then publish and mint a DOI.

Using EH.net in the meantime is a compromise and worth naming as one. It is a secondary
source in a collection whose whole claim is primary transcription. It is used because a
labelled secondary source is better than an unlabelled primary one that is wrong.
