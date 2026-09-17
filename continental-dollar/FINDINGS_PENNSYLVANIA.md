# The Pennsylvania scale: resolved from the enacted statute

**Read this before revising the paper.** Both reviewers were partly right, both compilations
are partly wrong, and the enacted statute settles it.

## What I did

I stopped relying on compilations and fetched the Pennsylvania statute itself:

> **Act of 3 April 1781, ch. CMXXXV** — "An Act directing the mode of adjusting and settling
> the payment of debts and contracts entered into and made between the first day of January,
> one thousand seven hundred and seventy-seven, and the first day of March, one thousand
> seven hundred and eighty-one."
> *Statutes at Large of Pennsylvania* (1904), vol. 10, pp. 283–289. The scale is Section IV,
> pp. 286–87.

Verified from the page image (archive.org `statutesatlargeo10penn`, PDF p. 293 = printed
p. 287), not OCR. I also checked the successor act of 21 June 1781 (ch. CMXLV), which
repealed legal tender: it refers back to this scale but does **not** extend it.

## What the statute says

The scale runs January 1777 through **February 1781** and then stops. Its closing entries:

> August, seventy. September, seventy-two. **October, seventy-three.** November, seventy-four.
> December, seventy-five.
> *One Thousand Seven Hundred and Eighty-one.* January, seventy-five. February, seventy-five.

Section V begins immediately after. **There is no statutory entry for March, April or May
1781** — consistent with the act covering contracts made before 1 March 1781.

## Therefore

| | Verdict |
|---|---|
| **October 1780 = 73** | The statute says seventy-three. **Webster is right.** American State Papers prints 72, and Phillips (1866, 207) reproduces that error. |
| **March–May 1781** | **Neither compilation is statutory.** ASP supplies 125, 160, 225. Webster carries 75 forward. The act contains neither. |

So my round-1 "correction" was wrong in one direction and the round-2 reviewer's correction
was wrong in the other. The ASP figures the reviewer cites are a real printed series, but
they are not in the act, and the reviewer's inference that they are "the official Pennsylvania
scale" for those months does not hold.

## What this does to the paper

**It vindicates the category-error objection, and documents it.** You cannot compare a
statutory settlement scale to market quotations for months the statute does not cover. The
March–May 1781 comparison should be dropped, not re-run with different numbers. Both the
"frozen at 75 through May" story and the "moved to 125/160/225" story are artifacts of
compilations padding or extending a schedule that had ended.

**The defensible finding is narrower and survives.** Over the months the act does cover,
Pennsylvania's enacted scale tracks Philadelphia quotations closely until late 1780 and then
falls increasingly below every available measure in its final four months:

| | Sep 1780 | Oct | Nov | Dec | Jan 1781 | Feb 1781 |
|---|---|---|---|---|---|---|
| Statute | 72 | 73 | 74 | 75 | 75 | 75 |
| Philadelphia quotation | 75.0 | 77.5 | 90.0 | 100.0 | 100.0 | 110.0 |
| Ratio | 0.96 | 0.94 | **0.82** | **0.75** | **0.75** | **0.68** |

Nov 1780 – Feb 1781 the statutory value is below all three Philadelphia measures (Webster
merchants, Bezanson specie, Bezanson commodity). Full-period mean over the act's coverage:
0.987. Mean from October 1780: 0.789.

**What it still cannot show.** Why the gap opened. A schedule enacted in April 1781 assigning
values to 1777–81 was constructed in one sitting, retrospectively; the terminal months may
reflect a drafting convention, the date the underlying observations were collected,
distributional pressure, or something else. The statute does not say, and neither do the
quotation series.

## Data

`data/published/pennsylvania_scale_three_sources.csv` — statute, ASP and Webster side by
side, with the discrepancies documented in the header. `data/working/phillips_state_scales.csv`
now carries the **statutory** Pennsylvania series, blank after February 1781.

## Everything else checked out

I verified every other state against the 1828 original (House Doc. No. 107, the printing that
became ASP Finance V), from page images: Massachusetts, Maryland, Virginia and North Carolina
all match my transcription exactly. The error was confined to Pennsylvania, and it came from
my treating Phillips as if it were reproducing Webster when the two descend from different
documents.
