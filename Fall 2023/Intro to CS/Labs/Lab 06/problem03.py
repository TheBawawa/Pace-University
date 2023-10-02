# Problem 03

num1 = float(input("Enter your first number: "))
operation = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter your second number: "))

if operation == "+":
  answer = num1 + num2
  print(f"{num1} {operation} {num2} = {answer}")
elif operation == "-":
  answer = num1 - num2
  print(f"{num1} {operation} {num2} = {answer}")
elif operation == "*":
  answer = num1 * num2
  print(f"{num1} {operation} {num2} = {answer}")
elif operation == "/":
  if num2 == 0:
    print(f"{num1} {operation} {num2} is an invalid operation")
  else:
    answer = num1 / num2
    print(f"{num1} {operation} {num2} = {answer}")
else:
  print(f"{num1} {operation} {num2} is an invalid operation")

