words = input("Въведете думи за листа: ")
my_list = list(map(str, words.split()))

first_letter = list(map(lambda x: x[0], my_list))
print(first_letter)