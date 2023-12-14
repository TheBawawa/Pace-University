"""
Author: Ana Paredes
Assignment / Part: HW6 - Q2
Date due: 12/07/23, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
Pace University Policies and Procedures on Academic
Misconduct.
"""

def create_entry(number, name, type_1, type_2, health_points, attack, defense, special_attack, special_defense, speed, generation, is_legendary):
   random_pokemon = {
      'Number' : number,
      'Name' : name,
      'Types' : {type_1, type_2},
      'Battle stats' : {'HP': health_points, 'Attack': attack, 'Defense': defense, 'Sp, Attack': special_attack, 'Sp. Defense': special_defense, 'Speed': speed},
      'Generation' : generation,
      'Legendary' : False
   }  

   return random_pokemon


def main():
  a_random_pokemon = create_entry(81, "Magnemite", "Electric", "Steel",
                                  25, 35, 70, 95, 55, 45, 1, False)
  for key in a_random_pokemon.keys():
      print("{}: {}".format(key, a_random_pokemon[key]))


main()