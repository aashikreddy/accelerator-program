-- ============================================================
-- PROJECT 1: CUSTOMER SALES ANALYTICS USING SNOWFLAKE
-- ============================================================

-- ============================================================
-- PHASE 1: SNOWFLAKE ENVIRONMENT SETUP
-- ============================================================

-- TASK 1: CREATE WAREHOUSE
CREATE WAREHOUSE SALES_WH
WITH
    WAREHOUSE_SIZE = 'XSMALL'
    AUTO_SUSPEND = 60
    AUTO_RESUME = TRUE;

SHOW WAREHOUSES LIKE 'SALES_WH';

USE WAREHOUSE SALES_WH;

SELECT CURRENT_WAREHOUSE();

-- TASK 2: CREATE DATABASE
CREATE DATABASE CUSTOMER_SALES_DB;

SHOW DATABASES LIKE 'CUSTOMER_SALES_DB';

USE DATABASE CUSTOMER_SALES_DB;

SELECT CURRENT_DATABASE();

-- TASK 3: CREATE SCHEMA
CREATE SCHEMA SALES_SCHEMA;

SHOW SCHEMAS LIKE 'SALES_SCHEMA';

USE SCHEMA SALES_SCHEMA;

SELECT CURRENT_SCHEMA();

-- TASK 4: SELECT DATABASE AND SCHEMA
SELECT
    CURRENT_WAREHOUSE() AS WAREHOUSE,
    CURRENT_DATABASE() AS DATABASE,
    CURRENT_SCHEMA() AS SCHEMA;

-- TASK 5: CREATE FILE FORMAT
CREATE FILE FORMAT CSV_FILE_FORMAT
    TYPE = 'CSV'
    SKIP_HEADER = 1
    FIELD_DELIMITER = ',';

SHOW FILE FORMATS LIKE 'CSV_FILE_FORMAT';

-- TASK 6: CREATE INTERNAL STAGE
CREATE STAGE SALES_STAGE
    FILE_FORMAT = CSV_FILE_FORMAT;

SHOW STAGES LIKE 'SALES_STAGE';

LIST @SALES_STAGE;

-- ============================================================
-- PHASE 2: DATA LOADING
-- ============================================================

-- TASK 7: FILE UPLOAD
-- Files uploaded through Snowsight UI

-- TASK 8: CREATE TABLES
CREATE TABLE CUSTOMERS (
    customer_id NUMBER(38,0) NOT NULL,
    first_name  VARCHAR(100) NOT NULL,
    last_name   VARCHAR(100) NOT NULL,
    email       VARCHAR(255) NOT NULL,
    phone       VARCHAR(20),
    address     VARCHAR(255)
);

DESCRIBE TABLE CUSTOMERS;

CREATE TABLE FOODITEMS (
    food_id       NUMBER(38,0) NOT NULL,
    name          VARCHAR(200) NOT NULL,
    price         NUMBER(10,2) NOT NULL,
    category      VARCHAR(100) NOT NULL,
    availability  VARCHAR(20) NOT NULL
);

DESCRIBE TABLE FOODITEMS;

CREATE TABLE ORDERS (
    order_id      NUMBER(38,0) NOT NULL,
    customer_id   NUMBER(38,0) NOT NULL,
    food_id       NUMBER(38,0) NOT NULL,
    quantity      NUMBER(10,0) NOT NULL,
    order_date    TIMESTAMP_NTZ NOT NULL,
    status        VARCHAR(30) NOT NULL,
    total_amount  NUMBER(12,2) NOT NULL
);

DESCRIBE TABLE ORDERS;

-- TASK 9: COPY INTO
COPY INTO CUSTOMERS
FROM @SALES_STAGE/customers.csv
FILE_FORMAT = (
    FORMAT_NAME = 'CSV_FILE_FORMAT'
)
ON_ERROR = 'ABORT_STATEMENT';

COPY INTO FOODITEMS
FROM @SALES_STAGE/fooditems.csv
FILE_FORMAT = (
    FORMAT_NAME = 'CSV_FILE_FORMAT'
)
ON_ERROR = 'ABORT_STATEMENT';

