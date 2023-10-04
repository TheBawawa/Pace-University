# Problem 02

day = 1
total = 0

while day < 8:
    steps = int(input(f"Enter the number of steps taken on day {day}: "))
    total += steps
    day += 1

print(f"Total number of steps taken throughout the week: {total}")
