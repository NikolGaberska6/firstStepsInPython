numbers = [1, 2, 3, 4, 4, 4, 5]
#first, second, third = numbers #items on the left side should be equal to the items in the list
first, second, *other = numbers #if we want only the first two items
print(first, second)
print(other)
#we unpack first and second item tha we pack again the *others

first, *other, last = numbers
print(first, last)
print(other) #print this IN LIST
print(*other) #print this OUT OF A LIST




#first = numbers[0]
#second = numbers[1]
#third = numbers[2]
