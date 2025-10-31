menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.50}

card = []
total = 0

print("------------MENU------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("----------------------------")

while True:
    food = input("Select an item (q to quit): ")
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        card.append(food)
    else:
        print("This food is not from the menu")

print("----------------------------")

for food in card:
    price = menu.get(food)
    total += price

print("Food you choose from the menu is: ")
for food in card:
    print(f"{food}", end= " ")

print()
print(f"Total price is: ${total:.2f}")