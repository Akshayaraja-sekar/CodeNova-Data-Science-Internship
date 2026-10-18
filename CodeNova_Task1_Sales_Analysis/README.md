
# Sales Data Analysis using Python

## Project Overview

This project focuses on analyzing sales data using Python to understand business performance, identify sales trends, evaluate profitability, and discover useful business insights.

The analysis uses a Superstore-style sales dataset containing order dates, geographical information, product categories, customer segments, sales, profit, and quantity sold.

The goal is to transform raw sales data into meaningful insights that can help businesses make better decisions about products, customers, regional performance, and sales strategies.

## Internship Information

- **Organization:** CodeNova
- **Project:** Sales Data Analysis
- **Task:** Data Cleaning, Exploratory Data Analysis (EDA), and Visualization
- **Domain:** Data Science and Business Analytics
- **Programming Language:** Python

## Objectives

The main objectives of this project are:

1. Clean and prepare the raw sales dataset for analysis.
2. Calculate key business performance metrics.
3. Analyze monthly and quarterly sales trends.
4. Compare sales and profit across product categories.
5. Evaluate regional and state-wise sales performance.
6. Understand sales across different customer segments.
7. Identify the most and least profitable product sub-categories.
8. Create visualizations to communicate business findings.
9. Provide actionable business recommendations.

## Dataset Description

The dataset contains sales transaction records with the following columns:

| Column | Description |
|---|---|
| Order Date | Date on which the order was placed |
| Region | Geographical sales region |
| State | State associated with the order |
| Category | Main product category |
| Sub-Category | Specific product sub-category |
| Segment | Customer segment |
| Sales | Sales amount for the record |
| Profit | Profit or loss associated with the record |
| Quantity | Number of units sold |

**Data preparation:** Duplicate records were removed, column names were cleaned, numeric columns were converted to appropriate data types, and order dates were converted to datetime format.

After removing duplicate rows, the dataset contained 9,992 records. Missing-value checks were performed to verify the cleaned dataset.

## Technologies and Libraries Used

- **Python** – Data analysis and programming
- **Pandas** – Data manipulation and aggregation
- **NumPy** – Numerical operations
- **Matplotlib** – Data visualization
- **Seaborn** – Statistical charts and visualizations
- **Jupyter Notebook / VS Code** – Development environment
- **Git and GitHub** – Version control and project hosting

## Project Workflow

### 1. Data Loading

The dataset was loaded from a CSV file using Pandas.

### 2. Data Cleaning

The following cleaning operations were performed:

- Removed duplicate records.
- Removed unnecessary spaces from column names.
- Converted Sales, Profit, and Quantity to numeric data types.
- Converted Order Date into datetime format.
- Checked for missing values and verified the cleaned data.

### 3. Business Metrics Analysis

The following metrics were calculated:

- Total Revenue
- Total Profit
- Total Units Sold
- Profit Margin
- Average Sales per Record

Profit margin was calculated using:

Profit Margin (%) = (Total Profit / Total Revenue) × 100

**Note:** Average sales per record is the average sales amount per dataset row. It is not Average Order Value (AOV), because a unique order identifier is not available in the dataset.

### 4. Monthly Sales Trend

Monthly sales were calculated by grouping records by year and month.

A line chart was created to identify changes in sales over time and observe monthly patterns.

### 5. Quarterly Sales Trend

Sales were grouped by quarter to compare business performance across different quarters.

A line chart was used to visualize quarterly sales fluctuations.

### 6. Category Analysis

Sales, profit, and quantity were aggregated for each product category.

Bar charts were created to compare category-wise sales and profitability.

### 7. Regional Sales Analysis

Sales, profit, and quantity were analyzed across geographical regions.

The results were visualized to compare regional performance.

### 8. Customer Segment Analysis

Sales, profit, and quantity were grouped by customer segment.

This analysis helps identify which customer segment contributes the most to sales and profit.

### 9. State-Wise Sales Analysis

The top 10 states were identified based on total sales.

A horizontal bar chart was used to compare sales performance across these states.

### 10. Sub-Category Analysis

Product sub-categories were analyzed based on sales, profit, and quantity.

The analysis included:

- Top 10 sub-categories by sales.
- Five most profitable sub-categories.
- Five least profitable sub-categories.
- Profit comparison across all sub-categories.

This helps identify products that generate strong sales and products that may require profitability improvements.

### 11. Business Insights and Recommendations

Key findings were generated from the analysis results.

Business recommendations were prepared to support product planning, regional sales strategies, customer targeting, and profitability monitoring.

### 12. Exporting Results

The main analysis tables were exported as CSV files for further analysis, reporting, and sharing.

## Key Business Metrics

