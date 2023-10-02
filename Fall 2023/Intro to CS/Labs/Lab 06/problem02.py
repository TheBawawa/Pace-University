# Problem 02
h_exam_1 = float(input("Enter your highest exam grade: "))
h_exam_2 = float(input("Enter your second highest exam grade: "))
h_exam_3 = float(input("Enter your third highest exam grade: "))
homework = float(input("Enter your average homework grade: "))
lab = float(input("Enter your average lab grade: "))

new_exam_1 = h_exam_1 * 0.25
new_exam_2 = h_exam_2 * 0.20
new_exam_3 = h_exam_3 * 0.15
new_homework = homework * 0.20
new_lab = lab * 0.20

total_average = new_exam_1 + new_exam_2 + new_exam_3 + new_homework + new_lab

if total_average > 92:
  print("Your final grade is A")
elif total_average >= 90:
  print("Your final grade is A-")
elif total_average >= 87:
  print("Your final grade is B+")
elif total_average >= 83:
  print("Your final grade is B")
elif total_average >= 80:
  print("Your final grade is B-")
elif total_average >= 77:
  print("Your final grade is C+")
elif total_average >= 73:
  print("Your final grade is C")
elif total_average >= 70:
  print("Your final grade is C-")
elif total_average >= 67:
  print("Your final grade is D+")
elif total_average >= 60:
  print("Your final grade is D")
elif total_average < 60:
  print("Your final grade is F")