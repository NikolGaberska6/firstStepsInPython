import math

num_chicken_menu = int(input())
num_fish_menu = int(input())
num_vegan_menu = int(input())

chicken_menu_price = num_chicken_menu * 10.35
fish_menu_price = num_fish_menu * 12.40
vegan_menu_price = num_vegan_menu * 8.15
all_menu_price = chicken_menu_price + fish_menu_price + vegan_menu_price
dessert_price = 20/100 * all_menu_price
full_price = all_menu_price + dessert_price + 2.50
print(round(full_price, 2))
