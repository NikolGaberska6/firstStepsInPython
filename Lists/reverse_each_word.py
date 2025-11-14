text = input("Въведете текст: ")

words_from_text = text.split(" ")
reversed_words = []

for word in words_from_text:
    reversed_word = word[::-1]
    reversed_words.append(reversed_word)

for reverse_word in reversed_words:
    print(reverse_word, end= " ")


