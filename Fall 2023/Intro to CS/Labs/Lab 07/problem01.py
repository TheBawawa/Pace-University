# Problem 01

print("Welcome to the grocery calculator")
price = float(input("Enter the price of an item (enter 0 to stop): $"))
total = 0

while price != 0:
    total += price
    price = float(input("Enter the price of an item (enter 0 to stop): $"))

print(f"Total cost: {round(total, 2)}")
