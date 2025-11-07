def my_fruits(fruits):
    for fruit in reversed(fruits):
        new_list_of_fruits.append(fruit)

    for idx in new_list_of_fruits:
        print(f"My favourite fruit is: {idx}")

fruits = ["apple", "orange", "banana", "coconut"]
new_list_of_fruits = []
my_fruits(fruits)