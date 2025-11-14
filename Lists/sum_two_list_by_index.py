import random
n = int(input("Въведете дължината на първия списък: ")) #4
m = int(input("Въведете дължинатa нa втория списък: ")) #3

first_list = [random.randint(1, 20) for _ in range(n)] #[1, 2, 4]
print(first_list)
second_list = [random.randint(1, 20) for _ in range(m)] #[1, 2, 4, 5]
print(second_list)

third_list = []

for idx in first_list: #вс елементи в първия лист
     index = first_list.index(idx) #индекса на дадения елемент в първия лист
     element = second_list[index] #елемента на съшия индекс във втория лист
     result = idx + element
     third_list.insert(index, result)

print(third_list)