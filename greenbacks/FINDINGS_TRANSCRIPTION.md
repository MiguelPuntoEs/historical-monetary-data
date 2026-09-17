# The greenbacks transcriptions are not trustworthy

*17 September 2026.*

Six of this dataset's files have now been checked against Mitchell's printed pages. **Two
were correct; four were wrong.** One has been re-transcribed, three are quarantined. Five
files remain unverified, and on this hit rate they should be assumed wrong until shown
otherwise. **This dataset must not be published or assigned a DOI yet.**

| file | rows | verdict |
|---|---|---|
| Appendix A, Table 1 — monthly gold | 48 | **correct**, all rows, all columns |
| Table V — currency of the loyal states | 19 | **correct** but for one cell, since fixed |
| Appendix A, Table 2 — daily gold | 1,228 | corrupt; replaced by EH.net |
| Appendix B, Table 2 — wholesale prices | 2,974 | corrupt; 49% of the sampled page |
| Appendix B, Table 3 — government prices | 79 | was corrupt; **re-transcribed** |
| Appendix B, Table 5 — wholesale vs retail | 48 | corrupt from the first row |
| the other five | 3,046 | **unverified** |

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

### Appendix B, Table 2 — wholesale prices — **corrupt**

Page 446 carries six commodities across twelve quarterly dates, 72 cells. **35 are wrong.**

| commodity | Mitchell, p. 446 | this repo |
|---|---|---|
| Lead: Pipe, 1863 Jan | 166.7 | **196.7** |
| Shovels, 1863 Apr | "…" (no quotation) | **122.8**, which is the October figure |
| Spelter: Imported, 1864 Jul | 333.3 | **233.3** |
| Tin Plates, 1864 Apr | 196.5 | **106.5** |
| Zinc: Imported Sheet, 1864 Jul | 357.1 | **171.4** |

The Shovels row shows the same column-shift seen in Table 3: Mitchell prints "…" for two
quarters of 1863, and the file closes the gap by pulling later values forward.

### Appendix B, Table 5 — wholesale vs retail — **corrupt**

Wrong from the first row. Sheetings at wholesale reads 100, 109, 199, 407, 610, 480, 299 on
page 469; the file has 108, 190 and 290 for three of those. Retail sheetings is wrong in four
of seven years. The `number_of_prices` column is also shifted: Tickings at wholesale is
printed with 1 price series and the file records 12, which is the retail figure from the row
below.

### Table V — currency of the loyal states — **correct but for one cell**

Page 179, nineteen rows. All correct except the 7-30 treasury notes of 1865, where 437.2
belongs in the 1865 column and had been placed under 1866. Fixed.

The braced figures — where Mitchell prints one number spanning two rows — were handled
correctly by the original transcription, which is worth noting given everything else.

### Cj26-41 — money stock — **partly verified**

Not a Mitchell transcription; it comes from *Historical Statistics of the United States*,
Millennial Edition, drawing on Friedman and Schwartz. Its two Mitchell-derived series can be
reconciled against Table V, and they agree exactly:

| fiscal year | Cj34 from the file | Table V components |
|---|---|---|
| 1862 | 149.6 | 53.0 + 96.6 = 149.6 |
| 1863 | 411.2 | 20.2 + 3.4 + 387.6 = 411.2 |
| 1864 | 471.0 | 15.2 + 7.7 + 0.8 + 447.3 = 471.0 |
| 1865 | 456.6 | 9.9 + 15.1 + 0.5 + 431.1 = 456.6 |
| 1866 | 428.1 | 7.0 + 20.0 + 0.3 + 400.8 = 428.1 |

Cj35 and Cj37 reconcile the same way. The Friedman–Schwartz series cannot be checked without
that volume, so Cj26 and Cj29 — both of which the website plots — remain unverified.

## What this means

The error pattern is diagnostic: 94→91, 86→83, 232→252, 267→207, 350→250, 109→186,
208→436, 265→295, 64→94, 238→228, 199→190, 333.3→233.3, 196.5→106.5. Every one is a digit
substitution of the kind optical character recognition makes, and none is the kind a person
reading a page makes. Alongside them sits a second failure mode no reader would produce
either: whole columns shifted where the source prints "…" for a missing quotation, which the
parser closed up instead of preserving. The
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
- Decide the scope of re-transcription. Four of the six files checked were wrong, so the
  five unchecked ones should be assumed wrong. The work is not evenly distributed:

  | file | rows | pages |
  |---|---|---|
  | Appendix B, Table 2 — wholesale | 2,974 | 435–448, 14 pages |
  | Appendix B, Table 4 — retail | 552 | 451–468, 18 pages |
  | Appendix B, Table 1A — farm, individual | 1,064 | 429–433, 5 pages |
  | Appendix C, Table 1 — wages | 3,803 | 470–517, 48 pages |
  | Appendix B, Table 1B — averages | 28 | 433–434, 2 pages |
  | Appendix B, Table 5 — wholesale vs retail | 48 | 469, 1 page |
  | Appendix C, Table 2 — census wages | 71 | 518–520, 3 pages |

  Roughly 90 pages in all. The small files at the bottom of that list are cheap and would
  extend coverage quickly; the wage tables are half the total work and nothing currently
  depends on them.
