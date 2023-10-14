"""
Author: Ana Paredes
Assignment / Part: HW3 - Q4
Date due: 10/20/23, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
Pace University Policies and Procedures on Academic
Misconduct.
"""

number = int(input("Please input a positive integer: "))

for i in range(1, number):
    odds = 0
    evens = 0
    for digit in str(i):
        if int(digit) % 2 == 0:
            evens += 1
        elif int(digit) % 2 != 0:
            odds += 1
    if evens > odds:
        print(i, end=" ")
