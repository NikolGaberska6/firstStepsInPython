# keyword arguments = helps with readability / order of arguments doesn't matter

def hello(greeting, title, first_name, last_name):
    print(f"{greeting} {title}{first_name} {last_name}")

hello("Hello", "Mr.", "Vasil", "Vasilev")
#Ако обаче разместим местата на аргументите, те ще се принтират в
# реда в който сме ги написали а няма да отговарят на индекса в дефиницията.
# Затова слагаме keywords

hello("Hello",title="Mr.", last_name="Vasilev", first_name="Vasil" ) # positional arguments FIRST