# 📊 Customer Sales Analytics using Snowflake

A cloud data warehouse project built using **Snowflake** to load customer, food item, and order data from CSV files and generate business-focused analytical reports using SQL.

This project demonstrates practical concepts in **SQL, Snowflake Cloud Data Warehousing, data loading, relational data modeling, joins, aggregations, analytical reporting, and views**.

---

## 📌 Project Overview

The objective of this project is to build a simple analytical data warehouse in Snowflake for an online food-ordering business.

The business receives three CSV files containing:

- Customer information
- Food item information
- Order transactions

These files are uploaded to a Snowflake internal stage and loaded into relational tables. SQL queries are then used to generate analytical reports that help answer important business questions.

### Business Questions

- Who are the highest-spending customers?
- What is the total business revenue?
- Which food category generates the highest revenue?
- How many orders has each customer placed?
- What is the revenue by order status?
- Which orders have been delivered?
- Which orders were placed after 12 July 2026?

A reusable Snowflake view is also created for customer sales reporting.

---

## 🎯 Objectives

The main objectives of this project are to:

- Create and configure a Snowflake environment
- Create a virtual warehouse, database, and schema
- Create a CSV file format
- Create and use an internal Snowflake stage
- Upload CSV files into Snowflake
- Design relational tables with appropriate data types
- Load CSV data using `COPY INTO`
- Validate imported data
- Perform analytical SQL queries
- Generate business reports
- Create a reusable Snowflake view

---

## 🏗️ Project Architecture

