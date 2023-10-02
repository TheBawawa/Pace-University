"""
Author: Ana Paredes
Assignment / Part: HW1 - Q1 (etc.)
Date due: 2023-09-21, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
Pace University Policies and Procedures on Academic
Misconduct.
"""
print("Please enter the amount of dollars and cents: ")
dollars = int(input("Dollars: "))
cents = int(input("Cents: "))

cents_in_the_dollars = dollars * 100
total_cents = cents_in_the_dollars + cents

quarters = total_cents // 25
total_cents -= quarters * 25

dimes = total_cents // 10
total_cents -= dimes * 10

nickels = total_cents // 5
total_cents -= nickels * 5

pennies = total_cents

print(str(dollars) + " dollars and " + str(cents) + " cents are: " + str(quarters) + " quarters, " + str(dimes) + " dimes, " + str(nickels) + " nickels and " + str(pennies) + " pennies.")



