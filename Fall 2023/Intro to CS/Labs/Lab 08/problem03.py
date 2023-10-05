# Problem 03

base = float(input("Please enter a positive integer to serve as the base: "))
power = float(input("Please enter a positive integer to serve as the highest power: "))

if base != int(base) or power != int(power):
  print("ERROR: Both values must be POSITIVE INTEGERS")
elif int(base) < 0 or int(power) < 0:
  print("ERROR: Both values must be POSITIVE INTEGERS")
else:
  limit = int(power) + 1 
  for x in range(0, limit):
    print(f"{base} ^ {power} = {int(base) ** x}")