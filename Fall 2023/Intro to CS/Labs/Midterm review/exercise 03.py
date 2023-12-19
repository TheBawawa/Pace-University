start = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))
step = int(input("Enter the step value: "))

sum = 0

for i in range(start, end + 1, step):
  sum += i

print(f"The sum of the sequence is: {sum}")