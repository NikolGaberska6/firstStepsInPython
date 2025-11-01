def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    # if we want to print specific arguments on a new line:
    # print(f"{kwargs.get('street')})
    for value in kwargs.values():
        print(value, end=" ")
    print()
    for key in kwargs.keys():
        print(key, end=" ")

shipping_label("Dr.", "Vasil", "Vasilev",
               street="123 Fake Str.",
               city="Detroid",
               state="MI",
               zip="54321") #you can remove and add arguments all the time