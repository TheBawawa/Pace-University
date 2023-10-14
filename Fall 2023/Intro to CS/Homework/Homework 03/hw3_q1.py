"""
Author: Ana Paredes
Assignment / Part: HW3 - Q1
Date due: 10/20/23, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
Pace University Policies and Procedures on Academic
Misconduct.
"""

base = float(input("Please enter a positive integer to serve as base: "))

while base != int(base) or base <= 0:
    print(f"Invalid value for the base ({base}).", end="  ")
    base = float(input("Please enter a positive integer to serve as base: "))

power = float(input("Please enter a positive integer to serve as the highest power: "))

while power != int(power) or power <= 0:
    print(f"Invalid value for the power ({power}).", end="  ")
    power = float(
        input("Please enter a positive integer to serve as the highest power: ")
    )

if base == int(base) and power == int(power):
    num = int(power)
    base = int(base)
    while num <= int(power) and num >= 0:
        print(f"{base} ^ {num} = {base**num}")
        num -= 2
