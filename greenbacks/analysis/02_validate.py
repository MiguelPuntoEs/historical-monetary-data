"""
Invariant checks over every CSV in data/.

    uv run python analysis/02_validate.py

These are the checks that should have been run when the files were transcribed.
They are cheap, they are mechanical, and one of them would have caught the corrupt
daily series years earlier: see FINDINGS_TRANSCRIPTION.md.

Nothing here judges whether a value is *right* — only whether a file contradicts
itself in a way the printed source could not have. data/suspect/ is skipped; it
holds files that already failed.
"""

import glob
import os
import sys

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")

# A high must not fall below a low, and an average must lie between them.
ORDERED = ["lowest", "average", "highest"]


def check(path):
    """Return a list of complaints about one file."""
    name = os.path.basename(path)
    problems = []
    try:
        df = pd.read_csv(path, comment="#")
    except pd.errors.ParserError as e:
        # A ragged row is itself a finding, not a reason to stop.
        return name, 0, [f"will not parse: {e}"]

    present = [c for c in ORDERED if c in df.columns]
    for lo, hi in zip(present, present[1:]):
        bad = df[pd.to_numeric(df[lo], errors="coerce")
                 > pd.to_numeric(df[hi], errors="coerce")]
        if len(bad):
            pct = 100 * len(bad) / len(df)
            problems.append(f"{len(bad)} of {len(df)} rows ({pct:.1f}%) have {lo} > {hi}")

    if "date" in df.columns:
        d = pd.to_datetime(df["date"], errors="coerce")
        if d.isna().any():
            problems.append(f"{int(d.isna().sum())} unparseable dates")
        # Guessing which columns form the key produces false alarms: these files
        # are a mix of wide and long, and a long file legitimately repeats a date
        # once per series. Only a wholly identical row is unambiguously wrong.
        dup = int(df.duplicated().sum())
        if dup:
            problems.append(f"{dup} rows are exact duplicates of another row")

    if not any(line.startswith("#") for line in open(path)):
        problems.append("no provenance header")

    return name, len(df), problems


def main():
    # data/tidy/ is derived by 03_build_tidy.py and data/suspect/ already failed.
    paths = sorted(glob.glob(os.path.join(DATA, "*.csv")))
    failed = 0
    for path in paths:
        name, n, problems = check(path)
        if problems:
            failed += 1
            print(f"  FAIL  {name}  ({n} rows)")
            for p in problems:
                print(f"          {p}")
        else:
            print(f"  ok    {name}  ({n} rows)")
    print(f"\n  {len(paths)} files checked, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
