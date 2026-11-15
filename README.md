# Duct Sizer Calculator

Sizes round and rectangular ducts from an airflow (CFM) and a design velocity (FPM): free area, round diameter, and equal-area rectangular options with Huebscher equivalent diameters.

**Live web tool:** https://dust2engineering.github.io/ontario-duct-sizer-calculator/web/

## How it works

- Free area (in2) = CFM / FPM x 144.
- Round diameter = 2 x sqrt(area / pi).
- Rectangular depth = area / chosen width; equivalent diameter De = 1.30 (a b)^0.625 / (a + b)^0.25.

## Data in this repository

- duct-sizing-data.json — the method and typical design velocity ranges, machine-readable.

## Command line

```bash
python3 duct_sizer.py --cfm 2000 --fpm 1000
```

## Worked examples

- [makeup-air-main-2000-cfm.md](examples/makeup-air-main-2000-cfm.md)
- [kitchen-exhaust-3000-cfm.md](examples/kitchen-exhaust-3000-cfm.md)

## Scope and limits

Preliminary design aid only. It does not replace the current Ontario Building Code or the judgement of the designer of record. Verify all values against the Code in force for your project before submitting drawings for permit.

## About

Maintained by **Dust 2 Engineering Inc.** (Mississauga, Ontario) — building permit drawings
(architectural, HVAC, plumbing, sprinkler, electrical) for restaurants and small commercial
projects across the Greater Toronto Area, stamped by an Ontario P.Eng. Flat rate $3,500–$5,000.

Category: HVAC / mechanical. More free Ontario code tools: see the full index at
https://github.com/dust2engineering
