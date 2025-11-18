students = [
    ("Ivan", [3, 4, 6]),
    ("Maria", [6, 6, 5]),
    ("Gosho", [2, 3, 4])
]

result = list(sorted(students, key=lambda x: sum(x[1]) / len(x[1])))
print("Оценките на учениците подредени са: ")
print("Имената на учениците подредени по успех са: ")
for idx in result:
    print(idx[1])
    print(idx[0])