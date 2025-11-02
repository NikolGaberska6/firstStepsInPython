name = input()
password = input()

is_reading = True
while is_reading:
    second_password = input()
    if password == second_password:
        is_reading = False
        print(f"Welcome {name}!")
    else:
        continue
