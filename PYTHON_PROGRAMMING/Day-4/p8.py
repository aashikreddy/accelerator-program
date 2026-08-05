"""


Problem Statement:

A company wants to automatically generate employee ID cards.

The employee name entered by the HR department may contain
extra spaces and inconsistent letter cases.

The system should:

1. Remove leading and trailing spaces.
2. Convert the name to title case.
3. Generate an email address in lowercase.
4. Replace spaces with underscores while creating the employee ID.
5. Count the total number of characters in the employee name
   (excluding spaces).
6. Display the first name and last name separately.
7. Check whether the employee name contains only alphabets.
8. Display the reversed employee name.

Requirements:
Use string methods appropriately.

Input Format:
Employee Name

Output Format:
Display formatted employee details.

Sample Input:
   ravi kumar

Sample Output:
Formatted Name : Ravi Kumar
Email : ravi.kumar@company.com
Employee ID : Ravi_Kumar
Character Count : 9
First Name : Ravi
Last Name : Kumar
Valid Name : True
Reversed Name : ramuK ivaR


case=1
input=ravi kumar

output=
Formatted Name : Ravi Kumar
Email : ravi.kumar@company.com
Employee ID : Ravi_Kumar
Character Count : 9
First Name : Ravi
Last Name : Kumar
Valid Name : True
Reversed Name : ramuK ivaR

case=2
input=Priya reddy 
output=
Formatted Name : Priya Reddy                                                    
Email : priya.reddy@company.com                                                 
Employee ID : Priya_Reddy                                                       
Character Count : 10                                                            
First Name : Priya                                                              
Last Name : Reddy                                                               
Valid Name : True                                                               
Reversed Name : yddeR ayirP



case=3
input=JOHN SMITH
output=
Formatted Name : John Smith                                                     
Email : john.smith@company.com                                                  
Employee ID : John_Smith                                                        
Character Count : 9                                                             
First Name : John                                                               
Last Name : Smith                                                               
Valid Name : True                                                               
Reversed Name : htimS nhoJ 


case=4
input=kiran123 kumar

output=
Formatted Name : Kiran123 Kumar
Email : kiran123.kumar@company.com
Employee ID : Kiran123_Kumar
Character Count : 13
First Name : Kiran123
Last Name : Kumar
Valid Name : False
Reversed Name : ramuK 321nariK

case=5
input=anitha

output=
Formatted Name : Anitha
Email : anitha@company.com
Employee ID : Anitha
Character Count : 6
First Name : Anitha
Last Name : Anitha
Valid Name : True
Reversed Name : ahtinA


case=6
input=a

output=
Formatted Name : A
Email : a@company.com
Employee ID : A
Character Count : 1
First Name : A
Last Name : A
Valid Name : True
Reversed Name : A

"""
name = input()
name = name.strip()
formatted_name = name.title()
email = formatted_name.lower().replace(" ",".") + "@company.com"
employee_id = formatted_name.replace(" ","_")
character_count = len(formatted_name.replace(" ",""))
parts = formatted_name.split()
first_name = parts[0]
last_name = parts[-1]
valid_name = "".join(parts).isalpha()
reversed_name = formatted_name[::-1]

print("Formatted Name :", formatted_name)
print("Email :", email)
print("Employee ID :", employee_id)
print("Character Count :", character_count)
print("First Name :", first_name)
print("Last Name :", last_name)
print("Valid Name :", valid_name)
print("Reversed Name :", reversed_name)