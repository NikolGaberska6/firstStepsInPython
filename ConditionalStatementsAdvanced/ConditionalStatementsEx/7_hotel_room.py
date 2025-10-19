month = input()
num_nights = int(input())
studio_price = 0
apartment_price = 0
discount_for_studio = 0
discount_for_apartment = 0

if month == "May" or month == "October":
    studio_price = 50 * num_nights
    apartment_price = 65 * num_nights
    if 7 < num_nights < 14:
        discount_for_studio = 5/100 * studio_price
        studio_price = studio_price - discount_for_studio
    elif num_nights > 14:
        discount_for_studio = 30/100 * studio_price
        studio_price = studio_price - discount_for_studio
        discount_for_apartment = 10/100 * apartment_price
        apartment_price = apartment_price - discount_for_apartment

elif month == "June" or month == "September":
    studio_price = 75.20 * num_nights
    apartment_price = 68.70 * num_nights
    if num_nights > 14:
        discount = 20/100 * studio_price
        studio_price = studio_price - discount
        discount_for_apartment = 10 / 100 * apartment_price
        apartment_price = apartment_price - discount_for_apartment
elif month == "July" or month == "August":
    studio_price = 76 * num_nights
    apartment_price = 77 * num_nights
    discount_for_apartment = 10 / 100 * apartment_price
    apartment_price = apartment_price - discount_for_apartment


print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")