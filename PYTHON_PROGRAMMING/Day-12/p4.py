## Problem 4: Hybrid Strategy: Chunked Processing with In-Flight Downcasting 
"""
Problem Statement:
Your production infrastructure requires processing a massive metrics export 
file under strict 5 GB layout constraints. 
You cannot hold uncompressed objects or entire segments in memory. 
You must integrate a chunking strategy with  real-time numeric optimization on 
each slice before appending it to global counters.

The program must execute the following operations:
--------------------------------------------------
Stream metric records in slices of 2 rows at a time.
For each incoming slice, downcast the MetricValue to its minimal valid numeric memory layout.
Compute and print out the localized safe peak memory overhead of that chunk's MetricValue slice.
Aggregate the global absolute maximum value observed across the entire stream.

Requirements:
-------------
Combine chunksize and pd.to_numeric(..., downcast='float').
Track a rolling global scalar.

Input File:
-------------
metrics.csv

Output Format:
-------------
Chunk Processed - Overhead: ... Bytes
...
Global Peak Metric Observed: ...


Sample metrics.csv:
-------------
Timestamp,MetricName,MetricValue
16112101,CPU_Usage,88.50
16112102,CPU_Usage,92.10
16112103,CPU_Usage,45.00
16112104,CPU_Usage,71.25

Test Case:
-------------
case=1
output=
Chunk Processed - Overhead: 8 Bytes                                             
Chunk Processed - Overhead: 8 Bytes                                             
                                                                                
Global Peak Metric Observed: 92.0999984741211  

"""
import pandas as pd

overhead = 0
global_max = None

for chunk in pd.read_csv('metrics.csv',chunksize=2):
    chunk['MetricValue'] = pd.to_numeric(chunk['MetricValue'],downcast='float')
    cur_max = chunk['MetricValue'].max()
    if global_max is None:
        global_max = cur_max
    elif cur_max > global_max:
        global_max = cur_max
    overhead = chunk['MetricValue'].memory_usage(index=False,deep=False)
    print(f"Chunk Processed - Overhead: {overhead} Bytes")

print(f"\nGlobal Peak Metric Observed: {global_max}")


## Problem 3: Memory-Bounded Categorical Optimization 
"""
Problem Statement:
An enterprise customer support desk logs hundreds of thousands of tickets every single day. 
The Status and Priority labels represent structural repeating patterns with 
high unique-string memory overhead. A script is needed to automatically optimize 
string objects to lighter memory footprints.

The application must execute the following operations:
Parse the support tickets log dataset.
Calculate and display the memory footprint of the string text columns (Status and Priority) combined.
Convert these columns from the default object data type to the optimized Pandas category type.
Calculate and display the new optimized memory footprint.
Provide a summary breakdown showing the category codes map.

Requirements:
Use astype('category').
Compare column .memory_usage(deep=True).

Input File:
--------------------
tickets.csv

Output Format:
--------------------
Unoptimized String Memory: ... Bytes
Optimized Category Memory: ... Bytes
Status Codes Mapping
...

Sample tickets.csv:
--------------------
TicketID,Status,Priority
T1,Open,High
T2,Closed,Low
T3,Open,Medium
T4,Open,High
T5,Closed,Low
Test Case:


case=1
output=
Unoptimized String Memory: 614 Bytes
Optimized Category Memory: 534 Bytes
Status Codes Mapping
Closed : 0
Open : 1

"""
import pandas as pd

df = pd.read_csv('tickets.csv')

unoptmized_memory = df[['Status','Priority']].memory_usage(deep=True,index=False).sum()
print(f"Unoptimized String Memory: {unoptmized_memory} Bytes")

df['Status'] = df['Status'].astype('category')
df['Priority'] = df['Priority'].astype('category')

optimized_memory = df[['Status','Priority']].memory_usage(deep=True,index=False).sum()
print(f"Optimized Category Memory: {optimized_memory} Bytes")

print("Status Codes Mapping")
for c,v in enumerate(df['Status'].cat.categories):
    print(f"{v} : {c}")
    



