text = input("Въведете текст: ").lower()
list = []

for idx in text:
    count = text.count(idx)
    if count > 1:
        if idx in list:
            pass
        else:
         list.append(idx)

print(list)