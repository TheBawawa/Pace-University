# any(char in "!@#*" for char in pw) 
# any(char.isupper() for char in pw)

def is_strong_pw(pw):
  checks = 0

  if len(pw) >= 8:
    checks +=1
    #print("len")

  if '!' in pw or '@' in pw or '#' in pw or '*' in pw:
    checks +=1
    #print("wah")
  
  a = False
  for i in pw:
    if i in "ABCDEFGHJKLMNOPQRSTUVWXYZ":
      a = True
    if a == True:
      checks += 1
      #print("caps")


  b = False
  for y in pw:
    if y in "abcdefghjklmnopqrstuvwxyz":
      b = True
    if b == True:
      checks += 1
      #print("notcaps")

  c = False
  for z in pw:
    if z in "0123456789":
      c = True
    if c == True:
      checks += 1
      #print("nums")
  
  if checks >= 5:
    print("Password accepted")
  else:
    print("Password denied")

def main():
  val = input("Enter password: ")
  is_strong_pw(val)

main()

