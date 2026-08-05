"""
A software company processes the monthly payroll of its employees.

Each employee record contains:

Employee ID
Employee Name
Department
Basic Salary
Bonus

The bonus may or may not be available for every employee.

The payroll system should calculate the Net Salary using the following formula:

Net Salary = Basic Salary + Bonus

If the bonus is not available, it should be treated as 0.

Store all employee records using a dictionary where: Employee ID → (Employee Name, Department, Basic Salary, Bonus)

After processing all employees, display the employee payroll sorted in descending order of Net Salary.

The payroll calculation function should use Python Type Hints.

The bonus parameter should use Optional.

The salary values should use Union[int, float].

Requirements:
---------------
Store employee records using a dictionary.
Create a payroll calculation function using Type Hints.
Use Optional for Bonus.
Use Union[int, float] for salary values.
Sort employees using a lambda expression.
Display Net Salary for every employee.

Input Format
-------------
The first line contains the number of employees N.
The next N sets contain:
Employee ID
Employee Name
Department
Basic Salary
Bonus

If bonus is not available, the input will be:None

Output Format:
---------------
Employee Payroll:

E101 -> Ravi -> Development -> 65000
E103 -> Rahul -> Testing -> 56000
E102 -> Priya -> HR -> 50000


sample input:
3
E101
Ravi
Development
60000
5000
E102
Priya
HR
50000
None
E103
Rahul
Testing
55000
1000

Sample Output:
Employee Payroll:
E101 -> Ravi -> Development -> 65000
E103 -> Rahul -> Testing -> 56000
E102 -> Priya -> HR -> 50000

Test Cases
-----------
case=1
input=3
E101
Ravi
Development
60000
5000
E102
Priya
HR
50000
None
E103
Rahul
Testing
55000
1000
output=
Employee Payroll:
E101 -> Ravi -> Development -> 65000
E103 -> Rahul -> Testing -> 56000
E102 -> Priya -> HR -> 50000

case=2
input=2
E201
Anu
Testing
40000
None
E202
Kiran
Development
45000
5000
output=
Employee Payroll:
E202 -> Kiran -> Development -> 50000
E201 -> Anu -> Testing -> 40000

case=3
input=1
E301
Ajay
HR
35000
2500
output=
Employee Payroll:
E301 -> Ajay -> HR -> 37500


case=4
input=1
E401
Ramesh
Testing
-5000
1000
output=
Invalid Basic Salary


case=5
input=1
E501
Pooja
Development
45000
-500
output=
Invalid Bonus

case=6
input=0
output=
Invalid Number of Employees
"""
from typing import Optional, Union

class SalaryException(Exception):
    pass

class BonusException(Exception):
    pass

def calculate_net(salary: Union[int,float],bonus: Optional[Union[int,float]] = None) -> Union[int,float]:
    if bonus is None:
        bonus=0
    return salary+bonus
    
n = int(input())
if n <= 0:
    print("Invalid Number of Employees")
    
else:
    emp_rec = {}
    try:
        for _ in range(n):
            emp_id = input()
            name = input()
            dept = input()
            
            salary = float(input())
            if salary < 0:
                raise SalaryException("Invalid Basic Salary")
            
            bonus_input = input()
            if bonus_input == "None":
                bonus = None
            else:
                bonus = float(bonus_input)
                if bonus < 0:
                    raise BonusException("Invalid Bonus")
            
            emp_rec[emp_id]=(name,dept,salary,bonus)
            
        sorted_emp_rec = sorted(
            emp_rec.items(),
            key=lambda x: calculate_net(x[1][2], x[1][3]),
            reverse = True
            )
                
        print("Employee Payroll:")
        for emp_id,(name,dept,salary,bonus) in sorted_emp_rec:
            net_salary = calculate_net(salary,bonus)
            if net_salary == int(net_salary):
                net_salary = int(net_salary)
            print(f"{emp_id} -> {name} -> {dept} -> {net_salary}")
    except SalaryException as e:
        print(e)
    except BonusException as e:
        print(e)
            
        



