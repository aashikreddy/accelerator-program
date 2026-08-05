"""
Problem Statement:

Given N words, convert all words to lowercase and determine
how many times each word appears.

Display the words sorted according to:
1. Frequency (descending)
2. Alphabetical order (ascending) when frequencies are equal.

Input Format:
First line contains an integer N.
Next N lines contain words.

Output Format:
Display a list of tuples containing:
(word, frequency)

Sample Input:
7
Apple
banana
apple
Orange
banana
APPLE
orange

Sample Output:
[('apple', 3), ('banana', 2), ('orange', 2)]
"""
n = int(input())

freq = {}

for _ in range(n):
    word = input().lower()

    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

result = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

print(result)