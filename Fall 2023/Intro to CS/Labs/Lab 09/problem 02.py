# Problem 2

reply = input("Hit ENTER to calculate a product or 'Q' to quit: ")

while reply != "Q" and reply != "q":
  num_1 = float(input("Please enter your first factor: "))
  num_2 = float(input("Please enter your second factor: "))

  if num_1 > 0 and num_2 > 0:
    answer = num_1 * num_2
    print(f"Your product is: {answer}")
  else:
    print("Error: Positive integers must be entered")
  reply = input("Hit ENTER to calculate a product or 'Q' to quit: ")