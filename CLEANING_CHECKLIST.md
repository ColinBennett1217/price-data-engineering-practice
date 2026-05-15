# EIA Cleaning Checklist

## Setup
- [x] Create `src/`
- [x] Create `src/__init__.py`
- [x] Create `src/build_eia_csv.py`
- [x] Create `CLEANING_CHECKLIST.md`
- [x] Create `notebooks/table1_1_cleaning.ipynb`
- [x] Create `notebooks/table7_1_cleaning.ipynb`
- [x] Create `notebooks/table9_1_cleaning.ipynb`

## Build helper
- [x] Add project paths to `build_eia_csv.py`
- [x] Add `flatten_header()` function
- [x] Add `build_clean_table()` function
- [x] Add `save_clean_csv()` function
- [x] Add `build_all_eia_csvs()` function
- [x] Verify notebook path handling from `notebooks/`
- [ ] Add optional column-name cleanup helper
- [ ] Add blank/duplicate column-name handling
- [ ] Test script from terminal

## Table 1.1
- [x] Confirm file path
- [x] Load raw Excel in notebook
- [x] Verify top header row
- [x] Verify bottom header row
- [x] Run `flatten_header()`
- [x] Confirm 17 flattened columns
- [ ] Inspect malformed/blank column names
- [ ] Test `build_clean_table()`
- [ ] Inspect output in notebook
- [ ] Export CSV

## Table 7.1
- [ ] Confirm file path
- [ ] Load raw Excel in notebook
- [ ] Verify top header row
- [ ] Verify bottom header row
- [ ] Run `flatten_header()`
- [ ] Compare row layout to Table 1.1
- [ ] Test `build_clean_table()`
- [ ] Inspect output in notebook
- [ ] Export CSV

## Table 9.1
- [ ] Confirm file path
- [ ] Load raw Excel in notebook
- [ ] Verify top header row
- [ ] Verify bottom header row
- [ ] Run `flatten_header()`
- [ ] Compare row layout to Table 1.1
- [ ] Test `build_clean_table()`
- [ ] Inspect output in notebook
- [ ] Export CSV

## Header cleanup
- [ ] Decide whether to keep or remove footnote letters (`a`, `b`, `c`, etc.)
- [ ] Decide how to handle blank column names
- [ ] Decide how to handle malformed labels from merged cells
- [ ] Document naming rules in `CLEANING_CHECKLIST.md`

## Validation
- [ ] Confirm CSV files exist in output folder
- [ ] Check row counts
- [ ] Check column names
- [ ] Check missing values and symbols
- [ ] Confirm all three tables use the same row indices, or add per-table config
- [ ] Commit progress to Git