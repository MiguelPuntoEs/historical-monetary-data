"""
Reshape the wide source tables into one tidy file per table.

    uv run python analysis/03_build_tidy.py

Two forms, one truth. The wide files in data/ mirror the printed page column for
column, which is what makes them checkable against Mitchell by eye — the only way
these tables can actually be verified. The tidy files in data/tidy/ are what you
analyse: one observation per row, every value carrying its own keys.

The tidy files are derived and must never be edited. Fix the wide file and re-run.

This split is not housekeeping. Every structural error found in this dataset was a
value sliding sideways into the wrong column where Mitchell printed "...." for a
missing quotation. In a wide table that is invisible; in a tidy one it cannot be
expressed, because the key travels with the value.
"""

import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
OUT = os.path.join(DATA, "tidy")

# filename -> (key columns, name for the melted column, name for the value column)
TABLES = {
    "mitchell_appendix_b_table1a_farm_individual.csv": (["date"], "series", "relative_price"),
    "mitchell_appendix_b_table1b_averages.csv": (["date"], "product", "relative_price"),
    "mitchell_appendix_b_table3_government_prices.csv": (
        ["section", "item"], "year", "relative_price"),
    "mitchell_appendix_b_table5_wholesale_vs_retail.csv": (
        ["commodity", "channel", "number_of_price_series"], "year", "relative_price"),
}


def provenance(path):
    return [l.rstrip("\n") for l in open(path) if l.startswith("#")]


def tidy(filename, keys, var, val):
    path = os.path.join(DATA, filename)
    rows = list(csv.DictReader(l for l in open(path) if not l.startswith("#")))
    header = list(rows[0].keys())
    melt = [c for c in header if c not in keys]

    out = []
    for r in rows:
        for c in melt:
            v = (r[c] or "").strip()
            if v == "":
                continue          # a gap in the source stays a gap, not a zero
            out.append([r[k] for k in keys] + [c.replace("year_", ""), v])

    dest = os.path.join(OUT, filename.replace(".csv", "_tidy.csv"))
    with open(dest, "w", newline="") as f:
        for line in provenance(path):
            f.write(line + "\n")
        f.write("#\n# DERIVED from ../%s by analysis/03_build_tidy.py. Do not edit.\n" % filename)
        w = csv.writer(f)
        w.writerow(keys + [var, val])
        w.writerows(out)
    dropped = len(rows) * len(melt) - len(out)
    print(f"  {os.path.basename(dest):<52} {len(out):>6} rows  ({dropped} empty cells omitted)")


def main():
    os.makedirs(OUT, exist_ok=True)
    for filename, (keys, var, val) in TABLES.items():
        if os.path.exists(os.path.join(DATA, filename)):
            tidy(filename, keys, var, val)


if __name__ == "__main__":
    main()
