def reversed_text (text):
    new_text = ""
    for char in reversed(text):
        new_text += char

    return new_text

print(reversed_text(input()).lower())