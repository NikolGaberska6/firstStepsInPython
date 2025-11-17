is_true = True

while is_true:
    for num in range (1, 11):
        if num % 3 == 0:
            pass
        elif num % 5 == 0:
            is_true = False
        else:
            print(num)