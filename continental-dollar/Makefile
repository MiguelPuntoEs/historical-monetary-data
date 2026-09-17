# Regenerates the analysis output and figures from data/. Nothing here needs the paper.

UVRUN := uv run --quiet --with svglib --with reportlab python

.PHONY: all analysis figures clean
.DEFAULT_GOAL := all

all: analysis figures

## analysis — the three tables the figures and the paper draw on
analysis:
	@python3 analysis/01_recognition_gap.py
	@python3 analysis/02_two_state_test.py

## figures — SVGs from the data, then the vector PDFs LaTeX embeds
figures:
	@python3 analysis/03_figure_two_markets.py
	@python3 analysis/04_figure_state_scales.py >/dev/null && echo "wrote figures/state_scales.svg"
	@$(UVRUN) analysis/06_figures_to_pdf.py

clean:
	@rm -f figures/*.pdf
