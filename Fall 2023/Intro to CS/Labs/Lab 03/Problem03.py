number_of_students = int(input("How many students do you have? "))
larger_classroom_limit = int(input("How many students can fit in the larger classroom? "))
smaller_classroom_limit = int(input("How many students can fit in the smaller classroom? "))

large_classroom = number_of_students // larger_classroom_limit
small_classroom = (number_of_students % larger_classroom_limit) // smaller_classroom_limit
leftovers = smaller_classroom_limit % (number_of_students%larger_classroom_limit)


print("We can form " + str(large_classroom) + " large classroom(s), " + str(small_classroom) + " small classroom(s), with " + str(leftovers) + " leftover student(s).")