# Question 19

food_items = ["apple:52", "banana:96", "yogurt:159"]


def calculate_calories_total(food_items):
    sum_calories = 0

    for item in food_items:
        list_food_items = item.split(":")
        sum_calories += int(list_food_items[1])

    return sum_calories


total_calories = calculate_calories_total(food_items)
print(total_calories)
