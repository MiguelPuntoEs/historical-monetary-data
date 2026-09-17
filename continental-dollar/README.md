# The Continental Dollar: Depreciation Scales and Market Rates, 1777–1781

Machine-readable transcriptions of the scales of depreciation enacted by the American
states to settle debts contracted in Continental currency, together with contemporary
merchants' book rates of exchange and two further price-based measures.

So far as I can determine, the state-level scales have not previously been available in
machine-readable form. They are usually cited, when cited at all, through the grouped
summary in Bullock (1895) or set aside entirely as unreliable price data.

## Primary sources

- **House Doc. No. 107**, 20th Cong. 1st sess., *Amount of Continental Money issued during the
  Revolutionary War, and the Depreciation of the same* (Washington: Gales & Seaton, 1828) —
  the printing reissued as *American State Papers*, Class III (Finance), vol. V. Carries the
  emissions statement and the state scales at pp. 30–33.
- **Statutes at Large of Pennsylvania** (1904), vol. 10, pp. 283–89 — the Act of 3 April 1781,
  ch. CMXXXV, whose Section IV contains Pennsylvania's enacted scale.
- **Pelatiah Webster**, *Political Essays* (Philadelphia, 1791), p. 501 — four scales,
  including the merchants' book series for Philadelphia and Virginia.
- **Henry Phillips, Jr.**, *Continental Paper Money* (Roxbury, 1866), App. D and pp. 217–18 —
  reproduces the federal state scales and Webster's merchants' columns.
- **Charles J. Bullock**, *The Finances of the United States from 1775 to 1789* (Madison,
  1895), p. 133 — the same state scales, grouped into three tiers.
- **Anne Bezanson**, *Prices and Inflation during the American Revolution* (Philadelphia,
  1951), Table 3, p. 65 — three Philadelphia measures.

## Data

All CSV files carry comment headers (`#`) with source, table reference and page numbers.
Unless stated otherwise, units are **Continental dollars required to purchase one specie
dollar**, so higher values denote greater depreciation.

| File | Description |
|------|-------------|
| `data/published/state_depreciation_scales.csv` | Scales for **seven states** — Massachusetts, Pennsylvania, New Jersey, Delaware, Maryland, Virginia, North Carolina — monthly 1777–81. Pennsylvania is the **enacted statute**; the others are the 1828 federal printing. |
| `data/published/pennsylvania_scale_three_sources.csv` | The Pennsylvania statute set against *American State Papers* and Webster, with the two discrepancies documented |
| `data/published/phillips_1866_merchants_books.csv` | Merchants' book exchange rates, **Philadelphia and Virginia**, monthly Jan 1777 – May 1781 (53 months) |
| `data/published/bullock_1895_grouped_scales.csv` | State scales grouped into three tiers, plus Congress's scale and Jefferson's figures |
| `data/published/bezanson_1951_table3_continental_specie.csv` | Three independent Philadelphia measures: Webster merchants, specie transactions, commodity ratios |
| `data/published/grubb_2023_table6_1_state_quotas.csv` | State shares of congressional quotas, 1775–83 (Grubb's compilation, reproduced for convenience) |

Connecticut, New York and South Carolina appear in the same 1828 source and are **not yet
transcribed**. They are stated as percentages and, for South Carolina, in a
pounds-and-shillings notation that needs care.

## Transcription method

Every figure was transcribed **from page images, not from OCR**. The optical character
recognition available for these volumes corrupts the fractions that pervade the originals
(¼, ½, ¾) and confuses digits in ways that change values materially — Massachusetts'
November and December 1777 entries, for instance, read 800 and 810 under OCR and are 300
and 310 on the page.

Two independent checks support the transcription:

- Bullock's Philadelphia merchant column and Phillips's agree at **15 of the 16** dates
  where both report (the exception is a rounded lowest quotation in April 1779).
- Bezanson's `webster_merchants` column matches the Philadelphia series transcribed here in
  **51 of 52** overlapping months (the exception is April 1779, which she summarises
  differently from a range of quotations).

## What the data show

**The Continental dollar did not have one legal price.** In June 1781 the same currency was
legally worth 100 to one in Massachusetts, 250 in Virginia, 280 in Maryland and 350 in North
Carolina. The Philadelphia and Virginia merchants' quotations track each other for most of the
currency's life and then separate, reaching a ratio of 2.33 by May 1781.

**Pennsylvania's enacted scale fell below its own market in its final months of coverage.**
Against three independent Philadelphia measures the statutory value runs at 0.82, 0.75, 0.75
and 0.68 from November 1780 to February 1781 — and then the schedule ends, because the act
covers only contracts made before 1 March 1781.

> **A source-critical result.** The two standard printed compilations disagree about
> Pennsylvania precisely where the statute is silent. *American State Papers* supplies 125,
> 160 and 225 for March–May 1781; Webster carries 75 forward. **Neither is in the act.** The
> compilations also differ on October 1780, where the statute reads seventy-three: Webster has
> 73, the federal printing 72. Anyone using these tables to build a price series should start
> from `pennsylvania_scale_three_sources.csv`.

## Repository layout

```
data/published/   citable CSVs, each with a source header (table, pages, provenance)
data/working/     same figures, terse column names, used by the scripts
analysis/         four dependency-free scripts — see analysis/README.md
figures/          generated SVGs
```

## Analysis

Dependency-free Python 3 — no packages, no virtual environment.

```bash
python3 analysis/02_two_state_test.py       # the central result
python3 analysis/03_figure_two_markets.py   # -> figures/two_markets.svg
python3 analysis/04_figure_state_scales.py  # -> figures/state_scales.svg
```

`02_two_state_test.py` is the one to read first: it compares Pennsylvania's statute against
the Philadelphia market and Virginia's against the Virginia market, month by month.
`analysis/README.md` documents each script, the units, and the figure conventions.

## Companion dataset

[**greenbacks**](../greenbacks/), in this same collection — prices, wages and the money stock
during the American Civil War, from Wesley C. Mitchell's *A History of the Greenbacks* (1903).
The two together cover the United States' two great paper-money episodes.

## Citation

> González Calvo, Miguel. *The Continental Dollar: Depreciation Scales and Market Rates,
> 1777–1781*. Machine-readable dataset. https://github.com/MiguelPuntoEs/historical-monetary-data

Machine-readable metadata is in `../CITATION.cff`. Please also cite the underlying sources
listed above: the transcription is mine, the data are the statute's, Webster's, Phillips's,
Bullock's, Bezanson's and Grubb's.

## Licence

Transcriptions and figures under CC0-1.0; the scripts under MIT. See `../LICENSE`. The
historical sources are in the public domain; Bezanson (1951) Table 3 and Grubb (2023)
Table 6.1 are reproduced only as the specific data tables identified in the file headers.
