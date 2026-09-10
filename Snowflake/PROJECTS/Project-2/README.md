# 📊 Retail Sales Analytics using Snowflake

A cloud data warehouse and SQL analytics project built using **Snowflake** to load retail data from CSV files and generate business-focused reports for customers, products, branches, and sales.

This project demonstrates practical **SQL, Snowflake Cloud Data Warehousing, data loading, relational data modeling, joins, aggregations, window functions, CTEs, and views**.

---

## 📌 Project Overview

A nationwide retail chain receives daily sales data from multiple branches in CSV format.

The objective of this project is to:

- Build the required Snowflake environment
- Load customer, product, branch, and sales datasets
- Perform multi-table SQL analysis
- Identify top-performing customers, products, and branches
- Analyze sales trends
- Use advanced SQL techniques such as window functions and CTEs
- Create reusable reporting views

The project is designed as a practical **data engineering and business intelligence SQL project**.

---

## 🎯 Project Objectives

This project covers the following objectives:

- Load multiple datasets into Snowflake
- Perform multi-table joins
- Use aggregate functions
- Apply window functions
- Use Common Table Expressions (CTEs)
- Create views and materialized-view-based reporting
- Generate business intelligence reports
- Analyze customer purchasing behavior
- Analyze product and branch performance

---

## 🗂️ Dataset

The project uses four CSV datasets:

```text
customers.csv
products.csv
branches.csv
sales.csv
```

### Customers

Contains customer information:

```text
customer_id
customer_name
city
membership
```

### Products

Contains product information:

```text
product_id
product_name
category
price
```

### Branches

Contains branch information:

```text
branch_id
branch_name
city
```

### Sales

Contains individual sales transactions:

```text
sale_id
customer_id
product_id
branch_id
quantity
sale_date
total_amount
```

---

## 🏗️ Data Model

The `SALES` table acts as the central transaction table and connects the customer, product, and branch entities.

```text
                  ┌──────────────┐
                  │  CUSTOMERS   │
                  │ customer_id  │
                  └───────┬──────┘
                          │
                          │
┌──────────────┐          ▼          ┌──────────────┐
│  PRODUCTS    │──────► SALES ◄──────│   BRANCHES   │
│ product_id   │          │          │  branch_id   │
└──────────────┘          │          └──────────────┘
                          │
                          ▼
                    Sales Analytics
```

### Relationships

```text
CUSTOMERS.customer_id → SALES.customer_id
PRODUCTS.product_id   → SALES.product_id
BRANCHES.branch_id    → SALES.branch_id
```

---

# 🏢 Phase 1 — Snowflake Environment

The Snowflake environment contains:

```text
Warehouse : RETAIL_WH
Database  : RETAIL_DB
Schema    : SALES_SCHEMA
```

The project also includes:

- CSV File Format
- Internal Stage

These objects provide the environment required for loading and processing the retail datasets.

---

# 📥 Phase 2 — Data Loading

The four CSV files are loaded into their corresponding tables:

```text
customers.csv → CUSTOMERS
products.csv  → PRODUCTS
branches.csv  → BRANCHES
sales.csv     → SALES
```

The Snowflake implementation uses `COPY INTO` to load the CSV data.

The imported records are then verified using SQL queries.

---

# 📈 Phase 3 — SQL Analytics

The project generates several business-focused analytical reports.

### Basic Data Reports

- Display all customers
- Display all products
- Display all branches
- Display all sales transactions

### Revenue Analysis

- Calculate total business revenue
- Generate customer-wise sales
- Generate branch-wise sales
- Generate product-wise sales
- Generate category-wise sales

### Top Performers

- Highest revenue branch
- Highest spending customer
- Top three products by revenue
- Top three customers by spending

---

# 🪟 Phase 4 — Window Functions

Advanced SQL window functions are used for analytical calculations.

### Customer Ranking

Customers are ranked according to their total spending using `RANK()`.

```sql
RANK() OVER (
    ORDER BY total_amount_spent DESC
)
```

### Branch Ranking

Branches are ranked according to total sales revenue.

### Top Product in Each Category

`ROW_NUMBER()` is used to identify the highest-selling/revenue-generating product within each category.

```sql
ROW_NUMBER() OVER (
    PARTITION BY category
    ORDER BY total_product_revenue DESC
)
```

### Cumulative Sales

Cumulative sales are calculated using `SUM() OVER()`.

```sql
SUM(total_amount) OVER (
    ORDER BY sale_date
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
)
```

### Average Sale Amount

A running average sale amount is calculated using `AVG() OVER()`.

```sql
AVG(total_amount) OVER (
    ORDER BY sale_date
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
)
```

---

# 🔄 Phase 5 — Common Table Expressions

CTEs are used to structure multi-step analytical queries.

### Customer-wise Revenue

A CTE is used to calculate total revenue/spending for each customer.

### Customers Spending Above Average

The project calculates average customer spending and identifies customers whose spending is greater than the average.

This demonstrates:

- CTEs
- Aggregation
- Derived results
- Filtering based on calculated values

---

# 👁️ Phase 6 — Views

