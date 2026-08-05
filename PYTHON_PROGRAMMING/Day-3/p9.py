"""

Problem Statement:

A DNA sequence contains characters A, T, G and C.

Create a class that stores the sequence using a constructor and
displays:

1. Length of sequence
2. Count of A
3. Count of G

Input Format:
DNA Sequence

Output Format:
Length
Count of A
Count of G

Sample Input:
ATGCGATAA

Sample Output:
9
4
2
"""
class DNA:
    def __init__(self, sequence):
        self.sequence = sequence

    def display(self):
        print(len(self.sequence))
        print(self.sequence.count("A"))
        print(self.sequence.count("G"))

sequence = input()

dna = DNA(sequence)
dna.display()