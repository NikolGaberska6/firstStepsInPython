scores = (("Ivan", 50), ("Petya", 75), ("Maria", 60), ("Georgi", 90))


for name, score in scores:
    sorted_list = sorted(scores, key=lambda x : x[1], reverse=True)

sorted_scores = tuple(sorted_list)
print("Сортираните точки в низходящ ред са: ", end="" )
print(*sorted_scores)