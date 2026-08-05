"""


Problem Statement:

An online coding platform stores participant names and their
contest scores.

To prepare the final leaderboard, the platform should:

1. Accept multiple participant scores.
2. Remove duplicate scores.
3. Arrange scores in descending order.
4. Calculate the total score of unique entries.
5. Generate a contest report object.
6. Display report information in a readable format.
7. Log when report generation starts and ends.
8. Retry report generation two times.

Requirements:
1. Use lists, sets and lambda functions.
2. Use *args to calculate the total score.
3. Use __repr__() to display object information.
4. Use decorators and decorator with arguments.
5. Preserve metadata using functools.wraps.

Input Format:
Number of Participants

Participant Name
Participant Score

Output Format:
Display contest reports for each retry attempt.

Sample Input:
5
Ravi
90
Priya
85
Kiran
90
John
70
David
95

Sample Output:
Attempt 1
Report Generation Started
ContestReport(scores=[95, 90, 85, 70], total=340)
Report Generation Finished

Attempt 2
Report Generation Started
ContestReport(scores=[95, 90, 85, 70], total=340)
Report Generation Finished
"""

from functools import wraps

# Decorator
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Report Generation Started")
        result = func(*args, **kwargs)
        print("Report Generation Finished")
        return result
    return wrapper

# Decorator with Arguments
def retry(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, times + 1):
                print(f"Attempt {i}")
                func(*args, **kwargs)
                print()
        return wrapper
    return decorator


# Class
class ContestReport:
    def __init__(self, scores, total):
        self.scores = scores
        self.total = total

    def __repr__(self):
        return f"ContestReport(scores={self.scores}, total={self.total})"


# *args
def calculate_total(*args):
    return sum(args)


@retry(2)
@logger
def generate_report(scores):

    # Remove duplicates
    unique_scores = list(set(scores))

    # Sort descending
    unique_scores.sort(key=lambda x: x, reverse=True)

    # Calculate total
    total = calculate_total(*unique_scores)

    report = ContestReport(unique_scores, total)

    print(report)


# Main Program
n = int(input())

scores = []

for _ in range(n):
    name = input()      # Name is not required in the report
    score = int(input())
    scores.append(score)

generate_report(scores)