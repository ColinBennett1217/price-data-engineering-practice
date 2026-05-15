# EIA Cleaning Checklist

## Setup
- [x] Create `src/`
- [x] Create `src/__init__.py`
- [x] Create `src/build_eia_csv.py`
- [x] Create `CLEANING_CHECKLIST.md`
- [ ] Create `notebooks/table1_1_cleaning.ipynb`
- [ ] Create `notebooks/table7_1_cleaning.ipynb`
- [ ] Create `notebooks/table9_1_cleaning.ipynb`

## Build helper
- [ ] Add project paths to `build_eia_csv.py`
- [ ] Add `flatten_header()` function
- [ ] Add `build_clean_table()` function
- [ ] Add `save_clean_csv()` function
- [ ] Add `build_all_eia_csvs()` function
- [ ] Test script from terminal

## Table 1.1
- [ ] Confirm file path
- [ ] Test cleaning function
- [ ] Inspect output in notebook
- [ ] Export CSV

## Table 7.1
- [ ] Confirm file path
- [ ] Test cleaning function
- [ ] Inspect output in notebook
- [ ] Export CSV

## Table 9.1
- [ ] Confirm file path
- [ ] Test cleaning function
- [ ] Inspect output in notebook
- [ ] Export CSV

## Validation
- [ ] Confirm CSV files exist in output folder
- [ ] Check row counts
- [ ] Check column names
- [ ] Check missing values and symbols
- [ ] Commit progress to Git