def is_palindrome(string):
  negative = -1
  for i in range(len(string)):
    if string[i] != string[negative]:
      return False
    negative -= 1
    return True
  
print(is_palindrome("racecar"))
print(is_palindrome("hello"))
