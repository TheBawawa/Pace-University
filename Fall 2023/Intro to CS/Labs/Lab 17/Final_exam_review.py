class Student:
  def __init__(self, name, id, grades_file):
    self.name = name
    self.id = id
    self.grades_file = grades_file
  
  def get_grades_dictionary(self):
    try:
      file = open(self.grades_file, "r")
      grades = {}
    except:
      print("File not found")
      return grades
    else:
      for line in file:
        line = line.strip()
        line = line.split("->")
        grades[line[0]] = int(line[1])

    file.close()
    return grades
  
  def is_passing(self,passing_grade):
    scores = self.get_grades_dictionary()
    total = 0

    for score in scores:
      total += scores[score]
    
    average = total / len(scores)
    #print(average)

    if average >= passing_grade:
      return True
    else:
      return False
  
  
  

me = Student("Sebastián", 402, "/Users/junjiequ/Desktop/Pace-University/Fall 2023/Intro to CS/Labs/Lab 17/grades.csv")

print(me.name)
print(me.id)
print(me.grades_file)

print(me.get_grades_dictionary())

if me.is_passing(70):
    print("You are passing!")
else:
    print("You are not passing.")