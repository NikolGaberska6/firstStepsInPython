is_reading = True

while is_reading:
    text = input()
    if text == "Stop":
        is_reading = False
    else:
        print(text)
