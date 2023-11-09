
#A student is given a list of numbers representing the scores of various students in a math class. Write a function
#that takes this list as input and returns the average score of the students

def get_average_score(scores):
  sum = 0
  counter = 0
  for score in scores:
    sum += score
    counter += 1

  return sum/counter

def main():
  scores = [50, 90.5, 100.0, 75.6, 80.0]
  average_score = get_average_score(scores)
  print(average_score)

main()

