"""
House chart style, read from chart-theme.json.

The canonical definition lives in the website repository
(src/charts/theme.js) and is exported with

    node scripts/data/export-chart-theme.mjs

so the figures in the paper and the charts on the site use one palette. If
chart-theme.json is absent the built-in fallback below keeps the figure scripts
working standalone; it must be kept in step with the JSON.
"""
import json
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_PATH = os.path.join(_HERE, "chart-theme.json")

_FALLBACK = {
    "SERIES": {"light": ["#2a78d6", "#eb6834", "#1baf7a", "#eda100",
                         "#e87ba4", "#008300", "#4a3aa7"]},
    "INK": {"light": {"text": "#0a0a0a", "muted": "#707070", "grid": "#e4e4e4",
                      "axis": "#cecece", "surface": "#fefefe",
                      "band": "#fdf8ee", "flag": "#8a6100"}},
    "EMPHASIS": {"light": "#0a0a0a"},
}

try:
    with open(_PATH) as fh:
        _T = json.load(fh)
except FileNotFoundError:                      # standalone use
    _T = _FALLBACK

# Figures for print are drawn on white, so the light column is the one that matters.
SERIES = _T["SERIES"]["light"]
INK = _T["INK"]["light"]
EMPHASIS = _T["EMPHASIS"]["light"]

TEXT, MUTED, GRID, AXIS, SURFACE = (
    INK["text"], INK["muted"], INK["grid"], INK["axis"], INK["surface"])

# Figures are set in a serif face to sit with the manuscript's body type.
FONT = "Georgia, &apos;Times New Roman&apos;, Times, serif"
