nums = input("Въведете числа за лист: ")
my_list = list(map(int, nums.split()))

even_nums =  list(filter(lambda x: x % 2 == 0, my_list))
print(even_nums)