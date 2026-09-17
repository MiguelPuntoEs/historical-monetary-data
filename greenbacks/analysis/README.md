# Analysis

Dependency-declared Python, run from the collection's environment (`uv sync` at the root).

| script | what it does |
|---|---|
| `00_fetch_sources.py` | downloads the two NBER price indices and EH.net's daily greenback quotations into `../data/` with provenance headers. Its output is committed; you do not need to run it |
| `01_pass_through.py` | reproduces Table 1 of the pass-through paper: monthly pass-through from greenback depreciation to Northern prices, 1862–1865 |
| `02_validate.py` | invariant checks over every file in `../data/`. Run it before trusting anything |

`make` at the top of `greenbacks/` runs validation and then the analysis.

## Units and conventions

The greenback quotations are **gold dollars per $100 of paper currency**: 100 is parity,
lower means greater depreciation. The analysis inverts them into the *gold price of
greenbacks*, `G = 100 / value`, so that a rise in `G` is a depreciation and pass-through
coefficients come out positive.

The price indices have different bases — the general index is 1913 = 100, the wholesale
index 1910–1914 = 100. This does not matter, because every regression is in log differences.

Standard errors are HAC with one monthly lag and **no small-sample correction**. That last
detail is not cosmetic: with 45 observations the correction moves the reported standard
errors by about 5 per cent, which is the difference between reproducing the paper's table
and not.

## Which daily series

`01_pass_through.py` uses `ehnet_greenback_daily_1862_1878.csv`, not this repository's own
transcription of the same Mitchell table. The transcription is corrupt and has been moved to
`../data/suspect/`. See `../FINDINGS_TRANSCRIPTION.md`.
