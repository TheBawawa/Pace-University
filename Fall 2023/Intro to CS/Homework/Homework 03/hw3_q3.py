"""
Author: Ana Paredes
Assignment / Part: HW3 - Q3
Date due: 10/20/23, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
Pace University Policies and Procedures on Academic
Misconduct.
"""

players = int(input("How many players played this round? "))

while players <= 0:
    print("Invalid input.", end=" ")
    players = int(input("How many players played this round? "))

current_winner = 0
winner_total = 0
total = 0

for player in range(1, players + 1):
    total = 0
    property_asset = input("Enter the value of a property/asset, or DONE to finish: ")

    while property_asset != "DONE" and property_asset != "done":
        total += int(property_asset)
        property_asset = input(
            "Enter the value of a property/asset, or DONE to finish: "
        )

    if property_asset == "DONE" or property_asset == "done":
        if player == 1:
            current_winner = player
            winner_total = total
        elif total > winner_total:
            current_winner = player
            winner_total = total
        print(f"Player {player} has {total} dollars.")

print(
    f"Congratulations, player {current_winner}! You won with ${round(winner_total, 2)}!"
)
