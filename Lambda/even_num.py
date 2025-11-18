num = int(input("Въведете число, което искате да проверите: "))

even_num = (lambda x: x % 2 == 0)(num)
print(even_num) #тук ще върне само true или false

# Ако използваме filter ще остави само четните числа в листа
numbers = [1, 2, 3, 4, 5, 6]
even_nums = list(filter(lambda x: x % 2 == 0, numbers))
print(even_nums)
