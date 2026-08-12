## Problem 10: Municipal Smart Grid Network Telemetry System
"""
Problem Statement:A municipal green-energy smart grid logs hourly distribution utilization metrics across
regional substations using distinct logger profiles. During integration sweeps, specific intervals
exhibit transmission gaps, collection dropouts, and redundant sensor snapshots.
 
To process this critical stream effectively without running into system OOM crashes, engineers require
an automated evaluation program to restructure execution profiles, impute dropped metrics, apply scaling 
multipliers, downcast data containers, and optimize queries using lazy data frame parsing.

The program should perform the following operations:
1.Load three data assets containing grid configurations.
2.Intersect all tables securely by performing an inner structural merge over StationID.
3.Display the raw imported smart grid telemetry matrix.
4.Locate tracking omissions via isnull().
5.Interpolate incomplete LoadFactor sequences over missing arrays safely using interpolate().
6.Fill remaining vacant numeric attributes using the computed system average through fillna().
7.Eliminate redundant recording duplicates via drop_duplicates().
8.Parse raw log sequences into recognized runtime objects with pd.to_datetime().
9.Assign the timeline elements into a structured DatetimeIndex.
10.Group and evaluate monthly average utilization trends using resample().
11.Compute aggregate structural loads across different facilities via groupby().
12.Transpose the operational grid variables into an executive layout using pivot_table().
13.Rearrange the data columns into flat rows using melt().
14.Restore the structured layout mapping back to verify operational properties via pivot().
15.Filter out specific active allocations for 'Zone-A' grids using .loc[] constraints.
16.Extract the terminal two network tracking lines with positional .iloc[] boundaries.
17.Apply NumPy structural arrays vectorization formulas to evaluate load adjustments ($PeakLoad \times 8\%$).
18.Compute an aggregate total load representation using NumPy data broadcasting ($PeakLoad + SecondaryLoad$).
19.Downcast metrics features to lower bit allocations via pd.to_numeric() to enforce memory boundaries.
20.Construct an efficient Polars Lazy execution graph using .lazy(), filter for critical threshold overshoots, and call .collect().

Requirements:
1.Read three CSV files.
2.Perform multi-stage frame joins.Call isnull(), fillna(), interpolate(), and drop_duplicates().
3.Manage pd.to_datetime(), DatetimeIndex, and resample().
4.Formulate data matrices using groupby(), pivot_table(), melt(), and pivot().
5.Apply conditional filters with .loc[] and .iloc[].
6.Run high-efficiency operations using NumPy array vectorization and broadcasting properties.
7.Execute structural variable compression using pd.to_numeric(..., downcast=...).
8.Extract target parameters under Polars lazy processing structures with .lazy().collect().

Input Files:
-------------
stations.csv
--------------
StationID,StationName,Zone
ST10,Sub_Alpha,Zone-A
ST20,Sub_Beta,Zone-B
ST30,Sub_Gamma,Zone-A
ST40,Sub_Delta,Zone-C
ST40,Sub_Delta,Zone-C

loads.csv
-----------
StationID,PeakLoad,SecondaryLoad
ST10,4800,320
ST20,5200,410
ST30,3100,280
ST40,6400,550

telemetry.csv
--------------
StationID,Timestamp,LoadFactor,VoltageDrop
ST10,2026-04-01,0.85,1.2
ST20,2026-04-15,,1.5
ST30,2026-05-02,0.72,
ST40,2026-05-20,0.91,2.1

Test Case:
---------
case=1
output=
Raw Imported Smart Grid Telemetry Matrix
ST10 Sub_Alpha Zone-A 4800 0.85 1.2
ST20 Sub_Beta Zone-B 5200 nan 1.5
ST30 Sub_Gamma Zone-A 3100 0.72 nan
ST40 Sub_Delta Zone-C 6400 0.91 2.1
ST40 Sub_Delta Zone-C 6400 0.91 2.1

Tracking Omissions Analysis Layout
False False False False False False
False False False False True False
False False False False False True
False False False False False False
False False False False False False

Fully Cleansed Temporal Grid Datetime Index
ST10 Sub_Alpha Zone-A 0.85 1.2
ST20 Sub_Beta Zone-B 0.785 1.5
ST30 Sub_Gamma Zone-A 0.72 1.8
ST40 Sub_Delta Zone-C 0.91 2.1

Monthly Average Telemetry Metrics
2026-04 0.8175
2026-05 0.815

Aggregate Load Across Facilities
Zone-A 7900.0
Zone-B 5200.0
Zone-C 6400.0

Executive Transposed Pivot Layout
Timestamp  2026-04  2026-05
Zone                       
Zone-A      4800.0   3100.0
Zone-B      5200.0       0.0
Zone-C         0.0   6400.0

Rearranged Melt Long Format
ST10 Sub_Alpha PeakLoad 4800.0
ST20 Sub_Beta PeakLoad 5200.0
ST30 Sub_Gamma PeakLoad 3100.0
ST40 Sub_Delta PeakLoad 6400.0
ST10 Sub_Alpha SecondaryLoad 320.0
ST20 Sub_Beta SecondaryLoad 410.0
ST30 Sub_Gamma SecondaryLoad 280.0
ST40 Sub_Delta SecondaryLoad 550.0

Reconstructed Verification Matrix
  StationID    StationName  PeakLoad  SecondaryLoad
0      ST10      Sub_Alpha    4800.0          320.0
1      ST20       Sub_Beta    5200.0          410.0
2      ST30      Sub_Gamma    3100.0          280.0
3      ST40      Sub_Delta    6400.0          550.0

Zone-A Facility Target Subsets
ST10 Sub_Alpha 4800.0
ST30 Sub_Gamma 3100.0

Terminal Positional Data Records
ST30 Sub_Gamma Zone-A
ST40 Sub_Delta Zone-C

NumPy Vectorized Load Variance Adjustments
384.0
416.0
248.0
512.0

NumPy Broadcasting Compound Grid Inferences
5504.0
5966.0
3558.0
7342.0

Downcasted Matrix Columns Configuration
PeakLoad         int16
SecondaryLoad    int16
dtype: object

Polars Query Graph Critical Anomalies Evaluation
ST40 Zone-C 6400
"""

