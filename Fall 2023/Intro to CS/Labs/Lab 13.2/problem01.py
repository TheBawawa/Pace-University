list_A = [1, 2, 3, 4, 5]
list_B = [10, 20, 30, 40, 50]
index_to_swap = 2
          
def swap_elements(list_A, list_B, index_to_swap):
  one = list_A[index_to_swap]
  two = list_B[index_to_swap]

  list_A[index_to_swap] = two
  list_B[index_to_swap] = one
  
  print(list_A)
  print(list_B)

swap_elements(list_A, list_B, index_to_swap)