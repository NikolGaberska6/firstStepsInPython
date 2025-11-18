word1 = input("Въведете първата дума: ")
word2 = input("Въведете първата дума: ")

word_lenght = (lambda x, y: len(x) + len(y))(word1, word2)

print(word_lenght)