text = input("Въведете текст: ")
dictionary = {}
most_common_word = ""
max_meeting = 0
count = 0

words_of_text = text.split(" ")
for word in words_of_text:
    count = words_of_text.count(word)
    if count > max_meeting:
        max_meeting = count
        most_common_word = word
    dictionary[word] = count

print(dictionary)
if count != 1:
 print(f"Most common word: {most_common_word}")
else:
    print("There is no most common word!")