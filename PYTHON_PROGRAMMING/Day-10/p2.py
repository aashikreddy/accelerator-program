"""
Problem Title: Smart Retail Business Intelligence Dashboard using NumPy and Pandas

Problem Statement:

A multinational retail company maintains its business data in multiple CSV files.

The management wants to generate a complete Business Intelligence Dashboard using both NumPy and Pandas.

Four CSV files are available.

Customer File contains:
Customer ID
Customer Name
City

Product File contains:
Product ID
Product Name
Category
Unit Price

Order File contains:
Order ID
Customer ID
Product ID
Order Date
Quantity

Payment File contains:
Order ID
Payment Amount

The program should perform the following operations.

Step 1:Load all CSV files using Pandas.
Step 2:Merge all datasets into a single DataFrame.
Step 3:Convert Order Date into Datetime format.
Step 4:Create a monthly revenue report using resample().
Step 5:Create a Pivot Table showing category-wise monthly revenue.
Step 6:Using groupby(), display category-wise total revenue.
Step 7:Using loc(),display only Electronics orders.
Step 8:Using iloc(),display the second and third order records.
Step 9:Using NumPy,calculate a 10% bonus revenue for every payment using Vectorization.
Bonus Revenue=Payment Amount × 10%

Step 10:Using NumPy Broadcasting,calculate the Final Revenue.
Final Revenue=Payment Amount + Bonus Revenue

Step 11:Display the highest revenue category.
Step 12:Display the highest spending customer.

Requirements
------------
1. Read four CSV files.
2. Merge multiple DataFrames.
3. Use loc().
4. Use iloc().
5. Use groupby().
6. Use pivot_table().
7. Use pd.to_datetime().
8. Use DatetimeIndex.
9. Use resample().
10. Use NumPy Arrays.
11. Use Vectorization.
12. Use Broadcasting.

Input Files
-----------
customers.csv
products.csv
orders.csv
payments.csv

Output Format
-------------
Complete Business Report
...
Electronics Orders
...
Second and Third Orders
...
Monthly Revenue Report
...
Category-wise Monthly Revenue Pivot Table
...
Category Revenue Report
...
Updated Revenue (10% Bonus)
...
Highest Revenue Category
...
Highest Spending Customer
...

customers.csv
--------------
CustomerID,CustomerName,City
C101,Ravi,Hyderabad
C102,Priya,Chennai
C103,Rahul,Bangalore
C104,Anu,Mumbai
C105,Kiran,Hyderabad


products.csv
-------------
ProductID,ProductName,Category,UnitPrice
P101,Laptop,Electronics,65000
P102,Mobile,Electronics,25000
P103,Shoes,Fashion,2000
P104,Watch,Accessories,3000
P105,Headphones,Electronics,3000

orders.csv
------------
OrderID,CustomerID,ProductID,OrderDate,Quantity
O101,C101,P101,2025-01-05,1
O102,C102,P103,2025-01-15,2
O103,C103,P102,2025-02-02,1
O104,C104,P104,2025-02-18,3
O105,C105,P105,2025-03-10,2

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
Complete Business Report
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

Monthly Revenue Report
2025-01 69000
2025-02 34000
2025-03 6000

Category-wise Monthly Revenue Pivot Table

Category 2025-01 2025-02 2025-03
Accessories 0 9000 0
Electronics 65000 25000 6000
Fashion 4000 0 0

Category Revenue Report
Electronics 96000
Accessories 9000
Fashion 4000

Updated Revenue (10% Bonus)
65000 6500.0 71500.0
4000 400.0 4400.0
25000 2500.0 27500.0
9000 900.0 9900.0
6000 600.0 6600.0

Highest Revenue Category
Electronics 96000

Highest Spending Customer
Ravi 65000
"""
import pandas as pd
import numpy as np

pd.options.display.max_rows=60
pd.options.display.max_columns=60

df1 = pd.read_csv('customers.csv')
df2 = pd.read_csv('products.csv')
df3 = pd.read_csv('orders.csv')
df4 = pd.read_csv('payments.csv')

merge1 = pd.merge(df1,df3,on='CustomerID')
merge2 = pd.merge(merge1,df2,on='ProductID')
final_merge = pd.merge(merge2,df4,on='OrderID')
# O101 Ravi Hyderabad Laptop Electronics 1 65000
final_merge['OrderDate'] = pd.to_datetime(final_merge['OrderDate'])
# print(final_merge.to_string(index = False))

print("Complete Business Report")
print(final_merge[['OrderID','CustomerName','City','ProductName','Category','Quantity','PaymentAmount']].to_string(index = False,header=False))

print("\nElectronics Orders")
electronic_orders = final_merge.loc[final_merge['Category']=='Electronics']
# O101 Ravi Laptop 65000
print(electronic_orders[['OrderID','CustomerName','ProductName','PaymentAmount']].to_string(index = False,header = False))

print('\nSecond and Third Orders')
print(final_merge.iloc[1:3,[3,1,7,10]].to_string(index = False, header = False))

print("\nMonthly Revenue Report")
final_merge1 = final_merge.set_index('OrderDate')
monthly_report = final_merge1['PaymentAmount'].resample('M').sum()
monthly_report.index = monthly_report.index.strftime("%Y-%m")
print(monthly_report.to_string(header = False))

print("\nCategory-wise Monthly Revenue Pivot Table\n")
# monthly_report = monthly_report.reset_index()
pivoted_df = pd.pivot_table(final_merge1,
    index='Category',
    columns = final_merge1.index.strftime("%Y-%m"),
    values = 'PaymentAmount',
    aggfunc = 'sum',
    fill_value = 0
    )
pivoted_df.columns.name = None
pivoted_df = pivoted_df.sort_index()
pivoted_df = pivoted_df.reset_index()
print(pivoted_df.to_string(index=False))

print("\nCategory Revenue Report")
category = final_merge1.groupby('Category')['PaymentAmount'].sum()
category = category.sort_values(ascending = False)
print(category.to_string(header = False))

print("\nUpdated Revenue (10% Bonus)")
payment = final_merge1["PaymentAmount"].to_numpy()
bonus = payment * 0.10
final = payment + bonus

for i in range(len(payment)):
    print(payment[i],bonus[i],final[i])

print("\nHighest Revenue Category")
print(category.idxmax(), category.max())

print("\nHighest Spending Customer")
customers = final_merge1.groupby("CustomerName")["PaymentAmount"].sum()
print(customers.idxmax(), customers.max())
