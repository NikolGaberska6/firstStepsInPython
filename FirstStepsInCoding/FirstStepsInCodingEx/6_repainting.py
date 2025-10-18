naylon_price = 1.50
paint_price = 14.50
paint_thinner_price = 5.00
bag_price = 0.40

needed_nylon = int(input())
needed_paint = int(input())
needed_thinner = int(input())
hours_work = int(input())

added_paint = (10/100 * needed_paint) * paint_price
added_nylon = 2 * naylon_price

full_price_for_nylon = (needed_nylon * naylon_price) + added_nylon
full_price_for_paint = (needed_paint * paint_price) + added_paint
full_price_for_thinner = needed_thinner * paint_thinner_price

full_sum_withot_masters = full_price_for_nylon + full_price_for_thinner + full_price_for_paint + bag_price

sum_for_masters = 30/100 * full_sum_withot_masters
all_sum_for_masters = hours_work * sum_for_masters

full_sum = full_sum_withot_masters + all_sum_for_masters

print(full_sum)