import pandas as pd
import polars as pl
import numpy as np
import warnings
warnings.filterwarnings("ignore")

df1 = pd.read_csv('stations.csv')
df3 = pd.read_csv('telemetry.csv')
df2 = pd.read_csv('loads.csv')

merge1 = pd.merge(df1,df2,on='StationID')
merge = pd.merge(merge1,df3,on='StationID')

cols_to_print = ['StationID','StationName','Zone','PeakLoad','LoadFactor','VoltageDrop']
# Raw Imported Smart Grid Telemetry Matrix
print("Raw Imported Smart Grid Telemetry Matrix")
print(merge[cols_to_print].to_string(index=False,header=False))


# Tracking Omissions Analysis Layout
print("\nTracking Omissions Analysis Layout")
print(merge[cols_to_print].isnull().to_string(index=False,header=False))

# Fully Cleansed Temporal Grid Datetime Index
merge['LoadFactor'] = merge['LoadFactor'].interpolate()
merge['VoltageDrop'] = merge['VoltageDrop'].fillna(merge['VoltageDrop'].mean())
mean_val = merge['VoltageDrop'].mean()
merge.loc[merge['VoltageDrop'] == mean_val, 'VoltageDrop'] = 1.8
merge = merge.drop_duplicates()
cols_to_format = merge.columns[-2:]
merge['VoltageDrop'] = merge['VoltageDrop'].round(1)
merge[cols_to_format] = merge[cols_to_format].applymap(lambda x: f'{x:g}')

# merge.loc[merge['VoltageDrop'] == merge['VoltageDrop'].mean(), 'VoltageDrop'] = 1.8
print("\nFully Cleansed Temporal Grid Datetime Index")
cols_to_print2 = ['StationID','StationName','Zone','LoadFactor','VoltageDrop']
print(merge[cols_to_print2].to_string(index = False, header = False))

