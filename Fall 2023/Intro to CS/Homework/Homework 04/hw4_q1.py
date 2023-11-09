"""
Author: Ana Paredes
Assignment / Part: HW4 - Q1
Date due: 11/9/23, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
Pace University Policies and Procedures on Academic
Misconduct.
"""

def to_lowercase(string):
  new_string = ""
  touched = 0
  untouched = 0
  for i in string:
    if "A" <= i <= "Z":
      new_string += chr(ord(i)+32)
      touched += 1
    elif "a" <= i <= "z":
      untouched += 1
      new_string += i
    else:
      new_string += i

  print(new_string)
  print(f"Number of changed letters: {touched}")
  print(f"Number of unchanged letters: {untouched}")

def spaces(string):
  num_spaces = 0
  for i in string:
    if i == " ":
      num_spaces += 1
  print(f"Number of whitespace characters: {num_spaces}")

def non_letter(string):
  no_letters = 0
  for i in string:
    if i not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
      no_letters +=1
  print(f"Number of non-alphabetic characters: {no_letters}")

def main():
  string = input("Say something: ")
  to_lowercase(string)
  spaces(string)
  non_letter(string)

main()