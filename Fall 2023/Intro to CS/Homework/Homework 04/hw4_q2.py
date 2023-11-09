"""
Author: Ana Paredes
Assignment / Part: HW4 - Q2
Date due: 11/9/23, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
Pace University Policies and Procedures on Academic
Misconduct.
"""

def complementary(dna1, dna2):
  mixed_dna = ""
  for i in range(len(dna1)):
    mixed_dna += dna1[i]
    mixed_dna += dna2[i]
  return mixed_dna

def transformed(mix):
  new_mix = ""
  for i in mix:
    if i == "A":
      new_mix += "T"
    elif i == "C":
      new_mix += "G"
    elif i == "T":
      new_mix += "A"
    elif i == "G":
      new_mix += "C"
  print(f"Fused sequence: {new_mix}")


def main():
  dna1 = str(input("Enter a DNA sequence: "))
  dna2 = str(input("Enter a second DNA sequence: "))
  mixed = complementary(dna1, dna2)
  transformed(mixed)

main()