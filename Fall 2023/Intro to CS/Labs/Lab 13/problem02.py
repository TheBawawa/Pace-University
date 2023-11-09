
#You have a list of average daily temperatures (in degrees Celsius) recorded for a week. Write the definition to the
#get_high_temperatures function that takes this list as input and returns the total number of days where the
#temperature exceeded 30 degrees Celsius

def get_high_temp_frequency(temperatures):
  days = 0
  for i in temperatures:
    if i >= 30:
      days += 1

  return days

def main():
  temperatures = [14, 90.5, -5.0, 29.6, 74.0]
  high_temp_days = get_high_temp_frequency(temperatures)
  print(high_temp_days) 

main()