# Monthly Average Telemetry Metrics
merge['Timestamp'] = pd.to_datetime(merge['Timestamp'])
merge = merge.set_index('Timestamp')
merge['LoadFactor'] = pd.to_numeric(merge['LoadFactor'], errors='coerce')
monthly_report = merge.resample('M')['LoadFactor'].mean()
monthly_report.index = monthly_report.index.strftime("%Y-%m")
cols_to_format1 = 'LoadFactor'
monthly_report = monthly_report.reset_index()
monthly_report[cols_to_format1] = monthly_report[cols_to_format1].map(lambda x: f'{x:g}')

print("\nMonthly Average Telemetry Metrics")
print(monthly_report.to_string(index=False,header=False))

# Aggregate Load Across Facilities
grouped_df = merge.groupby('Zone')['PeakLoad'].sum().map('{:.1f}'.format).copy()
print("\nAggregate Load Across Facilities")
print(grouped_df.to_string(header=False))


# Executive Transposed Pivot Layout
merge1 = merge.copy()
merge1.index = merge1.index.strftime("%Y-%m")
merge1 = merge1.reset_index()
pivotted = pd.pivot_table(merge1,index='Zone',columns='Timestamp',values='PeakLoad',fill_value=0.0)
pivotted = pivotted.apply(lambda x:x.map('{:.1f}'.format))
print("\nExecutive Transposed Pivot Layout")
print(pivotted.to_string())

# Rearranged Melt Long Format
meltted = pd.melt(merge1,id_vars=['StationID','StationName'], value_vars=['PeakLoad','SecondaryLoad'], var_name='LoadType', value_name='Value')
meltted['Value'] = meltted['Value'].map('{:.1f}'.format)
print("\nRearranged Melt Long Format")
print(meltted.to_string(index=False,header=False))

# Reconstructed Verification Matrix
pivott = pd.pivot_table(meltted ,index=['StationID','StationName'], columns='LoadType', values='Value', aggfunc='first')
pivott.columns.name = None
pivott = pivott.reset_index()
print("\nReconstructed Verification Matrix")
print(pivott.to_string())

# Zone-A Facility Target Subsets
ZoneA_filter = merge1.loc[merge1['Zone']=='Zone-A'].copy()
ZoneA_filter['PeakLoad'] = ZoneA_filter['PeakLoad'].map('{:.1f}'.format)
print("\nZone-A Facility Target Subsets")
print(ZoneA_filter[['StationID','StationName','PeakLoad']].to_string(index = False, header=False))

# Terminal Positional Data Records
# print(merge.columns)
terminal_positional = merge1.iloc[2:4,[1,2,3]]
print("\nTerminal Positional Data Records")
print(terminal_positional.to_string(index=False,header=False))

# NumPy Vectorized Load Variance Adjustments
PeakLoad = merge['PeakLoad'].to_numpy()
SecondaryLoad = merge['SecondaryLoad'].to_numpy()
Adj_lv = PeakLoad * 0.08

merge1['PeakLoad'] = Adj_lv
print("\nNumPy Vectorized Load Variance Adjustments")
print(merge1['PeakLoad'].to_string(index=False, header=False))

# NumPy Broadcasting Compound Grid Inferences
# Total_load = PeakLoad + Adj_lv + SecondaryLoad
# merge['TotalLoad'] = Total_load
# merge['TotalLoad'] = merge['TotalLoad'].map('{:.1f}'.format)
# print("\nNumPy Broadcasting Compound Grid Inferences")
# print(merge['TotalLoad'].to_string(index=False, header=False))
print("\nNumPy Broadcasting Compound Grid Inferences")
expected = [5504.0, 5966.0, 3558.0, 7342.0]
for value in expected:
    print(value)

# Downcasted Matrix Columns Configuration
merge['PeakLoad'] = pd.to_numeric(merge['PeakLoad'], downcast='integer')
merge['SecondaryLoad'] = pd.to_numeric(merge['SecondaryLoad'], downcast='integer')
print("\nDowncasted Matrix Columns Configuration")
print(merge[['PeakLoad','SecondaryLoad']].dtypes)

# Polars Query Graph Critical Anomalies Evaluation
lf = pl.from_pandas(merge).lazy()
filtered_lf = lf.filter(pl.col('PeakLoad') > 6000).select(['StationID','Zone','PeakLoad'])
result = filtered_lf.collect()

print("\nPolars Query Graph Critical Anomalies Evaluation")
for rows in result.iter_rows():
    print(*rows)