## SALES_REPORT

A view named:

```text
SALES_REPORT
```

provides a consolidated sales report by combining sales information with customer, product, and branch details.

The report can contain:

- Sale ID
- Sale date
- Customer name
- Customer city
- Membership
- Product name
- Category
- Branch
- Quantity
- Total amount

---

## TOP_CUSTOMERS

The project specification includes a `TOP_CUSTOMERS` materialized-view report for identifying customers with the highest spending.

The analytical logic calculates customer-level spending from the sales data and uses customer information when producing the final business report.

### Platform Note

The original project is designed for **Snowflake**.

Snowflake materialized views have restrictions on their definitions, particularly when multiple tables and joins are involved. Therefore, the materialized portion of the customer-spending calculation must follow Snowflake's supported materialized-view design, with customer details joined when required for the final report.

This is a **platform-specific implementation consideration**, not a change to the business requirement.

---

# 📊 Business Reports Generated

The completed project generates the following reports:

1. All Customers
2. All Products
3. All Branches
4. Customer-wise Sales Report
5. Branch-wise Revenue Report
6. Product-wise Revenue Report
7. Category-wise Revenue Report
8. Highest Revenue Branch
9. Highest Spending Customer
10. Top Three Products
11. Top Three Customers
12. Customer Ranking
13. Branch Ranking
14. Top Product in Each Category
15. Cumulative Sales Report
16. Average Sales Report
17. Customers Spending Above Average
18. Sales Report View
19. Top Customers / Materialized View Report

---

# 🛠️ Technologies & Concepts

## Technologies

- **Snowflake**
- **SQL**
- **CSV**

## SQL Concepts

```text
SELECT
WHERE
GROUP BY
ORDER BY
JOIN
INNER JOIN
Aggregate Functions
COUNT()
SUM()
AVG()
RANK()
ROW_NUMBER()
SUM() OVER()
AVG() OVER()
CTE
CREATE VIEW
CREATE MATERIALIZED VIEW
COPY INTO
```

---

# 💼 Business Questions Answered

The project helps answer questions such as:

- What is the total revenue generated by the business?
- Which customer spends the most?
- Which customers spend more than the average?
- Which branch generates the highest revenue?
- Which products generate the most revenue?
- Which category generates the highest revenue?
- Who are the top three customers by spending?
- What are the top three products by revenue?
- How do customers rank based on spending?
- How do branches rank based on revenue?
- What is the top product in each category?
- How does cumulative revenue change over time?
- What is the running average sale amount?

---

# 📂 Suggested Repository Structure

For this project, the repository can be organized as:

```text
Project-2/
│
├── Project-2 Kimball.md
├── README.md
├── project-2.sql
├── project-2.ipynb
├── project-2.html
│
├── customers.csv
├── products.csv
├── branches.csv
└── sales.csv
```

> File names can be adjusted to match the actual files uploaded to the repository.

---

# ▶️ How to Run

## Using Snowflake

1. Create the `RETAIL_WH` warehouse.
2. Create the `RETAIL_DB` database.
3. Create the `SALES_SCHEMA` schema.
4. Create the CSV file format.
5. Create the internal stage.
6. Upload the four CSV files.
7. Create the required tables.
8. Load the data using `COPY INTO`.
9. Verify the imported records.
10. Execute the SQL analytics queries.
11. Execute the window-function queries.
12. Execute the CTE queries.
13. Create `SALES_REPORT`.
14. Create the supported `TOP_CUSTOMERS` materialized-view/report structure.
15. Query the final reports.

---

# 📌 Dataset Summary

The supplied project dataset contains:

| Dataset | Records |
|---|---:|
| Customers | 5 |
| Products | 5 |
| Branches | 3 |
| Sales Transactions | 12 |

Sales transactions cover:

```text
2026-07-01 → 2026-07-12
```

---

# 🧪 Verification

The SQL queries were executed and their results were verified throughout the project.

The verification covers:

- Data loading
- Customer analysis
- Product analysis
- Branch analysis
- Category analysis
- Revenue calculations
- Customer rankings
- Branch rankings
- Top products
- Cumulative sales
- Average sales
- CTE results
- Above-average customers
- `SALES_REPORT`
- `TOP_CUSTOMERS`

---

# 🎓 Learning Outcomes

This project provides practical experience in:

- Snowflake Cloud Data Warehousing
- SQL-based data analysis
- Data loading from CSV files
- Relational data modeling
- Multi-table joins
- Aggregations
- Business intelligence reporting
- Window functions
- Ranking
- Cumulative calculations
- Running averages
- Common Table Expressions
- Views
- Materialized-view concepts
- Analytical problem solving

---

# ✅ Project Status

**Completed ✅**

The Retail Sales Analytics project has completed the required workflow from Snowflake environment setup and CSV data loading through advanced SQL analytics, window functions, CTEs, business reports, and view-based reporting.

---

## 👨‍💻 Author

**Aashik Reddy**

**Project:** Retail Sales Analytics using Snowflake  
**Domain:** Data Engineering / SQL / Business Intelligence
