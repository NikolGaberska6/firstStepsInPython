text = input("Въведете текст: ").lower()

dictionary = {}
count_words = 0
char = 0
count_chars = 0
count_digits = 0
count_special_symbols = 0

num_words = text.split(" ")
for word in num_words:
    count_words += 1
dictionary["num_words"] = count_words

num_chars = sorted(text)
for char in num_chars:
    if char == " ":
        pass
    elif char != " ":
        count_chars += 1
        if char.isdigit():
           count_digits += 1
        elif char.isalpha():
            pass
        else:
          count_special_symbols += 1

dictionary["num_chars"] = count_chars
dictionary["num_digits"] = count_digits
dictionary["num_special_symbols"] = count_special_symbols


print(dictionary)