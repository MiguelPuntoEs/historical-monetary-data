# Validation and analysis for the greenbacks dataset. Run from the collection's
# environment: `uv sync` at the repository root first.

.PHONY: all validate tidy crosscheck analysis fetch
.DEFAULT_GOAL := all

all: validate tidy crosscheck analysis

## validate — invariant checks over every file in data/
validate:
	@uv run --quiet python analysis/02_validate.py

## tidy — regenerate data/tidy/ from the wide source tables
tidy:
	@uv run --quiet python analysis/03_build_tidy.py

## crosscheck — tables that ought to agree with each other
crosscheck:
	@uv run --quiet python analysis/04_crosscheck.py

## analysis — the pass-through table
analysis:
	@uv run --quiet python analysis/01_pass_through.py

## fetch — refresh the external series. Output is committed; rarely needed.
fetch:
	@uv run --quiet python analysis/00_fetch_sources.py
