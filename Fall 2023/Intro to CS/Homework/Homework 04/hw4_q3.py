"""
Author: Ana Paredes
Assignment / Part: HW4 - Q3
Date due: 11/9/23, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
Pace University Policies and Procedures on Academic
Misconduct.
"""
def trend(string):
  temp_letter = ""
  for i in range(len(string)):
    if temp_letter == "":
      temp_letter += string[i]
    elif ord(string[i]) <= ord(temp_letter):
      temp_letter = string[i]
    else:
      return f"{string} is not decreasing." f" It stopped being lexicographically decreasing at location {i}"
  return f"{string} is decreasing"



def main():
  string = input("Please enter a string of lowercase letters: ")
  print(trend(string))

main()