number = input("Въведете число: ")
num_of_zeros = 0

for idx in number:
    idx = int(idx)
    if idx == 0:
       num_of_zeros += 1
    else:
        pass

print(f"Броят на нулите е: {num_of_zeros}")