film_budged = float(input())
num_statists = int(input())
price_for_dress_up_for_one_statist = float(input())

price_for_all_dress_up = num_statists * price_for_dress_up_for_one_statist
new_dress_up_price = 0

film_decor = 10/100 * film_budged
if num_statists > 150:
    discount_for_drees_up = 10/100 * price_for_all_dress_up
    new_dress_up_price = price_for_all_dress_up - discount_for_drees_up
else:
    new_dress_up_price = price_for_all_dress_up

full_sum = new_dress_up_price + film_decor

if full_sum > film_budged:
    needed_sum = full_sum - film_budged
    print("Not enough money!")
    print(f"Wingard needs {needed_sum:.2f} leva more.")
else:
    left_sum = film_budged - full_sum
    print("Action!")
    print(f"Wingard starts filming with {left_sum:.2f} leva left.")