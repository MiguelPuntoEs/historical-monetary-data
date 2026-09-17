# Historical monetary data

Primary-source monetary data, transcribed from the original printed tables into
machine-readable form and released openly.

Each dataset lives in its own directory with its own README and sources. What they aim at
is a method, and that method is the point: **data should be transcribed from page images
rather than from optical character recognition**, because for eighteenth- and
nineteenth-century tables OCR corrupts the fractions that pervade the originals and
confuses digits in ways that change values materially. In one case the difference between
an OCR reading and the page was 800 against 300.

The `continental-dollar` files meet that standard. **The `greenbacks` files do not**, and
two of them have been verified corrupt in exactly the way OCR corrupts a table. They are
quarantined in `greenbacks/data/suspect/` and the dataset should not be cited until it has
been re-transcribed: see [`greenbacks/FINDINGS_TRANSCRIPTION.md`](greenbacks/FINDINGS_TRANSCRIPTION.md).
The claim above is the standard this collection holds itself to, not yet a description of
everything in it.

## Datasets

| | |
|---|---|
| [`continental-dollar/`](continental-dollar/) | Scales of depreciation enacted by seven American states to settle debts in Continental currency, 1777–81, with contemporary merchants' quotations for Philadelphia and Virginia |
| [`greenbacks/`](greenbacks/) | Gold prices, commodity prices, wages and the money stock during the American Civil War, 1859–66, from Wesley C. Mitchell's *A History of the Greenbacks* (1903). **Partly unverified — see the warning above** |

`shared/` holds the chart style the figures draw from.

## Conventions

**Provenance in the file.** Every CSV opens with comment lines (`#`) giving the source,
table and page numbers, so any figure can be traced to the printed original without
consulting a README.

**Sources over compilations.** Where an enacted statute survives, it is preferred to any
later reprint of it. Where printed compilations disagree, both are published rather than
one being silently chosen — see `continental-dollar/data/published/pennsylvania_scale_three_sources.csv`,
where the statute, the federal compilation and Webster's 1791 tables are set side by side
and do not agree.

**Cross-checks reported.** Where a second source reproduces the same series, the agreement
rate is stated rather than assumed.

**Checks that run.** `greenbacks/analysis/02_validate.py` enforces what a printed table
cannot contradict — a high below a low, an average outside its own range, a row that will
not parse — across every file. It is the check whose absence let two corrupt files sit in
this repository unnoticed.

**Missing stays missing.** Where a source has no entry, the cell is blank. It is never
interpolated, and never filled from a different source without saying so.

## Using it

The analysis scripts are dependency-free Python 3 — no packages, no virtual environment:

```bash
cd continental-dollar
python3 analysis/02_two_state_test.py
```

## Related

- [`miguel.es/data`](https://www.miguel.es/data) — these datasets with interactive charts
- Papers drawing on them are listed at [`miguel.es/publications`](https://www.miguel.es/publications)

## Citation

See `CITATION.cff`. Please also cite the underlying primary sources, which are listed in
each dataset's README. The transcription is mine; the data are the sources'.

## Licence

Transcriptions and figures under CC0-1.0; scripts under MIT. See `LICENSE`. The historical
sources are in the public domain; a small number of modern tables are reproduced only as
the specific data identified in the file headers.
