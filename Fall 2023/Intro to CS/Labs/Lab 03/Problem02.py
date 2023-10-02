days = input("How many days do you have? ")
hours = input("How many hours do you have? ")
minutes = input("How many seconds do you have? ")
seconds = input("How many seconds do you have? ")

total_in_seconds = int(days)*86400 + int(hours)*3600 + int(minutes)*60 + int(seconds)

print(days + " days " + hours + " hours " + minutes + " minutes and " + seconds + " seconds results in a total of " + str(total_in_seconds) + " seconds.")