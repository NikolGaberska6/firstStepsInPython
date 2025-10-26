lily_age = int(input())
price_of_washing_machine = float(input())
unit_price_for_toys = int(input())
money_over_the_years = 0
num_toys = 0
num_even_years = 0

for years in range(1, lily_age+1):
    if years % 2 == 0:
        num_even_years += 1
        added_money = years * 5
        money_over_the_years += added_money
    else:
        num_toys += 1

took_money_from_Lily = num_even_years * 1
lily_full_price_from_year = money_over_the_years - took_money_from_Lily

price_from_toys = num_toys * unit_price_for_toys
lily_full_price_with_toys = lily_full_price_from_year + price_from_toys

if lily_full_price_with_toys >= price_of_washing_machine:
    diff = lily_full_price_with_toys - price_of_washing_machine
    print(f"Yes! {diff:.2f}")
else:
    diff = price_of_washing_machine - lily_full_price_with_toys
    print(f"No! {diff:.2f}")


