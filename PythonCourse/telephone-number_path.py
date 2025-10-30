num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for cast in num_pad:
    for num in cast:
        print(num, end=" ")
    print()

