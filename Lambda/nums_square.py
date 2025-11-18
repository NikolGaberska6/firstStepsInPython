user_input = input("Въведете числа, който да включите в листа: ")
list_of_numbers = list(map(int, user_input.split()))

result = list(map(lambda x: x * 3, list_of_numbers)) #използваме map когато искаме да променим всеки един елемент
print(result)