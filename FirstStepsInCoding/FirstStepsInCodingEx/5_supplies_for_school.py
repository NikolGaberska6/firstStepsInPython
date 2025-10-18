num_pens = int(input())
num_markers = int(input())
liters_preparation = int(input())
percent_discount = int(input())

sum_for_pens = num_pens * 5.80
sum_for_markers = num_markers * 7.20
sum_for_preparation = liters_preparation * 1.20

sum_without_discount = sum_for_pens + sum_for_markers + sum_for_preparation
discount = percent_discount/100
sum_with_discount = sum_without_discount - (sum_without_discount * discount)

print(sum_with_discount)