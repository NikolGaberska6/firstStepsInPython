import random
rows_and_columns = int(input("Въведете големината на матрицата: "))

matrix = [[random.randint(1, 9) for _ in range(rows_and_columns)]
          for _ in range(rows_and_columns)]

for num in matrix:
    print(num)

matrix_diagonal_nums = []
matrix_secondary_nums = []
sum_of_diagonal_nums = 1
sum_of_secondary_nums = 1
num_iteration = 0

#с този цикъл търсим сумата на главния диагонал
for pear in matrix:
#   print(pear)
    idx = matrix.index(pear)
#   print(idx)
    num_to_append = pear[idx]
#   print(num_to_append)
    matrix_diagonal_nums.append(num_to_append)

for idx in matrix_diagonal_nums:
    sum_of_diagonal_nums *= idx

print("Числата на главния диагонал са: ", end=" ")
print(*matrix_diagonal_nums)
print(f"Сумата на главния диагонал е: {sum_of_diagonal_nums}")

#С този цикъл търсим сумата на второстепенния диагонал
for pear in matrix: #[6, 8, 5]
    print(pear)
    num_iteration += 1
    num_to_append = pear[len(pear) - num_iteration]
    matrix_secondary_nums.append(num_to_append)

for idx in matrix_secondary_nums:
    sum_of_secondary_nums *= idx

print("Числата на второстепенния диагонал са: ", end=" ")
print(*matrix_secondary_nums)
print(f"Сумата на второстепенния диагонал е: {sum_of_secondary_nums}")