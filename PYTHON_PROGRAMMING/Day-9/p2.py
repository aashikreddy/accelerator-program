"""
Problem Title:Smart E-Commerce Business Intelligence Dashboard using Pandas

Problem Statement:
An e-commerce company maintains customer orders in multiple CSV files.
The management wants to generate a Business Intelligence (BI) dashboard using Pandas.
Four CSV files are available.

Customer File contains:
Customer ID
Customer Name
City

Product File contains:
Product ID
Product Name
Category

Order File contains:
Order ID
Customer ID
Product ID
Quantity

Payment File contains:
Order ID
Payment Amount

The program should perform the following operations.

Step 1: Load all four CSV files using Pandas.
Step 2:Merge Customer, Order, Product and Payment datasets.
Step 3:Display the complete sales report.
Step 4:Using loc(),display all Electronics category orders.
Step 5:Using iloc(),display the second and third order records.
Step 6:Using groupby(),display category-wise total revenue.
Step 7:Display the highest revenue generating category.
Step 8:Display the highest spending customer.

Requirements
------------
1. Read customers.csv.
2. Read products.csv.
3. Read orders.csv.
4. Read payments.csv.
5. Merge multiple DataFrames.
6. Use loc().
7. Use iloc().
8. Use groupby().
9. Display highest revenue category.
10. Display highest spending customer.

Input Files
-----------
customers.csv
products.csv
orders.csv
payments.csv

Output Format
-------------
Complete Sales Report
...
Electronics Orders
...
Second and Third Orders
...
Category Revenue Report
...
Highest Revenue Category
...
Highest Spending Customer
...

customers.csv
---------------
CustomerID,CustomerName,City
C101,Ravi,Hyderabad
C102,Priya,Chennai
C103,Rahul,Bangalore
C104,Anu,Mumbai
C105,Kiran,Hyderabad

products.csv
------------
ProductID,ProductName,Category
P101,Laptop,Electronics
P102,Mobile,Electronics
P103,Shoes,Fashion
P104,Watch,Accessories
P105,Headphones,Electronics


orders.csv
-------------
OrderID,CustomerID,ProductID,Quantity
O101,C101,P101,1
O102,C102,P103,2
O103,C103,P102,1
O104,C104,P104,3
O105,C105,P105,2

payments.csv
-------------
OrderID,PaymentAmount
O101,65000
O102,4000
O103,25000
O104,9000
O105,6000


case=1
output=
Complete Sales Report
O101 Ravi Hyderabad Laptop Electronics 1 65000
O102 Priya Chennai Shoes Fashion 2 4000
O103 Rahul Bangalore Mobile Electronics 1 25000
O104 Anu Mumbai Watch Accessories 3 9000
O105 Kiran Hyderabad Headphones Electronics 2 6000

Electronics Orders
O101 Ravi Laptop 65000
O103 Rahul Mobile 25000
O105 Kiran Headphones 6000

Second and Third Orders
O102 Priya Shoes 4000
O103 Rahul Mobile 25000

Category Revenue Report
Electronics 96000
Accessories 9000
Fashion 4000

Highest Revenue Category
Electronics 96000

Highest Spending Customer
Ravi 65000

"""
# Customer File contains:
# Customer ID
# Customer Name
# City

# Product File contains:
# Product ID
# Product Name
# Category

# Order File contains:
# Order ID
# Customer ID
# Product ID
# Quantity

# Payment File contains:
# Order ID
# Payment Amount

# The program should perform the following operations.

# Step 1: Load all four CSV files using Pandas.
# Step 2:Merge Customer, Order, Product and Payment datasets.
# Step 3:Display the complete sales report.
# Step 4:Using loc(),display all Electronics category orders.
# Step 5:Using iloc(),display the second and third order records.
# Step 6:Using groupby(),display category-wise total revenue.
# Step 7:Display the highest revenue generating category.
# Step 8:Display the highest spending customer.

# Requirements
# ------------
# 1. Read customers.csv.
# 2. Read products.csv.
# 3. Read orders.csv.
# 4. Read payments.csv.
# 5. Merge multiple DataFrames.
# 6. Use loc().
# 7. Use iloc().
# 8. Use groupby().
# 9. Display highest revenue category.
# 10. Display highest spending customer.

# Input Files
# -----------
# customers.csv
# products.csv
# orders.csv
# payments.cs
import pandas as pd
pd.options.display.max_rows=60
pd.options.display.max_columns=60

df1 = pd.read_csv('customers.csv')
df2 = pd.read_csv('products.csv')
df3 = pd.read_csv('orders.csv')
df4 = pd.read_csv('payments.csv')

merge1 = pd.merge(df1, df3, on = 'CustomerID', how = 'inner')
merge2 = pd.merge(merge1, df2, on = 'ProductID',how = 'inner')
merge3 = pd.merge(merge2, df4, on = 'OrderID', how = 'inner')
# O101 Ravi Hyderabad Laptop Electronics 1 65000

print('Complete Sales Report')
print(merge3[['OrderID','CustomerName','City','ProductName','Category','Quantity','PaymentAmount']].to_string(index=False,header=False))

print('\nElectronics Orders')
print(merge3.loc[merge3['Category']=='Electronics',['OrderID','CustomerName','ProductName','PaymentAmount']].to_string(index=False,header=False))

print('\nSecond and Third Orders')
print(merge3.iloc[1:3][['OrderID','CustomerName','ProductName','PaymentAmount']].to_string(header=False,index=False))

print('\nCategory Revenue Report')
category_revenue_report = merge3.groupby('Category')['PaymentAmount'].sum().reset_index()
category_revenue_report.columns = ['Category','Revenue']
category_revenue_report=category_revenue_report.sort_values(by='Revenue',ascending=False)
print(category_revenue_report.to_string(header=False,index=False))
# print(category_revenue_report.columns)

print('\nHighest Revenue Category')
print(category_revenue_report.head(1).to_string(header=False,index=False))

print('\nHighest Spending Customer')
customer_spending = merge3.groupby('CustomerName')['PaymentAmount'].sum().reset_index()
customer_spending.columns = ['CustomerName','TotalSpend']
customer_spending=customer_spending.sort_values(by='TotalSpend',ascending=False)
print(customer_spending.head(1).to_string(index=False,header=False))
