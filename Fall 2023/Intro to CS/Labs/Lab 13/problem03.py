
#You have a list of scores obtained by students in a class. Write a function that takes this list as input and returns
#the average score for the students who scored above 80

def get_average_above_80(scores):
  total = 0
  count = 0

  for score in scores:
    if score >= 80:
      total += score
      count += 1

  return round(total/count, 2)


def main():
  scores = [50, 90.5, 100.0, 75.6, 80.0]
  average_above_80 = get_average_above_80(scores)
  print(average_above_80)

main()