user_list = input("Въведете цели числа: ")
my_list = list(map(int, user_list.split()))

num_even_nums = 0
sum_of_even_nums = 0

for num in my_list:
    if num % 2 == 0:
        num_even_nums += 1
        sum_of_even_nums += num

average_of_even_nums = sum_of_even_nums / num_even_nums
print(f"Средното аритметично на числата е: {average_of_even_nums}")

