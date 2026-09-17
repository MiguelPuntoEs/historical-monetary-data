"""
Convert figures/*.svg to figures/*.pdf for LaTeX.

svglib and reportlab are pure Python, so this needs no system libraries. It is
run through `uv run --with`, which keeps them out of the project environment:

    uv run --with svglib --with reportlab python analysis/06_figures_to_pdf.py

The SVGs remain the source; the PDFs are derived and need regenerating only when
a figure changes. reportlab is put in invariant mode so that rerunning this on an
unchanged figure produces a byte-identical file: otherwise every run embeds a new
creation timestamp and the figures show up as modified in every diff.
"""
import glob
import os

from reportlab import rl_config

rl_config.invariant = 1

from reportlab.graphics import renderPDF  # noqa: E402
from svglib.svglib import svg2rlg  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.path.join(HERE, "..", "figures")

for svg in sorted(glob.glob(os.path.join(FIGS, "*.svg"))):
    pdf = svg[:-4] + ".pdf"
    drawing = svg2rlg(svg)
    renderPDF.drawToFile(drawing, pdf)
    print(f"  {os.path.basename(pdf):<28} {drawing.width:.0f} x {drawing.height:.0f} pt")
