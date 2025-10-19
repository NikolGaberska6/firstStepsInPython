budget = float(input())
season = input()
destination = ""
wasted_money = 0
specific_destination = ""

if budget <=100:
    destination = "Bulgaria"
    if season == "summer":
        specific_destination = "Camp"
        wasted_money = 30/100 * budget
    elif season == "winter":
        specific_destination = "Hotel"
        wasted_money = 70/100 * budget
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        specific_destination = "Camp"
        wasted_money = 40 / 100 * budget
    elif season == "winter":
        specific_destination = "Hotel"
        wasted_money = 80 / 100 * budget
elif budget > 1000:
    destination = "Europe"
    specific_destination = "Hotel"
    wasted_money = 90/100 * budget

print(f"Somewhere in {destination}")
print(f"{specific_destination} - {wasted_money:.2f}")