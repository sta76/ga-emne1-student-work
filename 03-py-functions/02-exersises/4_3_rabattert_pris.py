def calculate_discounted_price(price,discount_percent):
    return price - (price * (discount_percent/100))

print(calculate_discounted_price(9455, 35))