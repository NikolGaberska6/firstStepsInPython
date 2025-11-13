text = input("Въведете текст: ")

dictionary = {}

word = ""

for idx in text:
    if idx != " ":
        word += idx
    else:
        dictionary[word] = len(word)
        word = ""
        continue

dictionary[word] = len(word)
print(dictionary)