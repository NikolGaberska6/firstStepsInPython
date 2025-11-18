words = input("Въведете думите, които искате да съдържа кортежа: ")
words_tuple = tuple(map(str, words.split()))
new_tuple = []
for word in words_tuple:
    lenght = len(word)
    new_tuple.append(lenght)

new_tuple = tuple(new_tuple)
print("Кортеж с дължината на думите е: ", end=" ")
print(*new_tuple)
