"""
Author: Ana Paredes
Assignment / Part: HW2 - Q1 (etc.)
Date due: Oct 6, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
Pace University Policies and Procedures on
Academic Misconduct.
"""

day = input("Enter the day the call started at: ")
duration = float(input("Enter the duration of the call (in minutes): "))

cost = 0

if day == "Fri" or day == "Sat" or day == "Sun":
    cost = duration * 0.10
else:
    time = float(input("Enter the time the call started at (hhmm): "))
    if time >= 530 and time <= 2100:
        cost = duration * 0.55
    else:
        cost = duration * 0.35

print(f"This call will cost {round(cost,1)}")
