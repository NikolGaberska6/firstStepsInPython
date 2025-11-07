def palindrome_text(text):
    new_text = ""

    for idx in reversed(text):
        new_text += idx

    if text == new_text:
        print(f"Your text is palindrome and it's reversed is: {text}")
    else:
        print("Your text is not palindrome! Please try again")


text = input()
palindrome_text(text)
