"""
Author: Ana Paredes
Assignment / Part: HW3 - Q2
Date due: 10/20/23, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
Pace University Policies and Procedures on Academic
Misconduct.
"""

mochiko = int(input("Enter the amount (g) of mochiko: "))
sugar = int(input("Enter the amount (g) of sugar: "))
cornstarch = int(input("Enter the amount (g) of cornstarch: "))
anko = int(input("Enter the amount (g) of anko: "))

cups_of_mochiko = round(mochiko / 220, 1)
cups_of_sugar = round(sugar / 220, 1)
cups_of_cornstarch = round(cornstarch / 220, 1)
cups_of_anko = round(anko / 220, 1)

batch = 0
while (
    cups_of_mochiko >= 3
    and cups_of_sugar >= 1.5
    and cups_of_cornstarch >= 2
    and cups_of_anko >= 1
):
    batch += 1
    cups_of_mochiko -= 3
    cups_of_sugar -= 1.5
    cups_of_cornstarch -= 2
    cups_of_anko -= 1
else:
    print(
        f"With this amount of ingredients, you can make {batch} batch(es) of 24 mochi."
    )
