"""
Author: Ana Paredes
Assignment / Part: HW2 - Q1 (etc.)
Date due: Oct 6, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
Pace University Policies and Procedures on
Academic Misconduct.
"""

import math
import random

pokemon_lvl = int(input("What is this Pokémon's level? "))
pokemon_speed = int(input("What is this Pokémon's speed? "))
critical = ""

R = random.randint(0, 256)
T = pokemon_speed / 2

if R < T:
    critical = "y"
else:
    critical = "n"

if critical == "y":
    Multiplier = round((2 * pokemon_lvl + 6) / (pokemon_lvl + 6), 2)
else:
    Multiplier = 1

print(f"The Pokémon's move will be {Multiplier}x stronger")
