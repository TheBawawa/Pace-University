class Package:
  def __init__(self,tracking_number, carrier, shipment_date, delivery_date, origin_city, destination_city, weight, package_dimensions):
    self.tracking_number = tracking_number
    self.carrier = carrier
    self.shipping_data = {"Shipped": shipment_date, "Delivered": delivery_date}
    self.geodata = {"Origin": origin_city, "Destination": destination_city}
    self.package_info = {"Weight": weight, "Size": package_dimensions}

  def is_oversized(self):
    if self.package_info["Weight"] > 50.0 and self.package_info["Size"] == "Large":
      return True
    else:
      return False
  
def extract_package_data(filepath):
  try:
    file = open(filepath, "r")
  except FileNotFoundError:
    print("File not found.")
    return {}
  else:
    lines = file.readlines()[1:]
    all_packages = {}
    file.close()
    #print(lines)

    for line in lines:
      list_line = line.strip().split(",")
      all_packages[int(list_line[0])] = Package(list_line[0],list_line[1], list_line[2], list_line[3], list_line[4], list_line[5], list_line[6], list_line[7])
  
    return all_packages

data = extract_package_data("/Users/junjiequ/Desktop/Pace-University/Fall 2023/Intro to CS/Labs/Lab 16/shipping data.txt") # Mr. teacher, change this path to your own path :>
#print(data)
first_package = data[4471212485]
print(first_package.carrier)

package = Package(4471212485, "UPS", "12/31/2022", "1/17/2023", "Milwaukee", "Colorado Springs", 25.68, "Medium")
#print(package.tracking_number)
#print(package.carrier)
#print(package.shipping_data)
#print(package.geodata)
#print(package.package_info)

#print("Oversized!" if package.is_oversized() else "Regular")