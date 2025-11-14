text = input("Въведете текст: ")
max_digit = 0
index = 0

for idx in text:
    if idx.isalpha():
        pass
    elif idx.isdigit():
        idx = int(idx)
        if idx > max_digit:
            max_digit = idx
            idx = str(idx)
            index = text.index(idx)
    else:
        pass

print(f"Най-голямо число от въведения текст е: {max_digit} ")
print(f"Индекса на най-голямото число от въведния текст е: {index} ")