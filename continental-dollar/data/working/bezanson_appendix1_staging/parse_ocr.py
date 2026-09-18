import re, json

with open("ocr_raw.txt") as f:
    lines = f.readlines()

year_blocks = []
current_year = None
current_lines = []
for line in lines:
    m = re.match(r'^\s*(17[789]\d)\s*$', line)
    if m:
        if current_year:
            year_blocks.append((current_year, current_lines))
        current_year = int(m.group(1))
        current_lines = []
    elif current_year:
        current_lines.append(line.rstrip('\n'))
if current_year:
    year_blocks.append((current_year, current_lines))

UNIT_RE = re.compile(r'^[£sd£•iBIl][-–][A-Za-z]{2,4}$|^[£sd£•]$|^[-–][A-Za-z]{2,4}$')

def normalize_digit_token(t):
    return re.sub(r'[SIlO]', lambda m: {'S':'5','I':'1','l':'1','O':'0'}[m.group()], t)

def fix_num(tok):
    if not re.search(r'\d', tok):
        return tok
    t = normalize_digit_token(tok)
    t = t.replace(',', '').replace(':', '').replace(';','').replace('!','').replace(')','').replace('(','')
    return t

def merge_tokens(tokens):
    toks = list(tokens)
    changed = True
    while changed:
        changed = False
        out = []
        i = 0
        while i < len(toks):
            t = toks[i]
            if UNIT_RE.match(t):
                changed = True; i += 1; continue
            if (i+2 < len(toks) and re.fullmatch(r'\d+', t) and toks[i+1] == '.'
                    and re.fullmatch(r'\d+', toks[i+2])):
                out.append(f"{t}.{toks[i+2]}"); i += 3; changed = True; continue
            # broadened: ANY bare int (no dot) immediately followed by another bare int
            if (i+1 < len(toks) and re.fullmatch(r'\d+', t) and '.' not in t
                    and re.fullmatch(r'\d+', toks[i+1]) and '.' not in toks[i+1]):
                out.append(f"{t}.{toks[i+1]}"); i += 2; changed = True; continue
            out.append(t); i += 1
        toks = out
    return toks

NUM_ONLY_RE = re.compile(r'^\d+\.?\d*$')

results = {}
unresolved = []
for year, block_lines in year_blocks:
    results[year] = {}
    for line in block_lines:
        if not line.strip(): continue
        if "SOURCES" in line or "SOUICES" in line or "SOUHCES" in line: continue
        if "Commodity" in line and "Unit" in line: continue
        if re.search(r'APPENDIX|PRICES DURING|AVERAGE|MONTHLY|WHOLESALE', line): continue
        raw_tokens = line.split()
        fixed = [fix_num(t) for t in raw_tokens]
        numeric_flags = [bool(NUM_ONLY_RE.match(t)) for t in fixed]
        split_idx = None
        for i in range(len(fixed)):
            if numeric_flags[i] and all(numeric_flags[i:i+3]) and i+3 <= len(fixed):
                split_idx = i; break
        if split_idx is None: continue
        label = " ".join(raw_tokens[:split_idx])
        value_tokens = [t for t in fixed[split_idx:] if t != '']
        merged = merge_tokens(value_tokens)
        merged = [t for t in merged if NUM_ONLY_RE.match(t)]
        if len(merged) != 12:
            unresolved.append((year, label, merged))
        results[year][label] = merged

with open("ocr_parsed5.json", "w") as f:
    json.dump(results, f, indent=1)
n_resolved = sum(1 for y in results for l in results[y] if len(results[y][l]) == 12)
n_total = sum(len(results[y]) for y in results)
print(f"Rows with exactly 12 values: {n_resolved} / {n_total}")
print(f"Still unresolved: {len(unresolved)}")
for year, label, toks in unresolved:
    print(f"  {year} {label!r} (n={len(toks)}): {toks}")
