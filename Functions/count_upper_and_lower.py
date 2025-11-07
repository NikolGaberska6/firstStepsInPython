def count(text):
    count_upper = 0
    count_lower = 0
    for char in text:
        if char.isupper():
            count_upper += 1
        if char.islower():
            count_lower += 1
        else:
            pass

    if count_upper > count_lower:
        print(f"Upper cases - {count_upper} - are more than lower cases in this input!")
    else:
        print(f"Lower cases - {count_lower} - are more than upper cases in this input")

text = input()
count(text)
