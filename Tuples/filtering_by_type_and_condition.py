data = (1, 2.5, "hi", 9, True, 3.14, 8, "python")

new_tuple = []
for idx in data:
    if ((isinstance(idx, float) or isinstance(idx, int))
            and idx > 5):
        new_tuple.append(idx)

new_tuple = tuple(new_tuple)
print("Новият кортеж е: ")
print(*new_tuple)