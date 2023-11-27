# Question 18

prices = [100.0, 20.0, 50.0]
discount = 0.20  # 20% discount


def calculate_total(list_of_prices, discount_percentage):
    new_prices = []

    for i in list_of_prices:
        discount = i * discount_percentage
        new_price = i - discount
        new_prices.append(float(new_price))

    return new_prices


discounted_prices = calculate_total(prices, discount)
#print(discounted_prices)