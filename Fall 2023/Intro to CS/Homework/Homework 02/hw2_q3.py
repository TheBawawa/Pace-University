"""
Author: Ana Paredes
Assignment / Part: HW2 - Q1 (etc.)
Date due: Oct 6, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
Pace University Policies and Procedures on
Academic Misconduct.
"""

user_xp = float(input("Enter this user's current xp: "))
user_lvl = 0

if 0 <= user_xp <= 60:
    if user_xp < 15:
        user_lvl = 1
    elif 15 <= user_xp < 25:
        user_lvl = 2
    elif 25 <= user_xp < 30:
        user_lvl = 3
    elif 30 <= user_xp < 40:
        user_lvl = 4
    elif 40 <= user_xp <= 60:
        user_lvl = 5

if user_lvl > 0:
    print(f"Level {user_lvl} Player (XP: {user_xp})")
else:
    print("ERROR: Please enter a valid XP value.")
