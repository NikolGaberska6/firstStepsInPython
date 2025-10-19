degrees = int(input())
type_of_day = input()
outfit = ""
shoes = ""

if 10 <= degrees <= 18:
    if type_of_day == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif type_of_day == "Afternoon":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif type_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif 18 < degrees <= 24:
    if type_of_day == "Morning":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif type_of_day == "Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif type_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif degrees >= 25:
    if type_of_day == "Morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif type_of_day == "Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
    elif type_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {degrees} degrees, get your {outfit} "
      f"and {shoes}.")
