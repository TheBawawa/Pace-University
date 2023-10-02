"""
Author: Ana Paredes
Assignment / Part: HW1 - Q1 (etc.)
Date due: 2023-09-21, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
Pace University Policies and Procedures on Academic
Misconduct.
""" 

print("Please enter the number of coins: ")
quarters = int(input("Number of quarters: "))
dimes = int(input("Number of dimes: "))
nickels = int(input("Number of nickels: "))
pennies = int(input("Number of pennies: "))

total_cents = (quarters * 25) + (dimes * 10) + (nickels * 5) + pennies
dollars = total_cents // 100
cents = total_cents % 100

print("The total is " + str(dollars) + " dollar(s) and " + str(cents) + " cent(s).")