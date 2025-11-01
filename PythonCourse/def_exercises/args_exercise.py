#args type - tuple

def add (a, b):
    return a + b
add(1,2)
print(add(1,2))
#Ако добавим още едно число ще гърми грешка  в кода,
#защото имаме 2 аргумента и 3 числа
#В такъв случай използваме *args

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1, 2, 3, 4, 5)) # сега можем да добавяме колкото си искаме числа без значение от това колко са на брой аргументите


def display_name(*args):
    for arg in args:
        print(arg, end=" ")
display_name("Mr.", "Ivan", "Ivanov", "Yordanov")
