# American Civil War: Greenback Prices and Wages

Economic data from the American Civil War era, focusing on the effects of greenback currency issuance on prices, wages, and the money supply (1859-1866).

## Primary source

Wesley C. Mitchell, *A History of the Greenbacks: With Special Reference to the Economic Consequences of Their Issue, 1862-65* (University of Chicago Press, 1903).

> **Warning.** Six files have been checked against Mitchell's printed pages. **Four were
> wrong.** One has been re-transcribed; three are quarantined in `data/suspect/`. Five
> remain unverified and should be assumed wrong until checked. Do not cite this dataset —
> see
> [`FINDINGS_TRANSCRIPTION.md`](FINDINGS_TRANSCRIPTION.md). The monthly gold price table
> is verified correct, all 48 rows.

## Data

All CSV files include comment headers (`#`) with source, table reference, and page numbers. Most price/wage series are index numbers with base = 100.

Two files are not transcriptions and say so in their headers: the NBER price indices and the
EH.net daily greenback quotations, both fetched by `analysis/00_fetch_sources.py`.

### Appendix A -- Gold prices

| File | Description |
|------|-------------|
| `mitchell_appendix_a_table1_gold_prices_1862_1865.csv` | Monthly highest, average, and lowest gold price of $100 paper currency (New York) |
| `ehnet_greenback_daily_1862_1878.csv` | Daily highest and lowest gold prices, 5,170 trading days. EH.net's digitization of Appendix A Table 2, **not my transcription** — mine is corrupt, see `FINDINGS_TRANSCRIPTION.md` |

### Appendix B -- Commodity prices

| File | Description |
|------|-------------|
| `mitchell_appendix_b_table1_averages_combined.csv` | Farm product price averages, quarterly 1860-1866 |
| `mitchell_appendix_b_table1_farm_individual.csv` | Farm product prices by city (NY, Chicago, Cincinnati), quarterly 1860-1866 |
| `mitchell_appendix_b_table2_wholesale_prices.csv` | ~120 commodity series at wholesale, quarterly 1860-1865 |
| `mitchell_appendix_b_table3_government_prices.csv` | Prices paid by federal government for supplies (War Dept, Navy), annual 1860-1865 |
| `mitchell_appendix_b_table4_retail_prices.csv` | Retail prices of dry goods, groceries, provisions, and fuel by town, annual 1860-1866 |
| `mitchell_appendix_b_table5_wholesale_vs_retail.csv` | Comparison of 23 commodities at wholesale vs. retail |

### Appendix C -- Wages

| File | Description |
|------|-------------|
| `mitchell_appendix_c_table1_wages_part1.csv` | Wage series from the Aldrich Report, pp. 470-495 (semi-annual, by industry/occupation/location) |
| `mitchell_appendix_c_table1_wages_part2.csv` | Wage series continued, pp. 496-517 |
| `mitchell_appendix_c_table2_census_wages.csv` | Wage series from Vol. XX of the Tenth Census |

### Other sources

| File | Description |
|------|-------------|
| `mitchell_table_v_greenbacks_currency.csv` | Currency of the loyal states, fiscal years 1860-1866 |
| `Cj26-41_money_stock_1859_1866.csv` | Stock of money and components, 1859-1866 (Friedman, Schwartz, and Mitchell). From [Historical Statistics of the United States](https://hsus.cambridge.org/HSUSWeb/toc/showTableIdCj1-107.html), Millennial Edition |

## Analysis

`analysis/` holds the scripts. `make` runs validation and then the pass-through estimates,
which reproduce Table 1 of the pass-through paper exactly. See `analysis/README.md`.

## Notebooks

Exploratory, superseded by `analysis/`. Both read the corrupt daily file and their
pass-through figures should not be trusted.

- `gold_prices_plot.ipynb` -- Plot of monthly gold prices with high-low range
- `reproduce_greenback_paper_notebook_style.ipynb` -- earlier version of the analysis

## References

- Mitchell, Wesley C. *A History of the Greenbacks* (1903)
- Friedman, Milton and Anna J. Schwartz. *Monetary Statistics of the United States* (1970), Table 13
- Willard, Guinnane, and Rosen. "Turning Points in the Civil War: Views from the Greenback Market" (1996)
- Historical Statistics of the United States, Millennial Edition (Cambridge University Press, 2006), Table Cj26-41

## Companion dataset

[**continental-dollar**](../continental-dollar/), in this same collection — the depreciation
scales enacted by seven states to settle debts in Continental currency, 1777–1781, with
contemporary merchants' quotations. The two together cover the United States' two great
paper-money episodes.

## Setup

The notebooks need the collection's environment, which lives at the repository root:

```bash
cd .. && uv sync
```

Requires Python >= 3.13.

## Citation

See `../CITATION.cff`, and please also cite Mitchell (1903) and the other sources listed
above: the transcription is mine, the data are theirs.

## Licence

Transcriptions under CC0-1.0; the notebooks under MIT. See `../LICENSE`.
