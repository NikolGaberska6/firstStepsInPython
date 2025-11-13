text = input("Въведете текст: ")

dictionary = {}
word = " "

for idx in text:
    index = text.index(idx)
    if idx is text:
     if index == len(text) + 1:
        word += idx
        dictionary[word] = len(word)
        break
    if idx != " ":
        word += idx
    else:
        dictionary[word] = len(word)
        word = " "


print(dictionary)