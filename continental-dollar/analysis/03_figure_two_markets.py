"""
Figure 2: the Philadelphia and Virginia markets for the Continental dollar,
January 1777 - May 1781, log scale.

The two series are near-identical through 1779 and then separate, reaching a ratio
of 2.33 by May 1781. Source: Phillips (1866, 217-218), reproducing the tables of
depreciation in Webster's Essays, p. 501; transcribed from page images. Midpoints
where a range of quotations is given.
"""
import csv
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "shared"))
from _theme import SERIES, TEXT, MUTED, GRID, AXIS, SURFACE, FONT  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "figures", "two_markets.svg")
DATA = os.path.join(HERE, "..", "data", "working", "phillips_state_scales.csv")

PHILA, VA = SERIES[0], SERIES[1]
SEC, SURF = MUTED, SURFACE
W, H = 900, 500
ML, MR, MT, MB = 62, 26, 34, 92
PW, PH = W - ML - MR, H - MT - MB
YLO, YHI = 1.0, 420.0


def main():
    rows = [r for r in csv.DictReader(open(DATA)) if r["va_merch"]]
    n = len(rows) - 1
    xp = lambda i: ML + (i / n) * PW
    lo_, hi_ = math.log10(YLO), math.log10(YHI)
    yp = lambda v: MT + (1 - (math.log10(v) - lo_) / (hi_ - lo_)) * PH
    mid = lambda r: (float(r["phila_merch_lo"]) + float(r["phila_merch_hi"])) / 2

    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
         f'font-family="{FONT}">',
         f'<rect width="{W}" height="{H}" fill="{SURF}"/>']

    for g in (1, 2, 5, 10, 20, 50, 100, 200, 400):
        y = yp(g)
        s.append(f'<line x1="{ML}" x2="{ML+PW}" y1="{y:.1f}" y2="{y:.1f}" stroke="{GRID}" stroke-width="1"/>')
        s.append(f'<text x="{ML-10}" y="{y+4:.1f}" text-anchor="end" font-size="11.5" fill="{MUTED}">{g}</text>')
    s.append(f'<text x="{ML-52}" y="{MT-14}" font-size="11.5" fill="{MUTED}">Continental $ per specie $ (log)</text>')

    s.append(f'<line x1="{ML}" x2="{ML+PW}" y1="{MT+PH}" y2="{MT+PH}" stroke="{AXIS}" stroke-width="1"/>')
    idx = {r["date"]: i for i, r in enumerate(rows)}
    for d, lab in (("1777-01", "1777"), ("1778-01", "1778"), ("1779-01", "1779"),
                   ("1780-01", "1780"), ("1781-01", "1781")):
        if d not in idx: continue
        i = idx[d]
        anchor = "start" if i == 0 else ("end" if i == n else "middle")
        s.append(f'<line x1="{xp(i):.1f}" x2="{xp(i):.1f}" y1="{MT+PH}" y2="{MT+PH+5}" stroke="{AXIS}" stroke-width="1"/>')
        s.append(f'<text x="{xp(i):.1f}" y="{MT+PH+20}" text-anchor="{anchor}" font-size="11" fill="{SEC}">{lab}</text>')

    for name, colr, get in (("Philadelphia", PHILA, mid),
                            ("Virginia", VA, lambda r: float(r["va_merch"]))):
        d = ""
        for j, r in enumerate(rows):
            d += (" M " if j == 0 else " L ") + f"{xp(j):.1f} {yp(get(r)):.1f}"
        s.append(f'<path d="{d}" fill="none" stroke="{colr}" stroke-width="2" stroke-linejoin="round"/>')
        for j, r in enumerate(rows):
            s.append(f'<circle cx="{xp(j):.1f}" cy="{yp(get(r)):.1f}" r="2.6" fill="{colr}" '
                     f'stroke="{SURF}" stroke-width="1.4"/>')

    s.append(f'<text x="{xp(n)-8:.1f}" y="{yp(350.0)-10:.1f}" text-anchor="end" font-size="12.5" '
             f'fill="{SEC}" font-weight="600">Philadelphia</text>')
    s.append(f'<text x="{xp(n)-8:.1f}" y="{yp(150.0)+22:.1f}" text-anchor="end" font-size="12.5" '
             f'fill="{SEC}" font-weight="600">Virginia</text>')
    ytop, ybot = yp(350.0), yp(150.0)
    bx = xp(n) - 3
    s.append(f'<line x1="{bx:.1f}" x2="{bx:.1f}" y1="{ytop:.1f}" y2="{ybot:.1f}" stroke="{MUTED}" stroke-width="1"/>')
    s.append(f'<text x="{bx-6:.1f}" y="{(ytop+ybot)/2+4:.1f}" text-anchor="end" font-size="11.5" '
             f'fill="{SEC}" font-weight="600">2.33×</text>')
    s.append(f'<text x="{xp(idx["1778-06"]):.1f}" y="{yp(5.0)-14:.1f}" text-anchor="middle" '
             f'font-size="11.5" fill="{SEC}">one price</text>')

    ly = H - 22
    for k, (name, colr) in enumerate([("Philadelphia merchants' books", PHILA),
                                      ("Virginia merchants' books", VA)]):
        lx = ML + k * 250
        s.append(f'<rect x="{lx}" y="{ly-4}" width="16" height="3" rx="1.5" fill="{colr}"/>')
        s.append(f'<text x="{lx+23}" y="{ly+1}" font-size="12" fill="{SEC}">{name}</text>')

    s.append("</svg>")
    open(OUT, "w").write("\n".join(s))
    print("wrote", os.path.normpath(OUT), f"({len(rows)} months)")


if __name__ == "__main__":
    main()
