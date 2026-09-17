# Wages Data Completion Roadmap

## Current Status (Session End)

### ✅ Appendix B (Complete - 6 tables)
- Table 1A: Farm individual prices (1,064 cells) ✓
- Table 1B: Farm averages (364 cells) ✓  
- Table 2: Wholesale prices (2,928 cells) ✓
- Table 3: Government prices (79 rows) ✓
- Table 4: Retail prices (33,360 cells) ✓
- Table 5: Wholesale vs retail (576 cells) ✓

### 🟡 Appendix C Table 1: Aldrich Report Wages
**Progress: 22 of 48 pages (3,231 rows, 239 occupations)**

Completed industries:
- ✓ Establishment 38 (Cotton goods, Mass) - 2 pages
- ✓ Establishment 39 (Cotton goods, Mass) - 6 pages  
- ✓ Establishment 40 (Cotton goods, Mass) - 6 pages
- ✓ Establishment 42 (Dry goods, NH) - 1 page
- ✓ Establishment 43 (Ginghams, Mass) - 7 pages

Remaining industries (26 pages, ~400 additional rows expected):
- Building Trades (13-15 Mass, etc.) - ~6 pages
- City Public Works - ~2 pages
- Carriage & Wagons - ~1 page
- Groceries - ~1 page
- Illuminating Gas (45-49 Mass, etc.) - ~3 pages
- Leather (50 Mass, 52 NH, 53 NY) - ~3 pages
- Metals & Metallic (54-62 Conn, Mass, etc.) - ~4 pages
- Paper - ~2 pages
- Railways (75 Mass, 77 NY, etc.) - ~2 pages
- Spice - ~1 page
- Stove - ~1 page
- White Lead - ~1 page
- Woolen Goods (86 Conn, 89 RI) - ~2 pages

### 🟡 Appendix C Table 2: Census Wages
**Progress: 110 rows (framework established)**

Industries started:
- Flint Glass (4 locations) ✓
- Agricultural Implements (1 location) ✓
- Boots & Shoes (3 locations) ✓
- Gas & Gas Coke (2 locations) ✓
- Iron Blast Furnaces (3 types, multiple locations) ✓
- Iron & Steel Foundries - Stove (2 locations) ✓
- Hardware (1 location) ✓
- Machinery (1 location partial) ✓

Remaining: ~15-20 more industries with 5-10 occupations each

## CSV Locations
- `greenbacks/data/mitchell_appendix_c_table1_wages_partial.csv` - 22 pages staged
- `greenbacks/data/mitchell_appendix_c_table2_wages_census.csv` - 110 rows

## PDF Source
- `/Users/miguel/Downloads/historyofgreenba00mitcrich.pdf`
- Table 1 wages: Book pages ~469-520
- Table 2 wages: Book pages ~518-538+

## Completion Strategy

### High Priority (for paper deadline)
1. Complete Building Trades (highest value, establishes pattern)
2. Complete major industries: Leather, Metals, Paper, Railways
3. Finalize and validate Table 2

### Nice to Have
- Complete all remaining minor industries
- Cross-validate aggregate statistics

## Notes for Next Session
- Use Python framework in `/private/tmp/.../scratchpad/build_tc1.py` - it validates structure
- Each page follows: 6 occupations × 14 dates = 84 data cells
- Missing data marked as "..." (dot-dot-dot)
- Braced figures in original preserved as separate notes
- All dates: 1860 Jan, July; 1861 Jan, July; ... 1866 Jan, July (14 total)

## Estimated Effort
- Table 1: 26 more pages × ~5 min/page = ~2 hours to complete
- Table 2: ~50 more occupations × ~1 min = ~1 hour to complete
- Validation: ~30 minutes
- **Total remaining: ~3.5 hours for full dataset completion**
