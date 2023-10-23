#nums = int(input("How many numbers do you want to see? "))

reply = ""

while reply != "q" and reply != "Q":
  nums = int(input("How many numbers do you want to see? "))
  count = 1
  first = 2

  while count <= nums:
    print(first)
    first += 2
    count += 1
  reply = input("Would you like to do this again? (ENTER for yes, q for no.) ")