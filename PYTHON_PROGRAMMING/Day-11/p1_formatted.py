"""
Project Title: Smart Hospital Patient Data Cleansing and Healthcare Intelligence Platform using NumPy and Pandas

Problem Statement:
A multi-specialty hospital maintains patient information in multiple CSV files.
Patient records are collected from different hospital branches. During synchronization, 
some records contain missing values, duplicate entries, and inconsistent treatment information.
Before generating analytical reports, the hospital management wants to clean the data and 
generate a Healthcare Intelligence Dashboard.

The available CSV files are:
Patient File Contains
Patient ID
Patient Name
Department
Age

Treatment File Contains
Patient ID
Consultation Cost
Lab Cost
Pharmacy Cost

Billing File Contains
Patient ID
Admission Date
Total Bill

Vitals File Contains
    Patient ID
    Blood Pressure
 Some records contain
    Missing Treatment Costs
    Missing Blood Pressure
    Duplicate Patient Records

The program should perform the following operations.
Step 1:Load all four CSV files using Pandas.
Step 2:Merge all DataFrames using Patient ID.
Step 3: Display the complete merged dataset.
Step 4:Display missing values using isnull().
Step 5:Fill missing Total Bill using the average bill of all patients using fillna().
Step 6:Recover missing Blood Pressure using interpolate().
Step 7:Remove duplicate patient records using drop_duplicates().
Step 8:Convert Admission Date into Datetime using pd.to_datetime().
Step 9:Set Admission Date as DatetimeIndex.
Step 10:Generate Monthly Hospital Revenue using resample().
Step 11:Generate Department-wise Revenue using groupby().
Step 12:Generate a Department-wise Revenue Pivot Table using pivot_table().
Step 13:Convert Treatment Columns
Consultation Cost
Lab Cost
Pharmacy Cost
into Long Format using melt().

Step 14:Reconstruct the original treatment table using pivot().
Step 15:Using loc() Display only Cardiology patients.
Step 16:Using iloc() Display second and third patient records.
Step 17: Using NumPy Vectorization
Calculate
Insurance Bonus
Insurance Bonus = Total Bill × 5%

Step 18:Using NumPy Broadcasting
Calculate:Final Bill = Total Bill + Insurance Bonus

Step 19:Display the department generating the highest revenue.

Step 20:Display the patient having the highest bill.

Requirements:
----------------
Read four CSV files.
Merge multiple DataFrames.
Use isnull().
Use fillna().
Use interpolate().
Use drop_duplicates().
Use pd.to_datetime().
Use DatetimeIndex.
Use resample().
Use groupby().
Use pivot_table().
Use melt().
Use pivot().
Use loc().
Use iloc().
Use NumPy Arrays.
Use Vectorization.
Use Broadcasting.


Input Files:
--------------
patients.csv
----------
PatientID,PatientName,Department,Age
P101,Ravi,Cardiology,45
P102,Priya,Neurology,38
P103,Rahul,Orthopedics,50
P104,Anu,Cardiology,42
P105,Kiran,Neurology,36
P105,Kiran,Neurology,36

Note: Last record is intentionally duplicated.
It will be removed using drop_duplicates().

treatments.csv
--------------
PatientID,ConsultationCost,LabCost,PharmacyCost
P101,500,1200,800
P102,600,1000,900
P103,550,1500,1000
P104,650,1100,850
P105,500,1300,950



billing.csv
--------------
PatientID,AdmissionDate,TotalBill
P101,2025-01-05,25000
P102,2025-01-18,
P103,2025-02-10,32000
P104,2025-02-20,28000
P105,2025-03-08,

Note:Missing bills for
P102
P105
These must be filled

vitals.csv
--------------
PatientID,BloodPressure
P101,120
P102,
P103,130
P104,
P105,125

Missing Blood Pressure:
P102
P104
These will be recovered 


case=1
output=
Complete Hospital Report
P101 Ravi Cardiology 45 500 1200 800 2025-01-05 25000.0 120.0
P102 Priya Neurology 38 600 1000 900 2025-01-18 nan nan
P103 Rahul Orthopedics 50 550 1500 1000 2025-02-10 32000.0 130.0
P104 Anu Cardiology 42 650 1100 850 2025-02-20 28000.0 nan
P105 Kiran Neurology 36 500 1300 950 2025-03-08 nan 125.0
P105 Kiran Neurology 36 500 1300 950 2025-03-08 nan 125.0

Missing Values
False False False False False False False False False False
False False False False False False False False True True
False False False False False False False False False False
False False False False False False False False False True
False False False False False False False False True False
False False False False False False False False True False

Recovered Dataset
P101 Ravi Cardiology 45 25000.0 120.0
P102 Priya Neurology 38 28333.33 125.0
P103 Rahul Orthopedics 50 32000.0 130.0
P104 Anu Cardiology 42 28000.0 127.5
P105 Kiran Neurology 36 28333.33 125.0

Monthly Hospital Revenue
2025-01 53333.33
2025-02 60000.0
2025-03 28333.33

Department Revenue
Cardiology 53000.0
Neurology 56666.67
Orthopedics 32000.0

Department Revenue Pivot Table

OrderDate    2025-01  2025-02  2025-03
Department
Cardiology    25000.0   28000.0      0.0
Neurology     28333.33      0.0 28333.33
Orthopedics       0.0   32000.0      0.0

Treatment Long Format
P101 Ravi ConsultationCost 500
P102 Priya ConsultationCost 600
P103 Rahul ConsultationCost 550
P104 Anu ConsultationCost 650
P105 Kiran ConsultationCost 500
P101 Ravi LabCost 1200
P102 Priya LabCost 1000
P103 Rahul LabCost 1500
P104 Anu LabCost 1100
P105 Kiran LabCost 1300
P101 Ravi PharmacyCost 800
P102 Priya PharmacyCost 900
P103 Rahul PharmacyCost 1000
P104 Anu PharmacyCost 850
P105 Kiran PharmacyCost 950

Reconstructed Treatment Dataset

Treatment PatientID PatientName ConsultationCost LabCost PharmacyCost
0 P101 Ravi 500 1200 800
1 P102 Priya 600 1000 900
2 P103 Rahul 550 1500 1000
3 P104 Anu 650 1100 850
4 P105 Kiran 500 1300 950

Cardiology Patients
P101 Ravi 25000.0
P104 Anu 28000.0

Second and Third Patients
P102 Priya Neurology
P103 Rahul Orthopedics

Insurance Bonus
1250.0
1416.67
1600.0
1400.0
1416.67

Final Bill
26250.0
29750.0
33600.0
29400.0
29750.0

Highest Revenue Department
Neurology 56666.67

Highest Bill Patient
P103 Rahul 32000.0
"""

