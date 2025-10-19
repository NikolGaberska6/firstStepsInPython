days_of_staying = int(input())
nights = days_of_staying - 1
type_of_room = input()
feedback = input()
discount = 0
added_discount = 0
sum_for_staying = 0

if type_of_room == "room for one person":
    sum_for_staying = nights * 18.00

elif type_of_room == "apartment":
    sum_for_staying = nights * 25.00
    if days_of_staying < 10:
     discount = 30/100 * sum_for_staying
     sum_for_staying = sum_for_staying - discount
    elif 10 < days_of_staying < 15:
        discount = 35/100 * sum_for_staying
        sum_for_staying = sum_for_staying - discount
    elif days_of_staying > 15:
        discount = 50/100 * sum_for_staying
        sum_for_staying = sum_for_staying - discount

elif type_of_room == "president apartment":
    sum_for_staying = nights * 35.00
    if days_of_staying < 10:
        discount = 10 / 100 * sum_for_staying
        sum_for_staying = sum_for_staying - discount
    elif 10 < days_of_staying < 15:
        discount = 15 / 100 * sum_for_staying
        sum_for_staying = sum_for_staying - discount
    elif days_of_staying > 15:
        discount = 20 / 100 * sum_for_staying
        sum_for_staying = sum_for_staying - discount

if feedback == "positive":
    added_discount = 25/100 * sum_for_staying
    sum_for_staying = sum_for_staying + added_discount
else:
    added_discount = 10/100 * sum_for_staying
    sum_for_staying = sum_for_staying - added_discount

print(f"{sum_for_staying:.2f}")