"""
Author: Ana Paredes
Assignment / Part: HW6 - Q1
Date due: 12/07/23, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
Pace University Policies and Procedures on Academic
Misconduct.
"""

from pprint import pprint

def get_nucleotide_frequencies(nucleotides):
  data = {
    "A": 0,
    "C": 0,
    "G": 0,
  }
  temp_junk = {}

  caps_nucleotides = nucleotides.upper()

  for letter in caps_nucleotides:
    if letter == "A":
      data["A"] += 1
    elif letter == "C":
      data["C"] += 1
    elif letter == "G":
      data["G"] += 1
    elif letter in temp_junk:
      temp_junk[letter] += 1
    else:
      temp_junk[letter] = 1

  data["Junk"] = temp_junk

  return data

def main():
  frequencies = get_nucleotide_frequencies("ACTGTCACGRFRTNHYCTCGACCSGTGTCACGT")
  pprint(frequencies)


main()