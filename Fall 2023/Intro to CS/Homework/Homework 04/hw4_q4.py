"""
Author: Ana Paredes
Assignment / Part: HW4 - Q4
Date due: 11/9/23, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
Pace University Policies and Procedures on Academic
Misconduct.
"""

def decoder(string, num):
  counter = -1
  newlist = []
  while counter >= len(string)*-1:
    #print(string[counter])
    if string[counter] in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!?@/":
      newlist.append(string[counter])
      finallist = "".join(newlist)
    counter -= int(num) + 1
  
  print(f"Your message is '{finallist}'")

def main():
  encoded = input("Enter an encoded string: ")
  key = input("Enter a key: ")
  decoder(encoded, key)

main()