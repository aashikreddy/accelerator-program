"""

Problem Statement:

A cyber security company wants to analyze passwords created
by users.

For each password:
1. Determine its length.
2. Count the number of vowels present.
3. Display passwords sorted according to their length.

Requirements:
1. Read multiple passwords.
2. Analyze each password.
3. Display password information in ascending order of length.

Input Format:
First line contains an integer N representing the number of passwords.

Next N lines contain password strings.

Output Format:
Display a list containing:
(Password, Length, Number of Vowels)

Sample Input:
3
Python123
Admin@456
AI2025

Sample Output:
[('AI2025', 6, 2), ('Python123', 9, 1), ('Admin@456', 9, 3)]

"""

n=int(input())
passwords = [input().strip() for _ in range(n)]
def count(s):
    return sum(1 for c in s.lower() if c in 'aeiou')
result = [(p,len(p),count(p)) for p in passwords]
result.sort(key=lambda x:x[1])
print(result)