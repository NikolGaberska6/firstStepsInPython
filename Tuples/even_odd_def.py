user_input = input("Въведете числа за кортежа: ")
user_tuple = tuple(map(int, user_input.split()))
even_tuple = []

def even_nums ():
    for num in user_tuple:
        if num % 2 == 0:
            even_tuple.append(num)
        else:
            pass
    print(*even_tuple)

even_nums()