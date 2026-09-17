"""
Pass-through from greenback depreciation to Northern prices, 1862-1865.

    uv run python analysis/01_pass_through.py

Reproduces Table 1 of "From the Gold Room to Northern Prices: Greenback
Revaluations and Pass-Through in the Union, 1862-1865". Every coefficient,
cumulative effect, N and R-squared in that table comes out of this script.

Two specifications, both in monthly log differences, so coefficients read as
pass-through elasticities:

    (1)  d ln P_t = a + b   d ln G_t + e_t
    (2)  d ln P_t = a + b0  d ln G_t + b1 d ln G_{t-1} + b2 d ln G_{t-2} + e_t

P is a monthly Northern price index; G is the gold price of greenbacks, the
inverse of the monthly average greenback value in gold cents, so a rise in G is
a depreciation. Standard errors are HAC with one monthly lag and no small-sample
correction, which is what the paper reports.

G is built from EH.net's daily quotations, NOT from this repository's own
transcription of the same Mitchell table, which is corrupt. See
FINDINGS_TRANSCRIPTION.md.
"""

import os

import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.sandwich_covariance import cov_hac

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")

START, END = "1862-01-01", "1865-12-01"
HAC_LAGS = 1


def read(filename, column, parse):
    df = pd.read_csv(os.path.join(DATA, filename), comment="#")
    df["date"] = pd.to_datetime(df["date"], format=parse)
    return df.set_index("date")[column].sort_index()


def gold_price_of_greenbacks():
    """Monthly average of daily high/low midpoints, inverted."""
    df = pd.read_csv(os.path.join(DATA, "ehnet_greenback_daily_1862_1878.csv"), comment="#")
    df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
    if (df["lowest"] > df["highest"]).any():
        raise SystemExit("daily series violates the high/low invariant")
    df["midpoint"] = (df["highest"] + df["lowest"]) / 2.0
    value = df.set_index("date")["midpoint"].resample("MS").mean()
    return (100.0 / value).rename("G"), value


def build():
    G, value = gold_price_of_greenbacks()
    general = read("nber_general_price_index_monthly.csv", "general_price_index", "%Y-%m")
    wholesale = read("nber_wholesale_price_index_monthly.csv", "wholesale_price_index", "%Y-%m")

    df = pd.concat(
        [G, value.rename("greenback_value_cents"),
         general.rename("general"), wholesale.rename("wholesale")],
        axis=1, sort=True,
    ).loc[START:END]

    for col in ["G", "general", "wholesale"]:
        df["d_" + col] = np.log(df[col]).diff()
    return df


def fit(y, X):
    aligned = pd.concat([y, X], axis=1).dropna()
    model = sm.OLS(aligned.iloc[:, 0],
                   sm.add_constant(aligned.iloc[:, 1:], has_constant="add")).fit()
    cov = cov_hac(model, nlags=HAC_LAGS, use_correction=False)
    return model, cov, len(aligned)


def cell(b, se):
    return f"{b:.3f} ({se:.3f})"


def estimate(df, dep, label, rows):
    lags = pd.DataFrame({
        "b0": df["d_G"], "b1": df["d_G"].shift(1), "b2": df["d_G"].shift(2),
    })

    m, cov, n = fit(df["d_" + dep], lags[["b0"]])
    i = list(m.params.index).index("b0")
    b = m.params["b0"]
    se = np.sqrt(cov[i, i])
    rows.append([label, "Contemp.", cell(b, se), "", "", cell(b, se), n, round(m.rsquared, 3)])

    m, cov, n = fit(df["d_" + dep], lags)
    idx = {name: k for k, name in enumerate(m.params.index)}
    w = np.zeros(len(m.params))
    for name in ["b0", "b1", "b2"]:
        w[idx[name]] = 1.0
    rows.append([
        label, "DL(0-2)",
        *[cell(m.params[k], np.sqrt(cov[idx[k], idx[k]])) for k in ["b0", "b1", "b2"]],
        cell(float(w @ m.params.values), float(np.sqrt(w @ cov @ w))),
        n, round(m.rsquared, 3),
    ])


def main():
    df = build()
    v = df["greenback_value_cents"]
    print(f"\nSample: {df.index.min():%B %Y} to {df.index.max():%B %Y}, {len(df)} months")
    print(f"Greenback value  {v.iloc[0]:.1f} cents in {v.index[0]:%B %Y}"
          f" -> trough {v.min():.1f} in {v.idxmin():%B %Y}"
          f" -> {v.iloc[-1]:.1f} in {v.index[-1]:%B %Y}")
    for name, col, dp in [("Gold price of greenbacks", "G", 2),
                          ("Wholesale price index", "wholesale", 0),
                          ("General price index", "general", 0)]:
        print(f"  {name:26} peaks {df[col].max():.{dp}f} in {df[col].idxmax():%B %Y}")

    rows = []
    estimate(df, "general", "General price index", rows)
    estimate(df, "wholesale", "Wholesale price index", rows)
    table = pd.DataFrame(rows, columns=[
        "Dependent variable", "Model", "Delta ln G_t", "Lag 1", "Lag 2",
        "Cum. 0-2", "N", "R^2"])

    print("\nTable 1. Monthly pass-through from greenback depreciation to Northern prices")
    print(table.to_string(index=False))
    print(f"\nHAC({HAC_LAGS}) standard errors in parentheses, no small-sample correction.")
    return table


if __name__ == "__main__":
    main()
