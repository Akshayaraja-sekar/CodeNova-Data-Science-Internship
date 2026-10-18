
from pathlib import Path
import pandas as pd
import numpy as np

# ==========================================
# 1. SET PROJECT PATHS
# ==========================================

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "sales.csv"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================
# 2. LOAD ORIGINAL DATASET
# ==========================================

if not DATA_PATH.exists():
    raise FileNotFoundError(
        f"Dataset not found: {DATA_PATH}\n"
        "Place the original sales.csv inside the data folder."
    )

raw_df = pd.read_csv(DATA_PATH)
df = raw_df.copy()

print("=" * 60)
print("TASK 2: DATA CLEANING REPORT")
print("=" * 60)
print("\nOriginal dataset shape:", raw_df.shape)

# ==========================================
# 3. INITIAL DIAGNOSTICS
# ==========================================

missing_before = raw_df.isnull().sum()
duplicates_before = int(raw_df.duplicated().sum())
data_types_before = raw_df.dtypes.astype(str)

print("\n--- Missing Values Before Cleaning ---")
print(missing_before)

print("\n--- Duplicate Rows Before Cleaning ---")
print(duplicates_before)

print("\n--- Data Types Before Cleaning ---")
print(data_types_before)

print("\n--- Statistics Before Cleaning ---")
print(raw_df.describe(include="all").to_string())

missing_before.to_csv(
    OUTPUT_DIR / "missing_values_before.csv",
    header=["Missing_Count"]
)

data_types_before.to_csv(
    OUTPUT_DIR / "data_types_before.csv",
    header=["Data_Type"]
)

raw_df.describe(include="all").to_csv(
    OUTPUT_DIR / "statistics_before.csv"
)

# ==========================================
# 4. STANDARDIZE COLUMN NAMES AND TEXT
# ==========================================

df.columns = df.columns.str.strip()

for column in df.select_dtypes(include="object").columns:
    df[column] = df[column].str.strip()

# ==========================================
# 5. CONVERT DATA TYPES
# ==========================================

if "Order Date" in df.columns:
    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        errors="coerce"
    )

for column in ["Sales", "Profit", "Quantity"]:
    if column in df.columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

print("\n--- Data Types After Standardization ---")
print(df.dtypes)

# ==========================================
# 6. DETECT POTENTIALLY INVALID VALUES
# ==========================================

invalid_counts = {}

for column in ["Sales", "Quantity"]:
    if column in df.columns:
        invalid_counts[column] = int(
            (df[column] < 0).sum()
        )

print("\n--- Negative Values Requiring Review ---")

for column, count in invalid_counts.items():
    print(f"Negative {column} values: {count}")

# Negative profit is allowed because a transaction
# can legitimately result in a loss.

# ==========================================
# 7. DETECT OUTLIERS USING IQR
# ==========================================

outlier_results = {}

for column in ["Sales", "Profit", "Quantity"]:
    if column not in df.columns:
        continue

    values = df[column].dropna()

    if values.empty:
        outlier_results[column] = {
            "Q1": np.nan,
            "Q3": np.nan,
            "IQR": np.nan,
            "Lower_Bound": np.nan,
            "Upper_Bound": np.nan,
            "Outlier_Count": 0
        }
        continue

    q1 = values.quantile(0.25)
    q3 = values.quantile(0.75)
    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    outlier_mask = (
        (df[column] < lower_bound)
        | (df[column] > upper_bound)
    )

    outlier_results[column] = {
        "Q1": q1,
        "Q3": q3,
        "IQR": iqr,
        "Lower_Bound": lower_bound,
        "Upper_Bound": upper_bound,
        "Outlier_Count": int(outlier_mask.sum())
    }

outlier_table = pd.DataFrame(outlier_results).T

print("\n--- IQR Outlier Detection ---")
print(outlier_table)

outlier_table.to_csv(
    OUTPUT_DIR / "outlier_detection.csv"
)

# Outliers are reported, not automatically removed.
# Extreme sales/profit values may be legitimate.

# ==========================================
# 8. REMOVE EXACT DUPLICATE ROWS
# ==========================================

duplicates_removed = int(df.duplicated().sum())

df = df.drop_duplicates().copy()

print("\nDuplicate rows removed:", duplicates_removed)

# ==========================================
# 9. HANDLE MISSING AND INVALID VALUES
# ==========================================

# Remove rows where critical fields are missing or
# could not be converted to their required data types.

critical_columns = [
    column
    for column in ["Order Date", "Sales", "Quantity"]
    if column in df.columns
]

rows_before_required_check = len(df)

if critical_columns:
    df = df.dropna(subset=critical_columns).copy()

