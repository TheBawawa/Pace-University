import random

reply = ""

while reply != "DONE" and reply != "done":
    nums = int(input("How many random numbers would you like to generate? "))
    sum = 0
    product = 1
    even_sum = 0
    odd_sum = 0

    for i in range(nums):
        random_num = random.randint(1, 101)
        sum += random_num
        product *= random_num

        if random_num % 2 == 0:
            even_sum += random_num
        else:
            odd_sum += random_num

        print(f"{random_num} was generated!")

    print(
        f"The sum is {sum}, the product is {product}, the sum os evens is {even_sum}, and the sum of odds is {odd_sum}"
    )

    reply = input("Would you like to do this again? (ENTER for yes, 'DONE' for no) ")
