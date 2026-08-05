"""

Problem Statement:

A software company maintains the attendance percentage of all employees for the current month.

The attendance percentages are stored using a NumPy array.

The HR department wants to analyze the attendance records.

The program should perform the following operations:

• Identify employees eligible for attendance reward   (Attendance >= 75%).

• Identify employees not eligible for attendance reward  (Attendance < 75%).

• Increase the attendance percentage of every employee  by 5% using NumPy Vectorization.

• The updated attendance percentage should not exceed  100%.

• Display the updated attendance percentages.

The analysis should use NumPy Boolean Masking,Vectorization, np.where() and np.clip().

Requirements:
-------------
1. Store attendance percentages using a NumPy array.
2. Use Boolean Masking.
3. Use np.where().
4. Use np.clip().
5. Use Vectorization.
6. Display Eligible Employees.
7. Display Ineligible Employees.
8. Display Updated Attendance.

Input Format:
-------------
First line contains the number of employees N.

Next N lines contain attendance percentages.

Output Format:
--------------
Eligible Employees:
Employee 1
Employee 3
...

Ineligible Employees:
Employee 2
...

Updated Attendance:
80.0
74.0
95.0
...

If N <= 0 display

Invalid Number of Employees

If attendance is less than 0 or greater than 100

display

Invalid Attendance

Sample Input:
-------------
5
75
69
90
82
71

Sample Output:
--------------
Eligible Employees:
Employee 1
Employee 3
Employee 4

Ineligible Employees:
Employee 2
Employee 5

Updated Attendance:
80.0
74.0
95.0
87.0
76.0


Test Cases
----------

case=1
input=
5
75
69
90
82
71
output=
Eligible Employees:
Employee 1
Employee 3
Employee 4

Ineligible Employees:
Employee 2
Employee 5

Updated Attendance:
80.0
74.0
95.0
87.0
76.0


case=2
input=
4
65
80
70
95
output=
Eligible Employees:
Employee 2
Employee 4

Ineligible Employees:
Employee 1
Employee 3

Updated Attendance:
70.0
85.0
75.0
100.0


case=3
input=
1
100
output=
Eligible Employees:
Employee 1

Ineligible Employees:

Updated Attendance:
100.0


case=4
input=
0
output=
Invalid Number of Employees

case=5
input=
3
80
120
70
output=
Invalid Attendance
"""
import numpy as np

n = int(input())

if n <= 0:
    print("Invalid Number of Employees")
else:
    elements = []
    invalid = True
    for _ in range(n):
        val = int(input())
        if val < 0 or val > 100:
            invalid = False
        elements.append(val)
    if not invalid:
        print("Invalid Attendance")
        exit()
    else:
        arr = np.array(elements)
        arr_validate = np.where(arr >= 75, True, False)
        eligible_arr = np.where(arr_validate)[0]
        not_eligible_arr = np.where(~arr_validate)[0]
        inc_arr = arr + 5.0
        new_arr = np.clip(inc_arr, 0, 100)

        print("Eligible Employees:")
        for i in eligible_arr:
            print(f"Employee {i+1}")
            
        print("\nIneligible Employees:")
        for i in not_eligible_arr:
            print(f"Employee {i+1}")
            
        print("\nUpdated Attendance:")
        for i in new_arr:
            print(f"{i:.1f}")
            