"""

Problem Statement:

Given N words, identify all unique words and display
them in descending order of their length.

Input Format:
First line contains N.
Next N lines contain words.

Output Format:
Sorted list of unique words.

Sample Input:
6
python
java
python
database
sql
machine

Sample Output:
['database', 'machine', 'python', 'java', 'sql']

"""
n = int(input())

words = []

for _ in range(n):
    words.append(input())

words = list(set(words))
words.sort(key=lambda x: (-len(x)))

print(words)