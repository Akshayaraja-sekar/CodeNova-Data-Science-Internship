# Task 2: Data Cleaning Audit Report

## 1. Objective

Inspect data quality, identify missing values and duplicates,
standardize data types, detect potential outliers, and create
a reproducible cleaned dataset.

## 2. Dataset Overview

- Original rows: 9994
- Original columns: 9
- Final rows: 9992
- Final columns: 9

## 3. Missing Values

- Missing cells before cleaning: 0
- Missing cells after cleaning: 0

See missing_values_comparison.csv for column-level details.

## 4. Duplicate Records

- Duplicate rows before cleaning: 2
- Duplicate rows removed: 2
- Duplicate rows after cleaning: 0

Exact duplicate rows were removed to reduce the risk of
double-counting repeated records.

## 5. Data Type Standardization

- Order Date was converted to datetime when present.
- Sales, Profit, and Quantity were converted to numeric types
  when present.
- Failed conversions became missing values.
- Leading and trailing spaces were removed from column names
  and text values.

## 6. Missing and Invalid Data Treatment

- Rows with missing or invalid critical fields were removed.
- Remaining missing numeric values were filled with the median.
- Remaining missing categorical values were filled with the mode.
- Negative Sales and Quantity values were reported for review.
- Negative Profit values were retained because losses may be valid.

Rows removed for missing/invalid critical fields:
0

Imputation counts are printed in the terminal.

## 7. Outlier Detection

The IQR method was applied to Sales, Profit, and Quantity.

Lower bound = Q1 - 1.5 * IQR
Upper bound = Q3 + 1.5 * IQR

Outliers were flagged but not automatically removed because
extreme values may represent legitimate business transactions.

See outlier_detection.csv for thresholds and counts.

## 8. Before-and-After Comparison

See:
- before_after_comparison.csv
- missing_values_comparison.csv
- statistics_before.csv
- statistics_after.csv
- data_types_before.csv
- data_types_after.csv

## 9. Output

Cleaned dataset: sales_cleaned.csv

The original input dataset was not overwritten.

## 10. Reproducibility

Run this script from the Task-2-Data-Cleaning folder:

python clean_data.py

The script regenerates the cleaned dataset, diagnostic files,
comparison tables, and this report.
