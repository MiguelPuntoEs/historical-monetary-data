"""
Fetch the two external series the pass-through regressions need, and write them
into data/ with provenance headers.

    uv run python analysis/00_fetch_sources.py

The results are committed, so nothing downstream touches the network. This script
exists to record where those files came from and to let them be refreshed, not
because it needs running: an analysis whose numbers depend on what a web service
returns on the day is not reproducible, and these regressions are sensitive to the
inputs at the third decimal.

Neither file is my transcription, and both say so in their header. The collection's
CC0 grant covers my own work, not these.
"""

import io
import os
import urllib.request

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")

FRED = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={}"
EHNET = "https://eh.net/wp-content/uploads/2013/11/greenback.txt"

# Divergences found between EH.net and Mitchell's printed page, confirmed against the
# book. They are recorded rather than corrected: this file is EH.net's digitization,
# and silently editing it would make it something else. Nothing downstream depends on
# them — patching this one and re-running 01_pass_through.py leaves every coefficient
# in the paper's Table 1 unchanged to three decimals.
EHNET_DIVERGENCES = [
    ("1862-01-15", "lowest", "97.32", "97.33", "p. 425"),
]

PRICE_SERIES = {
    "nber_general_price_index_monthly.csv": dict(
        id="M04051USM324NNBR",
        column="general_price_index",
        title="Index of the General Price Level for United States",
        units="Index, 1913 = 100, not seasonally adjusted",
        notes=(
            "Weighted index combining industrial prices (10), farm prices (10), retail\n"
            "# food in 51 cities (10), rents in 32 cities (5), clothing and furnishings\n"
            "# (10), transportation (5), real estate (10), securities (10), equipment\n"
            "# (10), hardware (3), automobiles (2) and Federal Reserve wages (15)."
        ),
    ),
    "nber_wholesale_price_index_monthly.csv": dict(
        id="M0448AUSM323NNBR",
        column="wholesale_price_index",
        title="Index of Wholesale Prices, Variable Group Weights for United States",
        units="Index, 1910-1914 = 100, not seasonally adjusted",
        notes=(
            "Compiled from G. F. Warren and F. A. Pearson, *Prices* (1933), 12-13.\n"
            "# NBER Macrohistory series m04048a, chapter 4."
        ),
    ),
}


def get(url):
    with urllib.request.urlopen(url, timeout=60) as r:
        return r.read().decode("utf-8", errors="replace")


def fetch_price_indices():
    for filename, s in PRICE_SERIES.items():
        df = pd.read_csv(io.StringIO(get(FRED.format(s["id"]))))
        df.columns = [c.strip() for c in df.columns]
        date_col = next(c for c in df.columns if "date" in c.lower())
        value_col = next(c for c in df.columns if c != date_col)
        df = df[[date_col, value_col]].rename(
            columns={date_col: "date", value_col: s["column"]}
        )
        df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m")
        df[s["column"]] = pd.to_numeric(df[s["column"]], errors="coerce")

        # Coverage is read off the data, not off the series page: FRED's stated
        # range and what the CSV actually contains do not always agree.
        header = (
            f"# {s['title']}\n"
            f"# National Bureau of Economic Research, {s['title']}\n"
            f"# [{s['id']}], retrieved from FRED, Federal Reserve Bank of St. Louis,\n"
            f"# https://fred.stlouisfed.org/series/{s['id']}\n"
            f"#\n"
            f"# Units: {s['units']}\n"
            f"# Frequency: monthly, dated to the first of the month\n"
            f"# Coverage: {df['date'].iloc[0]} to {df['date'].iloc[-1]}, {len(df)} observations\n"
            f"#\n"
            f"# {s['notes']}\n"
            f"#\n"
            f"# Redistributed under FRED's citation requirement. Not my transcription,\n"
            f"# and not covered by this repository's CC0 grant.\n"
        )
        write(filename, header, df)


def fetch_greenback_daily():
    """EH.net's digitization of Mitchell's daily quotations.

    Preferred here over the transcription in this repository, which is corrupt:
    see FINDINGS_TRANSCRIPTION.md. Its records are the ones the pass-through paper
    was estimated on.
    """
    rows = []
    for line in get(EHNET).splitlines():
        p = line.split()
        if len(p) == 5 and p[0].isdigit() and len(p[1]) == 6:
            try:
                rows.append((p[1], float(p[3]), float(p[4])))
            except ValueError:
                continue
    df = pd.DataFrame(rows, columns=["yymmdd", "highest", "lowest"])
    yy = df["yymmdd"].str[:2].astype(int)
    century = np.where(yy < 50, 2000 + yy, 1800 + yy).astype(str)
    df["date"] = pd.to_datetime(
        century + df["yymmdd"].str[2:4] + df["yymmdd"].str[4:6], format="%Y%m%d"
    )
    df = df.sort_values("date").reset_index(drop=True)
    df["date"] = df["date"].dt.strftime("%Y-%m-%d")
    df = df[["date", "highest", "lowest"]]

    inverted = int((df["lowest"] > df["highest"]).sum())
    if inverted:
        raise SystemExit(f"EH.net series has {inverted} rows with lowest > highest")

    header = (
        "# Daily gold value of $100 in United States currency, 1862-1878\n"
        "# EH.net, \"Greenback Series\", https://eh.net/database/greenback-series/\n"
        "# A digitization of the daily quotations in Wesley C. Mitchell,\n"
        "# *A History of the Greenbacks* (University of Chicago Press, 1903),\n"
        "# Appendix A, Table 2. Contact given as Harvey Rosen, Princeton University;\n"
        "# the series underlies Willard, Guinnane and Rosen (1996).\n"
        "#\n"
        "# Units: gold dollars per $100 of paper currency. 100 is parity; lower values\n"
        "# mean greater depreciation of greenbacks against gold.\n"
        f"# Coverage: {df['date'].iloc[0]} to {df['date'].iloc[-1]}, {len(df)} trading days\n"
        "#\n"
        "# NOT MY TRANSCRIPTION. It is included because this repository's own\n"
        "# transcription of the same Mitchell table is unreliable — 168 of its 1,228\n"
        "# wartime rows record a low above the high — and because the pass-through\n"
        "# paper was estimated on these values. See FINDINGS_TRANSCRIPTION.md.\n"
        "# Verified on write: no row has lowest > highest.\n"
        "#\n"
        "# Checked against the page for January 1862 (p. 425): 17 of 18 trading days\n"
        "# match exactly. Known divergences from Mitchell, recorded not corrected:\n"
        + "".join(f"#   {d}  {col} reads {got} here, {want} in Mitchell, {where}\n"
                 for d, col, got, want, where in EHNET_DIVERGENCES)
    )
    write("ehnet_greenback_daily_1862_1878.csv", header, df)


def write(filename, header, df):
    path = os.path.join(DATA, filename)
    with open(path, "w") as f:
        f.write(header)
        df.to_csv(f, index=False)
    print(f"  {filename:<44} {len(df):>5} rows  {df.iloc[0, 0]} to {df.iloc[-1, 0]}")


if __name__ == "__main__":
    fetch_price_indices()
    fetch_greenback_daily()