```text
                    CSV Files
                       │
                       │
          ┌────────────▼────────────┐
          │    Snowflake Stage      │
          │       SALES_STAGE       │
          └────────────┬────────────┘
                       │
                    COPY INTO
                       │
          ┌────────────▼────────────┐
          │   Snowflake Tables      │
          │                         │
          │      CUSTOMERS          │
          │      FOODITEMS          │
          │      ORDERS             │
          └────────────┬────────────┘
                       │
                       │ SQL Analytics
                       ▼
          ┌─────────────────────────┐
          │    Business Reports     │
          │                         │
          │ Customer Sales          │
          │ Revenue Analysis        │
          │ Category Revenue        │
          │ Order Status Revenue    │
          │ Top Customers           │
          │ Purchase Frequency      │
          │ Order Analysis          │
          └────────────┬────────────┘
                       │
                       ▼
          ┌─────────────────────────┐
          │  CUSTOMER_SALES_REPORT  │
          │          VIEW           │
          └─────────────────────────┘
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Snowflake** | Cloud Data Warehouse |
| **Snowflake SQL** | Data definition, loading, transformation, and analytics |
| **CSV** | Source data format |
| **Snowsight** | Snowflake development interface |
| **Snowflake Notebook** | SQL development and execution |
| **GitHub** | Version control and project sharing |

---

# ☁️ Snowflake Environment

The following Snowflake objects were created for the project.

### Virtual Warehouse

```text
SALES_WH
```

Configuration:

```text
Warehouse Size : X-Small
Auto Resume    : TRUE
Auto Suspend   : 60 seconds
```

### Database

```text
CUSTOMER_SALES_DB
```

### Schema

```text
SALES_SCHEMA
```

### File Format

```text
CSV_FILE_FORMAT
```

Configuration:

```text
Type            : CSV
Skip Header     : 1
Field Delimiter : ,
```

### Internal Stage

```text
SALES_STAGE
```

---

# 📂 Source Data

The project uses three CSV files.

## 1. customers.csv

Contains customer information.

| Column | Description |
|---|---|
| `customer_id` | Unique Customer ID |
| `first_name` | Customer First Name |
| `last_name` | Customer Last Name |
| `email` | Customer Email |
| `phone` | Customer Phone Number |
| `address` | Customer City/Address |

**Records: 5**

---

## 2. fooditems.csv

Contains food item information.

| Column | Description |
|---|---|
| `food_id` | Unique Food ID |
| `name` | Food Item Name |
| `price` | Food Item Price |
| `category` | Food Category |
| `availability` | Item Availability |

**Records: 5**

---

## 3. orders.csv

Contains customer order transactions.

| Column | Description |
|---|---|
| `order_id` | Unique Order ID |
| `customer_id` | Customer ID |
| `food_id` | Ordered Food Item |
| `quantity` | Quantity Ordered |
| `order_date` | Date and Time of Order |
| `status` | Order Status |
| `total_amount` | Total Bill Amount |

**Records: 12**

---

# 🗄️ Data Warehouse Tables

## CUSTOMERS

```text
customer_id    NUMBER
first_name     VARCHAR
last_name      VARCHAR
email          VARCHAR
phone          VARCHAR
address        VARCHAR
```

## FOODITEMS

```text
food_id        NUMBER
name           VARCHAR
price          NUMBER(10,2)
category       VARCHAR
availability   VARCHAR
```

## ORDERS

```text
order_id       NUMBER
customer_id    NUMBER
food_id        NUMBER
quantity       NUMBER
order_date     TIMESTAMP_NTZ
status         VARCHAR
total_amount   NUMBER(12,2)
```

---

# 📥 Data Loading

The three CSV files were uploaded to the Snowflake internal stage:

```text
@SALES_STAGE
```

The data was loaded into the corresponding tables using Snowflake's `COPY INTO` command.

Example:

```sql
COPY INTO CUSTOMERS
FROM @SALES_STAGE/customers.csv
FILE_FORMAT = (
    FORMAT_NAME = 'CSV_FILE_FORMAT'
)
ON_ERROR = 'ABORT_STATEMENT';
```

The same process was performed for:

```text
FOODITEMS
ORDERS
```

---

# ✅ Data Validation

After loading the data, record counts were verified.

| Table | Expected Records | Loaded Records |
|---|---:|---:|
| CUSTOMERS | 5 | 5 |
| FOODITEMS | 5 | 5 |
| ORDERS | 12 | 12 |

All source records were successfully loaded.

---

# 📊 Business Analysis

The project includes SQL queries for customer spending, revenue analysis, category analysis, order status analysis, customer purchase frequency, and order filtering.

---

## 1. Customer-wise Sales Report

Calculates the total amount spent by each customer.

### Result

| Customer | Total Spent |
|---|---:|
| Amit Sharma | 1150 |
| Priya Singh | 970 |
| Arjun Gupta | 500 |
| Rahul Verma | 460 |
| Neha Patel | 390 |

---

## 2. Highest Spending Customer

Identifies the customer with the highest total spending.

### Result

**Amit Sharma — 1150**

---

## 3. Total Business Revenue

Calculates the total revenue generated from all orders.

### Result

```text
3470
```

---

## 4. Category-wise Revenue

Calculates the total revenue generated by each food category.

### Result

| Category | Revenue |
|---|---:|
| Main Course | 2000 |
| Breakfast | 720 |
| Snacks | 450 |
| Dessert | 300 |

### Data Note

The project specification lists the expected Main Course revenue as `1750`. However, the supplied order transaction data produces `2000` when the Main Course orders are summed.

The SQL result was therefore retained based on the actual transaction data rather than modifying the source data to match the expected value.

---

## 5. Order Status-wise Revenue

Calculates revenue based on the order status.

### Result

| Order Status | Revenue |
|---|---:|
| Delivered | 3350 |
| Preparing | 120 |

Total revenue:

```text
3350 + 120 = 3470
```

---

## 6. Top Three Customers

The top three customers based on total spending are:

| Rank | Customer | Total Spent |
|---:|---|---:|
| 1 | Amit Sharma | 1150 |
| 2 | Priya Singh | 970 |
| 3 | Arjun Gupta | 500 |

---

## 7. Customer Purchase Frequency

Calculates the number of orders placed by each customer.

| Customer | Number of Orders |
|---|---:|
| Amit Sharma | 3 |
| Priya Singh | 3 |
| Arjun Gupta | 2 |
| Rahul Verma | 2 |
| Neha Patel | 2 |

---

## 8. Delivered Orders

Filters the `ORDERS` table to display only orders with:

```sql
status = 'Delivered'
```

The dataset contains **11 delivered orders**.

---

## 9. Orders After 12 July 2026

Retrieves orders placed after:

```text
12 July 2026
```

The resulting orders are:

```text
6, 7, 8, 9, 10, 11, 12
```

---

# 👁️ Snowflake View

A reusable view named:

```text
CUSTOMER_SALES_REPORT
```

was created for customer sales reporting.

The view contains:

| Column | Description |
|---|---|
| `customer_id` | Customer ID |
| `customer_name` | Customer Full Name |
| `total_amount_spent` | Total Amount Spent |

The view can be queried using:

```sql
SELECT *
FROM CUSTOMER_SALES_REPORT;
```

The data can also be sorted by total spending:

```sql
SELECT *
FROM CUSTOMER_SALES_REPORT
ORDER BY total_amount_spent DESC;
```

---

# 📋 Project Tasks

All 25 tasks specified in the project have been completed.

| Task | Description | Status |
|---:|---|:---:|
| 1 | Create `SALES_WH` | ✅ |
| 2 | Create Database | ✅ |
| 3 | Create Schema | ✅ |
| 4 | Select Database and Schema | ✅ |
| 5 | Create CSV File Format | ✅ |
| 6 | Create Internal Stage | ✅ |
| 7 | Upload CSV Files | ✅ |
| 8 | Create Tables | ✅ |
| 9 | Load CSV Data using `COPY INTO` | ✅ |
| 10 | Verify Loaded Data | ✅ |
| 11 | Display Customer Details | ✅ |
| 12 | Display Food Item Details | ✅ |
| 13 | Display Order Details | ✅ |
| 14 | Customer-wise Sales Report | ✅ |
| 15 | Highest Spending Customer | ✅ |
| 16 | Total Business Revenue | ✅ |
| 17 | Category-wise Revenue | ✅ |
| 18 | Order Status-wise Revenue | ✅ |
| 19 | Top Three Customers | ✅ |
| 20 | Customer Purchase Frequency | ✅ |
| 21 | Delivered Orders | ✅ |
| 22 | Orders After 12 July 2026 | ✅ |
| 23 | Create `CUSTOMER_SALES_REPORT` View | ✅ |
| 24 | Retrieve View Records | ✅ |
| 25 | Sort View by Total Spending | ✅ |

---

# 📁 Project Structure

```text
Project-1-Customer-Sales-Analytics/
│
├── README.md
│
├── sql/
│   └── customer_sales_analytics.sql
│
├── data/
│   ├── customers.csv
│   ├── fooditems.csv
│   └── orders.csv
│
├── notebook/
│   └── project1.ipynb
│
└── screenshots/
    ├── warehouse.png
    ├── database_schema.png
    ├── stage.png
    ├── data_loading.png
    ├── data_validation.png
    ├── customer_sales.png
    ├── revenue_analysis.png
    ├── category_revenue.png
    ├── order_status.png
    ├── top_customers.png
    ├── purchase_frequency.png
    ├── delivered_orders.png
    ├── orders_after_date.png
    └── view_report.png
