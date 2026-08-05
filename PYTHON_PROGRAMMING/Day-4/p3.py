"""


Problem Statement:

A railway department maintains passenger records.

Create a base class Passenger.

Create two derived classes:

1. SleeperClass
   - Fare = Distance × ₹2

2. ACClass
   - Fare = Distance × ₹4

Override the fare calculation method.

If distance is negative, display:

Invalid Distance

Input Format:
Class Type (Sleeper / AC)
Passenger Name
Distance

Output Format:
Display fare amount.

Sample Input:
AC
Priya
100

Sample Output:
Fare = 400
"""

class Passenger:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance
    def calculate_fare(self):
        return 0

class SleeperClass(Passenger):
    def calculate_fare(self):
        return distance*2
        
class ACClass(Passenger):
    def calculate_fare(self):
        return distance*4
ctype = input().lower()
name = input()
distance = int(input())
try:
    if distance < 0:
        raise ValueError
    if ctype == "sleeper":
        passenger = SleeperClass(name, distance)
    elif ctype == "ac":
        passenger = ACClass(name, distance)
    else:
        print("Invalid Class Type")
        exit()
    print("Fare =", passenger.calculate_fare())
except ValueError:
    print("Invalid Distance")