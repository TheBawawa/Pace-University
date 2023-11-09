my_list = [1, 2, 3, 4, 5]
rotation_count = 2

def rotate_list(my_list, rotation_count):
  counter = 0

  while counter < rotation_count:
    temp = my_list.pop()
    my_list.insert(0, temp)
    counter += 1
    
  print(my_list)


rotate_list(my_list, rotation_count)