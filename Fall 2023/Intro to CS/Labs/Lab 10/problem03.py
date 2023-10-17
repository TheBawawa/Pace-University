message = input("Please enter your message: ")
lower_message = message.lower()
vowels = 0

#vowels = len([char for char in message if char in "aeiouAEIOU"])

for char in message:
  if char in "aeiouAEIOU":
    vowels += 1


print(f"Total vowels: {vowels}")
