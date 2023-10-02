"""
Author: Ana Paredes
Assignment / Part: HW1 - Q1 (etc.)
Date due: 2023-09-21, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
Pace University Policies and Procedures on Academic
Misconduct.
"""

year = int(input("Please enter a year greater than 2023: "))
current_population = 330109174
seconds_in_a_year = 60*60*24*365
times_year = year - 2023
seconds_in_new_year = times_year * seconds_in_a_year

births_total = seconds_in_new_year // 7
deaths_total = seconds_in_new_year // 15
new_immigrants_total = seconds_in_new_year // 42
new_emigration_total = seconds_in_new_year // 75

more = (births_total + new_immigrants_total) 
less = (deaths_total + new_emigration_total)

new_population = current_population - less
new_population += more

print("The population in the year " + str(year) + " will be " + str(new_population))

