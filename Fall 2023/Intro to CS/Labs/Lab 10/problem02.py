#2A
phrase = input("Enter your phrase: ")
print(phrase[::-1])

#2B
other_phrase = input("Enter your phrase: ")
count =  len(other_phrase) - 1
while count >= 0:
  print(other_phrase[count], end="")
  count -= 1

