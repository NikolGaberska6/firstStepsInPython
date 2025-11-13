text = input("Въведете текст: ")

word_by_word = text.split(" ")
num_words = len(word_by_word)
different_words = 0

print("Вашите отделни думи са: ")
for word in word_by_word:
    count = word_by_word.count(word)
    if count > 1:
        pass
    else:
        different_words += 1
    print(word)

print(f"Броят на вашите думи е: {num_words}")
print(f"Броят на различните думи в текста са: {different_words}")