```

---

# 🚀 How to Run the Project

## Prerequisites

- Snowflake account
- Access to Snowsight
- Appropriate Snowflake privileges
- Project CSV files

---

## Step 1 — Create Snowflake Environment

Create the following:

```text
SALES_WH
CUSTOMER_SALES_DB
SALES_SCHEMA
```

Then set the warehouse, database, and schema for the session.

---

## Step 2 — Create CSV File Format

Create:

```text
CSV_FILE_FORMAT
```

with:

```text
TYPE = CSV
SKIP_HEADER = 1
FIELD_DELIMITER = ','
```

---

## Step 3 — Create Internal Stage

Create:

```text
SALES_STAGE
```

and associate it with the CSV file format.

---

## Step 4 — Upload Source Files

Upload:

```text
customers.csv
fooditems.csv
orders.csv
```

to the internal stage.

---

## Step 5 — Create Tables

Create the following tables:

```text
CUSTOMERS
FOODITEMS
ORDERS
```

---

## Step 6 — Load Data

Use the `COPY INTO` command to load each CSV file into its corresponding table.

---

## Step 7 — Validate Data

Verify that the following record counts are present:

```text
CUSTOMERS → 5
FOODITEMS → 5
ORDERS    → 12
```

---

## Step 8 — Run Analytical Queries

Execute the SQL queries included in:

```text
sql/customer_sales_analytics.sql
```

to generate the required business reports.

---

## Step 9 — Create and Query the View

Create:

```text
CUSTOMER_SALES_REPORT
```

and execute the required view queries.

---

# 📸 Project Evidence

The project includes execution evidence for:

- Snowflake warehouse creation
- Database and schema creation
- File format creation
- Internal stage creation
- CSV file upload
- Successful `COPY INTO` operations
- Data validation
- Customer sales analysis
- Highest spending customer
- Total revenue
- Category-wise revenue
- Order status-wise revenue
- Top three customers
- Customer purchase frequency
- Delivered orders
- Orders after 12 July 2026
- View creation
- View execution
- View sorting

The executed Snowflake notebook is also included as a project artifact.

---

# 📚 SQL Concepts Demonstrated

```text
SELECT
WHERE
ORDER BY
GROUP BY
INNER JOIN
SUM()
COUNT()
LIMIT
CREATE WAREHOUSE
CREATE DATABASE
CREATE SCHEMA
CREATE FILE FORMAT
CREATE STAGE
CREATE TABLE
COPY INTO
CREATE VIEW
```

---

# 🎓 Learning Outcomes

Through this project, I gained practical experience in:

- Setting up a Snowflake cloud data warehouse
- Working with Snowflake warehouses, databases, schemas, and stages
- Designing relational tables
- Selecting appropriate SQL data types
- Loading CSV data into Snowflake
- Validating imported data
- Writing analytical SQL queries
- Performing joins and aggregations
- Generating business-oriented reports
- Creating reusable Snowflake views
- Interpreting transactional data for business analysis

---

# 🔮 Future Improvements

Possible improvements and extensions include:

- Implementing a proper **Kimball dimensional model**
- Creating `DIM_CUSTOMER`
- Creating `DIM_FOOD`
- Creating `DIM_DATE`
- Creating a `FACT_ORDERS` table
- Implementing surrogate keys
- Implementing incremental data loading
- Using Snowflake Streams and Tasks
- Building automated ETL pipelines
- Adding data quality checks
- Connecting the warehouse to Power BI or Tableau
- Implementing role-based access control
- Implementing Slowly Changing Dimensions (SCD)

---

# 👨‍💻 Author

**Aashik Reddy**

Computer Science Engineering Student

### Areas of Interest

- Data Engineering
- SQL
- Cloud Data Warehousing
- Data Analytics
- Python
- Full-Stack Development

---

# ⭐ Project Status

```text
PROJECT STATUS: COMPLETED ✅

Snowflake Environment   ✅
Data Ingestion          ✅
Data Validation         ✅
SQL Analytics           ✅
Business Reports        ✅
Snowflake View          ✅
25 Project Tasks        ✅
```

---

## 📄 License

This project was created for educational and placement-training purposes.
