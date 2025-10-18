from math import ceil

product = input()
city = input()
quantity = float(input())

if city == "Sofia":
    if product == "coffee":
        coffee_price = 0.50 * quantity
        print(round(coffee_price, 1))
    elif product == "water":
        water_price = 0.80 * quantity
        print(round(water_price, 1))
    elif product == "beer":
        beer_price = 1.20 * quantity
        print(round(beer_price, 1))
    elif product == "sweets":
        sweets_price = 1.45 * quantity
        print(round(sweets_price, 4))
    elif product == "peanuts":
        peanuts_price = 1.60 * quantity
        print(round(peanuts_price, 1))
elif city == "Plovdiv":
    if product == "coffee":
        coffee_price = 0.40 * quantity
        print(round(coffee_price, 1))
    elif product == "water":
        water_price = 0.70 * quantity
        print(round(water_price, 1))
    elif product == "beer":
        beer_price = 1.15 * quantity
        print(round(beer_price, 1))
    elif product == "sweets":
        sweets_price = 1.30 * quantity
        print(round(sweets_price, 1))
    elif product == "peanuts":
        peanuts_price = 1.50 * quantity
        print(round(peanuts_price, 1))
elif city == "Varna":
    if product == "coffee":
        coffee_price = 0.45 * quantity
        print(round(coffee_price, 1))
    elif product == "water":
        water_price = 0.70 * quantity
        print(round(water_price, 1))
    elif product == "beer":
        beer_price = 1.10 * quantity
        print(round(beer_price, 1))
    elif product == "sweets":
        sweets_price = 1.35 * quantity
        print(round(sweets_price, 4))
    elif product == "peanuts":
        peanuts_price = 1.55 * quantity
        print(round(peanuts_price, 1))
