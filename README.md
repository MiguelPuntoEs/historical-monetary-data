# American Civil War: Greenback Prices and Wages

Economic data from the American Civil War era, focusing on the effects of greenback currency issuance on prices, wages, and the money supply (1859-1866).

## Primary source

Wesley C. Mitchell, *A History of the Greenbacks: With Special Reference to the Economic Consequences of Their Issue, 1862-65* (University of Chicago Press, 1903).

## Data

All CSV files include comment headers (`#`) with source, table reference, and page numbers. Most price/wage series are index numbers with base = 100.

### Appendix A -- Gold prices

| File | Description |
|------|-------------|
| `mitchell_appendix_a_table1_gold_prices_1862_1865.csv` | Monthly highest, average, and lowest gold price of $100 paper currency (New York) |
| `mitchell_appendix_a_table2_daily_gold_prices.csv` | Daily highest and lowest gold prices, ~1,228 trading days |

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

## Notebooks

- `gold_prices_plot.ipynb` -- Plot of monthly gold prices with high-low range
- `reproduce_greenback_paper_notebook_style.ipynb` -- Analysis notebook

## References

- Mitchell, Wesley C. *A History of the Greenbacks* (1903)
- Friedman, Milton and Anna J. Schwartz. *Monetary Statistics of the United States* (1970), Table 13
- Willard, Guinnane, and Rosen. "Turning Points in the Civil War: Views from the Greenback Market" (1996)
- Historical Statistics of the United States, Millennial Edition (Cambridge University Press, 2006), Table Cj26-41

## Setup

```bash
uv sync
```

Requires Python >= 3.13.
