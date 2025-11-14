first_word = input("Въведете първата дума: ").lower()
second_word = input("Въведете втората дума: ").lower()

if sorted(first_word) == sorted(second_word):
    print("The words are anagram!")
else:
     print("The words are not anagram!")




# first_word = input("Въведете първата дума: ").lower()
# second_word = input("Въведете втората дума: ").lower()
#
# chars_first = []
# chars_second = []
# contains = 0
#
# for char1 in first_word:
#     chars_first.append(char1)
#
# for char2 in second_word:
#         chars_second.append(char2)
#
# for idx in chars_first:
#     index = chars_first.index(idx)
#     if idx in chars_second:
#         index2 = chars_second.index(idx)
#         if index == index2:
#             pass
#         else:
#             contains += 1
#
# if len(chars_first) == contains:
#     print("The words are anagram!")
# else:
#     print("The words are not anagram!")


first_word = input("Въведете първата дума: ").lower()
second_word = input("Въведете втората дума: ").lower()

if sorted(first_word) == sorted(second_word):
    print("The words are anagram!")
else:
     print("The words are not anagram!")






