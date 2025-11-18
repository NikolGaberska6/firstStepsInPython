word = input("Въведете думата: ")

last_string = (lambda x: x[len(x)-1])(word)

print("Последния индекс е: ", end="")
print(last_string)