words = ["apple", "kiwi", "banana", "pear"]

sort_lengh = sorted(words, key=lambda x: len(x)) #сортира по дължината на думите във възходящ ред
second_sort = sorted(words, key=lambda x: len(x), reverse=True) #сортира по дължината на думите в низходящ ред
print(sort_lengh)
print(second_sort)