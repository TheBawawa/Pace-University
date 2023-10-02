# Solution

print("Write the height and width of the rectangle")
height = float(input("Height: "))
width = float(input("Width: "))

if height > 0 and width > 0:
  area = height * width
  print(f"Area: {area}")
else:
  print("No")


