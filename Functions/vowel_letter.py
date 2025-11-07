def vowel_letter (word):
    num_vowel_letter = 0
    for letter in (word):
        if letter == "a" or letter == "e" or letter == "o" or letter == "u" or letter == "i":
            num_vowel_letter += 1
        else:
            continue

    return num_vowel_letter

print(vowel_letter(word=input().lower()))