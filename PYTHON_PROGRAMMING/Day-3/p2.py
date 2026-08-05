"""

Problem Statement:

Given a list of integers, group numbers based on their last digit.

Input Format:
Number of integers
Integers

Output Format:
Dictionary where key = last digit
value = list of numbers having that digit

Sample Input:
6
12
25
32
45
18
28

Sample Output:
{2: [12, 32], 5: [25, 45], 8: [18, 28]}

"""

n = int(input())

result = {}

for i in range(n):
    num = int(input())
    last_digit = num % 10
    if last_digit not in result:
        result[last_digit] = []
    result[last_digit].append(num)

print(result)