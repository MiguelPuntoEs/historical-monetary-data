"""
The two-state test: did each state's legislated scale track ITS OWN local market?

Phillips (1866, 218) gives merchants' book rates for Philadelphia and for Virginia.
Pennsylvania's local market is Philadelphia; Virginia's is Virginia. So two states
can be tested against their own local prices, not just one.

Result (see output): both scales reproduce their own local market exactly through
March 1779. From October 1780 Virginia continues to match exactly, while
Pennsylvania falls BELOW the Philadelphia market. The "real vs political" answer is
therefore not uniform.
"""
import csv, os

HERE = os.path.dirname(os.path.abspath(__file__))
rows = [r for r in csv.DictReader(open(os.path.join(HERE, "..", "data", "working",
        "phillips_state_scales.csv"))) if r.get("date")]

def f(x): return float(x) if x not in ("", None) else None

print("=" * 96)
print("EACH STATE'S LEGISLATED SCALE vs ITS OWN LOCAL MARKET")
print("=" * 96)
print(f"{'date':<10}{'PA scale':>10}{'Phila mkt':>11}{'PA/mkt':>9}"
      f"{'   ':>3}{'VA scale':>10}{'VA mkt':>9}{'VA/mkt':>9}")
print("-" * 96)

pa_hits = pa_n = va_hits = va_n = 0
pa_ratios, va_ratios = [], []
for r in rows:
    lo, hi = f(r["phila_merch_lo"]), f(r["phila_merch_hi"])
    if lo is None: continue
    ph = (lo + hi) / 2
    pa, va, vm = f(r["pa_scale"]), f(r["va_scale"]), f(r["va_merch"])
    line = f"{r['date']:<10}"
    if pa is not None:
        pa_n += 1; rr = pa / ph; pa_ratios.append(rr)
        if abs(pa - ph) < 1e-9: pa_hits += 1
        line += f"{pa:>10.1f}{ph:>11.1f}{rr:>9.2f}"
    else:
        line += f"{'--':>10}{ph:>11.1f}{'--':>9}"
    line += "   "
    if va is not None and vm is not None:
        va_n += 1; rr = va / vm; va_ratios.append(rr)
        if abs(va - vm) < 1e-9: va_hits += 1
        line += f"{va:>10.1f}{vm:>9.1f}{rr:>9.2f}"
    print(line)

print()
print(f"  Pennsylvania scale == Philadelphia market : {pa_hits} of {pa_n} months"
      f"   (mean ratio {sum(pa_ratios)/len(pa_ratios):.3f})")
print(f"  Virginia scale     == Virginia market     : {va_hits} of {va_n} months"
      f"   (mean ratio {sum(va_ratios)/len(va_ratios):.3f})")

print()
print("=" * 96)
print("SPLIT BY PERIOD")
print("=" * 96)
for label, test in (("through Mar 1779", lambda d: d < "1779-04"),
                    ("Oct 1780 onward",  lambda d: d >= "1780-10")):
    ph_h = ph_n = v_h = v_n = 0; pr, vr = [], []
    for r in rows:
        if not test(r["date"]): continue
        lo, hi = f(r["phila_merch_lo"]), f(r["phila_merch_hi"])
        if lo is None: continue
        ph = (lo + hi) / 2
        pa, va, vm = f(r["pa_scale"]), f(r["va_scale"]), f(r["va_merch"])
        if pa is not None:
            ph_n += 1; pr.append(pa/ph)
            if abs(pa-ph) < 1e-9: ph_h += 1
        if va is not None and vm is not None:
            v_n += 1; vr.append(va/vm)
            if abs(va-vm) < 1e-9: v_h += 1
    print(f"  {label:<18} PA exact {ph_h}/{ph_n} (mean {sum(pr)/len(pr):.3f})"
          f"   VA exact {v_h}/{v_n} (mean {sum(vr)/len(vr):.3f})")
