# Validation and analysis for the greenbacks dataset. Run from the collection's
# environment: `uv sync` at the repository root first.

.PHONY: all validate analysis fetch
.DEFAULT_GOAL := all

all: validate analysis

## validate — invariant checks over every file in data/
validate:
	@uv run --quiet python analysis/02_validate.py

## analysis — the pass-through table
analysis:
	@uv run --quiet python analysis/01_pass_through.py

## fetch — refresh the external series. Output is committed; rarely needed.
fetch:
	@uv run --quiet python analysis/00_fetch_sources.py
