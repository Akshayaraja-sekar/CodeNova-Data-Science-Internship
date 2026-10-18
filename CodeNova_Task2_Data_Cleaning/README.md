# Task 2: Data Cleaning Report

## Data Hygiene and Reproducibility

**Internship:** CodeNova Data Science Internship  
**Task:** Task 2 – Data Cleaning Report  
**Domain:** Data Science   
**Tools:** Python, Pandas, NumPy  
**Dataset:** Sales Data (`sales.csv`)

---

## 1. Project Overview

This project focuses on improving data quality through systematic data inspection, cleaning, validation, and reporting.

The main objective is to identify missing values, duplicate records, inconsistent data types, potentially invalid values, and statistical outliers in a sales dataset.

The project follows a reproducible workflow that preserves the original dataset and saves the cleaned dataset and audit files separately.

## 2. Objectives

- Identify missing values in each column.
- Detect and remove exact duplicate records.
- Standardize column names and text values.
- Convert date and numerical columns to appropriate data types.
- Identify potentially invalid negative sales and quantity values.
- Detect statistical outliers using the Interquartile Range (IQR) method.
- Handle missing values using documented rules.
- Compare data quality before and after cleaning.
- Export the cleaned dataset and supporting reports.
- Preserve the original dataset without modification.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data loading, inspection, cleaning, and analysis |
| NumPy | Numerical operations and missing-value handling |
| VS Code | Development environment |
| CSV | Dataset and output file format |
| Markdown | Data cleaning audit report |

## 4. Dataset Description

The project uses a sales dataset stored as `sales.csv`.

The expected columns include:

| Column | Description |
|---|---|
| Order Date | Date of the sales transaction |
| Region | Geographical sales region |
| State | State where the transaction occurred |
| Category | Main product category |
| Sub-Category | Specific product category |
| Segment | Customer segment |
| Sales | Sales amount |
| Profit | Profit or loss amount |
| Quantity | Number of units sold |

The script checks which columns are present before applying column-specific cleaning operations.

**Note:** The actual dataset contents and quality statistics are determined by running the cleaning script.

## 5. Project Structure

```text
Task-2-Data-Cleaning/
│
├── data/
│   └── sales.csv
│
├── outputs/
│   ├── sales_cleaned.csv
│   ├── cleaning_audit_report.md
│   ├── before_after_comparison.csv
│   ├── missing_values_before.csv
│   ├── missing_values_comparison.csv
│   ├── data_types_before.csv
│   ├── data_types_after.csv
│   ├── statistics_before.csv
│   ├── statistics_after.csv
│   └── outlier_detection.csv
│
├── clean_data.py
└── README.md
```

## 6. Data Cleaning Workflow

### Step 1: Load the Dataset

The original CSV file is loaded using Pandas. A separate copy is created for cleaning so that the input file is not overwritten.

### Step 2: Initial Data Inspection

The script examines:

- Dataset dimensions.
- Missing values in each column.
- Exact duplicate rows.
- Data types.
- Descriptive statistics.

The initial results are saved for comparison.

### Step 3: Standardize Column Names and Text

Leading and trailing spaces are removed from column names and text values to improve consistency.

### Step 4: Correct Data Types

- `Order Date` is converted to datetime.
- `Sales`, `Profit`, and `Quantity` are converted to numeric types.
- Values that cannot be converted are treated as missing values and handled according to the cleaning rules.

### Step 5: Detect Potentially Invalid Values

Negative values in `Sales` and `Quantity` are counted and reported for review.

These values are not automatically deleted because their validity depends on the dataset's business rules. Negative profit is retained because a transaction can legitimately result in a loss.

### Step 6: Detect Outliers Using IQR

The Interquartile Range method identifies unusually low or high numerical values.

The formula is:

**IQR = Q3 − Q1**

- Lower bound = Q1 − 1.5 × IQR
- Upper bound = Q3 + 1.5 × IQR

Values outside these limits are flagged as potential outliers.

Outliers are not automatically removed because extreme values may represent legitimate sales transactions.

### Step 7: Remove Exact Duplicates

Exact duplicate rows are removed to reduce the risk of double-counting repeated records.

This assumes that identical rows are unintended duplicates. If the dataset's business rules allow identical transactions, those records should be reviewed before removal.

### Step 8: Handle Missing Values

The script applies the following rules:

- Rows with missing or invalid critical fields, such as `Order Date`, `Sales`, or `Quantity`, are removed when those columns are present.
- Remaining missing numerical values are filled using the column median.
- Remaining missing categorical values are filled using the column mode.
- If no suitable median or mode exists, the missing value is left unresolved rather than filled arbitrarily.

The number of rows removed and values imputed is recorded during execution.

### Step 9: Validate the Cleaned Dataset

The script checks the final dataset for:

- Remaining missing values.
- Remaining duplicate records.
- Final row and column counts.
- Data types.
- Updated descriptive statistics.

### Step 10: Export Results

The cleaned dataset, comparison tables, diagnostic files, outlier results, and audit report are saved in the `outputs` directory.

## 7. Before-and-After Comparison

The script generates a comparison table containing:

- Row count.
- Column count.
- Total missing-value count.
- Duplicate-row count.

It also exports column-level missing-value comparisons, data types, and descriptive statistics before and after cleaning.

These files provide evidence of the changes made during the cleaning process.

## 8. Output Files

| File | Description |
|---|---|
| `sales_cleaned.csv` | Final cleaned dataset |
| `cleaning_audit_report.md` | Summary of cleaning rules and results |
| `before_after_comparison.csv` | Overall data quality comparison |
| `missing_values_before.csv` | Missing values before cleaning |
| `missing_values_comparison.csv` | Column-level missing-value comparison |
| `data_types_before.csv` | Original data types |
| `data_types_after.csv` | Data types after cleaning |
| `statistics_before.csv` | Initial descriptive statistics |
| `statistics_after.csv` | Final descriptive statistics |
| `outlier_detection.csv` | IQR thresholds and potential outlier counts |

## 9. Installation and Execution

### Prerequisites

- Python 3.10 or later.
- Pandas.
- NumPy.

### Install Dependencies

Open the VS Code terminal and run:

```bash
python -m pip install pandas numpy
```

### Run the Script

Navigate to the `Task-2-Data-Cleaning` directory and execute:

```bash
python clean_data.py
```

The script reads `data/sales.csv`, performs the cleaning workflow, and generates the output files in the `outputs` directory.

## 10. Data Integrity and Reproducibility

The project follows these practices:

- The original input dataset is not overwritten.
- Cleaning operations are automated in a Python script.
- Cleaning decisions are documented.
- Before-and-after statistics are exported.
- Outliers are reported rather than automatically deleted.
- Generated files can be recreated by rerunning the script.

The actual results depend on the contents of the input dataset.

## 11. Limitations

- Statistical outliers are not necessarily data errors.
- Negative sales and quantity values require business-rule validation.
- Median and mode imputation may affect statistical distributions.
- Exact duplicate removal should be validated against the dataset's transaction rules.
- This workflow does not establish that every remaining record is correct; domain-specific validation may still be required.

## 12. Conclusion

This project implements a reproducible data cleaning workflow using Python, Pandas, and NumPy. It examines data quality, standardizes data types, identifies duplicate records and potential outliers, applies documented missing-value handling rules, and generates before-and-after comparison files.

The final deliverables include a cleaned dataset, diagnostic outputs, and a Markdown audit report while preserving the original input file.

---

**Project:** CodeNova Data Science Internship – Task 2  
**Focus:** Data Cleaning, Data Quality, and Reproducibility