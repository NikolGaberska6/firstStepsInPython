meters_for_explatation = float(input())
price_for_all_meters = meters_for_explatation * 7.61
discount = price_for_all_meters * 0.18
price_with_discount = price_for_all_meters - discount

print(f"The final price is: {price_with_discount} lv." f"The discount is: {discount} lv.")