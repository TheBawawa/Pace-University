"""
Author: Ana Paredes
Assignment / Part: HW5 - Q1
Date due: 11/16/23, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
Pace University Policies and Procedures on Academic
Misconduct.
"""

def update_frequencies(old, new):
  count_A = 0
  count_C = 0
  count_T = 0
  count_G = 0
  new_list = []

  for letter in new:
    if letter == "A":
      count_A += 1
    elif letter == "C":
      count_C += 1
    elif letter == "T":
      count_T += 1
    elif letter == "G":
      count_G += 1
  
  for element in old:
    if element[0] == "A":
      new_list.append([element[0], element[1] + count_A])
    elif element[0] == "C":
      new_list.append([element[0], element[1] + count_C])
    elif element[0] == "T":
      new_list.append([element[0], element[1] + count_T])
    elif element[0] == "G":
      new_list.append([element[0], element[1] + count_G])

  print(f"Number of nucleotides added: A -> {count_A} | C -> {count_C} | T -> {count_T} | G -> {count_G}")
  return new_list 
     


def main():
  old_frequencies = [("A", 20), ("C", 23), ("T", 125), ("G", 4)]
  new_sequence = "ACCCGTTA"

  new_frequencies = update_frequencies(old_frequencies, new_sequence)

  print(new_frequencies)

main()