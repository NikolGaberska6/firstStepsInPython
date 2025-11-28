import sys

n = int(input("Въведете броя на елементите: "))
is_true = True
count_for_list = 0
my_list = []

if 15 < n < 35:
    while count_for_list < n:
     number = int(input("Въведете числото, което искате да добавите в списъка: "))
     if 30 < number < 300:
        count_for_list += 1
        my_list.append(number)
     else:
        print("Please enter a valid number")
else:
    print("Invalid num of numbers")
print("Твоят лист с числа е: ", end=" ")
print(*my_list)

num_multiples_of_3 = 0
for num in my_list:
    if (num //10 % 10) % 3 == 0:
        num_multiples_of_3 += 1
    else:
        pass
print(f"Броят на елеемнтите от списъка, чиято цифра на десетиците е кратна на"
      f" 3 е: {num_multiples_of_3}")

min_element = sys.maxsize
index = 0
for idx in my_list:
    if idx // 6 == 4:
        if idx < min_element:
            min_element = idx
            index = my_list.index(min_element)
        else:
            pass
    else:
        pass
print(f"Индекса на минималния елемент с остатък 4 при "
      f"целочислено деление на 6 е: {index}")
print("Първият списък с всички корекции е : ", end=" ")
print(*my_list)


second_list = []
for nums in my_list:
    if (10 < nums < 99) and (nums % 2 == 0 or nums % 3 == 0):
        second_list.append(nums)
    else:
        pass

count_odd_indexes = 0
sum_odd_indexes_num = 0
for n in second_list:
    n_index = second_list.index(n)
    if n_index % 2 != 0:
        count_odd_indexes += 1
        sum_odd_indexes_num += n
average = sum_odd_indexes_num / count_odd_indexes
print(f"Средноаритметичното на числата, чиито индекси "
      f"на на нечетна позиция е {average}")

min_even_number = sys.maxsize
for element in second_list:
    if element % 2 == 0:
        if element > min_even_number:
            min_even_number = element
        else:
            pass
    else:
        pass
print(f"Минималното четно число, което трябва да изтрием \
от този списък е: {min_even_number}")
second_list.remove(min_even_number)
print("Новият списък с всички корекции е : ", end=" ")
print(*second_list)