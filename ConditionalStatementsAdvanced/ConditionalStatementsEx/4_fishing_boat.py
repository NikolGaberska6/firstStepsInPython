budget = int(input())
season = input()
num_fisherman = int(input())
price_for_rent = 0
discount = 0
added_discount = 0

if season == "Spring":
    price_for_rent = 3000
elif season == "Summer" or season == "Autumn":
    price_for_rent = 4200
elif season == "Winter":
    price_for_rent = 2600

if num_fisherman <= 6:
    discount = 10/100 * price_for_rent
    price_for_rent = price_for_rent - discount
elif 7 <= num_fisherman <= 11:
    discount = 15/100 * price_for_rent
    price_for_rent = price_for_rent - discount
else:
    discount = 25/100 * price_for_rent
    price_for_rent = price_for_rent - discount

if num_fisherman %2 == 0 and season != "Autumn":
    added_discount = 5/100 * price_for_rent
    price_for_rent = price_for_rent - added_discount
else:
    price_for_rent = price_for_rent

if budget >= price_for_rent:
    left_money = budget - price_for_rent
    print(f"Yes! You have {left_money:.2f} leva left.")
else:
    needed_money = price_for_rent - budget
    print(f"Not enough money! You need {needed_money:.2f} leva.")