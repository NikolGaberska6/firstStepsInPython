user_words = input("Въведете думи с интервал: ")
my_list = list(map(str, user_words.split()))
dictionary = {}

for word in my_list:
    counter =  my_list.count(word)
    dictionary[word] = counter

print("Думите и техните срещания в твоя лист са: ")
for key, value in dictionary.items():
 print(key, ":", value)