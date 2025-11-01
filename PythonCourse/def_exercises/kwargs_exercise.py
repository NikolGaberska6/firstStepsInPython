#kwargs type - dictionary - key, value

def print_address(**kwargs):
    for value in kwargs.values(): #itterait over the values
        print(value)
    for key in kwargs.keys(): #itterait over the keys
        print(key)
    for key, value in kwargs.items(): #itterait over both
        print(f"{key} : {value}")

print_address(street="123 Fake St.",
              apartment="100", #we can add more argument
              city="Detroid",
              state="MI",
              zip="54321")