#default arguments = when the argument is ommited / moke you function more flexible

def net_price(list_price, discount=0, tax = 0.05): #discount = 0 и tax = 0.05 са default аргументи
    return list_price * (1 + discount * tax)

print(net_price(500))
print(net_price(500, 1))
print(net_price(500, 2, 0))