The project evaluates the following metrics:

| Metric | Purpose |
|---|---|
| Total Revenue | Measures the overall sales value |
| Total Profit | Measures the overall profit or loss |
| Total Units Sold | Measures sales volume |
| Profit Margin | Measures profit relative to revenue |
| Average Sales per Record | Measures the average sales amount per dataset row |

## Visualizations Created

The project includes the following visualizations:

1. Monthly Sales Trend
2. Quarterly Sales Trend
3. Total Sales by Product Category
4. Total Profit by Product Category
5. Total Sales by Region
6. Total Profit by Region
7. Total Sales by Customer Segment
8. Total Profit by Customer Segment
9. Top 10 States by Total Sales
10. Top 10 Sub-Categories by Sales
11. Profit by Product Sub-Category

These visualizations help communicate sales patterns, compare business performance, and identify areas that need further investigation.

## Business Recommendations

Based on the analysis, the following actions can be considered:

1. **Improve product strategy:** Study the best-performing categories and identify opportunities to increase sales.
2. **Strengthen regional performance:** Examine successful regions and investigate weaker regional results.
3. **Target customer segments:** Develop appropriate marketing campaigns based on segment-level sales and profit.
4. **Monitor product profitability:** Investigate sub-categories with low or negative profit.
5. **Review pricing and costs:** Examine product pricing, discounts, and costs before deciding how to improve profitability.
6. **Plan inventory effectively:** Use monthly and quarterly trends to support inventory planning and sales forecasting.
7. **Monitor business KPIs:** Regularly track revenue, profit, units sold, and profit margin.

These recommendations should be validated against detailed business information before implementation.

## Project Structure

The project directory is organized as follows:

```text
CodeNova-Sales-Analysis/
│
├── data/
│   └── sales.csv
│
├── outputs/
│   ├── category_analysis.csv
│   ├── region_analysis.csv
│   ├── segment_analysis.csv
│   ├── top_10_states.csv
│   ├── subcategory_profit_analysis.csv
│   ├── monthly_sales.csv
│   └── quarterly_sales.csv
│
├── sales_analysis.ipynb
└── README.md
```

*Note: The output files listed above should exist in the `outputs` folder after running the corresponding export cells.*

## Installation and Setup

### Prerequisites

Install Python 3 and Jupyter Notebook, or use Visual Studio Code with the Python and Jupyter extensions.

### Step 1: Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Replace the placeholder with your actual GitHub repository URL.

### Step 2: Navigate to the project directory

```bash
cd CodeNova-Sales-Analysis
```

### Step 3: Install the required libraries

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### Step 4: Place the dataset

Ensure that the dataset is available at:

```text
data/sales.csv
```

### Step 5: Open the notebook

Open `sales_analysis.ipynb` in Jupyter Notebook or Visual Studio Code.

Run the notebook cells in order, starting with data loading and cleaning.

**Important:** If your notebook uses a different relative path for the CSV file, update the dataset path in the first cell accordingly.

## Results

The project produces:

- A cleaned sales dataset in memory.
- Business performance metrics.
- Monthly and quarterly sales summaries.
- Category-wise, region-wise, segment-wise, and state-wise comparisons.
- Sub-category profitability analysis.
- Data visualizations.
- Business insights and recommendations.
- Exported CSV files containing analysis results.

Actual numerical findings should be documented after reviewing the executed notebook outputs.

## Limitations

- The dataset does not contain a unique Order ID, so Average Order Value (AOV) cannot be calculated reliably.
- Product-level analysis is limited to the available Category and Sub-Category columns.
- The analysis describes historical data and does not guarantee future sales performance.
- Recommendations are based on the available dataset and should be validated with additional business information.
- Seasonal patterns require sufficient historical coverage and should be interpreted carefully.

## Future Improvements

Possible extensions include:

- Building an interactive dashboard using Streamlit or Power BI.
- Adding more detailed sales and profitability visualizations.
- Performing customer-level analysis if customer identifiers become available.
- Developing sales forecasting models.
- Conducting discount and pricing analysis if the relevant columns are available.
- Automating the generation of business reports.

## Conclusion

This project demonstrates the use of Python for data cleaning, exploratory data analysis, business metrics calculation, and data visualization.

By analyzing sales trends, product categories, geographical regions, customer segments, and sub-category profitability, the project provides a structured approach to understanding business performance and identifying opportunities for improvement.

The project also demonstrates practical skills in Pandas, Matplotlib, Seaborn, and data-driven business analysis.

## Author

**Akshaya Rajasekar**

Data Science Intern | Artificial Intelligence and Data Science Undergraduate

---

*Developed as part of the CodeNova Sales Data Analysis Internship Task.*