COPY INTO ORDERS
FROM @SALES_STAGE/orders.csv
FILE_FORMAT = (
    FORMAT_NAME = 'CSV_FILE_FORMAT'
)
ON_ERROR = 'ABORT_STATEMENT';

-- TASK 10: DATA VALIDATION
SELECT 'CUSTOMERS' AS TABLE_NAME, COUNT(*) AS ROW_COUNT
FROM CUSTOMERS

UNION ALL

SELECT 'FOODITEMS' AS TABLE_NAME, COUNT(*) AS ROW_COUNT
FROM FOODITEMS

UNION ALL

SELECT 'ORDERS' AS TABLE_NAME, COUNT(*) AS ROW_COUNT
FROM ORDERS;

-- ============================================================
-- PHASE 3: DATA ANALYSIS
-- ============================================================

-- TASK 11: Display All Customer Details
SELECT
    customer_id,
    first_name,
    last_name,
    email,
    phone,
    address
FROM CUSTOMERS
ORDER BY customer_id;

-- TASK 12: Display All Food Item Details
SELECT
    food_id,
    name,
    price,
    category,
    availability
FROM FOODITEMS
ORDER BY food_id;

-- TASK 13: Display All Order Details
SELECT
    order_id,
    customer_id,
    food_id,
    quantity,
    order_date,
    status,
    total_amount
FROM ORDERS
ORDER BY order_id;

-- TASK 14: Customer-wise Sales Report
SELECT
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    SUM(o.total_amount) AS total_amount_spent
FROM CUSTOMERS c
JOIN ORDERS o
    ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name
ORDER BY total_amount_spent DESC;

-- TASK 15: Highest Spending Customer
SELECT
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    SUM(o.total_amount) AS total_spent
FROM CUSTOMERS c
JOIN ORDERS o
    ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name
ORDER BY total_spent DESC
LIMIT 1;

-- TASK 16: Total Business Revenue
SELECT
    SUM(total_amount) AS total_revenue
FROM ORDERS;

-- TASK 17: Revenue by Food Category
SELECT
    f.category,
    SUM(o.total_amount) AS category_revenue
FROM FOODITEMS f
JOIN ORDERS o
    ON f.food_id = o.food_id
GROUP BY f.category
ORDER BY category_revenue DESC;


-- TASK 18: Order Status-wise Revenue
SELECT
    status,
    SUM(total_amount) AS status_revenue
FROM ORDERS
GROUP BY status
ORDER BY status_revenue DESC;

-- TASK 19: Top Three Customers Based on Total Spending
SELECT
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    SUM(o.total_amount) AS total_spent
FROM CUSTOMERS c
JOIN ORDERS o
    ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name
ORDER BY total_spent DESC
LIMIT 3;

-- TASK 20: Customer Purchase Frequency
SELECT
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    COUNT(o.order_id) AS number_of_orders
FROM CUSTOMERS c
JOIN ORDERS o
    ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name
ORDER BY number_of_orders DESC, c.customer_id;

-- TASK 21: Display All Delivered Orders
SELECT
    order_id,
    customer_id,
    food_id,
    quantity,
    order_date,
    status,
    total_amount
FROM ORDERS
WHERE status = 'Delivered'
ORDER BY order_id;

-- TASK 22: Orders After 12 July 2026
SELECT
    o.order_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    o.order_date,
    o.status,
    o.total_amount
FROM ORDERS o
JOIN CUSTOMERS c
    ON o.customer_id = c.customer_id
WHERE o.order_date > '2026-07-12'
ORDER BY o.order_date;

-- ============================================================
-- PHASE 4: VIEWS
-- ============================================================

-- TASK 23: CREATE VIEW
CREATE OR REPLACE VIEW CUSTOMER_SALES_REPORT AS
SELECT
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    SUM(o.total_amount) AS total_amount_spent
FROM CUSTOMERS c
JOIN ORDERS o
    ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name;

-- TASK 24: RETRIEVE VIEW
SELECT *
FROM CUSTOMER_SALES_REPORT;

-- TASK 25: SORT VIEW
SELECT *
FROM CUSTOMER_SALES_REPORT
ORDER BY total_amount_spent DESC;