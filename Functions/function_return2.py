def get_b():
    return "b"
get_b()

def get_a():
    return "a"

def get_c():
    return "c"

result = f"{get_a()} {get_b()} {get_c()}"
print(result)
result2 = get_a() + get_b() + get_c()
print(result2)

def merge(x1, x2, x3): #argumenti
    return x1 + x2 + x3

a = get_a()
b = get_b()
c = get_c()
result3 = merge(x1=a, x2=b, x3=c)
print(result3)