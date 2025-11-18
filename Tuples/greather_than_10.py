user_tuple = input("Въведете числата, които искате да се съдържат в кортежа: ")
my_tuple = tuple(map(int, user_tuple.split()))
new_list = []

for num in my_tuple:
    if num > 10:
        new_list.append(num)

new_tuple = tuple(new_list)
print("Новият кортеж само с числата по-голями от 10 е: ", end=" ")

print(*new_tuple)
