"""
Cross-checks between tables that ought to agree.

    uv run python analysis/04_crosscheck.py

Mitchell prints both the individual farm-product series (Table 1A) and the averages
across them (Table 1B). The averages are recomputable, which makes the pair a test of
two independent transcriptions at once: if both are faithful, his printed average
should equal the mean of his own series.

358 of 364 do. The six that do not have been checked digit by digit against the page
on both sides and are reproduced faithfully here, so they are inconsistencies inside
the book rather than transcription errors. They are listed, not corrected — the point
of this collection is to publish what the source says, including where it disagrees
with itself.
"""

import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")

GROUPS = {
    "barley": ["barley_new_york", "barley_chicago", "barley_cincinnati"],
    "clover_seed": ["clover_seed_new_york", "clover_seed_chicago"],
    "corn": ["corn_new_york", "corn_cincinnati"],
    "flax_seed": ["flax_seed_new_york", "flax_seed_cincinnati"],
    "hides": ["hides_cincinnati", "hides_chicago", "hides_new_york"],
    "meat_beeves": ["meat_beeves_cincinnati", "meat_beeves_new_york", "meat_beeves_chicago"],
    "meat_sheep": ["meat_sheep_new_york", "meat_sheep_cincinnati"],
    "meat_pork": ["meat_pork_chicago", "meat_pork_cincinnati", "meat_pork_new_york"],
    "oats": ["oats_new_york", "oats_cincinnati"],
    "rye": ["rye_cincinnati", "rye_new_york"],
    "timothy_seed": ["timothy_seed_cincinnati", "timothy_seed_chicago", "timothy_seed_new_york"],
    "tobacco": ["tobacco_leaf_average_cincinnati", "tobacco_leaf_fine_cincinnati",
                "tobacco_wrappers_ohio_new_york", "tobacco_wrappers_pennsylvania_new_york",
                "tobacco_wrappers_connecticut_new_york", "tobacco_leaf_kentucky_new_york"],
    "wheat": ["wheat_winter_new_york", "wheat_spring_new_york", "wheat_prime_cincinnati",
              "wheat_no2_winter_chicago", "wheat_no2_spring_chicago"],
}

# Verified against the page on both sides; Mitchell's own figures disagree.
KNOWN = {
    ("timothy_seed", "1866-07"), ("timothy_seed", "1861-04"),
    ("meat_sheep", "1865-04"), ("hides", "1866-10"),
    ("meat_pork", "1863-01"), ("meat_pork", "1860-10"),
}
TOL = 0.51          # Mitchell rounds his averages to whole numbers


def read(name):
    path = os.path.join(DATA, name)
    return {r["date"]: r for r in csv.DictReader(l for l in open(path) if not l.startswith("#"))}


def main():
    a = read("mitchell_appendix_b_table1a_farm_individual.csv")
    b = read("mitchell_appendix_b_table1b_averages.csv")

    agree = unexplained = 0
    noted = []
    for product, cols in GROUPS.items():
        for date, row in a.items():
            vals = [float(row[c]) for c in cols if row[c]]
            if not vals:
                continue
            mean = sum(vals) / len(vals)
            printed = float(b[date][product])
            if abs(mean - printed) <= TOL:
                agree += 1
            elif (product, date) in KNOWN:
                noted.append((product, date, mean, printed))
            else:
                unexplained += 1
                print(f"  UNEXPLAINED  {product} {date}: series mean {mean:.1f}, printed {printed:g}")

    total = agree + len(noted) + unexplained
    print(f"  Table 1B averages vs the mean of Table 1A series: {agree} of {total} agree")
    print(f"\n  {len(noted)} disagree in the source itself, verified against the page on both sides:")
    for product, date, mean, printed in sorted(noted, key=lambda r: -abs(r[2] - r[3])):
        print(f"    {product:14} {date}   mean of his series {mean:>6.1f}   his printed average {printed:>5g}")
    if unexplained:
        print(f"\n  {unexplained} unexplained — a transcription error is likely.")
    return 1 if unexplained else 0


if __name__ == "__main__":
    raise SystemExit(main())
