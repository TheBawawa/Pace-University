"""
Author: [Your name here]
Assignment / Part: HW2 - Q1 (etc.)
Date due: Oct 6, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
Pace University Policies and Procedures on
Academic Misconduct.
"""

import math

w = float(input("Enter the frequency value: "))
T = float(input("Enter the duration value of the sound wave: "))

f_w = (2 * math.sin(w * T)) / w

print(f"The amplitude spectrum of this Fourier transform is: {round(f_w, 3)}")
