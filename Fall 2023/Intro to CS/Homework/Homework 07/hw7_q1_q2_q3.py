"""
Author: Ana Paredes
Assignment / Part: HW7
Date due: 12/07/23, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
Pace University Policies and Procedures on Academic
Misconduct.
"""

import random

class Instrument:
  def __init__(self, model, brand, strength):
    self.model = model
    self.brand = brand
    self.strength = float(strength)

  def does_break(self):

    force = round(random.random(), 1) 
    #print(force)

    if force < self.strength/2:
      return True
    else:
      return False

class Musician:
  def __init__(self, stage_name, instruments):
    self.stage_name = stage_name
    self.instruments = instruments
    self.number_of_instruments = len(instruments)

  def pick_instrument(self, instrument_index):
    if self.number_of_instruments == 0:
      return None
    elif instrument_index == None:
      return self.instruments[random.randint(0, self.number_of_instruments - 1)]
    elif instrument_index >= self.number_of_instruments:
      return self.instruments[-1]
    else:
      return self.instruments[instrument_index]


# Creating our Instrument objects
danelectro = Instrument("Stock '59", "Danelectro", 0.25)
fender_vi = Instrument("VI Bass", "Fender", 0.99)
four_double_o_one = Instrument("4001C64 Bass", "Rickenbacker", 0.856)
gear = [danelectro, fender_vi, four_double_o_one]

# Creating our Musician object
sad_musician = Musician("Robert Smith", gear)

# Checking the Musician object's attributes
"""""
print(sad_musician.stage_name)
print(sad_musician.number_of_instruments)
for instrument in sad_musician.instruments:
    print(f"{instrument.brand} {instrument.model}")
"""

instrument = sad_musician.pick_instrument(2)
instrument = sad_musician.pick_instrument(100000000)
instrument = sad_musician.pick_instrument(None)

def get_name_of_battle_winner(musician1, musician2):
  musician1_instrument = musician1.pick_instrument(None)
  print(f"{musician1.stage_name} picked a {musician1_instrument.brand} {musician1_instrument.model}!")
  musician2_instrument = musician2.pick_instrument(None)
  print(f"{musician2.stage_name} picked a {musician2_instrument.brand} {musician2_instrument.model}!")

  if musician1_instrument == None and musician2_instrument == None:
    return "NO CONTEST"
  elif musician1_instrument == None:
   return musician2.stage_name
  elif musician2_instrument == None:
    return musician1.stage_name
  else:
    if musician1_instrument.strength > musician2_instrument.strength:
      musician1_instrument.does_break()
      if True:
        print(f"{musician1.stage_name}'s {musician1_instrument.model} has broke!")
        return musician2.stage_name
      else:
        return musician1.stage_name
    elif musician2_instrument.strength > musician1_instrument.strength:
      musician2_instrument.does_break()
      if True:
        print(f"{musician2.stage_name}'s {musician2_instrument.model} has broke!")
        return musician1.stage_name
      else:
        return musician2.stage_name
    elif musician1_instrument.strength == musician2_instrument.strength:
      print("Both musician's instruments are the same strength. The winner will be decided by the whim of chance.")
      coin = random.randint(0, 2)
      if coin == 0:
        return musician1.stage_name
      else:
        return musician2.stage_name
      
def main():
    danelectro = Instrument("Stock '59", "Danelectro", 0.25)
    fender_vi = Instrument("VI Bass", "Fender", 0.99)
    four_double_o_one = Instrument("4001C64 Bass", "Rickenbacker", 0.856)
    gear = [danelectro, fender_vi, four_double_o_one]
    # Let's say both musicians have access to the same gear
    sad_musician = Musician("Robert Smith", gear)
    less_sad_musician = Musician("Miki Berenyi", gear)
    # Testing the get_name_of_battle_winner method a few times
    number_of_duels = 10
    for duel_number in range(number_of_duels):
        winner_name = get_name_of_battle_winner(sad_musician, less_sad_musician)
        print(f"THE WINNER OF DUEL #{duel_number + 1} IS {winner_name}!",end="\n\n")
   

"""""
def main():
    danelectro = Instrument("Stock '59", "Danelectro", 0.25)
    number_of_tests = 100
    number_of_breaks = 0
    # I'm testing does_break() 100 times and keeping track of how many times it breaks
    for i in range(number_of_tests):
        if danelectro.does_break():
            number_of_breaks += 1
    percentage = (number_of_breaks / number_of_tests) * 100
    print(f"The {danelectro.model} broke {round(percentage)}% of the time in {number_of_tests} tests!")
"""
main()