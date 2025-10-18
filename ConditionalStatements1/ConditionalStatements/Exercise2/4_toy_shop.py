vacation_price = float(input())
num_puzzles = int(input())
num_dolls = int(input())
num_bears = int(input())
num_minions = int(input())
num_trains = int(input())

puzzle_price = 2.60
doll_price = 3
bear_price = 4.10
minion_price = 8.20
train_price = 2

num_toys = num_puzzles + num_dolls + num_bears + num_minions + num_trains

full_price = (num_puzzles * puzzle_price + num_dolls * doll_price + num_bears * bear_price +
              num_minions * minion_price + num_trains * train_price)

discount = 0

if 50 <= num_toys:
    discount = 25/100 * full_price
    price_with_discount = full_price - discount
else:
    price_with_discount = full_price

rent_price = 10/100 * price_with_discount
all_money = price_with_discount - rent_price

if all_money >= vacation_price:
    left_money = all_money - vacation_price
    print(f"Yes! {left_money:.2f} lv left.")
else:
    left_money = vacation_price - all_money
    print(f"Not enough money! {left_money:.2f} lv needed.")


0