def create_pokedex(filepath):
    file_data = open(filepath,'r')
    lines = file_data.readlines()
    data_list = []
    pokedex = {}

    for index_line in range(len(lines)):
      if index_line != 0:
        data_list.append(lines[index_line])

    for item in data_list:
      item_list = item.split(',')

      number = item_list[0]
      name = item_list[1]
      type_1 = item_list[2]
      type_2 = item_list[3]
      total_stats = item_list[4]
      health_points = item_list[5]
      attack = item_list[6]
      defense = item_list[7]
      special_attack = item_list[8]
      special_defense = item_list[9]
      speed = item_list[10]
      generation = item_list[11]
      is_legendary = item_list[12] 
        
      pokedex[str(item_list[1])] = create_entry(number, name, type_1, type_2, total_stats, health_points, attack, defense, special_attack, special_defense, speed, generation, is_legendary)
    
    return pokedex
    

def create_entry(number, name, type_1, type_2, total_stats, health_points, attack, defense, special_attack, special_defense, speed, generation, is_legendary):
   random_pokemon = {
      'Number' : number,
      'Name' : name,
      'Types' : {type_1, type_2},
      'Total Stats' : total_stats,
      'Battle stats' : {'HP': health_points, 'Attack': attack, 'Defense': defense, 'Sp, Attack': special_attack, 'Sp. Defense': special_defense, 'Speed': speed},
      'Generation' : generation,
      'Legendary' : is_legendary
   }  

   return random_pokemon
    
def main():
  filepath = "/Users/junjiequ/Desktop/Pace-University/Fall 2023/Intro to CS/Homework/Homework 06/pokemon.csv" # change this to your filepath
  pokedex = create_pokedex(filepath)
  #print(pokedex)
  pokemon_key = "Glaceon"
  try:
     my_favorite_pokemon = pokedex[pokemon_key]
  except KeyError:
      print(f"ERROR: Pokemon {pokemon_key} does not exist!")
  else:
      print(f"PRINTING {pokemon_key}'S INFORMATION...")
      for key in my_favorite_pokemon.keys():
        print(f"{key}: {my_favorite_pokemon[key]}")
          
main()
