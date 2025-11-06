def calculate_price (weigh, distance, is_express, discount_code):
    price = 5.00 + 1.20 * weigh + 0.05 * distance

    if is_express == "yes":
        addcount = 30/100
        price = price + (addcount * price)
    else:
        price = price = 5.00 + 1.20 * weigh + 0.05 * distance

    if discount_code == "LESS10":
        if price > 0:
            price = price - 10.00
            if price <= 0:
                price = 0.00
    elif discount_code == "FREESHIP":
        price = 0.00
    else:
        price = price

    return f"{price:.2f}"

weight = float(input())
distance = float(input())
is_express = input()
discount_code = input()

print(calculate_price(weight, distance, is_express, discount_code))