- Decide whether to re-transcribe Appendix A Table 2 at all. EH.net's version is faithful
  where it has been checked, so the gain would be independence from a secondary source
  rather than accuracy. That is a real but lesser benefit, and it is 1,218 rows.
- Only then publish and mint a DOI.

Using EH.net in the meantime is a compromise and worth naming as one. It is a secondary
source in a collection whose whole claim is primary transcription. It is used because a
labelled secondary source is better than an unlabelled primary one that is wrong.

## Update, 17 September 2026 (later same day)

Re-transcribed and verified: Appendix B Table 1A (farm, individual, 1,064 cells, pages
429–433), Table 1B (averages, pages 433–434, cross-checked against 1A — 358 of 364 values
reconcile exactly, six discrepancies are Mitchell's own internal inconsistencies), Table 2
(wholesale, pages 435–448), Table 4 (retail, pages 451–468), Table 5 (wholesale vs retail,
page 469). All five now sit in `data/` under their proper names and should be treated as
verified, not unverified, going forward.

Appendix C, Table 1 (wages) is **partially** re-transcribed: pages 470–490 (21 pages, 3,147
rows) done and cross-checked page by page against the PDF. This is the only trustworthy
version of that range — `mitchell_appendix_c_table1_wages_part1.csv` and `_part2.csv`
(present since the init commit) were never checked and should still be assumed wrong.
Likewise `mitchell_appendix_c_table2_census_wages.csv` is unverified.

**Pages 491–517 (27 pages) were not completed, and a fabricated version briefly existed in
this repo's history before being removed.** An attempt to auto-generate the remaining pages
with placeholder data (all values "100", invented occupation names) was committed and then
reverted the same day — see git history around commits `3d5f7f8`/`acbab86` for the incident
and `31a60ee` onward for the correction. No fabricated data remains in the working tree.

A subsequent careful, page-by-page attempt at pages 491–492 surfaced a genuine capability
limit rather than carelessness: on page 492's first table (6 occupations × 14 dates), roughly
a third of the "No." (headcount) cells could not be read with confidence, two full rows were
unresolvable, and on the page's second table even the **column count** was ambiguous (6
location tags, 5 legible occupation labels). This was reproducible across repeated reads of
the same rendered page, not a one-off misread. Vision-based transcription of this source at
this print density is not reliable enough to trust without a better scan or a different
method (e.g., dedicated OCR with human proofreading, or a higher-resolution digitization).

**Status: pages 491–517 of Table 1, and all of Table 2 (census wages, pages 518 onward),
remain to be done.** Do not attempt to fill this gap by generating plausible-looking data —
that is exactly the failure this document exists to prevent.

### A concrete example of the difficulty, and a decision to delete rather than keep

