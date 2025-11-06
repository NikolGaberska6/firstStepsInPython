money_needed = float(input())
money_available = float(input())

days = 0
num_followed_days = 0

is_true = True

while is_true:
    type_action = input()
    money = float(input())
    days += 1
    if type_action == "spend":
        num_followed_days += 1
        money_available -= money
    if money_available < 0:
            money_available = 0
    elif type_action == "save":
        money_available += money
    if money_available >= money_needed:
        print(f"You saved the money for {days} days.")
        is_true = False
    if num_followed_days == 5:
        print("You can't save the money.")
        print(f"{days}")
        is_true = False