import math
from os.path import split

#def type_of_triangle ():
#  a = input()
#  b = input()
#  c = input()
#    if a == b == c:
#       print("равностранен")
#    elif a == b != c:
#        print("равнобедрен")
#    else:
#       print("разностранен")

#type_of_triangle()

def type_of_triangle(a, b, c):
    if a == b == c:
        return "равностранен"
    elif a == b != c:
        return "равнобедрен"
    else:
       return "разностранен"

# a = input()
# b = input()
# c = input()

print(type_of_triangle(a=input(), b=input(), c=input()))