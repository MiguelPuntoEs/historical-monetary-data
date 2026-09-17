# Lead: Connecticut, New York, South Carolina scales — a source that's actually accessible

**18 September 2026.** The README already flags Connecticut, New York and South Carolina as
"in the same 1828 source [House Doc. No. 107 / American State Papers, Finance, vol. V] but
not yet transcribed." I went looking for that source to close the gap and found the
Internet Archive copy (`americanstatepap00gree_3`) is **access-restricted** (controlled
digital lending) — not something to route around.

## What I found instead

**Henry Phillips, Jr., *Continental Paper Money* (1866), Appendix D, pp. 206–209.**
Archive.org item `continentalpaper00phil` — **fully unrestricted**, already the source for
this repo's `phillips_1866_merchants_books.csv` (pp. 217–18 of the same book). Appendix D is
titled "Scales of Depreciation for the Settlements with Individuals for the States of
Massachusetts, Connecticut, New York, New Jersey, Pennsylvania, Delaware, Maryland,
Virginia, North Carolina and South Carolina" — i.e., Phillips reprints the *same* federal
1828 table this repo already uses for the other seven states, in a source anyone can fetch:

```
curl -L "https://archive.org/download/continentalpaper00phil/continentalpaper00phil.pdf" \
  -o phillips1866.pdf
```

Page images: PDF pages match printed page numbers closely in this scan (printed p. 206 was
at PDF page ~208 in one read, ~206 in another — recheck the exact offset before relying on
it; it was not fully consistent across my own attempts).

## Why I did not just transcribe it and add it

Cross-checking Phillips's Massachusetts, Maryland, and Virginia columns against this
repo's already-verified `state_depreciation_scales.csv` mostly matched — good evidence
Phillips is reproducing the same underlying document. But two things surfaced that need
resolving before Phillips can be trusted as a stand-in for the restricted original:

1. **New Jersey, January–August 1777**: Phillips shows values (1.20, 1.10 or 1.9, 2.10,
   3.10, 4.10, 2, 2¼, 2½...); the existing verified file has this entire span **blank**,
   starting New Jersey only in January 1778. One of the two is wrong, or Phillips's edition
   differs from the original document.
2. **North Carolina, 1777**: the reverse pattern — Phillips shows blank ("..") for at least
   January–February 1777, but the existing verified file has real North Carolina values
   from March 1777 onward (1.25, 1.50, 1.50, 1.75, ...).
3. **Connecticut and New York's columns look suspiciously alike** in several months (e.g.
   both apparently read "146, 152" for one January entry, and several other months show
   matching pairs) — this could be genuine (a shared congressional baseline before state
   scales diverge) or could be a reading/printing artifact. I do not have enough confidence
   in my own transcription of this specific table, after this session's experience with the
   greenbacks wage tables, to resolve which.

## What this means

**Do not transcribe Connecticut/New York/South Carolina from Phillips's Appendix D and
add it as if equivalent to the primary-source file.** Treat it, if used, as a separate,
explicitly-labeled secondary source (Phillips's 1866 reproduction), the same way this repo
already treats Bullock and Bezanson — and document the New Jersey/North Carolina
discrepancies the way `FINDINGS_PENNSYLVANIA.md` documents Pennsylvania's.

Before that can happen, someone needs to:
- Re-read Phillips pp. 206–209 carefully, ideally twice independently, specifically for
  Connecticut, New York and South Carolina (the states not already cross-checkable against
  a verified file)
- Resolve whether the CT/NY near-duplicate values are real
- Decide how to handle South Carolina's notation (the existing README already flags this as
  needing care — my brief look suggests it may not be pounds-and-shillings but a different
  percentage format; needs a careful look, not assumption)
- Ideally get an unrestricted look at the actual 1828 document (or a second edition/printing
  of it) to adjudicate the New Jersey/North Carolina 1777 discrepancy independently of
  Phillips

This is genuine progress — a real, accessible source was identified for the exact gap the
README names — but the transcription itself is not done, and I'm flagging that explicitly
rather than risk another false "verified" claim.
