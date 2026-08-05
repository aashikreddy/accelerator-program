"""
Problem Statement:

A shopping mall maintains records of vehicles entering its parking area.
Initially, each vehicle is assigned a parking slot number.

For safety and monitoring purposes, the parking management system performs
two inspections every day:

1. Morning Inspection
   - Display the original parking slot allocation of all vehicles.

2. Evening Inspection
   - Reallocate vehicles based on their slot numbers:
     • Slot numbers from 1 to 10  → Basement Parking
     • Slot numbers from 11 to 20 → Ground Floor Parking
     • Slot numbers greater than 20 → First Floor Parking

The parking management system should:

1. Store parking information using a class constructor.
2. Display object information using __repr__().
3. Maintain vehicle-slot mappings using dictionaries.
4. Log report generation using decorators.
5. Perform both inspections automatically using decorators with arguments.
6. Update parking locations during the evening inspection based on slot numbers.

Requirements:
1. Use constructor and __repr__().
2. Use dictionaries.
3. Use if-elif-else conditions.
4. Use decorators.
5. Use decorators with arguments.
6. Preserve function metadata using functools.wraps.

Input Format:
The first line contains an integer N representing the number of vehicles.

The next 2 × N lines contain:
Vehicle Number
Slot Number

Output Format:
Display the parking report for both inspection cycles.

Sample Input:
4
TS09AB1234
12
TS08CD4567
8
TS10EF7890
25
TS07XY4321
18

Sample Output:
Inspection Cycle 1
Generating Parking Report
ParkingReport({'TS09AB1234': 12, 'TS08CD4567': 8, 'TS10EF7890': 25, 'TS07XY4321': 18})

Inspection Cycle 2
Generating Parking Report
ParkingReport({'TS09AB1234': 'Ground Floor Parking', 'TS08CD4567': 'Basement Parking', 'TS10EF7890': 'First Floor Parking', 'TS07XY4321': 'Ground Floor Parking'})
"""

from  functools import wraps
class ParkingReport:
    def __init__(self, parking):
        self.parking = parking
    def __repr__(self):
        return f"ParkingReport({self.parking})"
        
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Generating Parking Report")
        return func(*args, **kwargs)
    return wrapper
    
def inspection(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, times + 1):
                print(f"Inspection Cycle {i}")
                func(i, *args, **kwargs)
                print()
        return wrapper
    return decorator
    
@inspection(2)
@logger
def generate_report(cycle, parking):
    if cycle == 1:
        report = ParkingReport(parking)
    else:
        updated = {}
        for vehicle, slot in parking.items():
            if slot <= 10:
                updated[vehicle] = "Basement Parking"
            elif slot <= 20:
                updated[vehicle] = "Ground Floor Parking"
            else:
                updated[vehicle] = "First Floor Parking"
        report = ParkingReport(updated)
    print(report)
    
n = int(input())
parking = {}
for _ in range(n):
    vehicle = input()
    slot = int(input())
    parking[vehicle] = slot
generate_report(parking)    