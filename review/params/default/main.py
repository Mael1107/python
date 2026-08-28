def discount_calculate(price, discount_percentual = 10):
    discount = 1 - (discount_percentual / 100)
    final_value = price * discount

    return final_value

print(discount_calculate(100, 20))