import pandas as pd
import numpy as np
import os
# import sys

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

df1 = pd.read_csv(os.path.join(script_dir, 'patients.csv'))
df2 = pd.read_csv(os.path.join(script_dir, 'treatments.csv'))
df3 = pd.read_csv(os.path.join(script_dir, 'billing.csv'))
df4 = pd.read_csv(os.path.join(script_dir, 'vitals.csv'))

merge1 = pd.merge(df1,df2,on='PatientID')
merge2 = pd.merge(df3,df4,on='PatientID')
final = pd.merge(merge1,merge2,on='PatientID')
# print(sys.version)
print("Complete Hospital Report")
print(final.round({'TotalBill':2,'BloodPressure':2}).to_string(index=False,header=False))

print("\nMissing Values")
print(final.isnull().to_string(index=False,header=False))

final['TotalBill'] = final['TotalBill'].fillna(final['TotalBill'].mean())
final['BloodPressure'] = final['BloodPressure'].interpolate()


print("\nRecovered Dataset")

final = final.drop_duplicates()
print(final.to_string(index=False,header=False))

final['AdmissionDate'] = pd.to_datetime(final['AdmissionDate'])

final = final.set_index('AdmissionDate')

monthly_revenue = final.resample('ME').sum()
monthly_revenue = monthly_revenue.reset_index()
monthly_revenue['AdmissionDate'] = monthly_revenue['AdmissionDate'].dt.strftime("%Y-%m")

print()

print('\nMonthly Hospital Revenue')
monthly_revenue['TotalBill'] = monthly_revenue['TotalBill'].round(2)
 

print(monthly_revenue[['AdmissionDate','TotalBill']].to_string(index=False,header=False))

print("\nDepartment Revenue")
department_revenue = final.groupby('Department')['TotalBill'].sum().rename_axis(None)
print(department_revenue.to_string())


print("\nDepartment Revenue Pivot Table\n")

final_1 = final.copy()
final_1 = final_1.reset_index()

final_1['AdmissionDate'] = final_1['AdmissionDate'].dt.strftime('%Y-%m')


pivotted = pd.pivot_table(final_1, index="Department", columns="AdmissionDate", values="TotalBill",fill_value=0)
pivotted.columns.name = 'OrderDate' 
print(pivotted.to_string())

print("\nTreatment Long Format")
meltted = pd.melt(final,id_vars=['PatientID','PatientName'],value_vars=['ConsultationCost','LabCost','PharmacyCost'])
print(meltted.to_string(index=False,header=False))

print("\nReconstructed Treatment Dataset\n")
pivot = pd.pivot(meltted,index=['PatientID','PatientName'],columns='variable',values='value').reset_index()
pivot.columns.name = None
pivot =pivot[['PatientID','PatientName', 'ConsultationCost', 'LabCost', 'PharmacyCost']]
print(pivot.to_string(index=False,header=False))

print("\nCardiology Patients")
Cardiology = final.loc[final['Department']=='Cardiology']
print(Cardiology[['PatientID', 'PatientName', 'TotalBill']].to_string(index=0,header=0))

print("\nSecond and Third Patients")
print(final.iloc[1:3,[0,1,2]].to_string(index=False,header=False))

total_bill = final['TotalBill'].to_numpy()
i_bonus = total_bill * 0.05
final_bill = total_bill + i_bonus

final['InsuranceBonus'] = i_bonus
final['InsuranceBonus'] = round(final['InsuranceBonus'],2)
final['FinalBill'] = final_bill
final['FinalBill'] = round(final['FinalBill'],2)
print("\nInsurance Bonus")
print(final['InsuranceBonus'].to_string(index=False,header=False))

print("\nFinal Bill")
print(final['FinalBill'].to_string(index=False,header=False))

print("\nHighest Revenue Department")
print(department_revenue.idxmax(), department_revenue.max())

print("\nHighest Bill Patient")
highest = final.loc[final['TotalBill'].idxmax()]
bill = highest['TotalBill']
print(f"{highest['PatientID']} {highest['PatientName']} {bill}")
