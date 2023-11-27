"""
Author: Ana Paredes
Assignment / Part: HW5 - Q2/Q3
Date due: 11/16/23, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
Pace University Policies and Procedures on Academic
Misconduct.
"""

# Q2

def is_haiku(str):
  list_str = str.split("/")
  #print(list_str)

  if len(list_str) != 3:
    return "WARNING, this is not a haiku because it does not have 3 lines"

  line01 = list_str[0].split(",")
  line02 = list_str[1].split(",")
  line03 = list_str[2].split(",")


  print(line01)
  print(line02)
  print(line03)


  print(len(line01))
  print(len(line02))
  print(len(line03))

  if len(line01) != 5:
    return "WARNING, this is not a haiku because the first line does not have 5 syllabi"
  elif len(line02) != 7:
    return "WARNING, this is not a haiku because the second line does not have 7 syllabi"
  elif len(line03) != 5:
    return "WARNING, this is not a haiku because the third line does not have 5 syllabi"
  else:
    return "This is a haiku"

sample_input_string = "clouds ,mur,mur ,dark,ly /it ,is ,a ,blin,ding ,ha, bit /ga,zing ,at ,the ,moon"

print(is_haiku(sample_input_string))