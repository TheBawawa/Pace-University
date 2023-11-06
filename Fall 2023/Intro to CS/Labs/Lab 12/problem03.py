def numberify(word):
  word_upper = word.upper()
  for i in word_upper:
    if i == "A":
      print(4, end = "")
    elif i == "E":
      print(3, end = "")
    elif i == "I":
      print(1, end = "")
    elif i == "S":
      print(5, end = "")
    elif i == "T":
      print(7, end = "")
    elif i == "O":
      print(0, end = "")
    else:
      print(i, end ="")

def main():
  message = input("Please enter a message to numberify: ")
  print("Your numberified string is: ", end="")
  numberify(message)

main()