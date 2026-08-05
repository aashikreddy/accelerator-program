"""

Problem Statement:

Given a string, identify all unique characters and
store the positions at which each character appears.

Input Format:
A string

Output Format:
Dictionary containing character positions.

Sample Input:
banana

Sample Output:
{'b': [0], 'a': [1, 3, 5], 'n': [2, 4]}
"""
s = input()
result = {
    ch: [i for i, c in enumerate(s) if c == ch]
    for ch in dict.fromkeys(s)
}
print(result)