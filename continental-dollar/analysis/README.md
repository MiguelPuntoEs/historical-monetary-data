# Analysis

Four scripts. Dependency-free Python 3 — no packages, no virtual environment, no
`requirements.txt`. Run any of them from the repository root.

| Script | Produces | Reads |
|---|---|---|
| `01_recognition_gap.py` | Table 2 — grouped state scales against the Philadelphia benchmark, and the cross-group spread | `data/working/bullock_depreciation_scales.csv` |
| `02_two_state_test.py` | **The central result.** Each state's scale against its *own* local market, month by month, with period summaries | `data/working/phillips_state_scales.csv` |
| `03_figure_two_markets.py` | `figures/two_markets.svg` — Philadelphia and Virginia quotations, 53 months, log scale | `data/working/phillips_state_scales.csv` |
| `04_figure_state_scales.py` | `figures/state_scales.svg` — four states' legislated scales, log scale | `data/working/phillips_state_scales.csv` |

Read `02_two_state_test.py` first. It compares Pennsylvania's statute against Philadelphia
quotations and Virginia's against Virginia quotations, which is the comparison the whole
argument rests on.

## Conventions

**Units.** Continental dollars required to purchase one specie dollar. Higher values mean
greater depreciation. Where a source gives a range of quotations for a month, the midpoint is
used and the range is retained in the data.

**Figures** are emitted as hand-written SVG rather than plotted with matplotlib, so the repo
stays dependency-free, and converted to PDF for LaTeX by `06_figures_to_pdf.py`.

**Colours and type** come from `_theme.py`, which reads `chart-theme.json` at the repository
root. That file is exported from the house chart style on the website
(`src/charts/theme.js`), so a figure in the paper and a chart on the site use one palette.
`_theme.py` carries a fallback so the scripts still run standalone. The palette is
colourblind-safe: fixed order, checked for CVD separation and for contrast against white.

## Reproducing

```bash
python3 analysis/02_two_state_test.py      # the central result
python3 analysis/03_figure_two_markets.py  # regenerate figures/
python3 analysis/04_figure_state_scales.py
```

Every number in the accompanying paper's tables was generated or checked by these scripts
against the CSVs in `data/`.
