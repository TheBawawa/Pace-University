import csv

class CreditCard:
  def __init__(self, user_name, company, balance, credit_limit):
    # attributes
    self.user_name = user_name
    self.company = company
    self.balance = balance
    self.credit_limit = credit_limit

  def use(self, amount):
    int_balance = float(self.balance)
    int_credit_limit = float(self.credit_limit)

    if int_balance < int_credit_limit:
      int_balance += amount
    else:
      print("Error, the balance can't go over your credit limit")
  
  def pay(self, amount):
    int_balance = float(self.balance)

    if amount < int_balance:
      new_balance = int_balance - amount
      print(f"Your new balance is {new_balance}")
    else:
      change = amount - int_balance
      print(f"Your change is {change}")

def create_credit_card(file_name):
  file_data = open(file_name, 'r')
  lines = file_data.readlines()
  data_list = []

  for line in lines:
    list_line=line.split(',')
    data_list.append(list_line[1])

  user_name = data_list[0]
  company = data_list[1]
  balance = data_list[2]
  credit_limit = data_list[3]

  return CreditCard(user_name, company, balance, credit_limit)

  

random_card = create_credit_card('/Users/junjiequ/Desktop/Pace-University/Fall 2023/Intro to CS/Labs/Lab 14/data_import.csv')
random_card.use()