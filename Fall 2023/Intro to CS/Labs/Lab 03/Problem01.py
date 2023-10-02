
number_of_ice_cream_scoops = float(input("How many scoops?"))
radius_of_cone = float(input("What is the radius?"))
height_of_cone = float(input("What is the cone height?"))
pi = 3.1416

scoop_volume = (4/3) * pi * (radius_of_cone**3)
print(scoop_volume)
cone_volume = pi * (radius_of_cone**2) *  (height_of_cone/3)
print(cone_volume)
total_volume = number_of_ice_cream_scoops*scoop_volume + cone_volume
print(total_volume)

print("Your " + str(number_of_ice_cream_scoops) + " scoop ice cream cone has a total volume of " + str(total_volume))