critical_rows_removed = (
    rows_before_required_check - len(df)
)

print(
    "Rows removed for missing/invalid critical fields:",
    critical_rows_removed
)

# Negative sales and quantity are flagged for review.
# Do not automatically delete them without confirming
# that negative values are invalid for this dataset.

# Track remaining missing-value imputations.
imputed_counts = {}

# Fill missing numeric values with their column median.
numeric_columns = df.select_dtypes(
    include=np.number
).columns.tolist()

for column in numeric_columns:
    missing_count = int(df[column].isna().sum())

    if missing_count > 0:
        median_value = df[column].median()

        if pd.notna(median_value):
            df[column] = df[column].fillna(median_value)
            imputed_counts[column] = missing_count

# Fill missing categorical values with the mode.
categorical_columns = df.select_dtypes(
    include=["object", "category"]
).columns.tolist()

for column in categorical_columns:
    missing_count = int(df[column].isna().sum())

    if missing_count > 0:
        mode_values = df[column].mode(dropna=True)

        if not mode_values.empty:
            df[column] = df[column].fillna(
                mode_values.iloc[0]
            )
            imputed_counts[column] = missing_count

# Fill missing dates with the mode only when appropriate.
# For critical Order Date values, missing/invalid rows
# were already removed above.

print("\nMissing values imputed by column:", imputed_counts)

# ==========================================
# 10. FINAL DATA QUALITY CHECKS
# ==========================================

missing_after = df.isnull().sum()
data_types_after = df.dtypes.astype(str)
duplicates_after = int(df.duplicated().sum())

print("\n--- Missing Values After Cleaning ---")
print(missing_after)

print("\nFinal dataset shape:", df.shape)
print("Duplicate rows after cleaning:", duplicates_after)

print("\n--- Statistics After Cleaning ---")
print(df.describe(include="all").to_string())

# ==========================================
# 11. BEFORE-AND-AFTER COMPARISON
# ==========================================

comparison = pd.DataFrame(
    {
        "Before": [
            len(raw_df),
            len(raw_df.columns),
            int(raw_df.isnull().sum().sum()),
            duplicates_before
        ],
        "After": [
            len(df),
            len(df.columns),
            int(df.isnull().sum().sum()),
            duplicates_after
        ]
    },
    index=[
        "Row Count",
        "Column Count",
        "Total Missing Values",
        "Duplicate Rows"
    ]
)

print("\n--- Before and After Comparison ---")
print(comparison)

comparison.to_csv(
    OUTPUT_DIR / "before_after_comparison.csv"
)

missing_comparison = pd.DataFrame(
    {
        "Before": missing_before,
        "After": missing_after.reindex(
            missing_before.index,
            fill_value=0
        )
    }
)

missing_comparison.to_csv(
    OUTPUT_DIR / "missing_values_comparison.csv"
)

data_types_after.to_csv(
    OUTPUT_DIR / "data_types_after.csv",
    header=["Data_Type"]
)

df.describe(include="all").to_csv(
    OUTPUT_DIR / "statistics_after.csv"
)

# ==========================================
# 12. SAVE CLEANED DATASET
# ==========================================

cleaned_path = OUTPUT_DIR / "sales_cleaned.csv"

df.to_csv(cleaned_path, index=False)

# ==========================================
# 13. GENERATE AUDIT REPORT
# ==========================================

report = f"""# Task 2: Data Cleaning Audit Report

## 1. Objective

Inspect data quality, identify missing values and duplicates,
standardize data types, detect potential outliers, and create
a reproducible cleaned dataset.

## 2. Dataset Overview

- Original rows: {len(raw_df)}
- Original columns: {len(raw_df.columns)}
- Final rows: {len(df)}
- Final columns: {len(df.columns)}

## 3. Missing Values

- Missing cells before cleaning: {int(raw_df.isnull().sum().sum())}
- Missing cells after cleaning: {int(df.isnull().sum().sum())}

See missing_values_comparison.csv for column-level details.

## 4. Duplicate Records

- Duplicate rows before cleaning: {duplicates_before}
- Duplicate rows removed: {duplicates_removed}
- Duplicate rows after cleaning: {duplicates_after}

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
{critical_rows_removed}

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
"""

report_path = OUTPUT_DIR / "cleaning_audit_report.md"

report_path.write_text(report, encoding="utf-8")

# ==========================================
# 14. COMPLETION SUMMARY
# ==========================================

print("\n" + "=" * 60)
print("TASK 2 COMPLETED")
print("=" * 60)

print("Cleaned dataset:", cleaned_path)
print("Audit report:", report_path)
print("Output folder:", OUTPUT_DIR)
