imported_tuple = input("Въведете числа, които искате да са в кортежа: ")
imported_tuple = tuple(map(int, imported_tuple.split()))
new_list = []

for idx in imported_tuple:
    if idx in new_list:
        pass
    else:
        new_list.append(idx)

new_tuple = tuple(new_list)
print("Новият кортеж без повторенията на числата е: ", end= " ")
print(*new_tuple)
print("Новията кортеж във възходящ ред е: ", end=" ")
sorted_tuple = sorted(new_tuple)
print(*sorted_tuple)
print("Новият кортеж в низходящ ред е: ", end=" ")
descend = tuple(sorted(new_tuple, reverse=True))
print(*descend)
