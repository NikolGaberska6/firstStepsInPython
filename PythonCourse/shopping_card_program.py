foods = []
prices = []
total = 0

while True:
    food = input("Enter a food you want to buy (q to quit):")
    if food == "q":
        break
    else:
        price = float(input(f"Enter a price of a {food}: $ "))
        foods.append(food)
        prices.append(price)

print("----YOUR CARD---")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print(f"\nYour total price is: ${total} ")