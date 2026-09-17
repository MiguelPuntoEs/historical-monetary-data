"""
Recognition gap: how much of the market's observed depreciation did each state
group's legislated scale actually recognize?

Source: Bullock (1895: 133), reproducing the depreciation scales adopted by law in
the various states (American State Papers, Finance, V: 773 et seq.) alongside
Congress's own scale (ASP Finance V: 763-71) and rates from a Philadelphia
merchant's books.

Market benchmark = midpoint of the Philadelphia merchant range. This is the
contemporaneous market rate Bullock himself uses for comparison, and it is one of
the four evidence types Grubb (2023, ch. 11) evaluates.

recognition ratio = legislated rate / market rate
  1.00  -> the legislature recognized exactly the market depreciation
  < 1   -> the legislature recognized LESS depreciation than the market showed
           (it treated the Continental as worth more than it traded for)
  > 1   -> the legislature recognized MORE depreciation than the market showed

NOTE ON INTERPRETATION: a recognition ratio below 1 does not by itself establish
who gained or lost. The welfare direction depends on the application (private
contracts, loan office certificate settlement, soldiers' depreciation pay) and on
whether the distortion is to the LEVEL at a single date or to the CHANGE between
a borrowing date and a repayment date. See notes/03-incidence-problem.md.
This script measures the gap; it does not assign incidence.
"""

import csv
import os
import statistics

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data", "working", "bullock_depreciation_scales.csv")

GROUPS = {
    "NE (MA/CT/NY)": ("grp1_ne_lo", "grp1_ne_hi"),
    "Mid (PA/NJ/DE/MD/VA)": ("grp2_mid_lo", "grp2_mid_hi"),
    "Carolinas (NC/SC)": ("grp3_car_lo", "grp3_car_hi"),
}


def num(x):
    return float(x) if x not in ("", None) else None


def mid(lo, hi):
    lo, hi = num(lo), num(hi)
    if lo is None and hi is None:
        return None
    if lo is None:
        return hi
    if hi is None:
        return lo
    return (lo + hi) / 2


def main():
    with open(DATA) as f:
        rows = list(csv.DictReader(f))

    print("=" * 100)
    print("RECOGNITION RATIO  (legislated scale / Philadelphia market rate)")
    print("=" * 100)
    hdr = f"{'date':<9}{'market':>8}"
    for g in GROUPS:
        hdr += f"{g:>23}"
    hdr += f"{'Congress':>10}"
    print(hdr)
    print("-" * 100)

    series = {g: [] for g in GROUPS}
    cong_series = []
    spreads = []

    for r in rows:
        market = mid(r["phila_merchant_lo"], r["phila_merchant_hi"])
        line = f"{r['date']:<9}{market:>8.2f}"
        vals_this_date = []
        for g, (lo, hi) in GROUPS.items():
            m = mid(r[lo], r[hi])
            if m is None or market is None:
                line += f"{'--':>23}"
                continue
            ratio = m / market
            series[g].append((r["date"], ratio))
            vals_this_date.append(m)
            line += f"{m:>10.2f} ({ratio:>5.2f})  "
        cong = num(r["congress_rate"])
        if cong and market:
            cr = cong / market
            cong_series.append((r["date"], cr))
            line += f"{cr:>10.2f}"
        else:
            line += f"{'--':>10}"
        print(line)

        # cross-group dispersion among legislated scales at this date
        if len(vals_this_date) == 3:
            spreads.append((r["date"], max(vals_this_date) / min(vals_this_date)))

    print()
    print("=" * 100)
    print("MEAN RECOGNITION RATIO BY PERIOD")
    print("=" * 100)

    def period(d):
        return "1777" if d.startswith("1777") else ("1778" if d.startswith("1778") else "1779-80")

    for g in GROUPS:
        by_p = {}
        for d, v in series[g]:
            by_p.setdefault(period(d), []).append(v)
        out = f"{g:<24}"
        for p in ("1777", "1778", "1779-80"):
            if p in by_p:
                out += f"  {p}: {statistics.mean(by_p[p]):.2f}"
        print(out)
    by_p = {}
    for d, v in cong_series:
        by_p.setdefault(period(d), []).append(v)
    out = f"{'Congress':<24}"
    for p in ("1777", "1778", "1779-80"):
        if p in by_p:
            out += f"  {p}: {statistics.mean(by_p[p]):.2f}"
    print(out)

    print()
    print("=" * 100)
    print("CROSS-GROUP DISPERSION IN LEGISLATED SCALES  (max/min of group midpoints)")
    print("=" * 100)
    for d, s in spreads:
        bar = "#" * int(round((s - 1) * 40))
        print(f"  {d}   {s:>5.2f}x  {bar}")
    if spreads:
        print(f"\n  mean {statistics.mean(s for _, s in spreads):.2f}x   "
              f"max {max(s for _, s in spreads):.2f}x")


if __name__ == "__main__":
    main()
