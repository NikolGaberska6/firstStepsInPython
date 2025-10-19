type_flower = input()
num_flowers = int(input())
budget = int(input())
flower_price = 0
discount = 0
added_price = 0

if type_flower == "Roses":
    flower_price = num_flowers * 5
    if num_flowers > 80:
        discount = 10/100 * flower_price
        flower_price = flower_price - discount
elif type_flower == "Dahlias":
    flower_price = num_flowers * 3.80
    if num_flowers > 90:
        discount = 15/100 * flower_price
        flower_price = flower_price - discount
elif type_flower == "Tulips":
    flower_price = num_flowers * 2.80
    if num_flowers > 80:
        discount = 15/100 * flower_price
        flower_price = flower_price - discount
elif type_flower == "Narcissus":
    flower_price = num_flowers * 3
    if num_flowers < 120:
        added_price = 15/100 * flower_price
        flower_price = flower_price + added_price
elif type_flower == "Gladiolus":
    flower_price = num_flowers * 2.50
    if num_flowers < 80:
        added_price = 20/100 * flower_price
        flower_price = flower_price + added_price


if budget >= flower_price:
    left_money = budget - flower_price
    print(f"Hey, you have a great garden with {num_flowers} "
          f"{type_flower} and {left_money:.2f} leva left.")
else:
    needed_money = flower_price - budget
    print(f"Not enough money, you need {needed_money:.2f} leva more.")