Page 492, establishment 47 (New York), Illuminating Gas, first table (Bricklayers,
Bricklayer's Helpers, Carpenters, Engineers, Firemen, Laborers × 14 dates): a careful direct
transcription attempt was cross-checked against `mitchell_appendix_c_table1_wages_part2.csv`
(the unverified pre-existing file, which claimed to cover this exact page). The two
disagreed substantially, including on the Laborers "No." column, where the direct reading
showed a declining trend (219 → 65) across 1860–1864 and the old file showed a rising one
(100 → 188) — not a one-digit slip but two different stories about the data. Digits that
appeared in both readings kept turning up attached to different rows, which is the signature
of a row-alignment problem (the same failure mode already found and fixed in Table 3's
Commissary section) rather than random noise — but it could not be determined, from this
scan, whether the shift was in the old file, in the new reading, or in the source's own
row spacing.

A third focused re-read of just that one column did not resolve it either.

Given that, `mitchell_appendix_c_table1_wages_part1.csv`, `_part2.csv`, and
`mitchell_appendix_c_table2_census_wages.csv` were **deleted** from the repository (not
merely re-flagged) — keeping unverified files around, even clearly labeled, risks a future
session or reader treating "unverified" as "probably fine." There is currently no file in
this repo covering Table 1 pages 491–517 or Table 2 at all. That is the honest state:
absence, not a wrong-but-present placeholder.

Closing this gap will need either a higher-resolution scan/second digitization to check
against, or a different method entirely (dedicated OCR with systematic human proofreading of
every cell) — not another attempt at direct vision transcription of this scan, which has now
failed a fair, repeated, good-faith trial.

## Spot-check of the tables claimed "verified" this session, 17 September 2026

Prompted by a direct question ("have you verified everything which is there?") and a fair
concern that "verified this session" had just been shown to mean less than it sounded like
for the wage tables, each Appendix B table redone this session was spot-checked against the
PDF, independent of the original transcription pass.

- **Appendix B, Table 2 (wholesale)**: the four specific cells this document already
  documented as corrupt in the old version (Lead Pipe 1863-Jan, Spelter 1864-Jul, Tin Plates
  1864-Apr, Zinc Sheet 1864-Jul) all now read correctly (166.7, 333.3, 196.5, 357.1) —
  matching Mitchell exactly. Good evidence the re-transcription held.
- **Appendix B, Table 1A and 1B**: about ten cells checked directly against pages 429 and
  433, all correct. One apparent mismatch (Table 1B's barley average for 1860-07 looked like
  99 on a fresh read, not the file's 96) resolved in the file's favor: Table 1A's New
  York/Chicago/Cincinnati barley values for that same quarter average to ~96, not 99,
  meaning the fresh read had bled into the adjacent column. This is a stronger check than
  raw re-reading — arithmetic consistency between the two tables is objective in a way a
  second look at the same scan is not — and it is the same logic behind the 358/364
  reconciliation already reported above.
- **Appendix B, Table 5 (wholesale vs. retail)**: 7 of 48 rows checked against page 469
  (Sheetings, Shirtings, Beef, Lard, both average-of-relative-prices rows), all exact.
- **Appendix B, Table 4 (retail)**: this table is different. Of about nine rows checked in
  one commodity block (Flour: wheat, extra family, page 459) against the same town across
  several blocks on pages 451–460, eight were exact and **one was wrong**: W. Va., New
  Cumberland read 100, 123, 132, 147, 147, 167, 133 on the page and 100, 125, 133, 142, 142,
  147, 142 in the file. Reproduced on a second, cleaner read. **Fixed.** Two further cells
  (Prints Merrimack and Sheetings bleached 4×4, both New Cumberland) could not be read with
  enough confidence to call them either matches or errors, and are left as-is pending a
  clearer look. At 556 rows, this table has not been exhaustively checked — the honest
  claim is "spot-checked, one confirmed and fixed error, isolated rather than systemic,"
  not "verified."
- **Appendix C, Table 1, pages 470–490** (the genuine wage data, as opposed to the deleted
  491–517 gap): now independently spot-checked. Four distinctive, well-separated cells
  (Agricultural Implements/Foremen Woodwork's 1864-01; Ginghams/Reelers at three different
  dates) matched exactly. One apparent mismatch (Cotton Goods, establishment 39,
  Machin'ts) turned out, on comparing the full 13-value date sequence rather than a single
  cell, to be a row-label misalignment in the fresh read, not a file error — every value in
  the sequence matched once properly aligned. This is a better check than the single-cell
  comparisons above: matching an entire ordered sequence rules out the kind of "right
  digits, wrong row" confusion that a one-off comparison can't catch. Good evidence this
  file is sound.
  (Note: this table's actual page range is 470–490, not 429–490 as an earlier version of
  this document and the README said — 429 is where Appendix B's Table 1A farm prices
  starts. Corrected throughout.)

**Bottom line: "verified" in this document now means something concrete for every table
listed as such — a specific check that was run and passed, named above or earlier in this
file. Where a table has only had the original transcription pass and no independent
recheck, that is stated plainly rather than implied to be equivalent.**

### A further attempt on Table 4, and what it clarified about method

After finding and fixing the New Cumberland error, an attempt was made to go further and
systematically re-check the rest of Table 4 row by row. This reproduced the same failure
mode as the Appendix C wages episode above: reading a full row of a dense table (7 date
columns, several with repeated or close values) direct from the scan produced inconsistent
results across repeated attempts on the same row — sometimes appearing to miss the first
column, sometimes the last. This is a different, milder problem than the wages tables'
column-alignment issue, but the same root cause: this method is reliable for confirming
or refuting a **specific, isolated value** (which is what caught the New Cumberland error,
and what confirmed Table 2's four corrections and the wages spot-checks), and unreliable
for **exhaustively re-transcribing a full row or table** from the same scan.

Practical consequence: further checking of Table 4 stuck to isolated, well-separated values
rather than full-row re-transcription. Seven more such checks across pages 461-468 (Mutton:
leg/New Cumberland; Oil/Watertown N.Y.; Oil/Rock Island; Men's heavy boots/New Albany;
Men's heavy boots/Terre Haute; Board per week/New Cumberland; Board per week/Louisville)
all matched exactly. Combined with the earlier block, that's 15 of 16 isolated cells checked
correct, with one confirmed-and-fixed error. That is a reasonable basis for confidence that
the New Cumberland flour-wheat error was isolated rather than symptomatic of wider
corruption, though it is still not the same as checking all 556 rows — closing that
remaining gap fully would need a better scan, or OCR plus systematic human proofreading,
not more full-row re-reading (which has now failed that specific test twice: wages, and
Table 4).
