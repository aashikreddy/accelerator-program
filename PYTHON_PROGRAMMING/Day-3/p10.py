"""

Problem Statement:

A research organization stores citation counts of published papers.
Duplicate citation counts may exist.

The system should:

1. Remove duplicate citation counts.
2. Calculate the total citation count.
3. Sort citation counts in descending order.
4. Display report information using a class.

Requirements:
1. Use list operations and sets.
2. Use *args to compute total citations.
3. Use lambda while sorting.
4. Display object information using __repr__().

Input Format:
Number of Papers
Citation Counts

Output Format:
ResearchReport(total=?, citations=?)

Sample Input:
6
20
15
20
10
40
15

Sample Output:
ResearchReport(total=85, citations=[40, 20, 15, 10])
"""
class ResearchReport:
    def __init__(self, total, citations):
        self.total = total
        self.citations = citations

    def __repr__(self):
        return f"ResearchReport(total={self.total}, citations={self.citations})"

def total_citations(*args):
    return sum(args)

n = int(input())

citations = []

for _ in range(n):
    citations.append(int(input()))

citations = list(set(citations))

citations.sort(key=lambda x: x, reverse=True)

total = total_citations(*citations)

report = ResearchReport(total, citations)

print(report)
