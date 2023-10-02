integer = int(input("Enter any integer: "))

if integer % 3 == 0 and integer % 5 == 0:
  print("Hello World")
elif integer % 3 == 0:
  print("Hello")
elif integer % 5 == 0:
  print("World")