import json, re

with open("ocr_parsed.json") as f:
    results = json.load(f)

# Match against whitespace-STRIPPED label for robustness to OCR-inserted spaces
CANONICAL = [
    ("Beef", r"^Beef"),
    ("Chocolate", r"^Chocolate"),
    ("Coffee", r"^Co?f{1,2}e{1,2}"),
    ("Corn", r"^Corn"),
    ("Flour, Common", r"^Flour,?Co[mn]\.?"),
    ("Flour, Superfine", r"^Sup\.?"),
    ("Iron, Bar", r"^Iron,?Bar"),
    ("Molasses", r"^Mol[a-z,]*"),
    ("Pepper", r"^Pepper"),
    ("Pork", r"^Po[r\'l][kti]"),
    ("Rum, W.I.", r"^Rum[.,]?W\.?I?\.?1?"),
    ("Sugar, Muscovado", r"^Sugar,?Mu[sl][ei]?\.?"),
    ("Tar", r"^Tar"),
    ("Tea, Bohea", r"^Tea,?Bo[hb]ea"),
    ("Wheat", r"^Wheat"),
    ("Bread, Ship", r"^Bread,?Ship"),
    ("Cotton", r"^Cotton"),
    ("Flour, Middling", r"^Flour\.?,?Mi?[dn]\.?"),
    ("Indigo", r"^Indigo"),
    ("Leather, sole", r"^Lea[tn]ner,?sole|^Leather,?sole"),
    ("Rice", r"^Rice"),
    ("Sugar, Loaf", r"^Su[gt]far,?[lL][o¡]af|^Sugar,?Loaf"),
    ("Tobacco", r"^Tob[a-z]cco|^Tooacco"),
    ("Turpentine", r"^Turpentine"),
    ("Wine", r"^Wine"),
]

def canonicalize(label):
    stripped = re.sub(r'\s+', '', label)
    for name, pat in CANONICAL:
        if re.match(pat, stripped, re.IGNORECASE):
            return name
    return None

out_rows = []
skipped = []
for year_str, rowdict in results.items():
    year = int(year_str)
    for label, values in rowdict.items():
        canon = canonicalize(label)
        if canon is None:
            skipped.append((year, label))
            continue
        out_rows.append({"year": year, "commodity": canon, "label_raw": label, "n": len(values), "values": values})

print(f"Mapped {len(out_rows)} rows; skipped {len(skipped)}:")
for y, l in skipped:
    print(f"  {y}: {l!r}")

with open("canonical_rows.json", "w") as f:
    json.dump(out_rows, f, indent=1)
