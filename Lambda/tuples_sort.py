pairs = [(1, 3), (4, 1), (2, 8), (9, 0)]

result = list(sorted(pairs, key=lambda x: x[1]))
print(result)