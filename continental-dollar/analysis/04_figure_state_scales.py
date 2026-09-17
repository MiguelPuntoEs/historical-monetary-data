"""
Figure 3: four states' legislated scales of depreciation, 1777-1781, log scale.

Massachusetts, Virginia, Maryland and North Carolina adopted near-identical scales
through 1779, then fan apart. North Carolina separates furthest during the British
southern campaign (Charleston May 1780; Camden; Cowpens; Guilford Courthouse Mar
1781). By June 1781 the same Continental dollar was legally worth 100 to one in
Massachusetts and 350 to one in North Carolina.

Massachusetts' scale is monthly ("per cent") through April 1780 and DATE-specific
thereafter; months take the dated observation nearest mid-month, and months with no
dated observation are left blank rather than interpolated.

Source: Phillips (1866, 206, 208-209), transcribed from page images.
"""

import csv
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "shared"))
from _theme import (SERIES, TEXT, MUTED, GRID, AXIS,  # noqa: E402
                    SURFACE, FONT, INK)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "figures", "state_scales.svg")
DATA = os.path.join(HERE, "..", "data", "working", "phillips_state_scales.csv")

SERIES = [("North Carolina", "nc_scale", "#eb6834"),
          ("Maryland", "md_scale", SERIES[2]),
          ("Virginia", "va_scale", SERIES[0]),
          ("Massachusetts", "ma_scale", SERIES[3])]

SEC, SURF = MUTED, SURFACE
BAND = INK["band"]
W, H = 900, 500
ML, MR, MT, MB = 62, 26, 34, 92
PW, PH = W - ML - MR, H - MT - MB
YLO, YHI = 1.0, 1200.0


def main():
    rows = [r for r in csv.DictReader(open(DATA)) if r.get("date")]
    idx = {r["date"]: i for i, r in enumerate(rows)}
    xmax = len(rows) - 1

    def xp(i):
        return ML + (i / xmax) * PW

    def yp(v):
        lo, hi = math.log10(YLO), math.log10(YHI)
        return MT + (1 - (math.log10(v) - lo) / (hi - lo)) * PH

    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
         f'font-family="{FONT}">',
         f'<rect width="{W}" height="{H}" fill="{SURF}"/>']

    # southern campaign shading, behind the grid
    a, b = idx.get("1780-05"), idx.get("1781-03")
    if a is not None and b is not None:
        s.append(f'<rect x="{xp(a):.1f}" y="{MT}" width="{xp(b)-xp(a):.1f}" height="{PH}" fill="{BAND}"/>')
        s.append(f'<text x="{(xp(a)+xp(b))/2:.1f}" y="{MT+15}" text-anchor="middle" font-size="10.5" '
                 f'fill="{MUTED}">British southern campaign</text>')

    for g in (1, 3, 10, 30, 100, 300, 1000):
        y = yp(g)
        s.append(f'<line x1="{ML}" x2="{ML+PW}" y1="{y:.1f}" y2="{y:.1f}" stroke="{GRID}" stroke-width="1"/>')
        s.append(f'<text x="{ML-10}" y="{y+4:.1f}" text-anchor="end" font-size="11.5" fill="{MUTED}">{g}</text>')
    s.append(f'<text x="{ML-52}" y="{MT-14}" font-size="11.5" fill="{MUTED}">Continental $ per specie $ (log)</text>')

    s.append(f'<line x1="{ML}" x2="{ML+PW}" y1="{MT+PH}" y2="{MT+PH}" stroke="{AXIS}" stroke-width="1"/>')
    for d in ("1777-01", "1778-01", "1779-01", "1780-01", "1781-01", "1781-12"):
        if d not in idx:
            continue
        i = idx[d]
        anchor = "start" if i == 0 else ("end" if i == xmax else "middle")
        s.append(f'<line x1="{xp(i):.1f}" x2="{xp(i):.1f}" y1="{MT+PH}" y2="{MT+PH+5}" stroke="{AXIS}" stroke-width="1"/>')
        s.append(f'<text x="{xp(i):.1f}" y="{MT+PH+20}" text-anchor="{anchor}" font-size="11" '
                 f'fill="{SEC}">{d[:4] if i != xmax else "Dec 1781"}</text>')

    ends = []
    for name, col, colr in SERIES:
        pts = [(i, float(r[col])) for i, r in enumerate(rows) if r[col]]
        d = ""
        for j, (i, v) in enumerate(pts):
            d += (" M " if j == 0 else " L ") + f"{xp(i):.1f} {yp(v):.1f}"
        s.append(f'<path d="{d}" fill="none" stroke="{colr}" stroke-width="2" stroke-linejoin="round"/>')
        ends.append((name, colr, pts[-1][0], yp(pts[-1][1])))

    # inside labels, right-aligned at each series' own end, de-conflicted vertically
    ends.sort(key=lambda e: e[3])
    placed = []
    for name, colr, i, y in ends:
        ly = y + 4
        while any(abs(ly - p) < 15 for p in placed):
            ly += 15
        placed.append(ly)
        s.append(f'<text x="{xp(i)-7:.1f}" y="{ly:.1f}" text-anchor="end" font-size="12" '
                 f'fill="{SEC}" font-weight="600">{name}</text>')

    # legend
    ly = H - 22
    for k, (name, _, colr) in enumerate(SERIES):
        lx = ML + k * 200
        s.append(f'<rect x="{lx}" y="{ly-4}" width="16" height="3" rx="1.5" fill="{colr}"/>')
        s.append(f'<text x="{lx+23}" y="{ly+1}" font-size="12" fill="{SEC}">{name}</text>')

    s.append("</svg>")
    open(OUT, "w").write("\n".join(s))
    print("wrote", os.path.normpath(OUT))
    for d in ("1779-06", "1780-01", "1780-06", "1780-11", "1781-02", "1781-06"):
        r = rows[idx[d]]
        print(f"  {d}  MA {r['ma_scale'] or '--':>7}  VA {r['va_scale'] or '--':>7}"
              f"  MD {r['md_scale'] or '--':>7}  NC {r['nc_scale'] or '--':>7}")


if __name__ == "__main__":
    main()
