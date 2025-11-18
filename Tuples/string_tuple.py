mix = (1, "hi", 3.5, True, "apple", 9)
new_tuple =[]
for idx in mix:
    if isinstance(idx, str):
        new_tuple.append(idx)
    else:
        pass

new_tuple = tuple(new_tuple)
print("Новият кортеж, съдържащ само думи е: ", end=" ")
print(*new_tuple)